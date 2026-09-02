---
name: derecho-civil-testamento-planificacion
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
  - references/cc-legitimas-y-libre-disposicion.md
  - references/cc-desheredacion-causas-tasadas.md
  - references/cc-formas-revocacion-y-sustituciones.md
  - references/vecindad-civil-y-ambito-de-la-skill.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/minuta-testamento-abierto.md
  - assets/checklist-planificacion-sucesoria.md
---

# Planificacion Sucesoria en Vida: Minuta de Testamento Abierto

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija del Punto 1 y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

Esta linea es, junto con la introduccion fija del Punto 1 y los anuncios de seccion del Punto 5, la UNICA excepcion a la Directiva de Invisibilidad. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, el enrutamiento, la validacion de presupuestos, la verificacion normativa y la creacion de los documentos base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol.
- Resumenes de validacion con checks (ej. "Vecindad civil: ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin. No afirmes todavia que norma ni que articulos aplican: dependen de vectores aun no resueltos.

"Vamos a preparar la documentacion para que pueda ordenar su sucesion en vida y llevarla resuelta a la notaria. Para ajustarla correctamente a su caso, es necesario precisar antes algunos datos."

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:

- **V1 (Vecindad civil):** derecho civil comun / derecho civil foral o especial (Cataluna, Aragon, Navarra, Illes Balears, Pais Vasco, Galicia) / el testador no lo sabe con seguridad. **Es el filtro de alcance de toda la skill y se resuelve SIEMPRE el primero.** **Nunca lo des por resuelto por Escucha Activa a partir del lugar de nacimiento o de residencia del testador:** la vecindad civil se adquiere por filiacion (Art. 14.2 CC) y solo se muda por residencia continuada de dos anos con manifestacion expresa o de diez sin declaracion en contrario (Art. 14.5). Decir "naci y he vivido siempre en X" no acredita la vecindad; formula la pregunta de forma expresa en todo caso.
- **V2 (Alcance del testamento):** testamento simple (institucion de heredero y poco mas) / testamento con planificacion (mejora, legados especificos, sustituciones, fideicomiso, usufructo universal al conyuge o desheredacion).
- **V3 (Legitimarios):** se resuelve en tres sub-vectores:
  - **V3a:** tiene hijos o descendientes / no los tiene.
  - **V3b (solo si V3a = no):** viven sus padres u otros ascendientes / no viven.
  - **V3c:** esta casado y no separado legalmente ni de hecho / no lo esta.
  - **V3d:** alguno de los legitimarios se encuentra en situacion de discapacidad / ninguno.
- **V4 (Desheredacion):** el testador quiere desheredar a algun legitimario / no quiere.

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto, omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama. El usuario responde con el numero o con la palabra:

* Para V1:
  "Su vecindad civil es:
  1. Comun
  2. Foral o especial (Cataluna, Aragon, Navarra, Illes Balears, Pais Vasco o Galicia)
  3. No lo se con seguridad"

* Para V2:
  "El testamento que desea preparar es:
  1. Simple: designar heredero o herederos y poco mas
  2. Con planificacion: mejorar a alguien, dejar legados concretos, proteger a su conyuge, ordenar sustituciones o desheredar"

* Para V3a:
  "Respecto de sus descendientes:
  1. Tengo hijos o descendientes
  2. No tengo hijos ni descendientes"

* Para V3b (solo si V3a = 2):
  "Respecto de sus ascendientes:
  1. Vive alguno de mis padres u otro ascendiente
  2. No vive ninguno"

* Para V3c:
  "Respecto de su estado civil:
  1. Estoy casado y no separado legalmente ni de hecho
  2. No estoy casado, o estoy separado legalmente o de hecho"

* Para V3d:
  "Alguna de las personas que acaba de indicar:
  1. Se encuentra en situacion de discapacidad
  2. Ninguna se encuentra en esa situacion"

* Para V4:
  "Respecto de sus herederos forzosos:
  1. Deseo desheredar a alguno de ellos
  2. No deseo desheredar a nadie"

**PRINCIPIO: Preguntas simples, no mega-preguntas.** Cada pregunta resuelve un unico punto de decision. No comprimas V3a, V3b, V3c y V3d en una sola pregunta sobre "su situacion familiar", ni V1 y V2 en una sola sobre "su caso".

**Orden de las preguntas.** V1 se pregunta SIEMPRE el primero, aunque sea el vector mas abstracto, porque una respuesta foral o dudosa deja el caso fuera de alcance y hace inutil todo lo demas: preguntarlo antes ahorra al cliente aportar datos que no se van a usar.

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua en este orden:

- Si **V1 = 2 o V1 = 3** → **DETENER**. No se pregunta ningun otro vector, no se pide ningun dato del testador y **no se crea ningun documento**. Emite la advertencia fija de `references/vecindad-civil-y-ambito-de-la-skill.md`, apartado 6, y escala a un abogado o notario especializado en el derecho civil de ese territorio. Nunca redactes "una version provisional" ni respondas cuanta legitima corresponde: en derecho foral no es la del Art. 808 CC.
- Si **V1 = 1 y V2 = 1 y V4 = 2** → **HOJA SIMPLE**: `assets/minuta-testamento-abierto.md`, con los bloques condicionales de mejora, legados, usufructo universal con cautela, fideicomiso, desheredacion, facultades del Art. 831 y albacea DESACTIVADOS. Se activa la sustitucion vulgar salvo rechazo expreso del cliente, y el bloque de derechos del conyuge en su version de cuota legal si V3c = 1.
- Si **V1 = 1 y (V2 = 2 o V4 = 1)** → **HOJA PLANIFICACION**: dos documentos, en este orden. Primero `assets/checklist-planificacion-sucesoria.md`, sobre el que se recogen el patrimonio y todas las decisiones; despues, con las decisiones ya cerradas, `assets/minuta-testamento-abierto.md`. **Regla de reencaminamiento:** si el cliente respondio V2 = 1 pero despues manifiesta que quiere desheredar, mejorar, legar un bien concreto u ordenar un usufructo universal, reencamina en silencio a la HOJA PLANIFICACION y continua; no le anuncies el cambio de rama.
- Si **V3d = 1** → activa en la hoja que corresponda los bloques de los Arts. 808 in fine, 782 y 822, y trata la seccion de discapacidad del Punto 5 como obligatoria, no como opcional.
- Si lo que el usuario quiere es un **testamento olografo, cerrado o mancomunado**, o un **pacto sucesorio** → **DETENER**: fuera de alcance. El mancomunado es ademas nulo en derecho comun (Art. 669 CC). Advertir y escalar.
- Si el causante **ya ha fallecido** y lo que se pretende es aceptar, repudiar o partir la herencia → **DETENER**: esta skill cubre la fase previa, en vida. Derivar a `derecho-civil-herencia`.

### Validacion de presupuestos (interno, antes del Punto 3)

- **Capacidad para testar (Arts. 662, 663 y 665 CC):** si el testador es **menor de catorce anos**, detener: no puede testar (Art. 663.1.º). Si el testador no puede conformar o expresar su voluntad ni aun con ayuda de medios o apoyos, detener y escalar (Art. 663.2.º). Si el cliente plantea dudas sobre la capacidad del testador, **no la valores**: el juicio de capacidad corresponde al Notario (Arts. 665, 685 y 696 CC), que la aprecia atendiendo al estado en que se halle al tiempo del otorgamiento (Art. 666). Advierte, recomienda anticipar la cuestion con la notaria y ofrece escalacion. Tras la Ley 8/2021 ya no se exige el dictamen previo de dos facultativos.
- **Renuncia anticipada a la legitima (Art. 816 CC):** si el cliente propone que un hijo renuncie ahora a su legitima, o pactar con el su importe, **rechazar**: toda renuncia o transaccion sobre la legitima futura es nula. Explicarlo y no recogerlo en ningun documento.
- **Gravamen o condicion sobre la legitima (Art. 813 CC):** si el cliente quiere condicionar la legitima de un legitimario ("si se casa", "si no vende la casa", "si me cuida"), **rechazar la clausula**, explicar que se tendria por no puesta y proponer la alternativa valida: destinar a esa persona solo la legitima estricta y dirigir la mejora y el tercio de libre disposicion a quien decida.
- **Desheredacion sin causa legal (Arts. 849 a 855 CC):** si V4 = 1, contrastar el motivo con las causas tasadas antes de redactar nada. Si no encaja, aplicar el Guardrail 5. Nunca redactar la clausula "por si acaso".
- **Caudal compuesto esencialmente por un bien indivisible:** si del inventario resulta que la vivienda u otro bien no divisible absorbe la practica totalidad del patrimonio y el testador quiere adjudicarlo a alguno de sus hijos, **no lo articules como legado ni como atribucion de cuota sin mas**: el resto del caudal no bastara para cubrir la legitima de los demas y la disposicion seria inoficiosa. Advierte y ofrece las dos vias del Punto 5, seccion 5: el pago en metalico de los Arts. 841 a 847 CC, que exige autorizacion expresa en el testamento, o la adjudicacion en la particion con abono del exceso en dinero del Art. 1062 CC.
- **Legado de bien ganancial o no privativo:** si el testador quiere legar un bien concreto que no le pertenece integramente, advertir del Art. 864 CC (el legado se entiende limitado a su parte o derecho) y de la necesidad de liquidar previamente la sociedad de gananciales.
- **Patrimonio empresarial, bienes en el extranjero o elemento internacional:** escalar antes de redactar (Reglamento UE 650/2012; Art. 1056.2 CC para la empresa familiar). No redactar la professio iuris ni la particion del Art. 1056.
- **Testador con testamento anterior:** no dar por revocado nada de memoria. La revocacion se ordena expresamente en la clausula PRIMERA (Arts. 738 y 739 CC).

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del Codigo Civil y de la Ley 8/2021.

**2.2 — Consultar la fuente oficial vigente.** La API de legislacion consolidada del BOE devuelve el bloque de un articulo concreto (requiere cabecera `Accept: application/xml`). **La redaccion vigente es la ULTIMA `<version>` del bloque**, no la primera:
```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero_articulo}
```
Consultar del Codigo Civil los bloques de los arts. 14, 16 y 9.8 (vecindad civil y ley aplicable); 662 a 666 (capacidad); 667 a 675 (concepto y limites); 676 a 687 (formas y nulidad por defecto de forma); 694 a 699 (testamento abierto); 737 a 743 (revocacion); 774 a 787 (sustituciones); 806 a 822 (legitimas); 823 a 833 (mejora); 834 a 840 (derechos del conyuge viudo); 849 a 857 y 756 (desheredacion e indignidad); 858 a 882 (legados); y, si hay patrimonio empresarial, 1056.

**Aviso sobre el identificador de bloque:** el Codigo Civil usa `artNNN` (p. ej. `art808`). Otras normas usan otras convenciones (la LEC usa `aNNN`; la LOPJ y la LPH los deletrean). Si un identificador devuelve 404, probar la otra convencion antes de dar el precepto por inaccesible.

**2.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar `Write`/`Edit` para:
- Actualizar `references/cc-legitimas-y-libre-disposicion.md`, `references/cc-desheredacion-causas-tasadas.md`, `references/cc-formas-revocacion-y-sustituciones.md` y/o `references/vecindad-civil-y-ambito-de-la-skill.md` con la redaccion vigente.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Actualizar los assets si alguna clausula cita una redaccion que ha cambiado.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. **Prohibido dar por vigente lo que no se ha podido verificar.**

**2.5 — Fallback si la fuente no es accesible.** Si la lectura falla (error HTTP, timeout):
```
web_search("Codigo Civil legitima articulo 808 mejora 823 desheredacion 853 texto consolidado BOE")
web_search("Codigo Civil testamento abierto articulos 694 695 697 texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del Codigo Civil en el BOE. Los documentos se generan con la version de referencia. Verifique manualmente antes de acudir a la notaria."

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la norma aplicable y el valor del documento.** Textos fijos por hoja:
   - SIMPLE: "A su caso le resulta de aplicacion el Codigo Civil comun. Su testamento se otorgara en forma de testamento abierto ante Notario, conforme a los articulos 694 a 699 del Codigo Civil, y la legitima de sus herederos forzosos se rige por los articulos 806 a 808. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - PLANIFICACION: "A su caso le resulta de aplicacion el Codigo Civil comun. Su testamento se otorgara en forma de testamento abierto ante Notario, conforme a los articulos 694 a 699 del Codigo Civil; la legitima de sus herederos forzosos se rige por los articulos 806 a 808, la mejora por los articulos 823 y siguientes y los derechos de su conyuge por los articulos 834 y siguientes. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - **Si V3c = 2 (el testador no esta casado, o esta separado legalmente o de hecho), suprime de ese texto la mencion final a los derechos del conyuge**, que no concurren, y cierra la enumeracion en la mejora. No hables al cliente de un conyuge que no existe.
   - En ambas hojas, anadir esta advertencia fija: "Debe tener presente desde ahora que el documento que vamos a preparar **no es un testamento**: es una minuta destinada a la notaria. Solo produce efectos el testamento otorgado ante Notario, y es el propio Notario quien lo redacta con arreglo a la voluntad que usted le exprese, conforme al articulo 695 del Codigo Civil."
   - Si V3d = 1, anadir ademas: "Al encontrarse uno de sus legitimarios en situacion de discapacidad, dispone usted de un margen de planificacion mas amplio del ordinario, conforme a los articulos 808 y 822 del Codigo Civil en la redaccion dada por la Ley 8/2021."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (si el documento adjuntado los incumple — por ejemplo, condiciona la legitima o deshereda sin expresar causa legal —, adviertelo antes de continuar).

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento:

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa e investigacion, incluida `fecha_verificacion_cc` del Punto 2). Los faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{dni_testador}}`, `{{relacion_legados}}`); usa un marcador generico solo para un hueco suelto sin placeholder propio, y nunca repitas el mismo marcador generico dos veces en el mismo documento (`Edit` necesita un `oldString` unico).
3. Los bloques condicionales del asset que dependan de decisiones aun no tomadas se OMITEN por completo en este `Write`, sin dejar rastro del comentario, y se insertan durante el Punto 5 releyendo el asset y copiando el bloque **sin el envoltorio de comentario**. El documento escrito en disco lleva CERO comentarios HTML.
4. **Los placeholders de ordinal (`{{ordinal_...}}`) se dejan sin resolver en este `Write`** y se numeran al final, cuando todos los bloques condicionales esten decididos (ver "Numeracion final de las clausulas" en el Punto 5). La clausula de revocacion es siempre PRIMERA y su ordinal ya va fijo en el asset.
5. Utiliza `Write` para guardar el archivo en disco, con nombre en `snake_case.md` (ej. `minuta_testamento_abierto_testador_a.md`, `checklist_planificacion_sucesoria_testador_a.md`).
6. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. En esa MISMA respuesta, sin turno intermedio y **sin preguntar si desea empezar**, emite el anuncio fijo de la primera seccion y formula ya su primera pregunta, para que el flujo no se detenga (regla del `CLAUDE.md` raiz, seccion 6.1, punto 5, y coherencia con el Punto 0: la skill esta en ejecucion desde que se carga).

