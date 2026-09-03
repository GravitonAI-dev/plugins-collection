---
name: desahucio
description: >
  Genera el documento adecuado para recuperar la posesion de una finca urbana, eligiendo la via
  correcta conforme a la LEC verificada en el BOE: demanda de juicio verbal de desahucio por falta
  de pago de rentas (con opcion de acumular la reclamacion de las rentas debidas, Art. 437.4.3ª LEC),
  demanda de desahucio por expiracion del plazo contractual o legal (Art. 250.1.1º LEC), demanda de
  desahucio por precario (Art. 250.1.2º LEC) y acuerdo extrajudicial de condonacion de rentas a cambio
  de la entrega de llaves (transaccion del Art. 1809 CC, homologable conforme al Art. 19 LEC). Aplica
  la resolucion por impago del Art. 27 LAU, los requisitos de admisibilidad del Art. 439.3 y 439.6 LEC
  (Ley 12/2023), el regimen de enervacion del Art. 22.4 LEC y el requisito de MASC de la LO 1/2025.
  NO usar para la recuperacion de vivienda frente a ocupacion sin titulo previo (Art. 250.1.4º LEC),
  desahucio de finca rustica, ejecucion hipotecaria, ni para redactar la oposicion del demandado.
when_to_use: |
  - El usuario quiere recuperar la posesion de una vivienda o local urbano arrendado o cedido.
  - El arrendatario no paga la renta y el arrendador quiere desahuciarlo, con o sin reclamacion de rentas.
  - El contrato de arrendamiento ha expirado y el arrendatario no desaloja.
  - Un ocupante posee la finca sin titulo ni pago (precario) y el propietario quiere recuperarla.
  - El arrendador quiere pactar la salida del ocupante perdonando la deuda a cambio de las llaves.
  - El usuario pide una demanda de desahucio de finca urbana.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
- relacion_ocupante: arrendamiento con renta / cesion gratuita sin renta / entrada sin permiso ni contrato
  - causa: falta de pago de rentas / expiracion del plazo contractual o legal
  - via: demanda judicial / acuerdo extrajudicial de salida pactada
  - destino_inmueble: vivienda habitual de la parte ocupante / uso distinto del de vivienda (Art. 439.6.a LEC)
  - gran_tenedor: la parte actora es gran tenedora de vivienda conforme al Art. 3.k de la Ley 12/2023 (si / no / desconocido)
  - requerimiento_previo: requerimiento fehaciente de pago practicado con 30 dias de antelacion (si / no)
  - masc_intentado: se ha intentado un medio adecuado de solucion de controversias acreditable (si / no)
  - datos_demandante: nombre o razon social, NIF o CIF, domicilio, representante si persona juridica, procurador y letrado
  - datos_demandado: nombre o razon social, NIF o CIF si se conoce, domicilio del inmueble
  - datos_inmueble: direccion completa, referencia catastral, municipio y partido judicial
  - datos_contrato: fecha de firma, renta mensual, duracion pactada
  - rentas_debidas: importe total adeudado, conceptos y periodos impagados
  - fecha_expiracion: fecha en que expiro el contrato y sus prorrogas
  - titulo_precario: descripcion de la cesion gratuita y de su revocacion
  - acumular_rentas: acumular o no la reclamacion de las rentas debidas (si / no)
  - condonacion: alcance de la condonacion pactada (total / parcial) y renuncia reciproca de acciones
outputs:
- demanda_desahucio_falta_pago: demanda de juicio verbal de desahucio por falta de pago en markdown, DRAFT
  - demanda_desahucio_expiracion: demanda de juicio verbal de desahucio por expiracion del plazo en markdown, DRAFT
  - demanda_desahucio_precario: demanda de juicio verbal de desahucio por precario en markdown, DRAFT
  - acuerdo_condonacion: acuerdo de condonacion de rentas y entrega de llaves en markdown, DRAFT
references:
  - references/enervacion-y-vulnerabilidad.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lau-resolucion-por-impago.md
  - references/lec-juicio-desahucio.md
assets:
  - assets/template-acuerdo-condonacion-entrega-llaves.md
  - assets/template-demanda-desahucio-expiracion-plazo.md
  - assets/template-demanda-desahucio-falta-pago.md
  - assets/template-demanda-desahucio-precario.md
---

