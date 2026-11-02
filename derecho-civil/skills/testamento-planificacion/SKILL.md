---
name: testamento-planificacion
title: Testamento y planificación sucesoria
i18n:
  en:
    name: will-and-estate-planning
    title: Will and estate planning
    description: >
      Prepares LIFETIME estate planning under the common **Civil Code**, which governs wills,
      forced shares and hereditary substitutions, in the consolidated version verified in the
      BOE: a draft open will to take to the notary (appointment of heirs, revocation of earlier
      dispositions, legacies, the betterment of Arts. 808 and 823, universal usufruct to the
      spouse with the Socini clause under Art. 820.3, ordinary substitution under Art. 774,
      fideicommissary substitution within the limit of Art. 781, disinheritance on the grounds
      of Arts. 849 to 857, provisions for a forced heir with a disability, executor and
      partitioner and powers under Art. 831), and an estate planning checklist with the
      documents to gather, decisions to make and tax warnings. It covers ONLY common civil law
      and ONLY the notarial open will. Do not use for regional civil law (Catalonia, Aragon,
      Navarre, Balearic Islands, Basque Country, Galicia), for holographic or closed wills, for
      an estate already opened after death, or to calculate inheritance tax.
description: >
  Prepara la planificación sucesoria EN VIDA conforme al **Código Civil común**, que regula el testamento, las legitimas y las sustituciones hereditarias, (BOE-A-1889-4763) en su versión
  consolidada vigente verificada en el BOE: minuta de testamento abierto para llevar a la notaría (institución
  de herederos, revocación de disposiciones anteriores, legados, mejora de los Arts. 808 y 823, usufructo
  universal al cónyuge articulado con cautela socini al amparo del Art. 820.3.º, sustitución vulgar del Art. 774,
  sustitución fideicomisaria dentro del límite del Art. 781, desheredación por causa tasada de los Arts. 849 a
  857, disposiciones a favor del legitimario en situación de discapacidad de los Arts. 808 in fine, 782 y 822,
  albacea contador-partidor y facultades del Art. 831), y checklist de planificación sucesoria con la
  documentación a reunir, las decisiones a tomar y los avisos fiscales. Cubre ÚNICAMENTE derecho civil común y
  ÚNICAMENTE el testamento abierto notarial. NO usar para vecindad civil foral o especial (Cataluña, Aragon,
  Navarra, Baleares, País Vasco, Galicia), para el testamento ológrafo o cerrado, para la herencia ya abierta
  tras el fallecimiento, ni para calcular el Impuesto sobre Sucesiones.
when_to_use: |
  - El usuario quiere otorgar testamento y necesita preparar su contenido antes de acudir al notario.
  - El usuario quiere saber a quién puede dejar sus bienes y cuánto puede repartir libremente.
  - El usuario quiere mejorar a un hijo, dejar un legado concreto o proteger a su cónyuge con un usufructo universal.
  - El usuario quiere desheredar a un legitimario y necesita saber si su motivo encaja en una causa legal.
  - El usuario tiene un hijo o legitimario en situación de discapacidad y quiere protegerlo dentro de lo que la ley permite.
  - El usuario quiere revisar o sustituir un testamento que ya otorgo.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - vecindad_civil: común / foral (Cataluña, Aragon, Navarra, Baleares, País Vasco, Galicia) / desconocida
  - alcance: testamento simple (institución de heredero y poco más) / testamento con planificación
  - datos_testador: nombre, DNI o NIE, fecha y lugar de nacimiento, filiación, estado civil, domicilio
  - datos_conyuge: nombre, DNI o NIE, régimen económico matrimonial, situación de separación legal o de hecho
  - legitimarios: descendientes, ascendientes y cónyuge; y si alguno se encuentra en situación de discapacidad
  - patrimonio: relación orientativa de inmuebles, activos financieros, muebles de valor, seguros, deudas y donaciones previas
  - decisiones: destino del tercio de libre disposición, mejora, legados, derechos del cónyuge, sustituciones, albacea, facultades del Art. 831
  - desheredacion: persona, causa legal alegada y hechos concretos en que se funda
  - datos_notaria: notaría designada, población, fecha prevista de otorgamiento
  - comunidad_autonoma_residencia: para la advertencia del Impuesto sobre Sucesiones
outputs:
  - minuta_testamento_abierto: minuta de testamento abierto para llevar a la notaría, markdown, DRAFT
  - checklist_planificacion_sucesoria: checklist de documentación, decisiones y avisos fiscales, markdown, DRAFT
references:
  - references/cc-desheredacion-causas-tasadas.md
  - references/cc-formas-revocacion-y-sustituciones.md
  - references/cc-legitimas-y-libre-disposicion.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/vecindad-civil-y-ambito-de-la-skill.md
assets:
  - assets/template-checklist-planificacion-sucesoria.md
  - assets/template-minuta-testamento-abierto.md
---

