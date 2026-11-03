# Maquetas de reportes

Una maqueta es la estructura de un tipo de reporte: sus partes (`ficha`, `contenido`, `estilos`, `script`, `acciones`) y el esqueleto de su bloque de datos. El archivo lo monta el servidor con `create_file_from_skill_document` sobre la base `template-base-reportes.md`: cada parte se trae con `fragments` (`{"FICHA": "maquetas-codigo.md#<id>/ficha", "CONTENIDO": "maquetas-codigo.md#<id>/contenido", "ESTILOS_MAQUETA": "maquetas-codigo.md#<id>/estilos", "SCRIPT_MAQUETA": "maquetas-codigo.md#<id>/script", "ACCIONES": "maquetas-codigo.md#<id>/acciones"}`, solo las partes que la maqueta tiene; `ESTILOS_MAQUETA`, `SCRIPT_MAQUETA` y `ACCIONES` van en `remove` cuando no la tiene), los marcadores `{{…}}` se rellenan con `values` (`ANCHO` con el ancho de la maqueta) y el bloque `datos-reporte` inicial se sustituye con `replace` por los datos del caso, partiendo del ejemplo de la maqueta. El código de las partes no se lee ni se reescribe: vive en `maquetas-codigo.md` y lo copia el servidor.

Reglas comunes: los gráficos no se dibujan; en el HTML solo hay huecos `<figure class="grafico" data-grafico="nombre"></figure>` y en `datos-reporte.graficos` se declara cada nombre con su `tipo` (contrato en `catalogo-graficos.md`; todos los tipos vienen en la base). Cualquier hueco admite cualquier tipo, y los bloques se pueden repetir, quitar o reordenar sin renombrar clases. Las cifras del texto que salen de un gráfico van en `<span data-cifra="clave"></span>` y se declaran en `cifras`. Una línea de la ficha cuyo dato no esencial falta se quita; un dato esencial se pregunta; un marcador `{{VARIABLE}}` solo queda para lo que el usuario decidió no dar. `TITULO_CORTO` es el nombre de la pestaña y del PDF; `TITULO_DOCUMENTO`, el titular que afirma.

## Índice de maquetas

Todas son reportes (cifras y gráficos que se ven en el navegador y se imprimen); los documentos de texto se redactan en Markdown con su skill.

| `id` | Maqueta | Para qué | Partes |
| :--- | :--- | :--- | :--- |
| `panel_datos` | Panel de datos | Indicadores y gráficos de un periodo o una cartera | ficha, contenido |
| `informe_visual` | Informe visual | Un caso explicado con secciones, indicadores, plazos y cronología | ficha, estilos, contenido |
| `herramienta_interactiva` | Herramienta interactiva | Calculadora o simulador que recalcula al cambiar los datos | ficha, estilos, acciones, contenido, script |
| `presentacion` | Presentación | Diapositivas 16:9 con notas del orador | ficha, estilos, contenido, script |
| `documento_largo` | Documento largo | White paper o memoria con portada, índice y muchos gráficos | ficha, estilos, contenido, script |
| `resumen_ejecutivo` | Resumen ejecutivo | Una página A4 con la conclusión, tres cifras y la decisión que se pide | ficha, estilos, contenido |
| `cuadro_mando` | Cuadro de mando | Ocho KPIs con variación, objetivos y estado por área, para dirección | ficha, estilos, contenido |
| `ficha_una_pagina` | Ficha de una página | Datos clave de un asunto, un cliente o una sociedad en una página | ficha, estilos, contenido |
| `infografia` | Infografía | Tres cifras enormes y gráficos sencillos en vertical, para divulgar | ficha, estilos, contenido |
| `comparativa` | Comparativa de opciones | Dos a cuatro opciones con los mismos criterios y la recomendada destacada | ficha, estilos, contenido |
| `cronograma_expediente` | Cronograma del expediente | Qué ha pasado, qué plazo corre y qué viene en un asunto | ficha, estilos, contenido |
| `lista_control` | Lista de control | Cumplimiento por bloque y requisito, con evidencias | ficha, estilos, contenido |
| `mapa_riesgos` | Mapa de riesgos | Matriz de probabilidad e impacto, impacto económico y exposición | ficha, contenido |
| `escenarios` | Escenarios | Qué pasa si cambian los supuestos: horquilla y qué la mueve | ficha, contenido |
| `embudo_conversion` | Embudo de conversión | Un proceso por etapas y dónde se pierde | ficha, contenido |
| `actividad_equipo` | Actividad del equipo | Horas, asuntos y carga por área y por mes | ficha, contenido |
| `informe_territorial` | Informe territorial | Datos por comunidad o provincia en un mapa, con ranking | ficha, contenido |
| `poster` | Poster | Una hoja A3 apaisada con tres cifras y un gráfico grande | ficha, estilos, contenido |

---

## 1. Panel de datos (`panel_datos`)

**Ancho:** `1120px`

