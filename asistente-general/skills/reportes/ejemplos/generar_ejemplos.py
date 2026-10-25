#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera los artefactos de ejemplo de la skill `reportes`.

Compone cada ejemplo como lo hara el modelo: copia integra de la base
(`../assets/template-base-reportes.md`), la maqueta del tipo de entregable
(leida de `../references/maquetas-reportes.md`, de modo que referencia y
ejemplos no pueden divergir) y un bloque de datos en JSON. Los graficos los
dibuja el motor de la base en el navegador.

Despues abre cada ejemplo en Google Chrome sin ventana, falla si la consola
registra algun error y lo imprime a PDF con el mismo motor que usara el
usuario.

Uso:   python3 generar_ejemplos.py            (HTML, comprobacion y PDF)
       python3 generar_ejemplos.py --sin-pdf  (solo HTML y comprobacion)
"""
import json, os, re, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

AQUI = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(AQUI, "..")
BASE = os.path.join(SKILL, "assets", "template-base-reportes.md")
MAQUETAS = os.path.join(SKILL, "references", "maquetas-reportes.md")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DATOS_VACIOS = re.compile(r'(<script type="application/json" id="datos-reporte">\n).*?(\n</script>)', re.S)

# --------------------------------------------------------------------------- composicion
def _leer_maquetas():
    """{(maqueta, parte): texto} de los bloques de la referencia, mas {maqueta: ancho}."""
    texto = open(MAQUETAS, encoding="utf-8").read()
    piezas = {(m, p): c for m, p, c in re.findall(r"```\w+ maqueta=(\w+) parte=(\w+)\n(.*?)\n```", texto, re.S)}
    anchos = dict(re.findall(r"\(`(\w+)`\)\n\n\*\*Ancho:\*\* `(\w+)`", texto))
    return piezas, anchos
PIEZAS, ANCHOS = _leer_maquetas()
MODULOS = dict(re.findall(r"```js modulo=(\w+)\n(.*?)\n```", open(os.path.join(SKILL, "references", "modulos-motor.md"), encoding="utf-8").read(), re.S))
TEMAS = dict(re.findall(r"```css tema=(\w+)\n(.*?)\n```", open(os.path.join(SKILL, "references", "temas-visuales.md"), encoding="utf-8").read(), re.S))
BASE_HTML = open(BASE, encoding="utf-8").read()

def componer(destino, textos, datos, maqueta=None, tema="moderno", ficha=None, contenido=None, ancho=None, modulos=()):
    """Compone un ejemplo como lo hara el modelo: base, partes de la maqueta y datos."""
    parte = lambda nombre: PIEZAS.get((maqueta, nombre), "")
    html = BASE_HTML.replace('data-tema="moderno"', 'data-tema="%s"' % tema)
    html = html.replace("{{ANCHO}}", ancho or ANCHOS[maqueta])
    html = html.replace("{{FICHA}}", ficha or parte("ficha")).replace("{{CONTENIDO}}", contenido or parte("contenido"))
    html = html.replace("{{ESTILOS_MAQUETA}}", parte("estilos")).replace("{{ACCIONES}}", parte("acciones"))
    if tema not in TEMAS and tema not in ("moderno", "sobrio"):
        raise SystemExit("Tema desconocido en %s: %s (no esta en temas-visuales.md)" % (destino, tema))
    html = html.replace("{{ESTILOS_TEMA}}", TEMAS.get(tema, ""))  # moderno y sobrio van en la base; los demas, en temas-visuales.md
    html = DATOS_VACIOS.sub(lambda m: m.group(1) + json.dumps(datos, ensure_ascii=False, indent=1) + m.group(2), html)
    for modulo in modulos:  # los modulos van despues del motor y antes del script de la maqueta
        html = html.replace("</body>", MODULOS[modulo] + "\n</body>")
    if parte("script"):
        html = html.replace("</body>", parte("script") + "\n</body>")
    textos = dict({"TITULO_CORTO": textos.get("TITULO_DOCUMENTO", "")}, **textos)
    for clave, valor in textos.items():
        html = html.replace("{{%s}}" % clave, valor)
    pendientes = sorted(set(re.findall(r"\{\{(\w+)\}\}", html)) - {"LETRADO_RESPONSABLE", "clave"})
    open(os.path.join(AQUI, destino), "w", encoding="utf-8").write(html)
    print("  %-38s %6d bytes   pendientes: %s" % (destino, len(html.encode()), ", ".join(pendientes) or "ninguno"))
    return destino, not pendientes

# --------------------------------------------------------------------------- datos del caso
FUENTE_CLIENTE = {"cliente": {"nombre": "Mayor de clientes y facturas aportados por el cliente", "consulta": "2026-09-18"}}
FACTURAS = [("Factura 2025/118", 18400), ("Factura 2025/131", 11250), ("Factura 2025/147", 7930), ("Resto (4 facturas)", 4600.5)]
ELEMENTOS_FACTURAS = [{"rotulo": r, "valor": v} for r, v in FACTURAS]
PRINCIPAL, INTERESES, COSTAS = 42180.50, 1947.32, 3100.00
COMUN = {"PIE_AVISO_LEGAL": "Documento de trabajo. No sustituye al asesoramiento de un profesional colegiado ni a la liquidacion judicial de intereses."}

def datos_panel():
    datos = {
      "idioma": "es-ES", "moneda": "EUR", "fuentes": FUENTE_CLIENTE,
      "cifras": {
        "indicador_1": {"de": "evolucion", "calculo": "ultimo", "serie": 0, "unidad": "eur"},
        "indicador_2": {"de": "descomposicion", "calculo": "suma", "unidad": "eur"},
        "indicador_4": {"de": "evolucion", "calculo": "ultimo", "serie": 1, "unidad": "eur"},
        "peso_tres": {"de": "comparativa", "calculo": "porcentaje", "elemento": "Factura 2025/118", "unidad": "pct"},
      },
      "graficos": {
        "tendencia": {"tipo": "chispa", "valores": [12400, 21800, 28900, 36200, 42180.5], "etiquetas": ["Enero", "Marzo", "Mayo", "Julio", "Septiembre"],
                      "resumen": "Principal acumulado de enero a septiembre: al alza", "fuente": "cliente"},
        "comparativa": {"tipo": "barras", "unidad": "eur", "fuente": "cliente",
                        "elementos": ELEMENTOS_FACTURAS},
        "reparto": {"tipo": "anillo", "unidad": "pct", "fuente": "cliente",
                    "porciones": [{"rotulo": "Hasta 90 dias", "valor": 26}, {"rotulo": "De 91 a 180 dias", "valor": 38}, {"rotulo": "Mas de 180 dias", "valor": 36}],
                    "centro": {"cifra": "36 %", "rotulo": "mas de 180 dias"},
                    "resumen": "Reparto del principal por antiguedad: 26, 38 y 36 por ciento"},
        "evolucion": {"tipo": "linea", "unidad": "eur", "fuente": "cliente",
                      "etiquetas": ["Enero", "Marzo", "Mayo", "Julio", "Septiembre"],
                      "series": [{"nombre": "Principal acumulado", "valores": [12400, 21800, 28900, 36200, 42180.5]},
                                 {"nombre": "Importe cobrado", "valores": [0, 2100, 2100, 5600, 5600]}],
                      "umbral": {"desde": 0, "hasta": 15000, "rotulo": "Umbral de riesgo asumido (15.000 EUR)"},
                      "anotaciones": [{"indice": 2, "texto": "Reconocimiento de deuda"}], "destacar": ["ultimo"],
                      "resumen": "El principal acumulado pasa de 12.400 euros en enero a 42.180 en septiembre, mientras lo cobrado se detiene en 5.600 euros desde julio"},
        "descomposicion": {"tipo": "cascada", "unidad": "eur", "fuente": "cliente",
                           "pasos": [{"rotulo": "Principal", "valor": PRINCIPAL}, {"rotulo": "Intereses", "valor": INTERESES}, {"rotulo": "Costas est.", "valor": COSTAS}],
                           "total": {"rotulo": "Total"}, "resumen": "Principal, intereses y costas estimadas suman el total reclamable"},
        "medidor": {"tipo": "medidor", "valor": 7, "maximo": 10, "unidad": "dias", "cifra": "70 %", "rotulo": "del plazo de diez dias consumido",
                    "resumen": "Plazo del requerimiento consumido al 70 por ciento: siete dias de diez", "fuente": "cliente"},
      }}
    textos = dict(COMUN, **{
      "TITULO_DOCUMENTO": "La deuda se concentra en tres facturas de 2025",
      "ETIQUETA_SUPERIOR": "Reclamacion de cantidad | Expediente 2026/0417",
      "ENTRADILLA": "Situacion de la deuda de Construcciones Delta, S.L. a 24 de septiembre de 2026. La factura mas antigua supone ella sola el <span data-cifra=\"peso_tres\"></span> del principal y supera ya los 300 dias de demora.",
      "PERIODO": "enero a septiembre de 2026", "FECHA_ACTUALIZACION": "24 de septiembre de 2026",
      "INDICADOR_1_ROTULO": "Principal reclamado", "INDICADOR_1_DETALLE": "Siete facturas vencidas e impagadas",
      "INDICADOR_2_ROTULO": "Total reclamable", "INDICADOR_2_DETALLE": "Principal, intereses y costas estimadas",
      "INDICADOR_3_ROTULO": "Demora media", "INDICADOR_3_CIFRA": "214 dias", "INDICADOR_3_DETALLE": "Ponderada por importe de cada factura",
      "INDICADOR_4_ROTULO": "Importe cobrado", "INDICADOR_4_DETALLE": "Dos pagos parciales a cuenta",
      "TITULO_COMPARATIVA": "Tres facturas concentran la deuda", "SUBTITULO_COMPARATIVA": "Principal pendiente por documento, en euros",
      "TITULO_REPARTO": "Mas de un tercio supera los 180 dias", "SUBTITULO_REPARTO": "Reparto del principal por antiguedad de la deuda",
      "TITULO_EVOLUCION": "La deuda crece mientras el cobro se estanca", "SUBTITULO_EVOLUCION": "Principal acumulado frente a importe cobrado, en euros",
      "TITULO_DESCOMPOSICION": "Del principal al total reclamable", "SUBTITULO_DESCOMPOSICION": "Descomposicion de la cuantia de la demanda, en euros",
      "TITULO_MEDIDOR": "El plazo del requerimiento vence en tres dias", "SUBTITULO_MEDIDOR": "Consumo del plazo concedido en el burofax de 17/09/2026",
      "TITULO_NOTA_MEDIDOR": "Siguiente actuacion",
      "NOTA_MEDIDOR": "Agotado el plazo sin pago, procede presentar la peticion inicial de monitorio con el principal y los intereses devengados hasta la fecha de presentacion.",
      "TITULO_TABLA": "Detalle de las facturas mas antiguas", "SUBTITULO_TABLA": "Ordenadas de mayor a menor antiguedad",
      "COLUMNA_1": "Documento", "COLUMNA_2": "Vencimiento", "COLUMNA_3": "Principal", "COLUMNA_4": "Dias", "COLUMNA_5": "Situacion",
      "FILA_1_C1": "Factura 2025/118", "FILA_1_C2": "15/11/2025", "FILA_1_C3": "18.400,00", "FILA_1_C4": "313", "FILA_1_C5": "Requerida",
      "FILA_2_C1": "Factura 2025/131", "FILA_2_C2": "20/01/2026", "FILA_2_C3": "11.250,00", "FILA_2_C4": "247", "FILA_2_C5": "Requerida",
      "TOTAL_ROTULO": "Total de las dos mas antiguas", "TOTAL_C3": "29.650,00",
    })
    return textos, datos

def panel():
    textos, datos = datos_panel()
    return componer("panel_reclamacion_cantidad.html", textos, datos, "panel_datos")

def informe():
    datos = {"idioma": "es-ES", "moneda": "EUR", "fuentes": FUENTE_CLIENTE, "cifras": {},
             "graficos": {"plazos": {"tipo": "plazos", "hoy": "2026-09-24", "fuente": "cliente",
                                     "plazos": [{"rotulo": "Plazo del burofax", "inicio": "2026-09-17", "fin": "2026-09-27"},
                                                {"rotulo": "Preparar el monitorio", "inicio": "2026-09-28", "fin": "2026-10-09"},
                                                {"rotulo": "Plazo de pago u oposicion", "inicio": "2026-10-20", "fin": "2026-11-10"}],
                                     "resumen": "El plazo del burofax vence el 27 de septiembre; despues se prepara el monitorio y corren veinte dias de pago u oposicion"}}}
    textos = dict(COMUN, **{
      "TITULO_DOCUMENTO": "El monitorio es la via mas rapida y economica",
      "ETIQUETA_SUPERIOR": "Informe de viabilidad | Expediente 2026/0417",
      "ENTRADILLA": "Analisis de las vias de reclamacion frente a Construcciones Delta, S.L. por un principal de 42.180,50 euros, con el detalle de plazos, costes y riesgos de cada alternativa.",
      "REFERENCIA_EXPEDIENTE": "2026/0417", "FECHA_EMISION": "24 de septiembre de 2026",
      "DESTINATARIO": "Suministros Ibericos del Norte, S.L.", "AUTOR": "Departamento de procesal civil",
      "INDICADOR_1_ROTULO": "Principal reclamable", "INDICADOR_1_CIFRA": "42.180,50 €", "INDICADOR_1_DETALLE": "Mas 1.947,32 euros de intereses",
      "INDICADOR_2_ROTULO": "Plazo estimado", "INDICADOR_2_CIFRA": "2 a 4 meses", "INDICADOR_2_DETALLE": "Si no media oposicion del deudor",
      "INDICADOR_3_ROTULO": "Prescripcion mas proxima", "INDICADOR_3_CIFRA": "15/11/2030", "INDICADOR_3_DETALLE": "Factura 2025/118, accion personal",
      "TITULO_SECCION_1": "Antecedentes de hecho", "SUBTITULO_SECCION_1": "Hechos acreditados con la documentacion aportada",
      "CONTENIDO_SECCION_1": "Entre noviembre de 2025 y marzo de 2026 se emitieron siete facturas por suministro de material, todas ellas vencidas e impagadas. El deudor reconocio la deuda por correo electronico el 4 de mayo de 2026 y realizo dos pagos parciales a cuenta por importe conjunto de 5.600 euros, sin que desde julio se haya producido nuevo abono.",
      "TITULO_NOTA": "Reconocimiento de deuda",
      "CONTENIDO_NOTA": "El correo de 4 de mayo de 2026 interrumpe la prescripcion e integra el principio de prueba por escrito que sostiene la peticion inicial de monitorio.",
      "TITULO_SECCION_2": "Comparativa de vias de reclamacion", "SUBTITULO_SECCION_2": "Coste, plazo y probabilidad de cobro efectivo",
      "CONTENIDO_SECCION_2": "Se valoran las alternativas atendiendo al coste de iniciarlas, al plazo previsible de resolucion y a la probabilidad de cobro efectivo una vez obtenido el titulo.",
      "TITULO_TABLA": "Vias disponibles y su valoracion",
      "COLUMNA_1": "Via", "COLUMNA_2": "Requisitos", "COLUMNA_3": "Plazo", "COLUMNA_4": "Viabilidad",
      "FILA_1_C1": "Monitorio", "FILA_1_C2": "Documento que acredite la deuda", "FILA_1_C3": "2 a 4 meses", "FILA_1_C4": "Alta",
      "FILA_2_C1": "Juicio ordinario", "FILA_2_C2": "Abogado y procurador", "FILA_2_C3": "12 a 18 meses", "FILA_2_C4": "Media",
      "TITULO_SECCION_3": "Plazos y cronologia", "SUBTITULO_SECCION_3": "Lo que corre ahora y los hitos acreditados",
      "CONTENIDO_SECCION_3": "El calendario muestra los plazos en curso sobre una misma escala; la cronologia fija las fechas relevantes a efectos de prescripcion.",
      "HITO_1_FECHA": "4 de mayo de 2026", "HITO_1_TITULO": "Reconocimiento de deuda",
      "HITO_1_DETALLE": "Correo del administrador del deudor aceptando el saldo y proponiendo calendario de pagos.",
      "HITO_2_FECHA": "17 de septiembre de 2026", "HITO_2_TITULO": "Burofax de requerimiento",
      "HITO_2_DETALLE": "Requerimiento fehaciente con acuse de recibo y plazo de diez dias para el pago.",
      "TITULO_SECCION_4": "Conclusion y hoja de ruta", "SUBTITULO_SECCION_4": "Actuaciones recomendadas y su orden",
      "CONTENIDO_SECCION_4": "Agotado el plazo del requerimiento sin pago, se recomienda acudir al procedimiento monitorio, que no exige abogado ni procurador para la peticion inicial y permite obtener titulo ejecutivo en pocos meses si el deudor no se opone.",
      "PASO_1": "Esperar al vencimiento del plazo del burofax y documentar la ausencia de pago.",
      "PASO_2": "Presentar peticion inicial de monitorio por el principal y los intereses devengados hasta la fecha de presentacion.",
      "TITULO_ADVERTENCIA": "Riesgo de oposicion",
      "CONTENIDO_ADVERTENCIA": "Si el deudor se opone en plazo, el asunto se transforma en el juicio declarativo que corresponda por la cuantia, con la consiguiente necesidad de abogado y procurador y un plazo sensiblemente mayor.",
      "FIRMA_1": "Preparado por: Departamento de procesal civil", "FIRMA_2": "Revisado por: {{LETRADO_RESPONSABLE}}",
    })
    return componer("informe_viabilidad_monitorio.html", textos, datos, "informe_visual", tema="sobrio")

def herramienta():
    calculo = """var base = d.campo1;
    var tipo = d.campo2 / 100;
    var dias = d.campo3;
    var recargo = d.campo4 === "comercial" ? base * 0.4 / 100 * dias / 365 : 0;
    var intereses = base * tipo * dias / 365;
    var total = base + intereses + recargo;
    return {
      resultado1: total,
      resultado2: intereses + recargo,
      resultado3: dias,
      medidor: total ? (intereses + recargo) * 100 / total : 0,
      desglose: [
        { concepto: "Principal reclamado", importe: base, detalle: "--" },
        { concepto: "Intereses al tipo aplicado", importe: intereses, detalle: dias + " dias" },
        { concepto: "Recargo por morosidad comercial", importe: recargo, detalle: dias + " dias" }
      ]
    };"""
    datos = {"idioma": "es-ES", "moneda": "EUR", "fuentes": {"cliente": {"nombre": "Importes aportados por el cliente", "consulta": "2026-09-18"}}, "cifras": {},
             "graficos": {"resultado": {"tipo": "medidor", "valor": 0, "maximo": 100, "tramos": [5, 15], "rotulo": "intereses sobre el total", "tabla": False, "fuente": "cliente",
                                        "resumen": "Peso de los intereses y el recargo sobre el total a reclamar"}}}
    textos = dict(COMUN, **{
      "TITULO_DOCUMENTO": "Simulador de intereses de demora",
      "ETIQUETA_SUPERIOR": "Herramienta de apoyo | Expediente 2026/0417",
      "ENTRADILLA": "Calcule el importe total a reclamar ajustando el principal, el tipo aplicable y los dias transcurridos desde el vencimiento. El desglose se actualiza al instante.",
      "REFERENCIA_EXPEDIENTE": "2026/0417",
      "TITULO_PANEL_ENTRADA": "Parametros de calculo", "SUBTITULO_PANEL_ENTRADA": "Modifique cualquier campo para recalcular",
      "CAMPO_1_ROTULO": "Principal reclamado (EUR)", "CAMPO_1_VALOR_INICIAL": "42180.50", "CAMPO_1_AYUDA": "Suma de las facturas vencidas e impagadas.",
      "CAMPO_2_ROTULO": "Tipo de interes anual (%)", "CAMPO_2_VALOR_INICIAL": "3.25", "CAMPO_2_AYUDA": "Tipo pactado o, en su defecto, el interes legal del dinero vigente.",
      "CAMPO_3_ROTULO": "Dias transcurridos desde el vencimiento", "CAMPO_3_VALOR_INICIAL": "214", "CAMPO_3_AYUDA": "Demora media ponderada por importe de cada factura.",
      "CAMPO_4_ROTULO": "Naturaleza de la operacion", "CAMPO_4_AYUDA": "La operacion comercial entre empresas admite recargo adicional por morosidad.",
      "OPCION_1_VALOR": "civil", "OPCION_1_ROTULO": "Operacion civil ordinaria",
      "OPCION_2_VALOR": "comercial", "OPCION_2_ROTULO": "Operacion comercial entre empresas",
      "TITULO_VERIFICACION": "Documentacion previa", "SUBTITULO_VERIFICACION": "Verifique lo que ya obra en el expediente",
      "PUNTO_1": "Facturas emitidas y albaranes firmados", "PUNTO_1_DETALLE": "Acreditan la entrega y el importe reclamado.",
      "PUNTO_2": "Reconocimiento de deuda por escrito", "PUNTO_2_DETALLE": "Correo de 4 de mayo de 2026.",
      "PUNTO_3": "Burofax de requerimiento con acuse", "PUNTO_3_DETALLE": "Remitido el 17 de septiembre de 2026.",
      "TITULO_PANEL_RESULTADO": "Resultado estimado", "SUBTITULO_PANEL_RESULTADO": "Calculo orientativo con los parametros introducidos",
      "RESULTADO_1_ROTULO": "Total a reclamar", "RESULTADO_2_ROTULO": "Intereses y recargo", "RESULTADO_3_ROTULO": "Dias computados",
      "TITULO_DESGLOSE": "Desglose del importe", "DESGLOSE_COLUMNA_1": "Concepto", "DESGLOSE_COLUMNA_2": "Importe", "DESGLOSE_COLUMNA_3": "Periodo",
      "DESGLOSE_TOTAL_ROTULO": "Total", "BLOQUE_CALCULO": calculo,
      "TITULO_SUPUESTOS": "Supuestos del calculo",
      "CONTENIDO_SUPUESTOS": "Interes simple calculado sobre el principal, con base de 365 dias por ano. El recargo por morosidad comercial se aplica al 0,4 por ciento anual adicional unicamente cuando se selecciona operacion entre empresas.",
      "TITULO_ADVERTENCIA": "Caracter orientativo",
      "CONTENIDO_ADVERTENCIA": "El importe definitivo depende del tipo efectivamente aplicable a cada factura y de la fecha real de presentacion de la demanda. La liquidacion definitiva corresponde al letrado director del asunto.",
    })
    return componer("simulador_intereses_demora.html", textos, datos, "herramienta_interactiva")

def presentacion():
    datos = {
      "idioma": "es-ES", "moneda": "EUR", "fuentes": FUENTE_CLIENTE,
      "cifras": {"total": {"de": "cuantia", "calculo": "suma", "unidad": "eur"}},
      "graficos": {
        "cuantia": {"tipo": "cascada", "unidad": "eur", "fuente": "cliente",
                    "pasos": [{"rotulo": "Principal", "valor": PRINCIPAL}, {"rotulo": "Intereses", "valor": INTERESES}, {"rotulo": "Costas est.", "valor": COSTAS}],
                    "total": {"rotulo": "Total"}, "resumen": "Principal, intereses y costas estimadas suman el total reclamable"},
        "facturas": {"tipo": "barras", "unidad": "eur", "fuente": "cliente", "elementos": ELEMENTOS_FACTURAS,
                     "resumen": "Tres facturas concentran la deuda"},
        "flujo": dict(FLUJO_MONITORIO, fuente="cliente", resumen="Si no paga en el plazo del burofax, se presenta el monitorio"),
      },
      "diapositivas": [
        {"maqueta": "portada", "antetitulo": "Expediente 2026/0417", "titulo": "Como recuperar los 42.180 euros de Construcciones Delta",
         "subtitulo": "Situacion de la deuda, via recomendada y proximos pasos", "fecha": "24 de septiembre de 2026", "autor": "Departamento de procesal civil",
         "notas": "Agradecer la reunion. Objetivo: decidir hoy si presentamos el monitorio."},
        {"maqueta": "agenda", "titulo": "Que vamos a decidir hoy", "puntos": ["Cuanto se puede reclamar", "Que via es la mas rapida", "Que riesgos hay", "Que hacemos esta semana"]},
        {"maqueta": "cifra", "dato": "total", "titulo": "Es la cuantia total que se puede reclamar hoy",
         "texto": "Principal de siete facturas, intereses al tipo legal y una estimacion de costas.", "notas": "La cifra sale de la descomposicion de la siguiente diapositiva."},
        {"maqueta": "grafico", "titulo": "El principal explica casi toda la cuantia", "grafico": "cuantia",
         "conclusion": "Los intereses y las costas suman menos del 11 por ciento: el monitorio no pierde valor por no reclamarlos aparte."},
        {"maqueta": "puntos", "titulo": "Tres facturas concentran la deuda", "grafico": "facturas",
         "puntos": ["La 2025/118 es la mas antigua y la mayor", "El deudor reconocio la deuda por escrito", "No hay pagos desde julio"]},
        {"maqueta": "separador", "numero": "02", "titulo": "La via recomendada", "texto": "Monitorio, con el burofax ya enviado"},
        {"maqueta": "grafico", "titulo": "Si no paga en diez dias, presentamos el monitorio", "grafico": "flujo"},
        {"maqueta": "comparativa", "titulo": "El monitorio es mas rapido y mas barato", "opciones": [
          {"nombre": "Monitorio", "puntos": ["Sin abogado ni procurador al inicio", "2 a 4 meses si no hay oposicion"], "veredicto": "Recomendado", "estado": "ok"},
          {"nombre": "Juicio ordinario", "puntos": ["Abogado y procurador", "12 a 18 meses"], "veredicto": "Solo si hay oposicion", "estado": "atencion"},
          {"nombre": "Acuerdo", "puntos": ["Depende del deudor", "Sin garantia de cobro"], "veredicto": "Incierto", "estado": "riesgo"}]},
        {"maqueta": "cronologia", "titulo": "Los hechos que sostienen la reclamacion", "hitos": [
          {"fecha": "15 nov 2025", "titulo": "Vence la primera factura", "texto": "18.400 euros impagados"},
          {"fecha": "4 may 2026", "titulo": "Reconocimiento de deuda", "texto": "Correo del administrador"},
          {"fecha": "17 sep 2026", "titulo": "Burofax", "texto": "Diez dias para pagar"},
          {"fecha": "27 sep 2026", "titulo": "Vence el plazo", "texto": "Sin pago, monitorio"}]},
        {"maqueta": "cita", "cita": "Reconocemos el saldo pendiente y proponemos un calendario de pagos a partir de junio.",
         "autor": "Correo del administrador de Construcciones Delta, 4 de mayo de 2026"},
        {"maqueta": "proximos_pasos", "titulo": "Lo que hacemos esta semana", "pasos": [
          {"texto": "Confirmar que no ha habido pago", "responsable": "Cliente", "fecha": "28/09/2026"},
          {"texto": "Presentar la peticion de monitorio", "responsable": "Despacho", "fecha": "02/10/2026"},
          {"texto": "Informar del requerimiento judicial", "responsable": "Despacho", "fecha": "Al notificarse"}]},
        {"maqueta": "equipo", "titulo": "Quien lleva el asunto", "personas": [
          {"nombre": "Departamento procesal", "cargo": "Direccion del asunto"}, {"nombre": "Area de cobros", "cargo": "Seguimiento y contacto con el cliente"}]},
        {"maqueta": "cierre", "titulo": "Gracias", "texto": "Documento de trabajo para la reunion con el cliente.", "contacto": "Departamento de procesal civil"},
      ]}
    textos = dict(COMUN, **{"TITULO_DOCUMENTO": "Reclamacion a Construcciones Delta", "ETIQUETA_SUPERIOR": "Presentacion al cliente",
                            "ENTRADILLA": "Presentacion para la reunion con el cliente."})
    return componer("presentacion_reclamacion_cliente.html", textos, datos, "presentacion", modulos=["diagramas"])

def white_paper():
    demo = {"demo": {"nombre": "Datos ficticios de demostracion", "consulta": "2026-10-11"}}
    datos = {"idioma": "es-ES", "moneda": "EUR", "fuentes": demo,
      "marca": {"nombre": "Despacho de ejemplo", "acento": "#7a2e3b", "acento_fuerte": "#5c1f2b", "serie": ["#7a2e3b", "#b07d3a", "#3f6b5a", "#4b5d86", "#9a5a7c", "#6b7280"],
                "oscuro": {"acento": "#e48aa6", "serie": ["#e48aa6", "#e0b36a", "#8fc2a8", "#9fb2e0", "#d49ab8", "#a0a7ad"]},
                "pie": "Despacho de ejemplo, S.L.P. · Documento de demostracion con identidad corporativa aplicada desde el bloque marca."},
      "cifras": {"plazo_2026": {"de": "plazos_pago", "calculo": "ultimo", "unidad": "dias", "decimales": 0},
                 "plazo_2022": {"de": "plazos_pago", "calculo": "primero", "unidad": "dias", "decimales": 0},
                 "subida": {"operacion": "diferencia", "a": "plazo_2026", "b": "plazo_2022", "unidad": "dias", "decimales": 0, "signo": True, "mejor": "bajar"}},
      "graficos": {
        "plazos_pago": {"tipo": "linea", "unidad": "dias", "fuente": "demo", "etiquetas": ["2022", "2023", "2024", "2025", "2026"],
                        "series": [{"nombre": "Plazo medio de pago a pymes", "valores": [71, 74, 78, 80, 83]}],
                        "umbral": {"desde": 0, "hasta": 60, "rotulo": "Plazo de referencia (60 dias)"},
                        "resumen": "El plazo medio de pago pasa de 71 a 83 dias entre 2022 y 2026, por encima de los 60 de referencia"},
        "causas": {"tipo": "barras", "unidad": "pct", "fuente": "demo", "elementos": [{"rotulo": "Falta de liquidez del cliente", "valor": 41},
                   {"rotulo": "Discrepancia en la factura", "valor": 23}, {"rotulo": "Factura sin aceptar", "valor": 18}, {"rotulo": "Otras causas", "valor": 18}],
                   "resumen": "La falta de liquidez explica el 41 por ciento de los impagos"},
        "protocolo": dict(FLUJO_MONITORIO, fuente="demo", resumen="Del impago al monitorio pasando por el requerimiento"),
        "riesgos": {"tipo": "matriz", "fuente": "demo", "filas": ["Alta", "Media", "Baja"], "columnas": ["Bajo", "Medio", "Alto"],
                    "eje_filas": "Probabilidad", "eje_columnas": "Impacto",
                    "elementos": [{"nombre": "Cliente unico que concentra ventas", "fila": "Media", "columna": "Alto"},
                                  {"nombre": "Facturas sin aceptacion escrita", "fila": "Alta", "columna": "Medio"},
                                  {"nombre": "Prescripcion por inactividad", "fila": "Baja", "columna": "Alto"}]},
      }}
    contenido = PIEZAS[("documento_largo", "contenido")]
    contenido = contenido.replace('<figure class="grafico" data-grafico="figura_1"></figure>',
        '<figure class="grafico" data-grafico="plazos_pago"></figure>')
    contenido = contenido.replace("    <p>{{TEXTO_CAPITULO_3}}</p>",
        "    <p>{{TEXTO_CAPITULO_3}}</p>\n    <figure class=\"grafico\" data-grafico=\"causas\"></figure>\n"
        "    <figure class=\"grafico\" data-grafico=\"protocolo\"></figure>\n    <figure class=\"grafico\" data-grafico=\"riesgos\"></figure>")
    textos = dict(COMUN, **{
      "TITULO_CORTO": "Morosidad en pymes 2026", "TITULO_DOCUMENTO": "Cobrar antes de reclamar: un protocolo para la morosidad de las pymes",
      "ETIQUETA_SUPERIOR": "White paper | Derecho mercantil", "ENTRADILLA": "Por que los plazos de pago siguen creciendo y que puede hacer una empresa antes de llegar al juzgado.",
      "AUTOR": "Departamento de procesal civil", "FECHA_EMISION": "octubre de 2026",
      "TITULO_RESUMEN": "Resumen ejecutivo",
      "CONCLUSION_1": 'El plazo medio de pago a pymes ha subido <span data-cifra="subida"></span> desde 2022 y sigue por encima del de referencia.',
      "CONCLUSION_2": "La mayoria de los impagos no son insolvencias: son facturas discutidas o sin aceptar que un protocolo interno evita.",
      "CONCLUSION_3": "Un requerimiento fehaciente a tiempo y la via monitoria resuelven la mayor parte de las reclamaciones sin juicio.",
      "TITULO_INDICE": "Contenido",
      "TITULO_CAPITULO_1": "El problema", "TEXTO_CAPITULO_1": "Las pymes financian a sus clientes sin quererlo. Cada dia de retraso en el cobro es circulante que no se puede destinar a la actividad.",
      "IDEA_DESTACADA_1": "Cobrar no empieza cuando vence la factura: empieza cuando se firma el pedido.",
      "TITULO_CAPITULO_2": "Los plazos de pago",
      "TEXTO_CAPITULO_2": 'La serie de los ultimos cinco anos muestra una subida sostenida del plazo medio, de <span data-cifra="plazo_2022"></span> a <span data-cifra="plazo_2026"></span>.',
      "TEXTO_CAPITULO_2_CONTINUACION": "La distancia frente al plazo de referencia no se ha cerrado en ningun ejercicio.",
      "TITULO_CAPITULO_3": "Que puede hacer la empresa", "TEXTO_CAPITULO_3": "Las causas del impago marcan la respuesta: una discrepancia se resuelve con documentacion; una falta de liquidez, con garantias y con rapidez.",
      "SUBTITULO_CAPITULO_3": "Tres medidas que cambian el resultado", "PUNTO_1": "Aceptacion escrita de cada factura o albaran.", "PUNTO_2": "Requerimiento fehaciente a los treinta dias del vencimiento.",
      "TITULO_NOTAS": "Notas", "NOTA_1": "Todas las cifras de este documento son ficticias y sirven solo para mostrar el formato.",
    })
    return componer("white_paper_morosidad_pymes.html", textos, datos, "documento_largo", tema="editorial", contenido=contenido, modulos=["diagramas", "marca"])

def resumen():
    datos = {"idioma": "es-ES", "moneda": "EUR", "fuentes": FUENTE_CLIENTE,
      "cifras": {"principal": {"valor": PRINCIPAL}, "intereses": {"valor": INTERESES}, "costas": {"valor": COSTAS},
                 "principal_e_intereses": {"operacion": "suma", "a": "principal", "b": "intereses"},
                 "indicador_1": {"operacion": "suma", "a": "principal_e_intereses", "b": "costas", "unidad": "eur"},
                 "indicador_2": {"valor": 5600, "unidad": "eur"},
                 "tres_mayores": {"operacion": "diferencia", "a": "principal", "b": FACTURAS[3][1]},
                 "indicador_3": {"operacion": "porcentaje", "a": "tres_mayores", "b": "principal", "unidad": "pct"}},
      "graficos": {"principal": {"tipo": "barras", "unidad": "eur", "fuente": "cliente", "elementos": ELEMENTOS_FACTURAS,
                                 "resumen": "Tres facturas concentran la deuda"}}}
    textos = dict(COMUN, **{
      "TITULO_CORTO": "Resumen reclamacion Delta", "TITULO_DOCUMENTO": "Recomendamos presentar el monitorio la semana que viene",
      "ETIQUETA_SUPERIOR": "Resumen ejecutivo | Expediente 2026/0417",
      "ENTRADILLA": "Construcciones Delta, S.L. no ha pagado en el plazo del burofax. La via monitoria es la mas rapida y no exige abogado ni procurador al inicio.",
      "DESTINATARIO": "Direccion de Suministros Ibericos del Norte, S.L.", "FECHA_EMISION": "28 de septiembre de 2026",
      "INDICADOR_1_ROTULO": "Total reclamable", "INDICADOR_1_DETALLE": "Principal, intereses y costas estimadas",
      "INDICADOR_2_ROTULO": "Ya cobrado", "INDICADOR_2_DETALLE": "Dos pagos a cuenta",
      "INDICADOR_3_ROTULO": "En tres facturas", "INDICADOR_3_DETALLE": "Peso sobre el principal",
      "TITULO_GRAFICO": "Tres facturas concentran la deuda", "TITULO_CONCLUSIONES": "Conclusiones",
      "CONCLUSION_1": "La deuda esta reconocida por escrito: el monitorio tiene base documental solida.",
      "CONCLUSION_2": "Sin pagos desde julio, esperar solo aumenta el riesgo de insolvencia del deudor.",
      "CONCLUSION_3": "Si hay oposicion, el asunto pasa al declarativo; la cuantia lo justifica.",
      "DECISION_QUE_SE_PIDE": "Decision: autorizar la presentacion de la peticion de monitorio antes del 2 de octubre.",
    })
    return componer("resumen_reclamacion_una_pagina.html", textos, datos, "resumen_ejecutivo", tema="corporativo", modulos=["encaje"])

# --------------------------------------------------------------------------- galeria
FLUJO_MONITORIO = {"tipo": "diagrama", "disposicion": "capas", "grupos": {"1": "Via judicial", "2": "Cierre", "3": "Hechos"},
  "nodos": [{"id": "contrato", "texto": "Contrato de suministro", "forma": "inicio"}, {"id": "impago", "texto": "Impago de siete facturas", "grupo": 3},
            {"id": "pago", "texto": "¿Paga en el plazo del requerimiento?", "forma": "decision"}, {"id": "fin", "texto": "Archivo del expediente", "forma": "inicio", "grupo": 2},
            {"id": "monitorio", "texto": "Peticion de monitorio", "grupo": 1}],
  "conexiones": [{"de": "contrato", "a": "impago"}, {"de": "impago", "a": "pago", "texto": "burofax"}, {"de": "pago", "a": "fin", "texto": "si"},
                 {"de": "pago", "a": "monitorio", "texto": "no", "estilo": "destacada"}]}

GALERIA = [
  ("barras", "Barras horizontales", "Comparar partidas. Ordenadas de mayor a menor.",
   {"tipo": "barras", "unidad": "eur", "elementos": ELEMENTOS_FACTURAS}),
  ("columnas", "Columnas", "Comparar pocos periodos o grupos, una o varias series.",
   {"tipo": "columnas", "unidad": "eur", "etiquetas": ["1T", "2T", "3T", "4T"],
    "series": [{"nombre": "2025", "valores": [12000, 16000, 9000, 14000]}, {"nombre": "2026", "valores": [14000, 18500, 11000, None]}]}),
  ("apiladas", "Columnas apiladas", "Composicion de cada periodo, con el total encima.",
   {"tipo": "apiladas", "unidad": "eur", "etiquetas": ["Enero", "Febrero", "Marzo"],
    "series": [{"nombre": "Principal", "valores": [5000, 6000, 4000]}, {"nombre": "Intereses", "valores": [400, 520, 380]}]}),
  ("cien", "Apiladas al cien por cien", "Proporcion por periodo. Nunca cuando importa el volumen.",
   {"tipo": "apiladas", "cien": True, "etiquetas": ["2024", "2025", "2026"],
    "series": [{"nombre": "Estimadas", "valores": [30, 42, 51]}, {"nombre": "Desestimadas", "valores": [10, 8, 6]}]}),
  ("linea", "Linea con area, banda y anotaciones", "Evolucion frente a un limite, con huecos y marcas de contexto.",
   {"tipo": "linea", "unidad": "num", "etiquetas": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep"],
    "series": [{"nombre": "Asuntos abiertos", "valores": [31, 29, 33, None, 36, 37, 39, 40, 42]},
               {"nombre": "Media del ano anterior", "valores": [30, 30, 31, 31, 31, 32, 32, 32, 32]}],
    "umbral": {"desde": 25, "hasta": 35, "rotulo": "Capacidad del equipo"},
    "anotaciones": [{"indice": 4, "texto": "Nuevo cliente"}], "destacar": ["maximo"]}),
  ("medidor", "Medidor semicircular", "Porcentaje de algo con maximo conocido.",
   {"tipo": "medidor", "valor": 68, "rotulo": "plazo de prescripcion consumido"}),
  ("cascada", "Cascada", "Como se llega a un total; los saldos negativos bajan.",
   {"tipo": "cascada", "unidad": "eur", "pasos": [{"rotulo": "Principal", "valor": 12000}, {"rotulo": "Intereses", "valor": 1450},
                                                  {"rotulo": "Costas", "valor": 800}, {"rotulo": "Pagos", "valor": "@pagos"}],
    "total": {"rotulo": "A reclamar"}}),
  ("anillo", "Anillo", "Peso de cada parte sobre el total, con la cifra en el centro.",
   {"tipo": "anillo", "unidad": "eur", "porciones": [{"rotulo": "Principal", "valor": 12000}, {"rotulo": "Intereses", "valor": 1450},
                                                     {"rotulo": "Costas", "valor": 800}], "centro": {"rotulo": "total"}}),
  ("tarta", "Tarta", "Reparto en hasta seis porciones; el resto se agrupa en Otros.",
   {"tipo": "tarta", "unidad": "num", "porciones": [{"rotulo": "Madrid", "valor": 30}, {"rotulo": "Cataluna", "valor": 25},
     {"rotulo": "Andalucia", "valor": 20}, {"rotulo": "Valencia", "valor": 10}, {"rotulo": "Galicia", "valor": 6},
     {"rotulo": "Pais Vasco", "valor": 5}, {"rotulo": "Resto", "valor": 4}]}),
  ("matriz", "Matriz de riesgo e impacto", "Contingencias numeradas en su celda, con lo que hay que hacer.",
   {"tipo": "matriz", "filas": ["Alta", "Media", "Baja"], "columnas": ["Bajo", "Medio", "Alto"], "eje_filas": "Probabilidad", "eje_columnas": "Impacto",
    "elementos": [{"nombre": "Prescripcion de la accion", "fila": "Alta", "columna": "Alto"},
                  {"nombre": "Insolvencia del deudor", "fila": "Media", "columna": "Alto"},
                  {"nombre": "Prueba documental incompleta", "fila": "Media", "columna": "Medio"}]}),
  ("bala", "Bala: real frente a objetivo", "Cumplimiento de un objetivo con tramos de valoracion de fondo.",
   {"tipo": "bala", "unidad": "eur", "elementos": [{"rotulo": "Facturacion", "valor": 82000, "objetivo": 100000, "tramos": [60000, 90000, 120000]},
                                                   {"rotulo": "Cobros", "valor": 61000, "objetivo": 80000, "tramos": [50000, 70000, 100000]}]}),
  ("divergentes", "Barras divergentes", "Saldos con signo alrededor de cero: a favor y en contra.",
   {"tipo": "divergentes", "unidad": "eur", "nombres": {"positivo": "Cobros", "negativo": "Pagos"},
    "elementos": [{"rotulo": "Enero", "valor": 12000}, {"rotulo": "Febrero", "valor": -8000}, {"rotulo": "Marzo", "valor": 3000}, {"rotulo": "Abril", "valor": -15000}]}),
  ("flujo", "Diagrama de flujo con conectores", "Modulo de diagramas, disposicion por capas.", FLUJO_MONITORIO),
  ("sociedades", "Organigrama o estructura societaria", "Modulo de diagramas, disposicion en arbol.",
   {"tipo": "diagrama", "disposicion": "arbol", "nodos": [{"id": "h", "texto": "Holding Delta, S.L."}, {"id": "a", "texto": "Construcciones Delta, S.L.", "grupo": 2},
     {"id": "b", "texto": "Delta Inmuebles, S.L.", "grupo": 2}, {"id": "c", "texto": "Delta Servicios, S.A.", "grupo": 3},
     {"id": "a1", "texto": "Obras Norte, S.L.", "grupo": 4}, {"id": "a2", "texto": "Obras Sur, S.L.", "grupo": 4}],
    "conexiones": [{"de": "h", "a": "a", "texto": "100 %"}, {"de": "h", "a": "b", "texto": "80 %"}, {"de": "h", "a": "c", "texto": "51 %"},
                   {"de": "a", "a": "a1", "texto": "100 %"}, {"de": "a", "a": "a2", "texto": "60 %"}]}),
  ("partes", "Mapa de relaciones entre partes", "Modulo de diagramas, disposicion radial.",
   {"tipo": "diagrama", "disposicion": "radial", "nodos": [{"id": "c", "texto": "Cliente: Suministros Ibericos"}, {"id": "d", "texto": "Deudor: Construcciones Delta", "grupo": "riesgo"},
     {"id": "av", "texto": "Avalista", "grupo": 3}, {"id": "ban", "texto": "Banco pagador", "grupo": 4}, {"id": "as", "texto": "Aseguradora de credito", "grupo": 2}],
    "conexiones": [{"de": "c", "a": "d", "texto": "reclama"}, {"de": "c", "a": "av", "texto": "aval"}, {"de": "c", "a": "ban"}, {"de": "c", "a": "as", "texto": "poliza", "estilo": "discontinua"}]}),
  ("carriles", "Quien hace que", "Modulo de diagramas, disposicion por carriles.",
   {"tipo": "diagrama", "disposicion": "carriles", "carriles": ["Cliente", "Despacho", "Juzgado"],
    "nodos": [{"id": "1", "texto": "Entrega facturas", "carril": "Cliente"}, {"id": "2", "texto": "Redacta y envia burofax", "carril": "Despacho"},
              {"id": "3", "texto": "Presenta monitorio", "carril": "Despacho"}, {"id": "4", "texto": "Requiere de pago al deudor", "carril": "Juzgado"},
              {"id": "5", "texto": "Decreto de fin", "carril": "Juzgado"}, {"id": "6", "texto": "Informa al cliente", "carril": "Despacho"}],
    "conexiones": [{"de": "1", "a": "2"}, {"de": "2", "a": "3", "texto": "10 dias"}, {"de": "3", "a": "4"}, {"de": "4", "a": "5", "texto": "20 dias"}, {"de": "5", "a": "6"}]}),
  ("dispersion", "Dispersion y burbujas", "Modulo avanzado: relacion entre cuantia y duracion; el tamano, las costas.",
   {"tipo": "dispersion", "eje_x": {"nombre": "Cuantia reclamada", "unidad": "eur"}, "eje_y": {"nombre": "Dias hasta sentencia", "unidad": "dias"}, "nombre_tamano": "Costas", "unidad_tamano": "eur",
    "puntos": [{"rotulo": r, "x": x, "y": y, "tamano": c} for r, x, y, c in [("Asunto A", 12000, 210, 1800), ("Asunto B", 48000, 420, 5200), ("Asunto C", 7500, 150, 900),
               ("Asunto D", 86000, 610, 9800), ("Asunto E", 31000, 300, 3100), ("Asunto F", 22000, 380, 2600)]]}),
  ("histograma", "Histograma", "Modulo avanzado: como se reparten los dias de demora de 40 facturas.",
   {"tipo": "histograma", "unidad": "dias", "nombre": "Dias de demora", "valores": [12, 25, 33, 41, 45, 52, 58, 60, 61, 67, 70, 72, 75, 80, 84, 88, 90, 93, 97, 101,
     105, 110, 118, 121, 130, 138, 145, 151, 160, 172, 180, 195, 210, 230, 247, 262, 280, 301, 313, 340]}),
  ("radar", "Radar", "Modulo avanzado: dos vias puntuadas de 0 a 10 con los mismos criterios.",
   {"tipo": "radar", "maximo": 10, "ejes": ["Coste", "Rapidez", "Probabilidad de exito", "Riesgo reputacional", "Control del cliente"],
    "series": [{"nombre": "Monitorio", "valores": [9, 8, 7, 8, 6]}, {"nombre": "Arbitraje", "valores": [4, 6, 8, 9, 9]}]}),
  ("embudo", "Embudo", "Modulo avanzado: de la consulta al asunto cerrado.",
   {"tipo": "embudo", "etapas": [{"rotulo": "Consultas", "valor": 420}, {"rotulo": "Presupuestos", "valor": 260}, {"rotulo": "Encargos", "valor": 118}, {"rotulo": "Cerrados", "valor": 97}]}),
  ("treemap", "Treemap", "Modulo avanzado: peso de cada area cuando son muchas.",
   {"tipo": "treemap", "unidad": "eur", "elementos": [{"rotulo": r, "valor": v} for r, v in [("Mercantil", 1060000), ("Litigacion", 753000), ("Laboral", 530000), ("Fiscal", 307000), ("Penal", 90000), ("Otros", 50000)]]}),
  ("pendiente", "Pendiente", "Modulo avanzado: cada concepto, de la propuesta a la liquidacion definitiva.",
   {"tipo": "pendiente", "unidad": "eur", "etiquetas": ["Propuesta", "Definitiva"], "elementos": [{"rotulo": "Cuota", "antes": 184600, "despues": 151200},
     {"rotulo": "Intereses", "antes": 22900, "despues": 18700}, {"rotulo": "Sancion", "antes": 92300, "despues": 45400}]}),
  ("halteras", "Halteras", "Modulo avanzado: lo pedido frente a lo concedido en cada partida.",
   {"tipo": "halteras", "unidad": "eur", "nombres": {"a": "Pedido", "b": "Concedido"}, "elementos": [{"rotulo": "Danos materiales", "a": 48000, "b": 31000},
     {"rotulo": "Lucro cesante", "a": 60000, "b": 22000}, {"rotulo": "Dano moral", "a": 15000, "b": 9000}]}),
  ("piramide", "Piramide", "Modulo avanzado: plantilla por tramos de edad.",
   {"tipo": "piramide", "etiquetas": ["< 30", "30-39", "40-49", "50-59", "60+"], "izquierda": {"nombre": "Hombres", "valores": [12, 30, 41, 28, 9]}, "derecha": {"nombre": "Mujeres", "valores": [15, 36, 38, 22, 6]}}),
  ("calendario", "Calendario de calor", "Modulo avanzado: vencimientos por dia en el trimestre.",
   {"tipo": "calendario", "desde": "2026-07-01", "hasta": "2026-09-30", "dias": {"2026-07-%02d" % d: (d * 7) % 5 for d in range(1, 31) if d % 3} }),
  ("pictograma", "Pictograma", "Modulo avanzado: una proporcion contada en figuras.",
   {"tipo": "pictograma", "valor": 3, "total": 10, "rotulo": "3 de cada 10 impagos acaban en juicio"}),
  ("qr", "Codigo QR", "Modulo QR: lleva al lector en papel a la fuente.",
   {"tipo": "qr", "texto": "https://www.boe.es", "rotulo": "Boletin Oficial del Estado"}),
  ("mapa", "Mapa por comunidades autonomas", "Modulo mapa con mapa_ccaa: asuntos por cada 1.000 clientes (tasa), con Madrid destacada.",
   {"tipo": "mapa", "unidad": "num", "nombre_valor": "Asuntos por 1.000 clientes", "destacar": ["Madrid"],
    "tasa": {"por": 1000, "numerador": {"Andalucia": 412, "Cataluna": 388, "Madrid": 520, "Comunidad Valenciana": 301, "Galicia": 120, "Castilla y Leon": 96,
                                        "Pais Vasco": 143, "Canarias": 88, "Aragon": 71, "Baleares": 55, "Murcia": 64, "Ceuta": 4, "Melilla": 3},
             "denominador": {"Andalucia": 41000, "Cataluna": 39500, "Madrid": 38000, "Comunidad Valenciana": 26000, "Galicia": 14000, "Castilla y Leon": 12000,
                             "Pais Vasco": 9500, "Canarias": 7000, "Aragon": 6500, "Baleares": 4000, "Murcia": 6000, "Ceuta": 400, "Melilla": 350}}}),
  ("provincias", "Mapa por provincias", "Modulo mapa con mapa_provincias: facturacion por provincia; las que no tienen dato, rayadas.",
   {"tipo": "mapa", "nivel": "provincias", "unidad": "eur", "valores": {"Zaragoza": 182000, "Huesca": 41000, "Teruel": 18000, "Madrid": 260000, "Barcelona": 210000,
     "Valencia": 99000, "Sevilla": 120000, "Malaga": 87000, "A Coruna": 40000, "Las Palmas": 33000}}),
  ("plazos", "Diagrama de plazos", "Varios plazos en una escala comun, con la marca de hoy.",
   {"tipo": "plazos", "hoy": "2026-09-20", "plazos": [{"rotulo": "Recurso de reposicion", "inicio": "2026-08-01", "fin": "2026-08-20"},
     {"rotulo": "Requerimiento", "inicio": "2026-09-01", "fin": "2026-09-27"},
     {"rotulo": "Contestacion a la demanda", "inicio": "2026-10-01", "fin": "2026-11-13"},
     {"rotulo": "Negociacion con la contraria", "inicio": "2026-09-10"},
     {"rotulo": "Vista prevista", "inicio": "2026-12-01", "fin": "2026-12-15", "aproximada": True},
     {"rotulo": "Recurso (20 dias habiles)", "inicio": "2026-09-17", "fin": "@vencimiento_recurso"}]}),
  ("area_apilada", "Area apilada", "Modulo analitico: composicion de la cartera por antiguedad, mes a mes.",
   {"tipo": "area_apilada", "unidad": "eur", "etiquetas": ["Abr", "May", "Jun", "Jul", "Ago", "Sep"],
    "series": [{"nombre": "Hasta 90 dias", "valores": [9000, 8200, 7800, 6900, 6100, 5400]}, {"nombre": "De 91 a 180", "valores": [4000, 6500, 8800, 10900, 12200, 13600]},
               {"nombre": "Mas de 180", "valores": [1500, 2400, 4100, 6300, 9200, 12900]}]}),
  ("pareto", "Pareto", "Modulo analitico: cuatro deudores concentran el 80 por ciento de la deuda.",
   {"tipo": "pareto", "unidad": "eur", "nombre": "Deuda", "elementos": [{"rotulo": r, "valor": v} for r, v in [("Construcciones Delta", 42180.5), ("Talleres Ebro", 18400), ("Hostal Mirador", 9300),
     ("Fincas Soto", 7100), ("Bar Central", 3900), ("Clinica Vera", 2600), ("Resto (9 deudores)", 6200)]]}),
  ("escalones", "Escalones", "Modulo analitico: tipo de interes legal y de demora, que rigen por anos.",
   {"tipo": "escalones", "unidad": "pct", "etiquetas": ["2021", "2022", "2023", "2024", "2025", "2026"],
    "series": [{"nombre": "Interes legal", "valores": [3, 3, 3.25, 3.25, 3.25, 3.25]}, {"nombre": "Demora operaciones comerciales", "valores": [8, 8, 10.5, 12.5, 11.15, 10.65]}]}),
  ("cajas", "Cajas", "Modulo analitico: dias hasta sentencia en tres juzgados, con mediana, cuartiles y atipicos.",
   {"tipo": "cajas", "unidad": "dias", "grupos": [{"rotulo": "Juzgado n. 3", "valores": [120, 135, 140, 150, 158, 162, 170, 181, 190, 240, 410]},
     {"rotulo": "Juzgado n. 7", "valores": [95, 100, 108, 112, 120, 125, 130, 142, 150, 160]}, {"rotulo": "Juzgado n. 12", "valores": [200, 215, 230, 260, 275, 290, 310, 330, 360, 420, 480]}]}),
  ("tornado", "Tornado", "Modulo analitico: que parametro mueve mas la indemnizacion estimada.",
   {"tipo": "tornado", "unidad": "eur", "base": 48000, "nombres": {"bajo": "Escenario bajo", "alto": "Escenario alto"},
    "elementos": [{"rotulo": "Dias de baja", "bajo": 36000, "alto": 61000}, {"rotulo": "Secuelas (puntos)", "bajo": 41000, "alto": 58000},
                  {"rotulo": "Lucro cesante", "bajo": 44000, "alto": 53000}, {"rotulo": "Factor de correccion", "bajo": 46500, "alto": 50500}]}),
  ("rango", "Rango", "Modulo analitico: donde cae la sancion propuesta dentro de la horquilla legal.",
   {"tipo": "rango", "unidad": "eur", "minimo": 601, "maximo": 30000,
    "tramos": [{"hasta": 6000, "rotulo": "Grado minimo", "color": "ok"}, {"hasta": 18000, "rotulo": "Grado medio", "color": "aviso"}, {"rotulo": "Grado maximo", "color": "riesgo"}],
    "marcas": [{"rotulo": "Propuesta de la inspeccion", "valor": 12500}, {"rotulo": "Alegamos", "valor": 3000, "color": "ok"}]}),
  ("mapa_calor", "Mapa de calor", "Modulo analitico: asuntos nuevos por area y mes.",
   {"tipo": "mapa_calor", "unidad": "entero", "filas": ["Mercantil", "Laboral", "Civil", "Penal", "Fiscal"], "columnas": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep"],
    "valores": [[12, 15, 18, 14, 20, 22, 9, 4, 19], [8, 9, 11, 13, 12, 10, 7, 3, 14], [20, 18, 22, 25, 24, 21, 15, 6, 23], [3, 2, 4, 5, 3, 4, 2, 1, 3], [6, 14, 9, 21, 8, 7, 5, 2, 6]]}),
  ("sankey", "Sankey", "Modulo analitico: de la consulta al resultado, por donde pasa cada asunto.",
   {"tipo": "sankey", "unidad": "entero",
    "nodos": [{"id": "con", "texto": "Consultas"}, {"id": "mon", "texto": "Monitorio"}, {"id": "neg", "texto": "Negociacion"}, {"id": "arc", "texto": "Archivo", "color": 6},
              {"id": "cob", "texto": "Cobrado", "color": "ok"}, {"id": "jui", "texto": "Juicio", "color": "aviso"}],
    "flujos": [{"de": "con", "a": "mon", "valor": 120}, {"de": "con", "a": "neg", "valor": 60}, {"de": "con", "a": "arc", "valor": 20},
               {"de": "mon", "a": "cob", "valor": 80}, {"de": "mon", "a": "jui", "valor": 40}, {"de": "neg", "a": "cob", "valor": 45}, {"de": "neg", "a": "arc", "valor": 15}]}),
  ("anillos", "Anillos", "Modulo analitico: avance de tres objetivos del trimestre.",
   {"tipo": "anillos", "elementos": [{"rotulo": "Facturacion", "valor": 82000, "maximo": 100000}, {"rotulo": "Cobros", "valor": 61000, "maximo": 80000}, {"rotulo": "Asuntos cerrados", "valor": 97, "maximo": 110}]}),
  ("puntuacion", "Puntuacion", "Modulo analitico: nota de cada criterio de 0 a 5.",
   {"tipo": "puntuacion", "maximo": 5, "elementos": [{"rotulo": "Solidez documental", "valor": 4.5}, {"rotulo": "Solvencia del deudor", "valor": 2}, {"rotulo": "Rapidez esperada", "valor": 4}, {"rotulo": "Coste relativo", "valor": 3.5}]}),
  ("progreso", "Progreso", "Modulo de seguimiento: avance por fase, con marca de objetivo y color por tramos.",
   {"tipo": "progreso", "unidad": "pct", "tramos": [40, 75], "elementos": [{"rotulo": "Documentacion", "valor": 100}, {"rotulo": "Requerimiento", "valor": 80, "objetivo": 100},
     {"rotulo": "Monitorio", "valor": 35, "objetivo": 60}, {"rotulo": "Ejecucion", "valor": 0}]}),
  ("semaforos", "Semaforos", "Modulo de seguimiento: estado de cada punto de control de proteccion de datos.",
   {"tipo": "semaforos", "elementos": [{"rotulo": "Registro de actividades de tratamiento", "estado": "ok", "nota": "Actualizado en marzo de 2026"},
     {"rotulo": "Contratos con encargados", "estado": "aviso", "nota": "Faltan dos proveedores"}, {"rotulo": "Evaluacion de impacto", "estado": "riesgo", "nota": "No realizada para el videoanalisis"},
     {"rotulo": "Delegado de proteccion de datos", "estado": "pendiente"}]}),
  ("linea_tiempo", "Linea de tiempo", "Modulo de seguimiento: hitos del expediente sobre una escala real de fechas.",
   {"tipo": "linea_tiempo", "hoy": "2026-09-24", "hitos": [{"fecha": "2025-11-15", "rotulo": "Vence la primera factura"}, {"fecha": "2026-01-20", "rotulo": "Vence la segunda"},
     {"fecha": "2026-05-04", "rotulo": "Reconocimiento de deuda"}, {"fecha": "2026-07-02", "rotulo": "Ultimo pago parcial"}, {"fecha": "2026-09-17", "rotulo": "Burofax"},
     {"fecha": "2026-10-09", "rotulo": "Presentacion del monitorio", "estado": "aviso"}]}),
]

def galeria():
    graficos, tarjetas = {}, []
    for clave, titulo, uso, g in GALERIA:
        g = dict(g, fuente="ejemplo", resumen=titulo + ": " + uso)
        graficos[clave] = g
        ancho = " ancho-total" if clave in ("linea", "plazos", "flujo", "sociedades", "partes", "carriles", "bala", "divergentes", "dispersion", "treemap", "calendario",
                                             "area_apilada", "pareto", "escalones", "cajas", "tornado", "rango", "mapa_calor", "sankey", "linea_tiempo") else ""
        tarjetas.append('<section class="tarjeta%s">\n      <h2>%s</h2>\n      <p class="subtitulo">%s <code>"tipo": "%s"</code></p>\n'
                        '      <figure class="grafico" data-grafico="%s"></figure>\n    </section>' % (ancho, titulo, uso, g["tipo"], clave))
    graficos["tendencia"] = {"tipo": "chispa", "valores": [10, 12, 18, 22, 30, 34], "etiquetas": ["Abril", "Septiembre"], "fuente": "ejemplo"}
    datos = {"idioma": "es-ES", "moneda": "EUR", "cifras": {"total": {"de": "cascada", "calculo": "suma", "unidad": "eur"},
                                                           "pagado": {"valor": 2000}, "pagos": {"operacion": "producto", "a": "pagado", "b": -1},
                                                           "vencimiento_recurso": {"calculo": "vencimiento", "desde": "2026-09-17", "dias": 20, "festivos": ["2026-10-12"], "unidad": "fecha"}},
             "fuentes": {"ejemplo": {"nombre": "Datos ficticios de demostracion", "consulta": "2026-10-11"}}, "graficos": graficos}
    contenido = ('<div class="indicadores">\n    <div class="indicador">\n      <p class="rotulo"><span class="icono" data-icono="euro"></span>Indicador con minigrafico</p>\n'
                 '      <p class="cifra" data-cifra="total"></p>\n      <p class="detalle">La cifra sale del grafico de cascada</p>\n'
                 '      <div class="tendencia" data-grafico="tendencia"></div>\n    </div>\n'
                 '    <div class="indicador es-atencion">\n      <p class="rotulo"><span class="icono" data-icono="plazo"></span>Vence el recurso</p>\n'
                 '      <p class="cifra" data-cifra="vencimiento_recurso"></p>\n      <p class="detalle">20 dias habiles desde el 17/9, sin el 12 de octubre</p>\n    </div>\n  </div>\n\n  <div class="malla">\n    '
                 + "\n    ".join(tarjetas) + "\n  </div>")
    textos = dict(COMUN, **{
      "TITULO_DOCUMENTO": "Galeria de graficos del motor de artefactos",
      "ETIQUETA_SUPERIOR": "Skill reportes | Catalogo de formas",
      "ENTRADILLA": "Cada grafico se declara con sus datos en el bloque datos-reporte y lo dibuja el motor de la base. Bajo cada uno estan su tabla de datos, la descarga en CSV y su fuente.",
    })
    return componer("galeria_graficos.html", textos, datos, ficha='<li><b>Tipos:</b> %d</li>' % len(GALERIA),
                    contenido=contenido, ancho="1120px", modulos=["diagramas", "avanzados", "analiticos", "seguimiento", "iconos", "qr", "plazos", "mapa", "mapa_ccaa", "mapa_provincias"])

GALERIA_DICT = {c: dict(g) for c, _, _, g in GALERIA}

# --------------------------------------------------------------------------- maquetas de reporte nuevas
DEMO = {"demo": {"nombre": "Datos ficticios de demostracion", "consulta": "2026-10-11"}}
def _d(cifras, graficos, fuentes=None):
    for g in graficos.values():
        g.setdefault("fuente", "demo")
    return {"idioma": "es-ES", "moneda": "EUR", "fuentes": fuentes or DEMO, "cifras": cifras, "graficos": graficos}
def _ind(textos, n, rotulo, detalle, cifra=None):
    textos["INDICADOR_%d_ROTULO" % n] = rotulo
    textos["INDICADOR_%d_DETALLE" % n] = detalle
    if cifra is not None:
        textos["INDICADOR_%d_CIFRA" % n] = cifra
def _tit(textos, clave, titulo, subtitulo):
    textos["TITULO_" + clave] = titulo
    textos["SUBTITULO_" + clave] = subtitulo
PIE_DEMO = {"PIE_AVISO_LEGAL": "Datos ficticios de demostracion. No sustituye al asesoramiento de un profesional colegiado."}

def cuadro_mando():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="Septiembre cierra por encima del objetivo de facturacion", ETIQUETA_SUPERIOR="Cuadro de mando | Comite de direccion",
             ENTRADILLA="La facturacion supera el objetivo mensual y el cobro mejora, pero el area laboral sigue por debajo de sus horas y dos areas acumulan saldo vencido.",
             PERIODO="septiembre de 2026", FECHA_ACTUALIZACION="1 de octubre de 2026")
    for n, r, d in [(1, "Facturacion", "frente a agosto"), (2, "Cobrado", "frente a agosto"), (3, "Saldo vencido", "frente a agosto"), (4, "Asuntos nuevos", "frente a agosto"),
                    (5, "Horas facturables", "acumulado del ano"), (6, "Margen", "sobre facturacion"), (7, "Dias medios de cobro", "objetivo: 60 dias"), (8, "Clientes activos", "con asunto abierto")]:
        _ind(t, n, r, d)
    _tit(t, "OBJETIVOS", "Cobro y facturacion casi en objetivo", "Avance sobre el objetivo del trimestre")
    _tit(t, "CUMPLIMIENTO", "Laboral, por debajo de sus horas", "Horas facturadas frente a objetivo por area")
    _tit(t, "ESTADO", "Dos areas con saldo vencido", "Estado de cada area al cierre")
    _tit(t, "TABLA", "Detalle por area", "Septiembre de 2026, en euros")
    t.update(COLUMNA_1="Area", COLUMNA_2="Facturado", COLUMNA_3="Cobrado", COLUMNA_4="Pendiente",
             FILA_1_C1="Mercantil", FILA_1_C2="96.400,00", FILA_1_C3="88.100,00", FILA_1_C4="8.300,00",
             FILA_2_C1="Litigacion", FILA_2_C2="71.250,00", FILA_2_C3="52.900,00", FILA_2_C4="18.350,00",
             FILA_3_C1="Laboral", FILA_3_C2="38.900,00", FILA_3_C3="31.200,00", FILA_3_C4="7.700,00")
    cifras = {"indicador_1": {"valor": 206550, "unidad": "eur", "decimales": 0}, "indicador_2": {"valor": 172200, "unidad": "eur", "decimales": 0},
              "indicador_3": {"valor": 34350, "unidad": "eur", "decimales": 0}, "indicador_4": {"valor": 31, "unidad": "entero"},
              "indicador_5": {"valor": 9840, "unidad": "entero"}, "indicador_6": {"valor": 34.2, "unidad": "pct"}, "indicador_7": {"valor": 71, "unidad": "dias"},
              "indicador_8": {"valor": 214, "unidad": "entero"},
              "variacion_1": {"valor": 6.8, "unidad": "pct", "signo": True}, "variacion_2": {"valor": 11.2, "unidad": "pct", "signo": True},
              "variacion_3": {"valor": -4.1, "unidad": "pct", "signo": True, "mejor": "bajar"}, "variacion_4": {"valor": 3, "unidad": "entero", "signo": True, "mejor": "neutro"}}
    g = {"tendencia_1": {"tipo": "chispa", "valores": [168000, 175000, 181000, 172000, 193400, 206550], "etiquetas": ["Abril", "Septiembre"]},
         "tendencia_5": {"tipo": "chispa", "valores": [1050, 1180, 1120, 1240, 980, 1310], "etiquetas": ["Abril", "Septiembre"]},
         "objetivos": {"tipo": "anillos", "resumen": "Avance del trimestre", "elementos": [{"rotulo": "Facturacion", "valor": 581000, "maximo": 600000}, {"rotulo": "Cobro", "valor": 492000, "maximo": 540000}, {"rotulo": "Asuntos", "valor": 88, "maximo": 100}]},
         "cumplimiento": {"tipo": "bala", "unidad": "horas", "resumen": "Horas por area frente a objetivo", "elementos": [{"rotulo": "Mercantil", "valor": 1420, "objetivo": 1300, "tramos": [900, 1200, 1600]},
                          {"rotulo": "Litigacion", "valor": 1180, "objetivo": 1200, "tramos": [900, 1200, 1600]}, {"rotulo": "Laboral", "valor": 760, "objetivo": 1000, "tramos": [700, 950, 1300]}]},
         "estado": {"tipo": "semaforos", "resumen": "Estado por area", "elementos": [{"rotulo": "Mercantil", "estado": "ok", "nota": "En objetivo de horas y cobro"},
                    {"rotulo": "Litigacion", "estado": "aviso", "nota": "18.350 EUR pendientes de mas de 60 dias"}, {"rotulo": "Laboral", "estado": "riesgo", "nota": "24 % por debajo de sus horas"}]}}
    return componer("cuadro_mando_comite.html", t, _d(cifras, g), "cuadro_mando", tema="dorado", modulos=["analiticos", "seguimiento"])

def ficha_una_pagina():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="Construcciones Delta, S.L.: deuda vencida y en reclamacion", TITULO_CORTO="Ficha Construcciones Delta", ETIQUETA_SUPERIOR="Ficha de cliente deudor",
             ENTRADILLA="Datos clave del deudor y estado de la reclamacion a 24 de septiembre de 2026.", REFERENCIA="2026/0417", FECHA_EMISION="24 de septiembre de 2026")
    for i, (r, v) in enumerate([("NIF", "B-50000000"), ("Domicilio", "Zaragoza"), ("Actividad", "Construccion"), ("Cliente desde", "2019"), ("Facturas impagadas", "7"), ("Via", "Monitorio")], 1):
        t["DATO_%d_ROTULO" % i], t["DATO_%d_VALOR" % i] = r, v
    _ind(t, 1, "Principal", "Siete facturas vencidas"); _ind(t, 2, "Cobrado", "Dos pagos a cuenta"); _ind(t, 3, "Pendiente", "Principal menos lo cobrado")
    _tit(t, "GRAFICO", "Tres facturas concentran la deuda", "Principal por factura, en euros")
    _tit(t, "ESTADO", "La reclamacion esta lista", "Estado de cada requisito")
    cifras = {"indicador_1": {"de": "principal", "calculo": "suma", "unidad": "eur"}, "indicador_2": {"valor": 5600, "unidad": "eur"},
              "indicador_3": {"operacion": "diferencia", "a": "indicador_1", "b": "indicador_2", "unidad": "eur"}}
    g = {"principal": {"tipo": "barras", "unidad": "eur", "elementos": ELEMENTOS_FACTURAS, "resumen": "Principal por factura"},
         "estado": {"tipo": "semaforos", "resumen": "Requisitos de la reclamacion", "elementos": [{"rotulo": "Reconocimiento de deuda", "estado": "ok", "nota": "Correo de 4 de mayo"},
                    {"rotulo": "Requerimiento fehaciente", "estado": "ok", "nota": "Burofax de 17 de septiembre"}, {"rotulo": "Solvencia del deudor", "estado": "aviso", "nota": "Sin informe reciente"}]}}
    return componer("ficha_deudor_una_pagina.html", t, _d(cifras, g, FUENTE_CLIENTE | DEMO), "ficha_una_pagina", tema="minimal", modulos=["seguimiento", "encaje"])

def infografia():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="La morosidad de las pymes, en tres cifras", TITULO_CORTO="Infografia morosidad", ETIQUETA_SUPERIOR="Infografia | Datos de demostracion",
             ENTRADILLA="Que pasa cuando una factura no se cobra y cuanto tarda en resolverse.", FUENTE_BREVE="datos ficticios de demostracion",
             FRASE_1="es la deuda media que una pyme deja de cobrar al ano", FRASE_2="dias tarda de media en cobrarse una factura reclamada", FRASE_3="se recuperan con un monitorio sin llegar a juicio",
             TITULO_PROPORCION="3 de cada 10 impagos acaban en juicio", TITULO_AVANCE="Lo que se recupera, segun la via", TITULO_HITOS="Asi avanza una reclamacion tipica")
    cifras = {"cifra_1": {"valor": 42180, "unidad": "eur", "decimales": 0}, "cifra_2": {"valor": 214, "unidad": "entero"}, "cifra_3": {"valor": 70, "unidad": "pct"}}
    g = {"proporcion": {"tipo": "pictograma", "valor": 3, "total": 10, "rotulo": "de cada 10 impagos reclamados", "resumen": "3 de cada 10"},
         "avance": {"tipo": "anillos", "resumen": "Porcentaje recuperado por via", "elementos": [{"rotulo": "Negociacion", "valor": 55}, {"rotulo": "Monitorio", "valor": 70}, {"rotulo": "Juicio", "valor": 82}]},
         "hitos": {"tipo": "linea_tiempo", "resumen": "Hitos de una reclamacion", "hitos": [{"fecha": "2026-01-15", "rotulo": "Vence la factura"}, {"fecha": "2026-03-01", "rotulo": "Recordatorio"},
                   {"fecha": "2026-05-04", "rotulo": "Burofax"}, {"fecha": "2026-06-20", "rotulo": "Monitorio"}, {"fecha": "2026-08-17", "rotulo": "Cobro"}]}}
    return componer("infografia_morosidad.html", t, _d(cifras, g), "infografia", tema="menta", modulos=["avanzados", "analiticos", "seguimiento"])

def comparativa():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="El monitorio gana en coste y en rapidez", TITULO_CORTO="Comparativa de vias", ETIQUETA_SUPERIOR="Comparativa de opciones | Expediente 2026/0417",
             ENTRADILLA="Tres vias para cobrar 42.180,50 euros de Construcciones Delta, puntuadas con los mismos criterios.", REFERENCIA="2026/0417", FECHA_EMISION="24 de septiembre de 2026",
             TITULO_RECOMENDACION="Recomendacion", RECOMENDACION="Presentar el monitorio: es la via mas barata y rapida, y el reconocimiento de deuda la sostiene.",
             CRITERIO_1="Coste inicial", CRITERIO_2="Plazo", CRITERIO_3="Exito esperado", CRITERIO_4="Abogado y procurador",
             OPCION_1_NOMBRE="Monitorio", OPCION_1_VEREDICTO="Recomendada", OPCION_1_C1="Bajo", OPCION_1_C2="2 a 4 meses", OPCION_1_C3="Alto", OPCION_1_C4="No al inicio",
             OPCION_2_NOMBRE="Negociacion", OPCION_2_VEREDICTO="Complementaria", OPCION_2_C1="Muy bajo", OPCION_2_C2="1 a 3 meses", OPCION_2_C3="Medio", OPCION_2_C4="No",
             OPCION_3_NOMBRE="Juicio ordinario", OPCION_3_VEREDICTO="Si hay oposicion", OPCION_3_C1="Alto", OPCION_3_C2="12 a 18 meses", OPCION_3_C3="Alto", OPCION_3_C4="Si")
    _tit(t, "PERFIL", "El monitorio tiene el perfil mas equilibrado", "Puntuacion de 0 a 10 en cada criterio")
    _tit(t, "DISTANCIA", "La diferencia esta en el coste", "Coste estimado minimo y maximo, en euros")
    g = {"perfil": {"tipo": "radar", "maximo": 10, "resumen": "Perfil de cada via", "ejes": ["Coste", "Rapidez", "Exito", "Control", "Riesgo"],
                    "series": [{"nombre": "Monitorio", "valores": [9, 8, 7, 6, 8]}, {"nombre": "Negociacion", "valores": [10, 9, 5, 8, 7]}, {"nombre": "Juicio", "valores": [3, 2, 8, 6, 5]}]},
         "distancia": {"tipo": "halteras", "unidad": "eur", "resumen": "Coste minimo y maximo", "nombres": {"a": "Minimo", "b": "Maximo"},
                       "elementos": [{"rotulo": "Negociacion", "a": 300, "b": 900}, {"rotulo": "Monitorio", "a": 600, "b": 2400}, {"rotulo": "Juicio", "a": 4200, "b": 9800}]}}
    return componer("comparativa_vias.html", t, _d({}, g), "comparativa", tema="corporativo", modulos=["avanzados"])

def cronograma_expediente():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="El monitorio se presenta el 9 de octubre", TITULO_CORTO="Cronograma 2026/0417", ETIQUETA_SUPERIOR="Cronograma del expediente | 2026/0417",
             ENTRADILLA="Donde esta la reclamacion frente a Construcciones Delta, que plazo corre y que viene ahora.", REFERENCIA="2026/0417", FECHA_EMISION="24 de septiembre de 2026",
             TITULO_AVISO="Plazo en curso", AVISO_PLAZO="El plazo del burofax vence el 27 de septiembre. Si no hay pago, se presenta el monitorio el 9 de octubre.",
             TITULO_PASOS="Proximos pasos", SUBTITULO_PASOS="Con responsable y fecha",
             PASO_1="Comprobar si llega el pago", RESPONSABLE_1="Cliente", FECHA_PASO_1="27 sept", PASO_2="Preparar la peticion de monitorio", RESPONSABLE_2="Despacho", FECHA_PASO_2="9 oct",
             PASO_3="Seguir el requerimiento del juzgado", RESPONSABLE_3="Despacho", FECHA_PASO_3="nov")
    _ind(t, 1, "Fase", "de cuatro", "Requerimiento"); _ind(t, 2, "Proximo vencimiento", "Plazo del burofax", "27/09/2026"); _ind(t, 3, "Dias que quedan", "Naturales", "3")
    _tit(t, "HITOS", "Diez meses desde la primera factura", "Lo que ha pasado, en una escala real de fechas")
    _tit(t, "PLAZOS", "Lo que corre ahora", "Plazos en curso y previstos, con la marca de hoy")
    _tit(t, "FASES", "La reclamacion va por la mitad", "Avance por fase")
    g = {"hitos": GALERIA_DICT["linea_tiempo"], "plazos": {"tipo": "plazos", "hoy": "2026-09-24", "resumen": "Plazos en curso", "plazos": [{"rotulo": "Plazo del burofax", "inicio": "2026-09-17", "fin": "2026-09-27"},
               {"rotulo": "Preparar el monitorio", "inicio": "2026-09-28", "fin": "2026-10-09"}, {"rotulo": "Pago u oposicion", "inicio": "2026-10-20", "fin": "2026-11-10", "aproximada": True}]},
         "fases": {"tipo": "progreso", "unidad": "pct", "resumen": "Avance por fase", "elementos": [{"rotulo": "Documentacion", "valor": 100}, {"rotulo": "Requerimiento", "valor": 70},
                   {"rotulo": "Monitorio", "valor": 0, "objetivo": 100}, {"rotulo": "Cobro", "valor": 0}]}}
    return componer("cronograma_expediente_0417.html", t, _d({}, g), "cronograma_expediente", tema="esmeralda_noche", modulos=["seguimiento"])

def lista_control():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="Cumplimos el 70 % de los requisitos de proteccion de datos", TITULO_CORTO="Lista de control RGPD", ETIQUETA_SUPERIOR="Lista de control | Proteccion de datos",
             ENTRADILLA="Revision de los requisitos del RGPD en una clinica dental. Los estados los ha fijado el responsable de cumplimiento.", REFERENCIA="AUD-2026-12", FECHA_EMISION="10 de octubre de 2026",
             COLUMNA_1="Requisito", COLUMNA_2="Evidencia", COLUMNA_3="Estado",
             FILA_1_REQUISITO="Registro de actividades", FILA_1_EVIDENCIA="Hoja de registro de marzo de 2026", FILA_1_CLASE="ok", FILA_1_ESTADO="Correcto",
             FILA_2_REQUISITO="Contratos con encargados", FILA_2_EVIDENCIA="Faltan dos proveedores", FILA_2_CLASE="atencion", FILA_2_ESTADO="Atencion",
             FILA_3_REQUISITO="Evaluacion de impacto", FILA_3_EVIDENCIA="No realizada para videovigilancia", FILA_3_CLASE="riesgo", FILA_3_ESTADO="Riesgo",
             FILA_4_REQUISITO="Informacion a pacientes", FILA_4_EVIDENCIA="Clausula en la ficha de alta", FILA_4_CLASE="ok", FILA_4_ESTADO="Correcto")
    _ind(t, 1, "Cumplimiento", "7 de 10 requisitos"); _ind(t, 2, "Pendientes", "Requieren accion", "2"); _ind(t, 3, "En riesgo", "Accion inmediata", "1")
    _tit(t, "BLOQUES", "La seguridad es el bloque mas atrasado", "Avance por bloque")
    _tit(t, "REQUISITOS", "Un requisito en riesgo", "Estado de cada requisito clave")
    _tit(t, "TABLA", "Evidencias revisadas", "Lo que se ha comprobado y su estado")
    cifras = {"indicador_1": {"operacion": "porcentaje", "a": 7, "b": 10, "unidad": "pct"}}
    g = {"bloques": {"tipo": "progreso", "unidad": "pct", "tramos": [50, 80], "resumen": "Avance por bloque", "elementos": [{"rotulo": "Gobernanza", "valor": 100}, {"rotulo": "Informacion", "valor": 85},
                     {"rotulo": "Encargados", "valor": 60}, {"rotulo": "Seguridad", "valor": 40}]},
         "requisitos": GALERIA_DICT["semaforos"]}
    return componer("lista_control_rgpd.html", t, _d(cifras, g), "lista_control", tema="tecnico", modulos=["seguimiento"])

def mapa_riesgos():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="Dos riesgos concentran la exposicion de la operacion", TITULO_CORTO="Mapa de riesgos", ETIQUETA_SUPERIOR="Mapa de riesgos | Compra de Delta Servicios",
             ENTRADILLA="Contingencias detectadas en la revision, valoradas por el equipo. La exposicion es la suma de los escenarios centrales.", REFERENCIA="DD-2026-03", FECHA_EMISION="15 de octubre de 2026")
    _ind(t, 1, "Riesgos identificados", "En cinco areas", "8"); _ind(t, 2, "Criticos", "Actuar antes de firmar", "2"); _ind(t, 3, "Exposicion estimada", "Escenario central")
    _tit(t, "MATRIZ", "Dos riesgos en zona roja", "Probabilidad por impacto")
    _tit(t, "MEDIDAS", "Una medida sin empezar", "Estado de las medidas de mitigacion")
    _tit(t, "IMPACTO", "La inspeccion fiscal es lo que mas mueve la cifra", "Impacto economico de cada riesgo, en euros")
    _tit(t, "EXPOSICION", "La propuesta cae en grado medio", "Sancion propuesta dentro de la horquilla legal")
    cifras = {"indicador_3": {"valor": 186000, "unidad": "eur", "decimales": 0}}
    g = {"matriz": GALERIA_DICT["matriz"], "medidas": {"tipo": "semaforos", "resumen": "Medidas", "elementos": [
             {"rotulo": "Garantia del vendedor", "estado": "ok", "nota": "Pactada en la oferta"}, {"rotulo": "Regularizacion fiscal", "estado": "aviso", "nota": "En negociacion"},
             {"rotulo": "Auditoria laboral", "estado": "riesgo", "nota": "Sin empezar"}]},
         "impacto": {"tipo": "tornado", "unidad": "eur", "base": 186000, "resumen": "Impacto de cada riesgo", "nombres": {"bajo": "Escenario favorable", "alto": "Escenario adverso"}, "color_bajo": "ok", "color_alto": "riesgo",
                     "elementos": [{"rotulo": "Inspeccion fiscal", "bajo": 120000, "alto": 268000}, {"rotulo": "Contingencia laboral", "bajo": 158000, "alto": 231000},
                                   {"rotulo": "Litigio con cliente", "bajo": 171000, "alto": 214000}, {"rotulo": "Garantias bancarias", "bajo": 180000, "alto": 199000}]},
         "exposicion": GALERIA_DICT["rango"]}
    return componer("mapa_riesgos_operacion.html", t, _d(cifras, g), "mapa_riesgos", tema="ambar", modulos=["analiticos", "seguimiento"])

def escenarios():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="La indemnizacion estara entre 36.000 y 61.000 euros", TITULO_CORTO="Escenarios indemnizacion", ETIQUETA_SUPERIOR="Escenarios | Reclamacion por accidente",
             ENTRADILLA="Tres escenarios con los supuestos que se barajan. Los dias de baja son lo que mas mueve el resultado.", REFERENCIA="2026/0533", FECHA_EMISION="12 de octubre de 2026",
             COLUMNA_1="Supuesto", COLUMNA_2="Bajo", COLUMNA_3="Central", COLUMNA_4="Alto",
             FILA_1_C1="Dias de baja", FILA_1_C2="90", FILA_1_C3="140", FILA_1_C4="210", FILA_2_C1="Secuelas (puntos)", FILA_2_C2="4", FILA_2_C3="7", FILA_2_C4="10",
             FILA_3_C1="Lucro cesante (meses)", FILA_3_C2="2", FILA_3_C3="4", FILA_3_C4="6")
    _ind(t, 1, "Escenario central", "Con los supuestos centrales"); _ind(t, 2, "Minimo", "Escenario bajo"); _ind(t, 3, "Maximo", "Escenario alto")
    _tit(t, "SUPUESTOS", "Que cambia en cada escenario", "Valores de cada supuesto")
    _tit(t, "POR_ESCENARIO", "El escenario alto casi dobla al bajo", "Indemnizacion por partida y escenario, en euros")
    _tit(t, "SENSIBILIDAD", "Los dias de baja mueven mas el resultado", "Resultado con cada supuesto en su extremo")
    _tit(t, "HORQUILLA", "La oferta de la aseguradora queda por debajo", "Oferta y reclamacion dentro de la horquilla estimada")
    cifras = {"indicador_1": {"valor": 48000, "unidad": "eur", "decimales": 0}, "indicador_2": {"valor": 36000, "unidad": "eur", "decimales": 0}, "indicador_3": {"valor": 61000, "unidad": "eur", "decimales": 0}}
    g = {"por_escenario": {"tipo": "columnas", "unidad": "eur", "resumen": "Por escenario", "etiquetas": ["Bajo", "Central", "Alto"],
                           "series": [{"nombre": "Baja", "valores": [14000, 21800, 32700]}, {"nombre": "Secuelas", "valores": [17000, 21200, 23300]}, {"nombre": "Lucro cesante", "valores": [5000, 5000, 5000]}]},
         "sensibilidad": GALERIA_DICT["tornado"],
         "horquilla": {"tipo": "rango", "unidad": "eur", "resumen": "Horquilla", "minimo": 36000, "maximo": 61000,
                       "marcas": [{"rotulo": "Oferta aseguradora", "valor": 31000, "color": "riesgo"}, {"rotulo": "Reclamamos", "valor": 52000, "color": "ok"}]}}
    return componer("escenarios_indemnizacion.html", t, _d(cifras, g), "escenarios", tema="oliva_oro", modulos=["analiticos"])

def embudo_conversion():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="Uno de cada cuatro contactos acaba en encargo", TITULO_CORTO="Embudo de captacion", ETIQUETA_SUPERIOR="Embudo de conversion | Captacion",
             ENTRADILLA="De la primera consulta al asunto cerrado en el tercer trimestre. La mayor perdida esta entre presupuesto y encargo.", PERIODO="julio a septiembre de 2026", FECHA_ACTUALIZACION="1 de octubre de 2026")
    _ind(t, 1, "Consultas", "Primer contacto"); _ind(t, 2, "Conversion", "frente al trimestre anterior"); _ind(t, 3, "Asuntos cerrados", "Con honorarios cobrados"); _ind(t, 4, "Mayor perdida", "Presupuesto a encargo", "55 %")
    _tit(t, "EMBUDO", "La mayor caida esta en el presupuesto", "Asuntos en cada etapa")
    _tit(t, "EVOLUCION", "Crecen las consultas de mas de 90 dias", "Cartera por antiguedad, mes a mes")
    _tit(t, "FLUJOS", "La negociacion cierra casi tanto como el monitorio", "Por donde pasa cada asunto")
    cifras = {"indicador_1": {"de": "embudo", "calculo": "maximo", "unidad": "entero"}, "indicador_3": {"de": "embudo", "calculo": "ultimo", "unidad": "entero"},
              "indicador_2": {"operacion": "porcentaje", "a": "indicador_3", "b": "indicador_1", "unidad": "pct"}, "variacion_2": {"valor": 2.4, "unidad": "pct", "signo": True}}
    g = {"embudo": GALERIA_DICT["embudo"], "evolucion": GALERIA_DICT["area_apilada"], "flujos": GALERIA_DICT["sankey"]}
    return componer("embudo_captacion.html", t, _d(cifras, g), "embudo_conversion", tema="lima", modulos=["avanzados", "analiticos"])

def actividad_equipo():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="Civil y mercantil concentran la actividad del trimestre", TITULO_CORTO="Actividad del equipo", ETIQUETA_SUPERIOR="Actividad del equipo | Tercer trimestre",
             ENTRADILLA="Asuntos nuevos, dias de mas carga, tiempos de resolucion y horas frente a objetivo, por area.", PERIODO="enero a septiembre de 2026", FECHA_ACTUALIZACION="1 de octubre de 2026")
    _ind(t, 1, "Horas facturadas", "Todas las areas"); _ind(t, 2, "Asuntos nuevos", "En nueve meses"); _ind(t, 3, "Mediana de resolucion", "Dias hasta sentencia", "158 dias"); _ind(t, 4, "Area sobrecargada", "Por encima del 110 % de horas", "Civil")
    _tit(t, "POR_AREA", "Civil marca el ritmo todos los meses", "Asuntos nuevos por area y mes")
    _tit(t, "DIAS", "Julio concentra los vencimientos", "Vencimientos por dia en el trimestre")
    _tit(t, "TIEMPOS", "El juzgado 12 tarda el doble", "Dias hasta sentencia por juzgado")
    _tit(t, "HORAS", "Laboral, por debajo de su objetivo", "Horas frente a objetivo")
    cifras = {"indicador_1": {"de": "horas", "calculo": "suma", "unidad": "entero"}, "indicador_2": {"valor": 512, "unidad": "entero"}}
    g = {"por_area": GALERIA_DICT["mapa_calor"], "dias": GALERIA_DICT["calendario"], "tiempos": GALERIA_DICT["cajas"],
         "horas": {"tipo": "bala", "unidad": "horas", "resumen": "Horas por area", "elementos": [{"rotulo": "Civil", "valor": 1520, "objetivo": 1350, "tramos": [900, 1200, 1700]},
                   {"rotulo": "Mercantil", "valor": 1290, "objetivo": 1300, "tramos": [900, 1200, 1700]}, {"rotulo": "Laboral", "valor": 760, "objetivo": 1000, "tramos": [700, 950, 1300]}]}}
    return componer("actividad_equipo_t3.html", t, _d(cifras, g), "actividad_equipo", tema="pizarra", modulos=["analiticos", "avanzados"])

def informe_territorial():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="Madrid tiene la tasa mas alta de asuntos por cliente", TITULO_CORTO="Informe territorial", ETIQUETA_SUPERIOR="Informe territorial | Asuntos por comunidad",
             ENTRADILLA="Asuntos abiertos por cada 1.000 clientes en cada comunidad autonoma. Cuatro comunidades concentran el 70 % del volumen.", PERIODO="2026", FECHA_ACTUALIZACION="1 de octubre de 2026")
    _ind(t, 1, "Asuntos abiertos", "En todas las comunidades"); _ind(t, 2, "Tasa mas alta", "Madrid, por 1.000 clientes", "13,7"); _ind(t, 3, "Concentracion", "Cuatro comunidades", "70 %")
    _tit(t, "MAPA", "Madrid destaca por encima de la media", "Asuntos por cada 1.000 clientes")
    _tit(t, "RANKING", "Madrid y Andalucia lideran en volumen", "Asuntos abiertos por comunidad")
    _tit(t, "CONCENTRACION", "Cuatro comunidades suman el 70 %", "Asuntos ordenados con su porcentaje acumulado")
    num = GALERIA_DICT["mapa"]["tasa"]["numerador"]
    elementos = [{"rotulo": k, "valor": v} for k, v in sorted(num.items(), key=lambda kv: -kv[1])]
    cifras = {"indicador_1": {"de": "ranking", "calculo": "suma", "unidad": "entero"}}
    g = {"mapa": GALERIA_DICT["mapa"], "ranking": {"tipo": "barras", "unidad": "entero", "resumen": "Por comunidad", "elementos": elementos[:8]},
         "concentracion": {"tipo": "pareto", "unidad": "entero", "nombre": "Asuntos", "resumen": "Concentracion", "elementos": elementos[:6] + [{"rotulo": "Resto", "valor": sum(e["valor"] for e in elementos[6:])}]}}
    return componer("informe_territorial_asuntos.html", t, _d(cifras, g), "informe_territorial", tema="lavanda", modulos=["mapa", "mapa_ccaa", "analiticos"])

def poster():
    t = dict(PIE_DEMO, TITULO_DOCUMENTO="Reclamar a tiempo recupera el 70 % de la deuda", TITULO_CORTO="Poster morosidad", ETIQUETA_SUPERIOR="Jornada de morosidad | Octubre de 2026",
             ENTRADILLA="Cuanto antes se requiere el pago, mas se cobra. Datos de las reclamaciones del despacho en 2026.", FUENTE_BREVE="datos ficticios de demostracion",
             CIFRA_1_ROTULO="deuda media reclamada por cliente", CIFRA_2_ROTULO="dias de media hasta cobrar", CIFRA_3_ROTULO="de la deuda recuperada sin juicio", TITULO_GRAFICO="La deuda crece mientras el cobro se estanca")
    cifras = {"cifra_1": {"valor": 42180, "unidad": "eur", "decimales": 0}, "cifra_2": {"valor": 214, "unidad": "entero"}, "cifra_3": {"valor": 70, "unidad": "pct"}}
    _, datos_panel_ = datos_panel()
    g = {"principal": dict(datos_panel_["graficos"]["evolucion"], fuente="demo")}
    return componer("poster_morosidad.html", t, _d(cifras, g), "poster", tema="nocturno", modulos=["encaje"])

NUEVAS = [cuadro_mando, ficha_una_pagina, infografia, comparativa, cronograma_expediente, lista_control, mapa_riesgos, escenarios, embudo_conversion, actividad_equipo, informe_territorial, poster]

# --------------------------------------------------------------------------- galeria de temas
TEMAS_GALERIA = [("moderno", "Moderno"), ("sobrio", "Sobrio"), ("editorial", "Editorial"), ("corporativo", "Corporativo"), ("minimal", "Minimal"),
                 ("nocturno", "Nocturno"), ("tecnico", "Tecnico"), ("calido", "Calido"), ("institucional", "Institucional"), ("pizarra", "Pizarra"),
                 ("suave", "Suave"), ("prensa", "Prensa"), ("alto_contraste", "Alto contraste"),
                 ("dorado", "Dorado"), ("esmeralda_noche", "Esmeralda nocturno"), ("ambar", "Ambar"), ("oliva_oro", "Oliva y oro"), ("lima", "Lima"),
                 ("menta", "Menta"), ("melocoton", "Melocoton"), ("lavanda", "Lavanda")]

def forzar_esquemas(html):
    """Solo para la galeria de temas: copia los bloques de tokens de modo que data-esquema="claro" u
    "oscuro" en la etiqueta html fuerce ese modo, sin depender del sistema. Los artefactos reales no lo llevan."""
    ini, fin = html.index("<style>") + 7, html.index("</style>")
    css, extra, i = html[ini:fin], [], 0
    cabeza = "@media (prefers-color-scheme:dark){"
    while True:
        j = css.find(cabeza, i)
        if j < 0:
            break
        k = m = j + len(cabeza); hondo = 1
        while hondo:
            hondo += {"{": 1, "}": -1}.get(css[m], 0); m += 1
        extra.append(css[k:m - 1].replace(":root", ':root[data-esquema="oscuro"]'))
        i = m
    for m in re.finditer(r'^(:root(?:\[data-tema="\w+"\])?)\{(.*?)\}', css, re.S | re.M):
        extra.append(m.group(1) + '[data-esquema="claro"]{' + m.group(2) + "}")
        if "color-scheme:dark" in m.group(2):  # tema siempre oscuro: el modo oscuro forzado no debe volver a los colores de la base
            extra.append(m.group(1) + '[data-esquema="oscuro"]{' + m.group(2) + "}")
    return html[:fin] + "\n/* Galeria: modos forzados */\n" + "\n".join(extra) + "\n" + html[fin:]

def galeria_temas():
    textos, datos = datos_panel()
    textos = dict(textos, TITULO_DOCUMENTO="Galeria de temas: el mismo panel con los %d estilos" % len(TEMAS_GALERIA), TITULO_CORTO="Galeria de temas",
                  ETIQUETA_SUPERIOR="Skill reportes | Catalogo de temas visuales",
                  ENTRADILLA="Elija un tema y un modo con los botones. El contenido es el del panel de ejemplo; lo que cambia es el bloque de estilos del tema, que en un artefacto real se copia una sola vez.")
    estilos = "\n".join(TEMAS[t] for t, _ in TEMAS_GALERIA if t in TEMAS) + """
