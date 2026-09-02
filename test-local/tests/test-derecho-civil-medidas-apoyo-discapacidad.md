# Test de ejecucion — skill `derecho-civil-medidas-apoyo-discapacidad`

Ejecucion manual del arbol de decision sobre cuatro escenarios (3 principales + 1 contra-caso). Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: Codigo Civil (BOE-A-1889-4763, arts. 249 a 298), Ley 15/2015 de Jurisdiccion Voluntaria (BOE-A-2015-7391), LEC (BOE-A-2000-323, arts. 756 a 763) y LOPJ (BOE-A-1985-12666, art. 84).
- Verificacion real efectuada el 03/09/2026 contra la API de legislacion consolidada del BOE: **todos** los arts. 249 a 298 del Codigo Civil estan en la redaccion de la Ley 8/2021, con efectos desde el 03/09/2021; los arts. 756 a 762 LEC, en la misma redaccion y fecha; el art. 763 LEC conserva su redaccion de 2015 (no tocada por la Ley 8/2021); los arts. 42 bis a), b) y c), 52.3, 61 y 62 LJV proceden de la Ley 8/2021; y el art. 84 LOPJ, de la LO 1/2025 (vigencia 23/01/2025), crea los Tribunales de Instancia con posible Seccion de Familia, Infancia y Capacidad.
- Se verifico ademas la pagina de modelos normalizados del CGPJ: **no existe modelo especifico** de medidas de apoyo ni de curatela; si existe el modelo generico de solicitud de expediente de jurisdiccion voluntaria (art. 14.3 LJV), fichero de 01/08/2025, que ya se dirige "AL TRIBUNAL DE INSTANCIA DE".
- Aviso de identificadores de bloque confirmado en la practica: el Codigo Civil usa `artNNN`, la LEC y la LJV `aNNN`, la LOPJ el ordinal deletreado (`aochentaycuatro`), y los articulos "bis" de la LJV un id sintetico (`a4-2` = art. 42 bis a). Los intentos con `a42bisa` devolvieron 404 y se resolvieron consultando el indice de la norma.

---

## Test 1 — Persona mayor con deterioro incipiente que quiere dejar previsto quien le apoyara

**Mensaje inicial:** "Tengo 78 anos y empiezo a notar que me cuesta manejar mis cosas. Quiero dejar atado ahora quien me ayudara el dia que no pueda, y que no acabe decidiendolo un juez."

### Recorrido del arbol
```
Correccion terminologica -> NO se emite (el usuario no ha empleado
       el vocabulario derogado)
V1 -> escucha activa: "dejar atado ahora quien me ayudara
       el dia que no pueda"                                V1 = prevision voluntaria (sin pregunta)
V2 (filtro de subsidiariedad) -> NO aplica (exclusivo de V1 = 3)
V3 -> NO aplica          V4 -> NO aplica (solo hojas GUARDA y CURATELA)
Validacion (Arts. 255 y 260 CC): el otorgante comprende el acto y
       puede otorgar -> PROCEDE
HOJA VOLUNTARIA -> assets/minuta-poder-preventivo.md
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija; V1 ya resuelto por escucha activa -> verificacion normativa interna en silencio y paso directo a la Confirmacion.
- Turno 2: Confirmacion visible (Punto 3): texto fijo VOLUNTARIA con arts. 255 y ss., 256 a 262 y 271, enlace al BOE, y eleccion plantilla/documento propio.
- Turno 3: creacion del documento con `Write`, `Read` y confirmacion de ruta absoluta; **en la misma respuesta**, anuncio de la primera seccion ("Comenzamos por los datos de quien otorga las medidas de apoyo") y primera pregunta. **No hay turno de "¿desea empezar?"**.
- Turnos 4-8: otorgante (nombre, DNI, estado civil, domicilio/telefono/correo, vecindad civil), un dato por turno.
- Turno 9: vista previa unica y **confirmacion agrupada** de los cinco datos del otorgante, en el turno SIGUIENTE a la respuesta del ultimo.
- Turno 10: finalidad y motivo del otorgamiento.
- Turno 11: modalidad del poder [negociacion] — la skill explica la diferencia entre el art. 256 (subsistencia, opera ya, mas agilidad y mas confianza) y el art. 257 (solo para el futuro, mas control y un tramite mas: acta notarial con informe pericial). El usuario elige el art. 256.
- Turnos 12-15: persona designada (nombre, DNI, domicilio, relacion), con verificacion de la prohibicion del art. 250 in fine; confirmacion agrupada; despues, en turno propio, sustitutos.
- Turnos 16-17: facultades conferidas [negociacion] — la skill explica **primero** el art. 259 (si el poder comprende todos los negocios, el apoderado queda sujeto a las reglas de la curatela) y recomienda acotar; el usuario acota a facultades bancarias, tributarias y de administracion ordinaria, sin disposicion de inmuebles.
- Turnos 18-22: salvaguardas, control y revision [negociacion] — organo de control (un segundo hijo), rendicion de cuentas anual, revision cada tres anos, instrucciones y causas de extincion.
- Turno 23: prohibiciones del art. 251 [negociacion] — la skill explica las tres y que solo en las medidas voluntarias pueden excluirse; **ofrece por defecto mantenerlas**; el usuario las mantiene.
- Turnos 24-31: autocuratela [negociacion] — la skill explica que no es alternativa al poder y que el art. 272 la hace **vinculante para el juez**; el usuario la incluye y aporta curador propuesto, sustituto, personas excluidas, reglas de administracion, retribucion, dispensa de inventario y medidas de control. Se activa el bloque condicional y se resuelve `{{ordinal_clausula_autocuratela}}` = IX.
- Turnos 32-35: voluntad, deseos y preferencias del otorgante (residencia, atencion personal y sanitaria, patrimonio, otras instrucciones).
- Turnos 36-38: instrucciones al notario; se resuelve `{{ordinal_clausula_instrucciones_notario}}` = X.

### Documento generado (extracto relleno, datos sinteticos)
```
MINUTA DE ESCRITURA DE MEDIDAS DE APOYO VOLUNTARIAS Y PODER PREVENTIVO — PERSONA CON DISCAPACIDAD A
> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico definitivo.
> Version del Codigo Civil verificada en el BOE: 03/09/2026