**Partes:** ficha, contenido; `remove`: `ESTILOS_MAQUETA`, `SCRIPT_MAQUETA`, `ACCIONES`.

Cuatro indicadores (el primero con minigráfico), cinco gráficos y tabla con totales. Para un periodo o una cartera; un caso es `informe_visual`.

**Huecos:** `tendencia` chispa (indicador 1) · `comparativa` barras · `reparto` anillo · `evolucion` linea · `descomposicion` cascada · `medidor` medidor.

**Cifras:** `indicador_1`, `indicador_2`, `indicador_4` (el 3 es texto: `INDICADOR_3_CIFRA`).

**Marcadores.** Ficha: `PERIODO`, `FECHA_ACTUALIZACION`. Contenido: `INDICADOR_n_ROTULO` y `INDICADOR_n_DETALLE` (n = 1..4) · `TITULO_X` y `SUBTITULO_X` con X = COMPARATIVA, REPARTO, EVOLUCION, DESCOMPOSICION, MEDIDOR, TABLA · `TITULO_NOTA_MEDIDOR`, `NOTA_MEDIDOR` · tabla: `COLUMNA_1..5`, `FILA_n_C1..C5`, `TOTAL_ROTULO`, `TOTAL_C3`.

**Datos**:

```json maqueta=panel_datos parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_1": {"de": "evolucion", "calculo": "ultimo", "unidad": "eur"},
    "indicador_2": {"de": "descomposicion", "calculo": "suma", "unidad": "eur"},
    "indicador_4": {"valor": 0, "unidad": "eur"}
  },
  "graficos": {
    "tendencia": {"tipo": "chispa", "valores": [], "etiquetas": [], "resumen": "{{RESUMEN}}"},
    "comparativa": {"tipo": "barras", "unidad": "eur", "fuente": "cliente", "elementos": []},
    "reparto": {"tipo": "anillo", "unidad": "eur", "fuente": "cliente", "porciones": [], "centro": {"rotulo": "{{ROTULO_CENTRO}}"}},
    "evolucion": {"tipo": "linea", "unidad": "eur", "fuente": "cliente", "etiquetas": [], "series": []},
    "descomposicion": {"tipo": "cascada", "unidad": "eur", "fuente": "cliente", "pasos": [], "total": {"rotulo": "{{ROTULO_TOTAL}}"}},
    "medidor": {"tipo": "medidor", "valor": 0, "maximo": 100, "rotulo": "{{ROTULO_MEDIDOR}}"}
  }
}
```

---

## 2. Informe visual (`informe_visual`)

**Ancho:** `1000px`

**Partes:** ficha, estilos, contenido; `remove`: `SCRIPT_MAQUETA`, `ACCIONES`.

Lectura secuencial con índice lateral: tres indicadores, cuatro secciones numeradas con texto (una con nota destacada), tabla, cronología de hitos, diagrama de plazos, próximos pasos, advertencia y firmas. Para explicar un caso o una viabilidad; admite gráficos en cualquier sección (otro hueco `figure` + su entrada en `graficos`). Si solo hay cifras, `panel_datos`.

**Huecos:** `plazos` plazos (con `hoy` y la lista de plazos).

**Marcadores.** Ficha: `REFERENCIA_EXPEDIENTE`, `FECHA_EMISION`, `DESTINATARIO`, `AUTOR`. Contenido: `INDICADOR_n_ROTULO`, `INDICADOR_n_CIFRA`, `INDICADOR_n_DETALLE` (n = 1..3; cifras como texto) · `TITULO_SECCION_n`, `SUBTITULO_SECCION_n`, `CONTENIDO_SECCION_n` (n = 1..4; el contenido admite varios párrafos) · `TITULO_NOTA`, `CONTENIDO_NOTA` (nota destacada de la sección 1) · tabla: `TITULO_TABLA`, `COLUMNA_1..4`, `FILA_n_C1..C4` · cronología: `HITO_n_FECHA`, `HITO_n_TITULO`, `HITO_n_DETALLE` (hitos 1-2, se clonan) · `PASO_1`, `PASO_2` (próximos pasos) · `TITULO_ADVERTENCIA`, `CONTENIDO_ADVERTENCIA` · `FIRMA_1`, `FIRMA_2`.

**Datos**:

```json maqueta=informe_visual parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {},
  "graficos": {
    "plazos": {"tipo": "plazos", "hoy": "{{FECHA_AAAA_MM_DD}}", "plazos": [], "fuente": "cliente"}
  }
}
```

---

## 3. Herramienta interactiva (`herramienta_interactiva`)

**Ancho:** `1020px`

**Partes:** ficha, estilos, acciones, contenido, script; nada en `remove`.

Calculadora o simulador: tres campos numéricos y un desplegable, recálculo inmediato, tres resultados, medidor, desglose, lista de verificación, supuestos y advertencia. Si el usuario no va a mover los datos, `escenarios`.

