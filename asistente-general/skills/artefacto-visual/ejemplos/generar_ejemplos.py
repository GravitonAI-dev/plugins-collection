#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera los artefactos de ejemplo de la skill `artefacto-visual`.

Rellena las tres plantillas de `../assets` con un caso real (reclamacion de
cantidad) y compone ademas la galeria de graficos. Si encuentra Google Chrome,
imprime cada artefacto a PDF con el mismo motor que usara el navegador del
usuario.

Uso:   python3 generar_ejemplos.py          (HTML y PDF)
       python3 generar_ejemplos.py --sin-pdf
"""
import os, re, sys, math, socket, subprocess, threading, functools, http.server, socketserver

AQUI = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(AQUI, "..", "assets")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# --------------------------------------------------------------------------- utilidades de calculo
def y_cartesiana(valor, maximo):
    """Lienzo comun: cero en y=244, tope en y=44."""
    return round(244 - valor / maximo * 200, 1)

def puntos_linea(valores, maximo, x0=64, ancho=600):
    n = len(valores)
    return " ".join("%s,%s" % (round(x0 + i * ancho / (n - 1), 1), y_cartesiana(v, maximo))
                    for i, v in enumerate(valores))

def area_bajo(valores, maximo, x0=64, ancho=600):
    return puntos_linea(valores, maximo, x0, ancho) + " %s,244 %s,244" % (x0 + ancho, x0)

def chispa(valores, x0=1, ancho=118, alto=28, base=30):
    minimo, maximo = min(valores), max(valores)
    rango = (maximo - minimo) or 1
    n = len(valores)
    return " ".join("%s,%s" % (round(x0 + i * ancho / (n - 1), 1),
                               round(base - (v - minimo) / rango * alto, 1))
                    for i, v in enumerate(valores))

def chispa_area(valores):
    """El area bajo la linea: los mismos puntos mas los dos vertices del suelo."""
    return chispa(valores) + " 119,32 1,32"

def chispa_ultimo_y(valores):
    minimo, maximo = min(valores), max(valores)
    rango = (maximo - minimo) or 1
    return round(30 - (valores[-1] - minimo) / rango * 28, 1)

def arcos_anillo(porcentajes, radio=62):
    """Devuelve [(arco, resto, desplazamiento)] para cada porcion."""
    circunferencia = 2 * math.pi * radio
    salida, acumulado = [], 0.0
    for p in porcentajes:
        arco = p / 100 * circunferencia
        salida.append((round(arco, 1), round(circunferencia - arco, 1), round(-acumulado, 1)))
        acumulado += arco
    return salida

def arco_medidor(porcentaje, radio=90):
    longitud = math.pi * radio
    arco = porcentaje / 100 * longitud
    return round(arco, 1), round(longitud - arco, 1)

def cascada(pasos, maximo, base=240, alto_util=200):
    """pasos: [(rotulo, valor_inicial, valor_final)] -> geometria de cada columna."""
    salida = []
    for rotulo, ini, fin in pasos:
        techo = max(ini, fin)
        y = round(base - techo / maximo * alto_util, 1)
        alto = round(abs(fin - ini) / maximo * alto_util, 1)
        salida.append({"rotulo": rotulo, "y": y, "alto": alto, "etiqueta_y": round(y - 7, 1)})
    return salida

def eur(valor):
    entero, decimal = ("%.2f" % valor).split(".")
    grupos = ""
    while len(entero) > 3:
        grupos = "." + entero[-3:] + grupos
        entero = entero[:-3]
    return entero + grupos + "," + decimal + " EUR"

def rellenar(plantilla, destino, valores):
    origen = os.path.join(ASSETS, plantilla)
    texto = open(origen, encoding="utf-8").read()
    for clave, valor in valores.items():
        texto = texto.replace("{{%s}}" % clave, str(valor))
    # {{LETRADO_RESPONSABLE}} se deja a proposito en el informe: ejemplifica un dato
    # que el usuario decide no aportar y que debe quedar visible como marcador.
    pendientes = [m for m in sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", texto)))
                  if m != "{{LETRADO_RESPONSABLE}}"]
    ruta = os.path.join(AQUI, destino)
    open(ruta, "w", encoding="utf-8").write(texto)
    print("  %-38s %6d bytes   pendientes: %s" % (destino, len(texto), pendientes or "ninguno"))
    return len(pendientes) == 0

# --------------------------------------------------------------------------- datos del caso
PRINCIPAL, INTERESES, COSTAS = 42180.50, 1947.32, 3100.00
TOTAL = PRINCIPAL + INTERESES + COSTAS
SERIE_DEUDA = [12400, 21800, 28900, 36200, 42180.5]
SERIE_COBRO = [0, 2100, 2100, 5600, 5600]
EJE_MAX = 50000
UMBRAL = 15000

def panel():
    anillo = arcos_anillo([26, 38, 36])
    medidor = arco_medidor(70)
    columnas = cascada([("Principal", 0, PRINCIPAL),
                        ("Intereses", PRINCIPAL, PRINCIPAL + INTERESES),
                        ("Costas est.", PRINCIPAL + INTERESES, TOTAL),
                        ("Total", 0, TOTAL)], TOTAL)
    v = {
      "TITULO_ARTEFACTO": "La deuda se concentra en tres facturas de 2025",
      "ETIQUETA_SUPERIOR": "Reclamacion de cantidad | Expediente 2026/0417",
      "ENTRADILLA": "Situacion de la deuda de Construcciones Delta, S.L. a 24 de septiembre de 2026. Tres facturas concentran el 89 por ciento del principal y la mas antigua supera ya los 300 dias de demora.",
      "PERIODO": "enero a septiembre de 2026",
      "FUENTE_DATOS": "Mayor de clientes aportado por el cliente el 18/09/2026",
      "FECHA_ACTUALIZACION": "24 de septiembre de 2026",
      "INDICADOR_1_ROTULO": "Principal reclamado", "INDICADOR_1_CIFRA": eur(PRINCIPAL),
      "INDICADOR_1_DETALLE": "Siete facturas vencidas e impagadas",
      "CHISPA_PUNTOS": chispa(SERIE_DEUDA),
      "CHISPA_AREA": chispa_area(SERIE_DEUDA), "CHISPA_ULTIMO_Y": chispa_ultimo_y(SERIE_DEUDA),
      "CHISPA_NOTA": "Enero a septiembre: el principal se ha multiplicado por 3,4",
      "CHISPA_DESCRIPCION": "Tendencia del principal acumulado de enero a septiembre: al alza",
      "INDICADOR_2_ROTULO": "Intereses devengados", "INDICADOR_2_CIFRA": eur(INTERESES),
      "INDICADOR_2_DETALLE": "Interes legal del dinero hasta 24/09/2026",
      "INDICADOR_3_ROTULO": "Demora media", "INDICADOR_3_CIFRA": "214 dias",
      "INDICADOR_3_DETALLE": "Ponderada por importe de cada factura",
      "INDICADOR_4_ROTULO": "Importe cobrado", "INDICADOR_4_CIFRA": eur(5600),
      "INDICADOR_4_DETALLE": "Dos pagos parciales a cuenta",
      "TITULO_BARRAS": "Tres facturas concentran la deuda",
      "SUBTITULO_BARRAS": "Principal pendiente por documento, en euros",
      "BARRA_1_ROTULO": "Factura 2025/118", "BARRA_1_VALOR": eur(18400), "BARRA_1_PORCENTAJE": "100",
      "BARRA_2_ROTULO": "Factura 2025/131", "BARRA_2_VALOR": eur(11250), "BARRA_2_PORCENTAJE": "61.1",
      "BARRA_3_ROTULO": "Factura 2025/147", "BARRA_3_VALOR": eur(7930), "BARRA_3_PORCENTAJE": "43.1",
      "BARRA_4_ROTULO": "Resto (4 facturas)", "BARRA_4_VALOR": eur(4600.5), "BARRA_4_PORCENTAJE": "25.0",
      "TITULO_ANILLO": "Mas de un tercio supera los 180 dias",
      "SUBTITULO_ANILLO": "Reparto del principal por antiguedad de la deuda",
      "ANILLO_DESCRIPCION": "Reparto por antiguedad: hasta 90 dias 26 por ciento, de 91 a 180 dias 38 por ciento, mas de 180 dias 36 por ciento",
      "ANILLO_ARCO_1": anillo[0][0], "ANILLO_RESTO_1": anillo[0][1],
      "ANILLO_ARCO_2": anillo[1][0], "ANILLO_RESTO_2": anillo[1][1], "ANILLO_DESPLAZAMIENTO_2": anillo[1][2],
      "ANILLO_ARCO_3": anillo[2][0], "ANILLO_RESTO_3": anillo[2][1], "ANILLO_DESPLAZAMIENTO_3": anillo[2][2],
      "ANILLO_CIFRA_CENTRAL": "36%", "ANILLO_ROTULO_CENTRAL": "mas de 180 dias",
      "ANILLO_LEYENDA_1": "Hasta 90 dias (26%)", "ANILLO_LEYENDA_2": "De 91 a 180 dias (38%)",
      "ANILLO_LEYENDA_3": "Mas de 180 dias (36%)",
      "TITULO_EVOLUCION": "La deuda crece mientras el cobro se estanca",
      "SUBTITULO_EVOLUCION": "Principal acumulado frente a importe cobrado, en euros",
      "EVOLUCION_DESCRIPCION": "El principal acumulado pasa de 12.400 euros en enero a 42.180 en septiembre, mientras lo cobrado se detiene en 5.600 euros desde julio",
      "BANDA_Y": y_cartesiana(UMBRAL, EJE_MAX), "BANDA_ALTO": round(UMBRAL / EJE_MAX * 200, 1),
      "EJE_Y_4": "50.000", "EJE_Y_3": "37.500", "EJE_Y_2": "25.000", "EJE_Y_1": "12.500",
      "AREA_SERIE_1": area_bajo(SERIE_DEUDA, EJE_MAX),
      "PUNTOS_SERIE_1": puntos_linea(SERIE_DEUDA, EJE_MAX),
      "PUNTOS_SERIE_2": puntos_linea(SERIE_COBRO, EJE_MAX),
      "EJE_X_1": "Enero", "EJE_X_2": "Marzo", "EJE_X_3": "Mayo", "EJE_X_4": "Julio", "EJE_X_5": "Septiembre",
      "LEYENDA_SERIE_1": "Principal acumulado", "LEYENDA_SERIE_2": "Importe cobrado",
      "LEYENDA_BANDA": "Umbral de riesgo asumido (15.000 EUR)",
      "TITULO_CASCADA": "Del principal al total reclamable",
      "SUBTITULO_CASCADA": "Descomposicion de la cuantia de la demanda, en euros",
      "CASCADA_DESCRIPCION": "Principal 42.180,50 euros, intereses 1.947,32, costas estimadas 3.100, total 47.227,82",
      "CASCADA_1_Y": columnas[0]["y"], "CASCADA_1_ALTO": columnas[0]["alto"],
      "CASCADA_1_ROTULO": "Principal", "CASCADA_1_VALOR": "42.180", "CASCADA_1_ETIQUETA_Y": columnas[0]["etiqueta_y"],
      "CASCADA_2_Y": columnas[1]["y"], "CASCADA_2_ALTO": columnas[1]["alto"],
      "CASCADA_2_ROTULO": "Intereses", "CASCADA_2_VALOR": "1.947", "CASCADA_2_ETIQUETA_Y": columnas[1]["etiqueta_y"],
      "CASCADA_3_Y": columnas[2]["y"], "CASCADA_3_ALTO": columnas[2]["alto"],
      "CASCADA_3_ROTULO": "Costas est.", "CASCADA_3_VALOR": "3.100", "CASCADA_3_ETIQUETA_Y": columnas[2]["etiqueta_y"],
      "CASCADA_4_Y": columnas[3]["y"], "CASCADA_4_ALTO": columnas[3]["alto"],
      "CASCADA_4_ROTULO": "Total", "CASCADA_4_VALOR": "47.228", "CASCADA_4_ETIQUETA_Y": columnas[3]["etiqueta_y"],
      "TITULO_MEDIDOR": "El plazo del requerimiento vence en tres dias",
      "SUBTITULO_MEDIDOR": "Consumo del plazo concedido en el burofax de 17/09/2026",
      "MEDIDOR_DESCRIPCION": "Plazo del requerimiento consumido al 70 por ciento: siete dias de diez",
      "MEDIDOR_ARCO": medidor[0], "MEDIDOR_RESTO": medidor[1], "MEDIDOR_COLOR": "var(--aviso)",
      "MEDIDOR_CIFRA": "70%", "MEDIDOR_ROTULO": "del plazo consumido", "MEDIDOR_MAXIMO": "10 dias",
      "MEDIDOR_TITULO_NOTA": "Siguiente actuacion",
      "MEDIDOR_NOTA": "Agotado el plazo sin pago, procede presentar la peticion inicial de monitorio con el principal y los intereses devengados hasta la fecha de presentacion.",
      "TITULO_TABLA": "Detalle de facturas impagadas",
      "SUBTITULO_TABLA": "Ordenadas de mayor a menor antiguedad",
      "COLUMNA_1": "Documento", "COLUMNA_2": "Vencimiento", "COLUMNA_3": "Principal",
      "COLUMNA_4": "Dias", "COLUMNA_5": "Situacion",
      "FILA_1_C1": "Factura 2025/118", "FILA_1_C2": "15/11/2025", "FILA_1_C3": "18.400,00", "FILA_1_C4": "313", "FILA_1_C5": "Requerida",
      "FILA_2_C1": "Factura 2025/131", "FILA_2_C2": "20/01/2026", "FILA_2_C3": "11.250,00", "FILA_2_C4": "247", "FILA_2_C5": "Requerida",
      "FILA_3_C1": "Factura 2025/147", "FILA_3_C2": "28/03/2026", "FILA_3_C3": "7.930,00", "FILA_3_C4": "180", "FILA_3_C5": "Sin requerir",
      "TOTAL_ROTULO": "Total de las tres mayores", "TOTAL_C3": "37.580,00", "TOTAL_C4": "",
      "PIE_FUENTES": "Fuentes: mayor de clientes y facturas aportadas por el cliente el 18 de septiembre de 2026; calculo de intereses propio.",
      "PIE_AVISO_LEGAL": "Documento de trabajo. No sustituye al asesoramiento de un profesional colegiado ni a la liquidacion judicial de intereses.",
    }
    return rellenar("template-panel-datos.md", "panel_reclamacion_cantidad.html", v)

def informe():
    v = {
      "TITULO_ARTEFACTO": "El monitorio es la via mas rapida y economica",
      "ETIQUETA_SUPERIOR": "Informe de viabilidad | Expediente 2026/0417",
      "ENTRADILLA": "Analisis de las vias de reclamacion frente a Construcciones Delta, S.L. por un principal de 42.180,50 euros, con el detalle de plazos, costes y riesgos de cada alternativa.",
      "REFERENCIA_EXPEDIENTE": "2026/0417", "FECHA_EMISION": "24 de septiembre de 2026",
      "DESTINATARIO": "Suministros Ibericos del Norte, S.L.", "AUTOR": "Departamento de procesal civil",
      "INDICADOR_1_ROTULO": "Principal reclamable", "INDICADOR_1_CIFRA": eur(PRINCIPAL),
      "INDICADOR_1_DETALLE": "Mas 1.947,32 euros de intereses",
      "INDICADOR_2_ROTULO": "Plazo estimado", "INDICADOR_2_CIFRA": "2 a 4 meses",
      "INDICADOR_2_DETALLE": "Si no media oposicion del deudor",
      "INDICADOR_3_ROTULO": "Prescripcion mas proxima", "INDICADOR_3_CIFRA": "15/11/2030",
      "INDICADOR_3_DETALLE": "Factura 2025/118, accion personal",
      "TITULO_SECCION_1": "Antecedentes de hecho",
      "SUBTITULO_SECCION_1": "Hechos acreditados con la documentacion aportada",
      "CONTENIDO_SECCION_1": "Entre noviembre de 2025 y marzo de 2026 se emitieron siete facturas por suministro de material, todas ellas vencidas e impagadas. El deudor reconocio la deuda por correo electronico el 4 de mayo de 2026 y realizo dos pagos parciales a cuenta por importe conjunto de 5.600 euros, sin que desde julio se haya producido nuevo abono.",
      "TITULO_NOTA": "Reconocimiento de deuda",
      "CONTENIDO_NOTA": "El correo de 4 de mayo de 2026 interrumpe la prescripcion e integra el principio de prueba por escrito que sostiene la peticion inicial de monitorio.",
      "TITULO_SECCION_2": "Comparativa de vias de reclamacion",
      "SUBTITULO_SECCION_2": "Coste, plazo y probabilidad de cobro efectivo",
      "CONTENIDO_SECCION_2": "Se valoran tres alternativas atendiendo al coste de iniciarlas, al plazo previsible de resolucion y a la probabilidad de cobro efectivo una vez obtenido el titulo.",
      "TITULO_TABLA": "Vias disponibles y su valoracion",
      "COLUMNA_1": "Via", "COLUMNA_2": "Requisitos", "COLUMNA_3": "Plazo", "COLUMNA_4": "Viabilidad",
      "FILA_1_C1": "Monitorio", "FILA_1_C2": "Documento que acredite la deuda", "FILA_1_C3": "2 a 4 meses", "FILA_1_C4": "Alta",
      "FILA_2_C1": "Juicio ordinario", "FILA_2_C2": "Abogado y procurador", "FILA_2_C3": "12 a 18 meses", "FILA_2_C4": "Media",
      "FILA_3_C1": "Acuerdo extrajudicial", "FILA_3_C2": "Voluntad del deudor", "FILA_3_C3": "1 a 2 meses", "FILA_3_C4": "Incierta",
      "TITULO_SECCION_3": "Cronologia del expediente",
      "SUBTITULO_SECCION_3": "Hitos acreditados documentalmente",
      "CONTENIDO_SECCION_3": "La secuencia siguiente fija las fechas relevantes a efectos de prescripcion y de acreditacion de la deuda.",
      "HITO_1_FECHA": "15 de noviembre de 2025", "HITO_1_TITULO": "Vencimiento de la primera factura",
      "HITO_1_DETALLE": "Factura 2025/118 por 18.400,00 euros, impagada a su vencimiento.",
      "HITO_2_FECHA": "4 de mayo de 2026", "HITO_2_TITULO": "Reconocimiento de deuda",
      "HITO_2_DETALLE": "Correo del administrador del deudor aceptando el saldo y proponiendo calendario de pagos.",
      "HITO_3_FECHA": "17 de septiembre de 2026", "HITO_3_TITULO": "Burofax de requerimiento",
      "HITO_3_DETALLE": "Requerimiento fehaciente con acuse de recibo y plazo de diez dias para el pago.",
      "TITULO_SECCION_4": "Conclusion y hoja de ruta",
      "SUBTITULO_SECCION_4": "Actuaciones recomendadas y su orden",
      "CONTENIDO_SECCION_4": "Agotado el plazo del requerimiento sin pago, se recomienda acudir al procedimiento monitorio, que no exige abogado ni procurador para la peticion inicial y permite obtener titulo ejecutivo en pocos meses si el deudor no se opone.",
      "PASO_1": "Esperar al vencimiento del plazo del burofax y documentar la ausencia de pago.",
      "PASO_2": "Presentar peticion inicial de monitorio por el principal y los intereses devengados hasta la fecha de presentacion.",
      "PASO_3": "Si hay oposicion, valorar la transformacion en el declarativo que corresponda por la cuantia.",
      "TITULO_ADVERTENCIA": "Riesgo de oposicion",
      "CONTENIDO_ADVERTENCIA": "Si el deudor se opone en plazo, el asunto se transforma en el juicio declarativo que corresponda por la cuantia, con la consiguiente necesidad de abogado y procurador y un plazo sensiblemente mayor.",
      "FIRMA_1": "Preparado por: Departamento de procesal civil",
      "FIRMA_2": "Revisado por: {{LETRADO_RESPONSABLE}}",
      "PIE_FUENTES": "Fuentes: facturas y correspondencia aportadas por el cliente el 18 de septiembre de 2026.",
      "PIE_AVISO_LEGAL": "Documento de trabajo. No sustituye al asesoramiento de un profesional colegiado.",
    }
    return rellenar("template-informe-visual.md", "informe_viabilidad_monitorio.html", v)

def herramienta():
    calculo = """    var base = d.campo1;
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
    v = {
      "TITULO_ARTEFACTO": "Simulador de intereses de demora",
      "ETIQUETA_SUPERIOR": "Herramienta de apoyo | Expediente 2026/0417",
      "ENTRADILLA": "Calcule el importe total a reclamar ajustando el principal, el tipo aplicable y los dias transcurridos desde el vencimiento. El desglose se actualiza al instante.",
      "TITULO_PANEL_ENTRADA": "Parametros de calculo",
      "SUBTITULO_PANEL_ENTRADA": "Modifique cualquier campo para recalcular",
      "CAMPO_1_ROTULO": "Principal reclamado (EUR)", "CAMPO_1_VALOR_INICIAL": "42180.50",
      "CAMPO_1_AYUDA": "Suma de las facturas vencidas e impagadas.",
      "CAMPO_2_ROTULO": "Tipo de interes anual (%)", "CAMPO_2_VALOR_INICIAL": "3.25",
      "CAMPO_2_AYUDA": "Tipo pactado o, en su defecto, el interes legal del dinero vigente.",
      "CAMPO_3_ROTULO": "Dias transcurridos desde el vencimiento", "CAMPO_3_VALOR_INICIAL": "214",
      "CAMPO_3_AYUDA": "Demora media ponderada por importe de cada factura.",
      "CAMPO_4_ROTULO": "Naturaleza de la operacion",
      "CAMPO_4_AYUDA": "La operacion comercial entre empresas admite recargo adicional por morosidad.",
      "OPCION_1_VALOR": "civil", "OPCION_1_ROTULO": "Operacion civil ordinaria",
      "OPCION_2_VALOR": "comercial", "OPCION_2_ROTULO": "Operacion comercial entre empresas",
      "TITULO_VERIFICACION": "Documentacion previa",
      "SUBTITULO_VERIFICACION": "Verifique lo que ya obra en el expediente",
      "PUNTO_1": "Facturas emitidas y albaranes firmados", "PUNTO_1_DETALLE": "Acreditan la entrega y el importe reclamado.",
      "PUNTO_2": "Reconocimiento de deuda por escrito", "PUNTO_2_DETALLE": "Correo de 4 de mayo de 2026.",
      "PUNTO_3": "Justificantes de los pagos parciales", "PUNTO_3_DETALLE": "Dos transferencias por 5.600,00 euros.",
      "PUNTO_4": "Burofax de requerimiento con acuse", "PUNTO_4_DETALLE": "Remitido el 17 de septiembre de 2026.",
      "TITULO_PANEL_RESULTADO": "Resultado estimado",
      "SUBTITULO_PANEL_RESULTADO": "Calculo orientativo con los parametros introducidos",
      "MEDIDOR_DESCRIPCION": "Peso de los intereses y el recargo sobre el total a reclamar",
      "MEDIDOR_ROTULO": "intereses sobre el total",
      "RESULTADO_1_ROTULO": "Total a reclamar", "RESULTADO_2_ROTULO": "Intereses y recargo",
      "RESULTADO_3_ROTULO": "Dias computados",
      "TITULO_DESGLOSE": "Desglose del importe",
      "DESGLOSE_COLUMNA_1": "Concepto", "DESGLOSE_COLUMNA_2": "Importe", "DESGLOSE_COLUMNA_3": "Periodo",
      "DESGLOSE_TOTAL_ROTULO": "Total", "BLOQUE_CALCULO": calculo,
      "TITULO_SUPUESTOS": "Supuestos del calculo",
      "CONTENIDO_SUPUESTOS": "Interes simple calculado sobre el principal, con base de 365 dias por ano. El recargo por morosidad comercial se aplica al 0,4 por ciento anual adicional unicamente cuando se selecciona operacion entre empresas.",
      "TITULO_ADVERTENCIA": "Caracter orientativo",
      "CONTENIDO_ADVERTENCIA": "El importe definitivo depende del tipo efectivamente aplicable a cada factura y de la fecha real de presentacion de la demanda. La liquidacion definitiva corresponde al letrado director del asunto.",
      "PIE_FUENTES": "Fuentes: importes aportados por el cliente el 18 de septiembre de 2026.",
      "PIE_AVISO_LEGAL": "Documento de trabajo. No sustituye al asesoramiento de un profesional colegiado.",
    }
    return rellenar("template-herramienta-interactiva.md", "simulador_intereses_demora.html", v)

