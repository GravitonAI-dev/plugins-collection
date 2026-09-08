---
name: reclamacion-consumo
description: >
  Genera los documentos del itinerario extrajudicial de una reclamación de consumo en España: la
  reclamación previa dirigida a la empresa, la hoja oficial de quejas y reclamaciones, el escrito ante
  la administración autonómica o municipal de consumo y la solicitud de arbitraje de consumo. Aplica el
  texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios y el Reglamento del
  Sistema Arbitral de Consumo aprobado por Real Decreto 713/2024, que derogó el Real Decreto 231/2008
  con efectos desde el 13 de agosto de 2024, en sus versiones consolidadas vigentes verificadas en el
  BOE, y contrasta el procedimiento con la normativa de consumo de la comunidad autónoma, que fija el
  modelo de hoja y el organismo competente. Metodología: comprobación previa de la condición de
  consumidor y del agotamiento de la vía previa, clasificación del documento mediante formulario
  interactivo, cómputo y comunicación de plazos, creación del documento base en el workspace y edición
  incremental apartado a apartado. NO usar para la reclamación judicial de la cantidad, que corresponde
  a `derecho-civil:reclamacion-cantidad`, ni para la nulidad de cláusulas abusivas, que corresponde a
  `derecho-civil:reclamacion-clausulas-abusivas`.
when_to_use: |
  - El usuario quiere reclamar a una empresa por un producto defectuoso, un servicio mal prestado o un cobro indebido.
  - El usuario quiere rellenar la hoja oficial de quejas y reclamaciones.
  - El usuario ha reclamado a la empresa y no ha obtenido respuesta, o la respuesta ha sido negativa, y quiere dar el paso siguiente.
  - El usuario quiere solicitar arbitraje de consumo, o saber si le conviene.
  - El usuario quiere presentar un escrito ante la administración de consumo de su comunidad autónoma o ante la oficina municipal de información al consumidor.
  - El usuario pregunta qué plazo tiene la empresa para responder y qué ocurre si no lo hace.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_documento: reclamación previa a la empresa / hoja oficial de reclamaciones / solicitud de arbitraje de consumo / escrito ante la administración de consumo
  - sector: bienes de consumo / servicios básicos de electricidad, gas o agua / telecomunicaciones / banca o seguros / transporte / otro
  - estado_reclamacion_previa: todavía no se ha reclamado a la empresa / se reclamó y no hubo respuesta / se reclamó y la respuesta fue negativa
  - condicion_reclamante: consumidor / empresario o profesional
  - adhesion_arbitraje: la empresa está adherida al sistema arbitral / no lo está / no consta
  - datos_reclamante: nombre y apellidos, DNI o NIE, domicilio, teléfono y correo electrónico
  - datos_empresa: razón social, CIF si consta, domicilio del establecimiento y domicilio social
  - datos_contrato: número de contrato, factura o pedido, fecha y precio pagado
  - relato_hechos: descripción ordenada y fechada de lo ocurrido
  - pretension: qué se pide exactamente y su importe si es económica
outputs:
  - documento_reclamacion: documento completo en markdown, DRAFT, con hechos numerados, petición concreta y relación de documentos que se acompañan
references:
  - references/fuentes-plantillas-validadas.md
  - references/vias-de-reclamacion-y-organismo-competente.md
  - references/plazos-de-garantia-y-reclamacion.md
  - references/arbitraje-de-consumo.md
  - references/condicion-de-consumidor.md
assets:
  - assets/template-reclamacion-previa-empresa.md
  - assets/template-hoja-reclamaciones.md
  - assets/template-solicitud-arbitraje-consumo.md
  - assets/template-escrito-administracion-consumo.md
---

# Generar la Reclamación de Consumo

> DRAFT — para revisión por un abogado colegiado antes de su presentación. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `reclamacion_empresa` | `hoja_reclamaciones` | `solicitud_arbitraje` | `escrito_administracion`.
- **V2 (Sector):** `bienes` | `servicios_basicos` | `telecomunicaciones` | `banca_seguros` | `transporte` | `otro`.
- **V3 (Estado de la reclamación previa):** `no_reclamado` | `sin_respuesta` | `respuesta_negativa`.
- **V4 (Condición de quien reclama):** `consumidor` | `empresario_profesional`.
- **V5 (Adhesión de la empresa al arbitraje):** `si` | `no` | `no_consta`.
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa

Antes de invocar el formulario, extrae del mensaje del usuario todo dato que ya conste: qué ha comprado o contratado, con qué empresa, qué ha fallado, cuándo, cuánto pagó, si ya reclamó y qué le contestaron. **No vuelvas a preguntar nada que el usuario ya haya dicho:** preselecciona las opciones que se deduzcan del relato.

Presta atención especial a dos datos que el usuario suele dar sin que se le pregunte y que cambian el itinerario: **la fecha de compra o de contratación**, que gobierna los plazos, y **si quien reclama actuaba como particular o para su negocio**, que gobierna el régimen aplicable.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

Invoca la herramienta con las opciones de triaje:

```json
{
  "form_data": [
    {
      "id": "tipo_documento",
      "rationale": "Resolver V1: cada escalón del itinerario tiene su propio documento, su propio destinatario y su propio plazo de respuesta.",
      "question": "¿Qué documento necesita preparar?",
      "options": [
        {"id": "reclamacion_empresa", "label": "La reclamación dirigida a la propia empresa"},
        {"id": "hoja_reclamaciones", "label": "La hoja oficial de quejas y reclamaciones"},
        {"id": "solicitud_arbitraje", "label": "La solicitud de arbitraje de consumo"},
        {"id": "escrito_administracion", "label": "El escrito ante la administración de consumo"}
      ]
    },
    {
      "id": "sector",
      "rationale": "Resolver V2: el organismo competente y el procedimiento cambian por sector, y en cuatro de ellos existe un supervisor propio ante el que hay que reclamar antes o en lugar de la administración general de consumo.",
      "question": "¿A qué sector pertenece la empresa reclamada?",
      "options": [
        {"id": "bienes", "label": "Compra de un bien o producto"},
        {"id": "servicios_basicos", "label": "Electricidad, gas o agua"},
        {"id": "telecomunicaciones", "label": "Teléfono, internet o televisión de pago"},
        {"id": "banca_seguros", "label": "Banca, financiación o seguros"},
        {"id": "transporte", "label": "Transporte aéreo, ferroviario o por carretera"},
        {"id": "otro", "label": "Otro servicio"}
      ]
    },
    {
      "id": "estado_reclamacion_previa",
      "rationale": "Resolver V3: el arbitraje y la reclamación ante el organismo sectorial exigen haber reclamado antes a la empresa y acreditar su respuesta o el transcurso del plazo.",
      "question": "¿Ha reclamado ya a la empresa?",
      "options": [
        {"id": "no_reclamado", "label": "No, todavía no"},
        {"id": "sin_respuesta", "label": "Sí, y no ha obtenido respuesta"},
        {"id": "respuesta_negativa", "label": "Sí, y la respuesta ha sido negativa o insuficiente"}
      ]
    },
    {
      "id": "condicion_reclamante",
      "rationale": "Resolver V4: la protección del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios exige actuar con un propósito ajeno a la actividad empresarial o profesional. Sin esa condición, el régimen es otro.",
      "question": "¿Adquirió el producto o contrató el servicio como particular, o para su actividad profesional o empresarial?",
      "options": [
        {"id": "consumidor", "label": "Como particular, para uso personal o familiar"},
        {"id": "empresario_profesional", "label": "Para mi actividad profesional o empresarial"}
      ]
    },
    {
      "id": "adhesion_arbitraje",
      "rationale": "Resolver V5: el arbitraje solo obliga a la empresa si esta adherida o si acepta someterse. Sin adhesión, la solicitud puede quedar en nada y conviene decirlo antes de presentarla.",
      "question": "¿Está la empresa adherida al Sistema Arbitral de Consumo?",
      "options": [
        {"id": "si", "label": "Sí, tiene el distintivo o consta su adhesión"},
        {"id": "no", "label": "No está adherida"},
        {"id": "no_consta", "label": "No lo sé: verifíquelo usted"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_documento`
- `V2` — `sector`
- `V3` — `estado_reclamacion_previa`
- `V4` — `condicion_reclamante`
- `V5` — `adhesion_arbitraje`