**Huecos:** `resultado` medidor (0-100, con `tramos`). **Script:** trae la función `calcular`; tras crear el archivo se reescribe solo esa función (JavaScript nativo) con `edit_file`. Recibe el objeto de `leer()` y devuelve `{resultado1, resultado2, resultado3, medidor, desglose: [{concepto, importe, detalle}]}` (`medidor` 0-100; `totalDetalle` opcional). `UNIDAD` = unidad de los resultados 1 y 2 (`eur`, `dias`, `num` o texto). Formato con `Reportes.fmt`; el medidor se mueve con `Reportes.actualizar("resultado", {valor})`.

**Marcadores.** Ficha: `REFERENCIA_EXPEDIENTE`. Contenido: `TITULO_PANEL_ENTRADA`, `SUBTITULO_PANEL_ENTRADA` · campos: `CAMPO_n_ROTULO`, `CAMPO_n_VALOR_INICIAL`, `CAMPO_n_AYUDA` (n = 1..3), `CAMPO_4_ROTULO`, `CAMPO_4_AYUDA` y sus opciones `OPCION_n_VALOR`, `OPCION_n_ROTULO` (n = 1..2) · verificación: `TITULO_VERIFICACION`, `SUBTITULO_VERIFICACION`, `PUNTO_n`, `PUNTO_n_DETALLE` (n = 1..3) · resultados: `TITULO_PANEL_RESULTADO`, `SUBTITULO_PANEL_RESULTADO`, `RESULTADO_n_ROTULO` (n = 1..3) · desglose: `TITULO_DESGLOSE`, `DESGLOSE_COLUMNA_1..3`, `DESGLOSE_TOTAL_ROTULO` · `TITULO_SUPUESTOS`, `CONTENIDO_SUPUESTOS` · `TITULO_ADVERTENCIA`, `CONTENIDO_ADVERTENCIA`.

**Datos**:

```json maqueta=herramienta_interactiva parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {},
  "graficos": {
    "resultado": {"tipo": "medidor", "valor": 0, "maximo": 100, "tramos": [60, 85], "rotulo": "{{ROTULO_MEDIDOR}}", "tabla": false}
  }
}
```

---

## 4. Presentación (`presentacion`)

**Ancho:** `1280px`

**Partes:** ficha, estilos, contenido, script; `remove`: `ACCIONES`.

Diapositivas 16:9 con navegación y notas del orador (tecla N, no se imprimen); en papel, una por página. Sin marcadores propios: **las diapositivas se declaran como datos** en `diapositivas`; los gráficos van en `graficos` y se citan por nombre. Una idea por diapositiva, titular que afirma, 8-15 diapositivas; la de «Fuentes» la añade el script. `TITULO_CORTO` va en el pie de cada una.

**Tipos** (`maqueta` → campos): `portada` (antetitulo, titulo, subtitulo, fecha, autor) · `agenda` (titulo, puntos) · `separador` (numero, titulo, texto) · `cifra` (cifra o `dato` = clave de `cifras`, titulo, texto) · `grafico` (titulo, grafico, conclusion) · `puntos` (titulo, puntos ≤ 5, grafico) · `dos_columnas` (titulo, izquierda, derecha: titulo, texto o puntos) · `comparativa` (titulo, opciones: nombre, puntos, veredicto, estado ok/atencion/riesgo) · `cronologia` (titulo, hitos ≤ 6: fecha, titulo, texto) · `tabla` (titulo, cabecera, filas, nota) · `cita` (cita, autor) · `equipo` (titulo, personas: nombre, cargo, texto) · `proximos_pasos` (titulo, pasos: texto, responsable, fecha) · `cierre` (titulo, texto, contacto). Todas admiten `notas` y `aviso`; los textos, `{cifra:clave}`.

**Datos**:

```json maqueta=presentacion parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {},
  "graficos": {},
  "diapositivas": [
    {"maqueta": "portada", "antetitulo": "{{ANTETITULO}}", "titulo": "{{TITULO}}", "subtitulo": "{{SUBTITULO}}", "fecha": "{{FECHA}}", "autor": "{{AUTOR}}"},
    {"maqueta": "agenda", "titulo": "{{TITULO}}", "puntos": []},
    {"maqueta": "cifra", "cifra": "{{CIFRA}}", "titulo": "{{TITULO}}", "texto": "{{TEXTO}}", "notas": "{{NOTAS}}"},
    {"maqueta": "proximos_pasos", "titulo": "{{TITULO}}", "pasos": []}
  ]
}
```

---

## 5. Documento largo (`documento_largo`)

**Ancho:** `860px`

**Partes:** ficha, estilos, contenido, script; `remove`: `ACCIONES`.

White paper, memoria o estudio de 6 a 20 páginas con calidad editorial: la cabecera de la base es la portada; después resumen ejecutivo, índice, capítulos numerados, notas y fuentes. El índice lo compone el script a partir de los `h2` de los capítulos (no se escribe). Cada capítulo es `section class="capitulo"` (`capitulo nueva-pagina` para empezar en hoja nueva, recomendado desde el segundo); un gráfico va dentro del capítulo como `figure` precedido de un `h3` que afirma; las notas se marcan con `<sup class="nota">1</sup>`. Al imprimir, cabecera con el título corto y «3 / 12» en cada hoja. Si el texto no necesita gráficos, no es un reporte: documento en Markdown.

