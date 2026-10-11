---
name: reportes
title: Reportes
i18n:
  en:
    name: reports
    title: Reports
    description: >
      Generates self-contained single-file HTML visual documents that the user opens in a
      browser and prints or saves as PDF with one button: one-page visual reports and dossiers,
      data dashboards with indicators and charts, and interactive calculation, simulation and
      verification tools, and slide presentations. Charts and connector diagrams are declared as data and drawn by its own built-in engine
      (horizontal, grouped and stacked bars, line with area, threshold band and annotations,
      sparkline, gauge, waterfall, risk matrix, deadline timeline, donut and pie), which computes
      scales, totals and percentages, adds a data table with CSV download and the source line
      of each chart, with light, dark and sober themes, responsive layout, A4 print styles and
      accessible text alternatives, built with no external libraries or resources. All figures,
      dates and amounts come from the user, a workspace document or a source verified in the
      session. Do not use for contracts, claims, pleadings or procedural documents (which have
      their own vertical skill and are delivered in markdown), for office files (.docx, .xlsx or
      .pptx), or for web applications with a server, database or
      external services.
description: >
  Genera documentos visuales HTML autocontenidos de un solo archivo que el usuario abre directamente en su navegador
  y puede imprimir o guardar como PDF con un boton: informes visuales y dossieres de una pagina, paneles de datos
  con indicadores y graficos, herramientas interactivas de calculo, simulacion y verificacion, y presentaciones en
  diapositivas 16:9 con notas del orador que se imprimen una por pagina. Los graficos se
  declaran como datos y los dibuja un motor propio incluido en la plantilla (barras horizontales, columnas simples,
  agrupadas, apiladas y al cien por cien, linea con area, banda de umbral y anotaciones, minigrafico de tendencia,
  medidor semicircular, cascada de importes, matriz de riesgo e impacto, diagrama de plazos con marca de hoy, anillo
  tarta, bala de objetivo y barras divergentes, mas diagramas con conectores por capas, arbol, radial y carriles),
  que calcula escalas, totales y porcentajes, anade a cada grafico su tabla de datos con descarga en CSV
  y su fuente, y compone el pie de fuentes del documento. Todo se construye con HTML, CSS y SVG en linea, sin
  librerias ni recursos externos, con tema claro, oscuro y sobrio, diseno adaptable, animacion discreta de entrada, estilos de impresion en A4 y alternativas
  textuales accesibles en cada grafico. Opera con la misma
  metodologia que el resto del catalogo: clasificacion inicial mediante formulario interactivo, plan de trabajo y
  eleccion de plantilla en el chat, creacion del archivo completo en el espacio de trabajo y edicion incremental
  bloque a bloque con vista previa y confirmacion. Las cifras, fechas e importes proceden siempre de los datos
  aportados por el usuario, de un documento de su espacio de trabajo o de una fuente verificada en la sesion.
  NO usar para redactar contratos, demandas, escritos ni documentos de tramitacion (que disponen de skill vertical
  propia y se entregan en markdown), NO usar para producir archivos de ofimatica (.docx, .xlsx o .pptx; las
  presentaciones en diapositivas si se hacen, en HTML), y NO usar para construir aplicaciones web con servidor, base de datos o conexion a
  servicios externos.
when_to_use: |
  - El usuario pide un informe, resumen o dossier "visual", "bonito", "presentable" o "para enseñar al cliente".
  - El usuario pide un panel, cuadro de mando, dashboard o grafico a partir de datos, importes o plazos.
  - El usuario pide una calculadora, simulador, comparador o lista de verificacion con la que poder interactuar.
  - El usuario pide expresamente un documento visual, una pagina web, un HTML o algo "que se abra en el navegador".
  - El usuario quiere convertir a formato visual un documento que ya existe en su espacio de trabajo.
  - El usuario necesita un entregable listo para imprimir o exportar a PDF con identidad visual cuidada.
inputs:
  - tipo_documento: informe_visual / panel_datos / herramienta_interactiva / presentacion / fuera_de_alcance (V1)
  - destino_uso: fijado siempre en ambos, no se pregunta (V2)
  - origen_datos: datos_del_chat / documento_del_workspace / busqueda_web (V3)
  - identidad_visual: tema_moderno / tema_sobrio / tema_personalizado (V4)
  - origen_plantilla: plantilla estandar del sistema / plantilla propia del usuario (V5)
  - titulo_y_proposito: titulo del documento visual, destinatario y pregunta que debe responder
  - datos_de_contenido: cifras, fechas, importes, series, hitos, conceptos o criterios a representar
  - parametros_calculo: variables de entrada, formulas y supuestos cuando se trata de una herramienta interactiva
