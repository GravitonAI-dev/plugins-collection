---
name: masc-acuerdos
description: >
  Produce los documentos del requisito de procedibilidad de los medios adecuados de solución de
  controversias (MASC) introducido por la Ley Orgánica 1/2025, de 2 de enero, de medidas en materia de
  eficiencia del Servicio Público de Justicia, exigible en el orden civil desde el 3 de abril de 2025:
  el requerimiento de negociación con que se inicia la actividad negociadora, el acta que acredita el
  intento y su resultado, la oferta vinculante confidencial, el acuerdo transaccional que pone fin a la
  controversia y la declaración responsable de imposibilidad cuando el intento no puede llevarse a cabo.
  Aplica la Ley Orgánica 1/2025 y los artículos de la Ley 1/2000 de Enjuiciamiento Civil que aquella
  reforma, en sus versiones consolidadas vigentes verificadas en el BOE. Metodología: clasificación del
  documento y del medio empleado mediante formulario interactivo, control previo de si la materia está
  exceptuada del requisito, cómputo y comunicación de los plazos de suspensión de la prescripción y de
  la caducidad, creación del documento base en el workspace y edición incremental apartado a apartado.
  NO usar para redactar la demanda posterior, que corresponde a la skill del procedimiento aplicable, ni
  para el intento de conciliación previo a la vía social, que corresponde a la skill
  `derecho-laboral:conciliacion-previa`.
when_to_use: |
  - El usuario necesita acreditar el intento de un medio adecuado de solución de controversias antes de presentar una demanda civil.
  - El usuario quiere requerir a la otra parte para negociar, con constancia fehaciente de la fecha y del contenido.
  - El usuario quiere documentar el resultado de una negociación, una mediación o una conciliación privada, con acuerdo, sin acuerdo o sin respuesta.
  - El usuario quiere formular una oferta vinculante confidencial, o valorar la que ha recibido.
  - El usuario ha alcanzado un acuerdo y quiere recogerlo en un documento transaccional, con o sin elevación a escritura pública.
  - El usuario no puede intentar el MASC porque desconoce el domicilio o el medio de contacto de la otra parte, y necesita la declaración responsable.
  - Otra skill del catálogo ha detectado que falta el requisito de procedibilidad y deriva aquí.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_documento: requerimiento de negociación / acta del intento / oferta vinculante / acuerdo transaccional / declaración responsable de imposibilidad
  - momento_procesal: antes de presentar la demanda / con el proceso ya iniciado
  - medio_empleado: negociación directa entre las partes o sus abogados / mediación / conciliación privada / oferta vinculante confidencial / opinión de persona experta independiente / derecho colaborativo
  - materia_exceptuada: la materia está excluida del requisito / no lo está / el usuario no lo sabe
  - resultado_intento: acuerdo total / acuerdo parcial / sin acuerdo / la otra parte no ha respondido
  - datos_requirente: nombre o razón social, DNI, NIE o CIF, domicilio a efectos de notificaciones, teléfono y correo electrónico
  - datos_requerido: nombre o razón social, DNI, NIE o CIF, domicilio a efectos de notificaciones
  - objeto_controversia: descripción de la pretensión, su fundamento y, si es económica, su importe
  - fechas_actividad: fecha del requerimiento, de la respuesta, de las sesiones celebradas y de la terminación
  - contenido_acuerdo: obligaciones asumidas por cada parte, plazos, forma de pago y garantías
outputs:
  - documento_masc: documento completo en markdown, DRAFT, con la mención expresa de los preceptos que lo amparan y la advertencia sobre su eficacia procesal
references:
  - references/fuentes-plantillas-validadas.md
  - references/masc-tipos-y-requisitos.md
  - references/masc-materias-exceptuadas.md
  - references/masc-plazos-prescripcion-y-caducidad.md
  - references/masc-efectos-procesales-y-costas.md