# Recuperacion de la Posesion de Finca Urbana

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación (V1 a V4) y el origen de la plantilla (V5).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la naturaleza del caso y fijar los vectores deterministas de estado.

### 1.1 Escucha Activa Previa
Antes de abrir formularios interactivos o hacer preguntas, analiza el mensaje inicial del usuario y la documentación aportada:
- Si el mensaje ya especifica inequívocamente los vectores de la operación, asígnalos de forma inmediata y silenciosa en memoria y pasa a la **Fase 2**.
- Si restan vectores por definir, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado interactivo mediante la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Presenta al usuario las opciones estructuradas para resolver los vectores pendientes:
```json
{
  "type": "object",
  "properties": {
    "relacion_ocupante": {
      "type": "string",
      "description": "T\u00edtulo de ocupaci\u00f3n y relaci\u00f3n jur\u00eddica (V1)",
      "enum": [
        "arrendamiento",
        "precario"
      ]
    },
    "causa_desahucio": {
      "type": "string",
      "description": "Causa de resoluci\u00f3n y recuperaci\u00f3n (V2)",
      "enum": [
        "falta_pago",
        "expiracion_plazo",
        "recuperacion_precario"
      ]
    },
    "via_actuacion": {
      "type": "string",
      "description": "V\u00eda de tramitaci\u00f3n elegida (V3)",
      "enum": [
        "demanda_judicial",
        "acuerdo_extrajudicial"
      ]
    },
    "condicion_arrendador": {
      "type": "string",
      "description": "Condici\u00f3n del arrendador / demandante (V4)",
      "enum": [
        "particular",
        "gran_tenedor"
      ]
    }
  },
  "required": [
    "relacion_ocupante",
    "causa_desahucio"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = entrada sin permiso ni contrato previo → **DETENER**: el caso corresponde a la recuperacion de la posesion del Art. 250.1.4º de la LEC, con tramitacion propia (Art. 441.1 bis LEC), legitimacion tasada y exceptuada del requisito de MASC (Art. 5.2.e de la LO 1/2025). Fuera del alcance de esta skill. Informar del cauce y ofrecer escalacion. No crear documento.
- Si V3 = acuerdo de salida pactada → **HOJA ACUERDO**: `assets/template-acuerdo-condonacion-entrega-llaves.md`. V4, V5 y V7 no aplican (no hay demanda que admitir). Si V1 = cesion gratuita, no hay renta debida que condonar: omitir la clausula tercera y adaptar el acuerdo a la entrega de llaves sin condonacion, advirtiendolo al usuario.
- Si V3 = demanda y V1 = arrendamiento y V2 = falta de pago → **HOJA IMPAGO**: `assets/template-demanda-desahucio-falta-pago.md`.
- Si V3 = demanda y V1 = arrendamiento y V2 = expiracion del plazo → **HOJA EXPIRACION**: `assets/template-demanda-desahucio-expiracion-plazo.md`.
- Si V3 = demanda y V1 = cesion gratuita sin renta → **HOJA PRECARIO**: `assets/template-demanda-desahucio-precario.md`.
- En cualquier hoja de demanda, si V7 = no → generar ademas ANTES `assets/template-acuerdo-condonacion-entrega-llaves.md` NO: el intento previo se documenta con un requerimiento fehaciente. Redactar el requerimiento no forma parte de esta skill; derivar a `reclamacion-cantidad` (asset `burofax-masc-reclamacion.md`) y advertir de que la demanda no debe presentarse hasta disponer del justificante y de que hayan transcurrido treinta dias naturales sin respuesta (Art. 10.4.a de la LO 1/2025).
- Si la finca es rustica, o el arrendamiento esta excluido de la LAU (Art. 5 LAU), o se pretende la ejecucion hipotecaria → **DETENER**: fuera de alcance. Advertir y escalar.

### Validacion de admisibilidad (interno, antes del Punto 3)

- **TODAS LAS HOJAS DE DEMANDA (Art. 439.6 LEC, redaccion de la Ley 12/2023):** la demanda es inadmisible si no especifica (a) si el inmueble constituye vivienda habitual de la persona ocupante — valor de V4 — y (b) si la parte actora es gran tenedora de vivienda en los terminos del Art. 3.k de la Ley 12/2023 — valor de V5. Si V5 = no es gran tenedora, debe acompanarse certificacion del Registro de la Propiedad con la relacion de propiedades a nombre de la parte actora. Si V5 = no lo sabe, no dar el dato por resuelto: explicar el umbral y pedir que lo confirme antes de redactar.
  **Importante:** las letras c) del apartado 6 y el apartado 7 del Art. 439 (acreditar la vulnerabilidad de la parte demandada y acudir a conciliacion o intermediacion previa cuando la actora es gran tenedora) fueron declarados inconstitucionales y nulos por la Sentencia del Tribunal Constitucional 26/2025, de 29 de enero. NO exigirlos ni incluirlos en la demanda.
- **HOJA IMPAGO (Art. 439.3 LEC):** la demanda es inadmisible si no se indican las circunstancias concurrentes que permiten o impiden la enervacion en el caso concreto. Ese pronunciamiento se construye con el valor de V6 y es obligatorio.
- **HOJA IMPAGO (Art. 27.2.a LAU):** confirmar que lo impagado es la renta o cantidades asimiladas cuyo pago corresponde a la parte arrendataria.
- **HOJA EXPIRACION:** confirmar que el contrato y sus prorrogas legales han vencido (Arts. 9, 10 y 11 LAU) y que no procede prorroga obligatoria ni tacita.
- **HOJA PRECARIO:** confirmar la titularidad de la parte actora y la ausencia de titulo y de renta en la parte ocupante. Si media contraprestacion de cualquier clase, no hay precario: reconducir a la hoja que corresponda.
- **POSTULACION:** en el desahucio, la clase de juicio se determina por razon de la materia (Art. 250.1.1º y 2º), no por la cuantia, por lo que las excepciones de los Arts. 23.2.1º y 31.2.1º de la LEC no operan: abogado y procurador son preceptivos. La cuantia, a los efectos que procedan, es la de una anualidad de renta (Art. 251.9ª LEC).
- **MASC:** el desahucio no figura entre las materias exceptuadas del Art. 5.2 de la LO 1/2025, por lo que el intento previo es requisito de procedibilidad en las tres hojas de demanda. Solo la recuperacion de la posesion del Art. 250.1.4º esta exceptuada (letra e).
- **COMPETENCIA (Art. 52.1.7 LEC):** juzgado del lugar en que este sita la finca, sin sumision posible a otro fuero.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 250.1.1º y 2º, 439, 440, 441 y 444 de la Ley de Enjuiciamiento Civil (LEC), modificados por la Ley 12/2023 por el derecho a la vivienda; Art. 27 de la LAU (resolución por impago); y Art. 1.569 del Código Civil.
2. **Orientación Legal del Caso:**
Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Textos fijos por hoja:
   - IMPAGO: "A su caso corresponde el juicio verbal de desahucio por falta de pago, conforme al articulo 250.1.1º de la Ley 1/2000, de Enjuiciamiento Civil, cualquiera que sea la cuantia, con fundamento sustantivo en el articulo 27.2.a) de la Ley 29/1994, de Arrendamientos Urbanos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - EXPIRACION: "A su caso corresponde el juicio verbal de desahucio por expiracion del plazo, conforme al articulo 250.1.1º de la Ley 1/2000, de Enjuiciamiento Civil, en relacion con los articulos 9 y 10 de la Ley 29/1994, de Arrendamientos Urbanos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - PRECARIO: "A su caso corresponde el juicio verbal de desahucio por precario, conforme al articulo 250.1.2º de la Ley 1/2000, de Enjuiciamiento Civil, en relacion con el articulo 348 del Codigo Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - ACUERDO: "Su caso se resolvera mediante un contrato de transaccion, regulado en el articulo 1809 del Codigo Civil, con condonacion de la deuda condicionada a la entrega de la posesion (articulos 1156 y 1187 del Codigo Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - En las tres hojas de demanda, anadir: "El desahucio no figura entre las materias exceptuadas del articulo 5.2 de la Ley Organica 1/2025, de 2 de enero, por lo que debera acreditarse el intento previo de una solucion extrajudicial para que la demanda sea admitida (articulos 264.4º y 403.2 de la Ley de Enjuiciamiento Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2025-76"
   - En las tres hojas de demanda, anadir: "En el desahucio son preceptivos abogado y procurador, porque la clase de juicio viene determinada por la materia y no por la cuantia."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (advierte si el documento adjuntado los incumple, en especial las menciones obligatorias del Art. 439.3 y 439.6 LEC).
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-acuerdo-condonacion-entrega-llaves.md`).
4. **Pregunta Explícita al Usuario (Vía Chat):** Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
* **Si `[V5 = plantilla_sistema]` (El usuario acepta la plantilla propuesta):**
  Toma el texto íntegro de la plantilla correspondiente directamente desde el catálogo del prompt y procede de inmediato a la **Fase 3**.