outputs:
  - documento_visual_html: archivo unico en formato snake_case.html con nombre en el idioma del usuario, creado en el espacio de trabajo, autocontenido, con tema claro y oscuro, estilos de impresion en A4 y aviso DRAFT visible; se abre en el navegador con doble clic y se guarda como PDF desde su propio boton
references:
  - references/maquetas-reportes.md
  - references/modulos-motor.md
  - references/anatomia-documento-visual.md
  - references/biblioteca-componentes-visuales.md
  - references/criterios-visualizacion-datos.md
assets:
  - assets/template-base-reportes.md
---

# Generacion de Documentos Visuales Autocontenidos

> DRAFT — para revision por un abogado o profesional colegiado antes de su entrega, presentacion o difusion. Las cifras y conclusiones representadas no constituyen asesoramiento juridico vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guia al usuario de manera consultiva y transparente a traves de un procedimiento estructurado en cinco fases secuenciales, hasta entregar un archivo que se abre en el navegador con un doble clic.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Tipo de Documento visual):** `informe_visual` | `panel_datos` | `herramienta_interactiva` | `presentacion` | `fuera_de_alcance`.
- **V2 (Destino de Uso):** fijado siempre en `ambos`. **No se pregunta nunca:** todo documento visual se entrega util en pantalla y listo para imprimir o guardar como PDF. Preguntarlo solo anadia un paso al asistente para una respuesta que casi siempre era la misma.
- **V3 (Origen de los Datos):** `datos_del_chat` | `documento_del_workspace` | `busqueda_web`.
- **V4 (Identidad Visual):** `tema_moderno` (paleta viva de producto, la de las plantillas) | `tema_sobrio` (paleta de despacho: azul petroleo y neutros calidos, para juzgado y cliente institucional) | `tema_personalizado` (colores corporativos aportados por el usuario).
- **V5 (Origen Plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD Y COMUNICACION AMIGABLE (Global CLAUDE.md):**
> Los identificadores tecnicos de los vectores, las marcas de validacion interna y cualquier mencion a nombres de herramientas o a la arquitectura interna estan terminantemente prohibidos en el chat. Al referirte al resultado, habla del **documento visual**, del **editor** o de **tu espacio de trabajo**.

> **REGLA DE CERO VOLCADO DE CODIGO EN EL CHAT:**
> Queda **TERMINANTEMENTE PROHIBIDO** imprimir en el chat el codigo HTML, CSS o JavaScript del documento visual, ni siquiera de forma parcial o abreviada. Las vistas previas de la Fase 4 se describen **siempre en texto plano y en lenguaje natural** (que indicadores muestra el bloque, con que cifras, que forma grafica adopta y que dice el titulo). El codigo vive unicamente en el archivo del espacio de trabajo.

---

## FASE 1 — CLASIFICACION INICIAL (Resolucion de Vectores V1 a V4 mediante Formulario HITL — REG-TRI-01)

### 1.1 Escucha Activa Previa
Evalua el mensaje inicial y el historial antes de abrir ningun formulario. Si el usuario ya ha indicado de forma inequivoca el tipo de entregable, su destino, de donde salen los datos o si aporta identidad corporativa, registra esos vectores en silencio y pregunta unicamente por lo que falte. Si no falta nada, avanza directamente a la Fase 2.

**Correspondencia con el enrutamiento.** Los vectores de esta skill se nombran con los identificadores siguientes; cada uno se resuelve con la respuesta indicada. No preguntes de nuevo nada que ya este aqui:
- `V1` — respuesta a `tipo_documento`
- `V2` — fijado en `ambos` sin preguntar: pantalla e impresion a la vez
- `V3` — respuesta a `origen_datos`
- `V4` — respuesta a `identidad_visual`
- `V5` — respuesta a `origen_plantilla`, resuelto en la Fase 2 conforme a `REG-AST-01`

### 1.2 Formulario de Clasificacion (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "tipo_documento",
      "rationale": "Resolver V1 para determinar la plantilla base y la estructura visual del documento visual.",
      "question": "¿Que tipo de documento visual necesita?",
      "options": [
        {"id": "informe_visual", "label": "Informe o dossier visual de lectura (secciones, indicadores, cronograma y tablas)"},
        {"id": "panel_datos", "label": "Panel de datos con indicadores y graficos (evolucion, reparto y comparativas)"},
        {"id": "herramienta_interactiva", "label": "Herramienta interactiva: calculadora, simulador o lista de verificacion"},
        {"id": "presentacion", "label": "Presentacion en diapositivas para una reunion o un cliente"},
        {"id": "fuera_de_alcance", "label": "Otra cosa: un contrato o escrito, un archivo de ofimatica o una aplicacion con servidor"}
      ]
    },
    {
      "id": "origen_datos",
      "rationale": "Resolver V3 para saber de donde se toman las cifras, fechas y conceptos que se representaran.",
      "question": "¿De donde salen los datos que debe reflejar el documento visual?",
      "options": [
        {"id": "datos_del_chat", "label": "Se los facilito yo aqui mismo"},
        {"id": "documento_del_workspace", "label": "Estan en un documento de mi espacio de trabajo"},
        {"id": "busqueda_web", "label": "Hay que consultarlos en fuentes oficiales o publicas"}
      ]
    },
    {
      "id": "identidad_visual",
      "rationale": "Resolver V4 para fijar la paleta, el radio de las tarjetas y el encabezado del documento visual.",
      "question": "¿Que aspecto prefiere para el documento visual?",
      "options": [
        {"id": "tema_moderno", "label": "Moderno: cifras grandes, colores vivos y mucho aire"},
        {"id": "tema_sobrio", "label": "Sobrio de despacho: azules apagados y neutros calidos"},
        {"id": "tema_personalizado", "label": "Los colores y el nombre de mi despacho o empresa"}
      ]
    }
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Fijados los vectores de clasificacion, evalua la rama de ejecucion. `V2` esta fijado en `ambos` y no se pregunta; `V3` y `V4` no abren rama propia: modulan el contenido de la Fase 4 dentro de la rama elegida.

