---
name: derecho-civil-compraventa-inmueble
description: >
  Genera el documento que corresponda en una compraventa de vivienda entre particulares conforme al
  Codigo Civil verificado en el BOE: contrato de arras o senal previo a la compraventa (Art. 1454 CC),
  contrato privado de compraventa de vivienda completo (Arts. 1445 y siguientes CC) y requerimiento
  extrajudicial de cumplimiento por incumplimiento de un contrato ya firmado (Arts. 1124 y 1504 CC).
  Trata expresamente la clase de arras y su consecuencia, las cargas del inmueble, el reparto de
  impuestos y gastos, la condicion suspensiva de financiacion hipotecaria y el derecho de tanteo y
  retracto del arrendatario (Art. 25 de la Ley 29/1994). NO sustituye la escritura publica notarial
  ni la inscripcion registral, no hace due diligence de titularidad ni valoracion del inmueble, y NO
  cubre la compraventa de local, la de obra nueva sobre plano con entregas a cuenta, ni las herencias
  o donaciones de inmuebles.
when_to_use: |
  - El usuario va a comprar o vender una vivienda y necesita el contrato de arras o senal previo.
  - El usuario necesita el contrato privado de compraventa de vivienda antes de ir al notario.
  - El usuario ya firmo un contrato de arras o de compraventa y la otra parte no cumple: no paga, no
    acude a la notaria en el plazo pactado o no entrega la posesion.
  - El usuario quiere saber que ocurre con las arras si una de las partes se echa atras.
  - El usuario compra con hipoteca aun no concedida y necesita proteger su posicion si le deniegan el
    prestamo.
  - El usuario compra o vende una vivienda que esta arrendada.
inputs:
  - documento: contrato de arras / contrato privado de compraventa / requerimiento de cumplimiento
  - posicion_cliente: comprador / vendedor
  - financiacion_pendiente: si / no
  - inmueble_arrendado: si / no / no lo se
  - datos_vendedor: nombre o razon social, NIF/CIF, domicilio, estado civil y regimen matrimonial, representacion
  - datos_comprador: nombre o razon social, NIF/CIF, domicilio, estado civil y regimen matrimonial, representacion
  - datos_inmueble: direccion, municipio, provincia, codigo postal, superficie, referencia catastral, datos registrales, anejos
  - precio_y_pago: precio total, arras, pagos a cuenta, importe al otorgamiento, medios de pago
  - clase_arras: confirmatorias / penales / penitenciales, y consecuencia pactada para cada parte
  - cargas: situacion registral, hipoteca pendiente, deudas de comunidad, IBI
  - estado_posesorio: libre / arrendado / con ocupantes, y notificacion al arrendatario
  - fiscalidad: reparto de ITP, plusvalia municipal y gastos de escritura e inscripcion
  - plazo_escritura: fecha limite de otorgamiento, notario y quien lo designa
  - datos_incumplimiento: obligacion incumplida, fecha de vencimiento, importe pendiente, requerimientos previos
outputs:
  - contrato_arras: contrato de arras o senal sobre bien inmueble en markdown, DRAFT
  - contrato_compraventa_vivienda: contrato privado de compraventa de vivienda en markdown, DRAFT
  - requerimiento_cumplimiento: requerimiento extrajudicial de cumplimiento en markdown, DRAFT
references:
  - references/fuentes-plantillas-validadas.md
  - references/arras-cargas-fiscalidad-y-retracto.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/contrato-arras.md
  - assets/contrato-compraventa-vivienda.md
  - assets/requerimiento-cumplimiento.md
---

# Compraventa de Vivienda: Arras, Contrato Privado y Requerimiento

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija del Punto 1 y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. La verificacion normativa del Punto 2 se ejecuta en silencio y se continua hasta la primera pregunta o hasta la Confirmacion visible del Punto 3, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno. La linea se emite una unica vez, al cargar, y no se repite en ningun turno posterior.