* **Si `[V5 = plantilla_usuario]` (El usuario aporta su propia minuta adjuntando un documento o pegando texto):**
  1. Accede al contenido del adjunto desde `<attached_documents>` o el mensaje del usuario.
  2. **Guardrail de Verificación Legal:** Analiza el texto aportado. Si contiene cláusulas nulas, contrarias a normas imperativas o de imposible cumplimiento, adviértelo expresamente en el chat y propón la redacción legalmente válida.
  3. Adopta la minuta revisada como base y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos e inserta `{{DATO_FALTANTE}}` para aquellos que deban resolverse durante la redacción.
   - PROHIBIDO dejar archivos en blanco, crear resúmenes o esquemas provisionales.
2. **Validación de Integridad (`read_file`):**
   - Ejecuta inmediatamente `read_file` sobre el archivo recién creado para comprobar que el volcado es íntegro y que el archivo existe en disco.
3. **Confirmación en Chat y Encadenamiento Inmediato:**
   - Informa al usuario de la ruta absoluta del documento creado.
   - En esa **misma respuesta**, introduce la primera sección/cláusula de la **Fase 4** y formula ya su primera pregunta, sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

### Protocolo Obligatorio de Edición
Para cada cláusula o bloque temático del documento, ejecuta estrictamente el siguiente ciclo interactivo:
```
[Pregunta al Usuario] ──> [Vista Previa en texto plano] ──> [¿Confirmamos?] ──> [edit_file + read_file]
```
1. **Pregunta en Chat:** Solicita los datos específicos de la sección.
2. **Vista Previa:** Muestra el texto exacto redactado en texto plano en el chat.
3. **Confirmación:** Consulta al usuario si está conforme o desea algún ajuste.
4. **Persistencia en Disco:** Una vez confirmado, ejecuta `edit_file` con `old_string` y `new_string` exactos, y verifica con `read_file`.

