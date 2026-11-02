---
name: desahucio
title: Desahucio
i18n:
  en:
    name: eviction
    title: Eviction
    description: >
      Generates the right document to recover possession of urban property, choosing the correct
      route under the **Civil Procedure Act (Law 1/2000, LEC)**, which governs the summary
      eviction procedure and its admission requirements, verified in the BOE: eviction claim for
      non-payment of rent (optionally joined with the claim for rent due, Art. 437.4.3 LEC),
      eviction claim on expiry of the contractual or legal term (Art. 250.1.1 LEC), eviction
      claim for occupation without title after consent (precario, Art. 250.1.2 LEC) and
      out-of-court agreement waiving rent in exchange for handing over the keys (Art. 1809 CC,
      approvable under Art. 19 LEC). It applies termination for non-payment under Art. 27 LAU,
      the admissibility requirements of Arts. 439.3 and 439.6 LEC (Law 12/2023), the cure regime
      of Art. 22.4 LEC and the MASC requirement of Organic Law 1/2025. Do not use for recovery
      of housing from occupation without any prior title (Art. 250.1.4 LEC), rural evictions,
      mortgage foreclosure, or drafting the defendant's opposition.
description: >
  Genera el documento adecuado para recuperar la posesión de una finca urbana, eligiendo la vía
  correcta conforme a la **Ley 1/2000 de Enjuiciamiento Civil (LEC)**, que regula el juicio verbal de desahucio y sus requisitos de admisión, verificada en el BOE: demanda de juicio verbal de desahucio por falta
  de pago de rentas (con opción de acumular la reclamación de las rentas debidas, Art. 437.4.3ª LEC),
  demanda de desahucio por expiración del plazo contractual o legal (Art. 250.1.1º LEC), demanda de
  desahucio por precario (Art. 250.1.2º LEC) y acuerdo extrajudicial de condonación de rentas a cambio
  de la entrega de llaves (transacción del Art. 1809 CC, homologable conforme al Art. 19 LEC). Aplica
  la resolución por impago del Art. 27 LAU, los requisitos de admisibilidad del Art. 439.3 y 439.6 LEC
  (Ley 12/2023), el régimen de enervación del Art. 22.4 LEC y el requisito de MASC de la LO 1/2025.
  NO usar para la recuperación de vivienda frente a ocupación sin título previo (Art. 250.1.4º LEC),
  desahucio de finca rustica, ejecución hipotecaria, ni para redactar la oposición del demandado.
when_to_use: |
  - El usuario quiere recuperar la posesión de una vivienda o local urbano arrendado o cedido.
  - El arrendatario no paga la renta y el arrendador quiere desahuciarlo, con o sin reclamación de rentas.
  - El contrato de arrendamiento ha expirado y el arrendatario no desaloja.
  - Un ocupante posee la finca sin título ni pago (precario) y el propietario quiere recuperarla.
  - El arrendador quiere pactar la salida del ocupante perdonando la deuda a cambio de las llaves.
  - El usuario pide una demanda de desahucio de finca urbana.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - relacion_ocupante: arrendamiento con renta / cesión gratuita sin renta / entrada sin permiso ni contrato
  - causa: falta de pago de rentas / expiración del plazo contractual o legal
  - via: demanda judicial / acuerdo extrajudicial de salida pactada
  - destino_inmueble: vivienda habitual de la parte ocupante / uso distinto del de vivienda (Art. 439.6.a LEC)
  - gran_tenedor: la parte actora es gran tenedora de vivienda conforme al Art. 3.k de la Ley 12/2023 (sí / no / desconocido)
  - requerimiento_previo: requerimiento fehaciente de pago practicado con 30 días de antelación (sí / no)
  - masc_intentado: se ha intentado un medio adecuado de solución de controversias acreditable (sí / no)
  - datos_demandante: nombre o razón social, NIF o CIF, domicilio, representante si persona jurídica, procurador y letrado
  - datos_demandado: nombre o razón social, NIF o CIF si se conoce, domicilio del inmueble
  - datos_inmueble: dirección completa, referencia catastral, municipio y partido judicial
  - datos_contrato: fecha de firma, renta mensual, duración pactada
  - rentas_debidas: importe total adeudado, conceptos y periodos impagados
  - fecha_expiracion: fecha en que expiro el contrato y sus prórrogas
  - titulo_precario: descripción de la cesión gratuita y de su revocación
  - acumular_rentas: acumular o no la reclamación de las rentas debidas (sí / no)
  - condonacion: alcance de la condonación pactada (total / parcial) y renuncia recíproca de acciones