IV. MODALIDAD DEL PODER
El otorgante confiere el poder que se detalla en la clausula siguiente con eficacia desde este mismo momento, e incluye
expresamente la clausula de subsistencia prevista en el articulo 256 del Codigo Civil, de modo que el poder subsistira
si en el futuro el poderdante precisa apoyo en el ejercicio de su capacidad juridica.

IX. PROPUESTA DE AUTOCURATELA
[...] propone el nombramiento como curador de FAMILIAR A [...] El otorgante ha sido informado de que estas
disposiciones vincularan a la autoridad judicial al constituir la curatela.
```

**Bloques ACTIVADOS:** clausula de subsistencia del art. 256; sustitutos; autocuratela (clausula IX).
**Bloques NO activados:** poder *ad cautelam* del art. 257; advertencia del art. 259 (el poder no comprende todos los negocios); exclusion de las prohibiciones del art. 251; extincion automatica por cese de convivencia del art. 258 (el apoderado no es el conyuge); delegacion de la eleccion del curador del art. 274.

Resultado: **PASA**. Ninguna mencion a incapacitacion, tutela ni modificacion de la capacidad. El documento se entrega como minuta para el notario, con la advertencia expresa de que no produce efectos hasta su otorgamiento en escritura publica.

---

## Test 2 — Hijo que lleva anos ocupandose de su madre y necesita vender un inmueble de ella

**Mensaje inicial:** "Llevo seis anos cuidando de mi madre, que tiene un deterioro cognitivo. Ahora esta en una residencia y hay que vender su piso para pagarla, pero el notario me dice que no puedo firmar yo solo. ¿Que hago?"

### Recorrido del arbol
```
Correccion terminologica -> NO se emite (el usuario no ha empleado
       el vocabulario derogado)
V1 -> escucha activa: "llevo seis anos cuidando" + "hay que
       vender su piso" + "no puedo firmar yo solo"         V1 = 2, acto concreto en su nombre (sin pregunta)
V2 (filtro) -> NO aplica (exclusivo de V1 = 3)
V4 -> PREGUNTA: expresion de la voluntad -> 1 (puede
       expresar lo que quiere, con ayuda)                  V4 = puede expresarse
Validacion "acto concreto" -> hay acto determinado: la venta -> PROCEDE
Validacion Art. 264 parr. 3 -> NO es prestacion economica ni bien
       de escasa relevancia -> se requiere autorizacion
Validacion Art. 287 -> enajenacion de inmueble = Art. 287.2º -> preceptiva EN TODO CASO
Validacion Art. 62.3 LJV -> valor 120.000 euros > 6.000 -> abogado y
       procurador no preceptivos para la solicitud inicial, pero el
       Tribunal puede ordenarlos despues
HOJA GUARDA -> assets/solicitud-autorizacion-guarda-hecho.md
```

**Este es el escenario que la skill existe para no fallar.** El cliente describe una situacion que, bajo el regimen anterior, un despacho habria encaminado a una incapacitacion o a una tutela. Aqui la guarda de hecho **ya es** la medida de apoyo aplicable (arts. 250 y 263 CC) y lo unico que falta es la autorizacion puntual del art. 264 para el acto concreto. **No se enruta a curatela.**

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija + V4 (unico vector no resuelto por escucha activa).
- Turno 2: Confirmacion visible con texto fijo GUARDA (art. 264 CC y arts. 61 a 63 LJV), enlaces al BOE, aviso de que no existe modelo normalizado especifico del CGPJ, y eleccion plantilla/documento propio.
- Turno 3: creacion del documento (`Write` + `Read` + ruta absoluta) y, en la misma respuesta, anuncio de seccion y primera pregunta.
- Turnos 4-7: guardador solicitante (nombre, DNI, domicilio/telefono/correo, relacion), confirmacion agrupada en el turno 8.
- Turnos 9-12: la persona a la que se presta apoyo (nombre, DNI, domicilio de residencia, situacion de apoyo descrita en necesidades observables), confirmacion agrupada en el turno 13.
- Turnos 14-17: la guarda de hecho (desde cuando, en que consiste, convivencia, otras medidas existentes).
- Turno 18: otros familiares e interesados.
- Turnos 19-24: el acto [negociacion] — la skill explica primero el art. 63 LJV (motivo, necesidad, identificacion del bien, destino del dinero) y que pedir mas de lo necesario frustra el expediente; despues pide los seis datos, uno por turno. **Pregunta la conveniencia para la madre, no para la familia.**
- Turnos 25-26: venta directa o subasta [negociacion] — la skill explica el art. 287.2º y el art. 63.3 LJV y pregunta si dispone de valoracion pericial; el usuario la tiene, precio minimo 120.000 euros.
- Turnos 27-28: voluntad, deseos y preferencias [negociacion] — V4 ya resuelto: el usuario relata que su madre esta conforme con la venta y prefiere seguir en el centro actual, y como se le consulto.
- Turno 29: conflicto de intereses — el usuario confirma que no es comprador ni tiene interes en la operacion: el OTROSI de defensor judicial **NO se activa**.
- Turno 30: postulacion — la skill informa del art. 62.3 LJV; el usuario decide comparecer con abogado y procurador.
- Turno 31: documentos.
- Turno 32: organo, lugar y fecha — la skill **verifica expresamente** que el competente es el de la residencia de la madre (art. 62.1 LJV), que difiere del domicilio del hijo.

### Verificacion en vivo (documento real, no extracto manual)
Se ejecuto realmente el Punto 4 sobre el asset: `Write` en `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/solicitud_autorizacion_guarda_hecho_prueba.md`, `Read` de verificacion, y tres ciclos de `Edit` incremental (seccion del acto, ordinal dinamico y fundamento de la necesidad de autorizacion), con el `oldString` copiado literalmente del `Read` previo.

Extracto del archivo real:
```
CUARTO — El acto para el que se solicita autorizacion.
Se solicita autorizacion judicial para vender la vivienda propiedad de PERSONA CON DISCAPACIDAD A.
Bien o derecho al que se refiere, identificado con precision: vivienda sita en Calle Ejemplo 2, numero 3, primero,
de Ciudad Ejemplo, referencia catastral 0000000AA0000A0000AA, [...]
Destino que se dara a la suma que se obtenga: se ingresara integramente en la cuenta de titularidad exclusiva de
PERSONA CON DISCAPACIDAD A y se destinara al pago de su atencion residencial y sanitaria.
Valor economico del acto: 120.000 euros.