# --------------------------------------------------------------------------- galeria de graficos
def barras_verticales(valores, rotulos, maximo, color="var(--c1)"):
    n, partes = len(valores), []
    banda = 600.0 / n
    ancho = banda * 0.56
    for i, v in enumerate(valores):
        centro = 64 + banda * (i + 0.5)
        x = round(centro - ancho / 2, 1)
        y = y_cartesiana(v, maximo)
        partes.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" rx="3"></rect>'
                      % (x, y, round(ancho, 1), round(244 - y, 1), color))
        partes.append('<text class="eje" x="%s" y="264" text-anchor="middle">%s</text>'
                      % (round(centro, 1), rotulos[i]))
    return "\n        ".join(partes)

def barras_apiladas(series, rotulos, maximo, colores):
    n, partes = len(rotulos), []
    banda = 600.0 / n
    ancho = banda * 0.56
    for i in range(n):
        centro = 64 + banda * (i + 0.5)
        x = round(centro - ancho / 2, 1)
        acumulado = 0
        for k, serie in enumerate(series):
            valor = serie[i]
            y = y_cartesiana(acumulado + valor, maximo)
            alto = round(valor / maximo * 200, 1)
            partes.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s"></rect>'
                          % (x, y, round(ancho, 1), alto, colores[k]))
            acumulado += valor
        partes.append('<text class="eje" x="%s" y="264" text-anchor="middle">%s</text>'
                      % (round(centro, 1), rotulos[i]))
    return "\n        ".join(partes)

