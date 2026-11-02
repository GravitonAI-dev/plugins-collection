---
name: propiedad-horizontal
title: Propiedad horizontal
i18n:
  en:
    name: condominium-law
    title: Condominium law
    description: >
      Generates the right document in condominium matters under **Law 49/1960 on Horizontal
      Property (LPH)**, which governs owners' associations, their resolutions and fees, and the
      **Civil Procedure Act (Law 1/2000, LEC)**, verified in the BOE: certification of the debt
      settlement resolution (Art. 21.3 LPH), initial petition for the special order-for-payment
      procedure for community fees (Art. 21 LPH and Art. 812.2.2 LEC), ordinary claim
      challenging owners' meeting resolutions (Art. 18 LPH and Art. 249.1.8 LEC) and the
      president's demand to cease a prohibited or nuisance activity (Art. 7.2 LPH). Do not use
      for property management (accounting, budgets, meeting notices, minutes), for neighbour
      disputes without basis in the LPH, for drafting the cessation claim, or for works
      affecting the structure or the constitutive title.
description: >
  Genera el documento adecuado en materia de propiedad horizontal conforme a la **Ley 49/1960 de Propiedad Horizontal (LPH)**, que regula las comunidades de propietarios, sus acuerdos y las cuotas, y a la **Ley 1/2000 de Enjuiciamiento Civil (LEC)** verificadas en el BOE: certificación del acuerdo de liquidación de deuda (Art. 21.3 LPH), petición inicial del
  proceso monitorio especial de cuotas de comunidad (Art. 21 LPH y Art. 812.2.2º LEC), demanda de juicio ordinario
  de impugnación de acuerdos de junta (Art. 18 LPH y Art. 249.1.8º LEC) y requerimiento de cesación de actividad
  prohibida o molesta del presidente al infractor (Art. 7.2 LPH). NO usar para la administración de fincas
  (contabilidad, presupuestos, convocatorias, actas), para conflictos vecinales sin base en la LPH, para la
  redacción de la demanda de cesación ni para obras que afecten a la estructura o al título constitutivo.
when_to_use: |
  - Una comunidad de propietarios quiere reclamar judicialmente cuotas impagadas a un propietario.
  - Hace falta la certificación del acuerdo de liquidación de deuda para poder acudir al monitorio.
  - Un propietario quiere impugnar un acuerdo adoptado por la junta de propietarios.
  - La comunidad necesita requerir formalmente el cese de una actividad molesta, prohibida o no autorizada.
  - El presidente o el administrador pregunta qué pasos previos exige la LPH antes de reclamar o de demandar.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - rol_cliente: la comunidad de propietarios (o su presidente, secretario o administrador) / un propietario a título individual
  - asunto_comunidad: impago de cuotas / actividad prohibida o molesta
  - asunto_propietario: impugnación de un acuerdo de junta / otra cuestión
  - acuerdo_liquidacion: la junta ha aprobado ya la liquidación de la deuda y autorizado la reclamación (sí / no)
  - datos_comunidad: denominación, NIF, dirección de la finca, presidente y secretario o administrador
  - datos_deudor: nombre o razón social, NIF/CIF, elemento privativo, cuota de participación, domicilio designado
  - desglose_deuda: conceptos, periodos, fechas de exigibilidad e importes; total
  - datos_junta_impugnada: fecha, tipo de junta, convocatoria, punto del orden del día, texto del acuerdo, votación
  - posicion_votacion: salvo el voto / ausente / privado indebidamente del voto / voto a favor
  - al_corriente_pago: el propietario impugnante está al corriente o ha consignado (sí / no / excepción del Art. 18.2)
  - fecha_computo_plazo: fecha del acuerdo o, si el propietario estuvo ausente, de su comunicación
  - datos_infractor: nombre, NIF/CIF, condición de propietario u ocupante, elemento privativo, domicilio
  - descripcion_actividad: hechos verificables (fechas, horarios, mediciones, denuncias) y medios de acreditación
  - requerimiento_previo: el presidente ha requerido ya fehacientemente la cesación (no / sí, sin acreditación / sí, acreditado)
outputs:
  - certificacion_deuda: certificación del acuerdo de liquidación de deuda en markdown, DRAFT
  - peticion_monitorio_lph: petición inicial del monitorio especial de cuotas en markdown, DRAFT
  - demanda_impugnacion: demanda de juicio ordinario de impugnación de acuerdos en markdown, DRAFT
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

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación —cuyo catálogo y su correspondencia con las respuestas del formulario figuran en la Fase 1.2— y el origen de la plantilla (`origen_plantilla`).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas (por ejemplo, anotar un vector como resuelto) son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la naturaleza del caso y fijar los vectores deterministas de estado.