**4.b — Creacion de la minuta en la HOJA PLANIFICACION.** En esta rama el Punto 4 se ejecuta dos veces. La primera crea el checklist, tras la Confirmacion. La segunda se ejecuta **cuando el checklist queda cerrado** (completadas sus secciones 1 a 13 del Punto 5): entonces lee `assets/minuta-testamento-abierto.md`, vuelca en el `Write` inicial TODAS las decisiones ya confirmadas en el checklist (activando sus bloques condicionales y omitiendo los descartados), guarda el archivo, verifica con `Read`, confirma la ruta absoluta y, en esa misma respuesta, emite el anuncio de la seccion 14 y su primera pregunta. **No vuelvas a preguntar por una decision ya confirmada en el checklist.**

## 5. EDICION INCREMENTAL DE SECCIONES

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

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5 y la numeracion final de las clausulas, muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una seccion existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

En la HOJA SIMPLE, ofrece ademas, una sola vez, generar el checklist de planificacion sucesoria como documento complementario si el cliente lo desea.

Al cerrar, anade estas advertencias, ademas de las propias del asset:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado colegiado antes de llevarlo a la notaria.
2. Esta minuta no es un testamento y no produce efecto sucesorio alguno: solo lo produce el otorgado ante Notario (articulos 687 y 694 a 699 del Codigo Civil), que sera quien lo redacte con arreglo a la voluntad del testador (articulo 695).
3. El testamento es esencialmente revocable (articulo 737) y conviene revisarlo cuando cambien las circunstancias familiares o el patrimonio.
4. Version del Codigo Civil verificada en el BOE: fecha extraida en el Punto 2.
5. Impuesto sobre Sucesiones y Donaciones: tributo cedido a las comunidades autonomas. Esta skill no lo calcula. Verificar la normativa autonomica aplicable con un asesor fiscal.