# Planificación Sucesoria en Vida: Minuta de Testamento Abierto

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
      "id": "vecindad_civil",
      "rationale": "Resolver V1: esta skill solo cubre el derecho común; la vecindad civil foral impone legítimas y figuras propias y obliga a detener el proceso.",
      "question": "¿Cuál es la vecindad civil del testador?",
      "options": [
        {"id": "comun", "label": "Común (Código Civil)"},
        {"id": "foral", "label": "Foral o especial: Cataluña, Aragón, Navarra, Baleares, País Vasco o Galicia"},
        {"id": "desconocida", "label": "No lo sé con certeza"}
      ]
    },
    {
      "id": "alcance",
      "rationale": "Resolver V2: el testamento simple usa solo la minuta; la planificación exige antes el checklist de decisiones sucesorias.",
      "question": "¿Qué alcance tiene el encargo?",
      "options": [
        {"id": "testamento_simple", "label": "Un testamento sencillo: institución de heredero y poco más"},
        {"id": "con_planificacion", "label": "Una planificación sucesoria: mejora, legados, sustituciones, usufructo del cónyuge"}
      ]
    },
    {
      "id": "legitimario_con_discapacidad",
      "rationale": "Resolver V3: activa los bloques de los artículos 808 in fine, 782 y 822 del Código Civil y hace obligatoria la sección de discapacidad.",
      "question": "¿Hay algún legitimario en situación de discapacidad?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    },
    {
      "id": "tipo_testamento",
      "rationale": "Resolver V4: solo el testamento abierto notarial está dentro del alcance; el ológrafo, el cerrado, el mancomunado y los pactos sucesorios quedan excluidos.",
      "question": "¿Qué tipo de testamento se pretende?",
      "options": [
        {"id": "abierto_notarial", "label": "Testamento abierto ante notario"},
        {"id": "otro_tipo", "label": "Ológrafo, cerrado, mancomunado o pacto sucesorio"}
      ]
    },
    {
      "id": "existe_conyuge",
      "rationale": "Resolver V5: la cuota legal usufructuaria del cónyuge viudo (artículo 834 del Código Civil) condiciona el reparto y el bloque de derechos del cónyuge de la minuta.",
      "question": "¿Está el testador casado, sin separación legal ni de hecho?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `vecindad_civil`
- `V2` — `alcance`
- `V3` — `legitimario_con_discapacidad`
- `V4` — `tipo_testamento`
- `V5` — `existe_conyuge`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalúa en este orden:

- Si **V1 = foral o desconocida** → **DETENER**. No se pregunta ningún otro vector, no se pide ningún dato del testador y **no se crea ningún documento**. Emite la advertencia fija de `references/vecindad-civil-y-ambito-de-la-skill.md`, apartado 6, y escala a un abogado o notario especializado en el derecho civil de ese territorio. Nunca redactes "una versión provisional" ni respondas cuanta legítima corresponde: en derecho foral no es la del Art. 808 CC.
- Si **V1 = común, V2 = testamento simple y V4 = abierto notarial** → **HOJA SIMPLE**: `assets/template-minuta-testamento-abierto.md`, con los bloques condicionales de mejora, legados, usufructo universal con cautela, fideicomiso, desheredación, facultades del Art. 831 y albacea DESACTIVADOS. Se activa la sustitución vulgar salvo rechazo expreso del cliente, y el bloque de derechos del cónyuge en su versión de cuota legal si V5 = si (existe cónyuge viudo).
- Si **V1 = común, V4 = abierto notarial y V2 = con planificación** → **HOJA PLANIFICACIÓN**: dos documentos, en este orden. Primero `assets/template-checklist-planificacion-sucesoria.md`, sobre el que se recogen el patrimonio y todas las decisiones; después, con las decisiones ya cerradas, `assets/template-minuta-testamento-abierto.md`. **Regla de reencaminamiento:** si el cliente respondió V2 = testamento_simple pero después manifiesta que quiere desheredar, mejorar, legar un bien concreto u ordenar un usufructo universal, reencamina en silencio a la HOJA PLANIFICACIÓN y continúa; no le anuncies el cambio de rama.
- Si **V3 = si** → activa en la hoja que corresponda los bloques de los Arts. 808 in fine, 782 y 822, y trata la sección de discapacidad de la Fase 5 como obligatoria, no como opcional.
- Si **V4 = otro tipo**, es decir, un **testamento ológrafo, cerrado o mancomunado**, o un **pacto sucesorio** → **DETENER**: fuera de alcance. El mancomunado es además nulo en derecho común (Art. 669 CC). Advertir y escalar.
- Si el causante **ya ha fallecido** y lo que se pretende es aceptar, repudiar o partir la herencia → **DETENER**: esta skill cubre la fase previa, en vida. Derivar a `herencia`.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **Capacidad para testar (Arts. 662, 663 y 665 CC):** si el testador es **menor de catorce años**, detener: no puede testar (Art. 663.1.º). Si el testador no puede conformar o expresar su voluntad ni aun con ayuda de medios o apoyos, detener y escalar (Art. 663.2.º). Si el cliente plantea dudas sobre la capacidad del testador, **no la valores**: el juicio de capacidad corresponde al Notario (Arts. 665, 685 y 696 CC), que la aprecia atendiendo al estado en que se halle al tiempo del otorgamiento (Art. 666). Advierte, recomienda anticipar la cuestión con la notaría y ofrece escalación. Tras la Ley 8/2021 ya no se exige el dictamen previo de dos facultativos.
- **Renuncia anticipada a la legítima (Art. 816 CC):** si el cliente propone que un hijo renuncie ahora a su legítima, o pactar con el su importe, **rechazar**: toda renuncia o transacción sobre la legítima futura es nula. Explicarlo y no recogerlo en ningún documento.
- **Gravamen o condición sobre la legítima (Art. 813 CC):** si el cliente quiere condicionar la legítima de un legitimario ("si se casa", "si no vende la casa", "si me cuida"), **rechazar la cláusula**, explicar que se tendría por no puesta y proponer la alternativa válida: destinar a esa persona solo la legítima estricta y dirigir la mejora y el tercio de libre disposición a quien decida.
- **Desheredación sin causa legal (Arts. 849 a 855 CC):** si el cliente ha manifestado que desea desheredar, contrastar el motivo con las causas tasadas antes de redactar nada. Si no encaja, aplicar el Guardrail 5. Nunca redactar la cláusula "por si acaso".
- **Caudal compuesto esencialmente por un bien indivisible:** si del inventario resulta que la vivienda u otro bien no divisible absorbe la práctica totalidad del patrimonio y el testador quiere adjudicarlo a alguno de sus hijos, **no lo articules como legado ni como atribución de cuota sin más**: el resto del caudal no bastara para cubrir la legítima de los demás y la disposición sería inoficiosa. Advierte y ofrece las dos vías de la Fase 5, sección 5: el pago en metálico de los Arts. 841 a 847 CC, que exige autorización expresa en el testamento, o la adjudicación en la partición con abono del exceso en dinero del Art. 1062 CC.
- **Legado de bien ganancial o no privativo:** si el testador quiere legar un bien concreto que no le pertenece íntegramente, advertir del Art. 864 CC (el legado se entiende limitado a su parte o derecho) y de la necesidad de liquidar previamente la sociedad de gananciales.
- **Patrimonio empresarial, bienes en el extranjero o elemento internacional:** escalar antes de redactar (Reglamento UE 650/2012; Art. 1056.2 CC para la empresa familiar). No redactar la professio iuris ni la partición del Art. 1056.
- **Testador con testamento anterior:** no dar por revocado nada de memoria. La revocación se ordena expresamente en la cláusula PRIMERA (Arts. 738 y 739 CC).

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 662 a 743 del Código Civil (capacidad y forma del testamento abierto ante Notario, Art. 694 CC); Arts. 806 a 822 CC (legítimas de hijos y descendientes, padres y cónyuge viudo); Arts. 823 a 833 CC (mejora); Art. 848 CC (desheredación taxativa); y Art. 858 CC (legados).
2. **Orientación Legal del Caso:**

**Informa la norma aplicable y el valor del documento.** Textos fijos por hoja:
   - SIMPLE: "A su caso le resulta de aplicación el Código Civil común. Su testamento se otorgara en forma de testamento abierto ante Notario, conforme a los artículos 694 a 699 del Código Civil, y la legítima de sus herederos forzosos se rige por los artículos 806 a 808. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - PLANIFICACIÓN: "A su caso le resulta de aplicación el Código Civil común. Su testamento se otorgara en forma de testamento abierto ante Notario, conforme a los artículos 694 a 699 del Código Civil; la legítima de sus herederos forzosos se rige por los artículos 806 a 808, la mejora por los artículos 823 y siguientes y los derechos de su cónyuge por los artículos 834 y siguientes. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - **Si V5 = no (el testador no está casado, o está separado legalmente o de hecho), suprime de ese texto la mención final a los derechos del cónyuge**, que no concurren, y cierra la enumeración en la mejora. No hables al cliente de un cónyuge que no existe.
   - En ambas hojas, añadir esta advertencia fija: "Debe tener presente desde ahora que el documento que vamos a preparar **no es un testamento**: es una minuta destinada a la notaría. Solo produce efectos el testamento otorgado ante Notario, y es el propio Notario quien lo redacta con arreglo a la voluntad que usted le exprese, conforme al artículo 695 del Código Civil."
   - Si V3 = si, añadir además: "Al encontrarse uno de sus legitimarios en situación de discapacidad, dispone usted de un margen de planificación más amplio del ordinario, conforme a los artículos 808 y 822 del Código Civil en la redacción dada por la Ley 8/2021."

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

### Hoja de Ruta de Secciones y Cláusulas Condicionales

**Anuncio de sección y encadenamiento:** al terminar una sección y confirmar su edición en disco, emite en ese mismo turno el anuncio fijo de la sección que se abre y lanza de inmediato su formulario `slot_filling_request` (si es grupo de datos) o su planteamiento en chat (si es negociación). No pidas permiso para pasar de sección: informa y continúa en el mismo turno. Los anuncios nombran la sección SUSTANTIVA del documento, nunca la mecánica interna. La vista previa y la confirmación siempre van en el chat. Las decisiones marcadas `[negociación]` se explican y se confirman una a una en el chat.

**Validación de sentido, no solo de formato.** No aceptes mecánicamente cualquier respuesta. Si un dato es absurdo, imposible o no responde a lo preguntado (un DNI con forma de nombre, una fecha de nacimiento futura, un "hijo" que resulta ser un sobrino), no lo escribas: señala por qué no encaja y pide aclaración.

**Puntos `[negociación]`.** En ellos no te límites a registrar la respuesta: explica primero el régimen legal por defecto y las consecuencias concretas de cada opción, y solo después pide la decisión. Confirma que el cliente lo ha entendido antes de escribirlo. Los puntos `[dato objetivo]` se limitan a recoger el dato.

---

### Secciones — HOJA SIMPLE (`minuta-testamento-abierto.md`)

1. **Testador** `[dato objetivo — búsqueda prioritaria con slot_filling_request si es nuevo, volcado directo a disco per REG-CLI-04]`. Anuncio fijo: "Comenzamos por su identificación como testador." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre y apellidos; b) DNI o NIE; c) fecha de nacimiento; d) lugar de nacimiento; e) nombres del padre y de la madre; f) estado civil; g) domicilio. **La vecindad civil ya está resuelta: no la vuelvas a preguntar.** El estado civil también está parcialmente resuelto: si V5 = si, escribe "casado" sin preguntarlo, y si V5 = no, formula el sub-apartado f) solo para precisar cuál es (soltero, viudo, divorciado o separado). Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Conforme a `REG-CLI-04`, vuelca de inmediato al documento con `edit_file` (o ya volcado en `create_file`) sin confirmación en chat, sustituyendo exhaustivamente los nombres en todas sus apariciones a lo largo del documento (título/encabezado H1, comparecencia y firmas; use `replace_all: true` o ediciones que cubran las 3 ubicaciones).
2. **Cónyuge** `[dato objetivo — búsqueda prioritaria con search_clients, recogida en lote con slot_filling_request si es nuevo, volcado directo a disco per REG-CLI-04; solo si V5 = si]`. Anuncio fijo: "Pasamos a identificar a su cónyuge." Invoca `search_clients` prioritariamente. Si es nuevo, solicita en bloque vía `slot_filling_request`: a) nombre y apellidos; b) DNI o NIE; c) régimen económico matrimonial. Si es nuevo cliente, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca de inmediato a disco con `edit_file` sin confirmación en chat per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones (título H1, comparecencia y firmas).
3. **Legitimarios** `[dato objetivo con validación — búsqueda prioritaria con search_clients, recogida en lote con slot_filling_request si son nuevos, volcado directo a disco per REG-CLI-04]`. Anuncio fijo: "Relacionamos ahora a quienes la ley reconoce como herederos forzosos." Solicita de una vez vía `slot_filling_request` la relación de descendientes (nombre y apellidos, y DNI/NIE de cada uno) o en su caso ascendientes vivos. **Validación obligatoria:** advierte de que deben relacionarse TODOS los descendientes, reciban o no atribución, porque omitir a uno provoca la preterición del artículo 814 del Código Civil, que anula la institución de herederos. Si son nuevos clientes, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca directamente al documento con `edit_file` sin confirmación en chat per `REG-CLI-04`.
4. **Naturaleza del documento y revocación de disposiciones anteriores** `[negociación]`. Anuncio fijo: "Antes de entrar en el contenido, conviene fijar el valor de este documento y el destino de sus testamentos anteriores." Explica, antes de pedir nada: que esta minuta no es un testamento y solo produce efectos el otorgado ante Notario (artículos 687 y 695 del Código Civil); que **todas las disposiciones testamentarias son esencialmente revocables** (artículo 737), de modo que lo que decida hoy no le ata y puede sustituirlo en cualquier momento por otro testamento posterior otorgado con las mismas solemnidades (artículos 738 y 739); y que otorgar testamento **no limita su libertad de disponer de sus bienes en vida**. Pregunta después si ha otorgado testamentos anteriores y confirma la revocación expresa de todos ellos.
5. **Institución de herederos** `[negociación — PUNTO CLAVE]`. Anuncio fijo: "Pasamos al núcleo del testamento: la designación de sus herederos." **Explica ANTES de pedir ninguna decisión**, porque es el punto que más sorprende al cliente: con descendientes, dos de cada tres partes de la herencia son legítima y están reservadas por ley a los hijos o descendientes (artículo 808 del Código Civil); de esas dos, una es de legítima estricta y se reparte por partes iguales, y la otra es el tercio de mejora, que solo puede ir a hijos o descendientes pero permite elegir a cuál; **solo un tercio es realmente de libre disposición**. Añade que la legítima es intangible: no cabe imponer sobre ella condición, plazo ni gravamen alguno (artículo 813) y ningún hijo puede renunciar a ella en vida del testador (artículo 816). Solo después de que el cliente confirme que lo ha entendido, pide, en turnos separados: a) a quién instituye herederos; b) en que proporción. Verifica que el reparto respeta la legítima antes de escribirlo.
6. **Derechos del cónyuge viudo** `[negociación; solo si V5 = si]`. Anuncio fijo: "Determinamos ahora los derechos que corresponderán a su cónyuge." Explica el régimen por defecto según con quién concurra: usufructo del tercio de mejora con descendientes (artículo 834), de la mitad con ascendientes y sin descendientes (artículo 837), y de dos tercios sin unos ni otros (artículo 838). Pregunta si desea dejarlo así o ampliar la protección del cónyuge; si quiere ampliarla, aplica el punto de negociación de la cautela socini descrito en la sección 10 de la HOJA PLANIFICACIÓN y reencamina el caso a esa hoja.
7. **Sustitución vulgar** `[negociación]`. Anuncio fijo: "Valoramos ahora que debe ocurrir si alguno de sus herederos no llega a heredar." Explica el artículo 774 del Código Civil: la sustitución vulgar designa quién ocupa el lugar del heredero que fallece antes que el testador, renuncia o no puede aceptar; sin ella, esa porción se rige por las reglas legales supletorias de acrecimiento y de sucesión intestada, con un resultado que puede no coincidir con lo que el testador quiere. Recomienda ordenarla y pregunta a quién designa como sustitutos.
8. **Instrucciones para la notaría** `[dato objetivo — recogida con slot_filling_request, confirmación en chat]`. Anuncio fijo: "Cerramos con las instrucciones para la notaría." Solicita en bloque vía `slot_filling_request`: a) notaría a la que se dirigirá; b) población; c) fecha prevista de otorgamiento; d) documentación que aportará el testador; e) si el testador puede firmar y leer sin dificultad (artículos 695 y 697). Vista previa y confirmación en chat.
9. **Aviso fiscal** `[negociación — informativo]`. Anuncio fijo: "Por último, debe conocer las consecuencias fiscales de lo que acabamos de ordenar." Explica que el Impuesto sobre Sucesiones y Donaciones está cedido a las comunidades autónomas, que sus reducciones y bonificaciones varían de forma muy relevante entre ellas y que **esta herramienta no lo calcula ni lo estima**. Pregunta la comunidad autónoma de residencia habitual del testador y recomienda contrastar la planificación con un asesor fiscal de esa comunidad antes de acudir a la notaría.