* Si `V1 = informe_visual` -> Plantilla del sistema: la base `assets/template-base-reportes.md` con la maqueta `informe_visual` de `references/maquetas-reportes.md`. Lectura secuencial con encabezado, indice lateral pegajoso, fila de indicadores, secciones numeradas, tabla, cronologia de hitos, avisos y bloque de firmas. Procede a la Fase 2.
* Si `V1 = panel_datos` -> Plantilla del sistema: la base `assets/template-base-reportes.md` con la maqueta `panel_datos` de `references/maquetas-reportes.md`. Rejilla de tarjetas con indicadores (uno con minigrafico de tendencia), barras comparativas, anillo de reparto, evolucion con area y banda de umbral, cascada de descomposicion del importe, medidor semicircular y tabla de detalle con totales. Procede a la Fase 2.
* Si `V1 = herramienta_interactiva` -> Plantilla del sistema: la base `assets/template-base-reportes.md` con la maqueta `herramienta_interactiva` de `references/maquetas-reportes.md`. Panel de entrada con campos, recalculo inmediato, medidor semicircular que se mueve con el resultado, desglose tabular, lista de verificacion con progreso y bloque de supuestos. Procede a la Fase 2.
* Si `V1 = presentacion` -> Plantilla del sistema: la base `assets/template-base-reportes.md` con la maqueta `presentacion` de `references/maquetas-reportes.md`. Diapositivas 16:9 declaradas como datos (portada, agenda, separadores, cifra, grafico con conclusion, comparativa, cronologia, tabla, cita, equipo, proximos pasos y cierre), con navegacion, pantalla completa, notas del orador y una diapositiva por pagina al imprimir. Procede a la Fase 2.
* Si `V1 = fuera_de_alcance` -> Detener proceso: no crear documento visual. Explica en el chat que ese entregable corresponde a otra via (la skill vertical del catalogo si es un contrato o un escrito de tramitacion; un archivo de ofimatica si necesita documento de texto, hoja de calculo o presentacion; un desarrollo a medida si requiere servidor o conexion a servicios externos) y ofrece como alternativa el documento visual mas proximo a su necesidad.

---

## FASE 2 — PLAN DE TRABAJO Y ELECCION DE PLANTILLA (REG-AST-01)