assets:
  - assets/template-requerimiento-negociacion-masc.md
  - assets/template-acta-intento-masc.md
  - assets/template-oferta-vinculante.md
  - assets/template-acuerdo-transaccional-masc.md
  - assets/template-declaracion-responsable-imposibilidad-masc.md
---

# Producir los Documentos del Medio Adecuado de Solución de Controversias

> DRAFT — para revisión por un abogado colegiado antes de su firma o presentación. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `requerimiento_negociacion` | `acta_intento` | `oferta_vinculante` | `acuerdo_transaccional` | `declaracion_responsable`.
- **V2 (Momento procesal):** `antes_de_demanda` | `proceso_iniciado`.
- **V3 (Medio empleado):** `negociacion_directa` | `mediacion` | `conciliacion_privada` | `oferta_vinculante` | `opinion_experto` | `derecho_colaborativo`.
- **V4 (Materia exceptuada del requisito):** `si` | `no` | `no_lo_se`.
- **V5 (Resultado del intento):** `acuerdo_total` | `acuerdo_parcial` | `sin_acuerdo` | `sin_respuesta` | `no_procede`.
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa

Antes de invocar el formulario, extrae del mensaje del usuario todo dato que ya conste: qué documento necesita, si hay demanda presentada, qué medio se ha empleado o se pretende emplear, cuál es el objeto de la controversia y su importe, y si ya hubo requerimiento o respuesta. **No vuelvas a preguntar nada que el usuario ya haya dicho:** preselecciona en el formulario las opciones que se deduzcan del relato y omite las preguntas ya resueltas.

Si el usuario llega derivado de otra skill del catálogo porque le faltaba el requisito de procedibilidad, da por resuelto `V2 = antes_de_demanda` y toma de esa conversación el objeto y el importe de la controversia.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

Invoca la herramienta con las opciones de triaje:

```json
{
  "form_data": [
    {
      "id": "tipo_documento",
      "rationale": "Resolver V1: cada documento del itinerario del MASC tiene su propio asset, su propio contenido mínimo y una eficacia procesal distinta.",
      "question": "¿Qué documento necesita preparar?",
      "options": [
        {"id": "requerimiento_negociacion", "label": "El requerimiento con que se invita a la otra parte a negociar"},
        {"id": "acta_intento", "label": "El acta que acredita el intento y su resultado, para acompañar a la demanda"},
        {"id": "oferta_vinculante", "label": "Una oferta vinculante confidencial"},
        {"id": "acuerdo_transaccional", "label": "El acuerdo alcanzado, para documentarlo"},
        {"id": "declaracion_responsable", "label": "La declaración responsable de que el intento no puede llevarse a cabo"}
      ]
    },
    {
      "id": "momento_procesal",
      "rationale": "Resolver V2: el requisito de procedibilidad opera antes de la demanda, mientras que el MASC posterior a la iniciación del proceso tiene otro régimen y otros efectos.",
      "question": "¿En qué momento se encuentra el asunto?",
      "options": [
        {"id": "antes_de_demanda", "label": "Todavía no se ha presentado demanda"},
        {"id": "proceso_iniciado", "label": "El proceso judicial ya está iniciado"}
      ]
    },
    {
      "id": "medio_empleado",
      "rationale": "Resolver V3: el medio determina el contenido del acta, la intervención o no de un tercero neutral y si la asistencia letrada es preceptiva.",
      "question": "¿Qué medio se ha empleado o se pretende emplear?",
      "options": [
        {"id": "negociacion_directa", "label": "Negociación directa entre las partes o entre sus abogados"},
        {"id": "mediacion", "label": "Mediación, con persona mediadora"},
        {"id": "conciliacion_privada", "label": "Conciliación privada ante un tercero conciliador"},
        {"id": "oferta_vinculante", "label": "Formulación de una oferta vinculante confidencial"},
        {"id": "opinion_experto", "label": "Opinión de una persona experta independiente"},
        {"id": "derecho_colaborativo", "label": "Derecho colaborativo"}
      ]
    },
    {
      "id": "materia_exceptuada",
      "rationale": "Resolver V4: si la materia está exceptuada, el intento no es requisito de procedibilidad y presentarlo puede consumir plazo sin necesidad. Es un control previo bloqueante.",
      "question": "¿Versa el asunto sobre alguna materia excluida del requisito, como tutela de derechos fundamentales, medidas cautelares, protección de menores o filiación?",
      "options": [
        {"id": "no", "label": "No, es una materia civil ordinaria"},
        {"id": "si", "label": "Sí, es una de las materias excluidas"},
        {"id": "no_lo_se", "label": "No lo sé: verifíquelo usted"}
      ]
    },
    {
      "id": "resultado_intento",
      "rationale": "Resolver V5: el acta y el acuerdo cambian por completo según el resultado, y el acuerdo parcial obliga a delimitar qué queda pendiente para el proceso.",
      "question": "Si el intento ya se ha producido, ¿cuál ha sido su resultado?",
      "options": [
        {"id": "acuerdo_total", "label": "Acuerdo sobre la totalidad de la controversia"},
        {"id": "acuerdo_parcial", "label": "Acuerdo sobre parte de la controversia"},
        {"id": "sin_acuerdo", "label": "No ha sido posible alcanzar un acuerdo"},
        {"id": "sin_respuesta", "label": "La otra parte no ha respondido o no ha comparecido"},
        {"id": "no_procede", "label": "No procede: el intento todavía no se ha producido"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_documento`