### Hoja de Ruta de Secciones y Cláusulas Condicionales

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas de negociacion se explican y se confirman una a una.

### Secciones — HOJA IMPAGO / HOJA EXPIRACION / HOJA PRECARIO

1. **Parte demandante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte que reclama la posesion." Sub-apartados, uno por turno: a) nombre completo o razon social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) solo si es persona juridica: nombre, documento y cargo del representante; e) nombre del procurador y del letrado (preceptivos, no preguntar si son necesarios). Al completar el ultimo, vista previa unica con todos los datos y una sola confirmacion antes del `Edit`.
2. **Parte demandada** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte demandada." Sub-apartados: a) nombre o razon social; b) NIF o CIF si se conoce; c) domicilio, que en el desahucio suele ser el propio inmueble. Confirmacion agrupada.
3. **El inmueble y su destino** *(dato objetivo con mencion obligatoria)*. Anuncio fijo: "Describimos ahora el inmueble objeto del procedimiento." Sub-apartados: a) direccion completa; b) referencia catastral; c) municipio y partido judicial. El destino del inmueble ya quedo resuelto en la clasificacion: no volver a preguntarlo, pero hacerlo constar expresamente en el documento porque su omision determina la inadmision (Art. 439.6.a LEC).
4. **Condicion de gran tenedor** *(dato objetivo con consecuencia documental)*. Anuncio fijo: "Debemos hacer constar en la demanda su condicion respecto de la tenencia de vivienda." El valor ya quedo resuelto en la clasificacion. Explica antes de continuar: la mencion es obligatoria y su omision determina la inadmision (Art. 439.6.b LEC); si la parte actora NO es gran tenedora, debe acompanarse certificacion del Registro de la Propiedad con la relacion de sus propiedades, y hay que confirmar con el usuario que la solicitara. Aclara tambien, si el usuario lo plantea, que el deber de acreditar la vulnerabilidad de la parte demandada y de acudir a conciliacion previa fue anulado por la Sentencia del Tribunal Constitucional 26/2025.
5. **Contrato y causa del desahucio** *(dato objetivo, con contenido propio de cada hoja)*.
   - IMPAGO. Anuncio fijo: "Pasamos al contrato y a la deuda de rentas." Sub-apartados, uno por turno: a) fecha del contrato; b) renta mensual; c) periodos impagados; d) importe total adeudado y conceptos que lo componen (rentas y cantidades asimiladas del Art. 27.2.a LAU); e) relacion de documentos que se aportaran.
   - EXPIRACION. Anuncio fijo: "Pasamos al contrato y a su vencimiento." Sub-apartados: a) fecha del contrato; b) duracion pactada; c) fecha en que expiro el contrato y sus prorrogas; d) si se comunico la voluntad de no renovar, y con que antelacion y por que medio.
   - PRECARIO. Anuncio fijo: "Pasamos al origen de la ocupacion y a su revocacion." Sub-apartados: a) titulo de propiedad de la parte actora y documento que lo acredita; b) como y cuando se cedio el uso gratuito y que relacion une a las partes; c) como y cuando se revoco la tolerancia y se requirio la restitucion. Verifica expresamente que no media renta ni contraprestacion de ninguna clase.