### 2.1 Verificacion Previa
1. Consulta `references/criterios-visualizacion-datos.md` para decidir que forma grafica responde a la pregunta del usuario, y `references/anatomia-documento-visual.md` para las reglas invariables del formato.
2. Si `V3 = busqueda_web`, verifica los datos en fuentes oficiales mediante `web_search` antes de representarlos. **Regla de citas (obligatoria):** cada cifra obtenida de internet queda trazada a su fuente &mdash;nombre de la fuente, URL y fecha de consulta&mdash; y el documento visual lleva siempre su bloque de fuentes en el pie con esas referencias. Cada fuente se declara en `fuentes` del bloque de datos con su nombre, URL y fecha real de consulta (`AAAA-MM-DD`); el motor escribe la fuente bajo cada grafico y compone el pie de fuentes del documento. Una cifra sin fuente verificada en la sesion no entra en el documento: queda como `{{VARIABLE}}` o se omite el bloque que la necesitaba.
3. Si `V3 = documento_del_workspace`, toma el contenido prioritariamente de la seccion `# WORKSPACE ACTIVE DOCUMENTS`.
4. **Regla de enriquecimiento (obligatoria):** si los datos los aporta el usuario (`V3 = datos_del_chat` o `documento_del_workspace`), pregunta SIEMPRE, antes de crear el documento, si este se construye solo con sus datos o si se enriquece con documentacion buscada en internet, salvo que ya lo haya dicho en la conversacion (escucha activa). Si el usuario elige enriquecer: las cifras de internet cumplen la regla de citas del punto 2 y quedan diferenciadas de las del usuario (en el propio bloque o en el pie se dice que dato viene de cada origen); nunca se mezclan origenes sin marcarlos.

### 2.2 Mensaje de Plan de Accion y Formulario de Seleccion de Plantilla
En un unico turno, expon en el chat:
1. **Que va a mostrar el documento visual:** la idea principal, los indicadores que encabezaran la pagina y que forma grafica se usara para cada pregunta, con una justificacion breve (por ejemplo, barras ordenadas para comparar partidas y linea para la evolucion mensual).
2. **Que datos faltan** para completarlo, si los hay.
3. **Propuesta de plantilla oficial del sistema** mencionada solo por su denominacion formal (informe visual, panel de datos, herramienta interactiva o presentacion). Prohibido mostrar rutas de archivo y prohibido volcar el contenido de la plantilla.
4. **Formulario preceptivo** `restricted_human_in_the_loop_request` con `id` `origen_plantilla` y las dos opciones canonicas de `REG-AST-01` (`plantilla_sistema` y `plantilla_usuario`).

### 2.3 Fijacion de V5 y Manejo de la Eleccion
- Si `V5 = plantilla_sistema`: toma integra la plantilla enrutada en la Fase 1.3 y avanza a la Fase 3.
- Si `V5 = plantilla_usuario`: pide que pegue su maqueta o su documento base si aun no lo ha aportado, comprueba que cumple las reglas invariables de `references/anatomia-documento-visual.md` (archivo unico, sin recursos externos, sin librerias, con tema oscuro y estilos de impresion), advierte en el chat de los incumplimientos detectados proponiendo la correccion, adopta la version corregida como base y avanza a la Fase 3.

---

## FASE 3 — CREACION DEL ARTEFACTO BASE EN EL EDITOR (REG-DOC-01)