outputs:
  - demanda_desahucio_falta_pago: demanda de juicio verbal de desahucio por falta de pago en markdown, DRAFT
  - demanda_desahucio_expiracion: demanda de juicio verbal de desahucio por expiración del plazo en markdown, DRAFT
  - demanda_desahucio_precario: demanda de juicio verbal de desahucio por precario en markdown, DRAFT
  - acuerdo_condonacion: acuerdo de condonación de rentas y entrega de llaves en markdown, DRAFT
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

# Recuperación de la Posesión de Finca Urbana

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
      "id": "relacion_ocupante",
      "rationale": "Resolver V1: determina la acción procedente, y la ocupación sin título previo queda fuera del alcance de esta skill.",
      "question": "¿Qué relación existe con la persona que ocupa el inmueble?",
      "options": [
        {"id": "arrendamiento", "label": "Un contrato de arrendamiento con renta"},
        {"id": "cesion_gratuita", "label": "Una cesión gratuita del uso, sin renta (precario)"},
        {"id": "sin_titulo", "label": "Ninguna: entró sin permiso y sin contrato"}
      ]
    },
    {
      "id": "causa",
      "rationale": "Resolver V2: separa el desahucio por falta de pago, con enervación y posible acumulación de rentas, del de expiración del plazo.",
      "question": "Si existe arrendamiento, ¿por qué causa se pretende la recuperación?",
      "show_if": {"question_id": "relacion_ocupante", "option_ids": ["arrendamiento"]},
      "options": [
        {"id": "falta_pago", "label": "Impago de rentas o cantidades asimiladas"},
        {"id": "expiracion_plazo", "label": "Expiración del plazo contractual o de sus prórrogas"},
        {"id": "no_procede", "label": "No procede: no existe contrato de arrendamiento (precario o sin título)"}
      ]
    },
    {
      "id": "via",
      "rationale": "Resolver V3: el acuerdo extrajudicial evita el procedimiento y usa un asset distinto de la demanda.",
      "question": "¿Qué vía se pretende seguir?",
      "options": [
        {"id": "demanda_judicial", "label": "Demanda de desahucio ante el juzgado"},
        {"id": "acuerdo_salida", "label": "Acuerdo extrajudicial de salida pactada con entrega de llaves"}
      ]
    },
    {
      "id": "gran_tenedor",
      "rationale": "Resolver V5: la condición de gran tenedor de vivienda activa requisitos adicionales de admisibilidad de la demanda conforme a la Ley 12/2023.",
      "question": "¿Es la parte demandante gran tenedora de vivienda?",
      "options": [
        {"id": "no", "label": "No"},
        {"id": "si", "label": "Sí"},
        {"id": "desconocido", "label": "No lo sé con certeza"}
      ]
    },
    {
      "id": "destino_inmueble",
      "rationale": "Resolver V4: la mención del destino del inmueble es obligatoria en la demanda y su omisión determina la inadmisión (artículo 439.6.a de la Ley de Enjuiciamiento Civil).",
      "question": "¿Constituye el inmueble la vivienda habitual de la persona ocupante?",
      "options": [
        {"id": "vivienda_habitual", "label": "Sí, es su vivienda habitual"},
        {"id": "otro_uso", "label": "No, tiene otro uso"}
      ]
    },
    {
      "id": "masc_intentado",
      "rationale": "Resolver V7: el intento previo acreditable condiciona la admisibilidad de la demanda.",
      "question": "¿Se ha practicado requerimiento fehaciente de pago o intentado un medio adecuado de solución de controversias?",
      "options": [
        {"id": "si", "label": "Sí, y es acreditable"},
        {"id": "no", "label": "No"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — respuesta a `relacion_ocupante`
- `V2` — respuesta a `causa`
- `V3` — respuesta a `via`
- `V4` — respuesta a `destino_inmueble`
- `V5` — respuesta a `gran_tenedor`
- `V6` — circunstancias de enervación del artículo 439.3, que se recogen en la validación de admisibilidad de la Fase 1.4, no en el formulario
- `V7` — respuesta a `masc_intentado`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si V1 = sin_titulo → **DETENER**: el caso corresponde a la recuperación de la posesión del Art. 250.1.4º de la LEC, con tramitación propia (Art. 441.1 bis LEC), legitimación tasada y exceptuada del requisito de MASC (Art. 5.2.e de la LO 1/2025). Fuera del alcance de esta skill. Informar del cauce y ofrecer escalación. No crear documento.
- Si V3 = acuerdo_salida → **HOJA ACUERDO**: `assets/template-acuerdo-condonacion-entrega-llaves.md`. V4, V5 y V7 no aplican (no hay demanda que admitir). Si V1 = cesión gratuita, no hay renta debida que condonar: omitir la cláusula tercera y adaptar el acuerdo a la entrega de llaves sin condonación, advirtiéndolo al usuario.
- Si V3 = demanda_judicial y V1 = arrendamiento y V2 = falta_pago → **HOJA IMPAGO**: `assets/template-demanda-desahucio-falta-pago.md`.
- Si V3 = demanda_judicial y V1 = arrendamiento y V2 = expiracion_plazo → **HOJA EXPIRACIÓN**: `assets/template-demanda-desahucio-expiracion-plazo.md`.
- Si V3 = demanda_judicial y V1 = arrendamiento y V2 = no_procede → **DETENER** la elección de hoja: la respuesta es incoherente, porque hay arrendamiento pero no se indica causa. Aclarar en el chat (REG-VAL-01) si la causa es el impago o la expiración del plazo, o si en realidad no media renta (precario), y volver a resolver V2 o V1 antes de elegir hoja. No crear documento hasta resolverlo.
- Si V3 = demanda_judicial y V1 = cesion_gratuita → **HOJA PRECARIO**: `assets/template-demanda-desahucio-precario.md`.
- En cualquier hoja de demanda, si no se ha intentado un medio adecuado de solución de controversias: el intento previo se documenta con un requerimiento fehaciente, cuya redacción no forma parte de esta skill. Derivar a `reclamacion-cantidad` (asset `template-burofax-masc-reclamacion.md`) y advertir de que sin ese intento acreditado la demanda puede ser inadmitida.
- Si la finca es rustica, o el arrendamiento está excluido de la LAU (Art. 5 LAU), o se pretende la ejecución hipotecaria → **DETENER**: fuera de alcance. Advertir y escalar.
- **Requisito de procedibilidad (Ley Orgánica 1/2025).** Si el intento previo de un medio adecuado de solución de controversias no está acreditado y esta skill no genera por sí misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociación, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaración responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a trámite.

### 1.4 Validación de admisibilidad (interno, antes de la Fase 3)

- **TODAS LAS HOJAS DE DEMANDA (Art. 439.6 LEC, redacción de la Ley 12/2023):** la demanda es inadmisible si no especifica (a) si el inmueble constituye vivienda habitual de la persona ocupante — valor de V4 — y (b) si la parte actora es gran tenedora de vivienda en los términos del Art. 3.k de la Ley 12/2023 — valor de V5. Si V5 = no, debe acompañarse certificación del Registro de la Propiedad con la relación de propiedades a nombre de la parte actora. Si V5 = no, no dar el dato por resuelto: explicar el umbral y pedir que lo confirme antes de redactar.
  **Importante:** las letras c) del apartado 6 y el apartado 7 del Art. 439 (acreditar la vulnerabilidad de la parte demandada y acudir a conciliación o intermediación previa cuando la actora es gran tenedora) fueron declarados inconstitucionales y nulos por la Sentencia del Tribunal Constitucional 26/2025, de 29 de enero. NO exigirlos ni incluirlos en la demanda.
- **HOJA IMPAGO (Art. 439.3 LEC):** la demanda es inadmisible si no se indican las circunstancias concurrentes que permiten o impiden la enervación en el caso concreto. Ese pronunciamiento se construye con el valor de V6 y es obligatorio.
- **HOJA IMPAGO (Art. 27.2.a LAU):** confirmar que lo impagado es la renta o cantidades asimiladas cuyo pago corresponde a la parte arrendataria.
- **HOJA EXPIRACIÓN:** confirmar que el contrato y sus prórrogas legales han vencido (Arts. 9, 10 y 11 LAU) y que no procede prórroga obligatoria ni tácita.
- **HOJA PRECARIO:** confirmar la titularidad de la parte actora y la ausencia de título y de renta en la parte ocupante. Si media contraprestación de cualquier clase, no hay precario: reconducir a la hoja que corresponda.
- **POSTULACIÓN:** en el desahucio, la clase de juicio se determina por razón de la materia (Art. 250.1.1º y 2º), no por la cuantía, por lo que las excepciones de los Arts. 23.2.1º y 31.2.1º de la LEC no operan: abogado y procurador son preceptivos. La cuantía, a los efectos que procedan, es la de una anualidad de renta (Art. 251.9ª LEC).
- **MASC:** el desahucio no figura entre las materias exceptuadas del Art. 5.2 de la LO 1/2025, por lo que el intento previo es requisito de procedibilidad en las tres hojas de demanda. Solo la recuperación de la posesión del Art. 250.1.4º está exceptuada (letra e).
- **COMPETENCIA (Art. 52.1.7 LEC):** juzgado del lugar en que esté sita la finca, sin sumisión posible a otro fuero.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 250.1.1º y 2º, 439, 440, 441 y 444 de la Ley de Enjuiciamiento Civil (LEC), modificados por la Ley 12/2023 por el derecho a la vivienda; Art. 27 de la LAU (resolución por impago); y Art. 1.569 del Código Civil.
2. **Orientación Legal del Caso:**

**Informa la vía y la fuente aplicable.** Textos fijos por hoja:
   - IMPAGO: "A su caso corresponde el juicio verbal de desahucio por falta de pago, conforme al artículo 250.1.1º de la Ley 1/2000, de Enjuiciamiento Civil, cualquiera que sea la cuantía, con fundamento sustantivo en el artículo 27.2.a) de la Ley 29/1994, de Arrendamientos Urbanos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - EXPIRACIÓN: "A su caso corresponde el juicio verbal de desahucio por expiración del plazo, conforme al artículo 250.1.1º de la Ley 1/2000, de Enjuiciamiento Civil, en relación con los artículos 9 y 10 de la Ley 29/1994, de Arrendamientos Urbanos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - PRECARIO: "A su caso corresponde el juicio verbal de desahucio por precario, conforme al artículo 250.1.2º de la Ley 1/2000, de Enjuiciamiento Civil, en relación con el artículo 348 del Código Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - ACUERDO: "Su caso se resolverá mediante un contrato de transacción, regulado en el artículo 1809 del Código Civil, con condonación de la deuda condicionada a la entrega de la posesión (artículos 1156 y 1187 del Código Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - En las tres hojas de demanda, añadir: "El desahucio no figura entre las materias exceptuadas del artículo 5.2 de la Ley Orgánica 1/2025, de 2 de enero, por lo que deberá acreditarse el intento previo de una solución extrajudicial para que la demanda sea admitida (artículos 264.4º y 403.2 de la Ley de Enjuiciamiento Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2025-76"
   - En las tres hojas de demanda, añadir: "En el desahucio son preceptivos abogado y procurador, porque la clase de juicio viene determinada por la materia y no por la cuantía."

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

### Secciones — HOJA IMPAGO / HOJA EXPIRACIÓN / HOJA PRECARIO

1. **Parte demandante** *(dato objetivo — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de la parte que reclama la posesión." Ejecute prioritariamente `search_clients`. Si la ficha cubre los datos, úselos directamente; solicite solo los campos pendientes (ej. procurador/letrado) mediante `slot_filling_request`. Vuelque directamente los datos al documento con `edit_file` (o en `create_file` si ya constaban), sustituyendo exhaustivamente los nombres en todas sus apariciones (título/encabezado H1, comparecencia/encabezamiento procesal y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones), informe al usuario en chat y continúe sin confirmación previa en chat.
2. **Parte demandada** *(dato objetivo — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de la parte demandada." Ejecute prioritariamente `search_clients` o use los datos conocidos; solo si faltan campos indispensables, use `slot_filling_request`. Vuelque directamente los datos al documento con `edit_file` (o en `create_file`), sustituyendo exhaustivamente los nombres en todas sus apariciones (título H1, comparecencia y firmas), informe en chat y continúe sin confirmación previa en chat.
3. **El inmueble y su destino** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Describimos ahora el inmueble objeto del procedimiento." Solicita en bloque mediante `slot_filling_request`: a) dirección completa; b) referencia catastral; c) municipio y partido judicial. El destino del inmueble ya quedó resuelto en la clasificación: no volver a preguntarlo, pero hacerlo constar expresamente en el documento porque su omisión determina la inadmisión (Art. 439.6.a LEC). Vista previa en chat, confirmación y `edit_file`.
4. **Condición de gran tenedor** *(dato objetivo con consecuencia documental)*. Anuncio fijo: "Debemos hacer constar en la demanda su condición respecto de la tenencia de vivienda." El valor ya quedó resuelto en la clasificación. Explica antes de continuar: la mención es obligatoria y su omisión determina la inadmisión (Art. 439.6.b LEC); si la parte actora NO es gran tenedora, debe acompañarse certificación del Registro de la Propiedad con la relación de sus propiedades, y hay que confirmar con el usuario que la solicitara. Aclara también, si el usuario lo plantea, que el deber de acreditar la vulnerabilidad de la parte demandada y de acudir a conciliación previa fue anulado por la Sentencia del Tribunal Constitucional 26/2025.
5. **Contrato y causa del desahucio** *(dato objetivo, con contenido propio de cada hoja)*.
   - IMPAGO. Anuncio fijo: "Pasamos al contrato y a la deuda de rentas." Solicita en bloque mediante `slot_filling_request`: a) fecha del contrato; b) renta mensual; c) periodos impagados; d) importe total adeudado y conceptos que lo componen (rentas y cantidades asimiladas del Art. 27.2.a LAU); e) relación de documentos que se aportaran. Vista previa en chat, confirmación y `edit_file`.
   - EXPIRACIÓN. Anuncio fijo: "Pasamos al contrato y a su vencimiento." Solicita en bloque mediante `slot_filling_request`: a) fecha del contrato; b) duración pactada; c) fecha en que expiro el contrato y sus prórrogas; d) si se comunico la voluntad de no renovar, y con que antelación y por qué medio. Vista previa en chat, confirmación y `edit_file`.
   - PRECARIO. Anuncio fijo: "Pasamos al origen de la ocupación y a su revocación." Solicita en bloque: a) título de propiedad de la parte actora y documento que lo acredita; b) como y cuando se cedió el uso gratuito y que relación une a las partes; c) como y cuando se revoco la tolerancia y se requirió la restitución. Verifica expresamente que no media renta ni contraprestación de ninguna clase. Vista previa en chat, confirmación y `edit_file`.