### 1.3 Control de Admisibilidad y Enrutamiento (PRIMERA ACCIÓN OBLIGATORIA)

**Comprobación 1 — ¿Actúa como consumidor?**

* **Si `[V4 = empresario_profesional]` → DETENER y advertir.** Explica en el chat que el régimen protector de consumidores exige haber actuado con un propósito ajeno a la actividad empresarial o profesional, y que sin esa condición no caben ni la hoja oficial de reclamaciones ni el arbitraje de consumo, quedando la vía de la reclamación contractual ordinaria. Ofrece preparar una reclamación mercantil entre empresas y deriva a `derecho-civil:reclamacion-cantidad`. **No crear documento de consumo.**

**Comprobación 2 — ¿Está agotada la vía previa?** El arbitraje y los organismos sectoriales exigen haber reclamado antes a la empresa.

* **Si `[V3 = no_reclamado]` y `[V1 = solicitud_arbitraje]`, o `[V3 = no_reclamado]` y `[V1 = escrito_administracion]` → reconducir. Esta regla tiene prioridad sobre el enrutamiento de la comprobacion 4.** Explica que el paso previo es reclamar a la empresa y que sin acreditarlo la solicitud puede inadmitirse. Genera primero `assets/template-reclamacion-previa-empresa.md` y ofrece preparar después el documento pedido.

**Comprobación 3 — Cómputo y comunicación de plazos.** Antes de redactar, pide la fecha de compra o de contratación y la del hecho reclamado, y comunica en el chat el plazo de garantía o de reclamación aplicable, los días consumidos y la fecha límite, sobre `references/plazos-de-garantia-y-reclamacion.md`. **Verifica los plazos en el texto vigente: no los cites de memoria.**