1. **Escritura del archivo (`create_file`):** vuelca **integramente** la base `assets/template-base-reportes.md`, con los marcadores rellenos con las partes de la maqueta del tipo elegido (`{{ANCHO}}`, `{{FICHA}}`, `{{CONTENIDO}}`, `{{ESTILOS_MAQUETA}}` y `{{ACCIONES}}`, conforme a `references/maquetas-reportes.md`) y el bloque `datos-reporte` con lo que ya se conoce, en un archivo con nombre descriptivo en formato `snake_case.html`. **El nombre se escribe en el idioma del usuario, sin acentos ni enes para evitar problemas de codificacion** (por ejemplo `panel_reclamacion_cantidad.html`, `informe_viabilidad_monitorio.html`, `simulador_intereses_demora.html`). La base contiene el documento HTML completo: se copia tal cual, con su bloque de estilos, su aviso DRAFT y el motor de graficos, sin resumirlo, sin fragmentarlo, sin modificar el motor y sin envolverlo en marcas de codigo. En la herramienta interactiva se anade ademas el script de calculo de su maqueta, justo despues del motor.
2. **Zero-Omission:** sustituye en ese mismo volcado **todos** los marcadores cuyo valor ya conoces: titulo, entradilla, etiqueta superior, fechas, referencia del expediente, destinatario, nombres de las partes resueltos conforme a `REG-CLI-01` a `REG-CLI-04`, e indicadores cuyas cifras ya constan. Prohibido crear el archivo con los marcadores en blanco si la informacion ya obra en la conversacion.
3. **Marcadores pendientes:** los datos aun desconocidos permanecen visibles como `{{VARIABLE}}` y se resuelven en la Fase 4. Prohibido rellenarlos con ceros, guiones o cifras inventadas.
4. **Aplicacion de V4:** el tema se fija en la etiqueta `html`: `data-tema="moderno"` (la paleta por defecto) o `data-tema="sobrio"` (azul petroleo y neutros calidos, con su version oscura). Si `V4 = tema_personalizado`, se parte del tema moderno y se ajustan en `:root` los tokens `--acento`, `--acento-suave`, `--acento-fuerte` y la serie `--c1` a `--c6` a los colores aportados, tambien dentro del bloque oscuro, verificando el contraste en ambos, y se coloca el nombre del despacho en la etiqueta superior.
5. **Aplicacion de V2 (siempre `ambos`):** el documento visual tiene que sostener las dos lecturas a la vez, sin sacrificar ninguna. En pantalla: densidad de informacion, elementos manipulables y tema oscuro. En papel: bloque `@media print` completo, fidelidad de color, sin cortes de tarjeta ni titulos huerfanos. Si una decision favorece a una y perjudica a la otra, se busca la que sirva a ambas.
6. **Confirmacion en el chat y encadenamiento:** informa de la ruta absoluta del documento visual creado y anade siempre estas dos indicaciones al usuario:
   - **Como se abre:** al seleccionarlo en su espacio de trabajo, la plataforma ofrece abrirlo en el navegador o mostrarlo en su carpeta; tambien se abre con un doble clic sobre el archivo. El boton inferior de la propia pagina lo imprime o lo guarda como PDF (destino *Guardar como PDF* en el dialogo de impresion, con los graficos de fondo activados si se quiere conservar el color).
   - **Como se modifica:** cualquier ajuste se pide en el chat y el asistente lo aplica sobre el archivo. El documento visual no se edita a mano en el editor de texto, que trabaja en markdown.
   En esa **misma respuesta** abre el primer bloque de la Fase 4 sin pedir permiso para continuar.

---

## FASE 4 — EDICION INCREMENTAL BLOQUE A BLOQUE

Recorre los bloques del documento visual en el orden de la hoja de ruta, aplicando las directivas globales de `CLAUDE.md`: busqueda prioritaria de personas con `search_clients` y volcado directo sin confirmacion (`REG-CLI-01` a `REG-CLI-05`), solicitud en bloque de datos objetivos con `slot_filling_request`, ingestion directa de lo aportado por el chat (`REG-DAT-01`), cero insistencia ante negativa expresa (`REG-INS-01`), validacion de coherencia factica (`REG-VAL-01`) y anuncio de seccion con avance sin permiso (`REG-SEC-01`).

Para cada bloque sustantivo: recogida de datos -> **descripcion en texto plano de lo que mostrara el bloque** (nunca su codigo) -> `¿Confirmamos esta seccion?` -> `edit_file`.

### Hoja de Ruta de Bloques:

#### 1. Encabezado e identificacion
- Titulo del documento visual (afirma la idea principal, no etiqueta el contenido), entradilla de una o dos frases, etiqueta superior, referencia del expediente, fecha, destinatario y autoria.
- Datos de personas y entidades resueltos conforme a `REG-CLI-01` a `REG-CLI-05` y volcados de inmediato en el encabezado y en el pie, sin confirmacion previa en el chat.
- `{{TITULO_CORTO}}` (el elemento `title`) es distinto del titular: nombre corto y reconocible («Morosidad 2026 · Talleres Ebro»), mientras el `h1` afirma la idea principal. El titulo corto es lo que se lee en la pestana del navegador y el nombre que propone el PDF. Los caracteres especiales de HTML se escriben como entidades en cualquier texto del documento (`&amp;` para «&», `&lt;` para «<»); los acentos y la «ñ» se escriben tal cual.

