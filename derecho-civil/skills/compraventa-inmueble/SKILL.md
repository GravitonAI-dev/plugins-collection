---
name: compraventa-inmueble
title: Compraventa de inmueble
i18n:
  en:
    name: property-sale
    title: Property sale
    description: >
      Generates the right document for a home sale between private individuals under the **Civil
      Code**, which governs the sale contract, earnest money and the consequences of breach, in
      the consolidated version verified in the BOE. It covers three documents: the earnest money
      (arras) contract prior to the sale (**Art. 1454 CC**), the full private home sale contract
      (**Arts. 1445 et seq. CC**) and the out-of-court demand for performance when a party
      breaches a signed contract (**Arts. 1124 and 1504 CC**). It expressly deals with the type
      of earnest money and its consequence, encumbrances on the property, allocation of taxes
      and costs, the mortgage financing condition and the tenant's pre-emption rights (**Art. 25
      of Law 29/1994**). It does not replace the notarial deed or land registration, performs no
      title due diligence or valuation, and does not cover sales of business premises, off-plan
      new builds with staged payments, or inheritances or gifts of real estate.
description: >
  Genera el documento que corresponda en una compraventa de vivienda entre particulares conforme al
  **Código Civil**, que regula el contrato de compraventa, las arras y las consecuencias del
  incumplimiento, en su versión consolidada verificada en el BOE. Cubre tres documentos: contrato de
  arras o señal previo a la compraventa (**Art. 1454 CC**), contrato privado de compraventa de
  vivienda completo (**Arts. 1445 y siguientes CC**) y requerimiento extrajudicial de cumplimiento
  cuando una parte incumple un contrato ya firmado (**Arts. 1124 y 1504 CC**). Trata expresamente la
  clase de arras y su consecuencia, las cargas del inmueble, el reparto de impuestos y gastos, la
  condición suspensiva de financiación hipotecaria y el derecho de tanteo y retracto del arrendatario
  (**Art. 25 de la Ley 29/1994**). NO sustituye la escritura pública notarial ni la inscripción
  registral, no hace due diligence de titularidad ni valoración del inmueble, y NO cubre la
  compraventa de local, la de obra nueva sobre plano con entregas a cuenta, ni las herencias o
  donaciones de inmuebles.
when_to_use: |
  - El usuario va a comprar o vender una vivienda y necesita el contrato de arras o señal previo.
  - El usuario necesita el contrato privado de compraventa de vivienda antes de ir al notario.
  - El usuario ya firmo un contrato de arras o de compraventa y la otra parte no cumple: no paga, no
    acude a la notaría en el plazo pactado o no entrega la posesión.
  - El usuario quiere saber qué ocurre con las arras si una de las partes se echa atrás.
  - El usuario compra con hipoteca aún no concedida y necesita proteger su posición si le deniegan el
    préstamo.
  - El usuario compra o vende una vivienda que está arrendada.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - documento: contrato de arras / contrato privado de compraventa / requerimiento de cumplimiento
  - posicion_cliente: comprador / vendedor
  - financiacion_pendiente: sí / no
  - inmueble_arrendado: sí / no / no lo sé
  - datos_vendedor: nombre o razón social, NIF/CIF, domicilio, estado civil y régimen matrimonial, representación
  - datos_comprador: nombre o razón social, NIF/CIF, domicilio, estado civil y régimen matrimonial, representación
  - datos_inmueble: dirección, municipio, provincia, código postal, superficie, referencia catastral, datos registrales, anexos
  - precio_y_pago: precio total, arras, pagos a cuenta, importe al otorgamiento, medios de pago
  - clase_arras: confirmatorias / penales / penitenciales, y consecuencia pactada para cada parte
  - cargas: situación registral, hipoteca pendiente, deudas de comunidad, IBI
  - estado_posesorio: libre / arrendado / con ocupantes, y notificación al arrendatario
  - fiscalidad: reparto de ITP, plusvalía municipal y gastos de escritura e inscripción
  - plazo_escritura: fecha límite de otorgamiento, notario y quién lo designa
  - datos_incumplimiento: obligación incumplida, fecha de vencimiento, importe pendiente, requerimientos previos
outputs:
  - contrato_arras: contrato de arras o señal sobre bien inmueble en markdown, DRAFT
  - contrato_compraventa_vivienda: contrato privado de compraventa de vivienda en markdown, DRAFT
  - requerimiento_cumplimiento: requerimiento extrajudicial de cumplimiento en markdown, DRAFT
references:
  - references/arras-cargas-fiscalidad-y-retracto.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
assets:
  - assets/template-contrato-arras.md
  - assets/template-contrato-compraventa-vivienda.md
  - assets/template-requerimiento-cumplimiento.md
---