Este acto requiere autorizacion judicial porque implica la enajenacion de un bien inmueble de la persona a la que se
presta apoyo y, por tanto, una actuacion representativa del guardador de hecho.

Se trata de uno de los actos enumerados en el articulo 287, numero 2.º, del Codigo Civil, para los que el guardador
de hecho debe recabar autorizacion judicial en todo caso, conforme al parrafo segundo del articulo 264 del mismo Codigo.

Se interesa que la autorizacion se extienda a la celebracion de venta directa [...] A tal efecto se acompana dictamen
pericial de valoracion del precio de mercado del bien como Documento nº 4 [...]
```

**Bloques ACTIVADOS:** art. 287.2º; venta directa (art. 63.3 LJV); comparecencia con procurador y letrado.
**Bloques NO activados:** medidas de apoyo existentes que no se aplican eficazmente; autorizacion para varios actos; OTROSI de tramitacion preferente; OTROSI de defensor judicial por conflicto de intereses.

**Comprobaciones mecanicas sobre el archivo real:** cero comentarios HTML residuales; `{{ordinal_hecho_acto}}` resuelto a "cuarto"; ninguna aparicion de terminologia prohibida (`grep -niE "incapa|tutor|tutela|discapacitad[oa]|minusval|padece"` sin resultados); `Edit` aplicados sin fallos de coincidencia. Los placeholders que persisten son exactamente los datos que el `SKILL.md` deja para turnos posteriores (documentos, voluntad, organo, lugar y fecha), no datos inventados ni omitidos por error.

**Defecto real detectado y corregido durante esta ejecucion.** Al insertar el bloque condicional del art. 287 y el de venta directa, quedaron colocados **antes** del parrafo `{{fundamento_necesidad_autorizacion}}` que en el asset los precede, y la omision de comentarios dejo tres lineas en blanco consecutivas. **Fix aplicado al `SKILL.md`, Punto 4:** se anadio la instruccion de colapsar las lineas en blanco que deja la omision de un bloque condicional y de insertar cada bloque **en el orden en que figura en el asset**, no al final de la seccion. Y en el Punto 5, seccion 5 de la HOJA GUARDA, se aclaro que `{{fundamento_necesidad_autorizacion}}` es la razon **factica** y es un dato distinto del bloque del art. 287, que aporta la cita legal.

Resultado: **PASA con dos correcciones aplicadas**.

---

## Test 3 — Persona sin ningun apoyo y con necesidad continuada

**Mensaje inicial:** "Mi hermano vive solo, tiene una enfermedad mental grave y desde que murio nuestra madre no hay nadie que se ocupe. No paga los recibos, ha firmado cosas que no entendia y le han vaciado la cuenta. No tiene ningun poder dado a nadie. Necesitamos que alguien pueda ayudarle de forma estable."

### Recorrido del arbol
```
Correccion terminologica -> NO se emite
V1 -> escucha activa: "que alguien pueda ayudarle de forma
       estable"                                            V1 = 3, curatela
V2.a -> escucha activa: "no hay nadie que se ocupe"         V2.a = 2 (sin pregunta)
V2.b -> escucha activa: "no tiene ningun poder dado a nadie" V2.b = 2 (sin pregunta)
FILTRO DE SUBSIDIARIEDAD -> superado SIN pregunta de salida
       (V2.a = 2 y V2.b = 2)
Filtro de necesidad ocasional -> el relato describe necesidad
       continuada, no ocasional -> no procede defensor judicial