6. **Requerimiento previo y enervación** *(cláusula de negociación — explicar antes de decidir; solo HOJA IMPAGO)*. Anuncio fijo: "Abordamos ahora el requerimiento previo de pago y sus efectos sobre la enervación." Explica antes de pedir la decisión: la parte demandada puede enervar la acción pagando o consignando lo debido y dejar sin efecto el desahucio (Art. 22.4 LEC), salvo que ya enervara en una ocasión anterior o que se le requiriera de pago por medio fehaciente con al menos treinta días de antelación a la demanda sin haber pagado. Según el valor resuelto en la clasificación:
   - Requerimiento con más de treinta días y justificante: si aún no se conocen, pide el medio empleado (burofax, requerimiento notarial) y su fecha exacta, y se hace constar en la demanda que no procede la enervación, acompañando el requerimiento y su acuse.
   - Requerimiento sin ese plazo, o sin justificante, o inexistente: la enervación será posible. Explica que existe la alternativa de practicar ahora un requerimiento fehaciente y esperar treinta días antes de presentar la demanda, con la ventaja de que el mismo burofax puede servir para acreditar el intento de solución previa exigido por la Ley Orgánica 1/2025, y pide al usuario que decida entre presentar ya la demanda asumiendo la enervación o requerir primero. Confirma la decisión antes de escribirla.
   En todo caso, la demanda debe pronunciarse sobre las circunstancias que permiten o impiden la enervación: su omisión determina la inadmisión (Art. 439.3 LEC).