Esta linea es, junto con la introduccion fija del Punto 1 y los anuncios de seccion del Punto 5, la UNICA excepcion a la Directiva de Invisibilidad.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, la validacion de presupuestos, la verificacion normativa y la creacion base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol (ej. "HOJA ARRAS").
- Resumenes de validacion con checks (ej. "Cargas: ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez, en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin:

"Vamos a preparar el documento que corresponda a su operacion sobre el inmueble. Para ajustarlo a su caso, es necesario precisar antes algunos datos."

No amplies esta introduccion con la norma aplicable ni con el alcance concreto: eso se informa en el Punto 3, cuando la clasificacion ya esta resuelta.

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:

- **V1 (Documento necesario):** contrato de arras o senal previo / contrato privado de compraventa completo / requerimiento por incumplimiento de un contrato ya firmado.
- **V2 (Posicion del cliente):** comprador / vendedor. Determina que garantias se refuerzan y como se orientan los puntos de negociacion.
- **V3 (Financiacion pendiente — solo si V1 = arras o compraventa):** el pago no depende de financiacion pendiente / depende de un prestamo hipotecario aun no concedido.
- **V4 (Estado arrendaticio del inmueble — en las tres hojas):** libre de arrendatarios y ocupantes / arrendado / el cliente no lo sabe con certeza. Si esta arrendado, sub-vector: arrendamiento de vivienda / de local o para uso distinto de vivienda.

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto (omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama):

* Para V1:
  "El documento que necesita es:
  1. Un contrato de arras o senal, previo a la compraventa
  2. Un contrato privado de compraventa completo
  3. Un requerimiento por incumplimiento de un contrato ya firmado"

* Para V2:
  "En esta operacion usted interviene como:
  1. Comprador
  2. Vendedor"

* Para V4:
  "Respecto de la situacion del inmueble:
  1. Esta libre de arrendatarios y de ocupantes
  2. Esta arrendado
  3. No lo se con certeza"

* Sub-pregunta de V4, solo si la respuesta a V4 es 2:
  "El arrendamiento es:
  1. De vivienda
  2. De local o para un uso distinto de vivienda"

* Para V3 (solo si V1 = 1 o 2):
  "El pago del precio:
  1. No depende de ninguna financiacion pendiente de concesion
  2. Depende de un prestamo hipotecario que aun no esta concedido"

**Orden de las preguntas: por que V4 va antes que V3.** V4 puede dejar el caso fuera de alcance (arrendamiento de local) o cambiar por completo el deliverable (tanteo y retracto del arrendatario, con parada bloqueante en la validacion de presupuestos). V3 solo anade o quita una clausula. Preguntar primero V4 evita que el cliente invierta turnos en un documento que hay que replantear.

**PRINCIPIO: Preguntas simples, no mega-preguntas.** Cada pregunta resuelve un unico punto de decision. No comprimas V1 y V2 en una sola pregunta, ni V4 con su sub-pregunta.

**Si la respuesta a V4 es 3 ("no lo se con certeza"):** trata el caso, a efectos de validacion, como si estuviera arrendado (posicion conservadora) y aplica la parada bloqueante de la validacion de presupuestos, informando de que hay que comprobarlo antes de firmar.

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = 1 → **HOJA ARRAS**: `assets/contrato-arras.md`.
- Si V1 = 2 → **HOJA COMPRAVENTA**: `assets/contrato-compraventa-vivienda.md`.
- Si V1 = 3 → **HOJA REQUERIMIENTO**: `assets/requerimiento-cumplimiento.md`. V3 no se pregunta; V4 solo se usa para advertir del riesgo de retracto si el contrato ya firmado afecta a un inmueble arrendado sin notificar.
- Si V4 = 2 y el sub-vector es arrendamiento de local o para uso distinto de vivienda → **DETENER**: la compraventa de local esta fuera de alcance. Antes de escalar, advierte de que el articulo 31 de la Ley 29/1994 aplica al arrendamiento para uso distinto de vivienda el mismo regimen de tanteo y retracto del articulo 25, por lo que el riesgo de retracto tambien existe. Escalar. No crear documento.
- Si lo que se pretende es la compraventa de obra nueva **sobre plano con entregas a cuenta** del precio antes de la terminacion → **DETENER**: la disposicion adicional primera de la Ley 38/1999 exige garantizar la devolucion de las cantidades anticipadas mediante aval solidario de entidad de credito o seguro de caucion individualizado desde la obtencion de la licencia de edificacion, percibirlas en cuenta especial separada, y hacer constar en el contrato la obligacion de devolucion, la entidad garante y la cuenta. Advertir de esos requisitos y escalar. No crear documento.
- Si lo que se pretende es la transmision de un inmueble por herencia, legado, donacion, aportacion a sociedad, permuta, dacion en pago o adjudicacion en liquidacion de gananciales → **DETENER**: fuera de alcance. Derivar a `derecho-civil-herencia` cuando sea sucesorio, o escalar en los demas casos.
- Si el inmueble es un local comercial, una nave, un solar, una finca rustica o una plaza de garaje que se transmite de forma independiente → **DETENER**: los assets estan construidos para vivienda. Advertir y escalar.
- Si el caso se rige por derecho civil foral o especial (vecindad civil catalana, navarra, aragonesa, balear, gallega o vizcaina, o inmueble sujeto a esa legislacion) → **DETENER**: los assets se construyen sobre el Codigo Civil comun y Cataluna, entre otros territorios, regula la compraventa con reglas propias. Advertir y escalar.

### Validacion de presupuestos (interno, antes del Punto 3)

- **TODAS LAS HOJAS — legitimacion y titularidad.** Confirmar que el cliente es parte del contrato (o va a serlo) y, si es el vendedor, que es titular del inmueble. Si el inmueble pertenece a **varios cotitulares**, todos deben consentir la venta: pedir su relacion y advertir de que la firma de uno solo no vincula a los demas. Si el inmueble es la **vivienda habitual del matrimonio del vendedor**, advertir de que la disposicion requiere el consentimiento del otro conyuge y activar el bloque de comparecencia correspondiente.
- **TODAS LAS HOJAS — V4 arrendado, PARADA BLOQUEANTE (Art. 25 de la Ley 29/1994).** Si el inmueble esta arrendado como vivienda, **antes de continuar** informa del derecho de tanteo y retracto y pregunta si ya se ha notificado fehacientemente al arrendatario la decision de vender, el precio y las demas condiciones esenciales, y en que fecha. Tres salidas:
  1. **Notificacion practicada y transcurridos los treinta dias naturales sin tanteo:** continuar, activando el bloque de notificacion practicada del asset y pidiendo la fecha y el medio. Recordar que los efectos de la notificacion caducan a los ciento ochenta dias naturales: si la firma se retrasa mas alla, hay que volver a notificar.
  2. **Notificacion NO practicada:** advertir expresamente, en el mismo turno, de que (a) el arrendatario podra ejercitar el retracto sobre el inmueble ya vendido y subrogarse en la posicion del comprador reembolsandole el precio y los gastos (Art. 25.3 en relacion con el Art. 1518 CC), y (b) la escritura de venta de vivienda arrendada **no sera inscribible** en el Registro de la Propiedad sin justificar la notificacion (Art. 25.5), debiendo el vendedor declarar bajo pena de falsedad en documento publico que no estaba arrendada si asi fuera. Ofrecer dos vias: practicar la notificacion y esperar los treinta dias antes de firmar, o firmar condicionando la eficacia del contrato a la notificacion y al transcurso del plazo (bloque condicional del asset). **No continuar con el resto del documento hasta que el cliente elija una de las dos.**
  3. **El cliente alega que el arrendatario renuncio al derecho de adquisicion preferente:** **no dar por buena la renuncia.** Pedir el contrato de arrendamiento y comprobar que la renuncia es expresa (Art. 25.8) y que se ha practicado, o se va a practicar, la comunicacion de la intencion de vender con una **antelacion minima de treinta dias** a la fecha de formalizacion de la compraventa, que la renuncia no elimina. Si el contrato de arrendamiento no esta disponible, advertir y dejar el punto como pendiente de verificacion antes de la firma.
  - **Excepcion del Art. 25.7:** si la vivienda se vende conjuntamente con las restantes viviendas o locales del arrendador que forman parte del mismo inmueble, o distintos propietarios venden a un mismo comprador la totalidad de pisos y locales, no hay tanteo ni retracto. Pero **si en el inmueble solo existe una vivienda, si los hay**: no aplicar la excepcion a una casa unifamiliar arrendada. Verificar ademas si la normativa autonomica de vivienda atribuye tanteo y retracto a la Administracion en esos supuestos.
- **HOJA ARRAS y HOJA COMPRAVENTA — cargas (BLOQUEANTE en su redaccion).** Preguntar si se dispone de nota simple o certificacion registral actualizada. Si **no** se dispone: advertir de que no puede afirmarse que el inmueble esta libre de cargas, redactar la situacion registral **como manifestacion del vendedor** con la consecuencia pactada si resulta inexacta, y dejar constancia en el documento de la obligacion de comprobarlo antes de firmar. **Prohibido escribir que el inmueble esta libre de cargas sobre la sola afirmacion verbal del vendedor.** Recomendar siempre nota simple registral, certificado de la comunidad de propietarios con el visto bueno del presidente y ultimo recibo del IBI.
- **HOJA ARRAS — clase de arras (BLOQUEANTE).** El documento no puede cerrarse con la clase de arras sin pactar ni con la consecuencia del desistimiento sin redactar. Si el cliente no decide, no se cierra el documento: se explica de nuevo y se insiste, advirtiendo de que del silencio la jurisprudencia tiende a presumir el caracter confirmatorio, que **no** permite desistir.
- **HOJA COMPRAVENTA — obra nueva ya recibida.** Si la vivienda es de obra nueva y la obra ya esta recibida, activar el bloque de garantias de la Ley 38/1999 y pedir la fecha de recepcion de la obra, de la que se computan los plazos de diez, tres y un ano del Art. 17. Verificar que se entrega copia de las polizas del Art. 19. Si la obra **no** esta terminada y hay entregas a cuenta, aplicar la parada de enrutamiento.
- **HOJA REQUERIMIENTO — via del requerimiento (Art. 1504 CC, BLOQUEANTE).** Si el requirente es el **vendedor** y lo que busca es resolver la compraventa por impago del precio, verificar que el requerimiento se practicara **judicialmente o por acta notarial**. Un burofax constituye en mora, fija la fecha e interrumpe la prescripcion, pero **no cierra la facultad del comprador de pagar tardiamente**: mientras no medie requerimiento judicial o notarial, podra pagar aun despues de vencido el plazo y evitar la resolucion, y hecho el requerimiento el Juez no podra concederle nuevo termino. Si el cliente quiere enviar solo un burofax, advertirlo expresamente y dejarlo escrito en el documento.
- **HOJA REQUERIMIENTO — prescripcion (Art. 1964.2 CC).** Calcular si han transcurrido cinco anos desde que la obligacion era exigible. Si el plazo esta agotado o proximo a agotarse, advertir y escalar antes de redactar; recordar que la reclamacion extrajudicial interrumpe la prescripcion (Art. 1973 CC), de modo que la fecha del requerimiento es relevante.
- **HOJA REQUERIMIENTO — saneamiento por vicios ocultos (Art. 1490 CC).** Si lo que el cliente quiere reclamar son vicios o defectos ocultos, verificar que no han transcurrido **seis meses desde la entrega**. Si han transcurrido, advertir de que la accion de saneamiento esta extinguida y escalar: no dar falsas expectativas. Recordar que el vendedor no responde de los defectos manifiestos o que estuvieren a la vista (Art. 1484).
- **TODAS LAS HOJAS — fiscalidad.** No calcular la cuota del ITP ni de la plusvalia municipal: el tipo del ITP lo fija cada Comunidad Autonoma y la plusvalia depende de la ordenanza municipal. Identificar al sujeto pasivo legal y remitir a la normativa aplicable.

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del Codigo Civil, de la LAU, de la LOE, del ITPAJD, del TRLRHL y de la LGT.

**2.2 — Consultar la fuente oficial vigente.** La API de legislacion consolidada del BOE devuelve el bloque de un articulo concreto (requiere cabecera `Accept: application/xml`). **La version vigente es la ULTIMA `<version>` del bloque, no la primera.**
```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{ID_BOE}/texto/bloque/{bloque}
```
Consultar:
- **Codigo Civil (BOE-A-1889-4763)**, bloques `artNNNN`: `art1445`, `art1450`, `art1454`, `art1455`, `art1461`, `art1462`, `art1465`, `art1468`, `art1469`, `art1474`, `art1475`, `art1483`, `art1484`, `art1485`, `art1486`, `art1490`, `art1500`, `art1502`, `art1503`, `art1504`, `art1124`, `art1152`, `art1255`, `art1279`, `art1280`, `art1518`, `art1875`, `art1964`, `art1973`.
- **LAU, Ley 29/1994 (BOE-A-1994-26003)**, bloques `aNN`: `a25` y `a31`.
- **LOE, Ley 38/1999 (BOE-A-1999-21567)**: `a17`, `a19`, `a20` y `daprimera` (la disposicion adicional primera responde a `daprimera`; `da1` devuelve 404).
- **ITPAJD, RDLeg 1/1993 (BOE-A-1993-25359)**: `a8`.
- **TRLRHL, RDLeg 2/2004 (BOE-A-2004-4214)**: `a106`.
- **LGT, Ley 58/2003 (BOE-A-2003-23186)**: `a17`.

**2.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar `Write`/`Edit` para:
- Actualizar `references/fuentes-plantillas-validadas.md` (tablas de articulos verificados y tabla "Version registrada", con las fechas) y `references/arras-cargas-fiscalidad-y-retracto.md` si cambia el contenido sustantivo.
- Actualizar los assets afectados con la redaccion vigente, en particular las remisiones a articulos concretos.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**2.5 — Verificacion especifica del Art. 1454 CC (obligatoria en toda hoja que trate arras).** Comprobar en el bloque `art1454` que el precepto sigue diciendo unicamente lo que dice hoy: que el contrato podra rescindirse allanandose el comprador a perder las arras o el vendedor a devolverlas duplicadas. **El Codigo Civil NO clasifica las arras.** Si al verificar apareciese una redaccion nueva que si las clasificase, actualizar las references y el asset antes de redactar. Mientras no ocurra, la triple calificacion (confirmatorias, penales, penitenciales) se explica siempre como **construccion jurisprudencial**, nunca como categoria legal, y **nunca se cita el Art. 1454 como fundamento de las arras confirmatorias o penales**.

**2.6 — Fallback si la fuente no es accesible.** Si la lectura falla (error HTTP, timeout):
```
web_search("Codigo Civil articulo 1454 arras 1504 resolucion venta inmuebles texto consolidado BOE")
web_search("Ley 29/1994 Arrendamientos Urbanos articulo 25 tanteo retracto texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del Codigo Civil en el BOE. El documento se genera con la version de referencia. Verifique manualmente antes de firmar."

**Prohibido dar por vigente lo que no se ha podido verificar.**

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Textos fijos por hoja:
   - ARRAS: "A su caso corresponde un contrato de arras o senal previo a la compraventa, regido por el Codigo Civil y, en cuanto a las arras entregadas, por su articulo 1.454. Debe saber que ese articulo solo contempla el desistimiento perdiendo las arras o devolviendolas duplicadas: la distincion entre arras confirmatorias, penales y penitenciales no figura en el Codigo, la ha construido la jurisprudencia, y por ello es imprescindible pactar expresamente en el contrato de que clase son y que ocurre si una parte se retira. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - COMPRAVENTA: "A su caso corresponde un contrato privado de compraventa de vivienda, regido por los articulos 1.445 y siguientes del Codigo Civil. Debe saber que este documento obliga a ambas partes, pero no transmite la propiedad frente a terceros ni permite inscribir la vivienda a su nombre en el Registro de la Propiedad: para ello es necesaria la escritura publica notarial, conforme al articulo 1.280.1.º del Codigo Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - REQUERIMIENTO: "A su caso corresponde un requerimiento extrajudicial de cumplimiento, con fundamento en el articulo 1.124 del Codigo Civil, que le permite optar entre exigir el cumplimiento o resolver el contrato, con resarcimiento de danos e intereses en ambos casos. Tratandose de venta de bien inmueble, el articulo 1.504 del mismo Codigo permite al comprador pagar el precio aun despues de vencido el plazo mientras no haya sido requerido judicialmente o por acta notarial. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - En las hojas ARRAS y COMPRAVENTA, si el inmueble esta arrendado como vivienda, anadir: "Al estar el inmueble arrendado, resulta ademas de aplicacion el derecho de tanteo y retracto del arrendatario, previsto en el articulo 25 de la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003"
   - En la hoja COMPRAVENTA, si la vivienda es de obra nueva ya recibida, anadir: "Al tratarse de obra nueva, resultan ademas de aplicacion las garantias por vicios y defectos de la construccion del articulo 17 de la Ley 38/1999, de 5 de noviembre, de Ordenacion de la Edificacion, con plazos de diez, tres y un ano desde la recepcion de la obra. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1999-21567"
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio. Si el documento adjuntado los incumple —por ejemplo, si dice "arras" sin decir de que clase, si afirma que el inmueble esta libre de cargas sin comprobacion, o si no menciona la notificacion al arrendatario en una vivienda arrendada—, adviertelo expresamente antes de trabajar sobre el.

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento:

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa e investigacion: incluida `fecha_verificacion_normativa` del Punto 2). Los faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{clase_arras}}`, `{{referencia_catastral}}`); usa un marcador generico solo para un hueco suelto sin placeholder propio, y nunca repitas el mismo marcador generico dos veces en el mismo documento (`Edit` necesita un `oldString` unico).
3. Utiliza `Write` para guardar el archivo en disco, con nombre en `snake_case.md`: `contrato_arras_vendedor_a_comprador_a.md`, `contrato_compraventa_vivienda_vendedor_a_comprador_a.md`, `requerimiento_cumplimiento_comprador_a.md`.
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. En esa MISMA respuesta, sin turno intermedio y sin preguntar si desea empezar, emite el anuncio fijo de la primera seccion y formula ya su primera pregunta, para que el flujo no se detenga (regla del `CLAUDE.md` raiz, seccion 6.1, punto 5, y coherencia con el Punto 0: la skill esta en ejecucion desde que se carga).