6. **Requerimiento previo y enervacion** *(clausula de negociacion — explicar antes de decidir; solo HOJA IMPAGO)*. Anuncio fijo: "Abordamos ahora el requerimiento previo de pago y sus efectos sobre la enervacion." Explica antes de pedir la decision: la parte demandada puede enervar la accion pagando o consignando lo debido y dejar sin efecto el desahucio (Art. 22.4 LEC), salvo que ya enervara en una ocasion anterior o que se le requiriera de pago por medio fehaciente con al menos treinta dias de antelacion a la demanda sin haber pagado. Segun el valor resuelto en la clasificacion:
   - Requerimiento con mas de treinta dias y justificante: si aun no se conocen, pide el medio empleado (burofax, requerimiento notarial) y su fecha exacta, y se hace constar en la demanda que no procede la enervacion, acompanando el requerimiento y su acuse.
   - Requerimiento sin ese plazo, o sin justificante, o inexistente: la enervacion sera posible. Explica que existe la alternativa de practicar ahora un requerimiento fehaciente y esperar treinta dias antes de presentar la demanda, con la ventaja de que el mismo burofax puede servir para acreditar el intento de solucion previa exigido por la Ley Organica 1/2025, y pide al usuario que decida entre presentar ya la demanda asumiendo la enervacion o requerir primero. Confirma la decision antes de escribirla.
   En todo caso, la demanda debe pronunciarse sobre las circunstancias que permiten o impiden la enervacion: su omision determina la inadmision (Art. 439.3 LEC).