# Compraventa de Vivienda: Arras, Contrato Privado y Requerimiento

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
      "id": "documento",
      "rationale": "Resolver V1: cada documento tiene su propio asset y su propio régimen legal.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "arras", "label": "Contrato de arras o señal, previo a la compraventa"},
        {"id": "compraventa", "label": "Contrato privado de compraventa de vivienda"},
        {"id": "requerimiento", "label": "Requerimiento de cumplimiento por incumplimiento de la otra parte"}
      ]
    },
    {
      "id": "posicion_cliente",
      "rationale": "Resolver V2: orienta la redacción de las garantías y de las consecuencias del desistimiento a favor de la parte a la que se asiste.",
      "question": "¿A qué parte asiste usted?",
      "options": [
        {"id": "comprador", "label": "Al comprador"},
        {"id": "vendedor", "label": "Al vendedor"}
      ]
    },
    {
      "id": "inmueble_arrendado",
      "rationale": "Resolver V4: si el inmueble está arrendado como vivienda, nace el derecho de tanteo y retracto del artículo 25 LAU y hay que notificar al arrendatario.",
      "question": "¿Está el inmueble arrendado en este momento?",
      "options": [
        {"id": "no", "label": "No, está libre de arrendatarios y de ocupantes"},
        {"id": "si_vivienda", "label": "Sí, arrendado como vivienda"},
        {"id": "no_lo_se", "label": "No lo sé con certeza"}
      ]
    },
    {
      "id": "financiacion_pendiente",
      "rationale": "Resolver V3: la financiación hipotecaria pendiente condiciona la condición suspensiva y los plazos del contrato.",
      "question": "¿Depende la operación de una financiación hipotecaria todavía no concedida?",
      "options": [
        {"id": "no", "label": "No"},
        {"id": "si", "label": "Sí"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — respuesta a `documento`
- `V2` — respuesta a `posicion_cliente`
- `V3` — respuesta a `financiacion_pendiente`
- `V4` — respuesta a `inmueble_arrendado`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si V1 = arras → **HOJA ARRAS**: `assets/template-contrato-arras.md`.
- Si V1 = compraventa → **HOJA COMPRAVENTA**: `assets/template-contrato-compraventa-vivienda.md`.
- Si V1 = requerimiento → **HOJA REQUERIMIENTO**: `assets/template-requerimiento-cumplimiento.md`. V3 no se pregunta; V4 solo se usa para advertir del riesgo de retracto si el contrato ya firmado afecta a un inmueble arrendado sin notificar.
- Si V4 = si vivienda y el sub-vector es arrendamiento de local o para uso distinto de vivienda → **DETENER**: la compraventa de local está fuera de alcance. Antes de escalar, advierte de que el artículo 31 de la Ley 29/1994 aplica al arrendamiento para uso distinto de vivienda el mismo régimen de tanteo y retracto del artículo 25, por lo que el riesgo de retracto también existe. Escalar. No crear documento.
- Si lo que se pretende es la compraventa de obra nueva **sobre plano con entregas a cuenta** del precio antes de la terminación → **DETENER**: la disposición adicional primera de la Ley 38/1999 exige garantizar la devolución de las cantidades anticipadas mediante aval solidario de entidad de crédito o seguro de caución individualizado desde la obtención de la licencia de edificación, percibirlas en cuenta especial separada, y hacer constar en el contrato la obligación de devolución, la entidad garante y la cuenta. Advertir de esos requisitos y escalar. No crear documento.
- Si lo que se pretende es la transmisión de un inmueble por herencia, legado, donación, aportación a sociedad, permuta, dación en pago o adjudicación en liquidación de gananciales → **DETENER**: fuera de alcance. Derivar a `herencia` cuando sea sucesorio, o escalar en los demás casos.
- Si el inmueble es un local comercial, una nave, un solar, una finca rustica o una plaza de garaje que se transmite de forma independiente → **DETENER**: los assets están construidos para vivienda. Advertir y escalar.
- Si el caso se rige por derecho civil foral o especial (vecindad civil catalana, navarra, aragonesa, balear, gallega o vizcaína, o inmueble sujeto a esa legislación) → **DETENER**: los assets se construyen sobre el Código Civil común y Cataluña, entre otros territorios, regula la compraventa con reglas propias. Advertir y escalar.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **TODAS LAS HOJAS — legitimación y titularidad.** Confirmar que el cliente es parte del contrato (o va a serlo) y, si es el vendedor, que es titular del inmueble. Si el inmueble pertenece a **varios cotitulares**, todos deben consentir la venta: pedir su relación y advertir de que la firma de uno solo no vincula a los demás. Si el inmueble es la **vivienda habitual del matrimonio del vendedor**, advertir de que la disposición requiere el consentimiento del otro cónyuge y activar el bloque de comparecencia correspondiente.
- **TODAS LAS HOJAS — V4 arrendado, PARADA BLOQUEANTE (Art. 25 de la Ley 29/1994).** Si el inmueble está arrendado como vivienda, **antes de continuar** informa del derecho de tanteo y retracto y pregunta si ya se ha notificado fehacientemente al arrendatario la decisión de vender, el precio y las demás condiciones esenciales, y en que fecha. Tres salidas:
  1. **Notificación practicada y transcurridos los treinta días naturales sin tanteo:** continuar, activando el bloque de notificación practicada del asset y pidiendo la fecha y el medio. Recordar que los efectos de la notificación caducan a los ciento ochenta días naturales: si la firma se retrasa más allá, hay que volver a notificar.
  2. **Notificación NO practicada:** advertir expresamente, en el mismo turno, de que (a) el arrendatario podrá ejercitar el retracto sobre el inmueble ya vendido y subrogarse en la posición del comprador reembolsándole el precio y los gastos (Art. 25.3 en relación con el Art. 1518 CC), y (b) la escritura de venta de vivienda arrendada **no será inscribible** en el Registro de la Propiedad sin justificar la notificación (Art. 25.5), debiendo el vendedor declarar bajo pena de falsedad en documento público que no estaba arrendada si así fuera. Ofrecer dos vías: practicar la notificación y esperar los treinta días antes de firmar, o firmar condicionando la eficacia del contrato a la notificación y al transcurso del plazo (bloque condicional del asset). **No continuar con el resto del documento hasta que el cliente elija una de las dos.**
  3. **El cliente alega que el arrendatario renuncio al derecho de adquisición preferente:** **no dar por buena la renuncia.** Pedir el contrato de arrendamiento y comprobar que la renuncia es expresa (Art. 25.8) y que se ha practicado, o se va a practicar, la comunicación de la intención de vender con una **antelación mínima de treinta días** a la fecha de formalización de la compraventa, que la renuncia no elimina. Si el contrato de arrendamiento no está disponible, advertir y dejar el punto como pendiente de verificación antes de la firma.
  - **Excepción del Art. 25.7:** si la vivienda se vende conjuntamente con las restantes viviendas o locales del arrendador que forman parte del mismo inmueble, o distintos propietarios venden a un mismo comprador la totalidad de pisos y locales, no hay tanteo ni retracto. Pero **si en el inmueble solo existe una vivienda, si los hay**: no aplicar la excepción a una casa unifamiliar arrendada. Verificar además si la normativa autonómica de vivienda atribuye tanteo y retracto a la Administración en esos supuestos.
- **HOJA ARRAS y HOJA COMPRAVENTA — cargas (BLOQUEANTE en su redacción).** Preguntar si se dispone de nota simple o certificación registral actualizada. Si **no** se dispone: advertir de que no puede afirmarse que el inmueble esté libre de cargas, redactar la situación registral **como manifestación del vendedor** con la consecuencia pactada si resulta inexacta, y dejar constancia en el documento de la obligación de comprobarlo antes de firmar. **Prohibido escribir que el inmueble está libre de cargas sobre la sola afirmación verbal del vendedor.** Recomendar siempre nota simple registral, certificado de la comunidad de propietarios con el visto bueno del presidente y último recibo del IBI.
- **HOJA ARRAS — clase de arras (BLOQUEANTE).** El documento no puede cerrarse con la clase de arras sin pactar ni con la consecuencia del desistimiento sin redactar. Si el cliente no decide, no se cierra el documento: se explica de nuevo y se insiste, advirtiendo de que del silencio la jurisprudencia tiende a presumir el carácter confirmatorio, que **no** permite desistir.
- **HOJA COMPRAVENTA — obra nueva ya recibida.** Si la vivienda es de obra nueva y la obra ya está recibida, activar el bloque de garantías de la Ley 38/1999 y pedir la fecha de recepción de la obra, de la que se computan los plazos de diez, tres y un año del Art. 17. Verificar que se entrega copia de las pólizas del Art. 19. Si la obra **no** está terminada y hay entregas a cuenta, aplicar la parada de enrutamiento.
- **HOJA REQUERIMIENTO — vía del requerimiento (Art. 1504 CC, BLOQUEANTE).** Si el requirente es el **vendedor** y lo que busca es resolver la compraventa por impago del precio, verificar que el requerimiento se practicó **judicialmente o por acta notarial**. Un burofax constituye en mora, fija la fecha e interrumpe la prescripción, pero **no cierra la facultad del comprador de pagar tardíamente**: mientras no medie requerimiento judicial o notarial, podrá pagar aun después de vencido el plazo y evitar la resolución, y hecho el requerimiento el Juez no podrá concederle nuevo término. Si el cliente quiere enviar solo un burofax, advertirlo expresamente y dejarlo escrito en el documento.
- **HOJA REQUERIMIENTO — prescripción (Art. 1964.2 CC).** Calcular si han transcurrido cinco años desde que la obligación era exigible. Si el plazo está agotado o próximo a agotarse, advertir y escalar antes de redactar; recordar que la reclamación extrajudicial interrumpe la prescripción (Art. 1973 CC), de modo que la fecha del requerimiento es relevante.
- **HOJA REQUERIMIENTO — saneamiento por vicios ocultos (Art. 1490 CC).** Si lo que el cliente quiere reclamar son vicios o defectos ocultos, verificar que no han transcurrido **seis meses desde la entrega**. Si han transcurrido, advertir de que la acción de saneamiento está extinguida y escalar: no dar falsas expectativas. Recordar que el vendedor no responde de los defectos manifiestos o que estuvieren a la vista (Art. 1484).
- **TODAS LAS HOJAS — fiscalidad.** No calcular la cuota del ITP ni de la plusvalía municipal: el tipo del ITP lo fija cada Comunidad Autónoma y la plusvalía depende de la ordenanza municipal. Identificar al sujeto pasivo legal y remitir a la normativa aplicable.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 1.445 y siguientes del Código Civil (compraventa), Art. 1.454 CC (arras o señal y desistimiento), Art. 1.504 CC (resolución por impago e imperatividad de requerimiento notarial o judicial), y Art. 25 de la Ley 29/1994 (LAU, tanteo y retracto si la vivienda está arrendada).
2. **Orientación Legal del Caso:**

**Informa la vía y la fuente aplicable.** Textos fijos por hoja:
   - ARRAS: "A su caso corresponde un contrato de arras o señal previo a la compraventa, regido por el Código Civil y, en cuanto a las arras entregadas, por su artículo 1.454. Debe saber que ese artículo solo contempla el desistimiento perdiendo las arras o devolviéndolas duplicadas: la distinción entre arras confirmatorias, penales y penitenciales no figura en el Código, la ha construido la jurisprudencia, y por ello es imprescindible pactar expresamente en el contrato de que clase son y que ocurre si una parte se retira. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - COMPRAVENTA: "A su caso corresponde un contrato privado de compraventa de vivienda, regido por los artículos 1.445 y siguientes del Código Civil. Debe saber que este documento obliga a ambas partes, pero no transmite la propiedad frente a terceros ni permite inscribir la vivienda a su nombre en el Registro de la Propiedad: para ello es necesaria la escritura pública notarial, conforme al artículo 1.280.1.º del Código Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - REQUERIMIENTO: "A su caso corresponde un requerimiento extrajudicial de cumplimiento, con fundamento en el artículo 1.124 del Código Civil, que le permite optar entre exigir el cumplimiento o resolver el contrato, con resarcimiento de daños e intereses en ambos casos. Tratándose de venta de bien inmueble, el artículo 1.504 del mismo Código permite al comprador pagar el precio aun después de vencido el plazo mientras no haya sido requerido judicialmente o por acta notarial. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - En las hojas ARRAS y COMPRAVENTA, si el inmueble está arrendado como vivienda, añadir: "Al estar el inmueble arrendado, resulta además de aplicación el derecho de tanteo y retracto del arrendatario, previsto en el artículo 25 de la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003"
   - En la hoja COMPRAVENTA, si la vivienda es de obra nueva ya recibida, añadir: "Al tratarse de obra nueva, resultan además de aplicación las garantías por vicios y defectos de la construcción del artículo 17 de la Ley 38/1999, de 5 de noviembre, de Ordenación de la Edificación, con plazos de diez, tres y un año desde la recepción de la obra. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1999-21567"

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** (menciónala por su denominación formal, sin mostrar rutas internas ni volcar su contenido). Si el enrutamiento asigno varios documentos, nómbralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la sección de assets.
4. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` (ciclo de creación del documento base):
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

### Secciones — HOJA ARRAS

1. **Parte vendedora** *[dato objetivo — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04]*. Anuncio fijo: "Comenzamos por la identificación de la parte vendedora." Ejecute prioritariamente `search_clients`. Use los datos de la ficha si hay coincidencia única; si hay varias, desambigüe con `restricted_human_in_the_loop_request` (incluyendo siempre al final la opción obligatoria `{"id": "ninguna", "label": "Ninguna de las personas identificadas (otra persona)"}`); solo si no existe o faltan campos (ej. estado civil y régimen o título de adquisición), solicite los campos pendientes mediante `slot_filling_request`. Si es cliente nuevo, aplique `REG-CLI-03`. Conforme a `REG-CLI-04`, vuelque inmediatamente los datos al documento mediante `edit_file` (o en `create_file` si ya obraban en el sistema), sustituyendo exhaustivamente los nombres en todas sus apariciones (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones), informe en el chat de los datos incorporados y continúe de inmediato sin pedir confirmación previa en chat ("¿Confirmamos estos datos?").
2. **Parte compradora** *[dato objetivo — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04]*. Anuncio fijo: "Pasamos a la identificación de la parte compradora." Ejecute prioritariamente `search_clients`. Si hay 1 coincidencia, use los datos directamente; si hay varias, desambigüe con `restricted_human_in_the_loop_request` (incluyendo siempre al final la opción obligatoria `{"id": "ninguna", "label": "Ninguna de las personas identificadas (otra persona)"}`); solo para datos no cubiertos (ej. régimen matrimonial), use `slot_filling_request`. Si es cliente nuevo, aplique `REG-CLI-03`. Conforme a `REG-CLI-04`, vuelque inmediatamente los datos al documento mediante `edit_file` (o en `create_file`), sustituyendo exhaustivamente los nombres en todas sus apariciones (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones), informe en el chat de los datos incorporados y continúe de inmediato sin pedir confirmación previa en chat.
3. **El inmueble** *[dato objetivo con validación — `slot_filling_request` con confirmación en el chat]*. Anuncio fijo: "Describimos ahora el inmueble objeto de la operación." Solicita en bloque mediante `slot_filling_request`: a) dirección completa, municipio, provincia y código postal; b) superficie construida y descripción; c) referencia catastral; d) datos registrales (Registro, tomo, libro, folio y finca); e) anexos que se incluyen, si los hay. Los datos que el cliente no tenga quedan como placeholder (`{{DATO_FALTANTE}}`) y se advierte de que deben completarse antes de firmar: **no se inventan**. Muestra vista previa en el chat, pide confirmación y aplica el `edit_file`.
4. **Precio y forma de pago** *[negociación]*. Anuncio fijo: "Pasamos a determinar el precio y la forma de pago." Explica antes de pedir cifras: el precio debe expresarse en cifra y en letra, prevaleciendo la letra en caso de discordancia, y la forma de pago debe desglosarse por partidas, fechas y medios de pago, porque el otorgamiento de la escritura exigirá acreditar cada medio de pago. Pide después, en turnos separados: a) precio total; b) importe que quedará pendiente para el otorgamiento; c) medio de pago de cada partida y cuenta de destino.
5. **Importe de las arras** *[negociación]*. Anuncio fijo: "Concretamos el importe de la señal." Explica que no hay importe legal y que en la práctica se mueve entre el 5 % y el 10 % del precio; que un importe bajo apenas disuade de retirarse y uno alto expone al comprador a una pérdida grave. Pide el importe y el medio de entrega.
6. **Clase de arras y su consecuencia** *[negociación — punto crítico de la skill]*. Anuncio fijo: "Determinamos ahora la clase de arras y sus consecuencias, que es el punto más relevante de este contrato." Antes de pedir la decisión, explica los tres puntos siguientes, siempre en este orden:
   - Que el artículo 1.454 del Código Civil solo dice que, si median arras, el contrato podrá rescindirse allanándose el comprador a perderlas o el vendedor a devolverlas duplicadas, y que **la clasificación en arras confirmatorias, penales y penitenciales no está en el Código: la ha construido la jurisprudencia**.
   - Que ocurre con cada clase si una parte se echa atrás: las **confirmatorias** son señal y anticipo del precio y **no permiten desistir** (quien se retira incumple, y la otra parte puede exigir el cumplimiento o resolver con daños e intereses, artículo 1.124); las **penales** añaden una pena convencional, tampoco permiten desistir, y **la pena sustituye a la indemnización de daños salvo que se pacte lo contrario** (artículo 1.152); las **penitenciales** son el precio de la facultad de desistir, y son las únicas que encajan en el artículo 1.454: quien desiste pierde las arras, o las devuelve duplicadas, y el contrato queda sin efecto sin más consecuencias.
   - Que **el silencio juega en contra de quien quiere desistir**: si el contrato no dice de que clase son, la jurisprudencia tiende a presumir el carácter confirmatorio, el más restrictivo para retirarse.
   Orienta según V2: al **comprador** que quiere una salida por si no le conceden la hipoteca, adviértele de que las arras penitenciales le hacen perder la señal y que para recuperarla necesita además la condición suspensiva de financiación; al **vendedor** que quiere asegurar la venta, adviértele de que las penitenciales dejan al comprador retirarse perdiendo solo la señal. Pide después la decisión y confirma que entiende la consecuencia antes de escribirla. **Esta sección no puede cerrarse sin la clase pactada.**
7. **Plazo y notaría para la escritura** *[negociación]*. Anuncio fijo: "Fijamos el plazo para el otorgamiento de la escritura pública." Explica que sin fecha límite la obligación es difícil de exigir, y que conviene pactar quién designa notario y con cuanta antelación debe convocarse a la otra parte. Pide: a) fecha límite; b) notario o parte que lo designa; c) días de antelación de la convocatoria.
8. **Cargas del inmueble** *[negociación]*. Anuncio fijo: "Abordamos la situación de cargas del inmueble." Explica que la hipoteca sigue a la finca y solo se extingue con su cancelación registral; que las deudas de comunidad y el IBI afectan al propio inmueble frente al nuevo adquirente; y que las cargas o servidumbres no aparentes no mencionadas dan al comprador, conforme al artículo 1.483 del Código Civil, un plazo de solo un año desde el otorgamiento de la escritura para pedir la rescisión o la indemnización. Recomienda nota simple registral, certificado de la comunidad con el visto bueno del presidente y último recibo del IBI. Pide: a) si dispone de nota simple y que refleja; b) si hay hipoteca pendiente, su entidad e importe, y si se cancela con retención del precio o se pretende subrogación, advirtiendo de que la subrogación exige el consentimiento de la entidad y no puede darse por hecha.
9. **Estado posesorio y arrendatarios** *[negociación]*. Anuncio fijo: "Determinamos el estado posesorio del inmueble." El valor de V4 ya está resuelto y la parada bloqueante de la validación de presupuestos ya se ha aplicado. Si está arrendado: recoge la fecha del contrato de arrendamiento, su fecha de vencimiento, el nombre del arrendatario, la fecha y el medio de la notificación, y activa el bloque que corresponda (notificación practicada, renuncia comprobada, o condición de eficacia). Si está libre: pide la manifestación del vendedor y, si hay ocupantes que deban salir, la fecha de desalojo y la consecuencia del retraso.
   **El valor de V4 gobierna además otras dos cláusulas del asset, y hay que resolverlas en coherencia con esta:** la cláusula quinta (entrega de llaves si está libre, entrega de la documentación del arrendamiento si está arrendado) y la cláusula sexta (obligación de entregar libre de arrendatarios y ocupantes solo si está libre; si está arrendado, el inmueble se transmite con el arrendamiento subsistente y el comprador se subroga conforme al artículo 14 de la Ley 29/1994). Cada una ofrece dos bloques alternativos: inserta uno solo y el mismo en las tres. **Un contrato que en la cláusula sexta obligue a entregar libre de arrendatarios y en la séptima describa un arrendamiento vigente es un contrato contradictorio: no puede cerrarse así.**
10. **Financiación** *[negociación — condicional, solo si V3 = si]*. Anuncio fijo: "Valoramos como protegerle si la financiación no llega a concederse." Explica que sin esta cláusula la denegación del préstamo convierte al comprador en incumplidor, con pérdida de las arras o algo peor si son confirmatorias o penales, y que la condición suspensiva convierte la denegación en un supuesto previsto y no culpable. Pide, en turnos separados, los cuatro elementos: a) importe mínimo de financiación y fecha límite; b) destino de las arras si no se concede, ofreciendo por defecto la devolución íntegra; c) como se acredita la denegación (denegación escrita, número mínimo de entidades y plazo), advirtiendo de que sin acreditación documental el comprador que se retira alegando denegación queda en una posición muy débil; d) que ocurre si el plazo vence sin respuesta del banco. Orienta según V2: al comprador, plazo amplio y devolución íntegra; al vendedor, plazo corto y exigencia de acreditar diligencia. Si V3 = no, activa el bloque de que no hay condición suspensiva y **no formules las preguntas de esta sección**.
11. **Impuestos y gastos** *[negociación]*. Anuncio fijo: "Pasamos al reparto de impuestos y gastos." Explica el reparto legal: el ITP a cargo del comprador (artículo 8.a) del Real Decreto Legislativo 1/1993, "cualesquiera que sean las estipulaciones establecidas por las partes en contrario"); la plusvalía municipal a cargo del vendedor (artículo 106.1.b) del Real Decreto Legislativo 2/2004); los gastos de otorgamiento de la escritura a cargo del vendedor y los de la primera copia e inscripción a cargo del comprador (artículo 1.455 del Código Civil); y la cancelación de cargas a cargo del vendedor. Advierte de que **el pacto en contra vincula a las partes pero no a la Administración**, que seguirá exigiendo cada impuesto a su sujeto pasivo legal (artículo 17.5 de la Ley 58/2003), de modo que el pacto crea una acción de reembolso, no un cambio de contribuyente. No calcules cuotas: el tipo del ITP lo fija cada Comunidad Autónoma y la plusvalía depende de la ordenanza municipal. Pregunta si se mantiene el reparto legal o se pacta otro distinto y, en este último caso, activa el bloque con la advertencia incorporada al documento.
12. **Notificaciones** *[dato objetivo]*. Anuncio fijo: "Cerramos las vías de comunicación entre las partes." Pide los correos electrónicos de cada parte y recuerda que las comunicaciones con efecto resolutorio o de desistimiento deben practicarse por medio que acredite contenido y recepción.
13. **Lugar, fecha y ejemplares** *[dato objetivo]*. Anuncio fijo: "Cerramos con el lugar, la fecha y el número de ejemplares." Municipio y fecha de firma (fecha del día salvo indicación en contrario) y número de ejemplares.

### Secciones — HOJA COMPRAVENTA

1. **Parte vendedora** *[dato objetivo — volcado directo a disco per REG-CLI-04]*. Igual que en la HOJA ARRAS, añadiendo el sub-apartado del consentimiento del cónyuge si el inmueble es vivienda habitual del matrimonio.
2. **Parte compradora** *[dato objetivo — volcado directo a disco per REG-CLI-04]*. Igual que en la HOJA ARRAS, añadiendo la proporción de adquisición si compran varias personas.
3. **El inmueble** *[dato objetivo con validación]*. Igual que en la HOJA ARRAS, añadiendo superficie útil, linderos y, si procede, el inventario de mobiliario del Anexo I. Si la venta se hace con expresión de cabida y precio por unidad de medida, adviértelo y aplica el régimen del artículo 1.469 del Código Civil (rebaja proporcional o rescisión si la diferencia excede de la décima parte); si se vende como cuerpo cierto, déjalo escrito expresamente.
4. **Precio** *[negociación]*. Anuncio fijo: "Pasamos a determinar el precio de la compraventa." Igual explicación que en la HOJA ARRAS sobre cifra y letra. Pide el precio total y recoge la manifestación de que es el realmente convenido.
5. **Forma de pago** *[negociación]*. Anuncio fijo: "Concretamos la forma de pago." Pide, en turnos separados: a) arras o cantidades ya entregadas, con fecha y medio; b) importe que se entrega en el acto de la firma; c) importe pendiente para el otorgamiento de la escritura; d) medio de pago de cada partida y cuenta de destino. Recuerda la obligación de conservar los justificantes.
6. **Cargas, gravámenes y deudas** *[negociación]*. Igual que la sección 8 de la HOJA ARRAS, añadiendo la obligación del vendedor de aportar la certificación de la comunidad y el último recibo del IBI antes del otorgamiento, y la posibilidad de que el comprador acepte expresamente una carga que subsista.
7. **Estado posesorio y derecho de adquisición preferente** *[negociación]*. Igual que la sección 9 de la HOJA ARRAS. Si está arrendado y ya se notificó, añade la obligación del **comprador** de notificar después al arrendatario las condiciones esenciales en que se efectuó la compraventa, con copia de la escritura, a los efectos del cómputo del plazo de retracto del artículo 25.3.
8. **Otorgamiento de la escritura pública** *[negociación]*. Anuncio fijo: "Fijamos el otorgamiento de la escritura pública." Igual que la sección 7 de la HOJA ARRAS, añadiendo que cualquiera de las partes puede compeler a la otra al otorgamiento desde la perfección del contrato (artículo 1.279 del Código Civil).
9. **Entrega de la posesión** *[negociación]*. Anuncio fijo: "Determinamos cuando se entrega la posesión de la vivienda." Explica que el otorgamiento de la escritura pública equivale a la entrega salvo pacto en contrario (artículo 1.462 del Código Civil), y que los frutos y gastos ordinarios se imputan al comprador desde la entrega (artículo 1.468). Pregunta si la posesión se entrega en el otorgamiento o antes; si se entrega antes, advierte de que la propiedad no se transmite hasta la escritura y activa el bloque de ocupación en precario.
10. **Financiación** *[negociación — condicional, solo si V3 = si]*. Igual que la sección 10 de la HOJA ARRAS.
11. **Impuestos y gastos** *[negociación]*. Igual que la sección 11 de la HOJA ARRAS. Si la transmisión es primera entrega de edificación, activa el bloque de IVA y AJD en lugar del ITP.
12. **Estado de la vivienda y saneamiento** *[negociación]*. Anuncio fijo: "Abordamos el estado de la vivienda y la responsabilidad por vicios ocultos." Explica: el vendedor responde de la posesión legal y pacifica y de los vicios o defectos ocultos (artículo 1.474), **aunque los ignorase** (artículo 1.485), pero **no** de los defectos manifiestos o que estuvieren a la vista, ni de los que no lo estuvieran si el comprador es un perito que por su oficio debía conocerlos (artículo 1.484); ante el vicio oculto el comprador puede desistir con abono de gastos o pedir rebaja proporcional del precio, y además daños y perjuicios si el vendedor lo conocía y no lo manifesto (artículo 1.486); y las acciones de saneamiento **se extinguen a los seis meses desde la entrega** (artículo 1.490). Orienta según V2: al **comprador**, recomiéndale hacer constar por escrito los defectos que ya conoce y no aceptar una exoneración genérica de saneamiento; al **vendedor**, recomiéndale declarar los defectos que conoce, porque ocultarlos sabiéndolos abre la puerta a la indemnización de daños del artículo 1.486. Pide la relación de defectos que el vendedor declara y pregunta si se pacta alguna modulación de la responsabilidad por evicción (artículo 1.475, que permite aumentarla, disminuirla o suprimirla).
13. **Obra nueva** *[negociación — condicional, solo si la vivienda es de obra nueva ya recibida]*. Anuncio fijo: "Concretamos las garantías aplicables por tratarse de obra nueva." Explica los plazos del artículo 17 de la Ley 38/1999 contados desde la recepción de la obra sin reservas o desde la subsanación de estas: diez años por daños en elementos estructurales que comprometan la resistencia y la estabilidad, tres años por vicios que incumplan los requisitos de habitabilidad, y un año por vicios de ejecución en elementos de terminación o acabado; y que el promotor responde solidariamente frente a los adquirentes. Pide la fecha de recepción de la obra y confirma que se entregan copia de las pólizas del artículo 19 y la licencia de primera ocupación.
14. **Documentación que aportará el vendedor** *[dato objetivo]*. Anuncio fijo: "Relacionamos la documentación que el vendedor deberá aportar." Repasa la lista del asset y pregunta si hay documentación adicional propia del caso.
15. **Incumplimiento y remedios** *[negociación]*. Anuncio fijo: "Determinamos las consecuencias del incumplimiento." Explica el artículo 1.124 del Código Civil (opción entre cumplimiento y resolución, con daños e intereses en ambos casos) y, con especial claridad, el artículo 1.504: en la venta de inmuebles, **aun con pacto de resolución de pleno derecho por impago, el comprador puede pagar mientras no haya sido requerido judicialmente o por acta notarial**, y hecho el requerimiento el Juez no podrá concederle nuevo término. Orienta según V2: al **vendedor**, adviértele de que un simple burofax no cierra el plazo de pago del comprador; al **comprador**, infórmale de que dispone de esa ventana y de la facultad de suspender el pago si es perturbado en la posesión o teme fundadamente una acción reivindicatoria o hipotecaria (artículo 1.502). Pregunta si se pacta cláusula penal y, si se pacta, **su importe y si sustituye o se acumula** a la indemnización de daños, advirtiendo de que a falta de pacto **sustituye** (artículo 1.152).
16. **Notificaciones** *[dato objetivo]*. Igual que la sección 12 de la HOJA ARRAS.
17. **Lugar, fecha y ejemplares** *[dato objetivo]*. Igual que la sección 13 de la HOJA ARRAS.

### Secciones — HOJA REQUERIMIENTO

1. **Parte requirente** *[dato objetivo — `slot_filling_request` con confirmación en el chat]*. Anuncio fijo: "Comenzamos por la identificación de quien practica el requerimiento." Solicita en bloque mediante `slot_filling_request`: a) nombre o razón social; b) NIF o CIF; c) domicilio; d) vía de contacto para el cumplimiento voluntario. Su condición en el contrato (comprador o vendedor) ya está resuelta por V2: no la preguntes de nuevo. Vista previa en el chat, confirmación explícita y `edit_file`.
2. **Parte requerida** *[dato objetivo — `slot_filling_request` con confirmación en el chat]*. Anuncio fijo: "Pasamos a la identificación del destinatario del requerimiento." Solicita en bloque mediante `slot_filling_request`: a) nombre o razón social; b) NIF o CIF; c) domicilio al que se dirigirá la comunicación. Vista previa en el chat, confirmación explícita y `edit_file`.
3. **El contrato y el inmueble** *[dato objetivo con validación — `slot_filling_request` con confirmación en el chat]*. Anuncio fijo: "Describimos el contrato incumplido y el inmueble al que se refiere." Solicita en bloque mediante `slot_filling_request`: a) tipo y fecha del contrato firmado; b) dirección, referencia catastral y datos registrales del inmueble; c) precio total pactado. Vista previa en el chat, confirmación y `edit_file`.
4. **La obligación incumplida** *[dato objetivo con validación]*. Anuncio fijo: "Concretamos la obligación incumplida y su vencimiento." Recoge: a) que obligación se pacto y con que vencimiento; b) en que consiste el incumplimiento; c) importe pendiente, si es dinerario; d) convocatorias o requerimientos previos, con su fecha y medio. Aplica aquí las validaciones de prescripción (artículo 1.964.2) y, si lo reclamado son vicios ocultos, del plazo de seis meses del artículo 1.490. Muestra vista previa en el chat, pide confirmación y aplica el `edit_file`.
5. **Vía del requerimiento** *[negociación — crítica si el requirente es el vendedor]*. Anuncio fijo: "Determinamos por qué vía debe practicarse el requerimiento." Explica la diferencia con precisión: un **burofax** con acuse de recibo y certificación de texto constituye en mora, fija la fecha e interrumpe la prescripción (artículo 1.973), y es suficiente si lo que se busca es exigir el cumplimiento; un **acta notarial** (o el requerimiento judicial) es lo que exige el artículo 1.504 del Código Civil para **cerrar la facultad del comprador de pagar tardíamente** en la venta de inmuebles. Si V2 = vendedor y el incumplimiento es el impago del precio, recomienda expresamente el acta notarial y advierte de que con burofax el comprador podrá pagar después del plazo y evitar la resolución. Pregunta qué vía se va a emplear y activa el bloque correspondiente del asset.
6. **Conducta exigida y plazo** *[negociación]*. Anuncio fijo: "Fijamos que se exige y en que plazo." Explica que el requerimiento debe pedir una conducta concreta, con plazo y forma de cumplimiento, y que un requerimiento genérico pierde eficacia. Pide, en turnos separados: a) conducta exigida (pago del precio, otorgamiento de la escritura, entrega de la posesión, cancelación de una carga no declarada); b) plazo de cumplimiento; c) si es pago, medio y cuenta; si es otorgamiento, notario, dirección, día y hora, y documentación a aportar.
7. **Opción del artículo 1.124** *[negociación]*. Anuncio fijo: "Determinamos que acción se anuncia si el requerimiento no se atiende." Explica que el artículo 1.124 permite optar entre exigir el cumplimiento y resolver el contrato, con resarcimiento de daños e intereses en ambos casos, y que puede pedirse la resolución aun después de haber optado por el cumplimiento cuando este resulte imposible. Orienta según V2 y según el interés real del cliente: quien quiere la vivienda pide el cumplimiento; quien quiere desvincularse pide la resolución. Si V2 = comprador y la obligación incumplida es el otorgamiento de la escritura, informa de que puede compeler al vendedor conforme al artículo 1.279. Pide la opción y confirma que entiende su consecuencia.
8. **Cláusula penal o arras pactadas** *[negociación — condicional]*. Anuncio fijo: "Valoramos si procede reclamar la pena o las arras pactadas." Solo si el contrato incumplido prevé arras con consecuencia pactada o cláusula penal. Explica que a falta de pacto expreso la pena **sustituye** a la indemnización de daños e intereses (artículo 1.152), de modo que reclamar la pena puede cerrar la vía de reclamar el daño real si este es mayor. Pide el importe y la cláusula que lo pacta.
9. **Suspensión del pago** *[negociación — condicional, solo si V2 = comprador y hay perturbación o riesgo de acción reivindicatoria o hipotecaria]*. Anuncio fijo: "Valoramos si procede suspender el pago del precio pendiente." Explica el artículo 1.502: el comprador perturbado en la posesión o dominio, o con fundado temor de serlo por acción reivindicatoria o hipotecaria, puede suspender el pago hasta que cese la perturbación o el peligro, salvo que el vendedor afiance la devolución o se haya estipulado lo contrario. Pide la descripción de la perturbación o del riesgo.
10. **Lugar y fecha** *[dato objetivo]*. Anuncio fijo: "Cerramos con el lugar y la fecha del requerimiento." Municipio y fecha (fecha del día salvo indicación en contrario). Recuerda que la fecha es relevante a efectos de mora y de interrupción de la prescripción.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: una materia por cláusula, toda obligación con sujeto, verbo, plazo y consecuencia, precio y arras en cifra y en letra, inmueble identificado con referencia catastral y datos registrales, voz activa, sin latinismos, y cero cláusulas que las partes no hayan decidido.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre el Código Civil, la LAU, la LOE y las normas fiscales en el BOE antes de redactar (Fase 2). Sin verificación, no proceder. Recordar que la versión vigente es la ÚLTIMA `<version>` de cada bloque de la API.
2. **El contrato privado no transmite la propiedad frente a terceros ni permite inscribir en el Registro de la Propiedad: hace falta escritura pública notarial (Art. 1280.1.º CC).** Advertirlo siempre, en el chat y en el propio documento. Nunca dar a entender al cliente que con el contrato privado la vivienda ya es suya a todos los efectos, ni que puede obtener hipoteca sobre ella (la hipoteca solo queda válidamente constituida con su inscripción, Art. 1875 CC).
3. **La clasificación de las arras en confirmatorias, penales y penitenciales es jurisprudencial, no legal.** El Art. 1454 CC solo contempla el desistimiento. Prohibido presentar los tres tipos como categorías del Código Civil o citar el Art. 1454 como fundamento de las confirmatorias o penales. El documento debe pactar **expresamente** la clase y su consecuencia: del silencio la jurisprudencia tiende a presumir el carácter confirmatorio, que no permite desistir.
4. **Nunca redactar una compraventa sin comprobar las cargas del inmueble**, ni escribir que está libre de cargas sobre la sola afirmación verbal del vendedor. Recomendar siempre nota simple o certificación registral, certificado de la comunidad de propietarios y último recibo del IBI.
5. **Nunca dar por buena una renuncia del arrendatario al retracto sin verificar los requisitos del Art. 25 de la Ley 29/1994**: renuncia expresa en el contrato de arrendamiento (Art. 25.8) y comunicación de la intención de vender con antelación mínima de treinta días a la formalización de la compraventa, que la renuncia no elimina. Si el inmueble está arrendado y no se ha notificado la venta, advertir del retracto y de la no inscribibilidad de la escritura (Art. 25.5) **antes** de continuar con el documento.
6. En **obra nueva**, activar las garantías de la Ley 38/1999 (Art. 17: diez, tres y un año desde la recepción de la obra) y verificar la entrega de las pólizas del Art. 19. Si la venta es **sobre plano con entregas a cuenta**, detener: exige aval solidario de entidad de crédito o seguro de caución individualizado y cuenta especial separada (disposición adicional primera de la Ley 38/1999). No redactar ese contrato.
7. El **pacto fiscal en contra del reparto legal no vincula a la Administración** (Art. 17.5 LGT): el ITP se exige al comprador (Art. 8.a) RDLeg 1/1993) y la plusvalía municipal al vendedor (Art. 106.1.b) RDLeg 2/2004), y el pacto solo genera una acción de reembolso entre las partes. Advertirlo siempre que se pacte otro reparto. **No calcular cuotas**: el tipo del ITP es autonómico y la plusvalía depende de la ordenanza municipal.
8. En el **requerimiento por impago del precio de un inmueble**, si el objetivo es resolver, debe practicarse **judicialmente o por acta notarial** (Art. 1504 CC). Advertir siempre de que un burofax no cierra la facultad del comprador de pagar tardíamente.
9. Las **acciones de saneamiento por vicios ocultos se extinguen a los seis meses desde la entrega** (Art. 1490 CC) y las derivadas de cargas o servidumbres no aparentes al año desde el otorgamiento de la escritura (Art. 1483 CC). Comprobar el plazo antes de anunciar una reclamación; no dar falsas expectativas.
10. Nunca redactar cláusulas que exoneren al vendedor del saneamiento de forma genérica cuando conoce los vicios: el Art. 1485 solo excluye la responsabilidad si se estipulo lo contrario **y** el vendedor los ignoraba, y el Art. 1486 impone indemnización de daños al vendedor que los conocía y no los manifesto.
11. Si el inmueble tiene **varios cotitulares**, la firma de uno solo no vincula a los demás. Si es la **vivienda habitual del matrimonio**, la disposición requiere el consentimiento del otro cónyuge. Advertirlo y recoger las comparecencias necesarias.
12. Nunca inventar datos, cuantías, fechas, referencias catastrales, datos registrales, números de protocolo ni jurisprudencia. **Esta skill no cita sentencias**: si el usuario necesita apoyo jurisprudencial concreto, se escala. Los campos no proporcionados quedan como `{{DATO}}` con su nombre propio.
13. Los assets se construyen sobre el **Código Civil común**. Si el caso se rige por derecho civil foral o especial —Cataluña regula la compraventa en el Llibre sise del Codi civil de Catalunya, y hay derecho propio en Navarra, Aragon, Baleares, Galicia y País Vasco—, detener y escalar.
14. No existe modelo oficial normalizado de contrato de compraventa ni de arras (verificado: ni Consejo General del Notariado, ni Colegio de Registradores, ni CGPJ). No afirmar al usuario que el documento reproduce un modelo oficial.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- **No sustituye la escritura pública ante notario ni la inscripción en el Registro de la Propiedad.** El deliverable es un contrato privado o un requerimiento: la transmisión de la propiedad frente a terceros y la inscripción exigen escritura pública notarial.
- **No hace due diligence de titularidad ni valoración del inmueble.** No comprueba en el Registro quién es el titular, no verifica cargas por su cuenta, no revisa la situación urbanística ni tasa el inmueble. Recomienda esas comprobaciones; no las realiza.
- No usar para la **compraventa de local comercial, nave, solar, finca rustica o plaza de garaje transmitida de forma independiente**: los assets están construidos para vivienda. Escalar.
- No usar para la **compraventa de obra nueva sobre plano con entregas a cuenta**: exige aval solidario o seguro de caución de las cantidades anticipadas y cuenta especial separada (disposición adicional primera de la Ley 38/1999). Escalar.
- No usar para **herencias, legados ni donaciones de inmuebles**: derivar a `herencia`.
- No usar para permuta, dación en pago, aportación a sociedad ni adjudicación en liquidación de gananciales: escalar.
- No usar para redactar la **escritura pública** de compraventa ni el préstamo hipotecario: son documentos notariales.
- No usar para desalojar a un ocupante o arrendatario del inmueble: derivar a `desahucio`.
- No usar para reclamar judicialmente el precio impagado una vez agotada la vía extrajudicial: derivar a `reclamacion-cantidad` según cuantía, o a `juicio-ordinario` si lo que se pide es la resolución o el cumplimiento del contrato.
- No usar para ejecutar una escritura pública de compraventa ya otorgada e impagada: derivar a `ejecucion-titulos`.
- No usar si el usuario pide **opinión jurídica sobre la conveniencia de la operación o sobre su estrategia**: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