### 1.1 Escucha Activa Previa
Antes de abrir formularios interactivos o hacer preguntas, analiza el mensaje inicial del usuario y la documentación aportada:
- Si el mensaje ya especifica inequívocamente los vectores de la operación, asígnalos de forma inmediata y silenciosa en memoria y pasa a la **Fase 2**.
- Si restan vectores por definir, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado interactivo mediante la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las opciones de triaje:

```json
{
  "form_data": [
    {
      "id": "rol_cliente",
      "rationale": "Resolver V1: la comunidad y el propietario individual tienen acciones y assets distintos.",
      "question": "¿A quién asiste usted?",
      "options": [
        {"id": "comunidad", "label": "A la comunidad de propietarios, o a su presidente, secretario o administrador"},
        {"id": "propietario", "label": "A un propietario a título individual"}
      ]
    },
    {
      "id": "asunto",
      "rationale": "Resolver V2: determina el asset y el régimen de la Ley de Propiedad Horizontal aplicable.",
      "question": "¿Cuál es el asunto?",
      "options": [
        {"id": "impago_cuotas", "label": "Impago de cuotas de comunidad"},
        {"id": "actividad_molesta", "label": "Actividad prohibida, molesta, insalubre o peligrosa en un elemento privativo"},
        {"id": "impugnacion_acuerdo", "label": "Impugnación de un acuerdo de la junta de propietarios"}
      ]
    },
    {
      "id": "acuerdo_liquidacion",
      "rationale": "Resolver V3: el acuerdo de la junta que aprueba la liquidación de la deuda y autoriza la reclamación es requisito legal previo del monitorio de cuotas.",
      "question": "Si el asunto es un impago de cuotas, ¿ha aprobado ya la junta la liquidación de la deuda y autorizado su reclamación?",
      "show_if": {"question_id": "asunto", "option_ids": ["impago_cuotas"]},
      "options": [
        {"id": "si", "label": "Sí, hay acuerdo de junta"},
        {"id": "no", "label": "No, todavía no"},
        {"id": "no_procede", "label": "No procede: el asunto no es un impago de cuotas"}
      ]
    },
    {
      "id": "estado_requerimiento",
      "rationale": "Resolver V4: determina si procede el requerimiento de cesación o si el paso siguiente es ya la acción judicial de cesación, que exige autorización de la junta.",
      "question": "Si el asunto es una actividad molesta, ¿en qué estado está el requerimiento?",
      "show_if": {"question_id": "asunto", "option_ids": ["actividad_molesta"]},
      "options": [
        {"id": "sin_requerir", "label": "No se ha requerido todavía"},
        {"id": "requerido_informalmente", "label": "Se ha requerido, pero sin constancia fehaciente"},
        {"id": "requerido_y_desatendido", "label": "Se requirió fehacientemente y no se ha atendido"},
        {"id": "no_procede", "label": "No procede: el asunto no es una actividad molesta"}
      ]
    },
    {
      "id": "sentido_del_voto",
      "rationale": "Resolver V5: solo está legitimado para impugnar quien voto en contra, salvo su voto o estuvo ausente (artículo 18.2 de la Ley de Propiedad Horizontal). Preguntar únicamente si V2 = impugnacion_acuerdo.",
      "question": "Si el asunto es la impugnación de un acuerdo, ¿cuál fue la posición del cliente en la junta que lo adoptó?",
      "show_if": {"question_id": "asunto", "option_ids": ["impugnacion_acuerdo"]},
      "options": [
        {"id": "voto_en_contra", "label": "Votó en contra"},
        {"id": "salvo_su_voto", "label": "Se abstuvo salvando su voto"},
        {"id": "ausente", "label": "No asistió a la junta"},
        {"id": "voto_a_favor_o_abstencion", "label": "Votó a favor, o se abstuvo sin salvar su voto"},
        {"id": "no_procede", "label": "No procede: el asunto no es una impugnación"}
      ]
    },
    {
      "id": "al_corriente_de_pago",
      "rationale": "Resolver V6: la impugnación exige estar al corriente en el pago de las deudas vencidas con la comunidad, o haberlas consignado judicialmente (artículo 18.2 de la Ley de Propiedad Horizontal). Preguntar únicamente si V2 = impugnacion_acuerdo.",
      "question": "Si el asunto es la impugnación de un acuerdo, ¿está el cliente al corriente en el pago de las cuotas, o las ha consignado judicialmente?",
      "show_if": {"question_id": "asunto", "option_ids": ["impugnacion_acuerdo"]},
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No, tiene deudas pendientes"},
        {"id": "no_procede", "label": "No procede: el asunto no es una impugnación"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `rol_cliente`
- `V2` — `asunto`
- `V3` — `acuerdo_liquidacion`
- `V4` — `estado_requerimiento`
- `V5` — `sentido_del_voto`
- `V6` — `al_corriente_de_pago`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si V1 = comunidad y V2 = impago_cuotas:
  - **V3 = si → HOJA CUOTAS**: se generan DOS documentos, en este orden: `assets/template-certificacion-deuda-comunidad.md` y después `assets/template-peticion-monitorio-cuotas-lph.md`.
  - **V3 = no → HOJA CUOTAS-SIN-ACUERDO**: advertir de que el acuerdo de la junta que aprueba la liquidación y autoriza la reclamación es un requisito legal previo (artículos 21.1 a 21.3 de la Ley de Propiedad Horizontal) y de que sin el no cabe emitir la certificación ni presentar la petición. Generar únicamente `assets/template-certificacion-deuda-comunidad.md` como borrador, dejando como placeholders los datos del acuerdo, para emitirlo cuando la junta lo adopte. **NO** generar la petición de monitorio en esta rama.
  - **V3 = no_procede → DETENER** la elección de hoja: la respuesta es incoherente, porque el asunto es un impago de cuotas y la pregunta sobre el acuerdo de la junta si procede. Aclarar en el chat (REG-VAL-01) si la junta aprobó ya la liquidación, y volver a resolver V3. No crear documento hasta resolverlo.
- Si V1 = comunidad y V2 = actividad_molesta:
  - **V4 = sin requerir o requerido informalmente → HOJA CESACIÓN**: `assets/template-requerimiento-cesacion-actividad.md`. (En V4 = requerido_informalmente se advierte de que el requerimiento anterior no sirve como presupuesto de la acción por no ser acreditable, y de que este lo sustituye.)
  - **V4 = requerido_y_desatendido → DETENER**: el requerimiento ya está cumplido y el paso siguiente es la acción de cesación, que exige autorización de la junta debidamente convocada al efecto y se sustancia por juicio ordinario. Informar de la secuencia del artículo 7.2 de la Ley de Propiedad Horizontal, derivar a la skill `juicio-ordinario` y ofrecer escalación. No crear documento.
  - **V4 = no_procede → DETENER** la elección de hoja: la respuesta es incoherente, porque el asunto es una actividad molesta y la pregunta sobre el requerimiento si procede. Aclarar en el chat (REG-VAL-01) en que estado está el requerimiento, y volver a resolver V4. No crear documento hasta resolverlo.
- Si V1 = comunidad y V2 = impugnacion_acuerdo → **DETENER Y DERIVAR**: la comunidad no impugna sus propios acuerdos; si lo que se pretende es defenderla frente a la impugnación de un propietario, es una contestación a la demanda, que esta skill no cubre. Explicarlo y ofrecer escalación. No crear documento.
- Si V1 = propietario y V2 = impugnacion_acuerdo:
  - **V5 = voto_a_favor_o_abstencion → DETENER**: quien voto a favor o se abstuvo sin salvar su voto no está legitimado para impugnar (artículo 18.2 de la Ley de Propiedad Horizontal). Explicarlo y ofrecer escalación. No crear documento.
  - **V5 = voto_en_contra, salvo_su_voto o ausente, y plazo vigente → HOJA IMPUGNACIÓN**: `assets/template-demanda-impugnacion-acuerdos.md`.
  - **V5 = no_procede → DETENER** la elección de hoja: la respuesta es incoherente, porque el asunto es la impugnación de un acuerdo y la posición del cliente en la junta decide su legitimación. Aclarar en el chat (REG-VAL-01) como voto o si estuvo ausente, y volver a resolver V5. No crear documento hasta resolverlo.
  - **Plazo caducado → DETENER**: la acción caduca a los tres meses de adoptarse el acuerdo, o al año si es contrario a la ley o a los estatutos; para el ausente el cómputo arranca de la comunicación del acuerdo (artículo 18.3). Advertir de la caducidad, no dar falsas expectativas y ofrecer escalación. No crear documento.
  - **V6 = no (deudas pendientes)**: no detiene el flujo, pero es un obstáculo. Ver la validación de presupuestos.
- Si V1 = propietario y V2 = impago_cuotas o actividad_molesta, o la materia no es ninguna de las tres de V2 → **DETENER Y DERIVAR**: identificar la materia y derivar sin crear documento. Casos frecuentes: requerimiento de pago de un monitorio de la comunidad ya recibido (skill `reclamacion-cantidad`, escrito de oposición, plazo de veinte días); reclamación de cantidad frente a la comunidad por daños (skill `reclamacion-cantidad`); cuestiones arrendaticias del piso (skills `arrendamiento` o `desahucio`). Si no encaja en ninguna, ofrecer escalación.
- **Requisito de procedibilidad (Ley Orgánica 1/2025).** Si el intento previo de un medio adecuado de solución de controversias no está acreditado y está skill no genera por sí misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociación, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaración responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a trámite.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **HOJA CUOTAS:** comprobar que existe acuerdo de junta aprobando la liquidación y autorizando la reclamación; que quien va a firmar la certificación ejerce las funciones de secretario; y si el visto bueno del presidente es necesario o concurre la excepción del artículo 21.3 (secretario-administrador con cualificación profesional legalmente reconocida que no vaya a intervenir profesionalmente en la reclamación). Comprobar que la deuda puede desglosarse por concepto y periodo. Si el deudor no ha designado domicilio, anotar la regla del artículo 815.2 de la LEC (notificación en el propio piso o local) para explicarla en la sección correspondiente de la Fase 4.
- **HOJA CUOTAS-SIN-ACUERDO:** además de lo anterior, advertir de que la junta debe incluir el punto en el orden del día y de que la certificación no puede emitirse antes.
- **HOJA IMPUGNACIÓN:** verificar la legitimación (artículo 18.2), el plazo de caducidad (artículo 18.3, computado desde el acuerdo o desde su comunicación al ausente) y el requisito de estar al corriente de pago, con la excepción legal de los acuerdos sobre establecimiento o alteración de las cuotas de participación del artículo 9. Si el cliente estuvo ausente, comprobar si comunico su discrepancia dentro de los treinta días naturales del artículo 17.8 y advertir de las consecuencias si no lo hizo. Abogado y procurador son preceptivos.
- **HOJA CESACIÓN:** verificar que quien requiere es el presidente (o que actúa por su cuenta a iniciativa de un propietario u ocupante) y que la conducta encaja en alguno de los tres supuestos del artículo 7.2, o en el artículo 7.3 si se trata de alquiler de uso turístico sin aprobación de la comunidad. Comprobar si el infractor es propietario u ocupante.
- **MASC:** en la HOJA IMPUGNACIÓN es exigible el intento previo de solución (artículos 264.4º y 403.2 de la LEC). En la HOJA CUOTAS la cuestión es discutida: posición conservadora, aprovechar la notificación de la deuda y advertir. Ver `references/masc-y-requisitos-previos-lph.md`.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Ley 49/1960, de 21 de julio, sobre Propiedad Horizontal (LPH): Art. 7.2 (actividades prohibidas y acción de cesación), Art. 9.1.e (obligación contributiva y afección real), Art. 18 (impugnación de acuerdos, plazos de 3 meses o 1 año y requisito de estar al corriente de pago), y Art. 21 (proceso monitorio especial de reclamación de cuotas).
2. **Orientación Legal del Caso:**

**Informa el cauce y la fuente aplicable.** Indica qué documento corresponde a su caso y por qué, citando la norma con nombre completo y artículo, con el enlace del BOE consultado. Textos fijos por hoja:
   - CUOTAS: "A su caso corresponde el proceso monitorio especial de comunidades de propietarios, regulado en el artículo 21 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal, en relación con el artículo 812.2.2º de la Ley 1/2000, de Enjuiciamiento Civil. Prepararemos primero la certificación del acuerdo de liquidación de la deuda, que es el documento que la ley exige acompañar, y después la petición inicial. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"
   - CUOTAS-SIN-ACUERDO: añadir al texto anterior "Tenga en cuenta que la reclamación requiere un acuerdo previo de la junta que apruebe la liquidación de la deuda y autorice su reclamación judicial, conforme a los artículos 21.1 y 21.2 de la misma ley. Prepararemos ahora la certificación para que pueda emitirse en cuanto la junta lo adopte; la petición inicial no debe presentarse antes."
   - IMPUGNACIÓN: "A su caso corresponde la impugnación de acuerdos de la junta, regulada en el artículo 18 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal, que se sustancia por los trámites del juicio ordinario conforme al artículo 249.1.8º de la Ley 1/2000, de Enjuiciamiento Civil, cualquiera que sea la cuantía. La acción caduca a los tres meses desde la adopción del acuerdo, o al año si el acuerdo es contrario a la ley o a los estatutos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"
   - CESACIÓN: "A su caso corresponde el requerimiento previo de cesación del artículo 7.2 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal, que el presidente debe dirigir al infractor antes de que la comunidad pueda ejercitar la acción de cesación. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"
   - En IMPUGNACIÓN, añadir siempre: "Antes de presentar la demanda deberá acreditarse el intento de solución extrajudicial exigido por la Ley Orgánica 1/2025 (artículos 264 y 403.2 de la Ley de Enjuiciamiento Civil). La solicitud de negociación suspende el plazo de caducidad, pero no conviene apurarlo."

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** (menciónala por su denominación formal, sin mostrar rutas internas ni volcar su contenido). Si el enrutamiento asigno varios documentos, nómbralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la sección de assets.
4. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` y la sección 6.1 de `CLAUDE.md`:
1. **Escritura del Documento (`create_file`):** Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`, aplicando el principio Zero-Omission y el volcado inmediato total de partes (`REG-CLI-04`) en título H1, comparecencia y firmas.
2. **Validación de Integridad:** Comprobación prioritaria mediante `# WORKSPACE ACTIVE DOCUMENTS`.
3. **Confirmación en Chat y Encadenamiento Inmediato:** Informa en el chat de la ruta absoluta del documento creado y los datos de partes incorporados, e introduce en esa misma respuesta la primera sección de la Fase 4 sin detener el flujo.
---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial las secciones del documento respetando rigurosamente las directivas operativas globales de `CLAUDE.md`:
- **Partes e Intervinientes (REG-CLI-01 a 04):** Búsqueda prioritaria con `search_clients`, desambiguación con opción obligatoria `ninguna`, consentimiento de guardado con `save_client` (REG-CLI-03) y volcado directo e inmediato al editor (`edit_file` / `create_file`) sin confirmación en chat (REG-CLI-04).
- **Datos Estructurados Objetivos:** Solicitud en bloque mediante `slot_filling_request`.
- **Equivalencia Chat / Formulario (REG-DAT-01):** Ingestión directa de información aportada por chat sin re-emitir formularios innecesarios; reenvío oportuno si el usuario canceló sin responder.
- **Cláusulas Sustantivas / Negociables:** Negociación en chat -> Vista previa en texto plano -> Pregunta literal de confirmación (`¿Confirmamos esta cláusula?` / `¿Confirmamos esta sección?`) -> Persistencia con `edit_file`.