.selector-temas{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;background:var(--superficie);border:1px solid var(--borde);
  border-radius:var(--radio-s);padding:10px 14px;margin:0 0 var(--e4);box-shadow:var(--sombra);font-size:.84rem}
.selector-temas .rotulo{text-transform:uppercase;letter-spacing:.08em;font-size:.7rem;color:var(--apagado)}
.selector-temas .botones{display:flex;flex-wrap:wrap;gap:6px}
.selector-temas button{padding:5px 11px;font-size:.8rem;box-shadow:none;border-radius:var(--radio-s)}
.selector-temas button[aria-pressed="true"]{background:var(--acento);color:var(--superficie);border-color:var(--acento)}
@media print{.selector-temas{display:none}}"""
    selector = """<div class="selector-temas" id="selector-temas">
    <span class="rotulo">Tema</span><div class="botones" id="botones-tema"></div>
    <span class="rotulo">Modo</span><div class="botones" id="botones-esquema"></div>
  </div>

  <header>"""
    script = """<script>
(function(){
"use strict";
var TEMAS = %s, ESQUEMAS = [["auto", "Sistema"], ["claro", "Claro"], ["oscuro", "Oscuro"]], H = document.documentElement, q = new URLSearchParams(location.search);
function boton(cont, id, texto, grupo) { var b = document.createElement("button"); b.type = "button"; b.textContent = texto; b.dataset[grupo] = id; cont.appendChild(b); return b; }
var bt = document.getElementById("botones-tema"), be = document.getElementById("botones-esquema");
TEMAS.forEach(function (t) { boton(bt, t[0], t[1], "tema").addEventListener("click", function () { aplicar(t[0], null); }); });
ESQUEMAS.forEach(function (e) { boton(be, e[0], e[1], "esquema").addEventListener("click", function () { aplicar(null, e[0]); }); });
function aplicar(tema, esquema) {
  if (tema) H.setAttribute("data-tema", tema);
  if (esquema) { if (esquema === "auto") H.removeAttribute("data-esquema"); else H.setAttribute("data-esquema", esquema); H.style.colorScheme = esquema === "auto" ? "" : esquema === "oscuro" ? "dark" : "light"; }
  var t = H.getAttribute("data-tema"), e = H.getAttribute("data-esquema") || "auto";
  [].forEach.call(bt.children, function (b) { b.setAttribute("aria-pressed", b.dataset.tema === t); });
  [].forEach.call(be.children, function (b) { b.setAttribute("aria-pressed", b.dataset.esquema === e); });
  if (window.Reportes) window.dispatchEvent(new Event("resize"));
}
aplicar(q.get("tema") || "moderno", q.get("esquema") || "auto");
})();
</script>""" % json.dumps(TEMAS_GALERIA, ensure_ascii=False)
    # Se compone a mano para incrustar todos los temas y el selector; forzar_esquemas no existe en los artefactos reales.
    html = BASE_HTML.replace("{{ANCHO}}", ANCHOS["panel_datos"]).replace("{{FICHA}}", PIEZAS[("panel_datos", "ficha")]).replace("{{CONTENIDO}}", PIEZAS[("panel_datos", "contenido")])
    html = html.replace("{{ESTILOS_MAQUETA}}", PIEZAS.get(("panel_datos", "estilos"), "")).replace("{{ACCIONES}}", "").replace("{{ESTILOS_TEMA}}", estilos)
    html = DATOS_VACIOS.sub(lambda m: m.group(1) + json.dumps(datos, ensure_ascii=False, indent=1) + m.group(2), html)
    html = html.replace("\n  <header>", "\n  " + selector, 1).replace("</body>", script + "\n</body>")
    for clave, valor in textos.items():
        html = html.replace("{{%s}}" % clave, valor)
    html = forzar_esquemas(html)
    pendientes = sorted(set(re.findall(r"\{\{(\w+)\}\}", html)))
    destino = "galeria_temas.html"
    open(os.path.join(AQUI, destino), "w", encoding="utf-8").write(html)
    print("  %-38s %6d bytes   pendientes: %s" % (destino, len(html.encode()), ", ".join(pendientes) or "ninguno"))
    return destino, not pendientes

# --------------------------------------------------------------------------- galeria de maquetas
FICHAS_MAQUETAS = [  # (archivo, maqueta, nombre, para que, familia)
 ("panel_reclamacion_cantidad", "panel_datos", "Panel de datos", "Indicadores y gráficos de un periodo o una cartera; seguimiento de facturación o deuda", "datos"),
 ("cuadro_mando_comite", "cuadro_mando", "Cuadro de mando", "Ocho KPIs con su variación, objetivos y estado por área; para el comité de dirección", "datos"),
 ("embudo_captacion", "embudo_conversion", "Embudo de conversión", "Un proceso por etapas y dónde se pierde; captación, recobro o tramitación", "datos"),
 ("informe_territorial_asuntos", "informe_territorial", "Informe territorial", "Datos por comunidad autónoma o provincia en un mapa, con ranking y concentración", "datos"),
 ("simulador_intereses_demora", "herramienta_interactiva", "Herramienta interactiva", "Calculadora o simulador que recalcula al cambiar los datos", "datos"),
 ("cronograma_expediente_0417", "cronograma_expediente", "Cronograma del expediente", "Qué ha pasado, qué plazo corre y qué viene; para el cliente que pregunta cómo va lo suyo", "seguimiento"),
 ("lista_control_rgpd", "lista_control", "Lista de control", "Cumplimiento por bloque y por requisito, con sus evidencias; auditorías y compliance", "seguimiento"),
 ("actividad_equipo_t3", "actividad_equipo", "Actividad del equipo", "Horas, asuntos y carga por área y por mes", "seguimiento"),
 ("informe_viabilidad_monitorio", "informe_visual", "Informe visual", "Un caso explicado con secciones, indicadores, plazos y cronología", "decision"),
 ("comparativa_vias", "comparativa", "Comparativa", "Dos a cuatro opciones frente a frente con los mismos criterios y la recomendada destacada", "decision"),
 ("mapa_riesgos_operacion", "mapa_riesgos", "Mapa de riesgos", "Matriz de probabilidad e impacto, impacto económico y exposición", "decision"),
 ("escenarios_indemnizacion", "escenarios", "Escenarios", "Qué pasa si cambian los supuestos: horquilla del resultado y qué lo mueve más", "decision"),
 ("resumen_reclamacion_una_pagina", "resumen_ejecutivo", "Resumen ejecutivo", "Una página A4 con la conclusión, tres cifras y la decisión que se pide", "pagina"),
 ("ficha_deudor_una_pagina", "ficha_una_pagina", "Ficha de una página", "Datos clave de un asunto, un cliente o una sociedad en una página A4", "pagina"),
 ("poster_morosidad", "poster", "Póster", "Una hoja A3 apaisada con tres cifras y un gráfico grande, para colgar", "pagina"),
 ("infografia_morosidad", "infografia", "Infografía", "Tres cifras enormes y gráficos sencillos en vertical, para divulgar", "comunicacion"),
 ("presentacion_reclamacion_cliente", "presentacion", "Presentación", "Diapositivas 16:9 con notas del orador para una reunión", "comunicacion"),
 ("white_paper_morosidad_pymes", "documento_largo", "Documento largo", "White paper o memoria con portada, índice y muchos gráficos", "comunicacion"),
]
FAMILIAS = [("todas", "Todas"), ("datos", "Datos"), ("seguimiento", "Seguimiento"), ("decision", "Riesgo y decision"), ("pagina", "Una pagina"), ("comunicacion", "Comunicacion")]

def miniaturas(archivos):
    """Captura cada ejemplo con Chrome sin ventana y lo reduce a 590 px de ancho en ejemplos/miniaturas."""
    try:
        from PIL import Image
    except ImportError:
        print("  PIL no disponible: no se generan miniaturas.")
        return
    if not os.path.exists(CHROME):
        return
    destino = os.path.join(AQUI, "miniaturas")
    os.makedirs(destino, exist_ok=True)
    def una(archivo):
        png = os.path.join(destino, archivo + ".png")
        with tempfile.TemporaryDirectory(prefix="reportes-chrome-") as perfil:
            try:  # un Chrome colgado deja ese ejemplo sin miniatura, no bloquea la generacion
                subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--user-data-dir=" + perfil, "--hide-scrollbars", "--window-size=1240,1000",
                                "--virtual-time-budget=3000", "--screenshot=" + png, "file://" + os.path.join(AQUI, archivo + ".html")], capture_output=True, check=False, timeout=90)
            except subprocess.TimeoutExpired:
                print("  AVISO: Chrome no termino la miniatura de %s" % archivo)
        if os.path.exists(png):
            im = Image.open(png).convert("RGB")
            im.resize((590, int(im.height * 590 / im.width)), Image.LANCZOS).save(png, optimize=True)
    with ThreadPoolExecutor(6) as hilos:
        list(hilos.map(una, archivos))
    print("  miniaturas: %d en ejemplos/miniaturas" % len(archivos))

def galeria_maquetas():
    import html as H
    filtro = "".join('<button type="button" data-familia="%s"%s>%s</button>' % (f, ' aria-pressed="true"' if f == "todas" else "", n) for f, n in FAMILIAS)
    tarjetas = []
    for archivo, maqueta, nombre, uso, familia in FICHAS_MAQUETAS:
        tema = re.search(r'data-tema="([\w-]+)"', open(os.path.join(AQUI, archivo + ".html"), encoding="utf-8").read()).group(1)
        tarjetas.append('<article class="tarjeta maqueta" data-familia="%s"><a href="%s.html"><img src="miniaturas/%s.png" alt="Ejemplo de %s" loading="lazy"></a>'
                        '<h2>%s</h2><p class="subtitulo">%s</p><p class="pie-maqueta"><code>%s</code> · tema <code>%s</code> · <a href="%s.html">HTML</a> · <a href="%s.pdf">PDF</a></p></article>'
                        % (familia, archivo, archivo, H.escape(nombre), H.escape(nombre), H.escape(uso), maqueta, tema, archivo, archivo))
    estilos = """.filtro{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 var(--e4)}
