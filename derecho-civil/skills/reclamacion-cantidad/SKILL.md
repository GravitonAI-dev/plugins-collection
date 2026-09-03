---
name: reclamacion-cantidad
description: >
  Genera el documento adecuado para reclamar (o defenderse de la reclamacion de) una cantidad de dinero,
  eligiendo la via procesal correcta conforme a la LEC verificada en el BOE: peticion inicial de proceso
  monitorio (deuda documentada, liquida, vencida y exigible, cualquier cuantia), demanda de juicio verbal
  (hasta 15.000 euros o rentas de arrendamiento), demanda de juicio ordinario (mas de 15.000 euros, incluida
  la posterior a la oposicion de un monitorio, Art. 818.2 LEC), escrito de oposicion al monitorio (posicion
  de deudor) y burofax de requerimiento previo (MASC, LO 1/2025). NO usar para pretensiones no dinerarias,
  materias del Art. 249.1 LEC cuya pretension principal no sea el pago, reclamaciones frente a
  Administraciones Publicas, desahucios ni ejecuciones.
when_to_use: |
  - El usuario quiere reclamar judicialmente una cantidad de dinero y no sabe (o no indica) por que via.
  - El usuario quiere iniciar la reclamacion de una deuda con o sin documentos que la acrediten.
  - El usuario ha iniciado un monitorio, el deudor se ha opuesto y la cuantia obliga a demandar en ordinario.
  - El cliente ha recibido un requerimiento de pago de un proceso monitorio y quiere oponerse.
  - El usuario necesita el burofax de requerimiento previo (intento de MASC) antes de reclamar.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - rol: el cliente reclama una cantidad (acreedor) / ha recibido un requerimiento de monitorio (deudor)
  - estado_reclamacion: sin reclamacion judicial iniciada / monitorio propio con oposicion del deudor
  - deuda_documentada: existen documentos que acreditan la deuda (si / no)
  - deuda_vencida_liquida: la cantidad esta vencida y su importe es fijo o calculable (si / no; si no, subclasificar en discutida o no vencida)
  - cuantia: importe reclamado en euros (determina verbal u ordinario en el declarativo)
  - es_arrendamiento: la cantidad deriva de rentas o cantidades debidas por arrendamiento de inmueble (si / no)
  - masc_intentado: se ha intentado un medio adecuado de solucion de controversias (si / no)
  - datos_parte_reclamante: nombre o razon social, NIF/CIF, domicilio, representante si persona juridica
  - datos_parte_contraria: nombre o razon social, NIF/CIF, domicilio o lugar donde pueda ser hallado
  - origen_deuda: descripcion del origen y relacion de documentos acreditativos
  - intereses: legales o pactados, y fecha desde la que se devengan
  - deudor_consumidor: la deuda se funda en un contrato entre empresario y consumidor (si / no)
  - partido_judicial: para la competencia territorial
  - datos_monitorio_previo: juzgado, numero de autos y cuantia (solo oposicion o demanda del Art. 818.2)
  - motivos_oposicion: alcance (total / parcial) y razones fundadas (solo oposicion)
outputs:
  - peticion_monitorio: peticion inicial de proceso monitorio en markdown, DRAFT
  - demanda_juicio_verbal: demanda de juicio verbal de reclamacion de cantidad en markdown, DRAFT
  - demanda_juicio_ordinario: demanda de juicio ordinario de reclamacion de cantidad en markdown, DRAFT
  - oposicion_monitorio: escrito de oposicion a proceso monitorio en markdown, DRAFT
  - burofax_masc: opcional, burofax de requerimiento previo de pago en markdown, DRAFT
references:
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-vias-reclamacion-cantidad.md
  - references/masc-requisito-procedibilidad-lo1-2025.md
assets:
  - assets/template-burofax-masc-reclamacion.md
  - assets/template-demanda-juicio-ordinario.md
  - assets/template-demanda-juicio-verbal.md
  - assets/template-oposicion-monitorio.md
  - assets/template-peticion-monitorio.md