7. **Acumulacion de la reclamacion de rentas** *(clausula de negociacion — explicar antes de decidir; HOJA IMPAGO y HOJA EXPIRACION)*. Anuncio fijo: "Decidimos ahora si reclamamos las rentas debidas en la misma demanda." Explica antes de pedir la decision: cabe acumular a la accion de desahucio la reclamacion de las rentas y cantidades analogas vencidas y no pagadas, con independencia de su importe, y tambien la accion contra el fiador o avalista solidario previo requerimiento de pago no satisfecho (Art. 437.4.3ª LEC); los pronunciamientos sobre las acciones acumuladas si producen cosa juzgada, a diferencia del desahucio en si (Art. 447.2 LEC); acumular evita un segundo procedimiento posterior. Pide la decision, y si es afirmativa, el importe y los periodos, e inserta los bloques condicionales de acumulacion del asset. Confirmacion propia.
8. **Solicitud anticipada del lanzamiento** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos la solicitud de senalamiento del lanzamiento." Explica antes de pedir la decision: puede interesarse ya en la demanda que se tenga por solicitada la ejecucion del lanzamiento en la fecha y hora que fije el juzgado (Art. 437.3 in fine LEC); con esa solicitud, la sentencia condenatoria o el decreto que ponga fin al desahucio se ejecutan directamente el dia y hora senalados, sin necesidad de ningun otro tramite ni de nueva notificacion (Art. 549.3 LEC). Es la opcion habitual y acorta materialmente los plazos. Confirmacion propia.
9. **Compromiso de condonacion por desalojo voluntario** *(clausula de negociacion — explicar antes de decidir; HOJA IMPAGO y HOJA EXPIRACION)*. Anuncio fijo: "Valoramos si desea ofrecer una condonacion a cambio del desalojo voluntario." Explica antes de pedir la decision: puede anunciarse en la demanda el compromiso de condonar toda o parte de la deuda y de las costas, con expresion de la cantidad concreta, condicionado a que la parte demandada desaloje voluntariamente dentro del plazo que se indique, que no podra ser inferior a quince dias desde la notificacion de la demanda (Art. 437.3 LEC); ese compromiso se le pone de manifiesto en el requerimiento y su aceptacion equivale a un allanamiento (Art. 438.5 LEC), con senalamiento subsidiario del lanzamiento directo (Art. 447.1 LEC). Si el usuario prefiere pactarlo fuera del proceso, indicaselo y ofrece el acuerdo de condonacion y entrega de llaves como documento alternativo o complementario. Si declina, omitir el bloque. Confirmacion propia.
10. **Vivienda habitual y actuacion de los servicios sociales** *(informativo, sin pregunta; solo si V4 = vivienda habitual)*. Anuncio fijo: "Le informo de las consecuencias procesales de que el inmueble sea la vivienda habitual de la parte ocupante." Informar: el juzgado comunicara de oficio la existencia del procedimiento a las Administraciones competentes en vivienda y servicios sociales, que pueden verificar la situacion de vulnerabilidad y proponer alternativa habitacional; si se confirma, el tribunal puede suspender el proceso por un maximo de dos meses si la parte demandante es persona fisica y de cuatro meses si es persona juridica, ponderando tambien la vulnerabilidad de la parte actora (Art. 441.5, 441.6 y 441.7 LEC). No requiere dato del usuario; encadenar con la seccion siguiente. Informar tambien de que el regimen extraordinario de suspension de lanzamientos ligado a la crisis sanitaria dejo de surtir efecto y de que su estado debe verificarse en cada caso, junto con la normativa autonomica de vivienda aplicable.
11. **Solucion previa (MASC)** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos por ultimo los terminos del intento de solucion previa." Si ya se intento, pedir el medio empleado, la fecha y el documento que lo acredita, y describir el proceso de negociacion en la demanda (Art. 399.3 LEC). Si no se intento, explica: la acreditacion puede consistir en un documento firmado por ambas partes o en cualquier documento que pruebe que la otra parte recibio la solicitud o la propuesta (Art. 10.2 de la LO 1/2025); el proceso se entiende terminado sin acuerdo si transcurren treinta dias naturales desde la recepcion sin reunion ni respuesta escrita (Art. 10.4.a); y la demanda debe presentarse dentro del ano siguiente (Art. 7.3). Advierte de que la demanda no debe presentarse hasta disponer del justificante y de que los campos correspondientes quedan como placeholders hasta entonces. Confirmacion propia.
12. **Juzgado competente** *(dato objetivo con validacion)*. Anuncio fijo: "Determinamos ahora el juzgado competente." Es el del lugar en que este sita la finca (Art. 52.1.7 LEC). Si el usuario propone otro fuero o invoca una clausula de sumision del contrato, advertir de que no cabe y corregirlo.
13. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Lugar de firma; la fecha por defecto es la del dia, salvo indicacion en contrario.

### Secciones — HOJA ACUERDO