---

### Secciones — HOJA PLANIFICACIÓN

**Documento 1: `checklist-planificacion-sucesoria.md`** (secciones 1 a 13)

1. **Documentación a reunir** `[dato objetivo]`. Anuncio fijo: "Comenzamos por la documentación que deberá reunir antes de acudir a la notaría." Repasa la lista del asset y pregunta qué documentos no tiene todavía, para dejarlos anotados como pendientes.
2. **Mapa familiar y legitimarios** `[dato objetivo con validación — búsqueda prioritaria con search_clients, recogida en lote con slot_filling_request si son nuevos, volcado directo a disco per REG-CLI-04]`. Anuncio fijo: "Pasamos a fijar quiénes son sus herederos forzosos." Solicita de una vez vía `slot_filling_request` la relación de legitimarios (nombre y apellidos, DNI/NIE de cada descendiente o ascendiente y cónyuge). Misma validación de la preterición del artículo 814 que en la HOJA SIMPLE. Si son nuevos clientes, resuelve `restricted_human_in_the_loop_request` (`REG-CLI-03`). Vuelca directamente al documento con `edit_file` sin confirmación en chat per `REG-CLI-04`.
3. **Inventario orientativo del patrimonio** `[dato objetivo — recogida en lote con slot_filling_request, confirmación en chat]`. Anuncio fijo: "Relacionamos ahora, de forma orientativa, su patrimonio." Solicita en bloque vía `slot_filling_request`: a) inmuebles (dirección y referencia catastral); b) cuentas, fondos y valores; c) vehículos y muebles de valor; d) seguros de vida y planes de previsión; e) participaciones societarias; f) deudas y cargas; g) donaciones ya realizadas en vida. Advierte en el apartado g) que las donaciones se computan para el cálculo de la legítima y se imputan conforme a los artículos 818 y 819 del Código Civil: anticipar bienes en vida no saca esos bienes del cálculo. Si aparece patrimonio empresarial o bienes en el extranjero, aplica la escalación correspondiente antes de continuar. Vista previa y confirmación en chat.
4. **Legítima y margen real de libre disposición** `[negociación — PUNTO CLAVE]`. Anuncio fijo: "Antes de tomar ninguna decisión, debe conocer que parte de su patrimonio puede repartir libremente." Misma explicación que la sección 5 de la HOJA SIMPLE (tercios del artículo 808, intangibilidad del 813, nulidad de la renuncia anticipada del 816), aplicada ya a los legitimarios concretos identificados en la sección 2: calcula y muestra qué corresponde a legítima estricta, que al tercio de mejora y que al de libre disposición. Confirma que el cliente lo ha entendido antes de pasar a las decisiones. Si el cliente reacciona proponiendo condicionar la legítima o pactar su renuncia, aplica la validación de presupuestos y ofrece la alternativa válida.
5. **Institución de herederos y reparto del caudal** `[negociación — PUNTO CLAVE]`. Anuncio fijo: "Pasamos al núcleo del testamento: la designación de sus herederos." Es la cláusula que la minuta contiene siempre y sin la cual el testamento no cumple su función: **nunca la des por supuesta ni la deduzcas de las decisiones sobre la mejora o los legados**. Partiendo de los tercios ya calculados en la sección 4, pide en turnos separados: a) a quién instituye herederos; b) en que proporción se les llama, comprobando antes de escribirla que ningún legitimario recibe menos de su legítima estricta. Si el testador quiere dejar a un legitimario **solo lo mínimo legal**, explícale que la fórmula válida no es apartarlo del testamento —lo que provocaría la preterición del artículo 814— sino instituirlo también heredero en la porción que cubra exactamente su legítima estricta, y recógelo así. c) Si del inventario de la sección 3 resulta que el caudal se compone esencialmente de uno o varios **bienes indivisibles** (típicamente, la vivienda) y el testador quiere adjudicarlos a alguno de sus hijos, adviértele de que la cuota de los demás no podrá pagarse con los bienes que quedan y explícale las dos vías: ordenar la adjudicación del bien a esos hijos disponiendo que la porción de los restantes legitimarios **se pague en metálico**, al amparo del artículo 841 del Código Civil, que exige autorización expresa en el testamento al contador-partidor, comunicar la decisión a los perceptores dentro del año siguiente a la apertura de la sucesión y pagar en el plazo de otro año más (artículo 844), fijando la suma por el valor de los bienes al tiempo de la liquidación (artículo 847) y con aprobación notarial o del Letrado de la Administración de Justicia salvo confirmación expresa de todos los hijos (artículo 843); o dejar la cuestión a la partición, donde el bien indivisible se adjudica a uno abonando el exceso en dinero, bastando que un solo heredero pida la venta en pública subasta para que así se haga (artículo 1062). Adviértele además de que el hijo obligado a pagar en metálico puede exigir que esa cuota se satisfaga en bienes de la herencia (artículo 842). Pregunta cuál de las dos vías prefiere.
6. **Destino del tercio de libre disposición y legados** `[negociación]`. Anuncio fijo: "Determinamos el destino del tercio de libre disposición y los legados que desee ordenar." Explica que este tercio puede ir a cualquier persona, incluso ajena a la familia, y que los legados de bienes concretos se imputan a el y no pueden perjudicar la legítima (artículos 813, 817 y 820). Advierte del artículo 869: si el bien legado se vende o se transforma, el legado queda sin efecto. Pide, en turnos separados: a) destino del tercio de libre disposición; b) relación de legados, identificando cada bien de forma inequívoca y a su beneficiario.
7. **Mejora** `[negociación]`. Anuncio fijo: "Valoramos si desea mejorar a alguno de sus hijos o descendientes." Explica que el tercio de mejora solo puede ir a hijos o descendientes, que si no se ordena nada se reparte entre los legitimarios como legítima, y que **la mejora debe declararse expresamente** (artículos 823, 825 y 828): decir "le dejo la casa" no mejora a nadie. Pregunta si desea mejorar y a quién, y en que consiste la mejora.
8. **Legitimario en situación de discapacidad** `[negociación; obligatoria si V3 = si]`. Anuncio fijo: "Abordamos las disposiciones que la ley permite a favor del legitimario en situación de discapacidad." Explica las dos herramientas de la Ley 8/2021: la del **artículo 808, último párrafo**, que permite disponer a su favor de la legítima estricta de los demás legitimarios, quedando lo recibido gravado con sustitución fideicomisaria de residuo a favor de los perjudicados y correspondiendo al hijo que impugne acreditar que no concurre causa que lo justifique; y la del **artículo 822**, el derecho de habitación sobre la vivienda habitual, que no se computa para el cálculo de las legitimas si al fallecer ambos convivían en ella, es intransmisible y se atribuye además por ministerio de la ley salvo que el testador lo excluya expresamente. Pregunta, en turnos separados: a) si desea disponer a su favor de la legítima estricta de los demás; b) si desea legarle el derecho de habitación sobre la vivienda habitual, y en ese caso su dirección completa. Advierte de que el gravamen del artículo 808 es una de las pocas excepciones a la intangibilidad de la legítima y de que la acreditación concreta de la situación de discapacidad deberá confirmarse con la notaría.
9. **Desheredación** `[negociación — crítica; solo si el cliente desea desheredar]`. Anuncio fijo: "Abordamos la desheredación que desea ordenar." Procedimiento obligatorio, en este orden:
   a) Pregunta a quién desea desheredar y por qué motivo, en prosa.
   b) **Contrasta el motivo con las causas tasadas** de los artículos 852 a 855 del Código Civil, usando `references/cc-desheredacion-causas-tasadas.md`. No lo des por bueno por aproximación.
   c) **Si el motivo NO encaja en ninguna causa legal:** dilo con claridad, sin rodeos. Explica que la desheredación sin causa legal, o por causa que no se pruebe, **anula la institución de heredero en cuanto perjudique al desheredado** (artículo 851), de modo que la cláusula no solo no surtiría efecto sino que abriría un pleito entre los herederos. Ofrece la alternativa válida y sin riesgo: reducir a esa persona a su legítima estricta, destinando la mejora y el tercio de libre disposición a quien el cliente decida. Si el cliente la acepta, se recoge en el bloque **"Atribución limitada a la legítima estricta"** del asset de la minuta, y el legitimario sigue figurando como heredero instituido en la porción que cubra su legítima, para no incurrir en la preterición del artículo 814. **No redactes la cláusula de desheredación.** Si el cliente insiste, escala.
   d) **Si el motivo SI encaja:** advierte igualmente, antes de redactar, de las tres consecuencias que suelen ignorarse: que la prueba de la causa corresponderá a los herederos favorecidos si el desheredado la niega (artículo 850), y que el testador ya no estará para probarla; que una reconciliación posterior deja sin efecto la desheredación (artículo 856); y que **los hijos o descendientes del desheredado ocupan su lugar y conservan la legítima** (artículo 857), de modo que la desheredación no aparta a esa rama de la familia. Pide después: el artículo y la causa legal concreta, y una descripción de los hechos en que se funda, porque el artículo 849 exige expresar la causa en el testamento. Adopta siempre la posición conservadora.