### Hoja de Ruta de Secciones y Cláusulas Condicionales

**Anuncio de sección y encadenamiento:** al terminar una sección y confirmar su edición en disco, emite en ese mismo turno el anuncio fijo de la sección que se abre y lanza de inmediato su formulario `slot_filling_request` (si es grupo de datos) o su planteamiento en chat (si es negociación). No pidas permiso para pasar de sección: informa y continúa. Los anuncios nombran la sección SUSTANTIVA del documento, nunca la mecánica interna. La vista previa y la confirmación siempre van en el chat. Las secciones marcadas como de negociación se explican y se confirman una a una en el chat.

### Secciones — HOJA CUOTAS y HOJA CUOTAS-SIN-ACUERDO

1. **Datos de la comunidad** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nueva, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de la comunidad de propietarios." Invoca `search_clients` prioritariamente. Si es nueva, solicita en bloque vía `slot_filling_request`: a) denominación; b) NIF; c) dirección completa de la finca; d) nombre y NIF de quien ejerce las funciones de secretario o secretario-administrador, y su cargo exacto; e) nombre del presidente. Antes de cerrar el bloque, si el secretario es un administrador profesional, pregunta si va a intervenir profesionalmente en la reclamación, porque de ello depende que sea o no necesario el visto bueno del presidente (artículo 21.3). Si es nueva cliente/entidad, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Conforme a `REG-CLI-04`, vuelca de inmediato al documento con `edit_file` (o ya volcado en `create_file`) sin requerir confirmación en chat, sustituyendo exhaustivamente los nombres en todas sus apariciones a lo largo del documento (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones).
2. **Datos del propietario deudor** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación del propietario deudor." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre o razón social; b) NIF o CIF si se conoce; c) elemento privativo (piso, letra, planta, plaza o local); d) cuota de participación; e) domicilio designado por el deudor para las notificaciones de la comunidad. Si no ha designado ninguno, explicar que el requerimiento judicial se practicará en el propio piso o local (artículo 815.2 de la LEC) y hacerlo constar. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca directamente al documento con `edit_file` sin confirmación en chat per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones (título H1, comparecencia y firmas).
3. **Acuerdo de la junta y notificación de la deuda** *(dato objetivo con validación — recogida con `slot_filling_request`, confirmación en chat)*. Anuncio fijo: "Abordamos ahora el acuerdo de la junta y su notificación al deudor." Solicita en bloque vía `slot_filling_request`: a) fecha y tipo de la junta y punto del orden del día; b) persona facultada por la junta para reclamar; c) fecha y medio de notificación del acuerdo al deudor; d) solo si la notificación personal fracaso: fechas de inicio y fin de la publicación en el tablón de anuncios, verificando que cubre al menos tres días. En la HOJA CUOTAS-SIN-ACUERDO, los datos a) y b) quedan como placeholders y se advierte de ello sin preguntarlos. Vista previa y confirmación en chat.
4. **Desglose de la deuda** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos a determinar la deuda y su desglose." Antes de pedir cifras, explica que pueden reclamarse todas las cantidades debidas por gastos comunes, ordinarios o extraordinarios, generales o individualizables, y las aportaciones al fondo de reserva (artículo 21.2), así como las cuotas aprobadas que se devenguen hasta la notificación de la deuda (artículo 21.3); y explica que la ley exige el desglose y no admite un importe global. Recoge después, concepto a concepto, periodo, fecha de exigibilidad e importe, y calcula el total. Verifica que la suma cuadra antes de escribirla.
5. **Intereses y gastos de la reclamación** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Concretamos ahora los intereses y los gastos de la reclamación." Explica antes de pedir la decisión: los créditos de la comunidad devengan intereses desde el momento en que debió hacerse cada pago (artículo 21.1), sin necesidad de requerimiento; la junta puede haber acordado medidas disuasorias, que no pueden ser abusivas ni desproporcionadas ni retroactivas; y pueden repercutirse al deudor los gastos y costes de la reclamación, incluidos los del secretario administrador (artículo 21.3). Confirmación una a una (intereses primero, gastos después).
6. **Contra quién se dirige la reclamación** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos contra quién se dirige la reclamación." Explica antes de decidir: cabe demandar al titular registral a efectos de soportar la ejecución sobre el inmueble (artículo 21.2); si el piso cambio de manos, el adquirente responde con el propio inmueble de lo debido en la anualidad en curso y los tres años naturales anteriores, por la afección real del artículo 9.1.e); y el propietario anterior que no comunico la transmisión responde solidariamente de las deudas posteriores (artículo 9.1.i). Pregunta después si el piso ha cambiado de titularidad y si desea dirigir la reclamación también contra alguno de ellos.
7. **Juzgado competente** *(decisión con explicación)*. Anuncio fijo: "Determinamos ahora el juzgado competente." Explica que la comunidad puede elegir entre el juzgado del domicilio o residencia del deudor y el del lugar donde se halla la finca (artículo 813 de la LEC), que no cabe sumisión a otro fuero, y pide la elección. Si el usuario propone un fuero distinto, advertir y corregir.
8. **Postulación y embargo preventivo** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Cerramos con la intervención profesional y las medidas frente a una eventual oposición." Explica: no son preceptivos abogado ni procurador para la petición inicial, pero si se utilizan sus honorarios y derechos son repercutibles al deudor con los límites del artículo 394.3 de la LEC (artículo 21.5); y que, si el deudor se opone, cabe pedir el embargo preventivo de sus bienes, que el tribunal acordara en todo caso y sin caución (artículo 21.4). Pregunta si intervienen procurador y letrado y si desea anunciar el embargo preventivo. Confirmación una a una.
9. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del documento." Lugar de firma; la fecha por defecto es la del día, salvo indicación en contrario.