def gantt(plazos, dia_inicio, dia_fin, hoy, x0=150, ancho=520, y0=44, alto_fila=38):
    """plazos: [(rotulo, dia_desde, dia_hasta, color)] en dias desde dia_inicio."""
    total = dia_fin - dia_inicio
    x = lambda d: round(x0 + (d - dia_inicio) / total * ancho, 1)
    partes = []
    for i, (rotulo, desde, hasta, color) in enumerate(plazos):
        y = y0 + i * alto_fila
        partes.append('<text class="eje" x="%s" y="%s" text-anchor="end">%s</text>' % (x0 - 10, y + 13, rotulo))
        partes.append('<rect x="%s" y="%s" width="%s" height="18" rx="4" fill="%s"></rect>'
                      % (x(desde), y, round(x(hasta) - x(desde), 1), color))
    y_final = y0 + len(plazos) * alto_fila
    partes.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="var(--riesgo)" stroke-width="2" stroke-dasharray="4 3"></line>'
                  % (x(hoy), y0 - 14, x(hoy), y_final))
    partes.append('<text class="eje" x="%s" y="%s" text-anchor="middle" fill="var(--riesgo)">hoy</text>'
                  % (x(hoy), y0 - 20))
    return "\n        ".join(partes), x

def galeria():
    estilo = re.search(r"<style>.*?</style>", open(os.path.join(ASSETS, "template-panel-datos.md"),
                                                  encoding="utf-8").read(), re.S).group(0)
    anillo = arcos_anillo([44, 33, 23])
    medidor = arco_medidor(68)
    columnas = cascada([("Principal", 0, PRINCIPAL),
                        ("Intereses", PRINCIPAL, PRINCIPAL + INTERESES),
                        ("Costas est.", PRINCIPAL + INTERESES, TOTAL),
                        ("Total", 0, TOTAL)], TOTAL)
    trazos_gantt, escala_gantt = gantt(
        [("Requerimiento", 16, 26, "var(--aviso)"),
         ("Peticion monitorio", 27, 44, "var(--c1)"),
         ("Contestacion deudor", 45, 73, "var(--c3)"),
         ("Ejecucion prevista", 74, 105, "var(--c5)")],
        0, 121, 23)
    cuerpo = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Galeria de graficos</title>
