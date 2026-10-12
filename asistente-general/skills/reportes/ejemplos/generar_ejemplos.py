#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera los reportes de ejemplo de la skill `reportes`.

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
BASE_HTML = open(BASE, encoding="utf-8").read()

def componer(destino, textos, datos, maqueta=None, tema="moderno", ficha=None, contenido=None, ancho=None, modulos=()):
    """Compone un ejemplo como lo hara el modelo: base, partes de la maqueta y datos."""
    parte = lambda nombre: PIEZAS.get((maqueta, nombre), "")
    html = BASE_HTML.replace('data-tema="moderno"', 'data-tema="%s"' % tema)
    html = html.replace("{{ANCHO}}", ancho or ANCHOS[maqueta])
    html = html.replace("{{FICHA}}", ficha or parte("ficha")).replace("{{CONTENIDO}}", contenido or parte("contenido"))
    html = html.replace("{{ESTILOS_MAQUETA}}", parte("estilos")).replace("{{ACCIONES}}", parte("acciones"))
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
PRINCIPAL, INTERESES, COSTAS = 42180.50, 1947.32, 3100.00
COMUN = {"PIE_AVISO_LEGAL": "Documento de trabajo. No sustituye al asesoramiento de un profesional colegiado ni a la liquidacion judicial de intereses."}

def panel():
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
                        "elementos": [{"rotulo": r, "valor": v} for r, v in FACTURAS]},
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
        "facturas": {"tipo": "barras", "unidad": "eur", "fuente": "cliente", "elementos": [{"rotulo": r, "valor": v} for r, v in FACTURAS],
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

# --------------------------------------------------------------------------- galeria
FLUJO_MONITORIO = {"tipo": "diagrama", "disposicion": "capas", "grupos": {"1": "Via judicial", "2": "Cierre", "3": "Hechos"},
  "nodos": [{"id": "contrato", "texto": "Contrato de suministro", "forma": "inicio"}, {"id": "impago", "texto": "Impago de siete facturas", "grupo": 3},
            {"id": "pago", "texto": "¿Paga en el plazo del requerimiento?", "forma": "decision"}, {"id": "fin", "texto": "Archivo del expediente", "forma": "inicio", "grupo": 2},
            {"id": "monitorio", "texto": "Peticion de monitorio", "grupo": 1}],
  "conexiones": [{"de": "contrato", "a": "impago"}, {"de": "impago", "a": "pago", "texto": "burofax"}, {"de": "pago", "a": "fin", "texto": "si"},
                 {"de": "pago", "a": "monitorio", "texto": "no", "estilo": "destacada"}]}

GALERIA = [
  ("barras", "Barras horizontales", "Comparar partidas. Ordenadas de mayor a menor.",
   {"tipo": "barras", "unidad": "eur", "elementos": [{"rotulo": r, "valor": v} for r, v in FACTURAS]}),
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
  ("plazos", "Diagrama de plazos", "Varios plazos en una escala comun, con la marca de hoy.",
   {"tipo": "plazos", "hoy": "2026-09-20", "plazos": [{"rotulo": "Recurso de reposicion", "inicio": "2026-08-01", "fin": "2026-08-20"},
     {"rotulo": "Requerimiento", "inicio": "2026-09-01", "fin": "2026-09-27"},
     {"rotulo": "Contestacion a la demanda", "inicio": "2026-10-01", "fin": "2026-11-13"},
     {"rotulo": "Negociacion con la contraria", "inicio": "2026-09-10"},
     {"rotulo": "Vista prevista", "inicio": "2026-12-01", "fin": "2026-12-15", "aproximada": True}]}),
]

def galeria():
    graficos, tarjetas = {}, []
    for clave, titulo, uso, g in GALERIA:
        g = dict(g, fuente="ejemplo", resumen=titulo + ": " + uso)
        graficos[clave] = g
        ancho = " ancho-total" if clave in ("linea", "plazos", "flujo", "sociedades", "partes", "carriles", "bala", "divergentes") else ""
        tarjetas.append('<section class="tarjeta%s">\n      <h2>%s</h2>\n      <p class="subtitulo">%s <code>"tipo": "%s"</code></p>\n'
                        '      <figure class="grafico" data-grafico="%s"></figure>\n    </section>' % (ancho, titulo, uso, g["tipo"], clave))
    graficos["tendencia"] = {"tipo": "chispa", "valores": [10, 12, 18, 22, 30, 34], "etiquetas": ["Abril", "Septiembre"], "fuente": "ejemplo"}
    datos = {"idioma": "es-ES", "moneda": "EUR", "cifras": {"total": {"de": "cascada", "calculo": "suma", "unidad": "eur"},
                                                           "pagado": {"valor": 2000}, "pagos": {"operacion": "producto", "a": "pagado", "b": -1}},
             "fuentes": {"ejemplo": {"nombre": "Datos ficticios de demostracion", "consulta": "2026-10-11"}}, "graficos": graficos}
    contenido = ('<div class="indicadores">\n    <div class="indicador">\n      <p class="rotulo">Indicador con minigrafico</p>\n'
                 '      <p class="cifra" data-cifra="total"></p>\n      <p class="detalle">La cifra sale del grafico de cascada</p>\n'
                 '      <div class="tendencia" data-grafico="tendencia"></div>\n    </div>\n  </div>\n\n  <div class="malla">\n    '
                 + "\n    ".join(tarjetas) + "\n  </div>")
    textos = dict(COMUN, **{
      "TITULO_DOCUMENTO": "Galeria de graficos del motor de reportes",
      "ETIQUETA_SUPERIOR": "Skill reportes | Catalogo de formas",
      "ENTRADILLA": "Cada grafico se declara con sus datos en el bloque datos-reporte y lo dibuja el motor de la base. Bajo cada uno estan su tabla de datos, la descarga en CSV y su fuente.",
    })
    return componer("galeria_graficos.html", textos, datos, ficha='<li><b>Tipos:</b> %d</li>' % len(GALERIA),
                    contenido=contenido, ancho="1120px", modulos=["diagramas"])

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
            salida = subprocess.run(orden + ["file://" + ruta], capture_output=True, text=True, check=False)
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
    print("Generando reportes de ejemplo:")
    hechos = [panel(), informe(), herramienta(), presentacion(), galeria()]
    limpio = comprobar_y_imprimir([d for d, _ in hechos], "--sin-pdf" not in sys.argv)
    if not all(ok for _, ok in hechos) or not limpio:
        print("\nFALLO: hay marcadores sin resolver o errores en la consola del navegador.")
        sys.exit(1)
    print("\nListo. El informe conserva {{LETRADO_RESPONSABLE}} a proposito: ejemplo de dato pendiente.")