Los bloques condicionales del asset que dependan de decisiones aun no tomadas se OMITEN en este `Write` y se insertan durante el Punto 5, releyendo el asset y copiando el bloque **sin el envoltorio de comentario**. El documento escrito en disco no contiene ningun `<!-- ... -->`. En las clausulas que ofrecen bloques alternativos (clase de arras, financiacion), se inserta **uno solo**.

## 5. EDICION INCREMENTAL DE CLAUSULAS

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas de negociacion se explican y se confirman una a una. **La vista previa y la confirmacion agrupada de una parte se emiten en el turno SIGUIENTE a la respuesta del ultimo sub-apartado, nunca en el mismo turno en que aun se esta preguntando ese ultimo dato.**

**En los puntos marcados `[negociacion]`, explica antes de pedir la decision.** No registres el valor que dé el cliente sin haberle expuesto el regimen por defecto y la consecuencia de cada opcion, y sin confirmar que lo entiende y lo acepta. El material sustantivo de esas explicaciones esta en `references/arras-cargas-fiscalidad-y-retracto.md`. **Orienta la explicacion segun V2:** un mismo punto se explica distinto al comprador y al vendedor, porque el riesgo es distinto para cada uno.

**Validacion de sentido, no solo de formato.** Antes de escribir una respuesta en el documento, razona si tiene sentido: un precio de 300 euros por una vivienda, unas arras superiores al precio, una fecha de escritura anterior a la del contrato o una superficie de 3 m² no son datos validos. Senala por que no encaja y pide aclaracion antes de continuar.