#### 2. Indicadores principales
- Entre dos y cuatro cifras clave con su unidad, su fecha de referencia y una linea de detalle.
- **Validacion obligatoria (REG-VAL-01):** comprueba que las cifras cuadran entre si y con las tablas antes de volcarlas. Si un total no coincide con la suma de sus partidas, dialoga en el chat y aclara la discrepancia antes de escribirla.
- **Afirmaciones del usuario que sus datos no sostienen** (un «record» que no lo es, un total que no cuadra, un dato sin fecha o de alcance dudoso): no se reproducen en el documento como hechos. Se senalan en el chat pidiendo aclaracion y, mientras tanto, el documento no las afirma; si conviene que el lector lo sepa, va un aviso de verificacion visible. Un dato ambiguo (no consta la fecha o si forma parte de un total) no se combina con otros para sacar porcentajes hasta aclararlo.
- **Cifras derivadas** (porcentajes de cumplimiento, diferencias con un objetivo, totales, variaciones): siempre declaradas en `cifras` como calculo u operacion, nunca calculadas a mano (`references/biblioteca-componentes-visuales.md`).
- Si la cifra sale de un grafico, se escribe con `data-cifra` y se declara en `cifras` del bloque de datos, para que el indicador y el grafico no puedan contradecirse.
- Uso de los modificadores de estado (`es-ok`, `es-atencion`, `es-riesgo`) solo cuando el dato expresa realmente una situacion favorable, de atencion o de riesgo.

#### 3. Cuerpo visual (segun V1)
- *Si `V1 = informe_visual`:* secciones numeradas con texto, un aviso destacado cuando haya un plazo o un riesgo relevante, una tabla de detalle y un cronograma de hitos con fechas ciertas.
- *Si `V1 = panel_datos`:* elige la forma grafica segun la pregunta que responde, conforme a la tabla de `references/criterios-visualizacion-datos.md`. Cada grafico se declara en el bloque `datos-reporte` con el contrato de `references/biblioteca-componentes-visuales.md` y se coloca con su hueco `data-grafico`; el motor calcula escalas, totales y porcentajes. **Nunca se escriben coordenadas, arcos, porcentajes ni totales a mano**, y cada grafico cita su fuente por clave.
- *Si `V1 = informe_visual`:* las secciones admiten cualquier grafico del motor (el diagrama de plazos ya va en la maqueta); se declara igual que en el panel.
- *Si `V1 = presentacion`:* cada bloque de la hoja de ruta es una o varias diapositivas de la lista `diapositivas`, con su maqueta de diapositiva (`references/maquetas-reportes.md`). Una idea por diapositiva y un titular que afirma; los graficos y diagramas se declaran en `graficos` y se citan por su nombre; las notas del orador recogen lo que se dira y no se ve. La vista previa en el chat describe cada diapositiva en una linea.
- *Diagramas con conectores (cualquier tipo de reporte):* procesos, flujos de un procedimiento, cadenas de hechos, organigramas o estructuras societarias, relaciones entre partes y quien hace que se declaran como grafico `diagrama` y requieren copiar el modulo de `references/modulos-motor.md` despues del motor. Nunca se dibujan cajas ni flechas a mano.
- *Si `V1 = herramienta_interactiva`:* campos de entrada con etiqueta y texto de ayuda, bloque de calculo escrito en JavaScript nativo dentro del script de la maqueta que devuelve `{resultado1, resultado2, resultado3, medidor, desglose}`, resultados destacados, medidor semicircular dibujado por el motor y alimentado por el campo `medidor` (porcentaje de 0 a 100), desglose tabular y lista de verificacion con progreso.
- En los tres casos, cada grafico lleva su alternativa textual accesible y un titulo que afirma algo. Los rotulos de ejes, leyendas, unidades y descripciones accesibles se escriben **en el idioma del usuario**; las clases y los identificadores del documento permanecen en espanol tal como vienen en la plantilla.

#### 4. Supuestos, fuentes y advertencias
- Bloque de supuestos con las formulas, tipos e hipotesis empleadas en cualquier calculo. Si el documento visual calcula, el usuario debe poder auditar como.
- Pie con las fuentes efectivamente consultadas (documento aportado, expediente o fuente oficial verificada) y la advertencia legal. Todo dato buscado en internet cita fuente, URL y fecha de consulta (regla de citas de la Fase 2.1); si conviven datos del usuario y datos de internet, el pie deja claro que viene de cada origen.
- Aviso destacado de riesgo cuando corran plazos de caducidad o prescripcion.