.filtro button{padding:6px 14px;font-size:.85rem;box-shadow:none}
.filtro button[aria-pressed="true"]{background:var(--acento);color:var(--superficie);border-color:var(--acento)}
.maquetas{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:var(--e3)}
.maqueta{padding:var(--e3)}
.maqueta img{display:block;width:100%;height:220px;object-fit:cover;object-position:top;border-radius:var(--radio-s);border:1px solid var(--borde);margin:0 0 var(--e3)}
.maqueta[hidden]{display:none}
.pie-maqueta{font-size:.78rem;color:var(--apagado);margin:0}
.otras{margin:var(--e5) 0 0}
@media print{.filtro{display:none}.maquetas{display:grid;grid-template-columns:repeat(3,1fr)}.maqueta{break-inside:avoid}.maqueta img{height:150px}}"""
    contenido = ('<div class="filtro" id="filtro">%s</div>\n  <div class="maquetas">%s</div>\n  <p class="otras">Mas galerias: <a href="galeria_temas.html">los 21 estilos</a> · '
                 '<a href="galeria_graficos.html">los 44 graficos</a>.</p>') % (filtro, "\n".join(tarjetas))
    script = """<script>
(function(){
"use strict";
var botones = document.querySelectorAll("#filtro button"), tarjetas = document.querySelectorAll(".maqueta");
[].forEach.call(botones, function (b) { b.addEventListener("click", function () {
  [].forEach.call(botones, function (x) { x.setAttribute("aria-pressed", x === b); });
  [].forEach.call(tarjetas, function (t) { t.hidden = b.dataset.familia !== "todas" && t.dataset.familia !== b.dataset.familia; });
}); });
})();
</script>"""
    textos = {"TITULO_DOCUMENTO": "Galeria de maquetas: %d reportes con datos de ejemplo" % len(FICHAS_MAQUETAS), "TITULO_CORTO": "Galeria de maquetas",
              "ETIQUETA_SUPERIOR": "Skill reportes | Catalogo de maquetas",
              "ENTRADILLA": "Cada maqueta responde a una pregunta distinta. Todas son reportes de datos; los documentos de texto se redactan en Markdown con su skill.",
              "PIE_AVISO_LEGAL": "Datos ficticios de demostracion."}
    html = BASE_HTML.replace("{{ANCHO}}", "1180px").replace("{{FICHA}}", '<li><b>Maquetas:</b> %d</li>' % len(FICHAS_MAQUETAS)).replace("{{CONTENIDO}}", contenido)
    html = html.replace("{{ESTILOS_MAQUETA}}", estilos).replace("{{ACCIONES}}", "").replace("{{ESTILOS_TEMA}}", "")
    html = DATOS_VACIOS.sub(lambda m: m.group(1) + json.dumps({"idioma": "es-ES", "moneda": "EUR", "fuentes": {}, "cifras": {}, "graficos": {}}) + m.group(2), html)
    html = html.replace("</body>", script + "\n</body>")
    for clave, valor in textos.items():
        html = html.replace("{{%s}}" % clave, valor)
    pendientes = sorted(set(re.findall(r"\{\{(\w+)\}\}", html)))
    open(os.path.join(AQUI, "galeria_maquetas.html"), "w", encoding="utf-8").write(html)
    print("  %-38s %6d bytes   pendientes: %s" % ("galeria_maquetas.html", len(html.encode()), ", ".join(pendientes) or "ninguno"))
    return "galeria_maquetas.html", not pendientes

# --------------------------------------------------------------------------- catalogo visual de la skill
def catalogo_visual():
    G = sys.modules[__name__]
    import html as H
    GAL = {c: dict(g) for c, t, u, g in G.GALERIA}
    GAL["chispa"] = {"tipo": "chispa", "valores": [10, 12, 18, 16, 24, 30, 34], "etiquetas": ["Abril", "Octubre"]}

    GRUPOS = [
     ("¿Qué es mayor?", [
      ("barras", "Barras", "Comparar partidas ordenadas de mayor a menor: facturas, deudores, áreas."),
      ("columnas", "Columnas", "Comparar pocos periodos o grupos, con una o varias series."),
      ("pareto", "Pareto", "Ver qué pocos deudores o causas concentran casi todo."),
      ("bala", "Bala", "Lo real frente al objetivo, con tramos de valoración."),
      ("halteras", "Halteras", "Lo pedido frente a lo concedido en cada partida."),
      ("pendiente", "Pendiente", "Cómo cambia cada partida entre dos momentos."),
      ("divergentes", "Divergentes", "Saldos a favor y en contra alrededor de cero.")]),
     ("¿Cómo evoluciona?", [
      ("linea", "Línea", "Evolución en el tiempo, con umbral legal y anotaciones."),
      ("area_apilada", "Área apilada", "Cómo se compone el total mes a mes."),
      ("escalones", "Escalones", "Valores que rigen a tramos, como el interés legal."),
      ("chispa", "Minigráfico", "La tendencia dentro de una cifra, sin ocupar sitio.")]),
     ("¿Qué peso tiene cada parte?", [
      ("anillo", "Anillo", "Tres o cuatro partes de un total, con la cifra en el centro."),
      ("tarta", "Tarta", "Reparto en hasta seis porciones."),
      ("apiladas", "Columnas apiladas", "Composición de cada periodo, con el total encima."),
      ("cien", "Apiladas al 100 %", "Proporción por periodo, cuando no importa el volumen."),
      ("treemap", "Treemap", "El peso de muchas partidas a la vez."),
      ("pictograma", "Pictograma", "Una proporción contada en figuras: «3 de cada 10».")]),
     ("¿Cuándo y qué plazo corre?", [
      ("plazos", "Diagrama de plazos", "Varios plazos en un mismo calendario, con la marca de hoy."),
      ("linea_tiempo", "Línea de tiempo", "Hitos del expediente sobre una escala real de fechas."),
      ("calendario", "Calendario de calor", "Qué días concentran vencimientos o actividad.")]),
     ("¿Cuánto llevamos y en qué estado?", [
      ("medidor", "Medidor", "Porcentaje consumido de un plazo o alcanzado de un objetivo."),
      ("progreso", "Progreso", "Avance por fase, con marca de objetivo."),
      ("anillos", "Anillos", "Avance de hasta cuatro objetivos a la vez."),
      ("semaforos", "Semáforos", "Estado de cada punto de control o requisito."),
      ("puntuacion", "Puntuación", "Nota de cada criterio en una escala corta.")]),
     ("¿Qué riesgo hay y qué conviene?", [
      ("matriz", "Matriz de riesgo", "Probabilidad por impacto, con lo que hay que hacer."),
      ("tornado", "Tornado", "Qué parámetro mueve más el resultado de una simulación."),
      ("rango", "Rango", "Dónde cae una cifra dentro de la horquilla legal."),
      ("radar", "Radar", "El perfil de cada opción en varios criterios.")]),
     ("¿Cómo se reparten los valores?", [
      ("histograma", "Histograma", "Cómo se reparten muchos valores sueltos, como días de demora."),
      ("cajas", "Cajas", "Mediana y dispersión por grupo, como días por juzgado."),
      ("dispersion", "Dispersión", "Relación entre dos magnitudes; las burbujas añaden una tercera."),
      ("mapa_calor", "Mapa de calor", "Dónde se concentra algo en dos dimensiones."),
      ("piramide", "Pirámide", "Dos grupos enfrentados por tramos.")]),
     ("¿Por dónde pasa y cómo se organiza?", [
      ("cascada", "Cascada", "Cómo se llega del principal al total, paso a paso."),
      ("embudo", "Embudo", "Cuántos llegan a cada etapa y cuántos se pierden."),
      ("sankey", "Sankey", "De dónde a dónde fluye un importe o un volumen."),
      ("flujo", "Diagrama de flujo", "Pasos de un procedimiento y dónde se decide."),
      ("sociedades", "Organigrama", "Estructura societaria o quién depende de quién."),
      ("partes", "Mapa de relaciones", "Qué relación tiene cada parte con el caso."),
      ("carriles", "Carriles", "Quién hace qué en cada momento.")]),
     ("¿Dónde, en el territorio?", [
      ("mapa", "Mapa por comunidades", "Concentración por comunidad autónoma, con tasas."),
      ("provincias", "Mapa por provincias", "Detalle provincial; sin dato, rayado."),
      ("qr", "Código QR", "Lleva al lector en papel a la fuente original.")]),
    ]

    graficos, secciones, n = {}, [], 0
    for num_grupo, (titulo, items) in enumerate(GRUPOS, 1):
        tarjetas = []
        for clave, nombre, uso in items:
            g = dict(GAL[clave], tabla=False, resumen=nombre + ": " + uso); g.pop("fuente", None)
            graficos[clave] = g; n += 1
            tarjetas.append('<article class="mini%s">' % (" ancha" if clave in ("sankey", "linea_tiempo", "plazos", "flujo", "carriles", "mapa_calor") else "") + '<div class="lienzo"><figure class="grafico" data-grafico="%s"></figure></div>'
                            '<h3>%s</h3><p>%s</p></article>' % (clave, H.escape(nombre), H.escape(uso)))
        secciones.append('<section class="grupo" id="grupo-%d"><h2>%s</h2><div class="minis">%s</div></section>' % (num_grupo, H.escape(titulo), "".join(tarjetas)))

    # muestras de estilo a partir de los tokens reales de cada tema
    base = G.BASE_HTML
    def tokens(bloque):
        return dict(re.findall(r"--([\w-]+):([^;]+);", bloque))
    temas = [("moderno", "Moderno", "Paneles y presentaciones", tokens(re.search(r":root\{(.*?)\}", base, re.S).group(1))),
             ("sobrio", "Sobrio", "Juzgado y cliente institucional", tokens(re.search(r':root\[data-tema="sobrio"\]\{(.*?)\}', base, re.S).group(1)))]
    USOS = {"editorial": "Documentos para imprimir", "corporativo": "Memorias y comités", "minimal": "Resúmenes de una página", "nocturno": "Proyectar en pantalla",
            "tecnico": "Auditorías y cumplimiento", "calido": "Particulares y familia", "institucional": "Administración y organismos", "pizarra": "Paneles densos",
            "suave": "Boletines y comunicación", "prensa": "Novedades normativas", "alto_contraste": "Accesibilidad", "dorado": "Prestigio y dirección", "esmeralda_noche": "Paneles en pantalla",
            "ambar": "Paneles operativos", "oliva_oro": "Rural y patrimonio", "lima": "Tecnología y datos", "menta": "Salud y particulares", "melocoton": "Familia y eventos", "lavanda": "Comunicación interna"}
    NOMBRES = {"tecnico": "Técnico", "calido": "Cálido", "alto_contraste": "Alto contraste", "esmeralda_noche": "Esmeralda nocturno", "ambar": "Ámbar", "oliva_oro": "Oliva y oro", "melocoton": "Melocotón"}
    for t, css in G.TEMAS.items():
        tok = tokens(re.search(r':root\[data-tema="%s"\]\{(.*?)\}' % t, css, re.S).group(1))
        temas.append((t, NOMBRES.get(t, t.capitalize()), USOS[t], tok))
    # la pregunta de estilo de SKILL.md (1.2) ofrece estos mismos temas, en este orden y con este nombre y uso
    form = json.loads(re.search(r"### 1\.2 Formulario.*?```json\n(.*?)\n```", open(os.path.join(SKILL, "SKILL.md"), encoding="utf-8").read(), re.S).group(1))
    opciones = [(o["id"], o["label"]) for q in form["form_data"] if q["id"] == "identidad_visual" for o in q["options"] if o["id"] != "tema_personalizado"]
    esperadas = [("tema_" + t, "%s: %s" % (nombre, uso[0].lower() + uso[1:])) for t, nombre, uso, _ in temas]
    if opciones != esperadas:
        print("  AVISO la pregunta identidad_visual de SKILL.md no coincide con los temas del catalogo; deberia ser:")
        for i, l in esperadas: print('        {"id": "%s", "label": "%s"},' % (i, l))
    muestras = []
    fuente_base = temas[0][3]["fuente"]  # la del tema moderno, ya leida de la base
    for t, nombre, uso, k in temas:
        fuente = k.get("fuente", fuente_base)
        barras = "".join('<i style="height:%d%%;background:%s"></i>' % (h, k["c%d" % (j + 1)]) for j, h in enumerate([92, 70, 54, 38, 26, 18]))
        muestras.append(('<article class="tema"><div class="papel" style="background:%s;font-family:%s">'
          '<div class="hoja" style="background:%s;border-color:%s;border-radius:%s;color:%s">'
          '<b style="color:%s">42.180 €</b><span style="color:%s">Principal reclamado</span><div class="muestra-barras">%s</div></div></div>'
          '<h3>%s</h3><p>%s</p></article>') % (k["fondo"], fuente, k["superficie"], k["borde"], k.get("radio", "12px"), k["texto"],
           k["acento"], k["apagado"], barras, H.escape(nombre), H.escape(uso)))

    estilos = """
    .intro{max-width:70ch}
    .bloque-titulo{font-size:.8rem;text-transform:uppercase;letter-spacing:.12em;color:var(--apagado);margin:var(--e5) 0 var(--e3);border-top:1px solid var(--borde);padding-top:var(--e4)}
    .temas{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:var(--e3)}
    .tema h3,.mini h3{font-size:.92rem;margin:var(--e2) 0 2px}
    .tema p,.mini p{font-size:.8rem;color:var(--apagado);margin:0}
    .papel{border-radius:10px;padding:12px;border:1px solid var(--borde)}
    .hoja{border:1px solid;padding:10px;display:flex;flex-direction:column;gap:2px;font-size:.7rem}
    .hoja b{font-size:1.05rem;letter-spacing:-.02em}
    .muestra-barras{display:flex;align-items:flex-end;gap:3px;height:38px;margin-top:6px}
    .muestra-barras i{flex:1;border-radius:2px}
    .mini.ancha{grid-column:span 2}
    @media (max-width:760px){.mini.ancha{grid-column:auto}}
    .mini.ancha .lienzo{height:230px}.mini.ancha .lienzo svg{max-height:216px}
    .grupo h2{font-size:1.05rem;margin:var(--e5) 0 var(--e3)}
    .minis{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:var(--e3)}
    .mini{background:var(--superficie);border:1px solid var(--borde);border-radius:var(--radio-s);padding:var(--e3);box-shadow:var(--sombra)}
    .lienzo{height:190px;overflow:hidden;display:flex;align-items:center;justify-content:center;background:var(--superficie-2);border-radius:8px;padding:6px}
    .lienzo .grafico{width:100%}