- `V2` — `momento_procesal`
- `V3` — `medio_empleado`
- `V4` — `materia_exceptuada`
- `V5` — `resultado_intento`

### 1.3 Control de Procedibilidad y Enrutamiento (PRIMERA ACCIÓN OBLIGATORIA)

**Comprobación 1 — ¿Está la materia exceptuada del requisito?** La Ley Orgánica 1/2025 excluye del requisito de procedibilidad un grupo de materias por su naturaleza urgente, indisponible o de orden público. **Verifica con `web_search` la relación vigente de excepciones antes de pronunciarte**, sobre `references/masc-materias-exceptuadas.md`.

* **Si `[V4 = si]` → informa de que el intento no es exigible** y explica que presentarlo no es un defecto, pero tampoco un requisito, y que no conviene consumir plazo con un trámite innecesario cuando la acción está sujeta a caducidad. Ofrece continuar de todos modos si el usuario lo prefiere por estrategia, advirtiendo de que es una decisión suya.
* **Si `[V4 = no_lo_se]` → resuélvelo tú** con `web_search` sobre el texto consolidado antes de continuar, e informa del resultado en el chat con la cita del precepto y el enlace consultado.

**Comprobación 2 — Cómputo y comunicación de plazos.** Antes de redactar nada, pide la fecha del hecho o del vencimiento de la obligación y comunica en el chat, con este orden: el plazo de prescripción o caducidad de la acción, los días ya consumidos, la fecha límite y el efecto que el MASC produce sobre ese plazo. Trabaja sobre `references/masc-plazos-prescripcion-y-caducidad.md` y **verifica la redacción vigente antes de afirmar cualquier plazo**. Si la acción está sujeta a caducidad y el plazo se agota, adviértelo de forma destacada antes de continuar y no lo escondas en el documento.