### Secciones — HOJA ARRAS

1. **Parte vendedora** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio fijo: "Comenzamos por la identificacion de la parte vendedora." Sub-apartados, uno por turno: a) nombre completo o razon social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) estado civil y regimen economico matrimonial; e) titulo por el que adquirio el inmueble. Si es persona juridica, pedir en su lugar los datos del representante y su titulo de representacion. Si hay varios cotitulares, pedir su relacion y advertir de que todos deben firmar. Al recibir la respuesta al ultimo dato, en el turno siguiente, vista previa unica y una sola confirmacion antes del `Edit`.
2. **Parte compradora** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio fijo: "Pasamos a la identificacion de la parte compradora." Sub-apartados: a) nombre o razon social; b) NIF o CIF; c) domicilio; d) estado civil y regimen economico matrimonial. Confirmacion agrupada.
3. **El inmueble** *[dato objetivo con validacion]*. Anuncio fijo: "Describimos ahora el inmueble objeto de la operacion." Sub-apartados, uno por turno: a) direccion completa, municipio, provincia y codigo postal; b) superficie construida y descripcion; c) referencia catastral; d) datos registrales (Registro, tomo, libro, folio y finca); e) anejos que se incluyen, si los hay. Los datos que el cliente no tenga quedan como placeholder y se advierte de que deben completarse antes de firmar: **no se inventan**.
4. **Precio y forma de pago** *[negociacion]*. Anuncio fijo: "Pasamos a determinar el precio y la forma de pago." Explica antes de pedir cifras: el precio debe expresarse en cifra y en letra, prevaleciendo la letra en caso de discordancia, y la forma de pago debe desglosarse por partidas, fechas y medios de pago, porque el otorgamiento de la escritura exigira acreditar cada medio de pago. Pide despues, en turnos separados: a) precio total; b) importe que quedara pendiente para el otorgamiento; c) medio de pago de cada partida y cuenta de destino.
5. **Importe de las arras** *[negociacion]*. Anuncio fijo: "Concretamos el importe de la senal." Explica que no hay importe legal y que en la practica se mueve entre el 5 % y el 10 % del precio; que un importe bajo apenas disuade de retirarse y uno alto expone al comprador a una perdida grave. Pide el importe y el medio de entrega.
6. **Clase de arras y su consecuencia** *[negociacion — punto critico de la skill]*. Anuncio fijo: "Determinamos ahora la clase de arras y sus consecuencias, que es el punto mas relevante de este contrato." Antes de pedir la decision, explica los tres puntos siguientes, siempre en este orden:
   - Que el articulo 1.454 del Codigo Civil solo dice que, si median arras, el contrato podra rescindirse allanandose el comprador a perderlas o el vendedor a devolverlas duplicadas, y que **la clasificacion en arras confirmatorias, penales y penitenciales no esta en el Codigo: la ha construido la jurisprudencia**.
   - Que ocurre con cada clase si una parte se echa atras: las **confirmatorias** son senal y anticipo del precio y **no permiten desistir** (quien se retira incumple, y la otra parte puede exigir el cumplimiento o resolver con danos e intereses, articulo 1.124); las **penales** anaden una pena convencional, tampoco permiten desistir, y **la pena sustituye a la indemnizacion de danos salvo que se pacte lo contrario** (articulo 1.152); las **penitenciales** son el precio de la facultad de desistir, y son las unicas que encajan en el articulo 1.454: quien desiste pierde las arras, o las devuelve duplicadas, y el contrato queda sin efecto sin mas consecuencias.
   - Que **el silencio juega en contra de quien quiere desistir**: si el contrato no dice de que clase son, la jurisprudencia tiende a presumir el caracter confirmatorio, el mas restrictivo para retirarse.
   Orienta segun V2: al **comprador** que quiere una salida por si no le conceden la hipoteca, adviertele de que las arras penitenciales le hacen perder la senal y que para recuperarla necesita ademas la condicion suspensiva de financiacion; al **vendedor** que quiere asegurar la venta, adviertele de que las penitenciales dejan al comprador retirarse perdiendo solo la senal. Pide despues la decision y confirma que entiende la consecuencia antes de escribirla. **Esta seccion no puede cerrarse sin la clase pactada.**