**Huecos:** `figura_1` linea (en el capítulo 1); se añaden más huecos con el mismo patrón.

**Marcadores.** Ficha: `AUTOR`, `FECHA_EMISION`. Contenido: `TITULO_RESUMEN`, `CONCLUSION_1..3` · `TITULO_INDICE` · `TITULO_CAPITULO_n`, `TEXTO_CAPITULO_n` (n = 1..3), `TEXTO_CAPITULO_2_CONTINUACION`, `IDEA_DESTACADA_1` (cita destacada del capítulo 1), `SUBTITULO_CAPITULO_3`, `PUNTO_1`, `PUNTO_2` (lista del capítulo 3) · `TITULO_NOTAS`, `NOTA_1`.

**Datos**:

```json maqueta=documento_largo parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "fuente_1": {"nombre": "{{DESCRIPCION_FUENTE}}", "url": "{{URL}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {},
  "graficos": {
    "figura_1": {"tipo": "linea", "unidad": "num", "fuente": "fuente_1", "etiquetas": [], "series": [], "resumen": "{{RESUMEN}}"}
  }
}
```

---

## 6. Resumen ejecutivo (`resumen_ejecutivo`)

**Ancho:** `1000px`

**Partes:** ficha, estilos, contenido; `remove`: `SCRIPT_MAQUETA`, `ACCIONES`.

Una sola página A4: titular con la conclusión, tres indicadores, un gráfico que la sostiene, tres conclusiones y la decisión que se pide. Para un consejo, un socio o un cliente sin tiempo. Al imprimir se reduce la escala lo justo para caber en una hoja; si hay que reducir mucho, sobra contenido. Describe en vez de recomendar: `ficha_una_pagina`.

**Huecos:** `principal` barras. **Cifras:** `indicador_1..3` (claves de `cifras`; los nombres son de ejemplo).

**Marcadores.** Ficha: `DESTINATARIO`, `FECHA_EMISION`. Contenido: `INDICADOR_n_ROTULO`, `INDICADOR_n_DETALLE` (n = 1..3) · `TITULO_GRAFICO` · `TITULO_CONCLUSIONES`, `CONCLUSION_1..3` · `DECISION_QUE_SE_PIDE`.

**Datos**:

```json maqueta=resumen_ejecutivo parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {},
  "graficos": {
    "principal": {"tipo": "barras", "unidad": "eur", "fuente": "cliente", "elementos": [], "resumen": "{{RESUMEN}}"}
  }
}
```

---

## 7. Cuadro de mando (`cuadro_mando`)

**Ancho:** `1200px`

**Partes:** ficha, estilos, contenido; `remove`: `SCRIPT_MAQUETA`, `ACCIONES`.

Scorecard de dirección: ocho indicadores (los cuatro primeros con variación; el 1 y el 5 con minigráfico), objetivos en anillos, cumplimiento en bala, estado por área en semáforos y tabla compacta. Para ver el mes de un vistazo; explicar un caso es `informe_visual`.

**Huecos:** `tendencia_1`, `tendencia_5` chispa · `objetivos` anillos · `cumplimiento` bala · `estado` semaforos. **Cifras:** `indicador_1..8` y `variacion_1..4` (pct con signo).

**Marcadores.** Ficha: `PERIODO`, `FECHA_ACTUALIZACION`. Contenido: `INDICADOR_n_ROTULO`, `INDICADOR_n_DETALLE` (n = 1..8) · `TITULO_X`, `SUBTITULO_X` con X = OBJETIVOS, CUMPLIMIENTO, ESTADO, TABLA · tabla: `COLUMNA_1..4`, `FILA_n_C1..C4` (filas 1-3, se clonan).

**Datos** (recortado: `indicador_3..7`, `variacion_2..4` y `tendencia_5` siguen el mismo patrón):

```json maqueta=cuadro_mando parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_1": {"valor": 0, "unidad": "eur"},
    "indicador_2": {"valor": 0, "unidad": "eur"},
    "indicador_8": {"valor": 0, "unidad": "eur"},
    "variacion_1": {"valor": 0, "unidad": "pct", "signo": true}
  },
  "graficos": {
    "tendencia_1": {"tipo": "chispa", "fuente": "cliente", "resumen": "{{RESUMEN}}", "valores": [], "etiquetas": []},
    "objetivos": {"tipo": "anillos", "fuente": "cliente", "resumen": "{{RESUMEN}}", "elementos": []},
    "cumplimiento": {"tipo": "bala", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "eur", "elementos": []},
    "estado": {"tipo": "semaforos", "fuente": "cliente", "resumen": "{{RESUMEN}}", "elementos": []}
  }
}
```

---

