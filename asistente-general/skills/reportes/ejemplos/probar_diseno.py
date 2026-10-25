#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba el diseno editable de los ejemplos en Google Chrome sin ventana.

Para cada ejemplo abre una copia con un script de prueba que llama a la API que
usa la app (`window.Reportes`): recorre los 21 temas en modo claro, oscuro y del
sistema y comprueba el fondo; pone y quita los colores del despacho; cambia cada
grafico por cada una de sus alternativas y comprueba que se dibuja; y al final
`restaurar()` debe dejarlo todo como estaba. Lo repite con el sistema en oscuro.
Tambien guarda el documento como lo guarda el visor (el DOM serializado, tras una
vista previa con otro tema, modo y marca) y comprueba que al reabrirlo no se
duplica nada de lo que anaden el motor, los modulos o la maqueta.
Despues imprime a PDF unos ejemplos con el modo oscuro fijado y comprueba que el
papel sale en blanco.

Uso:   python3 probar_diseno.py                 (todos los ejemplos)
       python3 probar_diseno.py panel_reclamacion_cantidad.html ...
"""
import glob, json, os, re, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

AQUI = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
NO_SON_REPORTES = {"galeria_temas.html", "galeria_maquetas.html", "galeria_catalogo.html"}  # llevan su propio selector o no tienen graficos

PRUEBA = r"""<script>
(function(){
"use strict";
var D = document, H = D.documentElement, R = window.Reportes, r = {fallos: [], titulos: {}, cambios: 0};
function fallo(t) { r.fallos.push(t); }
/* Luminancia de un color calculado: rgb(...) o color(srgb ...) (lo que devuelve color-mix). */
function lum(c) {
  var m = /rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)/.exec(c), v;
  if (m) v = [m[1] / 255, m[2] / 255, m[3] / 255];
  else if ((m = /color\(srgb ([\d.]+) ([\d.]+) ([\d.]+)/.exec(c))) v = [+m[1], +m[2], +m[3]];
  else return NaN;
  v = v.map(function (x) { return x <= 0.04045 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); });
  return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
}
var sonda = D.createElement("i"); sonda.style.color = "var(--acento)";
function acento() { return getComputedStyle(sonda).color; }
function fondo() { return lum(getComputedStyle(D.body).backgroundColor); }
function cuentas() {
  var c = {}, q = {generado: "[data-generado]", marca: '[data-generado="marca"]', estilos: "style", imagenes: "img", fuentes: "#fuentes-reporte li",
                   diapositivas: ".diapositiva", indice: "#indice-documento li", pie: ".pie p"};
  for (var k in q) c[k] = D.querySelectorAll(q[k]).length;
  return c;
}
function errores() { return [].map.call(D.querySelectorAll(".error-grafico"), function (n) { return n.textContent; }); }
function terminar() { sonda.remove(); var p = D.createElement("pre"); p.id = "prueba-diseno"; p.textContent = JSON.stringify(r); D.body.appendChild(p); }
/* Despues de la carga y de que el motor dibuje, como la app. */
window.addEventListener("load", function () { setTimeout(probar, 50); });
function probar() {
try {
  r.cuentas = cuentas();
  r.estado = R && R.estado();
  errores().forEach(function (e) { fallo("al cargar: " + e); });
  if (!D.querySelector('meta[name="reportes-diseno"]')) fallo("falta la etiqueta reportes-diseno");
  D.body.appendChild(sonda);
  if (!R || !R.catalogo || !(R.catalogo.temas || []).length) { fallo("falta el catalogo"); return terminar(); }
  var inicial = R.estado(), sistemaOscuro = matchMedia("(prefers-color-scheme:dark)").matches;
  r.sistemaOscuro = sistemaOscuro;
  if (R.catalogo.temas.length !== 21) fallo("el catalogo tiene " + R.catalogo.temas.length + " temas");
  /* Temas y modos: el fondo es oscuro solo si toca. */
  R.catalogo.temas.forEach(function (t) {
    ["claro", "oscuro", "sistema"].forEach(function (modo) {
      R.vistaPrevia({tema: t.id, modo: modo});
      var e = R.estado(), oscuro = t.siempre_oscuro || modo === "oscuro" || (modo === "sistema" && sistemaOscuro);
      if (e.tema !== t.id || e.modo !== modo) fallo("estado tras vistaPrevia " + t.id + "/" + modo + ": " + e.tema + "/" + e.modo);
      if ((fondo() < 0.2) !== oscuro) fallo("fondo de " + t.id + " en " + modo + ": luminancia " + fondo().toFixed(3));
    });
  });
  /* Colores del despacho: en claro, el acento tal cual; en oscuro, aclarado; con null, los del tema. */
  R.vistaPrevia({tema: "sobrio", modo: "claro", marca: null});
  var delTema = acento();
  R.vistaPrevia({marca: {acento: "#7a1f3d"}});
  if (acento() !== "rgb(122, 31, 61)") fallo("marca en claro: " + acento());
  if (!R.estado().marca || R.estado().marca.acento !== "#7a1f3d") fallo("estado sin la marca");
  R.vistaPrevia({modo: "oscuro"});
  if (!(lum(acento()) > lum("rgb(122, 31, 61)") * 2)) fallo("marca en oscuro sin aclarar: " + acento());
  R.vistaPrevia({tema: "dorado"});
  if (!(lum(acento()) > 0.1)) fallo("marca en un tema siempre oscuro sin aclarar: " + acento());
  R.vistaPrevia({tema: "sobrio", modo: "claro", marca: null});
  if (acento() !== delTema) fallo("marca: null no devuelve el acento del tema: " + acento());
  if (R.estado().marca !== null) fallo("estado con marca tras quitarla");
  /* Graficos: cada alternativa se dibuja sin error. */
  inicial.graficos.forEach(function (g) {
    r.titulos[g.id] = g.titulo;
    var alt = R.alternativas(g.id);
    if (!alt.length) return;
    var actuales = alt.filter(function (a) { return a.actual; });
    if (actuales.length !== 1 || actuales[0].tipo !== g.tipo) fallo("alternativas de " + g.id + " sin el tipo actual");
    alt.forEach(function (a) {
      if (a.actual || a.aviso === R.T.no_dibuja) return;
      R.actualizar(g.id, {tipo: a.tipo});
      r.cambios++;
      var fig = D.querySelector('[data-grafico="' + g.id + '"]');
      if (fig.querySelector(".error-grafico")) fallo(g.id + " como " + a.tipo + ": " + fig.textContent.slice(0, 160));
    });
  });
  /* restaurar() vuelve al estado de la carga. */
  R.restaurar();
  if (JSON.stringify(R.estado()) !== JSON.stringify(inicial)) fallo("restaurar no vuelve al estado inicial: " + JSON.stringify(R.estado()).slice(0, 300));
  errores().forEach(function (e) { fallo("tras restaurar: " + e); });
} catch (e) { fallo("excepcion: " + e.message); }
terminar();
}
})();
</script>
</body>"""


GUARDAR = r"""<script>
(function(){
var yo = document.currentScript;
window.addEventListener("load", function () { setTimeout(function () {
  yo.remove();
  Reportes.vistaPrevia({tema: "prensa", modo: "oscuro", marca: {acento: "#7a1f3d", pie: "Pie de prueba"}});
}, 50); });
})();
</script>
</body>"""


def chrome(html, archivo, oscuro=False):
    """DOM serializado de una copia del ejemplo, tras cargarla en Chrome sin ventana."""
    with tempfile.TemporaryDirectory(prefix="reportes-prueba-") as tmp:
        copia = os.path.join(AQUI, ".prueba-%s-%s" % (os.path.basename(tmp), archivo))  # junto al original, por si enlaza otros archivos
        open(copia, "w", encoding="utf-8").write(html)
        try:
            orden = [CHROME, "--headless=new", "--disable-gpu", "--user-data-dir=" + tmp, "--virtual-time-budget=6000", "--dump-dom"]
            if oscuro:
                orden.append("--force-dark-mode")
            return subprocess.run(orden + ["file://" + copia], capture_output=True, text=True, check=False, timeout=180).stdout
        except subprocess.TimeoutExpired:
            return ""
        finally:
            os.remove(copia)


def probar(archivo, oscuro, html=None):
    """Abre una copia del ejemplo con el script de prueba y devuelve su resultado."""
    html = html or open(os.path.join(AQUI, archivo), encoding="utf-8").read()
    salida = chrome(html.replace("</body>", PRUEBA, 1), archivo, oscuro)
    m = re.search(r'<pre id="prueba-diseno">(.*?)</pre>', salida, re.S)
    if not m:
        return {"fallos": ["la prueba no termino (sin resultado en el DOM)"]}
    return json.loads(m.group(1).replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&amp;", "&"))


def guardar_y_reabrir(archivo):
    """Guarda el ejemplo como el visor (DOM serializado tras una vista previa) y lo prueba de nuevo."""
    html = open(os.path.join(AQUI, archivo), encoding="utf-8").read()
    guardado = "<!doctype html>\n" + chrome(html.replace("</body>", GUARDAR, 1), archivo)
    return probar(archivo, False, guardado)


def brillo_papel(archivo, tema=None, modo=None, sistema_oscuro=True):
    """Imprime el ejemplo (con otro tema y modo, si se dan) y mide el brillo medio de la primera pagina."""
    html = open(os.path.join(AQUI, archivo), encoding="utf-8").read()
    tema = tema or re.search(r'data-tema="(\w+)"', html).group(1)
    html = re.sub(r' data-tema="\w+"', ' data-tema="%s"%s' % (tema, ' data-modo="%s"' % modo if modo else ""), html, 1)
    with tempfile.TemporaryDirectory(prefix="reportes-papel-") as tmp:
        copia, pdf, png = os.path.join(AQUI, ".papel-%s-%s-%s-%s" % (tema, modo, sistema_oscuro, archivo)), os.path.join(tmp, "p.pdf"), os.path.join(tmp, "p.png")
        open(copia, "w", encoding="utf-8").write(html)
        try:
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--user-data-dir=" + tmp, "--virtual-time-budget=4000", "--no-pdf-header-footer",
                            "--print-to-pdf=" + pdf, "file://" + copia] + (["--force-dark-mode"] if sistema_oscuro else []), capture_output=True, check=False, timeout=120)
        finally:
            os.remove(copia)
        subprocess.run(["sips", "-s", "format", "png", pdf, "--out", png], capture_output=True, check=False)
        from PIL import Image, ImageStat
        return ImageStat.Stat(Image.open(png).convert("L")).mean[0]


if __name__ == "__main__":
    if not os.path.exists(CHROME):
        sys.exit("Chrome no encontrado: " + CHROME)
    archivos = sys.argv[1:] or sorted(os.path.basename(a) for a in glob.glob(os.path.join(AQUI, "*.html")) if os.path.basename(a) not in NO_SON_REPORTES)
    trabajos = [(a, o) for a in archivos for o in (False, True)]
    with ThreadPoolExecutor(6) as hilos:
        resultados = list(hilos.map(lambda t: probar(*t), trabajos))
    mal = False
    for (archivo, oscuro), r in zip(trabajos, resultados):
        print("  %-38s %-14s %s" % (archivo, "sistema oscuro" if oscuro else "sistema claro",
                                    "%d cambios de grafico, sin fallos" % r.get("cambios", 0) if not r["fallos"] else "%d fallos" % len(r["fallos"])))
        for f in r["fallos"]:
            print("      " + f[:240])
        if oscuro and r.get("sistemaOscuro") is False:
            print("      AVISO: --force-dark-mode no puso el sistema en oscuro")
        mal = mal or bool(r["fallos"])
    print("\nGuardado como el visor y reabierto (nada se duplica; tema y modo, los de la vista previa):")
    with ThreadPoolExecutor(6) as hilos:
        reabiertos = list(hilos.map(guardar_y_reabrir, archivos))
    for archivo, antes, despues in zip(archivos, [r for (a, o), r in zip(trabajos, resultados) if not o], reabiertos):
        fallos = list(despues["fallos"])
        if despues.get("cuentas") != antes.get("cuentas"):
            fallos.append("al cargar %s, al reabrir %s" % (antes.get("cuentas"), despues.get("cuentas")))
        e = despues.get("estado") or {}
        if (e.get("tema"), e.get("modo")) != ("prensa", "oscuro"):
            fallos.append("tema y modo al reabrir: %s/%s" % (e.get("tema"), e.get("modo")))
        print("  %-38s %s" % (archivo, "sin fallos" if not fallos else "%d fallos" % len(fallos)))
        for f in fallos:
            print("      " + f[:300])
        mal = mal or bool(fallos)
    print("\nTitulos que ve la app (estado().graficos[].titulo):")
    for (archivo, oscuro), r in zip(trabajos, resultados):
        if not oscuro and r.get("titulos"):
            print("  %s: %s" % (archivo, "; ".join("%s = %s" % kv for kv in r["titulos"].items())))
    print("\nPapel: brillo medio de la primera pagina (255 = blanco); ni el modo fijado ni el del sistema deben cambiarlo:")
    papel = "panel_reclamacion_cantidad.html" if "panel_reclamacion_cantidad.html" in archivos else archivos[0]
    for tema in (None, "nocturno", "lavanda"):
        con = lambda **k: brillo_papel(papel, tema, **k)
        claro, sistema_oscuro, fijado_oscuro, fijado_claro = con(sistema_oscuro=False), con(), con(modo="oscuro", sistema_oscuro=False), con(modo="claro")
        ok = max(claro, sistema_oscuro, fijado_oscuro, fijado_claro) - min(claro, sistema_oscuro, fijado_oscuro, fijado_claro) < 2
        mal = mal or not ok
        print("  %-36s %-9s sistema claro %5.1f, oscuro %5.1f; data-modo oscuro %5.1f, claro %5.1f  %s" % (papel, tema or "su tema", claro, sistema_oscuro, fijado_oscuro, fijado_claro, "igual" if ok else "DISTINTO"))
    if mal:
        print("\nFALLO")
        sys.exit(1)
    print("\nListo.")