%(estilo)s
<style>
.malla{display:grid;grid-template-columns:repeat(auto-fit,minmax(360px,1fr));gap:var(--e3);align-items:start}
.malla .ancho-total{grid-column:1/-1}
.formula{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.78rem;color:var(--apagado);
  background:var(--superficie-2);border:1px solid var(--borde-suave);border-radius:var(--radio-s);
  padding:var(--e2) var(--e3);margin:var(--e3) 0 0;white-space:pre-wrap}
.medidor .pista-arco{fill:none;stroke:var(--superficie-2);stroke-width:18;stroke-linecap:round}
.medidor .arco{fill:none;stroke-width:18;stroke-linecap:round}
.anillo circle{fill:none;stroke-width:24}
.anillo .base{stroke:var(--superficie-2)}
.centro-anillo{text-anchor:middle;fill:var(--texto);font-weight:670}
.cascada .conector{stroke:var(--linea-rejilla);stroke-width:1;stroke-dasharray:3 3}
.hoy{position:relative}
.hoy::after{content:"";position:absolute;top:-6px;bottom:-6px;left:62%%;width:2px;background:var(--riesgo)}
</style>
</head>
<body>
<main class="contenedor">

  <p class="borrador"><span><strong>DRAFT</strong> &mdash; Galeria de demostracion de la biblioteca de componentes de la skill. Los datos son ficticios y sirven unicamente para comprobar el renderizado de cada forma grafica.</span></p>

  <header>
    <p class="antetitulo">Skill artefacto-visual | Catalogo visual</p>
    <h1>Las diez formas graficas de la biblioteca</h1>
    <p class="entradilla">Cada tarjeta muestra una forma con datos de ejemplo y la formula exacta con la que se calculan sus coordenadas. Todo es SVG o CSS en linea: ni una sola dependencia externa.</p>
  </header>

  <div class="malla">

    <section class="tarjeta">
      <h2>1. Barras horizontales</h2>
      <p class="subtitulo">Comparar partidas. Solo exige el porcentaje sobre el mayor</p>
      <ul class="barras">
        <li><p class="fila"><span>Factura 2025/118</span><span class="valor">18.400,00 EUR</span></p>
          <div class="pista" role="img" aria-label="Factura 2025/118: 18.400 euros"><span style="width:100%%"></span></div></li>
        <li><p class="fila"><span>Factura 2025/131</span><span class="valor">11.250,00 EUR</span></p>
          <div class="pista" role="img" aria-label="Factura 2025/131: 11.250 euros"><span style="width:61.1%%"></span></div></li>
        <li><p class="fila"><span>Factura 2025/147</span><span class="valor">7.930,00 EUR</span></p>
          <div class="pista" role="img" aria-label="Factura 2025/147: 7.930 euros"><span style="width:43.1%%"></span></div></li>
      </ul>
      <p class="formula">porcentaje = valor / valor_maximo * 100</p>
    </section>

    <section class="tarjeta">
      <h2>2. Barras verticales</h2>
      <p class="subtitulo">Comparar pocas categorias con orden natural</p>
      <svg viewBox="0 0 700 300" role="img" aria-label="Importe reclamado por trimestre, de 8.200 a 18.400 euros">
        <line class="rejilla" x1="64" y1="44" x2="664" y2="44"></line>
        <line class="rejilla" x1="64" y1="144" x2="664" y2="144"></line>
        <line class="rejilla" x1="64" y1="244" x2="664" y2="244"></line>
        <text class="eje" x="56" y="48" text-anchor="end">20.000</text>
        <text class="eje" x="56" y="148" text-anchor="end">10.000</text>
        <text class="eje" x="56" y="248" text-anchor="end">0</text>
        %(verticales)s
      </svg>
      <p class="formula">banda = 600 / n ; ancho = banda * 0,56