## 8. Ficha de una página (`ficha_una_pagina`)

**Ancho:** `1000px`

**Partes:** ficha, estilos, contenido; `remove`: `SCRIPT_MAQUETA`, `ACCIONES`.

Datos clave de un asunto, un cliente, una finca o una sociedad en una página A4: rejilla de seis datos, tres indicadores, un gráfico y el estado de cada punto en semáforos. Describe; si hay que argumentar una decisión, `resumen_ejecutivo`.

**Huecos:** `principal` barras · `estado` semaforos. **Cifras:** `indicador_1..3`.

**Marcadores.** Ficha: `REFERENCIA`, `FECHA_EMISION`. Contenido: `DATO_n_ROTULO`, `DATO_n_VALOR` (n = 1..6) · `INDICADOR_n_ROTULO`, `INDICADOR_n_DETALLE` (n = 1..3) · `TITULO_GRAFICO`, `SUBTITULO_GRAFICO` · `TITULO_ESTADO`, `SUBTITULO_ESTADO`.

**Datos**:

```json maqueta=ficha_una_pagina parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_1": {"valor": 0, "unidad": "eur"},
    "indicador_2": {"valor": 0, "unidad": "eur"},
    "indicador_3": {"valor": 0, "unidad": "eur"}
  },
  "graficos": {
    "principal": {"tipo": "barras", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "eur", "elementos": []},
    "estado": {"tipo": "semaforos", "fuente": "cliente", "resumen": "{{RESUMEN}}", "elementos": []}
  }
}
```

---

## 9. Infografía (`infografia`)

**Ancho:** `760px`

**Partes:** ficha, estilos, contenido; `remove`: `SCRIPT_MAQUETA`, `ACCIONES`.

Divulgación en vertical: tres cifras enormes con una frase cada una, una proporción en figuras, el avance en anillos y los hitos en una línea de tiempo. Para el cliente final, un boletín o redes: una idea por bloque y sin tablas (si hace falta detalle, `panel_datos`).

**Huecos:** `proporcion` pictograma · `avance` anillos · `hitos` linea_tiempo. **Cifras:** `cifra_1..3`.

**Marcadores.** Ficha: `FUENTE_BREVE`. Contenido: `FRASE_n` (frase bajo la cifra n, n = 1..3) · `TITULO_PROPORCION`, `TITULO_AVANCE`, `TITULO_HITOS`.

**Datos**:

```json maqueta=infografia parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "cifra_1": {"valor": 0, "unidad": "eur", "decimales": 0},
    "cifra_2": {"valor": 0, "unidad": "eur", "decimales": 0},
    "cifra_3": {"valor": 0, "unidad": "eur", "decimales": 0}
  },
  "graficos": {
    "proporcion": {"tipo": "pictograma", "fuente": "cliente", "resumen": "{{RESUMEN}}", "valor": 0, "total": 10, "rotulo": "{{ROTULO}}"},
    "avance": {"tipo": "anillos", "fuente": "cliente", "resumen": "{{RESUMEN}}", "elementos": []},
    "hitos": {"tipo": "linea_tiempo", "fuente": "cliente", "resumen": "{{RESUMEN}}", "hitos": []}
  }
}
```

---

## 10. Comparativa de opciones (`comparativa`)

**Ancho:** `1100px`

**Partes:** ficha, estilos, contenido; `remove`: `SCRIPT_MAQUETA`, `ACCIONES`.

De dos a cuatro opciones frente a frente con los mismos criterios: recomendación arriba, una columna por opción con su veredicto y cuatro criterios, el perfil de cada una en radar y la distancia de coste o plazo en halteras. La recomendada va destacada. Con una sola opción, `ficha_una_pagina`.

**Huecos:** `perfil` radar (ejes = criterios, una serie por opción) · `distancia` halteras (`nombres.a` y `nombres.b` son las dos opciones comparadas).

**Marcadores.** Ficha: `REFERENCIA`, `FECHA_EMISION`. Contenido: `TITULO_RECOMENDACION`, `RECOMENDACION` · `CRITERIO_1..4` · por opción (n = 1..3; la columna 3 se quita si solo hay dos): `OPCION_n_NOMBRE`, `OPCION_n_VEREDICTO`, `OPCION_n_C1..C4` · `TITULO_PERFIL`, `SUBTITULO_PERFIL` · `TITULO_DISTANCIA`, `SUBTITULO_DISTANCIA`.

**Datos**:

```json maqueta=comparativa parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {},
  "graficos": {
    "perfil": {"tipo": "radar", "fuente": "cliente", "resumen": "{{RESUMEN}}", "maximo": 10, "ejes": [], "series": []},
    "distancia": {"tipo": "halteras", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "eur", "nombres": {"a": "{{A}}", "b": "{{B}}"}, "elementos": []}
  }
}
```

---

## 11. Cronograma del expediente (`cronograma_expediente`)

**Ancho:** `1080px`

**Partes:** ficha, estilos, contenido; `remove`: `SCRIPT_MAQUETA`, `ACCIONES`.

