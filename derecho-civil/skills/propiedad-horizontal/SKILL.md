---
name: propiedad-horizontal
description: >
  Genera el documento adecuado en materia de propiedad horizontal conforme a la Ley 49/1960 (LPH) y a la LEC
  verificadas en el BOE: certificacion del acuerdo de liquidacion de deuda (Art. 21.3 LPH), peticion inicial del
  proceso monitorio especial de cuotas de comunidad (Art. 21 LPH y Art. 812.2.2º LEC), demanda de juicio ordinario
  de impugnacion de acuerdos de junta (Art. 18 LPH y Art. 249.1.8º LEC) y requerimiento de cesacion de actividad
  prohibida o molesta del presidente al infractor (Art. 7.2 LPH). NO usar para la administracion de fincas
  (contabilidad, presupuestos, convocatorias, actas), para conflictos vecinales sin base en la LPH, para la
  redaccion de la demanda de cesacion ni para obras que afecten a la estructura o al titulo constitutivo.
when_to_use: |
  - Una comunidad de propietarios quiere reclamar judicialmente cuotas impagadas a un propietario.
  - Hace falta la certificacion del acuerdo de liquidacion de deuda para poder acudir al monitorio.
  - Un propietario quiere impugnar un acuerdo adoptado por la junta de propietarios.
  - La comunidad necesita requerir formalmente el cese de una actividad molesta, prohibida o no autorizada.
  - El presidente o el administrador pregunta que pasos previos exige la LPH antes de reclamar o de demandar.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - rol_cliente: la comunidad de propietarios (o su presidente, secretario o administrador) / un propietario a titulo individual
  - asunto_comunidad: impago de cuotas / actividad prohibida o molesta
  - asunto_propietario: impugnacion de un acuerdo de junta / otra cuestion
  - acuerdo_liquidacion: la junta ha aprobado ya la liquidacion de la deuda y autorizado la reclamacion (si / no)
  - datos_comunidad: denominacion, NIF, direccion de la finca, presidente y secretario o administrador
  - datos_deudor: nombre o razon social, NIF/CIF, elemento privativo, cuota de participacion, domicilio designado
  - desglose_deuda: conceptos, periodos, fechas de exigibilidad e importes; total
  - datos_junta_impugnada: fecha, tipo de junta, convocatoria, punto del orden del dia, texto del acuerdo, votacion
  - posicion_votacion: salvo el voto / ausente / privado indebidamente del voto / voto a favor
  - al_corriente_pago: el propietario impugnante esta al corriente o ha consignado (si / no / excepcion del Art. 18.2)
  - fecha_computo_plazo: fecha del acuerdo o, si el propietario estuvo ausente, de su comunicacion
  - datos_infractor: nombre, NIF/CIF, condicion de propietario u ocupante, elemento privativo, domicilio
  - descripcion_actividad: hechos verificables (fechas, horarios, mediciones, denuncias) y medios de acreditacion
  - requerimiento_previo: el presidente ha requerido ya fehacientemente la cesacion (no / si, sin acreditacion / si, acreditado)
outputs:
  - certificacion_deuda: certificacion del acuerdo de liquidacion de deuda en markdown, DRAFT
  - peticion_monitorio_lph: peticion inicial del monitorio especial de cuotas en markdown, DRAFT
  - demanda_impugnacion: demanda de juicio ordinario de impugnacion de acuerdos en markdown, DRAFT
  - requerimiento_cesacion: requerimiento del presidente al infractor en markdown, DRAFT
references:
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lph-reclamacion-y-acuerdos.md
  - references/masc-y-requisitos-previos-lph.md
assets:
  - assets/template-certificacion-deuda-comunidad.md
  - assets/template-demanda-impugnacion-acuerdos.md
  - assets/template-peticion-monitorio-cuotas-lph.md
  - assets/template-requerimiento-cesacion-actividad.md
---