10. **Derechos del cónyuge y cautela socini** `[negociación; solo si V5 = si]`. Anuncio fijo: "Determinamos los derechos que corresponderán a su cónyuge." Explica en este orden:
   - El régimen por defecto: usufructo del tercio de mejora con descendientes (artículo 834), de la mitad con ascendientes (artículo 837), de dos tercios sin descendientes ni ascendientes (artículo 838).
   - Que muchos testadores quieren dejar al cónyuge el usufructo de **toda** la herencia para que no dependa económicamente de los hijos, pero que un usufructo universal grava también la legítima estricta, y el artículo 813 lo prohíbe.
   - **Cómo funciona la cautela socini**, con su dilema explícito: se ordena el usufructo universal acompañado de una opción para cada hijo, amparada en el artículo 820, número 3.º, del Código Civil. El hijo elige entre aceptar el usufructo, recibiendo su parte completa pero en nuda propiedad y gravada de por vida, o no aceptarlo, recibiendo entonces **solo su legítima estricta**, libre y de inmediato. Cobra más y más tarde, o menos y ya. La cláusula no vulnera la legítima: la respeta y pone al hijo ante una elección incómoda.
   - La posición conservadora: es una cláusula de uso extendido pero **no tipificada en el Código Civil**, construida por la práctica notarial y la jurisprudencia; si está mal redactada es susceptible de litigio, y su redacción definitiva corresponde al Notario.
   Pregunta después cuál de las dos opciones prefiere. Si elige el usufructo universal, confirma expresamente que ha entendido el dilema que plantea a sus hijos antes de escribirlo.