---

# Reclamacion de Cantidad

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
    "posicion_cliente": {
      "type": "string",
      "description": "Posici\u00f3n del cliente (V1)",
      "enum": [
        "acreedor",
        "deudor"
      ]
    },
    "via_procesal": {
      "type": "string",
      "description": "V\u00eda procesal id\u00f3nea (V2)",
      "enum": [
        "burofax_masc",
        "monitorio",
        "juicio_verbal",
        "juicio_ordinario",
        "oposicion_monitorio"
      ]
    }
  },
  "required": [
    "posicion_cliente",
    "via_procesal"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = deudor requerido → **HOJA OPOSICION**: `assets/template-oposicion-monitorio.md`. V3-V6 no aplican.
- Si V1 = acreedor y V2 = monitorio con oposicion:
  - Cuantia > 15.000 euros → **HOJA ORDINARIO-818**: `assets/template-demanda-juicio-ordinario.md` (activar los bloques condicionales del Art. 818.2; V6 no aplica: la demanda trae causa del monitorio).
  - Cuantia <= 15.000 euros → **DETENER**: tras la oposicion, el asunto continua como juicio verbal dentro del mismo procedimiento (impugnacion de la oposicion en 10 dias, Art. 818.1 LEC); no procede una nueva demanda. Informar del cauce y del plazo, y ofrecer escalacion. No crear documento.
- Si V1 = acreedor, V2 = sin iniciar, V3 = si y V4 = vencida y liquida → **HOJA MONITORIO**: `assets/template-peticion-monitorio.md` (cualquier cuantia). Si V6 = no → generar ademas ANTES `assets/template-burofax-masc-reclamacion.md`.
- Si V1 = acreedor, V2 = sin iniciar y (V3 = no, o V4 = discutida/por determinar) → via declarativa:
  - Cuantia <= 15.000 euros, o rentas/cantidades de arrendamiento de inmueble (cualquier cuantia, Art. 250.1.1º LEC) → **HOJA VERBAL**: `assets/template-demanda-juicio-verbal.md`.
  - Cuantia > 15.000 euros (no arrendamiento) o interes economico imposible de calcular → **HOJA ORDINARIO**: `assets/template-demanda-juicio-ordinario.md`.
  - En ambas, si V6 = no → generar ademas ANTES `assets/template-burofax-masc-reclamacion.md` (requisito de procedibilidad, Arts. 264 y 403.2 LEC).
- Si V4 = pendiente de vencer → **DETENER**: la deuda no es exigible todavia; no cabe reclamarla judicialmente. Advertir y no crear documento.
- Si la pretension principal NO es el pago de una cantidad (materia del Art. 249.1 LEC, obligaciones de hacer, entrega de cosa) → **DETENER**: fuera de alcance; derivar a la skill correspondiente (`juicio-ordinario`) o a escalacion.

### Validacion de procedibilidad (interno, antes del Punto 3)

- **HOJA MONITORIO:** confirmar deuda dineraria, liquida, determinada, vencida y exigible con documento del Art. 812; competencia del Juzgado de Primera Instancia del domicilio del deudor (Art. 813, sin sumision); si el deudor es ilocalizable, advertir de la limitacion. Si la deuda se funda en contrato empresario-consumidor, anotar el control de oficio del Art. 815.4 para explicarlo en el Punto 5.
- **HOJA VERBAL / ORDINARIO:** verificar que la cuantia se puede fijar (Arts. 251-253); en verbal <= 2.000 euros, informar de que no son preceptivos abogado ni procurador (Arts. 23.2.1º y 31.2.1º) y de que existe formulario normalizado del CGPJ; en ordinario, abogado y procurador preceptivos.
- **HOJA ORDINARIO-818:** verificar que esta dentro del plazo de UN MES desde el traslado del escrito de oposicion (Art. 818.2). Si el plazo esta vencido o proximo a vencer, advertirlo de inmediato.
- **HOJA OPOSICION:** verificar que esta dentro del plazo de VEINTE DIAS desde el requerimiento (Art. 815.1). Si el plazo esta vencido, advertir del riesgo de despacho de ejecucion (Art. 816) y ofrecer escalacion. Si la cuantia reclamada excede de 2.000 euros, informar de que la oposicion requiere abogado y procurador.
- **MASC:** en las hojas iniciadoras con V6 = no, integrar el burofax previo (posicion conservadora, ver `references/masc-requisito-procedibilidad-lo1-2025.md`).

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Ley de Enjuiciamiento Civil (Arts. 249, 250, 437 y 812 a 818), Código Civil (Arts. 1.088, 1.091, 1.101, 1.108 y 1.124), y Ley Orgánica 1/2025 de medidas de eficiencia del servicio público de justicia.
2. **Orientación Legal del Caso:**
Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Indica al usuario que via procesal corresponde a su caso y por que, citando la norma con nombre completo y articulo, con el enlace del BOE consultado. Textos fijos por hoja (adaptar solo el dato de cuantia):
   - MONITORIO: "A su caso corresponde el proceso monitorio, regulado en los articulos 812 y siguientes de la Ley 1/2000, de Enjuiciamiento Civil, al tratarse de una deuda dineraria, liquida, vencida y exigible acreditada documentalmente, cualquiera que sea su cuantia. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - VERBAL: "A su caso corresponde el juicio verbal, conforme al articulo 250 de la Ley 1/2000, de Enjuiciamiento Civil, por no exceder la cuantia de 15.000 euros [o: por tratarse de rentas o cantidades debidas por arrendamiento de inmueble, articulo 250.1.1º]. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - ORDINARIO: "A su caso corresponde el juicio ordinario, conforme al articulo 249.2 de la Ley 1/2000, de Enjuiciamiento Civil, por exceder la cuantia de 15.000 euros. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - ORDINARIO-818: anadir ademas "Al haberse opuesto el deudor en el proceso monitorio, la demanda debe interponerse en el plazo de un mes desde el traslado del escrito de oposicion, conforme al articulo 818 de la misma ley."
   - OPOSICION: "Su escrito se rige por los articulos 815 y 818 de la Ley 1/2000, de Enjuiciamiento Civil: dispone de veinte dias desde el requerimiento para formular una oposicion fundada y motivada. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - Si la hoja incluye burofax previo (V6 = no), anadir: "Con caracter previo se preparara un burofax de requerimiento de pago, que acredita el intento de solucion extrajudicial exigido por la Ley Organica 1/2025 (articulos 264 y 403.2 de la Ley de Enjuiciamiento Civil). Tenga en cuenta que la demanda no debe presentarse hasta disponer del justificante del envio del burofax y haber dejado un plazo razonable de respuesta."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla del sistema, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (advierte si el documento adjuntado los incumple).
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-burofax-masc-reclamacion.md`).
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

**Propagacion de un dato confirmado (regla global de Edit):** varios datos (nombre y NIF de cada parte, cuantia) aparecen repetidos literalmente en mas de un punto del asset (encabezamiento/titulo, bloque de datos, cuerpo del EXPONE/HECHOS, SUPLICO y firma). Al confirmar el dato, sustituyelo mediante `Edit` en TODAS sus apariciones del documento, no solo en el bloque de datos donde se pregunto; verifica con `Read` que no queden placeholders sueltos del mismo dato ya confirmado.

### Secciones — HOJA MONITORIO / HOJA VERBAL / HOJA ORDINARIO / HOJA ORDINARIO-818

1. **Parte reclamante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte que reclama." Sub-apartados, uno por turno: a) nombre completo o razon social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) solo si es persona juridica: nombre, NIF y cargo del representante; e) solo en ORDINARIO y ORDINARIO-818 (y en VERBAL si la cuantia excede de 2.000 euros): nombre del procurador y del letrado. Al completar el ultimo, vista previa unica con todos los datos y una sola confirmacion antes del `Edit`.
2. **Parte deudora / demandada** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte deudora." Sub-apartados: a) nombre o razon social; b) NIF o CIF si se conoce; c) domicilio o lugar donde pueda ser hallada. Confirmacion agrupada.
3. **Origen de la deuda y prueba documental** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Abordamos ahora el origen de la deuda y su acreditacion documental." Antes de registrar la relacion de documentos, explica que documentos sirven para acreditar la deuda (en monitorio, los del articulo 812 de la LEC: firmados por el deudor, o facturas, albaranes y certificaciones habituales del trafico; en las demandas, los documentos fundamentales del articulo 265, con preclusion del 269) y confirma con el usuario cuales aportara y en que orden se numeraran. El origen y la fecha de vencimiento ya aportados en el mensaje inicial (escucha activa) no se vuelven a preguntar en bruto: se dan por confirmados y solo se solicitan los datos concretos que falten (numero e importe de cada documento, fecha exacta de cada vencimiento, fecha del contrato). Si hay mas de un documento con vencimientos distintos, recoge la fecha de cada uno y numeralos correlativamente en `{{relacion_documentos}}`; no fuerces una unica fecha de vencimiento cuando existan varias. Si no se desprende ya del origen descrito si el deudor actua como consumidor frente a un empresario, pregunta directamente: "¿El deudor contrato como consumidor particular o actuaba tambien como empresario o profesional?". Si la deuda se funda en un contrato entre empresario y consumidor, explica aqui el control de oficio de clausulas abusivas (articulo 815.4 LEC en el monitorio) y sus consecuencias antes de continuar.
4. **Cuantia, intereses y costas** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a la determinacion de la cuantia, los intereses y las costas." El principal ya resuelto en la clasificacion se reutiliza sin volver a preguntarlo. Explica la eleccion de intereses antes de pedir la decision: interes legal del dinero desde la constitucion en mora (articulos 1100 y 1108 del Codigo Civil, normalmente desde el requerimiento o el vencimiento) o interes pactado en el contrato si existe; y desde que fecha se devengan. Explica que las costas se solicitan conforme al articulo 394 de la LEC. En HOJA MONITORIO no incluyas una peticion expresa de costas en el SUPLICO: la peticion inicial no es todavia un procedimiento contencioso con sentencia; limitate a advertir de que, si el deudor se opone (paso a verbal u ordinario) o hay que instar la ejecucion, las costas de esas fases posteriores se rigen por sus normas especificas. Confirmacion una a una (intereses primero, costas despues).
5. **Juzgado competente** *(dato objetivo con validacion)*. Anuncio fijo: "Determinamos ahora el juzgado competente." En MONITORIO: partido judicial del domicilio o residencia del deudor (articulo 813 LEC, sin sumision a otro fuero: si el usuario propone otro, advertir y corregir). En VERBAL y ORDINARIO: fuero general del domicilio del demandado (articulos 50 y 51 LEC) salvo fuero especial aplicable. En ORDINARIO-818: el mismo juzgado que conocio del monitorio.
6. **Solucion previa (MASC)** *(solo si la hoja incluye burofax, clausula de negociacion)*. Anuncio fijo: "Concretamos por ultimo los terminos del requerimiento previo de pago." Sub-datos del burofax, uno por turno: plazo de pago que se concede (explicar que es practica habitual conceder 10 dias habiles), medio de pago (cuenta IBAN u otro) y via de contacto para negociar. Confirmacion una a una.
7. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Lugar de firma; la fecha por defecto es la del dia, salvo indicacion en contrario.

### Secciones — HOJA OPOSICION

1. **Datos del procedimiento** *(dato objetivo — confirmacion agrupada)*. Anuncio fijo: "Comenzamos por los datos del procedimiento que consta en el requerimiento recibido." Sub-apartados, uno por turno: a) juzgado (numero y partido judicial); b) numero de autos del monitorio; c) nombre del acreedor que reclama; d) cantidad reclamada; e) fecha en que recibio el requerimiento (para validar el plazo de veinte dias: si esta vencido, advertir y ofrecer escalacion antes de continuar). Confirmacion agrupada.
2. **Datos del cliente (deudor)** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a su identificacion como parte." Sub-apartados: a) nombre completo o razon social; b) NIF o CIF; c) domicilio; d) solo si la cuantia reclamada excede de 2.000 euros: nombre del procurador y del letrado (preceptivos; si no los tiene, advertir de que debe designarlos). Confirmacion agrupada.
3. **Alcance y motivos de la oposicion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Abordamos ahora el contenido de la oposicion." Explica antes de pedir la decision: la oposicion debe ser fundada y motivada (articulo 815.1 LEC), una negativa generica puede ser rechazada; puede ser total o parcial (pluspeticion: reconocer una parte y discutir el exceso); si la deuda deriva de un contrato con un empresario siendo el cliente consumidor, pueden alegarse clausulas abusivas. Pide el alcance (total o parcial, y en su caso la cantidad reconocida), despues los motivos concretos (prosa) y los documentos de apoyo. Confirmacion una a una (alcance, motivos, documentos).
4. **Efectos y via posterior** *(informativo, sin pregunta)*. Anuncio fijo: "Le informo de los efectos de la oposicion." Informar: hasta 15.000 euros el asunto sigue como juicio verbal (el acreedor podra impugnar la oposicion en diez dias); por encima, el acreedor debera demandar en juicio ordinario en un mes (articulo 818 LEC). No requiere dato del usuario; encadenar con la seccion siguiente.
5. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Igual que en las demas hojas.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo, HECHOS o ALEGACIONES numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

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

1. Verificar siempre la LEC en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder.
2. Si se detecta una version de la LEC o un modelo del CGPJ posterior al registrado en las references, actualizar los archivos del plugin antes de redactar. No usar una version desactualizada.
3. El monitorio solo procede con deuda dineraria, liquida, determinada, vencida y exigible acreditada con documento (Art. 812). Si falla cualquier requisito, enrutar al declarativo o detener; nunca forzar la via.
4. El umbral entre verbal y ordinario es 15.000 euros (Arts. 249.2 y 250.2); las rentas de arrendamiento van a verbal cualquiera que sea la cuantia (Art. 250.1.1º). No admitir elecciones de via contrarias a estos articulos aunque el usuario las pida.
5. Competencia del monitorio: exclusiva del Juzgado de Primera Instancia del domicilio del deudor (Art. 813). No admitir sumision a otro fuero.
6. Posicion conservadora sobre el MASC: en todo escrito iniciador sin intento previo acreditado, recomendar e integrar el burofax y advertir de la cuestion (LO 1/2025).
7. Plazos criticos: 20 dias para oponerse (Art. 815.1) y 1 mes para la demanda de ordinario tras la oposicion (Art. 818.2). Validarlos antes de redactar; si estan vencidos, advertir y no dar falsas expectativas.
8. Nunca inventar datos, cuantias, fechas ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.
9. Nunca afirmar que la deuda es exigible o incontrovertida sin base documental; nunca garantizar el resultado del procedimiento.
10. Si el deudor es consumidor y la deuda nace de un contrato con un empresario, informar siempre del control de oficio de clausulas abusivas (Art. 815.4 LEC) antes de cerrar la cuantia.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para pretensiones no dinerarias (entrega de cosa, obligaciones de hacer o no hacer) ni declarativas puras.
- No usar para materias del Art. 249.1 LEC cuya pretension principal no sea la condena al pago: derivar a la skill `juicio-ordinario`.
- No usar para reclamar a una Administracion Publica.
- No usar para desahucios por falta de pago (skill `desahucio`) ni para la ejecucion de titulos.
- No usar para redactar la impugnacion de la oposicion en el verbal transformado (Art. 818.1) ni la contestacion a una demanda: advertir y escalar.
- No usar si el usuario pide opinion juridica sobre la estrategia de un litigio: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