**Comprobación 4 — Enrutamiento:**
* **Si `[V1 = reclamacion_empresa]` → Plantilla: `assets/template-reclamacion-previa-empresa.md`.** Es el documento que abre el itinerario y del que dependen todos los siguientes.
* **Si `[V1 = hoja_reclamaciones]` → Plantilla: `assets/template-hoja-reclamaciones.md`.** Advierte de que el modelo oficial lo aprueba cada comunidad autónoma: este documento vuelca el contenido, y **verifica con `web_search` el modelo y el procedimiento de presentación de la comunidad autónoma** antes de darlo por bueno.
* **Si `[V1 = solicitud_arbitraje]` y `[V3 = sin_respuesta o respuesta_negativa]` → Plantilla: `assets/template-solicitud-arbitraje-consumo.md`.**
* **Si `[V1 = escrito_administracion]` y `[V3 = sin_respuesta o respuesta_negativa]` → Plantilla: `assets/template-escrito-administracion-consumo.md`.**
* **Si `[V5 = no]` y `[V1 = solicitud_arbitraje]` → advertencia obligatoria antes de redactar:** el arbitraje es voluntario para la empresa que no está adherida, y puede negarse a someterse, en cuyo caso el procedimiento termina sin laudo. Explica que la solicitud sigue siendo útil porque acredita el intento, pero no prometas resultado. Ofrece valorar en paralelo la vía judicial.
* **Si `[V5 = no_consta]` → resuélvelo tú** con `web_search` en el registro público de empresas adheridas antes de continuar, e informa del resultado.
* **Si `[V2 = banca_seguros]` → advertencia de vía propia:** la reclamación bancaria y de seguros tiene un itinerario específico ante el servicio de atención al cliente de la entidad y, después, ante el supervisor competente. Explícalo y **verifica con `web_search` el organismo y el plazo vigentes** antes de dirigir el escrito.
* **Si `[V2 = telecomunicaciones]` → advertencia de vía propia:** existe una oficina de atención al usuario de telecomunicaciones con procedimiento y plazo propios. Explícalo y verifica el procedimiento vigente antes de redactar.
* **Si `[V2 = servicios_basicos]` → advertencia de vía propia:** la reclamación de electricidad, gas o agua se dirige al servicio de atención de la comercializadora o distribuidora y, después, al organismo competente de la comunidad autónoma. Verifica cuál es.
* **Si `[V2 = transporte]` y el transporte es aéreo → advertencia de vía propia:** la compensación por cancelación, gran retraso o denegación de embarque se rige por el Reglamento (CE) 261/2004 y se reclama ante la compañía y después ante el organismo nacional de supervisión. Prepara la reclamación previa y advierte de esa vía.
* **Si la pretensión exige declarar nula una cláusula del contrato → DETENER esa pretensión concreta** y derivar a `derecho-civil:reclamacion-clausulas-abusivas`, sin perjuicio de continuar con la reclamación de consumo por los demás conceptos.
* **Si se reclaman daños personales o lesiones → DETENER esa pretensión concreta** y derivar a `derecho-civil:responsabilidad-civil`, que cuantifica el daño.
* **Si la empresa no responde y lo que procede ya es demandar → DETENER esa pretensión concreta**: derivar a `derecho-civil:reclamacion-cantidad` y advertir del requisito de procedibilidad del medio adecuado de solución de controversias, que cubre `derecho-civil:masc-acuerdos`.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **Identificación de la empresa.** Sin razón social o, al menos, nombre comercial y domicilio del establecimiento, la reclamación no llega a su destinatario. Si el usuario solo tiene el nombre comercial, indícale cómo obtener la razón social del ticket, la factura o el propio establecimiento.
- **Prueba de la relación de consumo.** Ticket, factura, contrato, pedido o extracto bancario. Sin ninguno de ellos, adviértelo: la reclamación es posible, pero su prueba es débil.
- **Concreción de la pretensión.** Reparación, sustitución, rebaja del precio, resolución con devolución o indemnización. Una reclamación que no pide algo concreto no obliga a la empresa a nada.
- **Coherencia entre lo pedido y lo probado.** Si el importe reclamado no se corresponde con lo acreditado, dialógalo antes de escribirlo.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente en el BOE del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios y del Reglamento del Sistema Arbitral de Consumo aprobado por Real Decreto 713/2024.
3. **Identifica el organismo competente** con `web_search` a partir de la comunidad autónoma y del sector: cada comunidad tiene su propia dirección general de consumo y su propio modelo de hoja de reclamaciones, y los sectores regulados tienen supervisor propio.
4. Verifica los plazos vigentes: el de garantía legal, el de reclamación ante la empresa, el de respuesta de la empresa y el de resolución del arbitraje. **No los cites de memoria.**
5. **Si detectas una versión posterior a la registrada, aplica la redacción vigente al documento que redactas en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Vía elegida y por qué**, con el organismo competente identificado por su denominación exacta.
2. **Plazos:** el que tiene el usuario para reclamar y el que tiene la empresa u organismo para responder, con la fecha límite concreta.
3. **Qué ocurre si no hay respuesta:** el paso siguiente del itinerario, dicho de antemano.
4. **Documentos que debe conservar y acompañar.**
5. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y verifica que identifique a las dos partes, describa los hechos con fechas y formule una petición concreta. Si falta alguno de esos elementos, adviértelo y propón la redacción que lo subsana.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission**: sustituye los datos ya conocidos y deja los pendientes como marcadores en mayúsculas entre dobles llaves. PROHIBIDO dejar archivos en blanco, con títulos solos o con resúmenes.
2. **Validación (`read_file`):** comprueba el volcado íntegro sobre la ruta exacta escrita.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (relato de hechos)] --> [Vista previa en texto plano]
      --> [«¿Confirmamos esta sección?»] --> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** los datos de quien reclama, los de la empresa y los del contrato o compra se piden en bloque, nunca dato a dato.
- **Confirmación agrupada por parte:** los datos de una misma persona o empresa se confirman todos juntos al final del bloque.
- **Anuncio de sección visible** al pasar de una sección a la siguiente, en el mismo mensaje que la primera solicitud.
- **Validación de sentido, no solo de formato:** si un importe o una fecha no encajan con lo relatado, dialógalo antes de volcarlo.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificarle a usted y a la empresa frente a la que reclama."
- Sección 2: "Identificadas las partes, corresponde precisar qué compró o contrató y cuándo."
- Sección 3: "Precisada la contratación, procede exponer los hechos que motivan la reclamación."
- Sección 4: "Expuestos los hechos, corresponde concretar qué solicita exactamente."
- Sección 5: "Por último, procede relacionar los documentos que acompaña y fijar el plazo de respuesta."