7. **Plazo y notaria para la escritura** *[negociacion]*. Anuncio fijo: "Fijamos el plazo para el otorgamiento de la escritura publica." Explica que sin fecha limite la obligacion es dificil de exigir, y que conviene pactar quien designa notario y con cuanta antelacion debe convocarse a la otra parte. Pide: a) fecha limite; b) notario o parte que lo designa; c) dias de antelacion de la convocatoria.
8. **Cargas del inmueble** *[negociacion]*. Anuncio fijo: "Abordamos la situacion de cargas del inmueble." Explica que la hipoteca sigue a la finca y solo se extingue con su cancelacion registral; que las deudas de comunidad y el IBI afectan al propio inmueble frente al nuevo adquirente; y que las cargas o servidumbres no aparentes no mencionadas dan al comprador, conforme al articulo 1.483 del Codigo Civil, un plazo de solo un ano desde el otorgamiento de la escritura para pedir la rescision o la indemnizacion. Recomienda nota simple registral, certificado de la comunidad con el visto bueno del presidente y ultimo recibo del IBI. Pide: a) si dispone de nota simple y que refleja; b) si hay hipoteca pendiente, su entidad e importe, y si se cancela con retencion del precio o se pretende subrogacion, advirtiendo de que la subrogacion exige el consentimiento de la entidad y no puede darse por hecha.
9. **Estado posesorio y arrendatarios** *[negociacion]*. Anuncio fijo: "Determinamos el estado posesorio del inmueble." El valor de V4 ya esta resuelto y la parada bloqueante de la validacion de presupuestos ya se ha aplicado. Si esta arrendado: recoge la fecha del contrato de arrendamiento, su fecha de vencimiento, el nombre del arrendatario, la fecha y el medio de la notificacion, y activa el bloque que corresponda (notificacion practicada, renuncia comprobada, o condicion de eficacia). Si esta libre: pide la manifestacion del vendedor y, si hay ocupantes que deban salir, la fecha de desalojo y la consecuencia del retraso.
   **El valor de V4 gobierna ademas otras dos clausulas del asset, y hay que resolverlas en coherencia con esta:** la clausula quinta (entrega de llaves si esta libre, entrega de la documentacion del arrendamiento si esta arrendado) y la clausula sexta (obligacion de entregar libre de arrendatarios y ocupantes solo si esta libre; si esta arrendado, el inmueble se transmite con el arrendamiento subsistente y el comprador se subroga conforme al articulo 14 de la Ley 29/1994). Cada una ofrece dos bloques alternativos: inserta uno solo y el mismo en las tres. **Un contrato que en la clausula sexta obligue a entregar libre de arrendatarios y en la septima describa un arrendamiento vigente es un contrato contradictorio: no puede cerrarse asi.**
10. **Financiacion** *[negociacion — condicional, solo si V3 = 2]*. Anuncio fijo: "Valoramos como protegerle si la financiacion no llega a concederse." Explica que sin esta clausula la denegacion del prestamo convierte al comprador en incumplidor, con perdida de las arras o algo peor si son confirmatorias o penales, y que la condicion suspensiva convierte la denegacion en un supuesto previsto y no culpable. Pide, en turnos separados, los cuatro elementos: a) importe minimo de financiacion y fecha limite; b) destino de las arras si no se concede, ofreciendo por defecto la devolucion integra; c) como se acredita la denegacion (denegacion escrita, numero minimo de entidades y plazo), advirtiendo de que sin acreditacion documental el comprador que se retira alegando denegacion queda en una posicion muy debil; d) que ocurre si el plazo vence sin respuesta del banco. Orienta segun V2: al comprador, plazo amplio y devolucion integra; al vendedor, plazo corto y exigencia de acreditar diligencia. Si V3 = 1, activa el bloque de que no hay condicion suspensiva y **no formules las preguntas de esta seccion**.
11. **Impuestos y gastos** *[negociacion]*. Anuncio fijo: "Pasamos al reparto de impuestos y gastos." Explica el reparto legal: el ITP a cargo del comprador (articulo 8.a) del Real Decreto Legislativo 1/1993, "cualesquiera que sean las estipulaciones establecidas por las partes en contrario"); la plusvalia municipal a cargo del vendedor (articulo 106.1.b) del Real Decreto Legislativo 2/2004); los gastos de otorgamiento de la escritura a cargo del vendedor y los de la primera copia e inscripcion a cargo del comprador (articulo 1.455 del Codigo Civil); y la cancelacion de cargas a cargo del vendedor. Advierte de que **el pacto en contra vincula a las partes pero no a la Administracion**, que seguira exigiendo cada impuesto a su sujeto pasivo legal (articulo 17.5 de la Ley 58/2003), de modo que el pacto crea una accion de reembolso, no un cambio de contribuyente. No calcules cuotas: el tipo del ITP lo fija cada Comunidad Autonoma y la plusvalia depende de la ordenanza municipal. Pregunta si se mantiene el reparto legal o se pacta otro distinto y, en este ultimo caso, activa el bloque con la advertencia incorporada al documento.
12. **Notificaciones** *[dato objetivo]*. Anuncio fijo: "Cerramos las vias de comunicacion entre las partes." Pide los correos electronicos de cada parte y recuerda que las comunicaciones con efecto resolutorio o de desistimiento deben practicarse por medio que acredite contenido y recepcion.
13. **Lugar, fecha y ejemplares** *[dato objetivo]*. Anuncio fijo: "Cerramos con el lugar, la fecha y el numero de ejemplares." Municipio y fecha de firma (fecha del dia salvo indicacion en contrario) y numero de ejemplares.

### Secciones — HOJA COMPRAVENTA