1. **Parte arrendadora** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte arrendadora." Sub-apartados, uno por turno: a) nombre completo o razon social; b) documento de identidad o CIF; c) domicilio a efectos de notificaciones; d) solo si es persona juridica: representante y titulo de su representacion. Confirmacion agrupada.
2. **Parte arrendataria u ocupante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte que ocupa el inmueble." Sub-apartados: a) nombre o razon social; b) documento de identidad o CIF; c) domicilio. Confirmacion agrupada.
3. **Inmueble y contrato que se extingue** *(dato objetivo)*. Anuncio fijo: "Describimos el inmueble y el contrato que se va a extinguir." Sub-apartados: a) direccion completa y referencia catastral; b) titulo de la parte arrendadora; c) fecha del contrato y renta mensual; d) si existe ya un procedimiento judicial en curso, juzgado y numero de autos.
4. **Deuda que se reconoce** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a fijar la deuda que se reconoce." Explica antes de pedir la cifra: el reconocimiento de deuda fija el importe sobre el que operara la condonacion y, si el acuerdo se incumple, es la cantidad que renace; conviene que incluya todos los conceptos vencidos (rentas y cantidades asimiladas) y que se cierre a una fecha concreta. Pide el importe, los conceptos y los periodos. Confirmacion propia.
5. **Alcance de la condonacion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Abordamos ahora el alcance de la condonacion." Explica antes de pedir la decision: la condonacion puede ser total o parcial; si es parcial hay que fijar la cantidad que subsiste, su forma de pago y su plazo; la condonacion se pacta como contraprestacion del desalojo dentro de una transaccion (Art. 1809 CC) y por eso debe quedar condicionada a la entrega efectiva, de modo que una condonacion incondicionada extinguiria la deuda aunque el inmueble no se entregase (Arts. 1156 y 1187 CC); y la operacion puede tener consecuencias tributarias para ambas partes que conviene verificar con un asesor fiscal. Confirmacion propia.
6. **Entrega de llaves y de la posesion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos la entrega de las llaves y de la posesion." Explica antes de pedir los datos: la fecha y la hora deben ser ciertas, porque de ellas depende la eficacia de la condonacion, y conviene levantar acta con el numero de llaves, el estado del inmueble y las lecturas de los contadores. Sub-apartados, uno por turno: a) fecha y hora de la entrega; b) lugar; c) tratamiento de las rentas que se devenguen hasta la entrega. Confirmacion de cada uno.
7. **Fianza, garantias y suministros** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos el destino de la fianza y de las garantias." Explica: la fianza puede devolverse, aplicarse a la deuda subsistente o compensarse con los danos que resulten del acta; conviene decidirlo ahora para evitar una controversia posterior. Pide el importe de la fianza, su destino y, si existen, el tratamiento de las garantias adicionales. Confirmacion propia.
8. **Renuncia reciproca de acciones** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Valoramos la renuncia reciproca de acciones." Explica antes de pedir la decision: una renuncia amplia cierra el asunto pero impide reclamar despues los danos en el inmueble; la posicion conservadora es exceptuar de la renuncia los danos que consten en el acta de entrega y los danos ocultos. Ofrece las dos redacciones del asset y pide la decision. Confirmacion propia.
9. **Consecuencias del incumplimiento** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Fijamos las consecuencias del incumplimiento del acuerdo." Explica: si no se entrega en la fecha pactada, la condonacion queda sin efecto, renace la deuda integra y la parte arrendadora puede ejercitar sin mas tramite las acciones de desahucio y de reclamacion; si hay procedimiento en curso, puede instar su continuacion. Confirma la redaccion antes de aplicarla.
10. **Fuerza ejecutiva del acuerdo** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Decidimos como dotar de fuerza ejecutiva al acuerdo." Explica las tres opciones y sus consecuencias: si hay procedimiento en curso, la homologacion judicial (Art. 19 LEC) le da los efectos de la transaccion judicial y permite ejecutarlo como una sentencia (Art. 517.2.3º LEC); sin procedimiento, la elevacion a escritura publica lo convierte en titulo ejecutivo (Art. 517.2.2º LEC); si no se hace ninguna de las dos, el acuerdo obliga entre las partes (Art. 1816 CC) pero su incumplimiento obliga a un nuevo pleito. Recomienda la homologacion o la escritura publica. Confirmacion propia.
11. **Lugar, fecha y firma** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del acuerdo." Lugar de firma; la fecha por defecto es la del dia, salvo indicacion en contrario.