1. **Partes [dato objetivo].** Solicita en bloque mediante `slot_filling_request`: de quien reclama, nombre y apellidos, DNI o NIE, domicilio, teléfono y correo electrónico; de la empresa, razón social si consta, nombre comercial, CIF si consta, domicilio del establecimiento y domicilio social. Explica que el domicilio de la empresa determina a dónde se dirige el escrito y qué administración es competente.
2. **Objeto de la contratación [dato objetivo].** Número de contrato, factura, pedido o referencia; fecha de compra o de contratación; precio pagado; medio de pago. Explica que el medio de pago importa: si se pagó con tarjeta o financiación, pueden existir vías adicionales de recuperación del importe.
3. **Hechos [negociación — el apartado que define la reclamación].** Solicita el relato en el chat, ordenado cronológicamente y con fechas. Explica que los hechos deben ser concretos y comprobables, y que conviene separar lo que se puede probar de lo que es una impresión.
4. **Pretensión [negociación].** Explica en el chat las opciones y sus consecuencias antes de elegir: reparación, sustitución, rebaja del precio, resolución del contrato con devolución del importe, o indemnización de daños. Explica el orden de prelación que la ley establece entre ellas y por qué no siempre se puede elegir libremente. Después, formula la petición con su importe.
5. **Documentos y plazo [dato objetivo].** Relaciona numerados los documentos que se acompañan, fija el plazo de respuesta y consigna el medio de envío. Explica que debe conservarse copia sellada o justificante de la presentación.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Ampliar el relato de hechos o el desglose de importes.
3. Cambiar la pretensión o el plazo concedido.
4. Preparar el documento siguiente del itinerario si la empresa no responde.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado colegiado antes de su presentación.
- **Conservación de la prueba:** copia sellada o justificante de presentación, y todos los documentos aportados. Sin ellos, la reclamación no se acredita.
- **Plazo de respuesta:** informar del plazo que tiene la empresa u organismo y de qué ocurre si transcurre sin respuesta.
- **Siguiente escalón:** decir de antemano cuál es, para que el usuario no pierda tiempo si no le contestan.
- **Voluntariedad del arbitraje:** si la empresa no está adherida, puede negarse a someterse y el procedimiento termina sin laudo.
- **Eficacia del laudo:** el laudo arbitral obliga a las partes y es ejecutable, y solo cabe frente a él la acción de anulación en los supuestos tasados.
- **Prescripción:** la reclamación extrajudicial no suspende indefinidamente el plazo de la acción judicial. Advertir de la fecha límite real.
- **Vía judicial:** si se acude después al juzgado, recordar el requisito de procedibilidad del medio adecuado de solución de controversias.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación previa obligatoria.** Verificar en el BOE la versión consolidada vigente del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios y del Reglamento del Sistema Arbitral de Consumo antes de redactar. Sin verificación, no proceder.
2. **Normativa autonómica.** El modelo de hoja de reclamaciones, el organismo competente y parte del procedimiento son autonómicos. Verificarlos con `web_search` para la comunidad autónoma del caso: no presumir el procedimiento de una comunidad en otra.
3. **Condición de consumidor como presupuesto.** Sin ella no hay hoja oficial ni arbitraje de consumo. Decirlo antes de redactar, no después.
4. **Cero promesas de resultado.** No afirmar que la empresa devolverá el dinero, ni que el arbitraje prosperará. Explicar plazos, vías y probabilidades en términos honestos.
5. **Cero invención de datos y de plazos.** No inventar números de contrato, referencias de expediente, importes, fechas ni plazos de garantía. Los datos no aportados permanecen como marcador con su nombre propio de plantilla.
6. **Prelación de remedios.** No ofrecer la resolución del contrato con devolución del importe como si fuera siempre la primera opción: la ley establece un orden entre reparación, sustitución, rebaja y resolución. Explicarlo con el precepto verificado.
7. **Separación de vías.** La nulidad de cláusulas, los daños personales y la reclamación judicial de cantidad tienen sus propias skills. No redactarlos aquí.
8. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real.