x(i)  = 64 + banda * (i + 0,5) - ancho / 2
y(v)  = 244 - v / maximo * 200</p>
    </section>

    <section class="tarjeta">
      <h2>3. Barras apiladas</h2>
      <p class="subtitulo">Composicion de cada periodo</p>
      <svg viewBox="0 0 700 300" role="img" aria-label="Composicion trimestral entre principal, intereses y costas">
        <line class="rejilla" x1="64" y1="44" x2="664" y2="44"></line>
        <line class="rejilla" x1="64" y1="144" x2="664" y2="144"></line>
        <line class="rejilla" x1="64" y1="244" x2="664" y2="244"></line>
        <text class="eje" x="56" y="48" text-anchor="end">24.000</text>
        <text class="eje" x="56" y="248" text-anchor="end">0</text>
        %(apiladas)s
      </svg>
      <ul class="leyenda">
        <li><i style="background:var(--c1)"></i>Principal</li>
        <li><i style="background:var(--c2)"></i>Intereses</li>
        <li><i style="background:var(--c4)"></i>Costas estimadas</li>
      </ul>
      <p class="formula">y(k) = 244 - (acumulado(k) + valor(k)) / maximo * 200</p>
    </section>

    <section class="tarjeta ancho-total">
      <h2>4 y 5. Linea con area y banda de umbral</h2>
      <p class="subtitulo">Evolucion frente a un limite pactado</p>
      <svg viewBox="0 0 700 300" role="img" aria-label="El principal acumulado supera el umbral de 15.000 euros en febrero y llega a 42.180 en septiembre">
        <defs>
          <linearGradient id="degradado-area" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%%" stop-color="var(--c1)" stop-opacity=".34"></stop>
            <stop offset="100%%" stop-color="var(--c1)" stop-opacity="0"></stop>
          </linearGradient>
        </defs>
        <rect class="banda" x="64" y="%(banda_y)s" width="600" height="%(banda_alto)s"></rect>
        <line class="rejilla" x1="64" y1="44" x2="664" y2="44"></line>
        <line class="rejilla" x1="64" y1="144" x2="664" y2="144"></line>
        <line class="rejilla" x1="64" y1="244" x2="664" y2="244"></line>
        <text class="eje" x="56" y="48" text-anchor="end">50.000</text>
        <text class="eje" x="56" y="148" text-anchor="end">25.000</text>
        <text class="eje" x="56" y="248" text-anchor="end">0</text>
        <polygon class="area-1" points="%(area)s"></polygon>
        <polyline class="serie-1" points="%(serie1)s"></polyline>
        <polyline class="serie-2" points="%(serie2)s"></polyline>
        <text class="eje" x="64" y="266">Enero</text>
        <text class="eje" x="364" y="266" text-anchor="middle">Mayo</text>
        <text class="eje" x="664" y="266" text-anchor="end">Septiembre</text>
      </svg>
      <ul class="leyenda">
        <li><i style="background:var(--c1)"></i>Principal acumulado</li>
        <li><i style="background:var(--c2)"></i>Importe cobrado</li>
        <li><i style="background:var(--ok);opacity:.35"></i>Umbral asumido (15.000 EUR)</li>
      </ul>
      <p class="formula">area = puntos de la linea + "664,244 64,244"