Al rellenar cualquier hoja de demanda, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones del documento, presenta al usuario un menú interactivo:
```
1. Modificar o ajustar una cláusula o sección existente.
2. Añadir una estipulación o pacto adicional a medida.
3. Eliminar contenido opcional o corregir datos de partes/fincas.
4. Revisar la coherencia global y realizar control de calidad final.
5. Dar el documento por finalizado y cerrar la sesión.
```
### Advertencias Legales Preceptivas de Cierre:
Al dar por finalizado el documento, emite siempre las siguientes advertencias:
- **Carácter DRAFT:** El documento generado es un borrador profesional que debe ser revisado por un abogado colegiado antes de su firma o presentación procesal.
- **Obligaciones Fiscales y Plazos:** Recuerda los plazos de liquidación de tributos (ITP/AJD o Plusvalía municipal en 30 días hábiles) cuando proceda.
- **Elevación a Instrumento Público:** Recuerda que para la inscripción en el Registro de la Propiedad o Mercantil, o para su ejecución forzosa directa, es necesario el otorgamiento ante Notario público.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre la LEC, la LAU y la LO 1/2025 en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder.
2. Si se detecta una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar. No usar una version desactualizada.
3. Las menciones del Art. 439.6.a) y b) de la LEC (destino del inmueble y condicion de gran tenedor de la parte actora) son obligatorias en toda demanda que pretenda recuperar la posesion de una finca por las vias del Art. 250.1.1º, 2º, 4º y 7º. Su omision determina la inadmision. Nunca redactar una demanda sin ellas.
4. Las letras c) del apartado 6 y el apartado 7 del Art. 439 de la LEC fueron declarados inconstitucionales y nulos por la STC 26/2025, de 29 de enero. No exigir al usuario acreditar la vulnerabilidad de la parte demandada ni acudir a conciliacion o intermediacion previa por ser gran tenedor, ni incluir esas menciones en la demanda.
5. En el desahucio por falta de pago, la demanda debe pronunciarse sobre las circunstancias que permiten o impiden la enervacion (Art. 439.3 LEC). Nunca omitir ese pronunciamiento.
6. La enervacion (Art. 22.4 LEC) solo cabe en el desahucio por falta de pago, una sola vez, y no procede si se requirio de pago por medio fehaciente con al menos treinta dias de antelacion sin resultado. No cabe enervacion en expiracion del plazo ni en precario. Informar siempre de esta regla y nunca afirmar que la enervacion esta excluida sin justificante del requerimiento.
7. El intento previo de un medio adecuado de solucion de controversias es requisito de procedibilidad en las tres hojas de demanda: el desahucio no figura entre las materias exceptuadas del Art. 5.2 de la LO 1/2025. Solo la recuperacion de la posesion del Art. 250.1.4º esta exceptuada (letra e).
8. Competencia exclusiva del tribunal del lugar en que este sita la finca (Art. 52.1.7 LEC). No admitir sumision a otro fuero aunque el contrato la contenga.
9. En el desahucio, abogado y procurador son preceptivos: la clase de juicio se determina por la materia, no por la cuantia, y las excepciones de los Arts. 23.2.1º y 31.2.1º de la LEC no operan.
10. El regimen extraordinario de suspension de lanzamientos por vulnerabilidad tiene vigencia temporal y ha sido objeto de prorrogas no siempre convalidadas. Nunca afirmar que esta vigente ni que esta derogado sin haberlo comprobado en el texto consolidado en el Punto 2. Lo que si es permanente es el mecanismo de los Arts. 441.5 a 441.7 de la LEC en desahucios de vivienda habitual.
11. Nunca redactar clausulas o pretensiones que contravengan normas imperativas de la LAU (Art. 6 LAU) ni afirmar la resolucion del contrato sin base en el Art. 27 LAU.
12. En el acuerdo de condonacion, la condonacion debe quedar siempre condicionada a la entrega efectiva de la posesion. Nunca redactar una condonacion incondicionada previa al desalojo.
13. Nunca inventar datos, rentas, fechas, referencias catastrales ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para la recuperacion de la posesion de una vivienda frente a quien entro en ella sin titulo ni relacion previa (Art. 250.1.4º LEC): tiene legitimacion tasada, tramitacion propia (Art. 441.1 bis LEC) y esta exceptuada del MASC. Advertir y escalar.
- No usar para la efectividad de derechos reales inscritos frente a quien los perturba (Art. 250.1.7º LEC).
- No usar para desahucio de finca rustica ni de arrendamientos excluidos de la LAU (Art. 5 LAU).
- No usar para la ejecucion hipotecaria ni para el lanzamiento derivado de ella.
- No usar para redactar la oposicion de la parte demandada, el escrito de enervacion ni el incidente de suspension por vulnerabilidad: advertir y escalar.
- No usar para reclamar solo rentas sin recuperar la posesion: derivar a `reclamacion-cantidad`.
- No usar para redactar el burofax de requerimiento previo: el asset esta en `reclamacion-cantidad`.
- No usar si el usuario pide opinion juridica sobre la estrategia de un litigio: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.