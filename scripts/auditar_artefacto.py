#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Control de calidad de un artefacto generado por la skill `artefacto-visual`.

Comprueba lo que un artefacto debe cumplir siempre y que revisarlo a ojo no
garantiza: que sea autocontenido, que no traiga codigo peligroso, que no deje
marcadores, que tenga sus dos temas, sus estilos de impresion y una alternativa
textual en cada grafico.

Uso:
    python3 scripts/auditar_artefacto.py ruta/al/artefacto.html
    python3 scripts/auditar_artefacto.py ruta.html --render   (ademas lo abre
        en Chrome sin ventana: consola, desbordamiento horizontal y PDF)

Salida: un informe por comprobacion y codigo 1 si alguna falla.
"""
import os
import re
import sys
import socket
import subprocess
import functools
import threading
import http.server
import socketserver

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
LIMITE_BYTES = 100 * 1024

fallos: list[str] = []
avisos: list[str] = []


def comprobar(condicion, titulo, detalle=""):
    print("  %-52s %s" % (titulo, "OK" if condicion else "FALLA"))
    if not condicion:
        fallos.append(titulo + (" — " + detalle if detalle else ""))


def avisar(condicion, titulo, detalle=""):
    if not condicion:
        print("  %-52s AVISO" % titulo)
        avisos.append(titulo + (" — " + detalle if detalle else ""))


# ----------------------------------------------------------------- analisis estatico
def auditar_texto(html, ruta):
    print("\nAutocontencion y seguridad")
    remotos = re.findall(r'(?:src|href)\s*=\s*["\']https?://[^"\']+', html)
    # Un enlace de texto en el pie es legitimo; lo que no vale es cargar recursos.
    recursos = [r for r in remotos if not re.match(r'href\s*=\s*["\']https?://[^"\']*$', r, re.I) or "<link" in html[:0]]
    comprobar(not re.search(r'<(?:script|link|img|iframe|source)[^>]+(?:src|href)\s*=\s*["\']https?://', html, re.I),
              "sin recursos remotos (script, link, img, iframe)",
              "; ".join(recursos[:2]))
    comprobar("@import" not in html, "sin @import en los estilos")
    comprobar(not re.search(r'\b(?:fetch|XMLHttpRequest|WebSocket)\s*\(', html), "sin llamadas de red")
    comprobar(not re.search(r'\b(?:eval|new Function|document\.write)\s*\(', html), "sin eval, new Function ni document.write")
    comprobar(not re.search(r'\b(?:alert|confirm|prompt)\s*\(', html), "sin dialogos bloqueantes del navegador")
    comprobar(not re.search(r'\.innerHTML\s*=', html), "sin innerHTML (se pinta con textContent)")
    avisar("localStorage" not in html and "sessionStorage" not in html,
           "sin almacenamiento del navegador", "falla bajo file:// en algunos navegadores")

    print("\nEstructura")
    comprobar(html.lstrip().lower().startswith("<!doctype html>"), "empieza por <!doctype html>")
    comprobar(re.search(r'<html[^>]+lang=', html, re.I) is not None, "el elemento html declara su idioma")
    comprobar(re.search(r'<meta[^>]+viewport', html, re.I) is not None, "tiene meta viewport")
    titulo = re.search(r'<title>(.*?)</title>', html, re.S | re.I)
    comprobar(titulo is not None and titulo.group(1).strip() != "", "tiene titulo de pestana",
              titulo.group(1).strip() if titulo else "no hay <title>")
    comprobar("DRAFT" in html, "lleva el aviso DRAFT visible")
    comprobar(re.search(r'<footer|class="pie"', html) is not None, "tiene pie de documento")

    print("\nDatos")
    marcadores = sorted(set(re.findall(r"\{\{[^}\n]{1,60}\}\}", html)))
    comprobar(not marcadores, "sin marcadores sin resolver", ", ".join(marcadores[:4]))

    print("\nTemas, impresion y accesibilidad")
    comprobar(re.search(r':root\s*\{[^}]*--', html) is not None, "declara sus tokens en :root")
    comprobar("prefers-color-scheme" in html, "tiene tema oscuro")
    comprobar("@media print" in html, "tiene estilos de impresion")
    comprobar("@page" in html, "fija tamano y margen de pagina")
    comprobar(re.search(r'\.acciones\s*\{[^}]*display\s*:\s*none', html) is not None,
              "los botones no salen impresos")
    svgs = re.findall(r'<svg\b[^>]*>', html)
    sin_alternativa = [s for s in svgs if 'role="img"' not in s or 'aria-label' not in s]
    comprobar(not sin_alternativa, "cada grafico tiene alternativa textual",
              "%d de %d sin role/aria-label" % (len(sin_alternativa), len(svgs)))
    campos = re.findall(r'<(?:input|select)\b[^>]*id="([^"]+)"', html)
    sin_etiqueta = [c for c in campos if ('for="%s"' % c) not in html]
    comprobar(not sin_etiqueta, "cada campo tiene su etiqueta", ", ".join(sin_etiqueta[:4]))
    avisar(not svgs or re.search(r'>0<', html) is not None,
           "los ejes parecen arrancar en cero", "no encuentro el 0 en las etiquetas del eje")

    print("\nTamano")
    tam = os.path.getsize(ruta)
    comprobar(tam <= LIMITE_BYTES, "por debajo de 100 KB", "%d bytes" % tam)
    print("  %-52s %.1f KB" % ("tamano del artefacto", tam / 1024))


# ----------------------------------------------------------------- render real
def auditar_render(ruta):
    if not os.path.exists(CHROME):
        avisos.append("Chrome no encontrado: no se pudo renderizar")
        return
    carpeta = os.path.dirname(os.path.abspath(ruta)) or "."
    nombre = os.path.basename(ruta)
    s = socket.socket(); s.bind(("127.0.0.1", 0)); puerto = s.getsockname()[1]; s.close()
    manejador = functools.partial(http.server.SimpleHTTPRequestHandler, directory=carpeta)
    servidor = socketserver.TCPServer(("127.0.0.1", puerto), manejador)
    threading.Thread(target=servidor.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:%d/%s" % (puerto, nombre)

    def chrome(args, entrada=base):
        return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=3000"] + args + [entrada],
                              capture_output=True, text=True, timeout=120)

    try:
        print("\nRenderizado")
        medida_html = os.path.join(carpeta, ".medida_%s" % nombre)
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
        sonda = ('<script>window.addEventListener("load",function(){document.title="MEDIDA "'
                 '+document.documentElement.scrollWidth+" "+document.documentElement.clientWidth;});</script>')
        with open(medida_html, "w", encoding="utf-8") as f:
            f.write(texto.replace("</body>", sonda + "</body>"))
        try:
            salida = chrome(["--window-size=520,900", "--dump-dom"],
                            "http://127.0.0.1:%d/%s" % (puerto, os.path.basename(medida_html))).stdout
            m = re.search(r"MEDIDA (\d+) (\d+)", salida)
            comprobar(m is not None and m.group(1) == m.group(2),
                      "sin desbordamiento horizontal a 520 px",
                      "scroll=%s client=%s" % (m.groups() if m else ("?", "?")))
        finally:
            os.remove(medida_html)

        consola = chrome(["--enable-logging=stderr", "--log-level=0", "--dump-dom"]).stderr
        errores = [l for l in consola.splitlines()
                   if re.search(r"CONSOLE|Uncaught|SyntaxError|TypeError", l)
                   and not re.search(r"task_policy|CVDisplayLink", l)]
        comprobar(not errores, "consola del navegador limpia", errores[0][:80] if errores else "")

        pdf = os.path.splitext(ruta)[0] + ".pdf"
        chrome(["--no-pdf-header-footer", "--print-to-pdf=" + pdf])
        comprobar(os.path.exists(pdf) and os.path.getsize(pdf) > 10000,
                  "se imprime a PDF", pdf)
    finally:
        servidor.shutdown()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); raise SystemExit(2)
    ruta = sys.argv[1]
    if not os.path.isfile(ruta):
        print("No existe el archivo: %s" % ruta); raise SystemExit(2)
    print("Auditando %s" % ruta)
    with open(ruta, encoding="utf-8") as f:
        html = f.read()
    auditar_texto(html, ruta)
    if "--render" in sys.argv:
        auditar_render(ruta)

    print("\n" + "=" * 60)
    for a in avisos:
        print("AVISO  " + a)
    if fallos:
        for f_ in fallos:
            print("FALLA  " + f_)
        print("\n%d comprobacion(es) fallidas" % len(fallos))
        raise SystemExit(1)
    print("Artefacto conforme" + (" (con %d aviso(s))" % len(avisos) if avisos else ""))