banda: y = 244 - limite / maximo * 200</p>
    </section>

    <section class="tarjeta">
      <h2>6. Minigrafico de tendencia</h2>
      <p class="subtitulo">Cabe dentro de la tarjeta del indicador</p>
      <div class="indicadores">
        <div class="indicador">
          <p class="rotulo">Principal acumulado</p>
          <p class="cifra">42.180,50 EUR</p>
          <p class="detalle">Nueve meses consecutivos al alza</p>
          <svg class="chispa" viewBox="0 0 120 32" role="img" aria-label="Tendencia al alza durante nueve meses">
            <polyline class="serie-1" style="stroke-width:2" points="%(chispa)s"></polyline>
          </svg>
        </div>
      </div>
      <p class="formula">x(i) = 1 + i / (n - 1) * 118
y(v) = 30 - (v - minimo) / (maximo - minimo) * 28</p>
    </section>

    <section class="tarjeta">
      <h2>7. Medidor semicircular</h2>
      <p class="subtitulo">Plazo consumido o porcentaje de avance</p>
      <svg class="medidor" viewBox="0 0 240 150" role="img" aria-label="Plazo consumido al 68 por ciento">
        <path class="pista-arco" d="M 30 125 A 90 90 0 0 1 210 125"></path>
        <path class="arco" d="M 30 125 A 90 90 0 0 1 210 125" stroke="var(--aviso)" stroke-dasharray="%(medidor_arco)s %(medidor_resto)s"></path>
        <text x="120" y="112" text-anchor="middle" font-size="34" font-weight="670">68%%</text>
        <text class="eje" x="120" y="136" text-anchor="middle">del plazo consumido</text>
        <text class="eje" x="30" y="145" text-anchor="middle">0</text>
        <text class="eje" x="210" y="145" text-anchor="middle">20 dias</text>
      </svg>
      <p class="formula">longitud = pi * radio (90) = 282,7