**Comprobación 3 — Enrutamiento:**
* **Si `[V1 = requerimiento_negociacion]` → Plantilla: `assets/template-requerimiento-negociacion-masc.md`.** Es el documento que abre la actividad negociadora y del que arranca el cómputo. Debe remitirse por un medio que deje constancia fehaciente de su contenido, de su fecha de envío y de su recepción.
* **Si `[V1 = acta_intento]` → Plantilla: `assets/template-acta-intento-masc.md`.** Es el documento que se acompaña a la demanda para acreditar el requisito.
* **Si `[V1 = oferta_vinculante]` → Plantilla: `assets/template-oferta-vinculante.md`.** Advierte en el chat, antes de redactar, de que la oferta vinculante obliga al oferente en sus propios términos si es aceptada dentro del plazo que se fije, y de que por ello el plazo y el contenido deben cerrarse con precisión.
* **Si `[V1 = acuerdo_transaccional]` → Plantilla: `assets/template-acuerdo-transaccional-masc.md`.**
* **Si `[V1 = declaracion_responsable]` → Plantilla: `assets/template-declaracion-responsable-imposibilidad-masc.md`.** Solo procede cuando el intento resulta materialmente imposible, señaladamente por desconocerse el domicilio o el medio por el que requerir a la otra parte. **No es una vía para saltarse el requisito:** exige que la imposibilidad sea real y quede razonada, y su falsedad tiene consecuencias.
* **Si `[V1 = acta_intento]` y `[V5 = no_procede]` → DETENER esa pretensión concreta:** no puede acreditarse un intento que todavía no se ha producido. Reconduce al requerimiento de negociación y ofrece preparar el acta cuando el intento haya terminado.
* **Si `[V1 = acuerdo_transaccional]` y `[V5 = sin_acuerdo o sin_respuesta]` → DETENER esa pretensión concreta:** no hay acuerdo que documentar. Reconduce al acta del intento, que es lo que habilita la demanda.
* **Si `[V5 = acuerdo_parcial]`,** cualquiera que sea el documento, **delimita por escrito qué extremos quedan acordados y qué extremos quedan subsistentes**, porque solo estos últimos podrán llevarse al proceso y el acuerdo sobre los demás vincula a las partes.
* **Si `[V2 = proceso_iniciado]`,** el documento no cumple ya el requisito de procedibilidad, que se refiere al momento anterior a la demanda. Explícalo y sitúa el documento en su función propia: poner fin al proceso por acuerdo, o suspenderlo mientras se negocia. **No presentes como requisito lo que ya no lo es.**
* **Si `[V3 = mediacion o conciliacion_privada]`,** el acta debe identificar a la persona mediadora o conciliadora y su condición, y **verifica con `web_search` los requisitos vigentes de capacitación y de registro** antes de afirmarlos.
* **Si `[V3 = oferta_vinculante]` y el interés económico del asunto excede del umbral legal,** advierte de que la asistencia letrada es preceptiva, **con el umbral verificado en el texto vigente y no citado de memoria**.
* **Si lo que se pretende es el intento de conciliación previo a una demanda ante el Juzgado de lo Social → DETENER**: régimen distinto. Derivar a `derecho-laboral:conciliacion-previa`. No crear documento.
* **Si lo que se pretende es redactar la demanda posterior → DETENER esa pretensión**: esta skill prepara el MASC. Derivar a la skill del procedimiento aplicable (`monitorio`, `juicio-ordinario`, `reclamacion-cantidad`, `desahucio` y las demás del plugin), y ofrecer encadenar con ella al cerrar el documento.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **Identificación suficiente del requerido.** Sin nombre y domicilio a efectos de notificaciones no hay requerimiento válido. Si faltan, pídelos antes de redactar; si son inaveriguables, reconduce a la declaración responsable.
- **Objeto determinado.** La controversia debe quedar acotada: pretensión, fundamento e importe si es económica. Un requerimiento genérico no acredita el intento y compromete la demanda posterior.
- **Coherencia entre el objeto del MASC y el de la futura demanda.** Adviértele de que lo que no se haya sometido a la actividad negociadora puede quedar fuera del requisito, y que ampliar después la pretensión obliga a valorar un nuevo intento.
- **Confidencialidad.** Recuérdale que lo actuado en el MASC es confidencial y que no puede aportarse al proceso más allá de lo que la ley permite, señaladamente el acta acreditativa del intento y su resultado.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna

- Consulta las referencias cargadas en tu contexto.
- Verifica con `web_search` la versión consolidada vigente de la Ley Orgánica 1/2025 en el BOE y la de los artículos de la Ley 1/2000 de Enjuiciamiento Civil que aquella reforma. **La relación de materias exceptuadas ya se verificó en el control de procedibilidad de la Fase 1.3: no la repitas.**
- Verifica el umbral económico a partir del cual la asistencia letrada es preceptiva y los plazos máximos de duración de la actividad negociadora. **No los cites de memoria.**
- **Si detectas una versión posterior a la registrada, aplica la redacción vigente al documento que redactas en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin.
- Si la fuente no es accesible, usa la referencia local y advierte expresamente de que la verificación queda pendiente.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets

Envía un mensaje formal que contenga:
1. **Función del documento:** qué acredita, ante quién y con qué eficacia, con cita del precepto que lo ampara.
2. **Cómputo del plazo:** días consumidos, días restantes, fecha límite y efecto del MASC sobre la prescripción o la caducidad.
3. **Medio de remisión:** el que se empleará y por qué debe dejar constancia fehaciente del contenido, de la fecha y de la recepción.
4. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
5. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y verifica que contenga la identificación completa de ambas partes con domicilio a efectos de notificaciones, el objeto delimitado de la controversia, la fecha y la mención del precepto que ampara la actuación. Si falta alguno de esos elementos, adviértelo expresamente y propón la redacción que lo subsana.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission**: sustituye todos los datos ya conocidos por la escucha activa y por el formulario, y deja los pendientes como marcadores en mayúsculas entre dobles llaves. PROHIBIDO dejar archivos en blanco, con títulos solos o con resúmenes.
2. **Validación (`read_file`):** comprueba el volcado íntegro sobre la ruta exacta escrita.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (relato y decisiones)] ──> [Vista previa en texto plano]
      ──> [«¿Confirmamos esta sección?»] ──> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** los datos del requirente, los del requerido y los importes se piden en bloque, nunca dato a dato.
- **Confirmación agrupada por parte:** los datos de una misma persona se confirman todos juntos al final del bloque, no uno a uno.
- **Anuncio de sección visible** al pasar de una sección a la siguiente, en el mismo mensaje que la primera solicitud y sin pedir permiso aparte.
- **Validación de sentido, no solo de formato:** si un dato es absurdo, imposible o no responde a lo preguntado, dialógalo en el chat antes de volcarlo.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificar a quien requiere y a quien es requerido, con sus domicilios a efectos de notificaciones."
- Sección 2: "Identificadas las partes, corresponde delimitar con precisión el objeto de la controversia."
- Sección 3: "Delimitado el objeto, procede fijar la propuesta y el plazo que se concede para responder."
- Sección 4: "Fijada la propuesta, corresponde consignar el medio de remisión y la constancia de su recepción."
- Sección 5: "Por último, procede incorporar las menciones legales de confidencialidad, eficacia y reserva de acciones."