Las secciones 1 a 6 rellenan la certificación (comunidad, deudor, acuerdo y notificación, desglose, intereses y gastos, contra quién se dirige la reclamación). Las secciones 7 (juzgado competente) y 8 (postulación y embargo preventivo) no tienen campo alguno en la certificación: se preguntan por primera vez al construir la petición inicial, inmediatamente después de cerrar la certificación. La sección 9 (lugar y fecha) se responde dos veces con sentido distinto: la fecha de la certificación al cerrar esta, y la fecha de la petición al construirla, que puede no coincidir; el lugar, si no cambia, no se vuelve a preguntar. Al terminar la certificación, encadenar con la creación de la petición inicial (solo en la HOJA CUOTAS) sin repetir ninguna pregunta ya respondida: los datos de las secciones 1 a 6 se vuelcan directamente.

### Secciones — HOJA IMPUGNACIÓN

1. **Datos del propietario demandante** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por su identificación como parte demandante." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre completo o razón social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) elemento privativo y cuota de participación; e) nombre del procurador y del letrado, preceptivos en el juicio ordinario. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` (o ya volcado en `create_file`) sin confirmación en chat per `REG-CLI-04`.
2. **Datos de la comunidad demandada** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nueva, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de la comunidad demandada." Invoca `search_clients` prioritariamente. Si es nueva, solicita en bloque vía `slot_filling_request`: a) denominación; b) NIF si se conoce; c) dirección de la finca; d) nombre del presidente, que es quien la representa en juicio. Si es nueva entidad cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` sin confirmación en chat per `REG-CLI-04`.
3. **La junta y el acuerdo impugnado** *(dato objetivo con validación — recogida con `slot_filling_request`, confirmación en chat)*. Anuncio fijo: "Abordamos ahora la junta y el acuerdo que se impugna." Solicita en bloque vía `slot_filling_request`: a) fecha y tipo de junta; b) fecha y medio de la convocatoria; c) punto del orden del día; d) texto literal del acuerdo tal como consta en el acta; e) resultado de la votación (votos a favor, en contra, abstenciones y cuotas que representan). Valida el sentido de las respuestas: si el resultado de la votación no cuadra con el acuerdo descrito, dialoga y pide aclaración antes de escribirlo. Vista previa y confirmación en chat.
4. **Legitimación y plazo** *(dato objetivo con validación y advertencia)*. Anuncio fijo: "Verificamos ahora su legitimación y el plazo para impugnar." La posición en la votación ya está resuelta y NO se vuelve a preguntar. Sub-apartados que si se piden: a) si consta en el acta la constancia de su voto en contra, o la fecha en que se le comunico el acuerdo si estuvo ausente; b) solo si estuvo ausente: si comunico su discrepancia al secretario dentro de los treinta días naturales siguientes, explicando antes que, de no hacerlo, su voto se computa como favorable (artículo 17.8) y ello debilita la impugnación. Calcula el plazo y adviértelo expresamente: tres meses desde el acuerdo, o un año si es contrario a la ley o a los estatutos.
5. **Situación de pago** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Tratamos ahora el requisito de estar al corriente de pago." Explica: para impugnar hay que estar al corriente de todas las deudas vencidas o consignarlas judicialmente antes de demandar (artículo 18.2), con la única excepción de los acuerdos sobre establecimiento o alteración de las cuotas de participación del artículo 9. Si el cliente tiene deudas pendientes, explica las dos salidas (pagar o consignar) y sus consecuencias antes de continuar; no redactes la demanda dando por resuelto el requisito.
6. **Motivos de la impugnación** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos a los motivos de la impugnación." Explica los tres supuestos del artículo 18.1 (acuerdo contrario a la ley o a los estatutos; gravemente lesivo para la comunidad en beneficio de uno o varios propietarios; grave perjuicio para un propietario sin obligación de soportarlo o adoptado con abuso de derecho) y, si el motivo es de mayorías, contrasta el acuerdo con el cuadro del artículo 17 recogido en `references/lph-reclamacion-y-acuerdos.md`. Elige con el cliente el supuesto y recoge después los motivos concretos en prosa y los documentos que los acreditan. Confirmación una a una.
7. **Suspensión cautelar del acuerdo** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Valoramos ahora si conviene pedir la suspensión del acuerdo." Explica: la impugnación NO suspende la ejecución del acuerdo; la suspensión debe pedirse como medida cautelar, se acuerda oída la comunidad, exige justificar apariencia de buen derecho y peligro por la mora procesal, y normalmente conlleva prestar caución (artículo 18.4 y artículos 721 y siguientes de la LEC). Pregunta después si desea solicitarla y con que justificación.
8. **Petición adicional del suplico** *(cláusula de negociación)*. Anuncio fijo: "Concretamos qué más debe pedirse en la demanda además de la nulidad del acuerdo." Ejemplos que puedes ofrecer: devolución de derramas ya cobradas, reposición a la situación anterior, condena a adoptar un nuevo acuerdo con la mayoría correcta. Si no hay ninguna, retirar el punto del suplico en lugar de dejarlo vacío.
9. **Intento de solución previa** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Cerramos con el intento de solución previa exigido antes de demandar." Explica que debe acreditarse el intento de negociación (artículos 264.4º y 403.2 de la LEC) y que la solicitud de negociación, si define bien su objeto, suspende el plazo de caducidad (artículo 7.1 de la Ley Orgánica 1/2025), pero que el cómputo se reanuda si no hay respuesta en treinta días naturales. Recoge el tipo de intento y su fecha; si aún no se ha hecho, déjalo como placeholder y advierte de que la demanda no debe presentarse sin ese documento.
10. **Juzgado, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el juzgado, el lugar y la fecha del escrito." Partido judicial en el que radica la finca; lugar de firma; fecha del día salvo indicación en contrario.

