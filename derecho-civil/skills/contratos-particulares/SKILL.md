---
name: contratos-particulares
title: Contratos entre particulares
i18n:
  en:
    name: private-contracts
    title: Contracts between private individuals
    description: >
      Generates the right contract for an asset transaction between private individuals under
      the **Civil Code**, which governs obligations and contracts, verified in the BOE: money
      loan between individuals (simple loan, Arts. 1740 and 1753 to 1757 CC, with usury control
      under the Law of 23 July 1908), acknowledgement of debt and payment commitment (Arts.
      1255, 1274 to 1277 and 1973 CC), gratuitous loan for use (commodatum, Arts. 1740 to 1752
      CC) and sale of movable property (Arts. 1445 et seq. CC). It explains and documents the
      choice between a private document and a public deed (Arts. 1278 to 1280 CC and Art.
      517.2.4 LEC). Do not use for loans from financial institutions or consumer credit,
      mortgage loans, real estate sales, claiming a debt already unpaid, or commercial contracts
      between companies.
description: >
  Genera el contrato adecuado para una operación patrimonial entre particulares, conforme al **Código Civil**, que regula las obligaciones y los contratos entre particulares,
  verificado en el BOE: contrato de préstamo de dinero entre particulares (simple préstamo o mutuo, Arts.
  1740 y 1753 a 1757 CC, con control de usura conforme a la Ley de 23 de julio de 1908), reconocimiento de
  deuda y compromiso de pago (Arts. 1255, 1274 a 1277 y 1973 CC), contrato de comodato o préstamo de uso
  gratuito de una cosa (Arts. 1740 a 1752 CC) y contrato de compraventa de un bien mueble (Arts. 1445 y
  siguientes CC). Explica y documenta la decisión entre documento privado y escritura pública (Arts. 1278 a
  1280 CC y Art. 517.2.4.º LEC). NO usar para préstamos con entidad financiera ni crédito al consumo, para
  préstamos hipotecarios, para la compraventa de inmuebles, para reclamar una deuda ya impagada, ni para
  contratos mercantiles o entre empresas.
when_to_use: |
  - El usuario quiere prestar dinero a un familiar, amigo o conocido y necesita dejarlo por escrito.
  - El usuario quiere documentar una deuda ya existente y fijar un calendario de pago.
  - El usuario quiere ceder gratuitamente el uso de una cosa (local, vehículo, maquinaria) sin cobrar nada
    por ella y con obligación de devolverla.
  - El usuario quiere vender o comprar un bien mueble concreto (vehículo, maquinaria, mobiliario, obra de
    arte) a otro particular.
  - El usuario pregunta si le conviene firmar un contrato privado o ir al notario, y necesita el documento.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_contrato: préstamo de dinero / reconocimiento de deuda / comodato / compraventa de bien mueble
  - datos_parte_acreedora: nombre o razón social, documento de identidad, domicilio, teléfono, email
  - datos_parte_deudora: nombre o razón social, documento de identidad, domicilio, teléfono, email
  - objeto: importe del préstamo o de la deuda, descripción e identificación del bien, o precio de venta
  - causa: origen de la deuda en el reconocimiento, finalidad del préstamo, relación entre las partes en el comodato
  - interes: si se pacta interés remuneratorio y a que tipo; si se pacta interés de demora distinto del legal
  - plazo: pago o devolución en un solo vencimiento, o calendario de cuotas con fechas e importes
  - garantia: fianza simple, fianza solidaria, prenda, reserva de dominio, o ninguna
  - datos_fiador: nombre, documento de identidad, domicilio, teléfono, email
  - forma: documento privado, documento privado con compromiso de elevación, o escritura pública
outputs:
  - contrato_prestamo_particulares: contrato de préstamo entre particulares en markdown, DRAFT
  - reconocimiento_deuda: reconocimiento de deuda y compromiso de pago en markdown, DRAFT
  - contrato_comodato: contrato de comodato o préstamo de uso en markdown, DRAFT
  - contrato_compraventa_mueble: contrato de compraventa de bien mueble en markdown, DRAFT
references:
  - references/estilo-redaccion-contratos.md
  - references/forma-documento-privado-o-publico.md
  - references/fuentes-plantillas-validadas.md
  - references/usura-y-limites-del-interes.md
assets:
  - assets/template-contrato-comodato.md
  - assets/template-contrato-compraventa-mueble.md
  - assets/template-contrato-prestamo-particulares.md
  - assets/template-reconocimiento-deuda.md
---