.lienzo:has(.barras){align-items:flex-start}
    .lienzo svg{max-height:176px;width:auto;margin:0 auto}
    .lienzo .leyenda,.lienzo .medidor-rotulo,.lienzo .semaforos-resumen,.lienzo ol.leyenda{display:none}
    .lienzo .semaforo{padding:3px 0;font-size:.72rem}.lienzo .semaforo .nota{display:none}
    .lienzo .fuente-grafico,.lienzo .datos-grafico{display:none}
    .formatos{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:var(--e3)}
    .formato img{display:block;width:100%;height:170px;object-fit:cover;object-position:top;border-radius:var(--radio-s);border:1px solid var(--borde)}
    .formato h3{font-size:.92rem;margin:var(--e2) 0 0}
    .formato p{font-size:.8rem;color:var(--texto-2);margin:4px 0 0;line-height:1.35}
    /* Modo compacto (?solo=...): iconos pequenos, a 760 px, para la ficha de la app. Los graficos y estilos van sin texto de uso; los formatos lo llevan debajo del nombre. */
    .compacto,.compacto body{background:transparent!important}  /* fondo transparente: las tarjetas se ven sobre la ficha clara u oscura */
    .compacto .contenedor{max-width:760px}
    .compacto .minis{grid-template-columns:repeat(auto-fill,minmax(128px,1fr));gap:10px}
    .compacto .mini{padding:8px;box-shadow:none}
    .compacto .mini p,.compacto .tema p{display:none}
    .compacto .mini h3,.compacto .tema h3,.compacto .formato h3{font-size:.76rem;text-align:center;margin:6px 0 0;font-weight:620}
    .compacto .lienzo,.compacto .mini.ancha .lienzo{height:86px;padding:4px}
    .compacto .lienzo svg,.compacto .mini.ancha .lienzo svg{max-height:78px}
    .compacto .lienzo:has(.barras) .grafico,.compacto .lienzo:has(.semaforos) .grafico{zoom:.42}
    .compacto .temas{grid-template-columns:repeat(7,minmax(0,1fr));gap:8px}
    .compacto .papel{padding:6px;border-radius:8px}
    .compacto .hoja{padding:6px;font-size:.5rem}
    .compacto .hoja b{font-size:.8rem}
    .compacto .muestra-barras{height:20px;margin-top:4px}
    .compacto .formatos{grid-template-columns:repeat(3,minmax(0,1fr));gap:10px 12px}
    .compacto .formato img{height:128px}
    .compacto .formato p{font-size:.66rem;text-align:center;margin-top:3px}
    """
    formatos = "".join('<article class="formato"><img src="miniaturas/%s.png" alt="Ejemplo de %s"><h3>%s</h3><p>%s</p></article>'
                       % (a, H.escape(nm), H.escape(nm), H.escape(uso)) for a, _, nm, uso, _ in FICHAS_MAQUETAS)
    contenido = ('<p class="intro">Cada gráfico con su aspecto real, su nombre y para qué sirve. '
      'Las miniaturas las dibuja el motor de la skill con datos de ejemplo; en el informe salen a tamaño completo, con su tabla de datos y su fuente.</p>'
      '<p class="bloque-titulo">Formatos · %d</p><div class="formatos" id="formatos">%s</div>'
      '<p class="bloque-titulo">Estilos · %d</p><div class="temas" id="temas">%s</div>'
      '<p class="bloque-titulo">Gráficos · %d, según la pregunta que responden</p>%s') % (len(FICHAS_MAQUETAS), formatos, len(temas), "".join(muestras), n, "".join(secciones))
    datos = {"idioma": "es-ES", "moneda": "EUR", "fuentes": {}, "cifras": dict({"pagado": {"valor": 2000}, "pagos": {"operacion": "producto", "a": "pagado", "b": -1}, "vencimiento_recurso": {"calculo": "vencimiento", "desde": "2026-09-17", "dias": 20, "festivos": ["2026-10-12"], "unidad": "fecha"}}), "graficos": graficos}
    textos = {"TITULO_DOCUMENTO": "Catálogo de estilos y gráficos", "TITULO_CORTO": "Catálogo Reportes", "ETIQUETA_SUPERIOR": "Skill Reportes | Qué puede elegir",
              "ENTRADILLA": "Elija un estilo para el aspecto del documento y los gráficos que respondan a sus preguntas. Puede pedirlos por su nombre en el chat.",
              "PIE_AVISO_LEGAL": "Datos ficticios de demostración."}
    html = G.BASE_HTML.replace("{{ANCHO}}", "1180px").replace("{{FICHA}}", "").replace("{{CONTENIDO}}", contenido)
    html = html.replace("{{ESTILOS_MAQUETA}}", estilos).replace("{{ACCIONES}}", "").replace("{{ESTILOS_TEMA}}", "")
    html = G.DATOS_VACIOS.sub(lambda m: m.group(1) + json.dumps(datos, ensure_ascii=False) + m.group(2), html)
    for mod in ["diagramas", "avanzados", "analiticos", "seguimiento", "qr", "plazos", "mapa", "mapa_ccaa", "mapa_provincias"]:
        html = html.replace("</body>", G.MODULOS[mod] + "\n</body>")
    html = html.replace("</body>", """<script>
    (function(){
    "use strict";
    /* ?solo=<id> deja solo ese bloque (un grupo de graficos o los estilos): es lo que se fotografia para la descripcion de la skill. */
    var solo = new URLSearchParams(location.search).get("solo"), D = document;
    if (!solo || !D.getElementById(solo)) return;
    D.documentElement.style.setProperty("--degradado", "none");
    var c = D.querySelector(".contenedor"), b = D.getElementById(solo);
    [].forEach.call(c.children, function (n) { if (!n.contains(b)) n.style.display = "none"; });
    c.style.padding = "16px";
    D.documentElement.classList.add("compacto");
    c.style.setProperty("--ancho", "760px");
var titulo = b.querySelector(":scope > h2");  /* el titulo del grupo ya va en el texto de la descripcion */
if (titulo) titulo.style.display = "none";
    })();
    </script>
    </body>""")
    for k, v in textos.items(): html = html.replace("{{%s}}" % k, v)
    pendientes = sorted(set(re.findall(r"\{\{(\w+)\}\}", html)))
    open(os.path.join(AQUI, "galeria_catalogo.html"), "w", encoding="utf-8").write(html)
    print("  %-38s %6d bytes   pendientes: %s" % ("galeria_catalogo.html", len(html.encode()), ", ".join(pendientes) or "ninguno"))
    return "galeria_catalogo.html", not pendientes, ["formatos", "temas"] + ["grupo-%d" % i for i in range(1, len(GRUPOS) + 1)]

def imagenes_catalogo(bloques):
    """Una imagen por bloque del catalogo (estilos y cada grupo de graficos) en ejemplos/catalogo: la
    descripcion de la skill las enlaza desde GitHub, porque la ficha de la app solo pinta imagenes por URL.
    Van a 760 px y en modo compacto: la ficha las pinta a su tamano natural, sin ampliarlas."""
    try:
        from PIL import Image
    except ImportError:
        print("  PIL no disponible: no se generan las imagenes del catalogo.")
        return
    destino = os.path.join(AQUI, "catalogo")
    os.makedirs(destino, exist_ok=True)
    def una(bloque):
        png = os.path.join(destino, bloque + ".png")
        with tempfile.TemporaryDirectory(prefix="reportes-chrome-") as perfil:
            try:
                subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--user-data-dir=" + perfil, "--hide-scrollbars", "--window-size=760,3000", "--default-background-color=00000000",
                                "--virtual-time-budget=4000", "--screenshot=" + png, "file://" + os.path.join(AQUI, "galeria_catalogo.html") + "?solo=" + bloque],
                               capture_output=True, check=False, timeout=90)
            except subprocess.TimeoutExpired:
                print("  AVISO: Chrome no termino la imagen %s" % bloque); return
        if not os.path.exists(png):
            print("  AVISO: Chrome no genero la imagen %s" % bloque); return
        im = Image.open(png).convert("RGBA")
        caja = im.getchannel("A").point(lambda v: 255 if v > 24 else 0).getbbox()  # lo transparente de abajo, sin contar sombras tenues
        if caja:
            im = im.crop((0, 0, im.width, min(im.height, caja[3] + 16)))
        im.save(png, optimize=True)
    with ThreadPoolExecutor(5) as hilos:
        list(hilos.map(una, bloques))
    print("  imagenes del catalogo: %d en ejemplos/catalogo" % len(bloques))

# --------------------------------------------------------------------------- comprobacion e impresion
def comprobar_y_imprimir(archivos, pdf):
    """Abre los ejemplos en Chrome sin ventana, en paralelo, y falla si la consola registra errores."""
    if not os.path.exists(CHROME):
        print("\nChrome no encontrado: no se comprueba la consola ni se generan PDF.")
        return True
    print("\nComprobando en Chrome%s:" % (" e imprimiendo a PDF" if pdf else ""))
    def abrir(archivo):
        ruta = os.path.join(AQUI, archivo)
        if pdf and os.path.exists(ruta.replace(".html", ".pdf")):
            os.remove(ruta.replace(".html", ".pdf"))  # un PDF viejo no debe pasar por uno nuevo
        with tempfile.TemporaryDirectory(prefix="reportes-chrome-") as perfil:
            orden = [CHROME, "--headless=new", "--disable-gpu", "--user-data-dir=" + perfil, "--enable-logging=stderr", "--v=0",
                     "--virtual-time-budget=3000", "--no-pdf-header-footer"]
            orden += ["--print-to-pdf=" + ruta.replace(".html", ".pdf")] if pdf else ["--dump-dom"]
            try:  # un Chrome colgado cuenta como error, no bloquea la generacion
                salida = subprocess.run(orden + ["file://" + ruta], capture_output=True, text=True, check=False, timeout=90)
            except subprocess.TimeoutExpired:
                return [":CONSOLE Chrome no termino en 90 s"]
        return [l for l in salida.stderr.splitlines() if ":CONSOLE" in l]
    with ThreadPoolExecutor() as hilos:
        resultados = list(hilos.map(abrir, archivos))
    for archivo, errores in zip(archivos, resultados):
        estado = "sin errores" if not errores else "%d errores de consola" % len(errores)
        if pdf:
            destino = os.path.join(AQUI, archivo.replace(".html", ".pdf"))
            estado += ", PDF de %d bytes" % os.path.getsize(destino) if os.path.exists(destino) else ", PDF NO GENERADO"
        print("  %-38s %s" % (archivo, estado))
        for e in errores:
            print("      " + e.split("CONSOLE")[-1][:200])
    sin_pdf = [a for a in archivos if pdf and not os.path.exists(os.path.join(AQUI, a.replace(".html", ".pdf")))]
    return not any(resultados) and not sin_pdf

# --------------------------------------------------------------------------- principal
if __name__ == "__main__":
    print("Generando artefactos de ejemplo:")
    hechos = [panel(), informe(), herramienta(), presentacion(), white_paper(), resumen()] + [f() for f in NUEVAS] + [galeria(), galeria_temas()]
    miniaturas([a for a, *_ in FICHAS_MAQUETAS])
    archivo_cat, ok_cat, bloques_cat = catalogo_visual()
    imagenes_catalogo(bloques_cat)
    hechos.append((archivo_cat, ok_cat))
    hechos.append(galeria_maquetas())
    limpio = comprobar_y_imprimir([d for d, _ in hechos], "--sin-pdf" not in sys.argv)
    if not all(ok for _, ok in hechos) or not limpio:
        print("\nFALLO: hay marcadores sin resolver o errores en la consola del navegador.")
        sys.exit(1)
    print("\nListo. El informe conserva {{LETRADO_RESPONSABLE}} a proposito: ejemplo de dato pendiente.")