V3 -> PREGUNTA: tipo de apoyo -> 1 (acompanamiento y asistencia)  V3 = asistencial
V4 -> PREGUNTA: expresion de la voluntad -> 1                     V4 = puede expresarse
Sub-pregunta de via procesal -> 1 (no hay actuaciones previas)  -> JURISDICCION VOLUNTARIA
HOJA CURATELA -> assets/demanda-curatela.md
       (bloques de facultades representativas DESACTIVADOS,
        variante contenciosa DESACTIVADA)
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija + V3 (V1, V2.a y V2.b ya resueltos por escucha activa).
- Turno 2: V4.
- Turno 3: sub-pregunta de via procesal.
- Turno 4: Confirmacion visible con texto fijo CURATELA en via de jurisdiccion voluntaria (art. 269 CC y art. 42 bis a) LJV), enlaces al BOE, aviso de inexistencia de modelo normalizado especifico y **aviso de que las medidas se revisaran en un maximo de tres anos**; eleccion plantilla/documento propio.
- Turno 5: creacion del documento y, en la misma respuesta, anuncio de seccion y primera pregunta.
- Turnos 6-10: promotor (nombre, DNI, domicilio/telefono/correo, relacion), con verificacion de legitimacion del art. 42 bis a).3 LJV — es hermano, legitimado; confirmacion agrupada.
- Turnos 11-17: la persona que precisa apoyo (nombre, DNI, fecha de nacimiento, residencia, situacion personal, situacion patrimonial); confirmacion agrupada. La skill reformula las respuestas en **necesidades observables**, no en diagnostico.
- Turnos 18-20: necesidades concretas de apoyo [negociacion] — la skill explica el art. 269 (actos fijados de manera precisa, sin curatela generica) antes de preguntar; el usuario aporta tres ambitos (gestion bancaria y de pagos, contratacion de servicios y suministros, decisiones patrimoniales relevantes) y justifica por que el apoyo es continuado.
- Turnos 21-23: inexistencia de otra medida suficiente [negociacion] — **la seccion decisiva**. La skill pide, por separado, la situacion de las medidas voluntarias, la de la guarda de hecho y por que no basta un apoyo ocasional. Rechaza la primera respuesta generica ("porque hace falta") y pide el hecho concreto: los recibos impagados desde una fecha, el contrato firmado sin comprenderlo y la disposicion de la cuenta.
- Turnos 24-26: actos para los que se precisa asistencia [negociacion] — relacion acto por acto; la skill advierte de que lo no incluido queda en el ambito de decision libre de la persona.
- Turno 27: facultades representativas — **SE OMITE** (V3 = 1).
- Turnos 28-29: voluntad, deseos y preferencias [negociacion] — el hermano puede expresarse: quiere seguir viviendo en su casa y acepta ayuda para el dinero; se resuelve `{{ordinal_hecho_voluntad}}` = SEXTO.
- Turnos 30-35: persona propuesta como curador [negociacion] — la skill explica el orden del art. 276, la fuerza vinculante del art. 272, que discrepar sobre el curador **no** hace contencioso el expediente (art. 42 bis b).5 LJV) y las exclusiones del art. 275 y del art. 250 in fine; verifica que el promotor no presta servicios asistenciales por contrato. Se resuelve `{{ordinal_hecho_curador}}` = SEPTIMO.
- Turnos 36-37: salvaguardas y revision [negociacion] — informe anual al Tribunal y revision a los tres anos. Se resuelve `{{ordinal_hecho_salvaguardas}}` = OCTAVO.
- Turnos 38-40: dictamen pericial [validacion bloqueante] — el usuario dispone de informe de la unidad de salud mental **pero no de un dictamen que aconseje medidas de apoyo**; la skill advierte expresamente de que el escrito no puede presentarse asi (art. 42 bis b).1 LJV), deja los placeholders del dictamen sin resolver y **enumera cuales son**.
- Turno 41: interesados a citar; se resuelve `{{ordinal_hecho_interesados}}` = NOVENO.
- Turnos 42-44: medidas provisionales y otrosies [negociacion] — hay riesgo patrimonial actual (la cuenta vaciada): se activan el OTROSI de medidas provisionales (art. 762 LEC) y el de informe sobre alternativas de apoyo (art. 42 bis b).2 LJV). El de ajustes de accesibilidad tambien, a peticion del usuario.
- Turnos 45-47: postulacion y documentos; se resuelven `{{ordinal_fundamento_designacion}}`, `{{ordinal_fundamento_salvaguardas}}` y `{{ordinal_fundamento_tramite}}` = VII, VIII y IX (el fundamento de representacion no existe).
- Turno 48: organo, lugar y fecha — el competente es el de la residencia del hermano (art. 42 bis a).2 LJV).

### Documento generado (extracto relleno, datos sinteticos)
```
SOLICITUD DE PROVISION JUDICIAL DE MEDIDAS DE APOYO — CURATELA DE PERSONA CON DISCAPACIDAD A
> DRAFT — para revision por un abogado colegiado antes de su firma.

HECHOS
CUARTO — Inexistencia de otra medida de apoyo suficiente.
Medidas de apoyo de naturaleza voluntaria: PERSONA CON DISCAPACIDAD A no ha otorgado poder ni medida voluntaria alguna,
segun resulta de la certificacion del Registro Civil que se interesa.
Guarda de hecho: nadie viene ejerciendo la guarda de hecho desde el fallecimiento de su madre el {{fecha}}; esta parte
reside en otra localidad y no puede prestar un apoyo estable.
Suficiencia de un apoyo de caracter ocasional: los hechos descritos no son puntuales sino recurrentes y sostenidos
en el tiempo, por lo que un apoyo ocasional del articulo 295.5º del Codigo Civil no resulta suficiente.

QUINTO — Actos para los que se precisa la asistencia del curador.
1. Operaciones bancarias de disposicion superiores a {{importe}} euros.
2. Contratacion, modificacion y baja de suministros y servicios de tracto sucesivo.
3. Actos de disposicion o gravamen sobre bienes inmuebles.
En todos los demas ambitos de su vida, PERSONA CON DISCAPACIDAD A conserva y ejercera su capacidad juridica sin
necesidad de apoyo alguno.
```