arco = porcentaje / 100 * longitud</p>
    </section>

    <section class="tarjeta">
      <h2>8. Cascada de importes</h2>
      <p class="subtitulo">Del principal al total reclamable</p>
      <svg class="cascada" viewBox="0 0 460 280" role="img" aria-label="Principal 42.180, intereses 1.947, costas 3.100, total 47.228 euros">
        <line class="rejilla" x1="40" y1="240" x2="440" y2="240"></line>
        <rect x="52" y="%(c1y)s" width="72" height="%(c1a)s" fill="var(--c1)" rx="3"></rect>
        <rect x="152" y="%(c2y)s" width="72" height="%(c2a)s" fill="var(--c2)" rx="3"></rect>
        <rect x="252" y="%(c3y)s" width="72" height="%(c3a)s" fill="var(--c4)" rx="3"></rect>
        <rect x="352" y="%(c4y)s" width="72" height="%(c4a)s" fill="var(--acento-fuerte)" rx="3"></rect>
        <line class="conector" x1="124" y1="%(c1y)s" x2="152" y2="%(c1y)s"></line>
        <line class="conector" x1="224" y1="%(c2y)s" x2="252" y2="%(c2y)s"></line>
        <line class="conector" x1="324" y1="%(c3y)s" x2="352" y2="%(c3y)s"></line>
        <text class="eje" x="88" y="258" text-anchor="middle">Principal</text>
        <text class="eje" x="188" y="258" text-anchor="middle">Intereses</text>
        <text class="eje" x="288" y="258" text-anchor="middle">Costas est.</text>
        <text class="eje" x="388" y="258" text-anchor="middle">Total</text>
        <text class="eje" x="88" y="%(c1e)s" text-anchor="middle">42.180</text>
        <text class="eje" x="188" y="%(c2e)s" text-anchor="middle">1.947</text>
        <text class="eje" x="288" y="%(c3e)s" text-anchor="middle">3.100</text>
        <text class="eje" x="388" y="%(c4e)s" text-anchor="middle">47.228</text>
      </svg>
      <p class="formula">alto(k) = |fin - inicio| / total * 200
y(k)    = 240 - mayor(inicio, fin) / total * 200</p>
    </section>

    <section class="tarjeta">
      <h2>9. Matriz de riesgo e impacto</h2>
      <p class="subtitulo">Que contingencias urgen</p>
      <svg viewBox="0 0 420 300" role="img" aria-label="Dos contingencias en probabilidad alta: oposicion del deudor con impacto alto e insolvencia con impacto medio">
        <rect x="120" y="40" width="130" height="80" fill="var(--aviso)" opacity=".16"></rect>
        <rect x="250" y="40" width="130" height="80" fill="var(--riesgo)" opacity=".20"></rect>
        <rect x="120" y="120" width="130" height="80" fill="var(--ok)" opacity=".16"></rect>
        <rect x="250" y="120" width="130" height="80" fill="var(--aviso)" opacity=".16"></rect>
        <text class="eje" x="185" y="84" text-anchor="middle">Vigilar</text>
        <text class="eje" x="315" y="84" text-anchor="middle">Actuar ya</text>
        <text class="eje" x="185" y="164" text-anchor="middle">Asumible</text>
        <text class="eje" x="315" y="164" text-anchor="middle">Preparar plan</text>
        <text class="eje" x="112" y="84" text-anchor="end">Probabilidad alta</text>
        <text class="eje" x="112" y="164" text-anchor="end">Probabilidad baja</text>
        <text class="eje" x="185" y="222" text-anchor="middle">Impacto medio</text>
        <text class="eje" x="315" y="222" text-anchor="middle">Impacto alto</text>
        <circle cx="300" cy="62" r="9" fill="var(--c4)"></circle>
        <text x="300" y="66" text-anchor="middle" font-size="11" font-weight="670" fill="#fff">1</text>
        <circle cx="170" cy="62" r="9" fill="var(--c5)"></circle>
        <text x="170" y="66" text-anchor="middle" font-size="11" font-weight="670" fill="#fff">2</text>
      </svg>
      <ul class="leyenda">
        <li><i style="background:var(--c4);border-radius:50%%"></i>1. Oposicion del deudor al monitorio</li>
        <li><i style="background:var(--c5);border-radius:50%%"></i>2. Insolvencia sobrevenida</li>
      </ul>
      <p class="formula">tres o cuatro niveles por eje, nunca mas</p>
    </section>

    <section class="tarjeta ancho-total">
      <h2>10. Diagrama de plazos con marca de hoy</h2>
      <p class="subtitulo">Calendario compartido de septiembre a diciembre de 2026; la linea roja es la fecha de hoy</p>
      <svg viewBox="0 0 700 210" role="img" aria-label="El requerimiento vence el 27 de septiembre, la peticion de monitorio se presenta a finales de septiembre, la contestacion corre hasta el 13 de noviembre y la ejecucion se preveria en diciembre">
        %(gantt)s
        <line class="rejilla" x1="150" y1="182" x2="670" y2="182"></line>
        <text class="eje" x="150" y="198">1 sep</text>
        <text class="eje" x="%(mes2)s" y="198" text-anchor="middle">1 oct</text>
        <text class="eje" x="%(mes3)s" y="198" text-anchor="middle">1 nov</text>
        <text class="eje" x="670" y="198" text-anchor="end">31 dic</text>
      </svg>
      <p class="formula">x(fecha) = x0 + (fecha - inicio) / (fin - inicio) * ancho