#### 5. Control de calidad final
Recorre la lista de verificacion de `references/criterios-visualizacion-datos.md`: ausencia de marcadores sin resolver, coherencia entre cifras del texto y de los graficos, legibilidad en tema claro y oscuro, ausencia de desbordamiento horizontal, ningun grafico con el recuadro rojo de error, vista de impresion correcta y presencia del aviso DRAFT.

---

## FASE 5 — BUCLE DE REALIMENTACION FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

1. **Verificacion final:** comprueba el estado del documento visual prioritariamente en `# WORKSPACE ACTIVE DOCUMENTS`.
2. **Menu interactivo de cierre:**
   ```markdown
   El documento visual esta listo en el editor y puede abrirse en el navegador.

   Seleccione una opcion si desea realizar ajustes:
   1. Modificar o ajustar un bloque existente (indicadores, grafico, tabla o texto).
   2. Anadir un bloque nuevo (otra comparativa, un cronograma o una lista de verificacion).
   3. Eliminar contenido o corregir cifras, fechas y datos de las partes.
   4. Revisar la coherencia global, la accesibilidad y la vista de impresion.
   5. Dar el documento visual por finalizado y cerrar la sesion.
   ```
3. **Advertencias preceptivas de cierre (REG-CLO-01):** al finalizar, recuerda que el documento visual es un borrador profesional sujeto a revision colegiada antes de su entrega o difusion; que las cifras calculadas son estimaciones que no sustituyen a la liquidacion oficial ni al calculo pericial; y que si el contenido se va a presentar ante un organismo o incorporar a un procedimiento, debe trasladarse al documento formal correspondiente, que dispone de su propia skill en el catalogo.

---

## Limites y Guardrails de Dominio

1. **Un archivo, cero dependencias externas:** prohibido enlazar librerias, fuentes, hojas de estilo o imagenes remotas, y prohibida cualquier llamada de red. El documento visual debe funcionar sin conexion y abierto directamente desde el espacio de trabajo del usuario.
2. **Cero invencion de datos:** ninguna cifra, fecha, importe, porcentaje o serie puede ser estimada, completada o extrapolada por el asistente. Lo que falte permanece como `{{VARIABLE}}` visible.
3. **Honestidad grafica innegociable:** eje de magnitudes desde cero, escala uniforme, sin recortes ni redondeos que favorezcan una tesis. Un grafico que exagera una diferencia es un defecto grave del entregable.
4. **Seguridad del contenido:** prohibido `eval`, `new Function`, `document.write` y la insercion con `innerHTML` de valores introducidos por el usuario. Prohibidos los dialogos bloqueantes del navegador (`alert`, `confirm`, `prompt`).
5. **Accesibilidad exigible:** contraste minimo 4.5 a 1, alternativa textual en cada grafico, etiquetas asociadas a cada campo y foco visible. El color nunca porta informacion en solitario.
6. **Cero volcado de codigo en el chat:** el documento visual se describe en lenguaje natural; su codigo vive unicamente en el archivo.
7. **Todo en el idioma del usuario:** nombre del archivo, titulo de la pestana, encabezados, rotulos, leyendas, unidades y alternativas accesibles. La estructura interna del HTML (clases e identificadores) esta en espanol y no se traduce ni se renombra.
8. **Tamano contenido:** el documento visual se mantiene por debajo de unos 120 KB (la base con el motor ocupa unos 50). Los documentos abiertos se incorporan enteros al contexto de la conversacion, de modo que un documento visual desmesurado desplaza al resto de documentos de trabajo. Si los datos no caben, se resume la serie o se reparte en dos documentos visuales.
9. **Impresion garantizada:** antes de dar el documento visual por bueno se comprueba la vista de impresion: sin botones, sin fondos oscuros, sin animacion, sin tarjetas partidas entre paginas y con el encabezado de las tablas repetido en cada pagina.
10. **Delimitacion frente al catalogo:** los contratos, demandas, escritos y solicitudes de tramitacion se redactan en su skill vertical y en formato markdown. Esta skill visualiza, resume y calcula; no sustituye al documento formal ni al asesoramiento de un profesional colegiado.