## Guardrails

1. Verificar siempre el Codigo Civil en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder. Si se detecta una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar.
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

## Como NO se usa esta skill

- No usar para testadores de vecindad civil foral o especial (Cataluna, Aragon, Navarra, Illes Balears, Pais Vasco, Galicia): **detener y escalar**. El regimen de legitimas y de sucesion es distinto y esta skill no lo cubre.
- No usar para el testamento olografo (Art. 688 CC), el cerrado (Art. 706) ni los testamentos especiales y supuestos excepcionales del Codigo: fuera de alcance.
- No usar para el testamento mancomunado ni para pactos sucesorios: el mancomunado es nulo en derecho comun (Art. 669 CC).
- No usar para la herencia ya abierta tras el fallecimiento —aceptacion, renuncia, interpelacion al heredero silente, cuaderno particional o division judicial—: derivar a `derecho-civil-herencia`.
- No usar para tramitar el acta notarial de declaracion de herederos abintestato ni para el otorgamiento en si: son actuaciones notariales.
- No usar para calcular ni liquidar el Impuesto sobre Sucesiones y Donaciones ni la plusvalia municipal.
- No usar para impugnar un testamento ajeno, reclamar la legitima, ejercitar la accion de complemento del Art. 815 CC o la reduccion de disposiciones inoficiosas del Art. 817: son posiciones litigiosas, fuera de alcance. Derivar a `escalate_to_attorney`.
- No usar para la planificacion de patrimonio empresarial o societario, ni para sucesiones con elemento internacional: escalar.
- No usar para valorar la capacidad del testador: corresponde al Notario.