11. **Sustituciones** `[negociación]`. Anuncio fijo: "Valoramos ahora que debe ocurrir si alguno de sus herederos no llega a heredar." Misma explicación de la sustitución vulgar que en la HOJA SIMPLE (artículo 774). Si además el cliente quiere que los bienes pasen después a otra persona (típicamente, del cónyuge a los nietos), explica la sustitución fideicomisaria: válida solo hasta el segundo grado o a favor de personas que vivan al fallecer el testador (artículo 781), de llamamiento necesariamente expreso (artículo 783), y que **nunca puede gravar la legítima** salvo el supuesto del legitimario con discapacidad del artículo 808 (artículo 782). Adviértele de que su nulidad no arrastra la institución, que se mantiene (artículo 786). Pide los sustitutos vulgares y, en su caso, el fiduciario, el fideicomisario y el objeto del fideicomiso.
12. **Albacea contador-partidor y facultades al cónyuge** `[negociación]`. Anuncio fijo: "Valoramos si conviene designar quien ejecute y reparta la herencia." Explica que sin albacea contador-partidor la partición exige el acuerdo unánime de todos los herederos, y que designarlo evita el bloqueo. Explica además, si hay cónyuge e hijos comunes, las facultades del artículo 831 del Código Civil: permiten que el cónyuge sobreviviente mejore y adjudique entre los hijos o descendientes comunes después del fallecimiento, con un plazo supletorio de dos años, y que **cesan** si pasa a ulterior matrimonio o relación análoga o tiene un hijo no común, salvo disposición contraria. Pregunta, en turnos separados: a) si designa albacea contador-partidor, y en su caso su nombre, DNI y plazo; b) si confiere al cónyuge las facultades del artículo 831 y con que plazo.
13. **Aviso fiscal** `[negociación — informativo]`. Anuncio fijo: "Antes de cerrar la planificación, debe conocer sus consecuencias fiscales." Explica que el Impuesto sobre Sucesiones y Donaciones esta cedido a las comunidades autónomas, que las reducciones y bonificaciones varían de forma muy relevante entre ellas de modo que una misma planificación puede tener un coste muy distinto según la comunidad aplicable, y que **esta herramienta no lo calcula ni lo estima**. Advierte además de la plusvalía municipal si hay inmuebles urbanos, del régimen propio de los seguros de vida y de que las donaciones en vida no son fiscalmente neutras. Pregunta la comunidad autónoma de residencia habitual del testador y recomienda contrastar la planificación con un asesor fiscal de esa comunidad.