**Bloques ACTIVADOS:** OTROSI de medidas provisionales; OTROSI de informe sobre alternativas de apoyo; OTROSI de ajustes de accesibilidad.
**Bloques NO activados:** variante contenciosa de los arts. 756 y ss. LEC; hecho SEXTO de facultades representativas y su fundamento VII; bloque de imposibilidad de determinar la voluntad (art. 249, parrafo 3); bloque de medidas voluntarias subsistentes; bloque de guarda de hecho que ha dejado de ser suficiente; bloque de autocuratela; bloque de pluralidad de curadores; OTROSI de defensor judicial para la administracion de bienes; OTROSI de defensor judicial para el expediente.

Resultado: **PASA**. El escrito pide una curatela **asistencial** con tres actos individualizados, no una curatela generica, y no contiene ninguna peticion de privacion de derechos. La validacion del dictamen pericial no bloquea la redaccion del borrador pero deja constancia visible de que falta.

---

## Contra-caso — El cliente pide "incapacitar" a su padre y resulta que la hermana ya se ocupa de todo

**Mensaje inicial:** "Quiero incapacitar a mi padre. Tiene 85 anos y ya no se entera de nada. Mi hermana vive con el y se ocupa de todo, pero no me fio de que lo haga bien y quiero que sea legal."

### Recorrido del arbol
```
Correccion terminologica -> SE EMITE (el usuario dice "incapacitar")
V1 -> escucha activa reconducida: la peticion, traducida al sistema
       vigente, es una medida judicial estable                V1 = 3, curatela
V2.a -> escucha activa: "mi hermana vive con el y se ocupa
       de todo"                                              V2.a = 1 (sin pregunta)
V2.b -> PREGUNTA: documentos otorgados con anterioridad -> 2  V2.b = 2
FILTRO DE SUBSIDIARIEDAD -> V2.a = 1 -> **BLOQUEA**: no se enruta a curatela
Pregunta de salida -> el usuario no identifica ningun acto concreto
       pendiente y reconoce que su hermana se ocupa con normalidad
-> NO se crea documento alguno
```

### Comportamiento esperado

**Turno 1.** Antes de la introduccion, la skill emite la correccion terminologica fija: que desde la Ley 8/2021 no existen la incapacitacion, la modificacion judicial de la capacidad ni la tutela de adultos, y que lo que el ordenamiento prevee son medidas de apoyo. Sin reproche y una sola vez. A continuacion, la introduccion fija y la pregunta de V2.b (V1 y V2.a ya resueltos por escucha activa).

**Turno 2.** Resuelto V2.b = 2, se dispara el filtro del art. 269. La skill emite, en un unico mensaje: (1) la explicacion de que la guarda de hecho que ejerce la hermana **es** una medida de apoyo del art. 250, que quien la ejerce adecuadamente continua en su funcion (art. 263) y que la curatela solo se constituye cuando no existe otra medida suficiente (art. 269); (2) la alternativa concreta: si hay un acto puntual que exija actuar en nombre del padre, la via es la autorizacion del art. 264, mas breve y sin abogado ni procurador preceptivos por debajo de 6.000 euros; y (3) la pregunta de salida con dos opciones.

**Turno 3.** El usuario responde que no hay ningun acto pendiente y que su hermana se ocupa con normalidad. La skill **no crea documento**: informa de que no procede iniciar ningun procedimiento, de que la guarda de hecho no se constituye ni se inscribe porque ya es la medida aplicable, y de que si en el futuro surge un acto que exija representacion se podra pedir la autorizacion puntual. Ofrece ademas, si el padre conserva capacidad para otorgar, la via de las medidas voluntarias.

**Trato de la desconfianza entre hermanos.** La skill no ignora el "no me fio". Informa de que el art. 265 del Codigo Civil permite pedir por expediente de jurisdiccion voluntaria que se requiera al guardador para que informe de su actuacion y rinda cuentas, y de que el art. 52 de la Ley de Jurisdiccion Voluntaria permite al Tribunal establecer medidas de control. Pero **escala**: un conflicto entre familiares por quien ejerce el apoyo esta expresamente en la matriz de escalacion, y esta skill no genera ese escrito.

**Resultado: PASA.** La terminologia se corrige en el primer turno, el filtro del art. 269 se aplica antes de pedir ningun dato de relleno, no se enruta a curatela y no se crea documento. El usuario recibe la respuesta correcta en tres turnos, sin invertir tiempo en un escrito que el Tribunal habria reconducido o desestimado.

---

## Revision UX

Hallazgos:

1. **El filtro de subsidiariedad se ejecuta antes que cualquier pregunta de relleno**, igual que la validacion de caducidad en la skill de ejecucion. El usuario del contra-caso recibe la respuesta en el turno 2, no despues de veinte turnos completando un escrito inutil. Esto es lo que separa esta skill de un generador de demandas de curatela.

2. **La correccion terminologica va antes de la introduccion, no despues.** Se probaron las dos posiciones. Si va despues, el usuario ya ha leido "vamos a determinar que medida de apoyo se ajusta a su caso" sin entender por que no se le habla de incapacitacion, y la correccion suena a matiz tardio. Yendo antes, ordena el resto de la conversacion. Se emite **una sola vez** y sin reproche: repetirla convierte el asesoramiento en una leccion.