7. **Acumulación de la reclamación de rentas** *(cláusula de negociación — explicar antes de decidir; HOJA IMPAGO y HOJA EXPIRACIÓN)*. Anuncio fijo: "Decidimos ahora si reclamamos las rentas debidas en la misma demanda." Explica antes de pedir la decisión: cabe acumular a la acción de desahucio la reclamación de las rentas y cantidades análogas vencidas y no pagadas, con independencia de su importe, y también la acción contra el fiador o avalista solidario previo requerimiento de pago no satisfecho (Art. 437.4.3ª LEC); los pronunciamientos sobre las acciones acumuladas si producen cosa juzgada, a diferencia del desahucio en si (Art. 447.2 LEC); acumular evita un segundo procedimiento posterior. Pide la decisión, y si es afirmativa, el importe y los periodos, e inserta los bloques condicionales de acumulación del asset. Confirmación propia.
8. **Solicitud anticipada del lanzamiento** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Concretamos la solicitud de señalamiento del lanzamiento." Explica antes de pedir la decisión: puede interesarse ya en la demanda que se tenga por solicitada la ejecución del lanzamiento en la fecha y hora que fije el juzgado (Art. 437.3 in fine LEC); con esa solicitud, la sentencia condenatoria o el decreto que ponga fin al desahucio se ejecutan directamente el día y hora señalados, sin necesidad de ningún otro trámite ni de nueva notificación (Art. 549.3 LEC). Es la opción habitual y acorta materialmente los plazos. Confirmación propia.
9. **Compromiso de condonación por desalojo voluntario** *(cláusula de negociación — explicar antes de decidir; HOJA IMPAGO y HOJA EXPIRACIÓN)*. Anuncio fijo: "Valoramos si desea ofrecer una condonación a cambio del desalojo voluntario." Explica antes de pedir la decisión: puede anunciarse en la demanda el compromiso de condonar toda o parte de la deuda y de las costas, con expresión de la cantidad concreta, condicionado a que la parte demandada desaloje voluntariamente dentro del plazo que se indique, que no podrá ser inferior a quince días desde la notificación de la demanda (Art. 437.3 LEC); ese compromiso se le pone de manifiesto en el requerimiento y su aceptación equivale a un allanamiento (Art. 438.5 LEC), con señalamiento subsidiario del lanzamiento directo (Art. 447.1 LEC). Si el usuario prefiere pactarlo fuera del proceso, indicáselo y ofrece el acuerdo de condonación y entrega de llaves como documento alternativo o complementario. Si declina, omitir el bloque. Confirmación propia.
10. **Vivienda habitual y actuación de los servicios sociales** *(informativo, sin pregunta; solo si V4 = vivienda habitual)*. Anuncio fijo: "Le informo de las consecuencias procesales de que el inmueble sea la vivienda habitual de la parte ocupante." Informar: el juzgado comunicará de oficio la existencia del procedimiento a las Administraciones competentes en vivienda y servicios sociales, que pueden verificar la situación de vulnerabilidad y proponer alternativa habitacional; si se confirma, el tribunal puede suspender el proceso por un máximo de dos meses si la parte demandante es persona física y de cuatro meses si es persona jurídica, ponderando también la vulnerabilidad de la parte actora (Art. 441.5, 441.6 y 441.7 LEC). No requiere dato del usuario; encadenar con la sección siguiente. Informar también de que el régimen extraordinario de suspensión de lanzamientos ligado a la crisis sanitaria dejo de surtir efecto y de que su estado debe verificarse en cada caso, junto con la normativa autonómica de vivienda aplicable.
11. **Solución previa (MASC)** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Concretamos por último los términos del intento de solución previa." Si ya se intento, pedir el medio empleado, la fecha y el documento que lo acredita, y describir el proceso de negociación en la demanda (Art. 399.3 LEC). Si no se intento, explica: la acreditación puede consistir en un documento firmado por ambas partes o en cualquier documento que pruebe que la otra parte recibió la solicitud o la propuesta (Art. 10.2 de la LO 1/2025); el proceso se entiende terminado sin acuerdo si transcurren treinta días naturales desde la recepción sin reunión ni respuesta escrita (Art. 10.4.a); y la demanda debe presentarse dentro del año siguiente (Art. 7.3). Advierte de que la demanda no debe presentarse hasta disponer del justificante y de que los campos correspondientes quedan como placeholders hasta entonces. Confirmación propia.
12. **Juzgado competente** *(dato objetivo con validación)*. Anuncio fijo: "Determinamos ahora el juzgado competente." Es el del lugar en que esté sita la finca (Art. 52.1.7 LEC). Si el usuario propone otro fuero o invoca una cláusula de sumisión del contrato, advertir de que no cabe y corregirlo.
13. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Lugar de firma; la fecha por defecto es la del día, salvo indicación en contrario.