Estado y calendario de un asunto: tres indicadores (fase, próximo vencimiento, días que quedan), aviso de plazo, lo que ha pasado en una línea de tiempo, lo que corre en el diagrama de plazos con la marca de hoy, el avance por fase y los próximos pasos con responsable y fecha. Para el cliente que pregunta cómo va lo suyo; para explicar la estrategia, `informe_visual`.

**Huecos:** `hitos` linea_tiempo · `plazos` plazos · `fases` progreso (ambos con `hoy`).

**Marcadores.** Ficha: `REFERENCIA`, `FECHA_EMISION`. Contenido: `INDICADOR_n_ROTULO`, `INDICADOR_n_CIFRA`, `INDICADOR_n_DETALLE` (n = 1..3; cifras como texto) · `TITULO_AVISO`, `AVISO_PLAZO` · `TITULO_X`, `SUBTITULO_X` con X = HITOS, PLAZOS, FASES, PASOS · pasos: `PASO_n`, `RESPONSABLE_n`, `FECHA_PASO_n` (n = 1..3).

**Datos**:

```json maqueta=cronograma_expediente parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {},
  "graficos": {
    "hitos": {"tipo": "linea_tiempo", "fuente": "cliente", "resumen": "{{RESUMEN}}", "hoy": "{{AAAA-MM-DD}}", "hitos": []},
    "plazos": {"tipo": "plazos", "fuente": "cliente", "resumen": "{{RESUMEN}}", "hoy": "{{AAAA-MM-DD}}", "plazos": []},
    "fases": {"tipo": "progreso", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "pct", "elementos": []}
  }
}
```

---

## 12. Lista de control (`lista_control`)

**Ancho:** `1080px`

**Partes:** ficha, estilos, contenido; `remove`: `SCRIPT_MAQUETA`, `ACCIONES`.

Auditoría o checklist de cumplimiento: porcentaje global calculado, avance por bloque, estado de cada requisito en semáforos y la tabla de evidencias con distintivos. Para protección de datos, blanqueo, compliance o una due diligence corta. Los estados los fija el usuario: nunca se presume un incumplimiento.

**Huecos:** `bloques` progreso (con `tramos`) · `requisitos` semaforos. **Cifras:** `indicador_1` = porcentaje de `a` (correctos) sobre `b` (total).

**Marcadores.** Ficha: `REFERENCIA`, `FECHA_EMISION`. Contenido: `INDICADOR_1_ROTULO`, `INDICADOR_1_DETALLE`; `INDICADOR_n_ROTULO`, `INDICADOR_n_CIFRA`, `INDICADOR_n_DETALLE` (n = 2..3) · `TITULO_X`, `SUBTITULO_X` con X = BLOQUES, REQUISITOS, TABLA · tabla: `COLUMNA_1..3`, por fila (n = 1..4, se clonan) `FILA_n_REQUISITO`, `FILA_n_EVIDENCIA`, `FILA_n_ESTADO` (texto del distintivo) y `FILA_n_CLASE` (`es-ok`, `es-atencion` o `es-riesgo`).

**Datos**:

```json maqueta=lista_control parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_1": {"operacion": "porcentaje", "a": "{{CORRECTOS}}", "b": "{{TOTAL}}", "unidad": "pct"}
  },
  "graficos": {
    "bloques": {"tipo": "progreso", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "pct", "tramos": [50, 80], "elementos": []},
    "requisitos": {"tipo": "semaforos", "fuente": "cliente", "resumen": "{{RESUMEN}}", "elementos": []}
  }
}
```

---

## 13. Mapa de riesgos (`mapa_riesgos`)

**Ancho:** `1120px`

**Partes:** ficha, contenido; `remove`: `ESTILOS_MAQUETA`, `SCRIPT_MAQUETA`, `ACCIONES`.

Riesgos de una operación o un asunto: cuántos hay y cuántos críticos, exposición total, matriz de probabilidad e impacto, estado de las medidas, impacto económico en tornado y exposición dentro de su horquilla. Probabilidad e impacto los valora el usuario; no se inventan.

**Huecos:** `matriz` matriz (filas = probabilidad, columnas = impacto) · `medidas` semaforos · `impacto` tornado (con `base`) · `exposicion` rango (`minimo`, `maximo`, `tramos`, `marcas`). **Cifras:** `indicador_3`.

**Marcadores.** Ficha: `REFERENCIA`, `FECHA_EMISION`. Contenido: `INDICADOR_n_ROTULO`, `INDICADOR_n_CIFRA`, `INDICADOR_n_DETALLE` (n = 1..2); `INDICADOR_3_ROTULO`, `INDICADOR_3_DETALLE` · `TITULO_X`, `SUBTITULO_X` con X = MATRIZ, MEDIDAS, IMPACTO, EXPOSICION.

**Datos**:

```json maqueta=mapa_riesgos parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_3": {"valor": 0, "unidad": "eur", "decimales": 0}
  },
  "graficos": {
    "matriz": {"tipo": "matriz", "fuente": "cliente", "resumen": "{{RESUMEN}}", "filas": ["Alta", "Media", "Baja"], "columnas": ["Bajo", "Medio", "Alto"], "eje_filas": "Probabilidad", "eje_columnas": "Impacto", "elementos": []},
    "medidas": {"tipo": "semaforos", "fuente": "cliente", "resumen": "{{RESUMEN}}", "elementos": []},
    "impacto": {"tipo": "tornado", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "eur", "base": 0, "elementos": []},
    "exposicion": {"tipo": "rango", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "eur", "minimo": 0, "maximo": 0, "tramos": [], "marcas": []}
  }
}
```

---

## 14. Escenarios (`escenarios`)

**Ancho:** `1120px`

**Partes:** ficha, contenido; `remove`: `ESTILOS_MAQUETA`, `SCRIPT_MAQUETA`, `ACCIONES`.

«Qué pasa si»: resultado central, mínimo y máximo (calculados de `por_escenario`), tabla de supuestos, resultado por escenario en columnas, qué parámetro mueve más en tornado y horquilla. Los extremos de cada parámetro se dicen en los supuestos. Si el usuario quiere mover él los parámetros, `herramienta_interactiva`.

**Huecos:** `por_escenario` columnas · `sensibilidad` tornado (con `base`) · `horquilla` rango. **Cifras:** `indicador_1..3` = primero, mínimo y máximo de `por_escenario`.

**Marcadores.** Ficha: `REFERENCIA`, `FECHA_EMISION`. Contenido: `INDICADOR_n_ROTULO`, `INDICADOR_n_DETALLE` (n = 1..3) · `TITULO_SUPUESTOS`, `SUBTITULO_SUPUESTOS`, tabla `COLUMNA_1..4` (parámetro y un escenario por columna), `FILA_n_C1..C4` (filas 1-3, se clonan) · `TITULO_X`, `SUBTITULO_X` con X = POR_ESCENARIO, SENSIBILIDAD, HORQUILLA.

**Datos**:

```json maqueta=escenarios parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_1": {"de": "por_escenario", "calculo": "primero", "unidad": "eur"},
    "indicador_2": {"de": "por_escenario", "calculo": "minimo", "unidad": "eur"},
    "indicador_3": {"de": "por_escenario", "calculo": "maximo", "unidad": "eur"}
  },
  "graficos": {
    "por_escenario": {"tipo": "columnas", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "eur", "etiquetas": [], "series": []},
    "sensibilidad": {"tipo": "tornado", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "eur", "base": 0, "elementos": []},
    "horquilla": {"tipo": "rango", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "eur", "minimo": 0, "maximo": 0, "marcas": []}
  }
}
```

---

## 15. Embudo de conversión (`embudo_conversion`)

**Ancho:** `1120px`

**Partes:** ficha, contenido; `remove`: `ESTILOS_MAQUETA`, `SCRIPT_MAQUETA`, `ACCIONES`.

Proceso por etapas (captación, recobro, tramitación): cuántos entran, qué porcentaje llega al final, en qué etapa se pierden (embudo), por dónde pasa cada asunto (sankey) y cómo evoluciona la composición (área apilada). Sin etapas, `panel_datos`.

**Huecos:** `embudo` embudo (`etapas`) · `evolucion` area_apilada · `flujos` sankey (`nodos`, `flujos`). **Cifras:** `indicador_1` (máximo del embudo), `indicador_3` (último), `indicador_2` = porcentaje 3/1, `variacion_2` (pct con signo).

**Marcadores.** Ficha: `PERIODO`, `FECHA_ACTUALIZACION`. Contenido: `INDICADOR_n_ROTULO`, `INDICADOR_n_DETALLE` (n = 1..3); `INDICADOR_4_ROTULO`, `INDICADOR_4_CIFRA`, `INDICADOR_4_DETALLE` · `TITULO_X`, `SUBTITULO_X` con X = EMBUDO, EVOLUCION, FLUJOS.

**Datos**:

```json maqueta=embudo_conversion parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_1": {"de": "embudo", "calculo": "maximo", "unidad": "entero"},
    "indicador_2": {"operacion": "porcentaje", "a": "indicador_3", "b": "indicador_1", "unidad": "pct"},
    "indicador_3": {"de": "embudo", "calculo": "ultimo", "unidad": "entero"},
    "variacion_2": {"valor": 0, "unidad": "pct", "signo": true}
  },
  "graficos": {
    "embudo": {"tipo": "embudo", "fuente": "cliente", "resumen": "{{RESUMEN}}", "etapas": []},
    "evolucion": {"tipo": "area_apilada", "fuente": "cliente", "resumen": "{{RESUMEN}}", "etiquetas": [], "series": []},
    "flujos": {"tipo": "sankey", "fuente": "cliente", "resumen": "{{RESUMEN}}", "nodos": [], "flujos": []}
  }
}
```

---