# Contratos Patrimoniales entre Particulares

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
      "id": "tipo_contrato",
      "rationale": "Resolver V1: cada figura tiene su propio asset y su propio régimen en el Código Civil, y el comodato exige gratuidad.",
      "question": "¿Qué quiere documentar?",
      "options": [
        {"id": "prestamo_dinero", "label": "Un préstamo de dinero entre particulares"},
        {"id": "comodato", "label": "La cesión gratuita del uso de una cosa, sin contraprestación alguna"},
        {"id": "reconocimiento_deuda", "label": "El reconocimiento de una deuda ya existente y su forma de pago"},
        {"id": "compraventa_mueble", "label": "La compraventa de un bien mueble"}
      ]
    },
    {
      "id": "garantia",
      "rationale": "Resolver V3: la garantía determina si hay que identificar fiador y si se incorporan las cláusulas de afianzamiento o de reserva de dominio.",
      "question": "¿Se pacta alguna garantía del cumplimiento?",
      "options": [
        {"id": "ninguna", "label": "Ninguna"},
        {"id": "fianza_solidaria", "label": "Fianza de un tercero, con renuncia a los beneficios de excusión y división"},
        {"id": "fianza_simple", "label": "Fianza de un tercero, sin renuncia a esos beneficios"},
        {"id": "reserva_dominio_o_prenda", "label": "Reserva de dominio o prenda sobre el bien"}
      ]
    },
    {
      "id": "forma",
      "rationale": "Resolver V4: determina si el documento incorpora el compromiso de elevación a escritura pública y la advertencia sobre la fuerza ejecutiva.",
      "question": "¿Qué forma va a darse al documento?",
      "options": [
        {"id": "privado", "label": "Documento privado entre las partes"},
        {"id": "privado_con_elevacion", "label": "Documento privado con compromiso de elevarlo a escritura pública"},
        {"id": "escritura_publica", "label": "Directamente escritura pública ante notario"}
      ]
    },
    {
      "id": "interes",
      "rationale": "Resolver V2: si se pacta interés, se activa el control de usura, que es bloqueante.",
      "question": "¿Se pacta interés remuneratorio?",
      "options": [
        {"id": "si", "label": "Sí, se pacta interés"},
        {"id": "no", "label": "No, sin interés"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — respuesta a `tipo_contrato`
- `V2` — respuesta a `interes`
- `V3` — respuesta a `garantia`
- `V4` — respuesta a `forma`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si V1 = prestamo_dinero → **HOJA PRÉSTAMO**: `assets/template-contrato-prestamo-particulares.md`.
- Si V1 = comodato → **HOJA COMODATO**: `assets/template-contrato-comodato.md`.
- Si V1 = reconocimiento_deuda → **HOJA RECONOCIMIENTO**: `assets/template-reconocimiento-deuda.md`.
- Si V1 = compraventa_mueble → **HOJA COMPRAVENTA**: `assets/template-contrato-compraventa-mueble.md`.
- Si V1 = comodato y **el cesionario debe pagar algo** por el uso de la cosa (renta, canon, cuota de gastos que exceda de los ordinarios, cualquier emolumento) → **NO es comodato**: el Art. 1741 CC dice que, si interviene emolumento, la convención deja de ser comodato. Si la cosa es un inmueble urbano, derivar a `arrendamiento`. Si es otra cosa, advertir de que se trata de un arrendamiento y ofrecer escalación. No crear documento de comodato.
- Si lo que el usuario pretende es **cobrar una deuda que ya está impagada** (no documentarla ni pactar su pago futuro) → derivar a `reclamacion-cantidad`. No crear documento.
- Si ya existe un **título ejecutivo** (sentencia, escritura pública, laudo) y lo que se quiere es ejecutarlo → derivar a `ejecucion-titulos`. No crear documento.
- Si el bien objeto de la operación es un **inmueble** y la operación es una compraventa → derivar a `compraventa-inmueble`. No crear documento.
- Si el préstamo se garantiza con **hipoteca sobre un inmueble** → **DETENER**: puede entrar en el ámbito de la Ley 5/2019 reguladora de los contratos de crédito inmobiliario, con requisitos de transparencia y acta notarial previa que exceden el alcance de esta skill. Advertir y escalar.
- Si **una de las partes es un consumidor y la otra actúa como empresario o profesional** → **DETENER**: no es un contrato entre particulares. Se aplica la normativa de protección de consumidores (y, si es crédito, la de crédito al consumo), con controles de transparencia y abusividad propios. Advertir y escalar o derivar a `reclamacion-clausulas-abusivas` si lo que se pretende es impugnar una cláusula ya firmada. No crear documento con estos assets.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **TODAS LAS HOJAS (Art. 1261 CC):** confirmar que concurren consentimiento, objeto cierto y causa. Si el objeto no está determinado ni es determinable sin nuevo acuerdo entre las partes (Art. 1273 CC), no redactar: pedir que se concrete.
- **TODAS LAS HOJAS (Art. 1255 CC):** ningún pacto puede ser contrario a las leyes, a la moral ni al orden público. Si el usuario pide un pacto que lo sea, rechazar la instrucción, explicar por qué es nulo y proponer una alternativa válida.
- **TODAS LAS HOJAS — condición de particulares:** verificar que ninguna de las partes actúa como empresario o profesional en el marco de esa actividad. Si lo hace, aplicar la regla de enrutamiento correspondiente y detener.
- **HOJA PRÉSTAMO (control de usura, BLOQUEANTE):** si V2 = sí, calcular el **coste real total** de la operación tal como el usuario la plantea: no solo el tipo nominal, sino todo lo que el prestatario devolverá por encima del principal, incluidas comisiones, gastos y penalizaciones. Contrastarlo con el orden de magnitud del interés legal del dinero vigente verificado en la Fase 2 y con el coste normal de operaciones equivalentes. Si la desproporción es manifiesta, **advertir expresamente ANTES de continuar**, con el texto del guardrail 3, explicando que la consecuencia es la **nulidad del préstamo** y no una rebaja del interés. No redactar la cláusula de interés hasta que el usuario confirme que, conocida la advertencia, mantiene o modifica su decisión. Si el usuario mantiene un interés que sigue siendo manifiestamente desproporcionado, ofrecer escalación y dejar constancia de la advertencia en las advertencias finales del documento.
- **HOJA PRÉSTAMO (Art. 1 párrafo 2.º de la Ley Azcárate, BLOQUEANTE):** si el importe que figuraría como prestado es superior al efectivamente entregado (por descuento del interés en el momento de la entrega o por cualquier otra vía), **DETENER**: ese contrato es nulo por el propio precepto. Explicarlo, no redactarlo y ofrecer escalación.
- **HOJA PRÉSTAMO (Art. 1755 CC):** si V2 = no, recordar al usuario que sin pacto expreso no se deberán intereses, y que esa es la regla legal por defecto, no un olvido del documento.
- **HOJA RECONOCIMIENTO (Arts. 1275 y 1276 CC y Art. 9 de la Ley Azcárate, BLOQUEANTE):** si la causa real de la deuda reconocida es un préstamo con interés desproporcionado, un importe superior al realmente debido, o cualquier causa ilícita, **DETENER**: el reconocimiento no puede usarse como envoltorio. Explicar que la Ley Azcárate se aplica a toda operación sustancialmente equivalente a un préstamo cualquiera que sea la forma del contrato, y que un contrato con causa ilícita no produce efecto alguno. No redactar y ofrecer escalación.
- **HOJA COMODATO (Arts. 1740 y 1741 CC):** confirmar que no hay contraprestación alguna a cargo del comodatario. La asunción de los gastos ordinarios de uso y conservación (Art. 1743 CC) no es contraprestación; el pago de una renta, canon o cuota por el uso, sí. Si la hay, aplicar la regla de enrutamiento y detener.
- **HOJA COMPRAVENTA (Art. 1445 CC):** confirmar que hay cosa determinada y precio cierto en dinero o signo que lo represente. Si la contraprestación no es dineraria, es una permuta y no una compraventa: advertir y escalar.
- **HOJA COMPRAVENTA:** si el bien es un vehículo, comprobar que se dispone de matrícula y número de bastidor. Si el bien es un inmueble, aplicar la regla de enrutamiento y detener.
- **PRESCRIPCIÓN (informativo, HOJA RECONOCIMIENTO):** las acciones personales sin plazo especial prescriben a los cinco años (Art. 1964.2 CC). Si la deuda que se reconoce es antigua, informar de que el reconocimiento **interrumpe** la prescripción (Art. 1973 CC) y reinicia el cómputo, lo que beneficia al acreedor y perjudica al deudor. Si quien pide el documento es el deudor, advertírselo expresamente antes de continuar.
- **DERECHO FORAL:** si la vecindad civil de alguna de las partes o el lugar de celebración apunta a un territorio con derecho civil propio (Cataluña, Navarra, Aragon, Baleares, Galicia, País Vasco), advertir de que puede desplazar reglas del Código Civil común y ofrecer escalación.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Código Civil (Arts. 1.740-1.757 para préstamo y comodato; Arts. 1.445-1.537 para compraventa mueble; Arts. 1.156 y 1.255 para reconocimiento de deuda), Ley de 23 de julio de 1908 (represión de la usura) y Real Decreto Legislativo 1/1993 (ITPAJD, operaciones exentas con obligación de declaración).
2. **Orientación Legal del Caso:**

**Informa el tipo de contrato y la fuente aplicable.** Textos fijos por hoja:
   - PRÉSTAMO: "A su caso corresponde un contrato de préstamo entre particulares, de los denominados simple préstamo o mutuo, regulado en los artículos 1.740 y 1.753 a 1.757 del Código Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - RECONOCIMIENTO: "A su caso corresponde un reconocimiento de deuda con compromiso de pago, que se ampara en la libertad de pacto del artículo 1.255 del Código Civil y se rige por sus normas generales sobre obligaciones y contratos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - COMODATO: "A su caso corresponde un contrato de comodato o préstamo de uso, regulado en los artículos 1.740 a 1.752 del Código Civil. Se trata de un contrato esencialmente gratuito. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - COMPRAVENTA: "A su caso corresponde un contrato de compraventa de bien mueble entre particulares, regulado en los artículos 1.445 y siguientes del Código Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - **Añadir en la HOJA PRÉSTAMO si V2 = sí:** "Le informo además de que el interés pactado está sujeto al control de la Ley de 23 de julio de 1908 sobre nulidad de los contratos de préstamos usurarios, que sigue vigente. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1908-5579"
   - **Añadir en la HOJA PRÉSTAMO si V2 = no:** "Conforme al artículo 1.755 del Código Civil, no se deberán intereses sino cuando expresamente se hubiesen pactado, de modo que su préstamo será gratuito."

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

### Secciones — HOJA PRÉSTAMO

1. **Parte prestamista** *(`[dato objetivo]` — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de quien entrega el dinero." Ejecute prioritariamente `search_clients`. Si la ficha cubre los datos, úselos directamente; si falta información, solicite solo los campos pendientes con `slot_filling_request`. Si es nuevo cliente, aplique `REG-CLI-03`. Vuelque directamente los datos al documento mediante `edit_file` (o en `create_file` si ya constaban), sustituyendo exhaustivamente los nombres en todas sus apariciones (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones), informe al usuario en chat y continúe sin confirmación previa en chat.
2. **Parte prestataria** *(`[dato objetivo]` — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de quien recibe el préstamo." Mismo procedimiento: volcado directo a disco per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones (título H1, comparecencia y firmas), informe en chat y continúe sin confirmación previa en chat.
3. **Importe y entrega del capital** *(`[dato objetivo]` — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Determinamos ahora el importe del préstamo y la forma en que se entrega el dinero." Solicita en bloque mediante `slot_filling_request`: a) importe (en cifra y letra); b) finalidad del préstamo; c) si el dinero ya se entregó o se entrega con la firma, y fecha; d) medio de entrega y, si es transferencia, IBAN de destino (recomienda transferencia bancaria frente a efectivo y explica por qué). Vista previa en chat, confirmación y `edit_file`.
4. **Intereses remuneratorios** *(`[negociacion]` — control de usura BLOQUEANTE)*. Anuncio fijo: "Abordamos ahora los intereses del préstamo." **Explica antes de preguntar nada:** (i) conforme al artículo 1.755 del Código Civil, sin pacto expreso no se deben intereses, de modo que el préstamo es gratuito por defecto; (ii) si decide pactarlos, la Ley de 23 de julio de 1908 sobre nulidad de los contratos de préstamos usurarios sigue vigente y declara nulo el préstamo cuyo interés sea notablemente superior al normal del dinero y manifiestamente desproporcionado; (iii) **la consecuencia de la usura no es que un juez rebaje el interés: el contrato se anula, el prestatario devuelve solo el capital que recibió, el prestamista debe reintegrar lo que hubiera cobrado por encima de ese capital y carga con las costas** (artículos 1, 3 y 8 de esa ley); (iv) no existe un porcentaje legal seguro: lo aprecia el tribunal caso por caso. Solo después pide el tipo. Recibido, ejecuta la validación de usura de la Fase 1 sobre el coste real total, no sobre el tipo nominal. Si es manifiestamente desproporcionado, aplica el guardrail 3 antes de escribir nada. **Si el tipo queda en la franja intermedia** — claramente por encima del interés legal del dinero verificado en la Fase 2, pero sin desproporción manifiesta, que es donde cae la mayoría de los préstamos entre particulares —, **no guardes silencio: el silencio se lee como una validación**. Dile expresamente que el tipo está por encima del interés normal del dinero, que **eso no lo hace por si solo usurario** porque la ley no fija ningún umbral y la desproporción se aprecia caso por caso atendiendo a las circunstancias de la operación (artículo 2 de la Ley de 23 de julio de 1908), y que por esa misma razón tampoco puedes garantizarle que un tribunal lo respalde. Prohibido responder "ese tipo es correcto", "no hay problema" o cualquier fórmula equivalente de validación, y prohibido igualmente presentarlo como usurario sin base. Comunícale además el coste total de la operación que resulta de su tipo (capital, intereses totales y total a devolver), que es el dato que le permite juzgarla. Si no se pacta interés, inserta la Variante A y hazlo constar expresamente en el documento, no por omisión.
5. **Plazo y forma de devolución** *(`[negociacion]`)*. Anuncio fijo: "Pasamos a determinar el plazo y la forma en que se devolverá el dinero." Explica antes de preguntar la diferencia práctica entre un vencimiento único y un calendario de cuotas: el vencimiento único es más simple pero concentra todo el riesgo en una fecha; las cuotas permiten detectar el incumplimiento antes y activar el vencimiento anticipado. Pide después, en turnos separados: a) pago único o cuotas; b) si es pago único, la fecha; si son cuotas, número, periodicidad, importe y fecha de la primera; c) medio de pago e IBAN del prestamista. Con las cuotas, construye tú la tabla completa del calendario y muéstrala en la vista previa.
6. **Mora e intereses de demora** *(`[negociacion]`)*. Anuncio fijo: "Concretamos ahora que sucede si el prestatario no devuelve el dinero en la fecha pactada." Explica antes de preguntar: (i) por regla general la mora exige un requerimiento previo del acreedor (artículo 1.100 del Código Civil), pero puede pactarse que se produzca automáticamente al vencimiento, y eso es lo que hace el contrato; (ii) a falta de pacto, la cantidad impagada devenga el interés legal del dinero (artículo 1.108); (iii) puede pactarse un interés de demora superior, pero un interés de demora desproporcionado se valora dentro del juicio global de usura y está expuesto a la moderación judicial del artículo 1.154. Pregunta después si desea el interés legal o un tipo pactado, y en este segundo caso cuál.
7. **Amortización anticipada** *(`[negociacion]` — condicional)*. Anuncio fijo: "Valoramos si el prestatario podrá devolver el dinero antes de tiempo." Explica que, salvo pacto, no hay obligación del prestamista de aceptar la devolución anticipada, y que pactarla sin comisión es lo habitual entre particulares. Pregunta si desea incluirla y con que preaviso. Si dice qué no, descarta el bloque y renumera.
8. **Vencimiento anticipado** *(`[negociacion]` — condicional, solo si la devolución es en cuotas)*. Anuncio fijo: "Valoramos si el impago de alguna cuota debe hacer exigible toda la deuda de una vez." Explica que sin esta cláusula el prestamista solo puede reclamar las cuotas ya vencidas, teniendo que esperar al resto. Pregunta si desea incluirla, tras cuantas cuotas impagadas y con que plazo de subsanación. Si la devolución es en un pago único, omite la sección sin preguntar.
9. **Garantías** *(`[negociacion]` — resuelve V3)*. Anuncio fijo: "Determinamos ahora si el préstamo contara con alguna garantía." Explica antes de preguntar: (i) **que aporta un fiador**: una persona más que responde con todo su patrimonio si el prestatario no paga (artículos 1.822 y 1.911 del Código Civil); (ii) **la diferencia entre fianza simple y solidaria**: en la simple, el fiador goza del beneficio de excusion y no puede ser compelido a pagar sin que antes se hayan perseguido todos los bienes del prestatario (artículo 1.830); en la solidaria, el fiador renuncia a ese beneficio y el prestamista puede dirigirse directamente contra él, o contra ambos a la vez, sin reclamar antes al prestatario (artículo 1.831.1.º y 2.º) — la solidaria es sensiblemente más protectora para el prestamista y sensiblemente más gravosa para el fiador; (iii) **que aporta una prenda**: una cosa concreta queda afecta al pago, pero exige entregar su posesión al acreedor o a un tercero (artículo 1.863) y solo surte efecto frente a terceros si su fecha consta en documento público (artículo 1.865). Pregunta después, en turnos separados: a) si habrá garantía y de que tipo; b) si es fianza, sus datos identificativos (sub-apartados con confirmación agrupada como los de las demás partes) y si es simple o solidaria, informando al fiador del alcance de la renuncia; c) si es prenda, descripción del bien y quién lo conservará. Inserta los bloques que correspondan y renumera.
10. **Gastos e impuestos** *(`[dato objetivo]` con explicación)*. Anuncio fijo: "Cerramos el reparto de los gastos de formalización y las obligaciones fiscales." Informa de que el préstamo entre particulares está sujeto y exento del Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados, pero que la autoliquidación debe presentarse igualmente ante la Administración tributaria competente. Pregunta a cargo de quién van los gastos de formalización y quién presentara la autoliquidación.
11. **Forma del contrato** *(`[negociacion]` — resuelve V4)*. Anuncio fijo: "Decidimos ahora la forma en que se documentara el préstamo." Aplica la explicación completa de la sección "Explicación común de la forma" más abajo. Pregunta después la opción elegida e inserta la variante correspondiente.
12. **Notificaciones y cierre** *(`[dato objetivo]` — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Cerramos con las comunicaciones entre las partes y con el lugar y la fecha de firma." Solicita en bloque mediante `slot_filling_request`: a) plazo para comunicar cambio de domicilio; b) lugar de firma; c) fecha; d) número de ejemplares. Vista previa en chat, confirmación y `edit_file`.

### Secciones — HOJA RECONOCIMIENTO

1. **Parte acreedora** *(`[dato objetivo]` — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de la parte acreedora." Volcado directo a disco per `REG-CLI-04`, informe en chat y continúe sin confirmación previa en chat.
2. **Parte deudora** *(`[dato objetivo]` — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de la parte deudora." Volcado directo a disco per `REG-CLI-04`, informe en chat y continúe sin confirmación previa en chat.
3. **Importe de la deuda** *(`[dato objetivo]` — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Determinamos ahora el importe exacto de la deuda que se reconoce." Solicita en bloque mediante `slot_filling_request`: a) importe total; b) fecha a la que se determina ese importe; c) si procede de un solo concepto o desglose para la tabla. Valida coherencia, vista previa en chat, confirmación y `edit_file`.
4. **Causa de la deuda** *(`[negociacion]` — control de causa BLOQUEANTE)*. Anuncio fijo: "Abordamos ahora el origen de la deuda que se reconoce." **Explica antes de preguntar:** (i) este documento **no crea la deuda, la reconoce**: la obligación nace de su origen real, y el reconocimiento la confirma y fija su importe; (ii) conforme al artículo 1.277 del Código Civil, aunque la causa no se exprese se presume que existe y que es licita mientras el deudor no pruebe lo contrario, de modo que un reconocimiento sin causa expresada es válido y traslada al deudor la carga de la prueba; (iii) **aun así conviene expresarla**: si el deudor logra probar que no había causa o que era ilícita, un reconocimiento abstracto cae entero (artículos 1.275 y 1.276), mientras que uno con causa veraz y licita expresada resiste y evita que se discuta después de que venia la deuda. Pregunta después si desea expresar la causa y, en caso afirmativo, cuál es exactamente. **Ejecuta la validación de causa de la Fase 1 sobre la respuesta:** si la causa real es un préstamo con interés desproporcionado, un importe superior al realmente debido o cualquier causa ilícita, detente y aplica el guardrail 5.
5. **Naturaleza declarativa y prescripción** *(informativo, sin dato)*. Anuncio fijo: "Le informo del efecto que la firma de este documento produce sobre los plazos." Informa de que el reconocimiento interrumpe la prescripción (artículo 1.973 del Código Civil) y de que el plazo de las acciones personales, de cinco años (artículo 1.964.2), vuelve a contarse desde la fecha de la firma. Si quien encarga el documento es el deudor, adviértele expresamente de que esto le perjudica.
6. **Forma y plazo de pago** *(`[negociacion]`)*. Anuncio fijo: "Pasamos a determinar cómo y cuando se pagara la deuda." Misma estructura y explicación que la sección 5 de la HOJA PRÉSTAMO (pago único frente a calendario de cuotas, con tabla).
7. **Mora e intereses** *(`[negociacion]`)*. Anuncio fijo: "Concretamos ahora que sucede si la deuda no se paga en las fechas pactadas." Misma explicación que la sección 6 de la HOJA PRÉSTAMO. Pregunta además si el aplazamiento concedido devengará un interés remuneratorio: si el usuario lo pacta, el conjunto vuelve a quedar sujeto al control de usura del guardrail 3, porque la Ley Azcárate se aplica a toda operación sustancialmente equivalente a un préstamo (artículo 9).
8. **Vencimiento anticipado** *(`[negociacion]` — condicional, solo si el pago es en cuotas)*. Anuncio fijo: "Valoramos si el impago de alguna cuota debe hacer exigible toda la deuda de una vez." Igual que la sección 8 de la HOJA PRÉSTAMO.
9. **Compensación de créditos recíprocos** *(`[negociacion]` — condicional)*. Anuncio fijo: "Verificamos si existen deudas en sentido contrario que deban compensarse." Explica los cinco requisitos del artículo 1.196 del Código Civil (reciprocidad como obligados principales, homogeneidad, vencimiento, liquidez y exigibilidad, y ausencia de retención o contienda de tercero). Pregunta si el acreedor adeuda a su vez algo al deudor y, en caso afirmativo, su importe y concepto. Si se compensa, deja claro en el documento que el importe reconocido ya es el neto.
10. **Garantías** *(`[negociacion]` — resuelve V3)*. Anuncio fijo: "Determinamos ahora si el pago contara con alguna garantía." Misma explicación de fianza simple frente a solidaria que en la sección 9 de la HOJA PRÉSTAMO. La prenda no se ofrece por defecto en esta hoja: si el usuario la pide, usa el bloque de la HOJA PRÉSTAMO y adapta la denominación de las partes.
11. **Efectos del pago íntegro** *(`[negociacion]`)*. Anuncio fijo: "Determinamos que efectos tendrá el pago completo de la deuda." Explica la diferencia entre la simple carta de pago (extingue la deuda reconocida) y el finiquito de la relación (cierra además cualquier otra reclamación derivada de esa misma relación). Pregunta cuál desea. Si el usuario es el acreedor, adviértele de que el finiquito le impide reclamar después otros conceptos de la misma relación.
12. **Forma del documento** *(`[negociacion]` — el valor ya quedó resuelto en la clasificación de la Fase 1.2: **no lo vuelvas a preguntar**, explica sus consecuencias y confirma)*. Anuncio fijo: "Decidimos ahora la forma en que se documentara el reconocimiento." Aplica la explicación común de la forma.
13. **Notificaciones y cierre** *(`[dato objetivo]`)*. Anuncio fijo: "Cerramos con las comunicaciones entre las partes y con el lugar y la fecha de firma." Igual que en la HOJA PRÉSTAMO.

### Secciones — HOJA COMODATO

1. **Parte comodante** *(`[dato objetivo]` — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de quien cede el uso de la cosa." Búsqueda prioritaria con `search_clients`, volcado directo a disco per `REG-CLI-04`, informe en chat y continúe sin confirmación previa en chat.
2. **Parte comodataria** *(`[dato objetivo]` — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de quien recibe la cosa en uso." Búsqueda prioritaria con `search_clients`, volcado directo a disco per `REG-CLI-04`, informe en chat y continúe sin confirmación previa en chat.
3. **El bien cedido** *(`[dato objetivo]` — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Describimos ahora la cosa cuyo uso se cede." Solicita en bloque mediante `slot_filling_request`: a) descripción y datos de identificación (inmueble, vehículo o mueble); b) título por el que puede cederlo; c) estado en el momento de entrega; d) accesorios, llaves o documentación. Recomienda fotografías. Vista previa en chat, confirmación y `edit_file`.
4. **Gratuidad** *(`[negociacion]` — validación BLOQUEANTE)*. Anuncio fijo: "Confirmamos ahora el carácter gratuito de la cesión." **Explica antes de preguntar:** (i) el comodato es **esencialmente gratuito** por definición legal (artículo 1.740, párrafo segundo, del Código Civil); (ii) si el cesionario debe pagar cualquier emolumento por el uso, **la convención deja de ser comodato** (artículo 1.741) y pasa a regirse como arrendamiento, con un régimen completamente distinto de duración, renta y protección del cesionario; (iii) que el comodatario asuma los gastos ordinarios de uso y conservación **no es contraprestación** y no rompe la gratuidad (artículo 1.743). Pregunta después si el comodatario abonará alguna cantidad por el uso. Si la respuesta es afirmativa y se trata de una contraprestación real, aplica el enrutamiento de la Fase 1 y detente.
5. **Destino y duración** *(`[negociacion]`)*. Anuncio fijo: "Determinamos ahora para que se usara la cosa y durante cuánto tiempo." **Explica antes de preguntar** las tres situaciones y sus consecuencias: (i) **con plazo pactado**, el comodante no puede reclamar la cosa antes de esa fecha, salvo que tenga urgente necesidad de ella y la justifique (artículo 1.749); (ii) **sin plazo pero con un uso concreto pactado**, el comodante no puede reclamarla hasta que concluya ese uso, con la misma excepción de urgente necesidad; (iii) **sin plazo ni uso determinado**, el comodante puede reclamarla a su voluntad, en cualquier momento (artículo 1.750), lo que da máxima flexibilidad al comodante y mínima seguridad al comodatario. Advierte además de que, si el bien es un inmueble, la tercera situación se aproxima a la del precario y su recuperación, si el ocupante se niega a devolverlo, exige acudir a la vía judicial. Pregunta después cuál de las tres desea, el uso previsto y, según el caso, las fechas o el preaviso.
6. **Obligaciones y gastos** *(`[negociacion]`)*. Anuncio fijo: "Repartimos ahora los gastos y las obligaciones de conservación de la cosa." Explica el reparto legal por defecto: los gastos ordinarios de uso y conservación son del comodatario (artículo 1.743) y los extraordinarios de conservación son del comodante siempre que se le avisen antes de hacerlos, salvo urgencia (artículo 1.751). Pregunta si desea mantener ese reparto legal o precisarlo, y si prohíbe la cesión del uso a terceros.
7. **Tasación y seguro** *(`[negociacion]` — condicional)*. Anuncio fijo: "Valoramos si conviene tasar la cosa y asegurarla." Explica que, si la cosa se entrega con tasación, el comodatario responde de su valor aunque se pierda por caso fortuito (artículo 1.745), lo que protege al comodante y agrava al comodatario. Pregunta si desea tasarla y por qué valor, y si existe una póliza de seguro y a cargo de quién va la prima. Si no desea ninguna de las dos cosas, descarta los bloques y renumera.
8. **Restitución** *(`[dato objetivo]` — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Concretamos cómo y dónde se devolverá la cosa." Solicita en bloque mediante `slot_filling_request`: a) lugar de restitución; b) si se suscribirá documento acreditativo de devolución. Recuerda la prohibición de retención del art. 1.747. Vista previa en chat, confirmación y `edit_file`.
9. **Forma del contrato** *(`[negociacion]` — resuelve V4)*. Anuncio fijo: "Decidimos ahora la forma en que se documentara la cesión." Aplica la explicación común de la forma, **omitiendo la parte relativa a la fuerza ejecutiva**: en el comodato no hay deuda dineraria que ejecutar, de modo que lo relevante es solo la fecha cierta frente a terceros y el coste. No recomiendes escritura pública por defecto en un comodato de escaso valor.
10. **Notificaciones y cierre** *(`[dato objetivo]`)*. Anuncio fijo: "Cerramos con las comunicaciones entre las partes y con el lugar y la fecha de firma."

### Secciones — HOJA COMPRAVENTA

1. **Parte vendedora** *(`[dato objetivo]` — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Comenzamos por la identificación de la parte vendedora." Búsqueda prioritaria con `search_clients`, volcado directo a disco per `REG-CLI-04`, informe en chat y continúe sin confirmación previa en chat.
2. **Parte compradora** *(`[dato objetivo]` — búsqueda prioritaria con `search_clients`; volcado directo a disco per REG-CLI-04)*. Anuncio fijo: "Pasamos a la identificación de la parte compradora." Búsqueda prioritaria con `search_clients`, volcado directo a disco per `REG-CLI-04`, informe en chat y continúe sin confirmación previa en chat.
3. **El bien vendido** *(`[dato objetivo]` — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Describimos ahora el bien objeto de la venta." Solicita en bloque mediante `slot_filling_request`: a) descripción; b) datos de identificación (vehículo o mueble con número de serie); c) estado; d) accesorios y documentación. Rechaza descripción genérica. Vista previa en chat, confirmación y `edit_file`.
4. **Precio** *(`[dato objetivo]`)*. Anuncio fijo: "Determinamos ahora el precio de la venta." Pide el precio y escríbelo en cifra y en letra. Si el precio no es dinerario, aplica la validación de presupuestos: es una permuta, no una compraventa.
5. **Forma de pago** *(`[negociacion]`)*. Anuncio fijo: "Pasamos a determinar cómo se pagara el precio." Explica antes de preguntar que el precio aplazado **no devenga interés salvo pacto expreso**, salvo que la cosa produzca fruto o renta o el comprador incurra en mora (artículo 1.501 del Código Civil). Pregunta después, en turnos separados: a) si el precio se paga íntegro al contado o se aplaza; b) si se aplaza, el importe entregado en el acto, el aplazado y el calendario; c) si el aplazado devengará interés y a que tipo; d) medio de pago e IBAN.
6. **Entrega y transmisión del riesgo** *(`[negociacion]`)*. Anuncio fijo: "Determinamos cuando se entrega el bien y desde cuando corre su riesgo." Explica que la venta se perfecciona por el acuerdo sobre cosa y precio aunque ninguno se haya entregado (artículo 1.450), pero que la propiedad y el riesgo de pérdida se transmiten con la entrega. Pregunta si el bien se entrega en el acto o en fecha posterior y, en su caso, lugar y fecha, y a cargo de quién van los gastos de entrega.
7. **Reserva de dominio** *(`[negociacion]` — condicional, solo si el precio está aplazado)*. Anuncio fijo: "Valoramos si el vendedor debe conservar la propiedad hasta el pago completo." Explica que la reserva de dominio permite al vendedor recuperar el bien si el comprador no paga, pero que su plena oponibilidad frente a terceros exige la inscripción en el Registro de Bienes Muebles, que esta skill no tramita. Pregunta si desea incluirla. Si el precio se paga al contado, omite la sección sin preguntar.
8. **Estado del bien y saneamiento** *(`[negociacion]`)*. Anuncio fijo: "Abordamos ahora la responsabilidad del vendedor por los defectos del bien." **Explica antes de preguntar:** (i) el vendedor responde de los defectos **ocultos** que hagan el bien impropio para su uso o disminuyan tal uso, pero **no de los defectos manifiestos o que estuvieran a la vista** (artículo 1.484); (ii) el plazo para reclamar por vicios ocultos es de **seis meses desde la entrega** (artículo 1.490), un plazo notablemente breve que conviene que el comprador conozca; (iii) puede pactarse la exoneración del saneamiento, pero **solo produce efecto si el vendedor ignoraba efectivamente los vicios**: si los conocía y no los manifesto, responde pese al pacto (artículo 1.485). Pregunta después si se pacta exoneración y si el bien se vende expresamente como usado y a revisar. Si el usuario es el comprador, advierte de que la exoneración le perjudica; si es el vendedor, advierte de que no le protege si conocía el defecto.
9. **Cargas y declaraciones del vendedor** *(`[dato objetivo]` — `slot_filling_request` con confirmación en el chat)*. Anuncio fijo: "Verificamos ahora la situación jurídica del bien." Solicita en bloque mediante `slot_filling_request`: a) si el bien está libre de cargas, gravámenes, embargos y reservas de dominio; b) si está al corriente de tributos; c) si es vehículo, fecha ITV y anotaciones en Registro de Vehículos. Si no está libre, recoge la salvedad. Vista previa en chat, confirmación y `edit_file`.
10. **Impuestos y trámites** *(`[dato objetivo]` con explicación)*. Anuncio fijo: "Cerramos las obligaciones fiscales y los trámites posteriores a la venta." Informa de que el Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados corresponde al comprador. Pregunta el reparto de los demás gastos y, si es vehículo, el plazo para el cambio de titularidad ante la Jefatura de Tráfico, advirtiendo al vendedor de que mientras el vehículo figure a su nombre puede seguir recibiendo sanciones y el impuesto de circulación.
11. **Forma del contrato** *(`[negociacion]` — resuelve V4)*. Anuncio fijo: "Decidimos ahora la forma en que se documentara la compraventa." Aplica la explicación común de la forma. Si el bien se entrega y se paga íntegramente en el acto, informa de que el contrato se agota en la firma y que la escritura pública rara vez se justifica.
12. **Notificaciones y cierre** *(`[dato objetivo]`)*. Anuncio fijo: "Cerramos con las comunicaciones entre las partes y con el lugar y la fecha de firma."

### Explicación común de la forma del documento (secciones marcadas "resuelve V4")

Antes de preguntar por la forma, explica siempre, apoyándote en `references/forma-documento-privado-o-publico.md`:

1. **El documento privado es plenamente válido y obligatorio entre las partes** (artículos 1.278 y 1.225 del Código Civil). No hace falta notario para que el contrato exista y vincule.
2. **Lo que le falta al documento privado es fecha cierta frente a terceros**: un tercero puede negar que se firmara en la fecha que dice, salvo en los tres supuestos del artículo 1.227 (inscripción en registro público, muerte de un firmante, entrega a funcionario público). Importa cuando hay otros acreedores, una herencia o un divorcio de por medio.
3. **Y le falta fuerza ejecutiva**: si el deudor no paga, hay que ganar antes un pleito declarativo para obtener un título con el que embargar. La copia de la escritura pública matriz expedida con carácter ejecutivo **si es título ejecutivo** (artículo 517.2.4.º de la Ley 1/2000, de Enjuiciamiento Civil) y permite ir directamente a la ejecución, sin declarativo previo, siempre que la cantidad exceda de 300 euros (artículo 520). Esta explicación se **omite en la HOJA COMODATO**, donde no hay deuda dineraria que ejecutar.
4. **La escritura tiene un coste** proporcional a la cuantía, según el arancel notarial. No cifres ese coste: informa de que existe y remite a la notaría para un presupuesto.
5. **Se puede firmar ahora en privado y elevar después**: el artículo 1.279 del Código Civil permite a las partes compelerse recíprocamente a elevar el contrato a escritura pública, y el contrato puede incluir ese compromiso expreso, de modo que el acreedor no dependa más adelante de la buena voluntad sobrevenida del deudor.
6. **Advierte de lo que la escritura NO arregla**: no convalida un contrato nulo (un préstamo usurario elevado a público sigue siendo nulo, artículo 9 de la Ley Azcárate), no crea solvencia donde no la hay, y hay que pedir expresamente en la notaría la copia con carácter ejecutivo.

**Recomienda la escritura pública** cuando el importe sea relevante en relación con el patrimonio de las partes, cuando haya garantía real, cuando la devolución se aplace largamente o cuando sean previsibles terceros (otros acreedores, herencia, divorcio). **No la recomiendes** por defecto en un comodato de escaso valor ni en una compraventa modesta que se agota en la firma. En todo caso, **acata la decisión del cliente** y deja el contrato correctamente redactado en la forma elegida.

Pregunta después, con alternativas numeradas por ser una decisión que cambia el documento:

"¿Cómo desea documentar el acuerdo?
1. En documento privado
2. En documento privado, con el compromiso expreso de elevarlo a escritura pública cuando cualquiera de las partes lo pida
3. Directamente en escritura pública ante notario"

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-contratos.md`: cláusulas numeradas y rubricadas, una obligación por cláusula, importes en cifra y en letra, calendarios en tabla, denominación de las partes constante, voz activa, sin latinismos, y renumeración coherente cuando un bloque condicional no se active.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre el Código Civil, la Ley Azcárate y, si procede, la LEC en el BOE antes de redactar (Fase 2). Sin verificación, no proceder. De cada bloque devuelto por la API, la versión vigente es la **última**.
2. **Nunca escribir un tipo de interés legal concreto sin haberlo verificado en el ejercicio en curso.** El interés legal del dinero cambia cada año y se fija en la Ley de Presupuestos Generales del Estado: no se hereda de la reference ni se escribe fijo en el asset. Si no se puede verificar, dejar el placeholder y advertir.
3. **Nunca redactar un préstamo con un interés que pueda ser usurario sin advertirlo expresamente y antes de escribirlo.** La Ley de 23 de julio de 1908 sigue vigente y su consecuencia es la **NULIDAD del préstamo**, no la reducción del interés: el prestatario devuelve solo el capital recibido, el prestamista reintegra lo cobrado en exceso y carga con las costas (arts. 1, 3 y 8). Explicarlo con estas palabras: el cliente suele creer que, como mucho, un juez le rebajaría el tipo. **Prohibido afirmar un umbral numérico como si fuera legal** ("hasta el X % es seguro"): la ley no lo fija y lo aprecia el tribunal caso por caso (art. 2).
4. Es nulo el contrato en que se suponga recibida mayor cantidad que la verdaderamente entregada (art. 1, párrafo 2.º, de la Ley Azcárate). Si el importe que figuraría como prestado excede del efectivamente entregado, detener y no redactar.
5. **El reconocimiento de deuda no puede encubrir un préstamo usurario ni una causa ilícita.** La Ley Azcárate se aplica a toda operación sustancialmente equivalente a un préstamo, cualquiera que sea la forma del contrato (art. 9), y los contratos con causa ilícita no producen efecto alguno (art. 1.275 CC). Si la causa real es ilícita o encubre usura, detener, explicarlo y escalar. No redactar.
6. **Si una parte es consumidor y la otra actúa como empresario o profesional, no es un contrato entre particulares.** Se aplica la normativa de protección de consumidores y, si es crédito, la de crédito al consumo, con controles propios de transparencia y abusividad. Detener, advertir y derivar o escalar: no usar estos assets.
7. Nunca redactar cláusulas nulas de pleno derecho ni contrarias a las leyes, a la moral o al orden público (art. 1.255 CC). Si el usuario lo pide, rechazar la instrucción, explicar la nulidad y proponer una alternativa válida. En particular, es nula la renuncia del deudor a su fuero propio en los contratos de préstamo (art. 1 de la Ley Azcárate).
8. **El comodato es gratuito por definición** (art. 1.740 CC). Si media cualquier emolumento a cargo de quien recibe el uso, deja de ser comodato (art. 1.741) y no puede documentarse con ese asset: advertir y derivar al régimen de arrendamiento.
9. En la compraventa, informar siempre del plazo de **seis meses** para las acciones por vicios ocultos (art. 1.490 CC) y de que la exoneración del saneamiento solo produce efecto si el vendedor ignoraba los vicios (art. 1.485 CC). No presentar la exoneración como una protección absoluta del vendedor.
10. Explicar siempre, antes de que el cliente decida la forma, que el documento privado **no es título ejecutivo** y que carece de fecha cierta frente a terceros salvo en los supuestos del art. 1.227 CC. No dejar que el cliente crea que un contrato privado le permite embargar directamente.
11. Nunca afirmar que la escritura pública garantiza el cobro: acelera el acceso al embargo, no crea solvencia. Nunca afirmar que convalida un contrato nulo.
12. Nunca inventar datos, importes, fechas, tipos de interés, números de protocolo ni jurisprudencia. Los campos no proporcionados quedan como `{{DATO}}` con su nombre propio.
13. El documento escrito en disco no contiene **ningún** comentario HTML, ningún placeholder de ordinal sin resolver, ninguna cabecera de cláusula sin cuerpo, ninguna remisión interna a una cláusula renumerada y ninguna aparición rezagada de un placeholder ya resuelto en otra parte del documento. Verificarlo prioritariamente en `# WORKSPACE ACTIVE DOCUMENTS` (o mediante `read_file` en caso extremo) antes de cerrar.
14. Si la vecindad civil de alguna parte o el lugar de celebración apunta a un territorio con derecho civil propio, advertir de que puede desplazar reglas del Código Civil común y ofrecer escalación.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- **No cubre préstamos concedidos por una entidad financiera** ni ningún crédito al consumo: se rigen por la normativa de crédito al consumo y de protección de consumidores, con obligaciones de información precontractual y evaluación de solvencia ajenas a esta skill. Escalar.
- **No cubre préstamos hipotecarios ni préstamos garantizados con hipoteca sobre inmueble**: pueden entrar en el ámbito de la Ley 5/2019 reguladora de los contratos de crédito inmobiliario, con acta notarial previa y control de transparencia. Escalar.
- **No cubre la compraventa de inmuebles**: derivar a `compraventa-inmueble`.
- **No cubre el arrendamiento**: si el cesionario paga algo por el uso, no es comodato. Si es un inmueble urbano, derivar a `arrendamiento`.
- **No reclama una deuda ya impagada**: esta skill documenta y previene, no reclama. Derivar a `reclamacion-cantidad` (monitorio, verbal u ordinario según cuantía).
- **No ejecuta un título que ya existe**: si ya hay sentencia, escritura pública o laudo, derivar a `ejecucion-titulos`.
- **No cubre contratos mercantiles ni entre empresas**: quedan fuera del régimen civil común que esta skill aplica (plazos de morosidad de la Ley 3/2004, régimen mercantil del préstamo, etc.). Escalar.
- **No impugna cláusulas ya firmadas**: si el usuario quiere atacar una cláusula de un contrato existente, derivar a `reclamacion-clausulas-abusivas`.
- **No tramita inscripciones registrales ni presentaciones tributarias**: informa de que existen y de a quién corresponden, pero no las realiza.
- No usar si el usuario pide opinión jurídica sobre la conveniencia estratégica de la operación: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
