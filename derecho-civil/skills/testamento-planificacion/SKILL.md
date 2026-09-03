---
name: testamento-planificacion
description: >
  Prepara la planificacion sucesoria EN VIDA conforme al Codigo Civil comun (BOE-A-1889-4763) en su version
  consolidada vigente verificada en el BOE: minuta de testamento abierto para llevar a la notaria (institucion
  de herederos, revocacion de disposiciones anteriores, legados, mejora de los Arts. 808 y 823, usufructo
  universal al conyuge articulado con cautela socini al amparo del Art. 820.3.º, sustitucion vulgar del Art. 774,
  sustitucion fideicomisaria dentro del limite del Art. 781, desheredacion por causa tasada de los Arts. 849 a
  857, disposiciones a favor del legitimario en situacion de discapacidad de los Arts. 808 in fine, 782 y 822,
  albacea contador-partidor y facultades del Art. 831), y checklist de planificacion sucesoria con la
  documentacion a reunir, las decisiones a tomar y los avisos fiscales. Cubre UNICAMENTE derecho civil comun y
  UNICAMENTE el testamento abierto notarial. NO usar para vecindad civil foral o especial (Cataluna, Aragon,
  Navarra, Baleares, Pais Vasco, Galicia), para el testamento olografo o cerrado, para la herencia ya abierta
  tras el fallecimiento, ni para calcular el Impuesto sobre Sucesiones.
when_to_use: |
  - El usuario quiere otorgar testamento y necesita preparar su contenido antes de acudir al notario.
  - El usuario quiere saber a quien puede dejar sus bienes y cuanto puede repartir libremente.
  - El usuario quiere mejorar a un hijo, dejar un legado concreto o proteger a su conyuge con un usufructo universal.
  - El usuario quiere desheredar a un legitimario y necesita saber si su motivo encaja en una causa legal.
  - El usuario tiene un hijo o legitimario en situacion de discapacidad y quiere protegerlo dentro de lo que la ley permite.
  - El usuario quiere revisar o sustituir un testamento que ya otorgo.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - vecindad_civil: comun / foral (Cataluna, Aragon, Navarra, Baleares, Pais Vasco, Galicia) / desconocida
  - alcance: testamento simple (institucion de heredero y poco mas) / testamento con planificacion
  - datos_testador: nombre, DNI o NIE, fecha y lugar de nacimiento, filiacion, estado civil, domicilio
  - datos_conyuge: nombre, DNI o NIE, regimen economico matrimonial, situacion de separacion legal o de hecho
  - legitimarios: descendientes, ascendientes y conyuge; y si alguno se encuentra en situacion de discapacidad
  - patrimonio: relacion orientativa de inmuebles, activos financieros, muebles de valor, seguros, deudas y donaciones previas
  - decisiones: destino del tercio de libre disposicion, mejora, legados, derechos del conyuge, sustituciones, albacea, facultades del Art. 831
  - desheredacion: persona, causa legal alegada y hechos concretos en que se funda
  - datos_notaria: notaria designada, poblacion, fecha prevista de otorgamiento
  - comunidad_autonoma_residencia: para la advertencia del Impuesto sobre Sucesiones
outputs:
  - minuta_testamento_abierto: minuta de testamento abierto para llevar a la notaria, markdown, DRAFT
  - checklist_planificacion_sucesoria: checklist de documentacion, decisiones y avisos fiscales, markdown, DRAFT
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

