---
name: artefacto-visual
description: >
  Genera artefactos HTML autocontenidos de un solo archivo que el usuario abre directamente en su navegador
  y puede imprimir o guardar como PDF con un boton: informes visuales y dossieres de una pagina, paneles de datos
  con indicadores y graficos, y herramientas interactivas de calculo, simulacion y verificacion. Dispone de una
  biblioteca propia de diez formas graficas en SVG en linea (barras horizontales, verticales, apiladas y al cien
  por cien, linea con area y banda de umbral, minigrafico de tendencia, medidor semicircular, cascada de importes,
  matriz de riesgo e impacto, diagrama de plazos con marca de hoy y anillo de reparto), cada una con su formula de
  calculo documentada. Todo se construye con HTML, CSS y SVG en linea, sin librerias ni recursos externos, con
  tema claro y oscuro, diseno adaptable, animacion discreta de entrada, estilos de impresion en A4 y alternativas
  textuales accesibles en cada grafico. Opera con la misma
  metodologia que el resto del catalogo: clasificacion inicial mediante formulario interactivo, plan de trabajo y
  eleccion de plantilla en el chat, creacion del archivo completo en el espacio de trabajo y edicion incremental
  bloque a bloque con vista previa y confirmacion. Las cifras, fechas e importes proceden siempre de los datos
  aportados por el usuario, de un documento de su espacio de trabajo o de una fuente verificada en la sesion.
  NO usar para redactar contratos, demandas, escritos ni documentos de tramitacion (que disponen de skill vertical
  propia y se entregan en markdown), NO usar para producir archivos de ofimatica (documentos de texto, hojas de
  calculo o presentaciones), y NO usar para construir aplicaciones web con servidor, base de datos o conexion a
  servicios externos.
when_to_use: |
  - El usuario pide un informe, resumen o dossier "visual", "bonito", "presentable" o "para enseñar al cliente".
  - El usuario pide un panel, cuadro de mando, dashboard o grafico a partir de datos, importes o plazos.
  - El usuario pide una calculadora, simulador, comparador o lista de verificacion con la que poder interactuar.
  - El usuario pide expresamente un artefacto, una pagina web, un HTML o algo "que se abra en el navegador".
  - El usuario quiere convertir a formato visual un documento que ya existe en su espacio de trabajo.
  - El usuario necesita un entregable listo para imprimir o exportar a PDF con identidad visual cuidada.
inputs:
  - tipo_artefacto: informe_visual / panel_datos / herramienta_interactiva / fuera_de_alcance (V1)
  - destino_uso: pantalla_interactiva / impresion_pdf / ambos (V2)
  - origen_datos: datos_del_chat / documento_del_workspace / busqueda_web (V3)
  - identidad_visual: tema_moderno / tema_sobrio / tema_personalizado (V4)
  - origen_plantilla: plantilla estandar del sistema / plantilla propia del usuario (V5)
  - titulo_y_proposito: titulo del artefacto, destinatario y pregunta que debe responder
  - datos_de_contenido: cifras, fechas, importes, series, hitos, conceptos o criterios a representar
  - parametros_calculo: variables de entrada, formulas y supuestos cuando se trata de una herramienta interactiva
outputs:
  - artefacto_html: archivo unico en formato snake_case.html con nombre en el idioma del usuario, creado en el espacio de trabajo, autocontenido, con tema claro y oscuro, estilos de impresion en A4 y aviso DRAFT visible; se abre en el navegador con doble clic y se guarda como PDF desde su propio boton
references:
  - references/anatomia-artefacto-html.md
  - references/biblioteca-componentes-visuales.md
  - references/criterios-visualizacion-datos.md
assets:
  - assets/template-informe-visual.md
  - assets/template-panel-datos.md
  - assets/template-herramienta-interactiva.md
---

# Generacion de Artefactos Visuales Autocontenidos