# Propiedad Horizontal

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
      "description": "Posici\u00f3n del requirente / cliente (V1)",
      "enum": [
        "comunidad",
        "propietario"
      ]
    },
    "asunto_lph": {
      "type": "string",
      "description": "Asunto o pretensi\u00f3n a ejercitar (V2)",
      "enum": [
        "reclamacion_morosos",
        "certificacion_deuda",
        "impugnacion_acuerdos",
        "actividad_molesta"
      ]
    }
  },
  "required": [
    "posicion_cliente",
    "asunto_lph"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = comunidad y V2 = impago:
  - **V4 = si → HOJA CUOTAS**: se generan DOS documentos, en este orden: `assets/template-certificacion-deuda-comunidad.md` y despues `assets/template-peticion-monitorio-cuotas-lph.md`.
  - **V4 = no → HOJA CUOTAS-SIN-ACUERDO**: advertir de que el acuerdo de la junta que aprueba la liquidacion y autoriza la reclamacion es un requisito legal previo (articulos 21.1 a 21.3 de la Ley de Propiedad Horizontal) y de que sin el no cabe emitir la certificacion ni presentar la peticion. Generar unicamente `assets/template-certificacion-deuda-comunidad.md` como borrador, dejando como placeholders los datos del acuerdo, para emitirlo cuando la junta lo adopte. **NO** generar la peticion de monitorio en esta rama.
- Si V1 = comunidad y V2 = actividad:
  - **V6 = 1 o 2 → HOJA CESACION**: `assets/template-requerimiento-cesacion-actividad.md`. (En V6 = 2 se advierte de que el requerimiento anterior no sirve como presupuesto de la accion por no ser acreditable, y de que este lo sustituye.)
  - **V6 = 3 → DETENER**: el requerimiento ya esta cumplido y el paso siguiente es la accion de cesacion, que exige autorizacion de la junta debidamente convocada al efecto y se sustancia por juicio ordinario. Informar de la secuencia del articulo 7.2 de la Ley de Propiedad Horizontal, derivar a la skill `juicio-ordinario` y ofrecer escalacion. No crear documento.
- Si V1 = propietario y V3 = impugnacion:
  - **V5.a = 4 → DETENER**: quien voto a favor o se abstuvo sin salvar su voto no esta legitimado para impugnar (articulo 18.2 de la Ley de Propiedad Horizontal). Explicarlo y ofrecer escalacion. No crear documento.
  - **V5.a = 1, 2 o 3 y plazo vigente → HOJA IMPUGNACION**: `assets/template-demanda-impugnacion-acuerdos.md`.
  - **Plazo caducado → DETENER**: la accion caduca a los tres meses de adoptarse el acuerdo, o al año si es contrario a la ley o a los estatutos; para el ausente el computo arranca de la comunicacion del acuerdo (articulo 18.3). Advertir de la caducidad, no dar falsas expectativas y ofrecer escalacion. No crear documento.
  - **V5.b = 2 (deudas pendientes)**: no detiene el flujo, pero es un obstaculo. Ver la validacion de presupuestos.
- Si V1 = propietario y V3 = otra cuestion → **DETENER Y DERIVAR**: identificar la materia y derivar sin crear documento. Casos frecuentes: requerimiento de pago de un monitorio de la comunidad ya recibido (skill `reclamacion-cantidad`, escrito de oposicion, plazo de veinte dias); reclamacion de cantidad frente a la comunidad por daños (skill `reclamacion-cantidad`); cuestiones arrendaticias del piso (skills `arrendamiento` o `desahucio`). Si no encaja en ninguna, ofrecer escalacion.

### Validacion de presupuestos (interno, antes del Punto 3)

- **HOJA CUOTAS:** comprobar que existe acuerdo de junta aprobando la liquidacion y autorizando la reclamacion; que quien va a firmar la certificacion ejerce las funciones de secretario; y si el visto bueno del presidente es necesario o concurre la excepcion del articulo 21.3 (secretario-administrador con cualificacion profesional legalmente reconocida que no vaya a intervenir profesionalmente en la reclamacion). Comprobar que la deuda puede desglosarse por concepto y periodo. Si el deudor no ha designado domicilio, anotar la regla del articulo 815.2 de la LEC (notificacion en el propio piso o local) para explicarla en el Punto 5.
- **HOJA CUOTAS-SIN-ACUERDO:** ademas de lo anterior, advertir de que la junta debe incluir el punto en el orden del dia y de que la certificacion no puede emitirse antes.
- **HOJA IMPUGNACION:** verificar la legitimacion (articulo 18.2), el plazo de caducidad (articulo 18.3, computado desde el acuerdo o desde su comunicacion al ausente) y el requisito de estar al corriente de pago, con la excepcion legal de los acuerdos sobre establecimiento o alteracion de las cuotas de participacion del articulo 9. Si el cliente estuvo ausente, comprobar si comunico su discrepancia dentro de los treinta dias naturales del articulo 17.8 y advertir de las consecuencias si no lo hizo. Abogado y procurador son preceptivos.
- **HOJA CESACION:** verificar que quien requiere es el presidente (o que actua por su cuenta a iniciativa de un propietario u ocupante) y que la conducta encaja en alguno de los tres supuestos del articulo 7.2, o en el articulo 7.3 si se trata de alquiler de uso turistico sin aprobacion de la comunidad. Comprobar si el infractor es propietario u ocupante.
- **MASC:** en la HOJA IMPUGNACION es exigible el intento previo de solucion (articulos 264.4º y 403.2 de la LEC). En la HOJA CUOTAS la cuestion es discutida: posicion conservadora, aprovechar la notificacion de la deuda y advertir. Ver `references/masc-y-requisitos-previos-lph.md`.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Ley 49/1960, de 21 de julio, sobre Propiedad Horizontal (LPH): Art. 7.2 (actividades prohibidas y acción de cesación), Art. 9.1.e (obligación contributiva y afección real), Art. 18 (impugnación de acuerdos, plazos de 3 meses o 1 año y requisito de estar al corriente de pago), y Art. 21 (proceso monitorio especial de reclamación de cuotas).
2. **Orientación Legal del Caso:**
Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa el cauce y la fuente aplicable.** Indica que documento corresponde a su caso y por que, citando la norma con nombre completo y articulo, con el enlace del BOE consultado. Textos fijos por hoja:
   - CUOTAS: "A su caso corresponde el proceso monitorio especial de comunidades de propietarios, regulado en el articulo 21 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal, en relacion con el articulo 812.2.2º de la Ley 1/2000, de Enjuiciamiento Civil. Prepararemos primero la certificacion del acuerdo de liquidacion de la deuda, que es el documento que la ley exige acompanar, y despues la peticion inicial. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"
   - CUOTAS-SIN-ACUERDO: anadir al texto anterior "Tenga en cuenta que la reclamacion requiere un acuerdo previo de la junta que apruebe la liquidacion de la deuda y autorice su reclamacion judicial, conforme a los articulos 21.1 y 21.2 de la misma ley. Prepararemos ahora la certificacion para que pueda emitirse en cuanto la junta lo adopte; la peticion inicial no debe presentarse antes."
   - IMPUGNACION: "A su caso corresponde la impugnacion de acuerdos de la junta, regulada en el articulo 18 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal, que se sustancia por los tramites del juicio ordinario conforme al articulo 249.1.8º de la Ley 1/2000, de Enjuiciamiento Civil, cualquiera que sea la cuantia. La accion caduca a los tres meses desde la adopcion del acuerdo, o al año si el acuerdo es contrario a la ley o a los estatutos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"
   - CESACION: "A su caso corresponde el requerimiento previo de cesacion del articulo 7.2 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal, que el presidente debe dirigir al infractor antes de que la comunidad pueda ejercitar la accion de cesacion. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"
   - En IMPUGNACION, anadir siempre: "Antes de presentar la demanda debera acreditarse el intento de solucion extrajudicial exigido por la Ley Organica 1/2025 (articulos 264 y 403.2 de la Ley de Enjuiciamiento Civil). La solicitud de negociacion suspende el plazo de caducidad, pero no conviene apurarlo."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla del sistema, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (advierte si el documento adjuntado los incumple, en particular si la certificacion carece de desglose o de las firmas exigidas por el articulo 21.3).
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-certificacion-deuda-comunidad.md`).
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

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las secciones marcadas como de negociacion se explican y se confirman una a una.

### Secciones — HOJA CUOTAS y HOJA CUOTAS-SIN-ACUERDO

1. **Datos de la comunidad** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la comunidad de propietarios." Sub-apartados, uno por turno: a) denominacion; b) NIF; c) direccion completa de la finca; d) nombre y NIF de quien ejerce las funciones de secretario o secretario-administrador, y su cargo exacto; e) nombre del presidente. Antes de cerrar el bloque, si el secretario es un administrador profesional, pregunta si va a intervenir profesionalmente en la reclamacion, porque de ello depende que sea o no necesario el visto bueno del presidente (articulo 21.3). Al completar el ultimo, vista previa unica con todos los datos y una sola confirmacion antes del `Edit`.
2. **Datos del propietario deudor** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion del propietario deudor." Sub-apartados: a) nombre o razon social; b) NIF o CIF si se conoce; c) elemento privativo (piso, letra, planta, plaza o local); d) cuota de participacion; e) domicilio designado por el deudor para las notificaciones de la comunidad. Si no ha designado ninguno, explicar que el requerimiento judicial se practicara en el propio piso o local (articulo 815.2 de la LEC) y hacerlo constar. Confirmacion agrupada.
3. **Acuerdo de la junta y notificacion de la deuda** *(dato objetivo con validacion)*. Anuncio fijo: "Abordamos ahora el acuerdo de la junta y su notificacion al deudor." Sub-apartados, uno por turno: a) fecha y tipo de la junta y punto del orden del dia; b) persona facultada por la junta para reclamar; c) fecha y medio de notificacion del acuerdo al deudor; d) solo si la notificacion personal fracaso: fechas de inicio y fin de la publicacion en el tablon de anuncios, verificando que cubre al menos tres dias. En la HOJA CUOTAS-SIN-ACUERDO, los datos a) y b) quedan como placeholders y se advierte de ello sin preguntarlos.
4. **Desglose de la deuda** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a determinar la deuda y su desglose." Antes de pedir cifras, explica que pueden reclamarse todas las cantidades debidas por gastos comunes, ordinarios o extraordinarios, generales o individualizables, y las aportaciones al fondo de reserva (articulo 21.2), asi como las cuotas aprobadas que se devenguen hasta la notificacion de la deuda (articulo 21.3); y explica que la ley exige el desglose y no admite un importe global. Recoge despues, concepto a concepto, periodo, fecha de exigibilidad e importe, y calcula el total. Verifica que la suma cuadra antes de escribirla.
5. **Intereses y gastos de la reclamacion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos ahora los intereses y los gastos de la reclamacion." Explica antes de pedir la decision: los creditos de la comunidad devengan intereses desde el momento en que debio hacerse cada pago (articulo 21.1), sin necesidad de requerimiento; la junta puede haber acordado medidas disuasorias, que no pueden ser abusivas ni desproporcionadas ni retroactivas; y pueden repercutirse al deudor los gastos y costes de la reclamacion, incluidos los del secretario administrador (articulo 21.3). Confirmacion una a una (intereses primero, gastos despues).
6. **Contra quien se dirige la reclamacion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos contra quien se dirige la reclamacion." Explica antes de decidir: cabe demandar al titular registral a efectos de soportar la ejecucion sobre el inmueble (articulo 21.2); si el piso cambio de manos, el adquirente responde con el propio inmueble de lo debido en la anualidad en curso y los tres años naturales anteriores, por la afeccion real del articulo 9.1.e); y el propietario anterior que no comunico la transmision responde solidariamente de las deudas posteriores (articulo 9.1.i). Pregunta despues si el piso ha cambiado de titularidad y si desea dirigir la reclamacion tambien contra alguno de ellos.
7. **Juzgado competente** *(decision con explicacion)*. Anuncio fijo: "Determinamos ahora el juzgado competente." Explica que la comunidad puede elegir entre el juzgado del domicilio o residencia del deudor y el del lugar donde se halla la finca (articulo 813 de la LEC), que no cabe sumision a otro fuero, y pide la eleccion. Si el usuario propone un fuero distinto, advertir y corregir.
8. **Postulacion y embargo preventivo** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Cerramos con la intervencion profesional y las medidas frente a una eventual oposicion." Explica: no son preceptivos abogado ni procurador para la peticion inicial, pero si se utilizan sus honorarios y derechos son repercutibles al deudor con los limites del articulo 394.3 de la LEC (articulo 21.5); y que, si el deudor se opone, cabe pedir el embargo preventivo de sus bienes, que el tribunal acordara en todo caso y sin caucion (articulo 21.4). Pregunta si intervienen procurador y letrado y si desea anunciar el embargo preventivo. Confirmacion una a una.
9. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del documento." Lugar de firma; la fecha por defecto es la del dia, salvo indicacion en contrario.

Las secciones 1 a 6 rellenan la certificacion (comunidad, deudor, acuerdo y notificacion, desglose, intereses y gastos, contra quien se dirige la reclamacion). Las secciones 7 (juzgado competente) y 8 (postulacion y embargo preventivo) no tienen campo alguno en la certificacion: se preguntan por primera vez al construir la peticion inicial, inmediatamente despues de cerrar la certificacion. La seccion 9 (lugar y fecha) se responde dos veces con sentido distinto: la fecha de la certificacion al cerrar esta, y la fecha de la peticion al construirla, que puede no coincidir; el lugar, si no cambia, no se vuelve a preguntar. Al terminar la certificacion, encadenar con la creacion de la peticion inicial (solo en la HOJA CUOTAS) sin repetir ninguna pregunta ya respondida: los datos de las secciones 1 a 6 se vuelcan directamente.

### Secciones — HOJA IMPUGNACION

1. **Datos del propietario demandante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por su identificacion como parte demandante." Sub-apartados, uno por turno: a) nombre completo o razon social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) elemento privativo y cuota de participacion; e) nombre del procurador y del letrado, preceptivos en el juicio ordinario. Confirmacion agrupada.
2. **Datos de la comunidad demandada** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la comunidad demandada." Sub-apartados: a) denominacion; b) NIF si se conoce; c) direccion de la finca; d) nombre del presidente, que es quien la representa en juicio. Confirmacion agrupada.
3. **La junta y el acuerdo impugnado** *(dato objetivo con validacion)*. Anuncio fijo: "Abordamos ahora la junta y el acuerdo que se impugna." Sub-apartados, uno por turno: a) fecha y tipo de junta; b) fecha y medio de la convocatoria; c) punto del orden del dia; d) texto literal del acuerdo tal como consta en el acta; e) resultado de la votacion (votos a favor, en contra, abstenciones y cuotas que representan). Valida el sentido de las respuestas: si el resultado de la votacion no cuadra con el acuerdo descrito, dialoga y pide aclaracion antes de escribirlo.
4. **Legitimacion y plazo** *(dato objetivo con validacion y advertencia)*. Anuncio fijo: "Verificamos ahora su legitimacion y el plazo para impugnar." La posicion en la votacion ya esta resuelta y NO se vuelve a preguntar. Sub-apartados que si se piden: a) si consta en el acta la constancia de su voto en contra, o la fecha en que se le comunico el acuerdo si estuvo ausente; b) solo si estuvo ausente: si comunico su discrepancia al secretario dentro de los treinta dias naturales siguientes, explicando antes que, de no hacerlo, su voto se computa como favorable (articulo 17.8) y ello debilita la impugnacion. Calcula el plazo y adviertelo expresamente: tres meses desde el acuerdo, o un año si es contrario a la ley o a los estatutos.
5. **Situacion de pago** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Tratamos ahora el requisito de estar al corriente de pago." Explica: para impugnar hay que estar al corriente de todas las deudas vencidas o consignarlas judicialmente antes de demandar (articulo 18.2), con la unica excepcion de los acuerdos sobre establecimiento o alteracion de las cuotas de participacion del articulo 9. Si el cliente tiene deudas pendientes, explica las dos salidas (pagar o consignar) y sus consecuencias antes de continuar; no redactes la demanda dando por resuelto el requisito.
6. **Motivos de la impugnacion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a los motivos de la impugnacion." Explica los tres supuestos del articulo 18.1 (acuerdo contrario a la ley o a los estatutos; gravemente lesivo para la comunidad en beneficio de uno o varios propietarios; grave perjuicio para un propietario sin obligacion de soportarlo o adoptado con abuso de derecho) y, si el motivo es de mayorias, contrasta el acuerdo con el cuadro del articulo 17 recogido en `references/lph-reclamacion-y-acuerdos.md`. Elige con el cliente el supuesto y recoge despues los motivos concretos en prosa y los documentos que los acreditan. Confirmacion una a una.
7. **Suspension cautelar del acuerdo** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Valoramos ahora si conviene pedir la suspension del acuerdo." Explica: la impugnacion NO suspende la ejecucion del acuerdo; la suspension debe pedirse como medida cautelar, se acuerda oida la comunidad, exige justificar apariencia de buen derecho y peligro por la mora procesal, y normalmente conlleva prestar caucion (articulo 18.4 y articulos 721 y siguientes de la LEC). Pregunta despues si desea solicitarla y con que justificacion.
8. **Peticion adicional del suplico** *(clausula de negociacion)*. Anuncio fijo: "Concretamos que mas debe pedirse en la demanda ademas de la nulidad del acuerdo." Ejemplos que puedes ofrecer: devolucion de derramas ya cobradas, reposicion a la situacion anterior, condena a adoptar un nuevo acuerdo con la mayoria correcta. Si no hay ninguna, retirar el punto del suplico en lugar de dejarlo vacio.
9. **Intento de solucion previa** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Cerramos con el intento de solucion previa exigido antes de demandar." Explica que debe acreditarse el intento de negociacion (articulos 264.4º y 403.2 de la LEC) y que la solicitud de negociacion, si define bien su objeto, suspende el plazo de caducidad (articulo 7.1 de la Ley Organica 1/2025), pero que el computo se reanuda si no hay respuesta en treinta dias naturales. Recoge el tipo de intento y su fecha; si aun no se ha hecho, dejalo como placeholder y advierte de que la demanda no debe presentarse sin ese documento.
10. **Juzgado, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el juzgado, el lugar y la fecha del escrito." Partido judicial en el que radica la finca; lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA CESACION

1. **Datos de la comunidad y del presidente** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la comunidad y de quien firma el requerimiento." Sub-apartados: a) denominacion de la comunidad; b) NIF; c) direccion de la finca; d) nombre y NIF del presidente. Confirmacion agrupada.
2. **Datos del infractor** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de quien desarrolla la actividad." Sub-apartados: a) nombre o razon social; b) NIF o CIF si se conoce; c) si es propietario u ocupante del elemento privativo; d) elemento privativo; e) domicilio a efectos de notificaciones. Si es ocupante y no propietario, advierte de que conviene remitir copia al propietario, porque la eventual demanda debe dirigirse contra ambos (articulo 7.2). Confirmacion agrupada.
3. **Descripcion de la actividad** *(dato objetivo con validacion de sentido)*. Anuncio fijo: "Abordamos ahora la descripcion de la actividad." Pide los hechos con concrecion: en que consiste, desde cuando, con que frecuencia, en que horario y a quien afecta. No aceptes calificativos como unica respuesta ("es un escandalo", "son unos incivicos"): si la respuesta no aporta hechos verificables, explica por que no sirve y pide datos concretos antes de escribirla.
4. **Acreditacion** *(dato objetivo)*. Anuncio fijo: "Pasamos a los medios con los que se acredita." Recoge que pruebas existen: denuncias presentadas, actas de la policia local, mediciones sonometricas, informes tecnicos, actas de junta, comunicaciones previas, testimonios de vecinos.
5. **Fundamento de la prohibicion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora en que se apoya la prohibicion." Explica las tres vias del articulo 7.2 (actividad prohibida en los estatutos; actividad dañosa para la finca; actividad que contraviene las disposiciones generales sobre actividades molestas, insalubres, nocivas, peligrosas o ilicitas) y, si se trata de alquiler de uso turistico, el regimen del articulo 7.3 y la mayoria de tres quintos del articulo 17.12. Elige con el cliente la via y recoge su justificacion. Si invoca los estatutos, pide la clausula concreta.
6. **Plazo de cesacion y medidas solicitadas** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos el plazo y las medidas que se le exigen." Explica que la ley habla de cesacion inmediata, y que fijar ademas un plazo breve y razonable (practica habitual: entre diez y quince dias) refuerza la posicion de la comunidad sin debilitar la exigencia. Recoge el plazo y las medidas concretas que se piden.
7. **Ofrecimiento de solucion negociada** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Incluimos un ofrecimiento de solucion negociada." Explica que incorporar un ofrecimiento expreso de dialogo y un canal de contacto permite que el mismo documento sirva como intento de solucion previa si la comunidad tiene que demandar despues. Recoge la via de contacto.
8. **Consecuencias que se advierten** *(informativo, sin pregunta)*. Anuncio fijo: "Le informo de las consecuencias que se advertiran en el requerimiento." Expon lo que la sentencia estimatoria puede acordar: cesacion definitiva, indemnizacion de daños y perjuicios, privacion del derecho al uso de la vivienda o local por tiempo no superior a tres años y, si el infractor no es el propietario, extincion de sus derechos y lanzamiento inmediato. Recuerda ademas que el paso siguiente exige autorizacion de la junta debidamente convocada al efecto. No requiere dato del usuario; encadenar con la seccion siguiente.
9. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del requerimiento."

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo, hechos numerados con una idea por apartado, documentos relacionados y numerados, desglose en tabla en lugar de prosa, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

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

1. Verificar siempre la LPH y la LEC en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder.
2. Si se detecta una version del texto consolidado posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario. No usar una version desactualizada.
3. La reclamacion de cuotas exige acuerdo previo de la junta que apruebe la liquidacion y autorice la reclamacion (articulos 21.1 y 21.2). Sin ese acuerdo no se genera la peticion inicial, por mucho que el usuario insista.
4. La certificacion debe expresar el importe adeudado Y SU DESGLOSE (articulo 21.3). Nunca emitir una certificacion con un importe global.
5. El visto bueno del presidente solo puede omitirse en el supuesto tasado del articulo 21.3 (secretario-administrador con cualificacion profesional legalmente reconocida que no vaya a intervenir profesionalmente en la reclamacion). No admitir otras excepciones.
6. La legitimacion para impugnar es tasada (articulo 18.2): quien voto a favor o se abstuvo sin salvar su voto no puede impugnar. No redactar la demanda en ese caso.
7. El requisito de estar al corriente de pago del articulo 18.2 solo decae para los acuerdos sobre establecimiento o alteracion de las cuotas de participacion del articulo 9. No extender la excepcion a otros acuerdos.
8. Los plazos del articulo 18.3 son de CADUCIDAD y no se interrumpen por reclamacion extrajudicial. Calcularlos siempre y advertir de su vencimiento; nunca dar por buena una impugnacion fuera de plazo.
9. Nunca afirmar que la impugnacion suspende el acuerdo: la suspension es cautelar, se pide, se justifica y suele exigir caucion (articulo 18.4).
10. El requerimiento del presidente es presupuesto de la accion de cesacion y debe ser fehaciente (articulo 7.2). Nunca presentar el requerimiento como si fuera ya la demanda, ni prometer la privacion del uso como resultado seguro.
11. Nunca inventar datos, importes, cuotas de participacion, fechas de junta, contenido de estatutos ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.
12. Si el usuario invoca estatutos o titulo constitutivo con reglas distintas de las legales, no suponer su contenido: pedirlos o escalar.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No es una herramienta de administracion de fincas: no elabora presupuestos, contabilidad, cuentas anuales, cuotas ni derramas.
- No convoca juntas, no redacta ordenes del dia ni levanta actas.
- No resuelve conflictos vecinales que carezcan de base en la Ley de Propiedad Horizontal (ruidos entre viviendas sin infraccion, discusiones personales, animales de compania sin prohibicion estatutaria ni infraccion administrativa): advertir y, en su caso, derivar.
- No redacta la demanda de la accion de cesacion del articulo 7.2 ni la demanda de juicio ordinario posterior a la oposicion en el monitorio: derivar a `juicio-ordinario` y escalar.
- No redacta la oposicion del propietario al monitorio de la comunidad: derivar a `reclamacion-cantidad` (plazo de veinte dias, que debe advertirse de inmediato).
- No se usa para reclamar cantidades que no sean gastos comunes ni fondo de reserva (por ejemplo, daños causados por un propietario a otro): derivar a `reclamacion-cantidad`.
- No emite dictamenes sobre la validez de estatutos, la interpretacion del titulo constitutivo ni la naturaleza de un elemento comun o privativo: escalar.
- No sustituye la lectura de los estatutos ni del titulo constitutivo, que pueden alterar el regimen legal supletorio.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