# Planificacion Sucesoria en Vida: Minuta de Testamento Abierto

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
    "tipo_documento": {
      "type": "string",
      "description": "Alcance de la planificaci\u00f3n sucesoria (V2)",
      "enum": [
        "minuta_testamento",
        "checklist_planificacion"
      ]
    },
    "vecindad_civil": {
      "type": "string",
      "description": "Vecindad civil y r\u00e9gimen sucesorio aplicable (V1)",
      "enum": [
        "comun",
        "foral"
      ]
    },
    "descendientes": {
      "type": "string",
      "description": "Situaci\u00f3n familiar respecto a descendientes (V3a)",
      "enum": [
        "con_hijos",
        "sin_hijos"
      ]
    }
  },
  "required": [
    "tipo_documento",
    "vecindad_civil"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores aplicables, evalua en este orden:

- Si **V1 = 2 o V1 = 3** → **DETENER**. No se pregunta ningun otro vector, no se pide ningun dato del testador y **no se crea ningun documento**. Emite la advertencia fija de `references/vecindad-civil-y-ambito-de-la-skill.md`, apartado 6, y escala a un abogado o notario especializado en el derecho civil de ese territorio. Nunca redactes "una version provisional" ni respondas cuanta legitima corresponde: en derecho foral no es la del Art. 808 CC.
- Si **V1 = 1 y V2 = 1 y V4 = 2** → **HOJA SIMPLE**: `assets/template-minuta-testamento-abierto.md`, con los bloques condicionales de mejora, legados, usufructo universal con cautela, fideicomiso, desheredacion, facultades del Art. 831 y albacea DESACTIVADOS. Se activa la sustitucion vulgar salvo rechazo expreso del cliente, y el bloque de derechos del conyuge en su version de cuota legal si V3c = 1.
- Si **V1 = 1 y (V2 = 2 o V4 = 1)** → **HOJA PLANIFICACION**: dos documentos, en este orden. Primero `assets/template-checklist-planificacion-sucesoria.md`, sobre el que se recogen el patrimonio y todas las decisiones; despues, con las decisiones ya cerradas, `assets/template-minuta-testamento-abierto.md`. **Regla de reencaminamiento:** si el cliente respondio V2 = 1 pero despues manifiesta que quiere desheredar, mejorar, legar un bien concreto u ordenar un usufructo universal, reencamina en silencio a la HOJA PLANIFICACION y continua; no le anuncies el cambio de rama.
- Si **V3d = 1** → activa en la hoja que corresponda los bloques de los Arts. 808 in fine, 782 y 822, y trata la seccion de discapacidad del Punto 5 como obligatoria, no como opcional.
- Si lo que el usuario quiere es un **testamento olografo, cerrado o mancomunado**, o un **pacto sucesorio** → **DETENER**: fuera de alcance. El mancomunado es ademas nulo en derecho comun (Art. 669 CC). Advertir y escalar.
- Si el causante **ya ha fallecido** y lo que se pretende es aceptar, repudiar o partir la herencia → **DETENER**: esta skill cubre la fase previa, en vida. Derivar a `herencia`.

### Validacion de presupuestos (interno, antes del Punto 3)

- **Capacidad para testar (Arts. 662, 663 y 665 CC):** si el testador es **menor de catorce anos**, detener: no puede testar (Art. 663.1.º). Si el testador no puede conformar o expresar su voluntad ni aun con ayuda de medios o apoyos, detener y escalar (Art. 663.2.º). Si el cliente plantea dudas sobre la capacidad del testador, **no la valores**: el juicio de capacidad corresponde al Notario (Arts. 665, 685 y 696 CC), que la aprecia atendiendo al estado en que se halle al tiempo del otorgamiento (Art. 666). Advierte, recomienda anticipar la cuestion con la notaria y ofrece escalacion. Tras la Ley 8/2021 ya no se exige el dictamen previo de dos facultativos.
- **Renuncia anticipada a la legitima (Art. 816 CC):** si el cliente propone que un hijo renuncie ahora a su legitima, o pactar con el su importe, **rechazar**: toda renuncia o transaccion sobre la legitima futura es nula. Explicarlo y no recogerlo en ningun documento.
- **Gravamen o condicion sobre la legitima (Art. 813 CC):** si el cliente quiere condicionar la legitima de un legitimario ("si se casa", "si no vende la casa", "si me cuida"), **rechazar la clausula**, explicar que se tendria por no puesta y proponer la alternativa valida: destinar a esa persona solo la legitima estricta y dirigir la mejora y el tercio de libre disposicion a quien decida.
- **Desheredacion sin causa legal (Arts. 849 a 855 CC):** si V4 = 1, contrastar el motivo con las causas tasadas antes de redactar nada. Si no encaja, aplicar el Guardrail 5. Nunca redactar la clausula "por si acaso".
- **Caudal compuesto esencialmente por un bien indivisible:** si del inventario resulta que la vivienda u otro bien no divisible absorbe la practica totalidad del patrimonio y el testador quiere adjudicarlo a alguno de sus hijos, **no lo articules como legado ni como atribucion de cuota sin mas**: el resto del caudal no bastara para cubrir la legitima de los demas y la disposicion seria inoficiosa. Advierte y ofrece las dos vias del Punto 5, seccion 5: el pago en metalico de los Arts. 841 a 847 CC, que exige autorizacion expresa en el testamento, o la adjudicacion en la particion con abono del exceso en dinero del Art. 1062 CC.
- **Legado de bien ganancial o no privativo:** si el testador quiere legar un bien concreto que no le pertenece integramente, advertir del Art. 864 CC (el legado se entiende limitado a su parte o derecho) y de la necesidad de liquidar previamente la sociedad de gananciales.
- **Patrimonio empresarial, bienes en el extranjero o elemento internacional:** escalar antes de redactar (Reglamento UE 650/2012; Art. 1056.2 CC para la empresa familiar). No redactar la professio iuris ni la particion del Art. 1056.
- **Testador con testamento anterior:** no dar por revocado nada de memoria. La revocacion se ordena expresamente en la clausula PRIMERA (Arts. 738 y 739 CC).

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 662 a 743 del Código Civil (capacidad y forma del testamento abierto ante Notario, Art. 694 CC); Arts. 806 a 822 CC (legítimas de hijos y descendientes, padres y cónyuge viudo); Arts. 823 a 833 CC (mejora); Art. 848 CC (desheredación taxativa); y Art. 858 CC (legados).
2. **Orientación Legal del Caso:**
Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la norma aplicable y el valor del documento.** Textos fijos por hoja:
   - SIMPLE: "A su caso le resulta de aplicacion el Codigo Civil comun. Su testamento se otorgara en forma de testamento abierto ante Notario, conforme a los articulos 694 a 699 del Codigo Civil, y la legitima de sus herederos forzosos se rige por los articulos 806 a 808. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - PLANIFICACION: "A su caso le resulta de aplicacion el Codigo Civil comun. Su testamento se otorgara en forma de testamento abierto ante Notario, conforme a los articulos 694 a 699 del Codigo Civil; la legitima de sus herederos forzosos se rige por los articulos 806 a 808, la mejora por los articulos 823 y siguientes y los derechos de su conyuge por los articulos 834 y siguientes. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - **Si V3c = 2 (el testador no esta casado, o esta separado legalmente o de hecho), suprime de ese texto la mencion final a los derechos del conyuge**, que no concurren, y cierra la enumeracion en la mejora. No hables al cliente de un conyuge que no existe.
   - En ambas hojas, anadir esta advertencia fija: "Debe tener presente desde ahora que el documento que vamos a preparar **no es un testamento**: es una minuta destinada a la notaria. Solo produce efectos el testamento otorgado ante Notario, y es el propio Notario quien lo redacta con arreglo a la voluntad que usted le exprese, conforme al articulo 695 del Codigo Civil."
   - Si V3d = 1, anadir ademas: "Al encontrarse uno de sus legitimarios en situacion de discapacidad, dispone usted de un margen de planificacion mas amplio del ordinario, conforme a los articulos 808 y 822 del Codigo Civil en la redaccion dada por la Ley 8/2021."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla del sistema, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (si el documento adjuntado los incumple — por ejemplo, condiciona la legitima o deshereda sin expresar causa legal —, adviertelo antes de continuar).
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-checklist-planificacion-sucesoria.md`).
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

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. No pidas permiso para pasar de seccion: informa y continua en el mismo turno.

**Un dato por turno.** Los datos identificativos de una misma persona se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las decisiones marcadas `[negociacion]` se explican y se confirman una a una. **La vista previa y la confirmacion agrupada de una parte se emiten en el turno SIGUIENTE a la respuesta del ultimo sub-apartado, nunca en el mismo turno en que aun se esta preguntando ese ultimo dato.**

**Validacion de sentido, no solo de formato.** No aceptes mecanicamente cualquier respuesta. Si un dato es absurdo, imposible o no responde a lo preguntado (un DNI con forma de nombre, una fecha de nacimiento futura, un "hijo" que resulta ser un sobrino), no lo escribas: senala por que no encaja y pide aclaracion.

**Puntos `[negociacion]`.** En ellos no te limites a registrar la respuesta: explica primero el regimen legal por defecto y las consecuencias concretas de cada opcion, y solo despues pide la decision. Confirma que el cliente lo ha entendido antes de escribirlo. Los puntos `[dato objetivo]` se limitan a recoger el dato.

---

### Secciones — HOJA SIMPLE (`minuta-testamento-abierto.md`)

1. **Testador** `[dato objetivo — confirmacion agrupada por parte]`. Anuncio fijo: "Comenzamos por su identificacion como testador." Sub-apartados, uno por turno: a) nombre y apellidos; b) DNI o NIE; c) fecha de nacimiento; d) lugar de nacimiento; e) nombres del padre y de la madre; f) estado civil; g) domicilio. **La vecindad civil ya esta resuelta: no la vuelvas a preguntar.** El estado civil tambien esta parcialmente resuelto: si V3c = 1, escribe "casado" sin preguntarlo, y si V3c = 2, formula el sub-apartado f) solo para precisar cual es (soltero, viudo, divorciado o separado). Al recibir la respuesta al ultimo sub-apartado, vista previa unica y una sola confirmacion antes del `Edit`.
2. **Conyuge** `[dato objetivo — confirmacion agrupada por parte; solo si V3c = 1]`. Anuncio fijo: "Pasamos a identificar a su conyuge." a) nombre y apellidos; b) DNI o NIE; c) regimen economico matrimonial. Confirmacion agrupada.
3. **Legitimarios** `[dato objetivo con validacion]`. Anuncio fijo: "Relacionamos ahora a quienes la ley reconoce como herederos forzosos." Por cada descendiente, uno por turno: nombre y apellidos, y DNI o NIE si se conoce. Si V3a = 2 y V3b = 1, pide la misma relacion de los ascendientes vivos. **Validacion obligatoria:** advierte de que deben relacionarse TODOS los descendientes, reciban o no atribucion, porque omitir a uno provoca la preterición del articulo 814 del Codigo Civil, que anula la institucion de herederos. Confirmacion agrupada por cada legitimario.
4. **Naturaleza del documento y revocacion de disposiciones anteriores** `[negociacion]`. Anuncio fijo: "Antes de entrar en el contenido, conviene fijar el valor de este documento y el destino de sus testamentos anteriores." Explica, antes de pedir nada: que esta minuta no es un testamento y solo produce efectos el otorgado ante Notario (articulos 687 y 695 del Codigo Civil); que **todas las disposiciones testamentarias son esencialmente revocables** (articulo 737), de modo que lo que decida hoy no le ata y puede sustituirlo en cualquier momento por otro testamento posterior otorgado con las mismas solemnidades (articulos 738 y 739); y que otorgar testamento **no limita su libertad de disponer de sus bienes en vida**. Pregunta despues si ha otorgado testamentos anteriores y confirma la revocacion expresa de todos ellos.
5. **Institucion de herederos** `[negociacion — PUNTO CLAVE]`. Anuncio fijo: "Pasamos al nucleo del testamento: la designacion de sus herederos." **Explica ANTES de pedir ninguna decision**, porque es el punto que mas sorprende al cliente: con descendientes, dos de cada tres partes de la herencia son legitima y estan reservadas por ley a los hijos o descendientes (articulo 808 del Codigo Civil); de esas dos, una es de legitima estricta y se reparte por partes iguales, y la otra es el tercio de mejora, que solo puede ir a hijos o descendientes pero permite elegir a cual; **solo un tercio es realmente de libre disposicion**. Anade que la legitima es intangible: no cabe imponer sobre ella condicion, plazo ni gravamen alguno (articulo 813) y ningun hijo puede renunciar a ella en vida del testador (articulo 816). Solo despues de que el cliente confirme que lo ha entendido, pide, en turnos separados: a) a quien instituye herederos; b) en que proporcion. Verifica que el reparto respeta la legitima antes de escribirlo.
6. **Derechos del conyuge viudo** `[negociacion; solo si V3c = 1]`. Anuncio fijo: "Determinamos ahora los derechos que corresponderan a su conyuge." Explica el regimen por defecto segun con quien concurra: usufructo del tercio de mejora con descendientes (articulo 834), de la mitad con ascendientes y sin descendientes (articulo 837), y de dos tercios sin unos ni otros (articulo 838). Pregunta si desea dejarlo asi o ampliar la proteccion del conyuge; si quiere ampliarla, aplica el punto de negociacion de la cautela socini descrito en la seccion 10 de la HOJA PLANIFICACION y reencamina el caso a esa hoja.
7. **Sustitucion vulgar** `[negociacion]`. Anuncio fijo: "Valoramos ahora que debe ocurrir si alguno de sus herederos no llega a heredar." Explica el articulo 774 del Codigo Civil: la sustitucion vulgar designa quien ocupa el lugar del heredero que fallece antes que el testador, renuncia o no puede aceptar; sin ella, esa porcion se rige por las reglas legales supletorias de acrecimiento y de sucesion intestada, con un resultado que puede no coincidir con lo que el testador quiere. Recomienda ordenarla y pregunta a quien designa como sustitutos.
8. **Instrucciones para la notaria** `[dato objetivo]`. Anuncio fijo: "Cerramos con las instrucciones para la notaria." Sub-apartados, uno por turno: a) notaria a la que se dirigira; b) poblacion; c) fecha prevista de otorgamiento; d) documentacion que aportara el testador. Pregunta ademas, en la misma seccion y en la misma frase por ser un dato puntual de respuesta cerrada, si el testador puede firmar y leer sin dificultad (si / no / con dificultad), para activar en su caso los bloques de los articulos 695 y 697.
9. **Aviso fiscal** `[negociacion — informativo]`. Anuncio fijo: "Por ultimo, debe conocer las consecuencias fiscales de lo que acabamos de ordenar." Explica que el Impuesto sobre Sucesiones y Donaciones esta cedido a las comunidades autonomas, que sus reducciones y bonificaciones varian de forma muy relevante entre ellas y que **esta herramienta no lo calcula ni lo estima**. Pregunta la comunidad autonoma de residencia habitual del testador y recomienda contrastar la planificacion con un asesor fiscal de esa comunidad antes de acudir a la notaria.

---

### Secciones — HOJA PLANIFICACION

**Documento 1: `checklist-planificacion-sucesoria.md`** (secciones 1 a 13)

1. **Documentacion a reunir** `[dato objetivo]`. Anuncio fijo: "Comenzamos por la documentacion que debera reunir antes de acudir a la notaria." Repasa la lista del asset y pregunta que documentos no tiene todavia, para dejarlos anotados como pendientes.
2. **Mapa familiar y legitimarios** `[dato objetivo con validacion]`. Anuncio fijo: "Pasamos a fijar quienes son sus herederos forzosos." Por cada descendiente, uno por turno: nombre y apellidos, y DNI o NIE si se conoce. Si procede, los ascendientes vivos y la situacion del conyuge. Misma validacion de la preterición del articulo 814 que en la HOJA SIMPLE. Confirmacion agrupada por cada legitimario.
3. **Inventario orientativo del patrimonio** `[dato objetivo]`. Anuncio fijo: "Relacionamos ahora, de forma orientativa, su patrimonio." Sub-apartados, uno por turno: a) inmuebles, con direccion y referencia catastral; b) cuentas, fondos y valores; c) vehiculos y muebles de valor; d) seguros de vida y planes de prevision; e) participaciones societarias, si las hay; f) deudas y cargas; g) donaciones ya realizadas en vida. Advierte en el apartado g) que las donaciones se computan para el calculo de la legitima y se imputan conforme a los articulos 818 y 819 del Codigo Civil: anticipar bienes en vida no saca esos bienes del calculo. Si aparece patrimonio empresarial o bienes en el extranjero, aplica la escalacion correspondiente antes de continuar.
4. **Legitima y margen real de libre disposicion** `[negociacion — PUNTO CLAVE]`. Anuncio fijo: "Antes de tomar ninguna decision, debe conocer que parte de su patrimonio puede repartir libremente." Misma explicacion que la seccion 5 de la HOJA SIMPLE (tercios del articulo 808, intangibilidad del 813, nulidad de la renuncia anticipada del 816), aplicada ya a los legitimarios concretos identificados en la seccion 2: calcula y muestra que corresponde a legitima estricta, que al tercio de mejora y que al de libre disposicion. Confirma que el cliente lo ha entendido antes de pasar a las decisiones. Si el cliente reacciona proponiendo condicionar la legitima o pactar su renuncia, aplica la validacion de presupuestos y ofrece la alternativa valida.
5. **Institucion de herederos y reparto del caudal** `[negociacion — PUNTO CLAVE]`. Anuncio fijo: "Pasamos al nucleo del testamento: la designacion de sus herederos." Es la clausula que la minuta contiene siempre y sin la cual el testamento no cumple su funcion: **nunca la des por supuesta ni la deduzcas de las decisiones sobre la mejora o los legados**. Partiendo de los tercios ya calculados en la seccion 4, pide en turnos separados: a) a quien instituye herederos; b) en que proporcion se les llama, comprobando antes de escribirla que ningun legitimario recibe menos de su legitima estricta. Si el testador quiere dejar a un legitimario **solo lo minimo legal**, explicale que la formula valida no es apartarlo del testamento —lo que provocaria la preterición del articulo 814— sino instituirlo tambien heredero en la porcion que cubra exactamente su legitima estricta, y recogelo asi. c) Si del inventario de la seccion 3 resulta que el caudal se compone esencialmente de uno o varios **bienes indivisibles** (tipicamente, la vivienda) y el testador quiere adjudicarlos a alguno de sus hijos, adviertele de que la cuota de los demas no podra pagarse con los bienes que quedan y explicale las dos vias: ordenar la adjudicacion del bien a esos hijos disponiendo que la porcion de los restantes legitimarios **se pague en metalico**, al amparo del articulo 841 del Codigo Civil, que exige autorizacion expresa en el testamento al contador-partidor, comunicar la decision a los perceptores dentro del ano siguiente a la apertura de la sucesion y pagar en el plazo de otro ano mas (articulo 844), fijando la suma por el valor de los bienes al tiempo de la liquidacion (articulo 847) y con aprobacion notarial o del Letrado de la Administracion de Justicia salvo confirmacion expresa de todos los hijos (articulo 843); o dejar la cuestion a la particion, donde el bien indivisible se adjudica a uno abonando el exceso en dinero, bastando que un solo heredero pida la venta en publica subasta para que asi se haga (articulo 1062). Adviertele ademas de que el hijo obligado a pagar en metalico puede exigir que esa cuota se satisfaga en bienes de la herencia (articulo 842). Pregunta cual de las dos vias prefiere.
6. **Destino del tercio de libre disposicion y legados** `[negociacion]`. Anuncio fijo: "Determinamos el destino del tercio de libre disposicion y los legados que desee ordenar." Explica que este tercio puede ir a cualquier persona, incluso ajena a la familia, y que los legados de bienes concretos se imputan a el y no pueden perjudicar la legitima (articulos 813, 817 y 820). Advierte del articulo 869: si el bien legado se vende o se transforma, el legado queda sin efecto. Pide, en turnos separados: a) destino del tercio de libre disposicion; b) relacion de legados, identificando cada bien de forma inequivoca y a su beneficiario.
7. **Mejora** `[negociacion]`. Anuncio fijo: "Valoramos si desea mejorar a alguno de sus hijos o descendientes." Explica que el tercio de mejora solo puede ir a hijos o descendientes, que si no se ordena nada se reparte entre los legitimarios como legitima, y que **la mejora debe declararse expresamente** (articulos 823, 825 y 828): decir "le dejo la casa" no mejora a nadie. Pregunta si desea mejorar y a quien, y en que consiste la mejora.
8. **Legitimario en situacion de discapacidad** `[negociacion; obligatoria si V3d = 1]`. Anuncio fijo: "Abordamos las disposiciones que la ley permite a favor del legitimario en situacion de discapacidad." Explica las dos herramientas de la Ley 8/2021: la del **articulo 808, ultimo parrafo**, que permite disponer a su favor de la legitima estricta de los demas legitimarios, quedando lo recibido gravado con sustitucion fideicomisaria de residuo a favor de los perjudicados y correspondiendo al hijo que impugne acreditar que no concurre causa que lo justifique; y la del **articulo 822**, el derecho de habitacion sobre la vivienda habitual, que no se computa para el calculo de las legitimas si al fallecer ambos convivian en ella, es intransmisible y se atribuye ademas por ministerio de la ley salvo que el testador lo excluya expresamente. Pregunta, en turnos separados: a) si desea disponer a su favor de la legitima estricta de los demas; b) si desea legarle el derecho de habitacion sobre la vivienda habitual, y en ese caso su direccion completa. Advierte de que el gravamen del articulo 808 es una de las pocas excepciones a la intangibilidad de la legitima y de que la acreditacion concreta de la situacion de discapacidad debera confirmarse con la notaria.
9. **Desheredacion** `[negociacion — critica; solo si V4 = 1]`. Anuncio fijo: "Abordamos la desheredacion que desea ordenar." Procedimiento obligatorio, en este orden:
   a) Pregunta a quien desea desheredar y por que motivo, en prosa.
   b) **Contrasta el motivo con las causas tasadas** de los articulos 852 a 855 del Codigo Civil, usando `references/cc-desheredacion-causas-tasadas.md`. No lo des por bueno por aproximacion.
   c) **Si el motivo NO encaja en ninguna causa legal:** dilo con claridad, sin rodeos. Explica que la desheredacion sin causa legal, o por causa que no se pruebe, **anula la institucion de heredero en cuanto perjudique al desheredado** (articulo 851), de modo que la clausula no solo no surtiria efecto sino que abriria un pleito entre los herederos. Ofrece la alternativa valida y sin riesgo: reducir a esa persona a su legitima estricta, destinando la mejora y el tercio de libre disposicion a quien el cliente decida. Si el cliente la acepta, se recoge en el bloque **"Atribucion limitada a la legitima estricta"** del asset de la minuta, y el legitimario sigue figurando como heredero instituido en la porcion que cubra su legitima, para no incurrir en la preterición del articulo 814. **No redactes la clausula de desheredacion.** Si el cliente insiste, escala.
   d) **Si el motivo SI encaja:** advierte igualmente, antes de redactar, de las tres consecuencias que suelen ignorarse: que la prueba de la causa correspondera a los herederos favorecidos si el desheredado la niega (articulo 850), y que el testador ya no estara para probarla; que una reconciliacion posterior deja sin efecto la desheredacion (articulo 856); y que **los hijos o descendientes del desheredado ocupan su lugar y conservan la legitima** (articulo 857), de modo que la desheredacion no aparta a esa rama de la familia. Pide despues: el articulo y la causa legal concreta, y una descripcion de los hechos en que se funda, porque el articulo 849 exige expresar la causa en el testamento. Adopta siempre la posicion conservadora.
10. **Derechos del conyuge y cautela socini** `[negociacion; solo si V3c = 1]`. Anuncio fijo: "Determinamos los derechos que corresponderan a su conyuge." Explica en este orden:
   - El regimen por defecto: usufructo del tercio de mejora con descendientes (articulo 834), de la mitad con ascendientes (articulo 837), de dos tercios sin descendientes ni ascendientes (articulo 838).
   - Que muchos testadores quieren dejar al conyuge el usufructo de **toda** la herencia para que no dependa economicamente de los hijos, pero que un usufructo universal grava tambien la legitima estricta, y el articulo 813 lo prohibe.
   - **Como funciona la cautela socini**, con su dilema explicito: se ordena el usufructo universal acompanado de una opcion para cada hijo, amparada en el articulo 820, numero 3.º, del Codigo Civil. El hijo elige entre aceptar el usufructo, recibiendo su parte completa pero en nuda propiedad y gravada de por vida, o no aceptarlo, recibiendo entonces **solo su legitima estricta**, libre y de inmediato. Cobra mas y mas tarde, o menos y ya. La clausula no vulnera la legitima: la respeta y pone al hijo ante una eleccion incomoda.
   - La posicion conservadora: es una clausula de uso extendido pero **no tipificada en el Codigo Civil**, construida por la practica notarial y la jurisprudencia; si esta mal redactada es susceptible de litigio, y su redaccion definitiva corresponde al Notario.
   Pregunta despues cual de las dos opciones prefiere. Si elige el usufructo universal, confirma expresamente que ha entendido el dilema que plantea a sus hijos antes de escribirlo.
11. **Sustituciones** `[negociacion]`. Anuncio fijo: "Valoramos ahora que debe ocurrir si alguno de sus herederos no llega a heredar." Misma explicacion de la sustitucion vulgar que en la HOJA SIMPLE (articulo 774). Si ademas el cliente quiere que los bienes pasen despues a otra persona (tipicamente, del conyuge a los nietos), explica la sustitucion fideicomisaria: valida solo hasta el segundo grado o a favor de personas que vivan al fallecer el testador (articulo 781), de llamamiento necesariamente expreso (articulo 783), y que **nunca puede gravar la legitima** salvo el supuesto del legitimario con discapacidad del articulo 808 (articulo 782). Adviertele de que su nulidad no arrastra la institucion, que se mantiene (articulo 786). Pide los sustitutos vulgares y, en su caso, el fiduciario, el fideicomisario y el objeto del fideicomiso.
12. **Albacea contador-partidor y facultades al conyuge** `[negociacion]`. Anuncio fijo: "Valoramos si conviene designar quien ejecute y reparta la herencia." Explica que sin albacea contador-partidor la particion exige el acuerdo unanime de todos los herederos, y que designarlo evita el bloqueo. Explica ademas, si hay conyuge e hijos comunes, las facultades del articulo 831 del Codigo Civil: permiten que el conyuge sobreviviente mejore y adjudique entre los hijos o descendientes comunes despues del fallecimiento, con un plazo supletorio de dos anos, y que **cesan** si pasa a ulterior matrimonio o relacion analoga o tiene un hijo no comun, salvo disposicion contraria. Pregunta, en turnos separados: a) si designa albacea contador-partidor, y en su caso su nombre, DNI y plazo; b) si confiere al conyuge las facultades del articulo 831 y con que plazo.
13. **Aviso fiscal** `[negociacion — informativo]`. Anuncio fijo: "Antes de cerrar la planificacion, debe conocer sus consecuencias fiscales." Explica que el Impuesto sobre Sucesiones y Donaciones esta cedido a las comunidades autonomas, que las reducciones y bonificaciones varian de forma muy relevante entre ellas de modo que una misma planificacion puede tener un coste muy distinto segun la comunidad aplicable, y que **esta herramienta no lo calcula ni lo estima**. Advierte ademas de la plusvalia municipal si hay inmuebles urbanos, del regimen propio de los seguros de vida y de que las donaciones en vida no son fiscalmente neutras. Pregunta la comunidad autonoma de residencia habitual del testador y recomienda contrastar la planificacion con un asesor fiscal de esa comunidad.

**Cierre del checklist.** Completada la seccion 13, aplica el Punto 4.b: crea `minuta-testamento-abierto.md` volcando todas las decisiones confirmadas, verifica con `Read`, confirma la ruta absoluta y, en la misma respuesta, emite el anuncio de la seccion 14 y su primera pregunta.

**Documento 2: `minuta-testamento-abierto.md`** (secciones 14 a 17)

14. **Testador** `[dato objetivo — confirmacion agrupada por parte]`. Anuncio fijo: "Comenzamos por su identificacion como testador." Mismos sub-apartados que la seccion 1 de la HOJA SIMPLE. Omite los que ya conozcas.
15. **Conyuge** `[dato objetivo — confirmacion agrupada por parte; solo si V3c = 1]`. Anuncio fijo: "Pasamos a identificar a su conyuge." Mismos sub-apartados que la seccion 2 de la HOJA SIMPLE.
16. **Naturaleza del documento y revocacion de disposiciones anteriores** `[negociacion]`. Anuncio fijo: "Antes de cerrar el contenido, conviene fijar el valor de este documento y el destino de sus testamentos anteriores." Mismo contenido que la seccion 4 de la HOJA SIMPLE.
17. **Instrucciones para la notaria** `[dato objetivo]`. Anuncio fijo: "Cerramos con las instrucciones para la notaria." Mismos sub-apartados que la seccion 8 de la HOJA SIMPLE.

---

### Numeracion final de las clausulas (obligatorio antes del bucle final)

Cuando todas las secciones esten completadas y todos los bloques condicionales decididos, y **antes** de mostrar el menu del bucle de realimentacion:

1. Lee la minuta con `Read`.
2. Sustituye cada placeholder `{{ordinal_...}}` por su ordinal en letra, **correlativo y sin saltos**, siguiendo el orden en que las clausulas aparecen realmente en el documento. La revocacion es siempre PRIMERA.
3. Verifica con `Read` que no queda ningun placeholder de ordinal sin resolver, ningun ordinal repetido y ninguna clausula sin encabezado.
4. Verifica en la misma lectura que el documento no contiene ningun comentario HTML (`<!-- ... -->`) ni ningun bloque de una rama descartada.

Esta numeracion se rehace cada vez que el bucle de realimentacion anada o elimine una clausula condicional.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: una disposicion por clausula, voz activa con el testador como sujeto, personas y bienes identificados de forma inequivoca, sin latinismos ni formulas huecas, mejora declarada expresamente, causa legal expresada en toda desheredacion, y nada impuesto sobre la legitima estricta.

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

1. Verificar siempre el Codigo Civil en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder. Si se detecta una version posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario.
2. **La vecindad civil es el filtro de alcance.** Si es foral o especial, o el testador no la conoce con seguridad, detener de inmediato y escalar (Arts. 14 y 16 CC). No redactar, no adaptar, no estimar legitimas. Esta skill solo cubre derecho civil comun.
3. **La legitima es intangible** (Arts. 806, 808 y 813 CC). Nunca redactar una clausula que la reduzca, la condicione, la someta a plazo o la grave, fuera de las excepciones expresas de los Arts. 782, 808 y del usufructo del viudo. Si el usuario lo pide, rechazar la instruccion, explicar que la clausula se tendria por no puesta y proponer la alternativa valida.
4. **Nulidad de la renuncia anticipada** (Art. 816 CC). Nunca documentar la renuncia de un legitimario a su legitima futura ni un pacto sobre ella con el causante en vida.
5. **Desheredacion solo por causa tasada** (Arts. 849 a 855 CC). Contrastar siempre el motivo con la lista legal. Si no encaja, no redactar la clausula, explicar el efecto del Art. 851 y ofrecer la alternativa de reducir a la legitima estricta. Si encaja, advertir del Art. 850 (la prueba corresponde a los herederos favorecidos), del Art. 856 (la reconciliacion la deja sin efecto) y del Art. 857 (los descendientes del desheredado conservan la legitima). Posicion conservadora siempre.
6. **Relacionar a todos los legitimarios**, reciban o no atribucion, para evitar la preterición del Art. 814 CC, que anula la institucion de herederos.
7. **La minuta no es un testamento.** Nunca presentarla como tal ni dar a entender que produce efectos. Solo el testamento otorgado ante Notario con las formalidades de los Arts. 694 a 699 CC vale como tal (Art. 687), y es el Notario quien lo redacta (Art. 695).
8. **El juicio de capacidad corresponde al Notario** (Arts. 665, 685 y 696 CC). La skill nunca valora ni certifica la capacidad del testador: si hay dudas, advierte, recomienda anticiparlo con la notaria y escala.
9. **La mejora debe ser expresa** (Arts. 825 y 828 CC). Nunca dar por mejorado a un hijo por el hecho de dejarle un bien concreto.
10. **La sustitucion fideicomisaria no puede gravar la legitima** salvo el supuesto del legitimario con discapacidad del Art. 808 (Art. 782 CC), y no puede pasar del segundo grado o de personas que vivan al fallecer el testador (Art. 781).
11. **Esta skill no calcula el Impuesto sobre Sucesiones y Donaciones** ni valora la fiscalidad de las disposiciones. Advertir siempre de que es un tributo autonomico con consecuencias muy distintas segun la comunidad, y no dar cifras ni estimaciones.
12. Nunca inventar datos, cuantias, bienes, fechas ni jurisprudencia. Nunca citar un articulo sin haberlo verificado en el Punto 2. Los campos no proporcionados quedan como `{{dato}}` con el nombre propio del placeholder del asset.
13. **La institucion de heredero se pregunta siempre y de forma expresa**, en las dos hojas. Nunca deducirla de la mejora, de los legados o del reparto de un bien concreto: sin ella el testamento no dispone de la herencia y se abre la sucesion intestada respecto de lo no dispuesto (Art. 912.2.º CC).
14. **Bien indivisible que absorbe el caudal.** Adjudicar la vivienda a algunos legitimarios solo es viable ordenando el pago en metalico de la porcion de los demas (Arts. 841 a 847 CC, con autorizacion expresa en el testamento) o remitiendo la cuestion a la particion (Art. 1062 CC). Nunca darlo por resuelto con un legado del inmueble cuando el resto del caudal no cubre la legitima.
15. El documento escrito en disco lleva CERO comentarios HTML y CERO placeholders de ordinal sin resolver al cerrar.

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para testadores de vecindad civil foral o especial (Cataluna, Aragon, Navarra, Illes Balears, Pais Vasco, Galicia): **detener y escalar**. El regimen de legitimas y de sucesion es distinto y esta skill no lo cubre.
- No usar para el testamento olografo (Art. 688 CC), el cerrado (Art. 706) ni los testamentos especiales y supuestos excepcionales del Codigo: fuera de alcance.
- No usar para el testamento mancomunado ni para pactos sucesorios: el mancomunado es nulo en derecho comun (Art. 669 CC).
- No usar para la herencia ya abierta tras el fallecimiento —aceptacion, renuncia, interpelacion al heredero silente, cuaderno particional o division judicial—: derivar a `herencia`.
- No usar para tramitar el acta notarial de declaracion de herederos abintestato ni para el otorgamiento en si: son actuaciones notariales.
- No usar para calcular ni liquidar el Impuesto sobre Sucesiones y Donaciones ni la plusvalia municipal.
- No usar para impugnar un testamento ajeno, reclamar la legitima, ejercitar la accion de complemento del Art. 815 CC o la reduccion de disposiciones inoficiosas del Art. 817: son posiciones litigiosas, fuera de alcance. Derivar a derivación formal.
- No usar para la planificacion de patrimonio empresarial o societario, ni para sucesiones con elemento internacional: escalar.
- No usar para valorar la capacidad del testador: corresponde al Notario.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.