## 16. Actividad del equipo (`actividad_equipo`)

**Ancho:** `1120px`

**Partes:** ficha, contenido; `remove`: `ESTILOS_MAQUETA`, `SCRIPT_MAQUETA`, `ACCIONES`.

Horas, asuntos y carga por área o persona: totales, asuntos por área y mes en mapa de calor, días de más actividad en calendario, tiempos de resolución en cajas y horas frente al objetivo en bala. Datos agregados; nunca un ranking de personas sin que el usuario lo pida.

**Huecos:** `por_area` mapa_calor (`filas`, `columnas`, `valores`) · `dias` calendario (`dias` por fecha) · `tiempos` cajas (`grupos`) · `horas` bala. **Cifras:** `indicador_1` (suma de `horas`), `indicador_2`.

**Marcadores.** Ficha: `PERIODO`, `FECHA_ACTUALIZACION`. Contenido: `INDICADOR_n_ROTULO`, `INDICADOR_n_DETALLE` (n = 1..2); `INDICADOR_n_ROTULO`, `INDICADOR_n_CIFRA`, `INDICADOR_n_DETALLE` (n = 3..4) · `TITULO_X`, `SUBTITULO_X` con X = POR_AREA, DIAS, TIEMPOS, HORAS.

**Datos**:

```json maqueta=actividad_equipo parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_1": {"de": "horas", "calculo": "suma", "unidad": "entero"},
    "indicador_2": {"valor": 0, "unidad": "entero"}
  },
  "graficos": {
    "por_area": {"tipo": "mapa_calor", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "entero", "filas": [], "columnas": [], "valores": []},
    "dias": {"tipo": "calendario", "fuente": "cliente", "resumen": "{{RESUMEN}}", "dias": {}},
    "tiempos": {"tipo": "cajas", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "dias", "grupos": []},
    "horas": {"tipo": "bala", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "horas", "elementos": []}
  }
}
```

---

## 17. Informe territorial (`informe_territorial`)

**Ancho:** `1120px`

**Partes:** ficha, contenido; `remove`: `ESTILOS_MAQUETA`, `SCRIPT_MAQUETA`, `ACCIONES`.

Datos por comunidad autónoma o provincia: el mapa de España (con tasas cuando las poblaciones son muy distintas), las zonas ordenadas en barras y la concentración en pareto. Si las zonas no son de España, barras ordenadas y sin mapa.

**Huecos:** `mapa` mapa (`nivel`: `ccaa` o `provincias`; `valores` por nombre de zona; `destacar` opcional) · `ranking` barras · `concentracion` pareto. **Cifras:** `indicador_1` (suma de `ranking`).

**Marcadores.** Ficha: `PERIODO`, `FECHA_ACTUALIZACION`. Contenido: `INDICADOR_1_ROTULO`, `INDICADOR_1_DETALLE`; `INDICADOR_n_ROTULO`, `INDICADOR_n_CIFRA`, `INDICADOR_n_DETALLE` (n = 2..3) · `TITULO_X`, `SUBTITULO_X` con X = MAPA, RANKING, CONCENTRACION.

**Datos**:

```json maqueta=informe_territorial parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "indicador_1": {"de": "ranking", "calculo": "suma", "unidad": "entero"}
  },
  "graficos": {
    "mapa": {"tipo": "mapa", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "num", "valores": {}},
    "ranking": {"tipo": "barras", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "entero", "elementos": []},
    "concentracion": {"tipo": "pareto", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "entero", "elementos": []}
  }
}
```

---

## 18. Poster (`poster`)

**Ancho:** `1400px`

**Partes:** ficha, estilos, contenido; `remove`: `SCRIPT_MAQUETA`, `ACCIONES`.

Una hoja A3 apaisada para colgar: titular grande, tres cifras en columna y un gráfico que ocupa el resto. Nada que obligue a acercarse: sin tablas ni textos largos. Al imprimir se reduce la escala para caber en un A3 apaisado.

**Huecos:** `principal` linea. **Cifras:** `cifra_1..3`.

**Marcadores.** Ficha: `FUENTE_BREVE`. Contenido: `CIFRA_n_ROTULO` (n = 1..3) · `TITULO_GRAFICO`.

**Datos**:

```json maqueta=poster parte=datos
{
  "idioma": "es-ES",
  "moneda": "EUR",
  "fuentes": {
    "cliente": {"nombre": "{{DESCRIPCION_FUENTE}}", "consulta": "{{FECHA_AAAA_MM_DD}}"}
  },
  "cifras": {
    "cifra_1": {"valor": 0, "unidad": "eur", "decimales": 0},
    "cifra_2": {"valor": 0, "unidad": "eur", "decimales": 0},
    "cifra_3": {"valor": 0, "unidad": "eur", "decimales": 0}
  },
  "graficos": {
    "principal": {"tipo": "linea", "fuente": "cliente", "resumen": "{{RESUMEN}}", "unidad": "eur", "etiquetas": [], "series": []}
  }
}
```