> DRAFT — para revision por un abogado o profesional colegiado antes de su entrega, presentacion o difusion. Las cifras y conclusiones representadas no constituyen asesoramiento juridico vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guia al usuario de manera consultiva y transparente a traves de un procedimiento estructurado en cinco fases secuenciales, hasta entregar un archivo que se abre en el navegador con un doble clic.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Tipo de Artefacto):** `informe_visual` | `panel_datos` | `herramienta_interactiva` | `fuera_de_alcance`.
- **V2 (Destino de Uso):** `pantalla_interactiva` | `impresion_pdf` | `ambos`. Determina el peso de la interaccion frente a la fidelidad de impresion.
- **V3 (Origen de los Datos):** `datos_del_chat` | `documento_del_workspace` | `busqueda_web`.
- **V4 (Identidad Visual):** `tema_moderno` (paleta viva de producto, la de las plantillas) | `tema_sobrio` (paleta de despacho: azul petroleo y neutros calidos, para juzgado y cliente institucional) | `tema_personalizado` (colores corporativos aportados por el usuario).
- **V5 (Origen Plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD Y COMUNICACION AMIGABLE (Global CLAUDE.md):**
> Los identificadores tecnicos de los vectores, las marcas de validacion interna y cualquier mencion a nombres de herramientas o a la arquitectura interna estan terminantemente prohibidos en el chat. Al referirte al resultado, habla del **artefacto**, del **editor** o de **tu espacio de trabajo**.

> **REGLA DE CERO VOLCADO DE CODIGO EN EL CHAT:**
> Queda **TERMINANTEMENTE PROHIBIDO** imprimir en el chat el codigo HTML, CSS o JavaScript del artefacto, ni siquiera de forma parcial o abreviada. Las vistas previas de la Fase 4 se describen **siempre en texto plano y en lenguaje natural** (que indicadores muestra el bloque, con que cifras, que forma grafica adopta y que dice el titulo). El codigo vive unicamente en el archivo del espacio de trabajo.

---

## FASE 1 — CLASIFICACION INICIAL (Resolucion de Vectores V1 a V4 mediante Formulario HITL — REG-TRI-01)

### 1.1 Escucha Activa Previa
Evalua el mensaje inicial y el historial antes de abrir ningun formulario. Si el usuario ya ha indicado de forma inequivoca el tipo de entregable, su destino, de donde salen los datos o si aporta identidad corporativa, registra esos vectores en silencio y pregunta unicamente por lo que falte. Si no falta nada, avanza directamente a la Fase 2.

**Correspondencia con el enrutamiento.** Los vectores de esta skill se nombran con los identificadores siguientes; cada uno se resuelve con la respuesta indicada. No preguntes de nuevo nada que ya este aqui:
- `V1` — respuesta a `tipo_artefacto`
- `V2` — respuesta a `destino_uso`
- `V3` — respuesta a `origen_datos`
- `V4` — respuesta a `identidad_visual`
- `V5` — respuesta a `origen_plantilla`, resuelto en la Fase 2 conforme a `REG-AST-01`

### 1.2 Formulario de Clasificacion (`restricted_human_in_the_loop_request`)

```json
{
  "form_data": [
    {
      "id": "tipo_artefacto",
      "rationale": "Resolver V1 para determinar la plantilla base y la estructura visual del artefacto.",
      "question": "¿Que tipo de artefacto necesita?",
      "options": [
        {"id": "informe_visual", "label": "Informe o dossier visual de lectura (secciones, indicadores, cronograma y tablas)"},
        {"id": "panel_datos", "label": "Panel de datos con indicadores y graficos (evolucion, reparto y comparativas)"},
        {"id": "herramienta_interactiva", "label": "Herramienta interactiva: calculadora, simulador o lista de verificacion"},
        {"id": "fuera_de_alcance", "label": "Otra cosa: un contrato o escrito, un archivo de ofimatica o una aplicacion con servidor"}
      ]
    },
    {
      "id": "destino_uso",
      "rationale": "Resolver V2 para calibrar el peso de la interaccion frente a la fidelidad de impresion.",
      "question": "¿Que uso le va a dar principalmente?",
      "options": [
        {"id": "pantalla_interactiva", "label": "Verlo y manejarlo en pantalla"},
        {"id": "impresion_pdf", "label": "Imprimirlo o guardarlo como PDF para entregarlo"},
        {"id": "ambos", "label": "Ambos usos por igual"}
      ]
    },
    {
      "id": "origen_datos",
      "rationale": "Resolver V3 para saber de donde se toman las cifras, fechas y conceptos que se representaran.",
      "question": "¿De donde salen los datos que debe reflejar el artefacto?",
      "options": [
        {"id": "datos_del_chat", "label": "Se los facilito yo aqui mismo"},
        {"id": "documento_del_workspace", "label": "Estan en un documento de mi espacio de trabajo"},
        {"id": "busqueda_web", "label": "Hay que consultarlos en fuentes oficiales o publicas"}
      ]
    },
    {
      "id": "identidad_visual",
      "rationale": "Resolver V4 para fijar la paleta, el radio de las tarjetas y el encabezado del artefacto.",
      "question": "¿Que aspecto prefiere para el artefacto?",
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
Fijados los vectores de clasificacion, evalua la rama de ejecucion. Las respuestas de `V2`, `V3` y `V4` no abren rama propia: modulan el contenido de la Fase 4 dentro de la rama elegida.

* Si `V1 = informe_visual` -> Plantilla del sistema: `assets/template-informe-visual.md`. Lectura secuencial con encabezado, indice lateral pegajoso, fila de indicadores, secciones numeradas, tabla, cronologia de hitos, avisos y bloque de firmas. Procede a la Fase 2.
* Si `V1 = panel_datos` -> Plantilla del sistema: `assets/template-panel-datos.md`. Rejilla de tarjetas con indicadores (uno con minigrafico de tendencia), barras comparativas, anillo de reparto, evolucion con area y banda de umbral, cascada de descomposicion del importe, medidor semicircular y tabla de detalle con totales. Procede a la Fase 2.
* Si `V1 = herramienta_interactiva` -> Plantilla del sistema: `assets/template-herramienta-interactiva.md`. Panel de entrada con campos, recalculo inmediato, medidor semicircular que se mueve con el resultado, desglose tabular, lista de verificacion con progreso y bloque de supuestos. Procede a la Fase 2.
* Si `V1 = fuera_de_alcance` -> Detener proceso: no crear artefacto. Explica en el chat que ese entregable corresponde a otra via (la skill vertical del catalogo si es un contrato o un escrito de tramitacion; un archivo de ofimatica si necesita documento de texto, hoja de calculo o presentacion; un desarrollo a medida si requiere servidor o conexion a servicios externos) y ofrece como alternativa el artefacto visual mas proximo a su necesidad.

---

## FASE 2 — PLAN DE TRABAJO Y ELECCION DE PLANTILLA (REG-AST-01)

### 2.1 Verificacion Previa
1. Consulta `references/criterios-visualizacion-datos.md` para decidir que forma grafica responde a la pregunta del usuario, y `references/anatomia-artefacto-html.md` para las reglas invariables del formato.
2. Si `V3 = busqueda_web`, verifica los datos en fuentes oficiales mediante `web_search` antes de representarlos, y anota la fuente que figurara en el pie del artefacto.
3. Si `V3 = documento_del_workspace`, toma el contenido prioritariamente de la seccion `# WORKSPACE ACTIVE DOCUMENTS`.

### 2.2 Mensaje de Plan de Accion y Formulario de Seleccion de Plantilla
En un unico turno, expon en el chat:
1. **Que va a mostrar el artefacto:** la idea principal, los indicadores que encabezaran la pagina y que forma grafica se usara para cada pregunta, con una justificacion breve (por ejemplo, barras ordenadas para comparar partidas y linea para la evolucion mensual).
2. **Que datos faltan** para completarlo, si los hay.
3. **Propuesta de plantilla oficial del sistema** mencionada solo por su denominacion formal (informe visual, panel de datos o herramienta interactiva). Prohibido mostrar rutas de archivo y prohibido volcar el contenido de la plantilla.
4. **Formulario preceptivo** `restricted_human_in_the_loop_request` con `id` `origen_plantilla` y las dos opciones canonicas de `REG-AST-01` (`plantilla_sistema` y `plantilla_usuario`).

### 2.3 Fijacion de V5 y Manejo de la Eleccion
- Si `V5 = plantilla_sistema`: toma integra la plantilla enrutada en la Fase 1.3 y avanza a la Fase 3.
- Si `V5 = plantilla_usuario`: pide que pegue su maqueta o su documento base si aun no lo ha aportado, comprueba que cumple las reglas invariables de `references/anatomia-artefacto-html.md` (archivo unico, sin recursos externos, sin librerias, con tema oscuro y estilos de impresion), advierte en el chat de los incumplimientos detectados proponiendo la correccion, adopta la version corregida como base y avanza a la Fase 3.

---

## FASE 3 — CREACION DEL ARTEFACTO BASE EN EL EDITOR (REG-DOC-01)

1. **Escritura del archivo (`create_file`):** vuelca **integramente** el documento HTML de la plantilla acordada en un archivo con nombre descriptivo en formato `snake_case.html`. **El nombre se escribe en el idioma del usuario, sin acentos ni enes para evitar problemas de codificacion** (por ejemplo `panel_reclamacion_cantidad.html`, `informe_viabilidad_monitorio.html`, `simulador_intereses_demora.html`). El asset contiene el documento HTML completo: se copia tal cual, con su bloque de estilos, su aviso DRAFT y su script, sin resumirlo, sin fragmentarlo y sin envolverlo en marcas de codigo.
2. **Zero-Omission:** sustituye en ese mismo volcado **todos** los marcadores cuyo valor ya conoces: titulo, entradilla, etiqueta superior, fechas, referencia del expediente, destinatario, nombres de las partes resueltos conforme a `REG-CLI-01` a `REG-CLI-04`, e indicadores cuyas cifras ya constan. Prohibido crear el archivo con los marcadores en blanco si la informacion ya obra en la conversacion.
3. **Marcadores pendientes:** los datos aun desconocidos permanecen visibles como `{{VARIABLE}}` y se resuelven en la Fase 4. Prohibido rellenarlos con ceros, guiones o cifras inventadas.
4. **Aplicacion de V4:** si `V4 = tema_personalizado`, ajusta en el bloque de estilos los tokens `--accent`, `--accent-soft` y la serie `--c1` a `--c6` a los colores aportados, verificando el contraste en tema claro y oscuro, y coloca el nombre del despacho en la etiqueta superior. Si `V4 = tema_sistema`, conserva la paleta por defecto.
5. **Aplicacion de V2:** si `V2 = impresion_pdf`, refuerza el bloque `@media print` y reduce la interaccion a lo imprescindible; si `V2 = pantalla_interactiva`, prioriza la densidad de informacion y los elementos manipulables; si `V2 = ambos`, ambos requisitos se cumplen sin sacrificar ninguno.
6. **Confirmacion en el chat y encadenamiento:** informa de la ruta absoluta del artefacto creado y anade siempre estas dos indicaciones al usuario:
   - **Como se abre:** al seleccionarlo en su espacio de trabajo, la plataforma ofrece abrirlo en el navegador o mostrarlo en su carpeta; tambien se abre con un doble clic sobre el archivo. El boton inferior de la propia pagina lo imprime o lo guarda como PDF (destino *Guardar como PDF* en el dialogo de impresion, con los graficos de fondo activados si se quiere conservar el color).
   - **Como se modifica:** cualquier ajuste se pide en el chat y el asistente lo aplica sobre el archivo. El artefacto no se edita a mano en el editor de texto, que trabaja en markdown.
   En esa **misma respuesta** abre el primer bloque de la Fase 4 sin pedir permiso para continuar.

---

## FASE 4 — EDICION INCREMENTAL BLOQUE A BLOQUE

Recorre los bloques del artefacto en el orden de la hoja de ruta, aplicando las directivas globales de `CLAUDE.md`: busqueda prioritaria de personas con `search_clients` y volcado directo sin confirmacion (`REG-CLI-01` a `REG-CLI-05`), solicitud en bloque de datos objetivos con `slot_filling_request`, ingestion directa de lo aportado por el chat (`REG-DAT-01`), cero insistencia ante negativa expresa (`REG-INS-01`), validacion de coherencia factica (`REG-VAL-01`) y anuncio de seccion con avance sin permiso (`REG-SEC-01`).

Para cada bloque sustantivo: recogida de datos -> **descripcion en texto plano de lo que mostrara el bloque** (nunca su codigo) -> `¿Confirmamos esta seccion?` -> `edit_file`.

### Hoja de Ruta de Bloques:

#### 1. Encabezado e identificacion
- Titulo del artefacto (afirma la idea principal, no etiqueta el contenido), entradilla de una o dos frases, etiqueta superior, referencia del expediente, fecha, destinatario y autoria.
- Datos de personas y entidades resueltos conforme a `REG-CLI-01` a `REG-CLI-05` y volcados de inmediato en el encabezado y en el pie, sin confirmacion previa en el chat.
- Ajuste del elemento `title` del documento: nombre corto y reconocible, porque es lo que se lee en la pestana del navegador.

#### 2. Indicadores principales
- Entre dos y cuatro cifras clave con su unidad, su fecha de referencia y una linea de detalle.
- **Validacion obligatoria (REG-VAL-01):** comprueba que las cifras cuadran entre si y con las tablas antes de volcarlas. Si un total no coincide con la suma de sus partidas, dialoga en el chat y aclara la discrepancia antes de escribirla.
- Uso de los modificadores de estado (`is-ok`, `is-warn`, `is-risk`) solo cuando el dato expresa realmente una situacion favorable, de atencion o de riesgo.

#### 3. Cuerpo visual (segun V1)
- *Si `V1 = informe_visual`:* secciones numeradas con texto, un aviso destacado cuando haya un plazo o un riesgo relevante, una tabla de detalle y un cronograma de hitos con fechas ciertas.
- *Si `V1 = panel_datos`:* elige la forma grafica segun la pregunta que responde, conforme a la tabla de `references/criterios-visualizacion-datos.md`: barras horizontales para comparar partidas, barras verticales o apiladas para composicion por periodo, evolucion con area y banda de umbral para series temporales, anillo para reparto en tres o cuatro porciones, cascada para descomponer un importe (principal, intereses, costas, total), medidor semicircular para consumo de plazo o porcentaje de avance, matriz de riesgo e impacto para cruzar dos ejes cualitativos y diagrama de plazos con marca de hoy para vencimientos en curso. Las coordenadas, arcos y porcentajes se calculan **siempre** con las formulas de `references/biblioteca-componentes-visuales.md`; nunca se estiman a ojo.
- *Si `V1 = herramienta_interactiva`:* campos de entrada con etiqueta y texto de ayuda, bloque de calculo escrito en JavaScript nativo que devuelve `{resultado1, resultado2, resultado3, medidor, desglose}`, resultados destacados, medidor semicircular alimentado por el campo `medidor` (porcentaje de 0 a 100), desglose tabular y lista de verificacion con progreso.
- En los tres casos, cada grafico lleva su alternativa textual accesible y un titulo que afirma algo. Los rotulos de ejes, leyendas, unidades y descripciones accesibles se escriben **en el idioma del usuario**; las clases y los identificadores del documento permanecen en espanol tal como vienen en la plantilla.

#### 4. Supuestos, fuentes y advertencias
- Bloque de supuestos con las formulas, tipos e hipotesis empleadas en cualquier calculo. Si el artefacto calcula, el usuario debe poder auditar como.
- Pie con las fuentes efectivamente consultadas (documento aportado, expediente o fuente oficial verificada) y la advertencia legal.
- Aviso destacado de riesgo cuando corran plazos de caducidad o prescripcion.

#### 5. Control de calidad final
Recorre la lista de verificacion de `references/criterios-visualizacion-datos.md`: ausencia de marcadores sin resolver, coherencia entre cifras del texto y de los graficos, legibilidad en tema claro y oscuro, ausencia de desbordamiento horizontal, vista de impresion correcta y presencia del aviso DRAFT.

---

## FASE 5 — BUCLE DE REALIMENTACION FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

1. **Verificacion final:** comprueba el estado del artefacto prioritariamente en `# WORKSPACE ACTIVE DOCUMENTS`.
2. **Menu interactivo de cierre:**
   ```markdown
   El artefacto esta listo en el editor y puede abrirse en el navegador.

   Seleccione una opcion si desea realizar ajustes:
   1. Modificar o ajustar un bloque existente (indicadores, grafico, tabla o texto).
   2. Anadir un bloque nuevo (otra comparativa, un cronograma o una lista de verificacion).
   3. Eliminar contenido o corregir cifras, fechas y datos de las partes.
   4. Revisar la coherencia global, la accesibilidad y la vista de impresion.
   5. Dar el artefacto por finalizado y cerrar la sesion.
   ```
3. **Advertencias preceptivas de cierre (REG-CLO-01):** al finalizar, recuerda que el artefacto es un borrador profesional sujeto a revision colegiada antes de su entrega o difusion; que las cifras calculadas son estimaciones que no sustituyen a la liquidacion oficial ni al calculo pericial; y que si el contenido se va a presentar ante un organismo o incorporar a un procedimiento, debe trasladarse al documento formal correspondiente, que dispone de su propia skill en el catalogo.

---

## Limites y Guardrails de Dominio

1. **Un archivo, cero dependencias externas:** prohibido enlazar librerias, fuentes, hojas de estilo o imagenes remotas, y prohibida cualquier llamada de red. El artefacto debe funcionar sin conexion y abierto directamente desde el espacio de trabajo del usuario.
2. **Cero invencion de datos:** ninguna cifra, fecha, importe, porcentaje o serie puede ser estimada, completada o extrapolada por el asistente. Lo que falte permanece como `{{VARIABLE}}` visible.
3. **Honestidad grafica innegociable:** eje de magnitudes desde cero, escala uniforme, sin recortes ni redondeos que favorezcan una tesis. Un grafico que exagera una diferencia es un defecto grave del entregable.
4. **Seguridad del contenido:** prohibido `eval`, `new Function`, `document.write` y la insercion con `innerHTML` de valores introducidos por el usuario. Prohibidos los dialogos bloqueantes del navegador (`alert`, `confirm`, `prompt`).
5. **Accesibilidad exigible:** contraste minimo 4.5 a 1, alternativa textual en cada grafico, etiquetas asociadas a cada campo y foco visible. El color nunca porta informacion en solitario.
6. **Cero volcado de codigo en el chat:** el artefacto se describe en lenguaje natural; su codigo vive unicamente en el archivo.
7. **Todo en el idioma del usuario:** nombre del archivo, titulo de la pestana, encabezados, rotulos, leyendas, unidades y alternativas accesibles. La estructura interna del HTML (clases e identificadores) esta en espanol y no se traduce ni se renombra.
8. **Tamano contenido:** el artefacto se mantiene por debajo de unos 100 KB. Los documentos abiertos se incorporan enteros al contexto de la conversacion, de modo que un artefacto desmesurado desplaza al resto de documentos de trabajo. Si los datos no caben, se resume la serie o se reparte en dos artefactos.
9. **Impresion garantizada:** antes de dar el artefacto por bueno se comprueba la vista de impresion: sin botones, sin fondos oscuros, sin animacion, sin tarjetas partidas entre paginas y con el encabezado de las tablas repetido en cada pagina.
10. **Delimitacion frente al catalogo:** los contratos, demandas, escritos y solicitudes de tramitacion se redactan en su skill vertical y en formato markdown. Esta skill visualiza, resume y calcula; no sustituye al documento formal ni al asesoramiento de un profesional colegiado.