1. **Parte vendedora** *[dato objetivo — confirmacion agrupada por parte]*. Igual que en la HOJA ARRAS, anadiendo el sub-apartado del consentimiento del conyuge si el inmueble es vivienda habitual del matrimonio.
2. **Parte compradora** *[dato objetivo — confirmacion agrupada por parte]*. Igual que en la HOJA ARRAS, anadiendo la proporcion de adquisicion si compran varias personas.
3. **El inmueble** *[dato objetivo con validacion]*. Igual que en la HOJA ARRAS, anadiendo superficie util, linderos y, si procede, el inventario de mobiliario del Anexo I. Si la venta se hace con expresion de cabida y precio por unidad de medida, adviertelo y aplica el regimen del articulo 1.469 del Codigo Civil (rebaja proporcional o rescision si la diferencia excede de la decima parte); si se vende como cuerpo cierto, dejalo escrito expresamente.
4. **Precio** *[negociacion]*. Anuncio fijo: "Pasamos a determinar el precio de la compraventa." Igual explicacion que en la HOJA ARRAS sobre cifra y letra. Pide el precio total y recoge la manifestacion de que es el realmente convenido.
5. **Forma de pago** *[negociacion]*. Anuncio fijo: "Concretamos la forma de pago." Pide, en turnos separados: a) arras o cantidades ya entregadas, con fecha y medio; b) importe que se entrega en el acto de la firma; c) importe pendiente para el otorgamiento de la escritura; d) medio de pago de cada partida y cuenta de destino. Recuerda la obligacion de conservar los justificantes.
6. **Cargas, gravamenes y deudas** *[negociacion]*. Igual que la seccion 8 de la HOJA ARRAS, anadiendo la obligacion del vendedor de aportar la certificacion de la comunidad y el ultimo recibo del IBI antes del otorgamiento, y la posibilidad de que el comprador acepte expresamente una carga que subsista.
7. **Estado posesorio y derecho de adquisicion preferente** *[negociacion]*. Igual que la seccion 9 de la HOJA ARRAS. Si esta arrendado y ya se notifico, anade la obligacion del **comprador** de notificar despues al arrendatario las condiciones esenciales en que se efectuo la compraventa, con copia de la escritura, a los efectos del computo del plazo de retracto del articulo 25.3.
8. **Otorgamiento de la escritura publica** *[negociacion]*. Anuncio fijo: "Fijamos el otorgamiento de la escritura publica." Igual que la seccion 7 de la HOJA ARRAS, anadiendo que cualquiera de las partes puede compeler a la otra al otorgamiento desde la perfeccion del contrato (articulo 1.279 del Codigo Civil).
9. **Entrega de la posesion** *[negociacion]*. Anuncio fijo: "Determinamos cuando se entrega la posesion de la vivienda." Explica que el otorgamiento de la escritura publica equivale a la entrega salvo pacto en contrario (articulo 1.462 del Codigo Civil), y que los frutos y gastos ordinarios se imputan al comprador desde la entrega (articulo 1.468). Pregunta si la posesion se entrega en el otorgamiento o antes; si se entrega antes, advierte de que la propiedad no se transmite hasta la escritura y activa el bloque de ocupacion en precario.
10. **Financiacion** *[negociacion — condicional, solo si V3 = 2]*. Igual que la seccion 10 de la HOJA ARRAS.
11. **Impuestos y gastos** *[negociacion]*. Igual que la seccion 11 de la HOJA ARRAS. Si la transmision es primera entrega de edificacion, activa el bloque de IVA y AJD en lugar del ITP.
12. **Estado de la vivienda y saneamiento** *[negociacion]*. Anuncio fijo: "Abordamos el estado de la vivienda y la responsabilidad por vicios ocultos." Explica: el vendedor responde de la posesion legal y pacifica y de los vicios o defectos ocultos (articulo 1.474), **aunque los ignorase** (articulo 1.485), pero **no** de los defectos manifiestos o que estuvieren a la vista, ni de los que no lo estuvieran si el comprador es un perito que por su oficio debia conocerlos (articulo 1.484); ante el vicio oculto el comprador puede desistir con abono de gastos o pedir rebaja proporcional del precio, y ademas danos y perjuicios si el vendedor lo conocia y no lo manifesto (articulo 1.486); y las acciones de saneamiento **se extinguen a los seis meses desde la entrega** (articulo 1.490). Orienta segun V2: al **comprador**, recomiendale hacer constar por escrito los defectos que ya conoce y no aceptar una exoneracion generica de saneamiento; al **vendedor**, recomiendale declarar los defectos que conoce, porque ocultarlos sabiendolos abre la puerta a la indemnizacion de danos del articulo 1.486. Pide la relacion de defectos que el vendedor declara y pregunta si se pacta alguna modulacion de la responsabilidad por eviccion (articulo 1.475, que permite aumentarla, disminuirla o suprimirla).
13. **Obra nueva** *[negociacion — condicional, solo si la vivienda es de obra nueva ya recibida]*. Anuncio fijo: "Concretamos las garantias aplicables por tratarse de obra nueva." Explica los plazos del articulo 17 de la Ley 38/1999 contados desde la recepcion de la obra sin reservas o desde la subsanacion de estas: diez anos por danos en elementos estructurales que comprometan la resistencia y la estabilidad, tres anos por vicios que incumplan los requisitos de habitabilidad, y un ano por vicios de ejecucion en elementos de terminacion o acabado; y que el promotor responde solidariamente frente a los adquirentes. Pide la fecha de recepcion de la obra y confirma que se entregan copia de las polizas del articulo 19 y la licencia de primera ocupacion.
14. **Documentacion que aportara el vendedor** *[dato objetivo]*. Anuncio fijo: "Relacionamos la documentacion que el vendedor debera aportar." Repasa la lista del asset y pregunta si hay documentacion adicional propia del caso.
15. **Incumplimiento y remedios** *[negociacion]*. Anuncio fijo: "Determinamos las consecuencias del incumplimiento." Explica el articulo 1.124 del Codigo Civil (opcion entre cumplimiento y resolucion, con danos e intereses en ambos casos) y, con especial claridad, el articulo 1.504: en la venta de inmuebles, **aun con pacto de resolucion de pleno derecho por impago, el comprador puede pagar mientras no haya sido requerido judicialmente o por acta notarial**, y hecho el requerimiento el Juez no podra concederle nuevo termino. Orienta segun V2: al **vendedor**, adviertele de que un simple burofax no cierra el plazo de pago del comprador; al **comprador**, informale de que dispone de esa ventana y de la facultad de suspender el pago si es perturbado en la posesion o teme fundadamente una accion reivindicatoria o hipotecaria (articulo 1.502). Pregunta si se pacta clausula penal y, si se pacta, **su importe y si sustituye o se acumula** a la indemnizacion de danos, advirtiendo de que a falta de pacto **sustituye** (articulo 1.152).
16. **Notificaciones** *[dato objetivo]*. Igual que la seccion 12 de la HOJA ARRAS.
17. **Lugar, fecha y ejemplares** *[dato objetivo]*. Igual que la seccion 13 de la HOJA ARRAS.

### Secciones — HOJA REQUERIMIENTO