### Secciones — HOJA ACUERDO

1. **Parte arrendadora** *(dato objetivo — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de la parte arrendadora." Búsqueda prioritaria con `search_clients`, volcado directo a disco per `REG-CLI-04`, informe en chat y continúe sin confirmación previa en chat.
2. **Parte arrendataria u ocupante** *(dato objetivo — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de la parte que ocupa el inmueble." Búsqueda prioritaria con `search_clients`, volcado directo a disco per `REG-CLI-04`, informe en chat y continúe sin confirmación previa en chat.
3. **Inmueble y contrato que se extingue** *(dato objetivo — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Describimos el inmueble y el contrato que se va a extinguir." Solicita en bloque mediante `slot_filling_request`: a) dirección completa y referencia catastral; b) título de la parte arrendadora; c) fecha del contrato y renta mensual; d) si existe procedimiento judicial en curso, juzgado y autos. Vista previa en chat, confirmación y `edit_file`.
4. **Deuda que se reconoce** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Pasamos a fijar la deuda que se reconoce." Explica antes de pedir la cifra: el reconocimiento de deuda fija el importe sobre el que operara la condonación y, si el acuerdo se incumple, es la cantidad que renace; conviene que incluya todos los conceptos vencidos (rentas y cantidades asimiladas) y que se cierre a una fecha concreta. Pide el importe, los conceptos y los periodos. Confirmación propia.
5. **Alcance de la condonación** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Abordamos ahora el alcance de la condonación." Explica antes de pedir la decisión: la condonación puede ser total o parcial; si es parcial hay que fijar la cantidad que subsiste, su forma de pago y su plazo; la condonación se pacta como contraprestación del desalojo dentro de una transacción (Art. 1809 CC) y por eso debe quedar condicionada a la entrega efectiva, de modo que una condonación incondicionada extinguiría la deuda aunque el inmueble no se entregase (Arts. 1156 y 1187 CC); y la operación puede tener consecuencias tributarias para ambas partes que conviene verificar con un asesor fiscal. Confirmación propia.
6. **Entrega de llaves y de la posesión** *(cláusula de negociación — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Concretamos la entrega de las llaves y de la posesión." Explica antes de pedir los datos: la fecha y la hora deben ser ciertas, porque de ellas depende la eficacia de la condonación, y conviene levantar acta con el número de llaves, el estado del inmueble y las lecturas de los contadores. Solicita en bloque mediante `slot_filling_request`: a) fecha y hora de la entrega; b) lugar; c) tratamiento de las rentas que se devenguen hasta la entrega. Muestra vista previa en el chat, pide confirmación y aplica `edit_file`.
7. **Fianza, garantías y suministros** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Determinamos el destino de la fianza y de las garantías." Explica: la fianza puede devolverse, aplicarse a la deuda subsistente o compensarse con los daños que resulten del acta; conviene decidirlo ahora para evitar una controversia posterior. Pide el importe de la fianza, su destino y, si existen, el tratamiento de las garantías adicionales. Confirmación propia.
8. **Renuncia recíproca de acciones** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Valoramos la renuncia recíproca de acciones." Explica antes de pedir la decisión: una renuncia amplia cierra el asunto pero impide reclamar después los daños en el inmueble; la posición conservadora es exceptuar de la renuncia los daños que consten en el acta de entrega y los daños ocultos. Ofrece las dos redacciones del asset y pide la decisión. Confirmación propia.
9. **Consecuencias del incumplimiento** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Fijamos las consecuencias del incumplimiento del acuerdo." Explica: si no se entrega en la fecha pactada, la condonación queda sin efecto, renace la deuda íntegra y la parte arrendadora puede ejercitar sin más trámite las acciones de desahucio y de reclamación; si hay procedimiento en curso, puede instar su continuación. Confirma la redacción antes de aplicarla.
10. **Fuerza ejecutiva del acuerdo** *(cláusula de negociación — explicar antes de decidir)*. Anuncio fijo: "Decidimos como dotar de fuerza ejecutiva al acuerdo." Explica las tres opciones y sus consecuencias: si hay procedimiento en curso, la homologación judicial (Art. 19 LEC) le da los efectos de la transacción judicial y permite ejecutarlo como una sentencia (Art. 517.2.3º LEC); sin procedimiento, la elevación a escritura pública lo convierte en título ejecutivo (Art. 517.2.2º LEC); si no se hace ninguna de las dos, el acuerdo obliga entre las partes (Art. 1816 CC) pero su incumplimiento obliga a un nuevo pleito. Recomienda la homologación o la escritura pública. Confirmación propia.
11. **Lugar, fecha y firma** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del acuerdo." Lugar de firma; la fecha por defecto es la del día, salvo indicación en contrario.

Al rellenar cualquier hoja de demanda, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre la LEC, la LAU y la LO 1/2025 en el BOE antes de redactar (Fase 2). Sin verificación, no proceder.
2. Si se detecta una versión posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario. No usar una versión desactualizada.
3. Las menciones del Art. 439.6.a) y b) de la LEC (destino del inmueble y condición de gran tenedor de la parte actora) son obligatorias en toda demanda que pretenda recuperar la posesión de una finca por las vías del Art. 250.1.1º, 2º, 4º y 7º. Su omisión determina la inadmisión. Nunca redactar una demanda sin ellas.
4. Las letras c) del apartado 6 y el apartado 7 del Art. 439 de la LEC fueron declarados inconstitucionales y nulos por la STC 26/2025, de 29 de enero. No exigir al usuario acreditar la vulnerabilidad de la parte demandada ni acudir a conciliación o intermediación previa por ser gran tenedor, ni incluir esas menciones en la demanda.
5. En el desahucio por falta de pago, la demanda debe pronunciarse sobre las circunstancias que permiten o impiden la enervación (Art. 439.3 LEC). Nunca omitir ese pronunciamiento.
6. La enervación (Art. 22.4 LEC) solo cabe en el desahucio por falta de pago, una sola vez, y no procede si se requirió de pago por medio fehaciente con al menos treinta días de antelación sin resultado. No cabe enervación en expiración del plazo ni en precario. Informar siempre de esta regla y nunca afirmar que la enervación está excluida sin justificante del requerimiento.
7. El intento previo de un medio adecuado de solución de controversias es requisito de procedibilidad en las tres hojas de demanda: el desahucio no figura entre las materias exceptuadas del Art. 5.2 de la LO 1/2025. Solo la recuperación de la posesión del Art. 250.1.4º está exceptuada (letra e).
8. Competencia exclusiva del tribunal del lugar en que esté sita la finca (Art. 52.1.7 LEC). No admitir sumisión a otro fuero aunque el contrato la contenga.
9. En el desahucio, abogado y procurador son preceptivos: la clase de juicio se determina por la materia, no por la cuantía, y las excepciones de los Arts. 23.2.1º y 31.2.1º de la LEC no operan.
10. El régimen extraordinario de suspensión de lanzamientos por vulnerabilidad tiene vigencia temporal y ha sido objeto de prórrogas no siempre convalidadas. Nunca afirmar que está vigente ni que está derogado sin haberlo comprobado en el texto consolidado en la Fase 2. Lo que si es permanente es el mecanismo de los Arts. 441.5 a 441.7 de la LEC en desahucios de vivienda habitual.
11. Nunca redactar cláusulas o pretensiones que contravengan normas imperativas de la LAU (Art. 6 LAU) ni afirmar la resolución del contrato sin base en el Art. 27 LAU.
12. En el acuerdo de condonación, la condonación debe quedar siempre condicionada a la entrega efectiva de la posesión. Nunca redactar una condonación incondicionada previa al desalojo.
13. Nunca inventar datos, rentas, fechas, referencias catastrales ni jurisprudencia. Los campos no proporcionados quedan como `{{DATO}}`.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para la recuperación de la posesión de una vivienda frente a quien entro en ella sin título ni relación previa (Art. 250.1.4º LEC): tiene legitimación tasada, tramitación propia (Art. 441.1 bis LEC) y está exceptuada del MASC. Advertir y escalar.
- No usar para la efectividad de derechos reales inscritos frente a quien los perturba (Art. 250.1.7º LEC).
- No usar para desahucio de finca rustica ni de arrendamientos excluidos de la LAU (Art. 5 LAU).
- No usar para la ejecución hipotecaria ni para el lanzamiento derivado de ella.
- No usar para redactar la oposición de la parte demandada, el escrito de enervación ni el incidente de suspensión por vulnerabilidad: advertir y escalar.
- No usar para reclamar solo rentas sin recuperar la posesión: derivar a `reclamacion-cantidad`.
- No usar para redactar el burofax de requerimiento previo: el asset está en `reclamacion-cantidad`.
- No usar si el usuario pide opinión jurídica sobre la estrategia de un litigio: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