la marca de hoy cruza todas las filas: la escala es comun</p>
    </section>

    <section class="tarjeta">
      <h2>11. Anillo de reparto</h2>
      <p class="subtitulo">Peso de cada parte sobre el total</p>
      <svg class="anillo" viewBox="0 0 230 190" role="img" aria-label="Reparto: suministro 44 por ciento, maquinaria 33, transporte 23">
        <g transform="translate(115,95) rotate(-90)">
          <circle class="base" cx="0" cy="0" r="62"></circle>
          <circle cx="0" cy="0" r="62" stroke="var(--c1)" stroke-dasharray="%(a1)s %(r1)s" stroke-dashoffset="0"></circle>
          <circle cx="0" cy="0" r="62" stroke="var(--c2)" stroke-dasharray="%(a2)s %(r2)s" stroke-dashoffset="%(d2)s"></circle>
          <circle cx="0" cy="0" r="62" stroke="var(--c3)" stroke-dasharray="%(a3)s %(r3)s" stroke-dashoffset="%(d3)s"></circle>
        </g>
        <text class="centro-anillo" x="115" y="92" font-size="27">44%%</text>
        <text class="centro-anillo eje" x="115" y="112" font-size="11">suministro</text>
      </svg>
      <ul class="leyenda">
        <li><i style="background:var(--c1)"></i>Suministro (44%%)</li>
        <li><i style="background:var(--c2)"></i>Maquinaria (33%%)</li>
        <li><i style="background:var(--c3)"></i>Transporte (23%%)</li>
      </ul>
      <p class="formula">C = 2 * pi * 62 = 389,6
arco = porcentaje / 100 * C ; desplazamiento = -acumulado</p>
    </section>

  </div>

  <div class="acciones">
    <button type="button" id="imprimir">Imprimir o guardar en PDF</button>
  </div>

  <footer class="pie">
    <p>Galeria de demostracion de la skill artefacto-visual. Datos ficticios.</p>
  </footer>

</main>
<script>
document.getElementById("imprimir").addEventListener("click", function(){ window.print(); });
</script>
</body>
</html>
""" % {
      "estilo": estilo,
      "verticales": barras_verticales([8200, 12400, 18400, 15900, 11250], ["1T 2025", "2T 2025", "3T 2025", "4T 2025", "1T 2026"], 20000),
      "apiladas": barras_apiladas([[8200, 12400, 18400], [320, 640, 1180], [600, 900, 1400]],
                                  ["1T", "2T", "3T"], 24000,
                                  ["var(--c1)", "var(--c2)", "var(--c4)"]),
      "banda_y": y_cartesiana(UMBRAL, EJE_MAX), "banda_alto": round(UMBRAL / EJE_MAX * 200, 1),
      "area": area_bajo(SERIE_DEUDA, EJE_MAX),
      "serie1": puntos_linea(SERIE_DEUDA, EJE_MAX),
      "serie2": puntos_linea(SERIE_COBRO, EJE_MAX),
      "chispa": chispa(SERIE_DEUDA),
      "gantt": trazos_gantt,
      "mes2": escala_gantt(30), "mes3": escala_gantt(61),
      "medidor_arco": medidor[0], "medidor_resto": medidor[1],
      "c1y": columnas[0]["y"], "c1a": columnas[0]["alto"], "c1e": columnas[0]["etiqueta_y"],
      "c2y": columnas[1]["y"], "c2a": columnas[1]["alto"], "c2e": columnas[1]["etiqueta_y"],
      "c3y": columnas[2]["y"], "c3a": columnas[2]["alto"], "c3e": columnas[2]["etiqueta_y"],
      "c4y": columnas[3]["y"], "c4a": columnas[3]["alto"], "c4e": columnas[3]["etiqueta_y"],
      "a1": anillo[0][0], "r1": anillo[0][1],
      "a2": anillo[1][0], "r2": anillo[1][1], "d2": anillo[1][2],
      "a3": anillo[2][0], "r3": anillo[2][1], "d3": anillo[2][2],
    }
    ruta = os.path.join(AQUI, "galeria_graficos.html")
    open(ruta, "w", encoding="utf-8").write(cuerpo)
    print("  %-38s %6d bytes   pendientes: ninguno" % ("galeria_graficos.html", len(cuerpo)))
    return True

# --------------------------------------------------------------------------- impresion a PDF
def imprimir_pdf(archivos):
    if not os.path.exists(CHROME):
        print("\nChrome no encontrado: se omite la generacion de PDF.")
        return
    puerto = socket.socket(); puerto.bind(("127.0.0.1", 0))
    numero = puerto.getsockname()[1]; puerto.close()
    manejador = functools.partial(http.server.SimpleHTTPRequestHandler, directory=AQUI)
    servidor = socketserver.TCPServer(("127.0.0.1", numero), manejador)
    hilo = threading.Thread(target=servidor.serve_forever, daemon=True); hilo.start()
    print("\nImprimiendo a PDF:")
    try:
        for archivo in archivos:
            salida = os.path.join(AQUI, archivo.replace(".html", ".pdf"))
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=3000",
                            "--no-pdf-header-footer", "--print-to-pdf=" + salida,
                            "http://127.0.0.1:%d/%s" % (numero, archivo)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
            hecho = os.path.exists(salida)
            print("  %-38s %s" % (os.path.basename(salida),
                                  "%d bytes" % os.path.getsize(salida) if hecho else "ERROR"))
    finally:
        servidor.shutdown()

# --------------------------------------------------------------------------- principal
if __name__ == "__main__":
    print("Generando artefactos de ejemplo:")
    completos = [panel(), informe(), herramienta(), galeria()]
    if not all(completos):
        print("\nAviso: algun artefacto conserva marcadores sin resolver.")
    else:
        print("  (el informe conserva {{LETRADO_RESPONSABLE}} a proposito: ejemplo de dato pendiente)")
    if "--sin-pdf" not in sys.argv:
        imprimir_pdf(["panel_reclamacion_cantidad.html", "informe_viabilidad_monitorio.html",
                      "simulador_intereses_demora.html", "galeria_graficos.html"])
    print("\nListo. Abre cualquiera de los .html con doble clic.")