1. **Parte requirente** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio fijo: "Comenzamos por la identificacion de quien practica el requerimiento." Sub-apartados, uno por turno: a) nombre o razon social; b) NIF o CIF; c) domicilio; d) via de contacto para el cumplimiento voluntario. Su condicion en el contrato (comprador o vendedor) ya esta resuelta por V2: no la preguntes de nuevo. Confirmacion agrupada.
2. **Parte requerida** *[dato objetivo — confirmacion agrupada por parte]*. Anuncio fijo: "Pasamos a la identificacion del destinatario del requerimiento." Sub-apartados: a) nombre o razon social; b) NIF o CIF; c) domicilio al que se dirigira la comunicacion.
3. **El contrato y el inmueble** *[dato objetivo con validacion]*. Anuncio fijo: "Describimos el contrato incumplido y el inmueble al que se refiere." Sub-apartados, uno por turno: a) tipo y fecha del contrato firmado; b) direccion, referencia catastral y datos registrales del inmueble; c) precio total pactado.
4. **La obligacion incumplida** *[dato objetivo con validacion]*. Anuncio fijo: "Concretamos la obligacion incumplida y su vencimiento." Sub-apartados, uno por turno: a) que obligacion se pacto y con que vencimiento; b) en que consiste el incumplimiento; c) importe pendiente, si es dinerario; d) convocatorias o requerimientos previos, con su fecha y medio. Aplica aqui las validaciones de prescripcion (articulo 1.964.2) y, si lo reclamado son vicios ocultos, del plazo de seis meses del articulo 1.490.
5. **Via del requerimiento** *[negociacion — critica si el requirente es el vendedor]*. Anuncio fijo: "Determinamos por que via debe practicarse el requerimiento." Explica la diferencia con precision: un **burofax** con acuse de recibo y certificacion de texto constituye en mora, fija la fecha e interrumpe la prescripcion (articulo 1.973), y es suficiente si lo que se busca es exigir el cumplimiento; un **acta notarial** (o el requerimiento judicial) es lo que exige el articulo 1.504 del Codigo Civil para **cerrar la facultad del comprador de pagar tardiamente** en la venta de inmuebles. Si V2 = vendedor y el incumplimiento es el impago del precio, recomienda expresamente el acta notarial y advierte de que con burofax el comprador podra pagar despues del plazo y evitar la resolucion. Pregunta que via se va a emplear y activa el bloque correspondiente del asset.
6. **Conducta exigida y plazo** *[negociacion]*. Anuncio fijo: "Fijamos que se exige y en que plazo." Explica que el requerimiento debe pedir una conducta concreta, con plazo y forma de cumplimiento, y que un requerimiento generico pierde eficacia. Pide, en turnos separados: a) conducta exigida (pago del precio, otorgamiento de la escritura, entrega de la posesion, cancelacion de una carga no declarada); b) plazo de cumplimiento; c) si es pago, medio y cuenta; si es otorgamiento, notario, direccion, dia y hora, y documentacion a aportar.
7. **Opcion del articulo 1.124** *[negociacion]*. Anuncio fijo: "Determinamos que accion se anuncia si el requerimiento no se atiende." Explica que el articulo 1.124 permite optar entre exigir el cumplimiento y resolver el contrato, con resarcimiento de danos e intereses en ambos casos, y que puede pedirse la resolucion aun despues de haber optado por el cumplimiento cuando este resulte imposible. Orienta segun V2 y segun el interes real del cliente: quien quiere la vivienda pide el cumplimiento; quien quiere desvincularse pide la resolucion. Si V2 = comprador y la obligacion incumplida es el otorgamiento de la escritura, informa de que puede compeler al vendedor conforme al articulo 1.279. Pide la opcion y confirma que entiende su consecuencia.
8. **Clausula penal o arras pactadas** *[negociacion — condicional]*. Anuncio fijo: "Valoramos si procede reclamar la pena o las arras pactadas." Solo si el contrato incumplido preve arras con consecuencia pactada o clausula penal. Explica que a falta de pacto expreso la pena **sustituye** a la indemnizacion de danos e intereses (articulo 1.152), de modo que reclamar la pena puede cerrar la via de reclamar el dano real si este es mayor. Pide el importe y la clausula que lo pacta.
9. **Suspension del pago** *[negociacion — condicional, solo si V2 = comprador y hay perturbacion o riesgo de accion reivindicatoria o hipotecaria]*. Anuncio fijo: "Valoramos si procede suspender el pago del precio pendiente." Explica el articulo 1.502: el comprador perturbado en la posesion o dominio, o con fundado temor de serlo por accion reivindicatoria o hipotecaria, puede suspender el pago hasta que cese la perturbacion o el peligro, salvo que el vendedor afiance la devolucion o se haya estipulado lo contrario. Pide la descripcion de la perturbacion o del riesgo.
10. **Lugar y fecha** *[dato objetivo]*. Anuncio fijo: "Cerramos con el lugar y la fecha del requerimiento." Municipio y fecha (fecha del dia salvo indicacion en contrario). Recuerda que la fecha es relevante a efectos de mora y de interrupcion de la prescripcion.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: una materia por clausula, toda obligacion con sujeto, verbo, plazo y consecuencia, precio y arras en cifra y en letra, inmueble identificado con referencia catastral y datos registrales, voz activa, sin latinismos, y cero clausulas que las partes no hayan decidido.

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5, muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una clausula existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

Antes de dar el documento por bueno, verifica con un `Read` final que:
- No queda ningun `<!-- ... -->` en el archivo.
- La clase de arras esta pactada si la hoja es de arras, con su consecuencia redactada. Si la clase pactada **no** es penitencial, el documento **no** cita el articulo 1.454 en ninguna clausula, tampoco en la de legislacion aplicable.
- El estado posesorio es coherente en todo el documento: si el inmueble esta arrendado, ninguna clausula obliga a entregarlo libre de arrendatarios ni a entregar las llaves al comprador en el otorgamiento.
- No se ha escrito que el inmueble esta libre de cargas sin comprobacion registral.
- **No queda ningun placeholder `{{...}}` sin resolver.** En particular, si el cliente no ha pedido clausulas adicionales, elimina con `Edit` el apartado "CLAUSULAS ADICIONALES" completo junto con su placeholder y el separador que lo precede: un placeholder residual se muestra al cliente como texto literal del contrato. Si queda algun otro placeholder porque el dato no existe todavia (numero de protocolo, notario aun no designado), informa al cliente de cuales son y de que deben completarse antes de la firma, en lugar de cerrarlos en silencio.

## Guardrails

1. Verificar siempre el Codigo Civil, la LAU, la LOE y las normas fiscales en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder. Recordar que la version vigente es la ULTIMA `<version>` de cada bloque de la API.
2. **El contrato privado no transmite la propiedad frente a terceros ni permite inscribir en el Registro de la Propiedad: hace falta escritura publica notarial (Art. 1280.1.º CC).** Advertirlo siempre, en el chat y en el propio documento. Nunca dar a entender al cliente que con el contrato privado la vivienda ya es suya a todos los efectos, ni que puede obtener hipoteca sobre ella (la hipoteca solo queda validamente constituida con su inscripcion, Art. 1875 CC).
3. **La clasificacion de las arras en confirmatorias, penales y penitenciales es jurisprudencial, no legal.** El Art. 1454 CC solo contempla el desistimiento. Prohibido presentar los tres tipos como categorias del Codigo Civil o citar el Art. 1454 como fundamento de las confirmatorias o penales. El documento debe pactar **expresamente** la clase y su consecuencia: del silencio la jurisprudencia tiende a presumir el caracter confirmatorio, que no permite desistir.
4. **Nunca redactar una compraventa sin comprobar las cargas del inmueble**, ni escribir que esta libre de cargas sobre la sola afirmacion verbal del vendedor. Recomendar siempre nota simple o certificacion registral, certificado de la comunidad de propietarios y ultimo recibo del IBI.
5. **Nunca dar por buena una renuncia del arrendatario al retracto sin verificar los requisitos del Art. 25 de la Ley 29/1994**: renuncia expresa en el contrato de arrendamiento (Art. 25.8) y comunicacion de la intencion de vender con antelacion minima de treinta dias a la formalizacion de la compraventa, que la renuncia no elimina. Si el inmueble esta arrendado y no se ha notificado la venta, advertir del retracto y de la no inscribibilidad de la escritura (Art. 25.5) **antes** de continuar con el documento.
6. En **obra nueva**, activar las garantias de la Ley 38/1999 (Art. 17: diez, tres y un ano desde la recepcion de la obra) y verificar la entrega de las polizas del Art. 19. Si la venta es **sobre plano con entregas a cuenta**, detener: exige aval solidario de entidad de credito o seguro de caucion individualizado y cuenta especial separada (disposicion adicional primera de la Ley 38/1999). No redactar ese contrato.
7. El **pacto fiscal en contra del reparto legal no vincula a la Administracion** (Art. 17.5 LGT): el ITP se exige al comprador (Art. 8.a) RDLeg 1/1993) y la plusvalia municipal al vendedor (Art. 106.1.b) RDLeg 2/2004), y el pacto solo genera una accion de reembolso entre las partes. Advertirlo siempre que se pacte otro reparto. **No calcular cuotas**: el tipo del ITP es autonomico y la plusvalia depende de la ordenanza municipal.
8. En el **requerimiento por impago del precio de un inmueble**, si el objetivo es resolver, debe practicarse **judicialmente o por acta notarial** (Art. 1504 CC). Advertir siempre de que un burofax no cierra la facultad del comprador de pagar tardiamente.
9. Las **acciones de saneamiento por vicios ocultos se extinguen a los seis meses desde la entrega** (Art. 1490 CC) y las derivadas de cargas o servidumbres no aparentes al ano desde el otorgamiento de la escritura (Art. 1483 CC). Comprobar el plazo antes de anunciar una reclamacion; no dar falsas expectativas.
10. Nunca redactar clausulas que exoneren al vendedor del saneamiento de forma generica cuando conoce los vicios: el Art. 1485 solo excluye la responsabilidad si se estipulo lo contrario **y** el vendedor los ignoraba, y el Art. 1486 impone indemnizacion de danos al vendedor que los conocia y no los manifesto.
11. Si el inmueble tiene **varios cotitulares**, la firma de uno solo no vincula a los demas. Si es la **vivienda habitual del matrimonio**, la disposicion requiere el consentimiento del otro conyuge. Advertirlo y recoger las comparecencias necesarias.
12. Nunca inventar datos, cuantias, fechas, referencias catastrales, datos registrales, numeros de protocolo ni jurisprudencia. **Esta skill no cita sentencias**: si el usuario necesita apoyo jurisprudencial concreto, se escala. Los campos no proporcionados quedan como `{{dato}}` con su nombre propio.
13. Los assets se construyen sobre el **Codigo Civil comun**. Si el caso se rige por derecho civil foral o especial —Cataluna regula la compraventa en el Llibre sise del Codi civil de Catalunya, y hay derecho propio en Navarra, Aragon, Baleares, Galicia y Pais Vasco—, detener y escalar.
14. No existe modelo oficial normalizado de contrato de compraventa ni de arras (verificado: ni Consejo General del Notariado, ni Colegio de Registradores, ni CGPJ). No afirmar al usuario que el documento reproduce un modelo oficial.