1. **Partes [dato objetivo, con validación crítica del domicilio].** Solicita en bloque mediante `slot_filling_request`: del requirente, nombre o razón social, documento de identidad o CIF, domicilio a efectos de notificaciones, teléfono y correo electrónico; del requerido, nombre o razón social, documento si consta y domicilio a efectos de notificaciones. **El domicilio es crítico:** un domicilio erróneo frustra la acreditación del intento y consume plazo. Si el requerido es persona jurídica, pide también el domicilio social y el del establecimiento con el que se contrató.
2. **Objeto de la controversia [negociación — el apartado que define el alcance].** Recaba el relato en el chat, ordenado y con fechas, y el importe si la pretensión es económica. Explica que lo que aquí se delimite marca el perímetro del requisito y, con ello, lo que podrá pedirse en la demanda sin un nuevo intento.
3. **Propuesta y plazo [negociación].** Formula la propuesta con precisión y fija el plazo de respuesta. Explica la diferencia entre una propuesta abierta y una oferta vinculante, y las consecuencias de cada una. En la oferta vinculante, el plazo y el contenido son esenciales: sin plazo cierto no hay oferta útil.
4. **Medio de remisión y constancia [dato objetivo].** Consigna el medio elegido y la fecha prevista de envío. Explica que el documento vale lo que valga su prueba, y que debe conservarse el justificante del contenido, de la fecha y de la recepción o del rechazo.
5. **Menciones legales de cierre [dato objetivo].** Incorpora la confidencialidad de lo actuado, la eficacia del documento, el efecto sobre los plazos y la reserva expresa de acciones judiciales si el intento resulta infructuoso.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Ampliar el objeto de la controversia o el desglose de importes.
3. Cambiar el plazo de respuesta o el medio de remisión.
4. Preparar el documento siguiente del itinerario (del requerimiento al acta, o del acta al acuerdo).
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado colegiado antes de su remisión o presentación.
- **Constancia fehaciente:** conservar el justificante del contenido, de la fecha de envío y de la recepción o del rechazo. Sin esa prueba, el intento no queda acreditado.
- **Efecto sobre los plazos:** informar del efecto que la actividad negociadora produce sobre la prescripción y sobre la caducidad, con la redacción vigente verificada, y del momento en que el cómputo se reanuda.
- **Terminación del intento:** explicar cuándo se entiende intentado sin acuerdo y por tanto cumplido el requisito, señaladamente por rechazo expreso, por incomparecencia injustificada a una citación válida y por transcurso del plazo máximo de duración sin acuerdo.
- **Aportación a la demanda:** el documento acreditativo debe acompañarse a la demanda; su falta determina la inadmisión, subsanable en los términos que la ley prevea.
- **Costas:** advertir de que la conducta de las partes durante el intento puede tener consecuencias en materia de costas, con el precepto verificado.
- **Confidencialidad:** lo actuado es confidencial y no puede aportarse al proceso fuera de lo que la ley permite.
- **Acuerdo alcanzado:** para su ejecución forzosa directa o su acceso al Registro, el acuerdo debe elevarse a escritura pública u homologarse judicialmente según corresponda.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación previa obligatoria.** Verificar en el BOE la versión consolidada vigente de la Ley Orgánica 1/2025 y de los preceptos reformados de la Ley 1/2000 antes de redactar. Sin verificación, no proceder.
2. **Cero invención de plazos, umbrales y preceptos.** No escribir ningún plazo, umbral económico ni número de artículo que no se haya verificado en esta sesión. Ante la imposibilidad de verificar, decirlo y no cifrar.
3. **La declaración responsable no es un atajo.** Solo procede ante una imposibilidad real y razonada. No ofrecerla como alternativa cómoda al intento, y advertir de las consecuencias de una declaración inveraz.
4. **No presentar como obligatorio lo que no lo es.** Si la materia está exceptuada, decirlo. Si el proceso ya está iniciado, el documento no cumple el requisito de procedibilidad.
5. **No asumir la posición de tercero neutral.** Esta skill redacta documentos por cuenta de una parte. No actúa como mediador ni como conciliador, no valora la posición de la contraria como si fuera imparcial y no emite la opinión de persona experta independiente.
6. **Oferta vinculante: advertencia previa e inexcusable.** Antes de redactarla, advertir de que obliga al oferente en sus propios términos si es aceptada en plazo, y de que la asistencia letrada es preceptiva por encima del umbral legal vigente.
7. **Acuerdo transaccional: control de disponibilidad.** No redactar acuerdos sobre materias indisponibles, ni sobre derechos de menores o de personas con discapacidad sin la intervención y las aprobaciones que la ley exija. Ante cualquier duda, detener y escalar.
8. **Confidencialidad como límite de redacción.** No incorporar al documento acreditativo el contenido de las propuestas ni de las concesiones hechas durante el intento más allá de lo que la ley permita hacer valer.
9. **Cero invención de datos.** No inventar nombres, domicilios, importes ni fechas. Los datos no aportados permanecen como marcador con su nombre propio de plantilla.
10. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real. Nunca se deja en el documento la descripción del tipo ni parte de ella.