3. **V2 se divide en dos preguntas (V2.a y V2.b) en lugar de una con tres opciones.** Una pregunta unica del tipo "¿hay alguien ocupandose, o se otorgo algun poder, o no hay nada?" mezcla dos hechos independientes — puede haber guarda de hecho **y** poder previo — y obliga al usuario a elegir entre opciones que no son excluyentes. Dos binarias cuestan un turno mas y no producen respuestas ambiguas.

4. **El filtro tiene una salida por confirmacion expresa del cliente, no un bloqueo absoluto.** Si el cliente afirma que el apoyo actual no basta, la skill continua, pero **exige el hecho concreto que lo demuestra** antes de seguir. Bloquear sin salida seria paternalista y dejaria fuera los casos en que la guarda de hecho realmente ha dejado de funcionar; continuar sin exigir el hecho produciria un escrito que el Tribunal rechazaria por falta de motivacion del art. 269.

5. **La pregunta de V4 esta redactada sin tecnicismo y sin juicio de valor** ("¿puede expresar lo que quiere y lo que prefiere?" frente a "¿tiene capacidad natural de autogobierno?"). Es la pregunta mas delicada de la skill: determina si se piden facultades representativas. Formularla en terminos clinicos invitaria al cliente a emitir un juicio que no le corresponde.

6. **El aviso del art. 268 (revision maxima a los tres anos) se da en la Confirmacion, no al final.** El cliente que llega pidiendo una curatela suele creer que es definitiva. Saberlo desde el principio cambia sus expectativas y, en algunos casos, su decision.

7. **La validacion del dictamen pericial advierte pero no bloquea la redaccion.** Bloquear obligaria al cliente a volver mas adelante y repetir toda la conversacion. Redactar el borrador y decirle con precision que placeholders quedan pendientes le permite encargar el dictamen sabiendo exactamente para que.

8. **Los tres assets estan escritos con la persona como sujeto, no como objeto.** En la revision de texto se elimino toda formula del tipo "procede someter a X a...", y las necesidades se describen como observables ("no puede acudir por si misma a la entidad bancaria"), nunca como diagnostico. El guardrail de terminologia se comprobo con `grep` sobre los tres assets y sobre el documento real generado: cero coincidencias.

Ajustes aplicados: los dos del Test 2 (colapso de lineas en blanco y orden de insercion de los bloques condicionales en el Punto 4; aclaracion de `{{fundamento_necesidad_autorizacion}}` frente al bloque del art. 287 en el Punto 5). Ningun otro ajuste adicional a los ya reflejados en el `SKILL.md`.

---

## QA en vivo por agente independiente

Ejecucion real (03/09/2026) por un agente sin contexto previo de la skill. Escenario con vocabulario
deliberadamente equivocado: *"Quiero incapacitar a mi madre. Tiene 84 anos y alzheimer avanzado. Yo vivo con
ella desde hace cuatro anos y me ocupo de todo: la cuido, le gestiono la pension y le pago las facturas de su
cuenta. Ahora hay que vender su piso del pueblo para pagar la residencia y el notario me dice que asi no puedo."*

Datos sinteticos: PERSONA CON DISCAPACIDAD A, FAMILIAR A, NIF 00000000-T.
Documento realmente generado: `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/apoyo-qa-prueba.md`
(`Write` + `Read` de verificacion + nueve `Edit` incrementales con `oldString` literal).

### Verificacion normativa realmente ejecutada (Punto 2)