## Como NO se usa esta skill

- **No sustituye la escritura publica ante notario ni la inscripcion en el Registro de la Propiedad.** El deliverable es un contrato privado o un requerimiento: la transmision de la propiedad frente a terceros y la inscripcion exigen escritura publica notarial.
- **No hace due diligence de titularidad ni valoracion del inmueble.** No comprueba en el Registro quien es el titular, no verifica cargas por su cuenta, no revisa la situacion urbanistica ni tasa el inmueble. Recomienda esas comprobaciones; no las realiza.
- No usar para la **compraventa de local comercial, nave, solar, finca rustica o plaza de garaje transmitida de forma independiente**: los assets estan construidos para vivienda. Escalar.
- No usar para la **compraventa de obra nueva sobre plano con entregas a cuenta**: exige aval solidario o seguro de caucion de las cantidades anticipadas y cuenta especial separada (disposicion adicional primera de la Ley 38/1999). Escalar.
- No usar para **herencias, legados ni donaciones de inmuebles**: derivar a `derecho-civil-herencia`.
- No usar para permuta, dacion en pago, aportacion a sociedad ni adjudicacion en liquidacion de gananciales: escalar.
- No usar para redactar la **escritura publica** de compraventa ni el prestamo hipotecario: son documentos notariales.
- No usar para desalojar a un ocupante o arrendatario del inmueble: derivar a `derecho-civil-desahucio`.
- No usar para reclamar judicialmente el precio impagado una vez agotada la via extrajudicial: derivar a `derecho-civil-reclamacion-cantidad` segun cuantia, o a `derecho-civil-juicio-ordinario` si lo que se pide es la resolucion o el cumplimiento del contrato.
- No usar para ejecutar una escritura publica de compraventa ya otorgada e impagada: derivar a `derecho-civil-ejecucion-titulos`.
- No usar si el usuario pide **opinion juridica sobre la conveniencia de la operacion o sobre su estrategia**: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Inmueble arrendado y venta ya firmada sin notificacion al arrendatario | Advertir de inmediato del retracto del Art. 25.3 de la Ley 29/1994 y de la no inscribibilidad de la escritura (Art. 25.5), y escalar: la situacion puede requerir accion correctora antes de la escritura |
| Renuncia del arrendatario al retracto alegada pero no acreditada, o contrato de arrendamiento no disponible | No dar por buena la renuncia. Dejar el punto pendiente de verificacion y escalar si el cliente insiste en firmar sin comprobarlo |
| Compraventa de obra nueva sobre plano con entregas a cuenta | Detener: exige aval solidario o seguro de caucion individualizado y cuenta especial separada (disposicion adicional primera de la Ley 38/1999). Escalar |
| Compraventa de local, nave, solar, finca rustica o plaza de garaje independiente | Fuera de alcance de los assets. Advertir y escalar |
| Caso regido por derecho civil foral o especial (Cataluna, Navarra, Aragon, Baleares, Galicia, Pais Vasco) | Detener: los assets se construyen sobre el Codigo Civil comun. Escalar |
| Cargas registrales relevantes: embargos, condicion resolutoria, anotacion preventiva de demanda, doble venta | Escalar antes de firmar: el riesgo de perder el inmueble excede el alcance de un borrador |
| Vivienda de proteccion oficial o sujeta a precio maximo, o a tanteo y retracto administrativo autonomico | Advertir y escalar: el precio y la transmision pueden estar limitados por la normativa autonomica de vivienda |
| Discrepancia relevante entre la superficie registral, la catastral y la real, o venta con expresion de cabida | Advertir del regimen del Art. 1469 CC y escalar si la diferencia excede de la decima parte |
| Vendedor no titular registral, titularidad no inscrita, herencia sin partir o inmueble en proceso de division | Detener y escalar: no se puede vender lo que no se acredita tener |
| Accion de saneamiento por vicios ocultos con mas de seis meses desde la entrega (Art. 1490 CC) | Advertir de que la accion esta extinguida y escalar; no dar falsas expectativas |
| Impago del precio con mas de cinco anos desde su exigibilidad (Art. 1964.2 CC) | Advertir del riesgo de prescripcion y escalar |
| Concurso de acreedores del vendedor, o inmueble integrado en masa activa | Detener y escalar a concursal: la transmision puede quedar sujeta a rescision o a autorizacion judicial |
| Vendedor o comprador menor de edad o con discapacidad sin representacion clara | Advertir de la normativa de proteccion y de la necesidad de autorizacion o de apoyo, y escalar |
| Solicitud de reflejar en el contrato un precio distinto del realmente satisfecho | Rechazar la instruccion, explicar que es una simulacion con consecuencias fiscales y penales, y no redactarla |
| El usuario pide citar sentencias concretas sobre la clase de arras | Esta skill no cita jurisprudencia: explicar la calificacion como construccion jurisprudencial y escalar para el apoyo con sentencias |
| El usuario pide una opinion sobre si le conviene firmar o sobre su estrategia negociadora | Derivar via `escalate_to_attorney` |