**Cierre del checklist.** Completada la sección 13, aplica el ciclo de creación de la Fase 3 sobre el segundo documento: crea `minuta-testamento-abierto.md` volcando todas las decisiones confirmadas, verifica prioritariamente en `# WORKSPACE ACTIVE DOCUMENTS` (o mediante `read_file` en caso extremo), confirma la ruta absoluta y, en la misma respuesta, emite el anuncio de la sección 14 y su primera pregunta.

**Documento 2: `minuta-testamento-abierto.md`** (secciones 14 a 17)

14. **Testador** `[dato objetivo — volcado directo a disco per REG-CLI-04]`. Anuncio fijo: "Comenzamos por su identificación como testador." Mismos sub-apartados que la sección 1 de la HOJA SIMPLE. Omite los que ya conozcas y vuelca directamente a disco per `REG-CLI-04` sin turno de confirmación en chat.
15. **Cónyuge** `[dato objetivo — volcado directo a disco per REG-CLI-04; solo si V5 = si]`. Anuncio fijo: "Pasamos a identificar a su cónyuge." Mismos sub-apartados que la sección 2 de la HOJA SIMPLE. Vuelca directamente a disco per `REG-CLI-04` sin turno de confirmación en chat.
16. **Naturaleza del documento y revocación de disposiciones anteriores** `[negociación]`. Anuncio fijo: "Antes de cerrar el contenido, conviene fijar el valor de este documento y el destino de sus testamentos anteriores." Mismo contenido que la sección 4 de la HOJA SIMPLE.
17. **Instrucciones para la notaría** `[dato objetivo]`. Anuncio fijo: "Cerramos con las instrucciones para la notaría." Mismos sub-apartados que la sección 8 de la HOJA SIMPLE.