### Secciones — HOJA CESACIÓN

1. **Datos de la comunidad y del presidente** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nueva, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de la comunidad y de quien firma el requerimiento." Invoca `search_clients` prioritariamente. Si es nueva, solicita en bloque vía `slot_filling_request`: a) denominación de la comunidad; b) NIF; c) dirección de la finca; d) nombre y NIF del presidente. Si es nueva entidad cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` (o en `create_file`) sin confirmación en chat per `REG-CLI-04`.
2. **Datos del infractor** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de quien desarrolla la actividad." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre o razón social; b) NIF o CIF si se conoce; c) si es propietario u ocupante del elemento privativo; d) elemento privativo; e) domicilio a efectos de notificaciones. Si es ocupante y no propietario, advierte de que conviene remitir copia al propietario, porque la eventual demanda debe dirigirse contra ambos (artículo 7.2). Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca directamente a disco con `edit_file` sin confirmación en chat per `REG-CLI-04`.
3. **Descripción de la actividad** *(dato objetivo con validación de sentido)*. Anuncio fijo: "Abordamos ahora la descripción de la actividad." Pide los hechos con concreción: en que consiste, desde cuando, con que frecuencia, en que horario y a quién afecta. No aceptes calificativos como única respuesta ("es un escándalo", "son unos incívicos"): si la respuesta no aporta hechos verificables, explica por qué no sirve y pide datos concretos antes de escribirla.
4. **Acreditación** *(dato objetivo)*. Anuncio fijo: "Pasamos a los medios con los que se acredita." Recoge que pruebas existen: denuncias presentadas, actas de la policía local, mediciones sonométricas, informes técnicos, actas de junta, comunicaciones previas, testimonios de vecinos.
5. **Fundamento de la prohibición** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora en que se apoya la prohibición." Explica las tres vías del artículo 7.2 (actividad prohibida en los estatutos; actividad dañosa para la finca; actividad que contraviene las disposiciones generales sobre actividades molestas, insalubres, nocivas, peligrosas o ilícitas) y, si se trata de alquiler de uso turístico, el régimen del artículo 7.3 y la mayoría de tres quintos del artículo 17.12. Elige con el cliente la vía y recoge su justificación. Si invoca los estatutos, pide la cláusula concreta.
6. **Plazo de cesación y medidas solicitadas** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Concretamos el plazo y las medidas que se le exigen." Explica que la ley habla de cesación inmediata, y que fijar además un plazo breve y razonable (práctica habitual: entre diez y quince días) refuerza la posición de la comunidad sin debilitar la exigencia. Recoge el plazo y las medidas concretas que se piden.
7. **Ofrecimiento de solución negociada** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Incluimos un ofrecimiento de solución negociada." Explica que incorporar un ofrecimiento expreso de diálogo y un canal de contacto permite que el mismo documento sirva como intento de solución previa si la comunidad tiene que demandar después. Recoge la vía de contacto.
8. **Consecuencias que se advierten** *(informativo, sin pregunta)*. Anuncio fijo: "Le informo de las consecuencias que se advertirán en el requerimiento." Expón lo que la sentencia estimatoria puede acordar: cesación definitiva, indemnización de daños y perjuicios, privación del derecho al uso de la vivienda o local por tiempo no superior a tres años y, si el infractor no es el propietario, extinción de sus derechos y lanzamiento inmediato. Recuerda además que el paso siguiente exige autorización de la junta debidamente convocada al efecto. No requiere dato del usuario; encadenar con la sección siguiente.
9. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del requerimiento."

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo, hechos numerados con una idea por apartado, documentos relacionados y numerados, desglose en tabla en lugar de prosa, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre la LPH y la LEC en el BOE antes de redactar (Fase 2). Sin verificación, no proceder.
2. Si se detecta una versión del texto consolidado posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario. No usar una versión desactualizada.
3. La reclamación de cuotas exige acuerdo previo de la junta que apruebe la liquidación y autorice la reclamación (artículos 21.1 y 21.2). Sin ese acuerdo no se genera la petición inicial, por mucho que el usuario insista.
4. La certificación debe expresar el importe adeudado Y SU DESGLOSE (artículo 21.3). Nunca emitir una certificación con un importe global.
5. El visto bueno del presidente solo puede omitirse en el supuesto tasado del artículo 21.3 (secretario-administrador con cualificación profesional legalmente reconocida que no vaya a intervenir profesionalmente en la reclamación). No admitir otras excepciones.
6. La legitimación para impugnar es tasada (artículo 18.2): quien voto a favor o se abstuvo sin salvar su voto no puede impugnar. No redactar la demanda en ese caso.
7. El requisito de estar al corriente de pago del artículo 18.2 solo decae para los acuerdos sobre establecimiento o alteración de las cuotas de participación del artículo 9. No extender la excepción a otros acuerdos.
8. Los plazos del artículo 18.3 son de CADUCIDAD y no se interrumpen por reclamación extrajudicial. Calcularlos siempre y advertir de su vencimiento; nunca dar por buena una impugnación fuera de plazo.
9. Nunca afirmar que la impugnación suspende el acuerdo: la suspensión es cautelar, se pide, se justifica y suele exigir caución (artículo 18.4).
10. El requerimiento del presidente es presupuesto de la acción de cesación y debe ser fehaciente (artículo 7.2). Nunca presentar el requerimiento como si fuera ya la demanda, ni prometer la privación del uso como resultado seguro.
11. Nunca inventar datos, importes, cuotas de participación, fechas de junta, contenido de estatutos ni jurisprudencia. Los campos no proporcionados quedan como `{{DATO}}`.
12. Si el usuario invoca estatutos o título constitutivo con reglas distintas de las legales, no suponer su contenido: pedirlos o escalar.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No es una herramienta de administración de fincas: no elabora presupuestos, contabilidad, cuentas anuales, cuotas ni derramas.
- No convoca juntas, no redacta órdenes del día ni levanta actas.
- No resuelve conflictos vecinales que carezcan de base en la Ley de Propiedad Horizontal (ruidos entre viviendas sin infracción, discusiones personales, animales de compañía sin prohibición estatutaria ni infracción administrativa): advertir y, en su caso, derivar.
- No redacta la demanda de la acción de cesación del artículo 7.2 ni la demanda de juicio ordinario posterior a la oposición en el monitorio: derivar a `juicio-ordinario` y escalar.
- No redacta la oposición del propietario al monitorio de la comunidad: derivar a `reclamacion-cantidad` (plazo de veinte días, que debe advertirse de inmediato).
- No se usa para reclamar cantidades que no sean gastos comunes ni fondo de reserva (por ejemplo, daños causados por un propietario a otro): derivar a `reclamacion-cantidad`.
- No emite dictámenes sobre la validez de estatutos, la interpretación del título constitutivo ni la naturaleza de un elemento común o privativo: escalar.
- No sustituye la lectura de los estatutos ni del título constitutivo, que pueden alterar el régimen legal supletorio.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