## Escalacion

| Situacion | Accion |
|---|---|
| Vecindad civil foral o especial, o desconocida por el testador | **Detener de inmediato.** No redactar ni estimar legitimas: el regimen sucesorio es distinto (Arts. 14 y 16 CC). Escalar a especialista en el derecho civil de ese territorio |
| Testador con posible falta de capacidad para testar | No valorar la capacidad: corresponde al Notario (Arts. 665, 685 y 696 CC). Advertir, recomendar anticiparlo con la notaria y escalar |
| Testador menor de catorce anos | Detener: no puede testar (Art. 663.1.º CC) |
| Motivo de desheredacion que no encaja en las causas tasadas y el cliente insiste | No redactar la clausula. Advertir del Art. 851 CC, ofrecer la reduccion a legitima estricta y escalar |
| Patrimonio empresarial o participaciones societarias relevantes | Escalar: la particion del Art. 1056.2 CC y el protocolo familiar exceden el alcance de esta skill |
| Bienes en el extranjero, otra nacionalidad o residencia habitual fuera de Espana | Escalar: entra en juego el Reglamento (UE) 650/2012 y la eleccion de ley aplicable |
| Peticion de condicionar, gravar o pactar la renuncia de la legitima, con insistencia del cliente | Rechazar la clausula (Arts. 813 y 816 CC), explicar la alternativa valida y escalar si insiste |
| Conflicto familiar activo, testamento anterior impugnado o litigio sucesorio en curso | Detener y escalar via `escalate_to_attorney` |
| Legitimario en situacion de discapacidad con medidas de apoyo judiciales ya establecidas | Advertir de que el alcance de las medidas de apoyo debe verificarse y escalar si condicionan la disposicion |
| Persona con discapacidad como testador | No valorar su capacidad: el Art. 665 CC atribuye el juicio al Notario, que debera facilitar los ajustes necesarios. Advertir y recomendar anticiparlo con la notaria |
| El cliente pide opinion juridica sobre la estrategia sucesoria o fiscal optima | Derivar a `escalate_to_attorney` y, para lo fiscal, a un asesor de la comunidad autonoma aplicable |