---

### Numeración final de las cláusulas (obligatorio antes del bucle final)

Cuando todas las secciones estén completadas y todos los bloques condicionales decididos, y **antes** de mostrar el menú del bucle de realimentación:

1. Consulta la minuta prioritariamente en `# WORKSPACE ACTIVE DOCUMENTS` (o mediante `read_file` en caso extremo).
2. Sustituye cada placeholder `{{ORDINAL_...}}` por su ordinal en letra, **correlativo y sin saltos**, siguiendo el orden en que las cláusulas aparecen realmente en el documento. La revocación es siempre PRIMERA.
3. Verifica prioritariamente en `# WORKSPACE ACTIVE DOCUMENTS` (o mediante `read_file` en caso extremo) que no queda ningún placeholder de ordinal sin resolver, ningún ordinal repetido y ninguna cláusula sin encabezado.
4. Verifica en la misma lectura que el documento no contiene ningún comentario HTML (`<!-- ... -->`) ni ningún bloque de una rama descartada.

Esta numeración se rehace cada vez que el bucle de realimentación añada o elimine una cláusula condicional.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: una disposición por cláusula, voz activa con el testador como sujeto, personas y bienes identificados de forma inequívoca, sin latinismos ni fórmulas huecas, mejora declarada expresamente, causa legal expresada en toda desheredación, y nada impuesto sobre la legítima estricta.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre el Código Civil en el BOE antes de redactar (Fase 2). Sin verificación, no proceder. Si se detecta una versión posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario.
2. **La vecindad civil es el filtro de alcance.** Si es foral o especial, o el testador no la conoce con seguridad, detener de inmediato y escalar (Arts. 14 y 16 CC). No redactar, no adaptar, no estimar legitimas. Esta skill solo cubre derecho civil común.
3. **La legítima es intangible** (Arts. 806, 808 y 813 CC). Nunca redactar una cláusula que la reduzca, la condicione, la someta a plazo o la grave, fuera de las excepciones expresas de los Arts. 782, 808 y del usufructo del viudo. Si el usuario lo pide, rechazar la instrucción, explicar que la cláusula se tendría por no puesta y proponer la alternativa válida.
4. **Nulidad de la renuncia anticipada** (Art. 816 CC). Nunca documentar la renuncia de un legitimario a su legítima futura ni un pacto sobre ella con el causante en vida.
5. **Desheredación solo por causa tasada** (Arts. 849 a 855 CC). Contrastar siempre el motivo con la lista legal. Si no encaja, no redactar la cláusula, explicar el efecto del Art. 851 y ofrecer la alternativa de reducir a la legítima estricta. Si encaja, advertir del Art. 850 (la prueba corresponde a los herederos favorecidos), del Art. 856 (la reconciliación la deja sin efecto) y del Art. 857 (los descendientes del desheredado conservan la legítima). Posición conservadora siempre.
6. **Relacionar a todos los legitimarios**, reciban o no atribución, para evitar la preterición del Art. 814 CC, que anula la institución de herederos.
7. **La minuta no es un testamento.** Nunca presentarla como tal ni dar a entender que produce efectos. Solo el testamento otorgado ante Notario con las formalidades de los Arts. 694 a 699 CC vale como tal (Art. 687), y es el Notario quien lo redacta (Art. 695).
8. **El juicio de capacidad corresponde al Notario** (Arts. 665, 685 y 696 CC). La skill nunca valora ni certifica la capacidad del testador: si hay dudas, advierte, recomienda anticiparlo con la notaría y escala.
9. **La mejora debe ser expresa** (Arts. 825 y 828 CC). Nunca dar por mejorado a un hijo por el hecho de dejarle un bien concreto.
10. **La sustitución fideicomisaria no puede gravar la legítima** salvo el supuesto del legitimario con discapacidad del Art. 808 (Art. 782 CC), y no puede pasar del segundo grado o de personas que vivan al fallecer el testador (Art. 781).
11. **Esta skill no calcula el Impuesto sobre Sucesiones y Donaciones** ni valora la fiscalidad de las disposiciones. Advertir siempre de que es un tributo autonómico con consecuencias muy distintas según la comunidad, y no dar cifras ni estimaciones.
12. Nunca inventar datos, cuantías, bienes, fechas ni jurisprudencia. Nunca citar un artículo sin haberlo verificado en la Fase 2. Los campos no proporcionados quedan como `{{DATO}}` con el nombre propio del placeholder del asset.
13. **La institución de heredero se pregunta siempre y de forma expresa**, en las dos hojas. Nunca deducirla de la mejora, de los legados o del reparto de un bien concreto: sin ella el testamento no dispone de la herencia y se abre la sucesión intestada respecto de lo no dispuesto (Art. 912.2.º CC).
14. **Bien indivisible que absorbe el caudal.** Adjudicar la vivienda a algunos legitimarios solo es viable ordenando el pago en metálico de la porción de los demás (Arts. 841 a 847 CC, con autorización expresa en el testamento) o remitiendo la cuestión a la partición (Art. 1062 CC). Nunca darlo por resuelto con un legado del inmueble cuando el resto del caudal no cubre la legítima.
15. El documento escrito en disco lleva CERO comentarios HTML y CERO placeholders de ordinal sin resolver al cerrar.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para testadores de vecindad civil foral o especial (Cataluña, Aragon, Navarra, Illes Balears, País Vasco, Galicia): **detener y escalar**. El régimen de legitimas y de sucesión es distinto y esta skill no lo cubre.
- No usar para el testamento ológrafo (Art. 688 CC), el cerrado (Art. 706) ni los testamentos especiales y supuestos excepcionales del Código: fuera de alcance.
- No usar para el testamento mancomunado ni para pactos sucesorios: el mancomunado es nulo en derecho común (Art. 669 CC).
- No usar para la herencia ya abierta tras el fallecimiento —aceptación, renuncia, interpelación al heredero silente, cuaderno particional o división judicial—: derivar a `herencia`.
- No usar para tramitar el acta notarial de declaración de herederos abintestato ni para el otorgamiento en sí: son actuaciones notariales.
- No usar para calcular ni liquidar el Impuesto sobre Sucesiones y Donaciones ni la plusvalía municipal.
- No usar para impugnar un testamento ajeno, reclamar la legítima, ejercitar la acción de complemento del Art. 815 CC o la reducción de disposiciones inoficiosas del Art. 817: son posiciones litigiosas, fuera de alcance. Derivar a derivación formal.
- No usar para la planificación de patrimonio empresarial o societario, ni para sucesiones con elemento internacional: escalar.
- No usar para valorar la capacidad del testador: corresponde al Notario.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