Consulta real a la API de legislacion consolidada del BOE (`Accept: application/xml`) de los bloques `art264`,
`art269` y `art287` del Codigo Civil. Los tres devuelven como ultima version la de `BOE-A-2021-9233` (Ley 8/2021),
`fecha_vigencia="20210903"`, coincidente con la version registrada en `fuentes-plantillas-validadas.md`: **no
procedia auto-actualizacion**. Se confirmo literalmente el art. 287.2.º ("Enajenar o gravar bienes inmuebles...")
como ordinal aplicable a la venta del piso, y el art. 269 parrafo 1 ("cuando no exista otra medida de apoyo
suficiente para la persona con discapacidad"). El aviso del Punto 2 sobre que **la ultima `<version>` del bloque
es la vigente** resulto imprescindible: la API devuelve tambien las redacciones de 1889 y 1983, y la de 1983 del
art. 264 habla de "tutor" y del "loco, demente o sordomudo". Un LLM que tomara la primera version del XML
redactaria con vocabulario derogado por seguir la instruccion al pie de la letra. El aviso esta bien puesto.
No se re-verificaron los bloques de la LJV ni la pagina de modelos normalizados del CGPJ.

### Transcripcion literal (extractos)

**Turno 1** — linea de carga, correccion terminologica, introduccion y primera pregunta, todo en el mismo mensaje:

> **Skill cargada satisfactoriamente.**
>
> Antes de continuar, una precision necesaria. Desde la Ley 8/2021 no existen en Espana la incapacitacion ni la
> modificacion judicial de la capacidad, ni la tutela de personas adultas. Lo que el ordenamiento preve hoy son
> medidas de apoyo para que la persona ejerza su propia capacidad juridica. No es un cambio de nombre: cambia lo
> que puede pedirse y como se pide.
>
> Vamos a determinar que medida de apoyo se ajusta a la situacion que me plantea y a preparar el documento que
> corresponda. Para hacerlo correctamente, es necesario precisar antes algunos datos.
>
> Lo que necesita preparar es:
> 1. Que la propia persona deje previsto ahora quien le apoyara si en el futuro lo necesita
> 2. Que quien ya se ocupa de ella pueda realizar un acto concreto en su nombre
> 3. Que un juez establezca un apoyo estable para ella

*Cliente: "La 2, supongo. Lo urgente es el piso."*

**Turno 2** — V4, sin preambulo:

> Sobre su capacidad de expresarse hoy:
> 1. Puede expresar lo que quiere y lo que prefiere, aunque necesite ayuda para comprender o decidir
> 2. No es posible saber lo que quiere, ni siquiera dedicandole tiempo y buscando el modo

*Cliente: "La 2. Ya no mantiene una conversacion."*

**Turno 4** — tras el `Write`, confirmacion y primera pregunta encadenadas en la misma respuesta:

> He creado el documento en /Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/apoyo-qa-prueba.md.
>
> Comenzamos por sus datos como persona que presta el apoyo. Indiqueme su nombre y apellidos.

**Seccion 5** (`[negociacion]`), explicacion antes de pedir la decision:

> Concretamos el acto para el que se solicita la autorizacion. Antes de pedirle los datos conviene que sepa como
> se examina esta peticion. La autorizacion se concede para actos determinados y no en abstracto: el articulo 63
> de la Ley 15/2015, de Jurisdiccion Voluntaria, exige que se exprese el motivo del acto, se razone su necesidad
> o conveniencia, se identifique con precision el bien y se diga a que se destinara el dinero que se obtenga.
> Pedir mas de lo necesario retrasa o frustra el expediente. Indiqueme, en primer lugar, en que consiste
> exactamente el acto que necesita realizar.

**Seccion 7** (voluntad, con V4 = 2):

> Recogemos lo que la propia persona quiere y prefiere sobre este acto. Usted me ha indicado que hoy no es posible
> saber que desea. La ley no se detiene ahi: el articulo 249, parrafo tercero, del Codigo Civil exige que, cuando
> pese a un esfuerzo considerable no pueda determinarse su voluntad, el apoyo se preste atendiendo a su trayectoria
> vital, a sus creencias y valores y a los factores que ella habria tomado en consideracion. Indiqueme en que ha
> consistido el esfuerzo por averiguar su parecer sobre la venta de la vivienda.

### A) Veredicto sobre el texto al cliente — **PASA con una reserva**

- **Tratamiento formal:** correcto en todos los turnos. "Indiqueme su nombre y apellidos", "Usted me ha indicado",
  "conviene que sepa". Ni un "tu", ni un "vale/genial/perfecto", ni un preambulo del tipo "para empezar necesito".
- **Se habla de una persona, no de un expediente:** el cliente aporto un diagnostico ("alzheimer avanzado") y el
  documento **no lo reproduce en ningun punto**. El hecho PRIMERO describe necesidades observables: *"no puede
  acudir por si misma a una entidad bancaria ni realizar gestiones administrativas; no reconoce el valor del dinero
  ni comprende el alcance de un contrato de compraventa"*. Es exactamente lo que pide la regla cero de
  `estilo-redaccion-escritos.md`, y es el punto donde una skill mediocre habria escrito "padece alzheimer avanzado".
- **Clausulas de negociacion:** las dos `[negociacion]` recorridas (secciones 5 y 7) explican el regimen legal y su
  consecuencia practica **antes** de pedir la decision. Cumplido.
- **Cero fugas de mecanica interna:** no aparecen "V1", "V4", "HOJA GUARDA", "filtro", "vector" ni "paso 2".
- **Cero invenciones:** el unico dato juridico que el asistente aporto de por si fue el ordinal del art. 287, y se
  verifico en el BOE antes de escribirlo. Fecha de inicio de la guarda y relacion de parentesco **no** se dedujeron
  del relato ("desde hace cuatro anos", "mi madre") sino que se preguntaron, evitando inventar una precision que el
  cliente no habia dado.
- **Reserva (no corregida, decision deliberada):** el texto fijo de la Confirmacion del Punto 3 **no responde a la
  pregunta que trae el cliente**. El ha dicho "el notario me dice que asi no puedo" y se va con la via correcta pero
  sin saber por que: que la guarda de hecho no confiere por si sola poder de representacion y que por eso el art. 264
  exige autorizacion judicial. Es una frase que cabria en el texto fijo y ahorraria la llamada de vuelta. No se
  edito por no tocar textos fijos de los que dependen los tests 1 a 3 de este mismo fichero; queda anotado.

### B) Veredicto sobre el asset — **3 defectos reales, los 3 corregidos**

Placeholders: **limpios**. `grep` sobre los tres assets: cero placeholders anidados, cero con texto de ayuda dentro,
cero `[DATO]`. Cero terminologia prohibida.

Numeracion: **sin huecos posibles**. A diferencia de `demanda-curatela.md`, la hoja GUARDA usa ordinales fijos
PRIMERO-SEXTO y ningun hecho condicional, de modo que omitir un bloque no puede abrir un hueco. El unico ordinal
dinamico, `{{ordinal_hecho_acto}}` de la comparecencia, se resolvio a "cuarto" en el `Write`.

**Defecto 1 (grave) — bloque inexistente en la rama V4 = 2.** El `SKILL.md`, Punto 5, hoja GUARDA, seccion 7,
ordenaba: *"Si no puede expresarse: ... y activa el bloque correspondiente"*. **Ese bloque no existia en
`solicitud-autorizacion-guarda-hecho.md`**; solo estaba en `demanda-curatela.md` (linea 68). El hecho QUINTO era
texto fijo escrito para la rama contraria, de modo que con V4 = 2 el escrito quedaba asi:

> No ha sido posible determinar su voluntad, deseos y preferencias.
> **Esta voluntad se ha recabado del siguiente modo:** ...
> Esta parte hace constar que la autorizacion se ejercitara **de conformidad con la voluntad, deseos y preferencias**
> de PERSONA CON DISCAPACIDAD A.

Frase forzada y ademas contradictoria: se afirma haber recabado una voluntad que se acaba de declarar indeterminable,
y se promete ejercitar la autorizacion conforme a ella. En un expediente del art. 264 es justo el parrafo que el
Tribunal lee. **Corregido:** el hecho QUINTO tiene ahora dos bloques condicionales **excluyentes**, uno por valor de
V4; el de V4 = 2 invoca el art. 249, parrafo tercero, y los placeholders `{{descripcion_esfuerzo_determinar_voluntad}}`
y `{{trayectoria_creencias_valores}}`, en paralelo al asset de curatela. Y se reescribio la seccion 7 del `SKILL.md`
para decir que hay dos bloques excluyentes y prohibir expresamente escribir "esta voluntad se ha recabado" con V4 = 2.

**Defecto 2 — texto fijo que contradice su propio bloque condicional.** El hecho SEGUNDO afirmaba en texto fijo
*"sin que consten medidas de apoyo voluntarias ni judiciales que se esten aplicando eficazmente"*, y tres lineas mas
abajo el bloque condicional para el caso contrario empieza *"Consta que {{descripcion_medidas_existentes}}..."*.
Activado el bloque, el escrito dice "sin que consten" y "Consta que" en parrafos consecutivos. **Corregido:** la
afirmacion negativa se extrajo a su propio bloque condicional, excluyente con el existente.

**Defecto 3 (menor) — concordancia de genero forzada.** La comparecencia fijaba *"domiciliado en"*. En este caso la
guardadora es la hija, y el LLM tiene que reescribir texto que la plantilla dio por cerrado. **Corregido** a
*"con domicilio en"*, valido para ambos generos.

Lectura de corrido: el escrito resultante **si suena a documento judicial real**. Encabezamiento al Tribunal de
Instancia, comparecencia, seis HECHOS con una idea por apartado, seis FUNDAMENTOS en el orden competencia /
legitimacion / postulacion / fondo / contenido / tramite, SUPLICO individualizado con finca registral y precio
minimo, y relacion de documentos correlativa a los hechos. Verificacion final del documento generado: **cero
placeholders sin resolver, cero comentarios HTML, cero lineas en blanco dobles, cero terminologia prohibida.**

### C) Veredicto sobre los tres puntos criticos

**C1. Subsidiariedad de la curatela — PASA, y por partida doble.** Es el punto que el escenario ataca: el cliente
pide "incapacitar" pero relata una guarda de hecho que funciona. La skill **no enruta a curatela por ninguno de los
dos caminos posibles**:
- Camino recorrido: la regla de enrutamiento *"Si lo que se pretende es una incapacitacion ... reconducir el caso por
  V1, sin detener el flujo"* obliga a preguntar V1 en vez de traducir "incapacitar" a curatela. El cliente elige la
  opcion 2 y se va directo a la HOJA GUARDA.
- Camino alternativo verificado sobre el papel: si un LLM resolviera V1 = 3 por escucha activa (lectura defendible
  de "quiero incapacitar"), V2.a queda resuelto en 1 por el propio relato ("vivo con ella y me ocupo de todo") y el
  filtro del art. 269 **bloquea** antes de pedir un solo dato de relleno, ofreciendo como salida numerada la
  autorizacion puntual del art. 264. Ambos caminos convergen en el mismo documento. La skill es robusta aqui, que es
  lo que hay que exigirle: no depende de que el LLM acierte la lectura del primer mensaje.

**C2. Terminologia — PASA.** La correccion se emite **una sola vez**, en el turno 1, antes de la introduccion, sin
reproche y sin volver a mencionarse en ningun turno posterior. `grep -niE 'incapaz|incapacitad|modificacion de la
capacidad|tutor|tutela|discapacitad[ao]|padece|alzheimer'` sobre el documento generado: **cero coincidencias**. El
unico falso positivo es la cita literal del art. 264 ("adecuados a las circunstancias del caso").

**C3. Voluntad y preferencias — FALLABA; corregido.** El regimen se recoge en el `SKILL.md` (guardrail 4, vector V4,
seccion 7 de cada hoja) y se pregunta siempre, sin sustituirlo por el "interes superior". Pero en la hoja GUARDA la
implementacion estaba rota: el asset carecia del bloque de la rama V4 = 2 y producia el parrafo contradictorio del
defecto 1. Con la correccion aplicada, el escrito invoca ahora el criterio correcto del art. 249, parrafo tercero
—trayectoria vital, creencias y valores— en lugar de fingir una voluntad recabada.

### Otras comprobaciones

- Tras el `Write`, la skill **no** inserta un turno preguntando "¿desea empezar?": confirma ruta absoluta y encadena
  el anuncio de seccion y su primera pregunta en la misma respuesta. Cumplido.
- Competencia territorial: el piso esta en Medina del Campo y la residencia de la persona en Valladolid. La seccion 11
  obliga a confirmarlo expresamente cuando difieren, y el escrito se dirige correctamente a Valladolid (art. 62.1 LJV).
- Nombre del fichero: la skill manda `snake_case.md`; el nombre `apoyo-qa-prueba.md` lo impuso el arnes de esta QA.
  Artefacto de test, no defecto.

### Ficheros modificados por esta QA

- `derecho-civil/skills/derecho-civil-medidas-apoyo-discapacidad/assets/solicitud-autorizacion-guarda-hecho.md`
  (defectos 1, 2 y 3).
- `derecho-civil/skills/derecho-civil-medidas-apoyo-discapacidad/SKILL.md` (Punto 5, hoja GUARDA, seccion 7).
