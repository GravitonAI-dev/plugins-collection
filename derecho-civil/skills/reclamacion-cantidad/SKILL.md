---
name: reclamacion-cantidad
title: Reclamación de cantidad
i18n:
  en:
    name: debt-claim
    title: Debt claim
    description: >
      Generates the right document to claim (or defend against a claim for) a sum of money,
      choosing the correct procedural route under the **Civil Procedure Act (Law 1/2000, LEC)**,
      which sets the procedure according to the amount and type of debt, verified in the BOE:
      initial petition for order-for-payment proceedings (documented, liquid, due and payable
      debt, any amount), summary proceedings claim (up to 15,000 euros or rent), ordinary
      proceedings claim (over 15,000 euros, including the claim following opposition to an order
      for payment, Art. 818.2 LEC), opposition to the order for payment (debtor's position) and
      prior demand letter by burofax (MASC, Organic Law 1/2025). Do not use for non-monetary
      claims, matters under Art. 249.1 LEC whose main claim is not payment, claims against
      public administrations, evictions or enforcement.
description: >
  Genera el documento adecuado para reclamar (o defenderse de la reclamación de) una cantidad de dinero,
  eligiendo la vía procesal correcta conforme a la **Ley 1/2000 de Enjuiciamiento Civil (LEC)**, que fija qué procedimiento corresponde según la cuantía y el tipo de deuda, verificada en el BOE: petición inicial de proceso
  monitorio (deuda documentada, líquida, vencida y exigible, cualquier cuantía), demanda de juicio verbal
  (hasta 15.000 euros o rentas de arrendamiento), demanda de juicio ordinario (más de 15.000 euros, incluida
  la posterior a la oposición de un monitorio, Art. 818.2 LEC), escrito de oposición al monitorio (posición
  de deudor) y burofax de requerimiento previo (MASC, LO 1/2025). NO usar para pretensiones no dinerarias,
  materias del Art. 249.1 LEC cuya pretensión principal no sea el pago, reclamaciones frente a
  Administraciones Públicas, desahucios ni ejecuciones.
when_to_use: |
  - El usuario quiere reclamar judicialmente una cantidad de dinero y no sabe (o no indica) por qué vía.
  - El usuario quiere iniciar la reclamación de una deuda con o sin documentos que la acrediten.
  - El usuario ha iniciado un monitorio, el deudor se ha opuesto y la cuantía obliga a demandar en ordinario.
  - El cliente ha recibido un requerimiento de pago de un proceso monitorio y quiere oponerse.
  - El usuario necesita el burofax de requerimiento previo (intento de MASC) antes de reclamar.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - rol: el cliente reclama una cantidad (acreedor) / ha recibido un requerimiento de monitorio (deudor)
  - estado_reclamacion: sin reclamación judicial iniciada / monitorio propio con oposición del deudor
  - deuda_documentada: existen documentos que acreditan la deuda (sí / no)
  - deuda_vencida_liquida: la cantidad está vencida y su importe es fijo o calculable (sí / no; si no, subclasificar en discutida o no vencida)
  - cuantia: importe reclamado en euros (determina verbal u ordinario en el declarativo)
  - es_arrendamiento: la cantidad deriva de rentas o cantidades debidas por arrendamiento de inmueble (sí / no)
  - masc_intentado: se ha intentado un medio adecuado de solución de controversias (sí / no)
  - datos_parte_reclamante: nombre o razón social, NIF/CIF, domicilio, representante si persona jurídica
  - datos_parte_contraria: nombre o razón social, NIF/CIF, domicilio o lugar donde pueda ser hallado
  - origen_deuda: descripción del origen y relación de documentos acreditativos
  - intereses: legales o pactados, y fecha desde la que se devengan
  - deudor_consumidor: la deuda se funda en un contrato entre empresario y consumidor (sí / no)
  - partido_judicial: para la competencia territorial
  - datos_monitorio_previo: juzgado, número de autos y cuantía (solo oposición o demanda del Art. 818.2)
  - motivos_oposicion: alcance (total / parcial) y razones fundadas (solo oposición)
outputs:
  - peticion_monitorio: petición inicial de proceso monitorio en markdown, DRAFT
  - demanda_juicio_verbal: demanda de juicio verbal de reclamación de cantidad en markdown, DRAFT
  - demanda_juicio_ordinario: demanda de juicio ordinario de reclamación de cantidad en markdown, DRAFT
  - oposicion_monitorio: escrito de oposición a proceso monitorio en markdown, DRAFT
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

# Reclamación de Cantidad

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
      "id": "rol",
      "rationale": "Resolver V1: quién ha recibido un requerimiento de monitorio no reclama, se opone, y usa un asset distinto.",
      "question": "¿En qué posición se encuentra el cliente?",
      "options": [
        {"id": "acreedor", "label": "Es acreedor y reclama una cantidad"},
        {"id": "deudor_requerido", "label": "Ha recibido un requerimiento de pago de un proceso monitorio"}
      ]
    },
    {
      "id": "estado_reclamacion",
      "rationale": "Resolver V2: si ya hay monitorio con oposición del deudor, el asunto continúa por el cauce del artículo 818 de la LEC.",
      "question": "Si es acreedor, ¿en qué estado está la reclamación?",
      "show_if": {"question_id": "rol", "option_ids": ["acreedor"]},
      "options": [
        {"id": "sin_iniciar", "label": "Sin reclamación judicial iniciada"},
        {"id": "monitorio_con_oposicion", "label": "Ya se presentó monitorio y el deudor se ha opuesto"},
        {"id": "no_procede", "label": "No procede: el cliente es el deudor requerido"}
      ]
    },
    {
      "id": "deuda_documentada",
      "rationale": "Resolver V3: la existencia de documento acreditativo es presupuesto del proceso monitorio conforme al artículo 812 de la LEC.",
      "question": "¿Existen documentos que acrediten la deuda: facturas, contrato, albaranes, reconocimiento?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    },
    {
      "id": "deuda_vencida_liquida",
      "rationale": "Resolver V4: el monitorio exige deuda dineraria, líquida, determinada, vencida y exigible; si el importe se discute, procede la vía declarativa.",
      "question": "¿Está la deuda vencida y su importe es fijo o calculable sin discusión?",
      "options": [
        {"id": "vencida_y_liquida", "label": "Sí, está vencida y el importe es cierto"},
        {"id": "discutida", "label": "No, el importe está discutido por la otra parte"},
        {"id": "por_determinar", "label": "No, el importe todavía debe determinarse"},
        {"id": "pendiente_de_vencer", "label": "Todavía no ha vencido"}
      ]
    },
    {
      "id": "es_arrendamiento",
      "rationale": "Resolver V5: las rentas de arrendamiento admiten la acumulación de la reclamación al desahucio y tienen especialidades procesales.",
      "question": "¿Deriva la cantidad de rentas o cantidades debidas por arrendamiento de inmueble?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    },
    {
      "id": "masc_intentado",
      "rationale": "Resolver V6: el intento previo de un medio adecuado de solución de controversias es requisito de procedibilidad de la demanda declarativa (artículos 264 y 403.2 de la Ley de Enjuiciamiento Civil) y no se exige en la petición inicial de monitorio.",
      "question": "¿Se ha intentado previamente un medio adecuado de solución de controversias, o un requerimiento fehaciente de pago acreditable?",
      "options": [
        {"id": "si", "label": "Sí, y es acreditable"},
        {"id": "no", "label": "No"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `rol`
- `V2` — `estado_reclamacion`
- `V3` — `deuda_documentada`
- `V4` — `deuda_vencida_liquida`
- `V5` — `es_arrendamiento`
- `V6` — `masc_intentado`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si V1 = deudor requerido → **HOJA OPOSICIÓN**: `assets/template-oposicion-monitorio.md`. V3-V6 no aplican.
- Si V1 = acreedor y V2 = monitorio con oposición:
  - Cuantía > 15.000 euros → **HOJA ORDINARIO-818**: `assets/template-demanda-juicio-ordinario.md` (activar los bloques condicionales del Art. 818.2; V6 no aplica: la demanda trae causa del monitorio).
  - Cuantía <= 15.000 euros → **DETENER**: tras la oposición, el asunto continúa como juicio verbal dentro del mismo procedimiento (impugnación de la oposición en 10 días, Art. 818.1 LEC); no procede una nueva demanda. Informar del cauce y del plazo, y ofrecer escalación. No crear documento.
- Si V1 = acreedor, V2 = sin_iniciar, V3 = si y V4 = vencida_y_liquida → **HOJA MONITORIO**: `assets/template-peticion-monitorio.md` (cualquier cuantía). Si V6 = no → generar además ANTES `assets/template-burofax-masc-reclamacion.md`.
- Si V4 = pendiente_de_vencer → **DETENER**: la deuda no es exigible todavía y no cabe reclamarla judicialmente. Esta rama tiene prioridad sobre todas las siguientes. Advertir y no crear documento.
- **Vía declarativa — puertas de entrada.** Basta con que se cumpla una de las tres:
- Si V1 = acreedor, V2 = sin_iniciar y V3 = no, por no haber documento del Art. 812 → **RUTA DECLARATIVA**: `assets/template-demanda-juicio-verbal.md` o `assets/template-demanda-juicio-ordinario.md`, según el desglose de cuantía que sigue.
- Si V1 = acreedor, V2 = sin_iniciar y V4 = discutida → **RUTA DECLARATIVA**: las mismas dos hojas, según el desglose de cuantía que sigue.
- Si V1 = acreedor, V2 = sin_iniciar y V4 = por_determinar → **RUTA DECLARATIVA**: las mismas dos hojas, según el desglose de cuantía que sigue.
- **Desglose de la vía declarativa.** La hoja la fija el interés económico, que no es un vector sino un dato del asunto:
  - Si V5 = si (rentas y cantidades debidas del arrendamiento de un inmueble, cualquier cuantía, Art. 250.1.1º LEC) → **HOJA VERBAL**: `assets/template-demanda-juicio-verbal.md`.
  - Si V5 = no y la cuantía es <= 15.000 euros → **HOJA VERBAL**: `assets/template-demanda-juicio-verbal.md`.
  - Si V5 = no y la cuantía es > 15.000 euros, o el interés económico es imposible de calcular → **HOJA ORDINARIO**: `assets/template-demanda-juicio-ordinario.md`.
  - En las tres, si V6 = no → generar además ANTES `assets/template-burofax-masc-reclamacion.md` (requisito de procedibilidad, Arts. 264 y 403.2 LEC).
- Si la pretensión principal NO es el pago de una cantidad (materia del Art. 249.1 LEC, obligaciones de hacer, entrega de cosa) → **DETENER**: fuera de alcance; derivar a la skill correspondiente (`juicio-ordinario`) o a escalación.
- **Requisito de procedibilidad (Ley Orgánica 1/2025).** Si el intento previo de un medio adecuado de solución de controversias no está acreditado y esta skill no genera por sí misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociación, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaración responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a trámite.

### 1.4 Validación de procedibilidad (interno, antes de la Fase 3)

- **HOJA MONITORIO:** confirmar deuda dineraria, líquida, determinada, vencida y exigible con documento del Art. 812; competencia del Juzgado de Primera Instancia del domicilio del deudor (Art. 813, sin sumisión); si el deudor es ilocalizable, advertir de la limitación. Si la deuda se funda en contrato empresario-consumidor, anotar el control de oficio del Art. 815.4 para explicarlo en la sección correspondiente de la Fase 4.
- **HOJA VERBAL / ORDINARIO:** verificar que la cuantía se puede fijar (Arts. 251-253); en verbal <= 2.000 euros, informar de que no son preceptivos abogado ni procurador (Arts. 23.2.1º y 31.2.1º) y de que existe formulario normalizado del CGPJ; en ordinario, abogado y procurador preceptivos.
- **HOJA ORDINARIO-818:** verificar que está dentro del plazo de UN MES desde el traslado del escrito de oposición (Art. 818.2). Si el plazo está vencido o próximo a vencer, advertirlo de inmediato.
- **HOJA OPOSICIÓN:** verificar que está dentro del plazo de VEINTE DÍAS desde el requerimiento (Art. 815.1). Si el plazo está vencido, advertir del riesgo de despacho de ejecución (Art. 816) y ofrecer escalación. Si la cuantía reclamada excede de 2.000 euros, informar de que la oposición requiere abogado y procurador.
- **MASC:** en las hojas iniciadoras con V6 = no, integrar el burofax previo (posición conservadora, ver `references/masc-requisito-procedibilidad-lo1-2025.md`).

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Ley de Enjuiciamiento Civil (Arts. 249, 250, 437 y 812 a 818), Código Civil (Arts. 1.088, 1.091, 1.101, 1.108 y 1.124), y Ley Orgánica 1/2025 de medidas de eficiencia del servicio público de justicia.
2. **Orientación Legal del Caso:**

**Informa la vía y la fuente aplicable.** Indica al usuario que vía procesal corresponde a su caso y por qué, citando la norma con nombre completo y artículo, con el enlace del BOE consultado. Textos fijos por hoja (adaptar solo el dato de cuantía):
   - MONITORIO: "A su caso corresponde el proceso monitorio, regulado en los artículos 812 y siguientes de la Ley 1/2000, de Enjuiciamiento Civil, al tratarse de una deuda dineraria, líquida, vencida y exigible acreditada documentalmente, cualquiera que sea su cuantía. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - VERBAL: "A su caso corresponde el juicio verbal, conforme al artículo 250 de la Ley 1/2000, de Enjuiciamiento Civil, por no exceder la cuantía de 15.000 euros [o: por tratarse de rentas o cantidades debidas por arrendamiento de inmueble, artículo 250.1.1º]. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - ORDINARIO: "A su caso corresponde el juicio ordinario, conforme al artículo 249.2 de la Ley 1/2000, de Enjuiciamiento Civil, por exceder la cuantía de 15.000 euros. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - ORDINARIO-818: añadir además "Al haberse opuesto el deudor en el proceso monitorio, la demanda debe interponerse en el plazo de un mes desde el traslado del escrito de oposición, conforme al artículo 818 de la misma ley."
   - OPOSICIÓN: "Su escrito se rige por los artículos 815 y 818 de la Ley 1/2000, de Enjuiciamiento Civil: dispone de veinte días desde el requerimiento para formular una oposición fundada y motivada. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - Si la hoja incluye burofax previo (V6 = no), añadir: "Con carácter previo se preparara un burofax de requerimiento de pago, que acredita el intento de solución extrajudicial exigido por la Ley Orgánica 1/2025 (artículos 264 y 403.2 de la Ley de Enjuiciamiento Civil). Tenga en cuenta que la demanda no debe presentarse hasta disponer del justificante del envío del burofax y haber dejado un plazo razonable de respuesta."

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

**Anuncio de sección y encadenamiento:** al terminar una sección y confirmar su edición en disco, emite en ese mismo turno el anuncio fijo de la sección que se abre y lanza de inmediato su formulario `slot_filling_request` (si es grupo de datos) o su planteamiento en chat (si es negociación). No pidas permiso para pasar de sección: informa y continúa. Los anuncios nombran la sección SUSTANTIVA del documento, nunca la mecánica interna. La vista previa y la confirmación siempre van en el chat. Las cláusulas de negociación se explican y se confirman una a una en el chat.

**Propagación de un dato confirmado (regla global de Edit):** varios datos (nombre y NIF de cada parte, cuantía) aparecen repetidos literalmente en más de un punto del asset (encabezamiento/título, bloque de datos, cuerpo del EXPONE/HECHOS, SUPLICO y firma). Al asentar el dato, incorpóralo mediante `edit_file` en TODAS sus apariciones del documento, no solo en el bloque de datos donde se pregunto; verifica prioritariamente en `# WORKSPACE ACTIVE DOCUMENTS` (o mediante `read_file` en caso extremo) que no queden placeholders sueltos del mismo dato ya asentado.

### Secciones — HOJA MONITORIO / HOJA VERBAL / HOJA ORDINARIO / HOJA ORDINARIO-818

1. **Parte reclamante** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de la parte que reclama." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre completo o razón social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) solo si es persona jurídica: nombre, NIF y cargo del representante; e) solo en ORDINARIO y ORDINARIO-818 (y en VERBAL si la cuantía excede de 2.000 euros): nombre del procurador y del letrado. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` (o ya volcado en `create_file`) sin confirmación en chat per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones a lo largo del documento (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones).
2. **Parte deudora / demandada** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de la parte deudora." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre o razón social; b) NIF o CIF si se conoce; c) domicilio o lugar donde pueda ser hallada. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` sin confirmación en chat per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones (título H1, comparecencia y firmas).
3. **Origen de la deuda y prueba documental** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Abordamos ahora el origen de la deuda y su acreditación documental." Antes de registrar la relación de documentos, explica qué documentos sirven para acreditar la deuda (en monitorio, los del artículo 812 de la LEC: firmados por el deudor, o facturas, albaranes y certificaciones habituales del tráfico; en las demandas, los documentos fundamentales del artículo 265, con preclusion del 269) y confirma con el usuario cuáles aportará y en que orden se numeraran. El origen y la fecha de vencimiento ya aportados en el mensaje inicial (escucha activa) no se vuelven a preguntar en bruto: se dan por confirmados y solo se solicitan los datos concretos que falten (número e importe de cada documento, fecha exacta de cada vencimiento, fecha del contrato). Si hay más de un documento con vencimientos distintos, recoge la fecha de cada uno y numéralos correlativamente en `{{RELACION_DOCUMENTOS}}`; no fuerces una única fecha de vencimiento cuando existan varias. Si no se desprende ya del origen descrito si el deudor actúa como consumidor frente a un empresario, pregunta directamente: "¿El deudor contrato como consumidor particular o actuaba también como empresario o profesional?". Si la deuda se funda en un contrato entre empresario y consumidor, explica aquí el control de oficio de cláusulas abusivas (artículo 815.4 LEC en el monitorio) y sus consecuencias antes de continuar.
4. **Cuantía, intereses y costas** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos a la determinación de la cuantía, los intereses y las costas." El principal ya resuelto en la clasificación se reutiliza sin volver a preguntarlo. Explica la elección de intereses antes de pedir la decisión: interés legal del dinero desde la constitución en mora (artículos 1100 y 1108 del Código Civil, normalmente desde el requerimiento o el vencimiento) o interés pactado en el contrato si existe; y desde que fecha se devengan. Explica que las costas se solicitan conforme al artículo 394 de la LEC. En HOJA MONITORIO no incluyas una petición expresa de costas en el SUPLICO: la petición inicial no es todavía un procedimiento contencioso con sentencia; limítate a advertir de que, si el deudor se opone (paso a verbal u ordinario) o hay que instar la ejecución, las costas de esas fases posteriores se rigen por sus normas específicas. Confirmación una a una (intereses primero, costas después).
5. **Juzgado competente** *(dato objetivo con validación)*. Anuncio fijo: "Determinamos ahora el juzgado competente." En MONITORIO: partido judicial del domicilio o residencia del deudor (artículo 813 LEC, sin sumisión a otro fuero: si el usuario propone otro, advertir y corregir). En VERBAL y ORDINARIO: fuero general del domicilio del demandado (artículos 50 y 51 LEC) salvo fuero especial aplicable. En ORDINARIO-818: el mismo juzgado que conoció del monitorio.
6. **Solución previa (MASC)** *(solo si la hoja incluye burofax, cláusula de negociación)*. Anuncio fijo: "Concretamos por último los términos del requerimiento previo de pago." Sub-datos del burofax: plazo de pago que se concede (explicar que es práctica habitual conceder 10 días hábiles), medio de pago (cuenta IBAN u otro) y vía de contacto para negociar. Vista previa y confirmación en chat.
7. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Lugar de firma; la fecha por defecto es la del día, salvo indicación en contrario.

### Secciones — HOJA OPOSICIÓN

1. **Datos del procedimiento** *(dato objetivo — recogida en lote con `slot_filling_request`, confirmación en chat)*. Anuncio fijo: "Comenzamos por los datos del procedimiento que consta en el requerimiento recibido." Solicita en bloque vía `slot_filling_request`: a) juzgado (número y partido judicial); b) número de autos del monitorio; c) nombre del acreedor que reclama; d) cantidad reclamada; e) fecha en que recibió el requerimiento (para validar el plazo de veinte días: si está vencido, advertir y ofrecer escalación antes de continuar). Vista previa y confirmación en chat.
2. **Datos del cliente (deudor)** *(dato objetivo — búsqueda prioritaria con `search_clients`, recogida en lote con `slot_filling_request` si es nuevo, volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a su identificación como parte." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre completo o razón social; b) NIF o CIF; c) domicilio; d) solo si la cuantía reclamada excede de 2.000 euros: nombre del procurador y del letrado (preceptivos; si no los tiene, advertir de que debe designarlos). Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca directamente a disco con `edit_file` (o ya volcado en `create_file`) sin confirmación en chat per `REG-CLI-04`.
3. **Alcance y motivos de la oposición** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Abordamos ahora el contenido de la oposición." Explica antes de pedir la decisión: la oposición debe ser fundada y motivada (artículo 815.1 LEC), una negativa genérica puede ser rechazada; puede ser total o parcial (pluspetición: reconocer una parte y discutir el exceso); si la deuda deriva de un contrato con un empresario siendo el cliente consumidor, pueden alegarse cláusulas abusivas. Pide el alcance (total o parcial, y en su caso la cantidad reconocida), después los motivos concretos (prosa) y los documentos de apoyo. Confirmación una a una (alcance, motivos, documentos).
4. **Efectos y vía posterior** *(informativo, sin pregunta)*. Anuncio fijo: "Le informo de los efectos de la oposición." Informar: hasta 15.000 euros el asunto sigue como juicio verbal (el acreedor podrá impugnar la oposición en diez días); por encima, el acreedor deberá demandar en juicio ordinario en un mes (artículo 818 LEC). No requiere dato del usuario; encadenar con la sección siguiente.
5. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Igual que en las demás hojas.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo, HECHOS o ALEGACIONES numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre la LEC en el BOE antes de redactar (Fase 2). Sin verificación, no proceder.
2. Si se detecta una versión de la LEC o un modelo del CGPJ posterior al registrado en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario. No usar una versión desactualizada.
3. El monitorio solo procede con deuda dineraria, líquida, determinada, vencida y exigible acreditada con documento (Art. 812). Si falla cualquier requisito, enrutar al declarativo o detener; nunca forzar la vía.
4. El umbral entre verbal y ordinario es 15.000 euros (Arts. 249.2 y 250.2); las rentas de arrendamiento van a verbal cualquiera que sea la cuantía (Art. 250.1.1º). No admitir elecciones de vía contrarias a estos artículos aunque el usuario las pida.
5. Competencia del monitorio: exclusiva del Juzgado de Primera Instancia del domicilio del deudor (Art. 813). No admitir sumisión a otro fuero.
6. Posición conservadora sobre el MASC: en todo escrito iniciador sin intento previo acreditado, recomendar e integrar el burofax y advertir de la cuestión (LO 1/2025).
7. Plazos críticos: 20 días para oponerse (Art. 815.1) y 1 mes para la demanda de ordinario tras la oposición (Art. 818.2). Validarlos antes de redactar; si están vencidos, advertir y no dar falsas expectativas.
8. Nunca inventar datos, cuantías, fechas ni jurisprudencia. Los campos no proporcionados quedan como `{{DATO}}`.
9. Nunca afirmar que la deuda es exigible o incontrovertida sin base documental; nunca garantizar el resultado del procedimiento.
10. Si el deudor es consumidor y la deuda nace de un contrato con un empresario, informar siempre del control de oficio de cláusulas abusivas (Art. 815.4 LEC) antes de cerrar la cuantía.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para pretensiones no dinerarias (entrega de cosa, obligaciones de hacer o no hacer) ni declarativas puras.
- No usar para materias del Art. 249.1 LEC cuya pretensión principal no sea la condena al pago: derivar a la skill `juicio-ordinario`.
- No usar para reclamar a una Administración Pública.
- No usar para desahucios por falta de pago (skill `desahucio`) ni para la ejecución de títulos.
- No usar para redactar la impugnación de la oposición en el verbal transformado (Art. 818.1) ni la contestación a una demanda: advertir y escalar.
- No usar si el usuario pide opinión jurídica sobre la estrategia de un litigio: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
