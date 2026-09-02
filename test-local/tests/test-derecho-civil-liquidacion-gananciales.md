# Test de ejecucion — skill `derecho-civil-liquidacion-gananciales`

Ejecucion manual del arbol de decision sobre cuatro escenarios (3 principales + 1 contra-caso). Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: Codigo Civil (BOE-A-1889-4763), arts. 1315, 1316, 1344 a 1361, 1362 a 1368, 1373, 1392, 1397 a 1411 y 1435; y LEC (BOE-A-2000-323), arts. 806 a 811.
- Verificacion real efectuada el 02-03/09/2026 contra la API de legislacion consolidada del BOE (`.../legislacion-consolidada/id/{ID}/texto/bloque/{bloque}`, cabecera `Accept: application/xml`, tomando la ULTIMA `<version>` de cada bloque):
  - **Art. 1392 CC** vigente desde 23/07/2015 (Ley 15/2015): la sociedad concluye de pleno derecho al disolverse el matrimonio, al declararse nulo, al acordarse la separacion legal o al convenir los conyuges otro regimen.
  - **Arts. 807, 808 y 810 LEC** en la redaccion de la **LO 2/2022, de 21 de marzo (BOE-A-2022-4516), vigencia 23/03/2022**. Los arts. 806, 809 y 811 sin modificacion posterior (806 en su redaccion originaria de 08/01/2001; 809 y 811 con vigencia 01/10/2015).
  - **Art. 1361 CC** (presuncion de ganancialidad) vigente desde 03/07/2005; **art. 1358 CC** (reintegros por importe actualizado) desde 08/06/1981; **arts. 1397, 1398, 1403 y 1404 CC** verificados; **art. 1406.4.º CC** verificado con su limite ("en caso de muerte del otro conyuge").
  - **No existe modelo normalizado del CGPJ** para la solicitud de formacion de inventario ni para la liquidacion del regimen economico matrimonial: verificado el 02/09/2026 sobre el listado publicado (juicio verbal, monitorio, monitorio de propiedad horizontal, jurisdiccion voluntaria, asistencia juridica gratuita, denuncia, delitos leves y juicio rapido).
- En este test la lectura online se ejecuto realmente y estuvo disponible -> version verificada 02-03/09/2026.

---

## Test 1 — Acuerdo total, vivienda hipotecada adjudicada a un conyuge y compensacion en metalico

**Mensaje inicial:** "Me divorcie hace unos meses y la sentencia ya es firme. Estamos de acuerdo en todo: yo me quedo la casa, que tiene hipoteca, y le compenso a el con dinero. Necesito el documento del reparto."

### Recorrido del arbol
```
V4 -> PREGUNTA: regimen economico -> 3 (no lo sabe con certeza)
      sub-pregunta capitulaciones -> 1 (no otorgamos)
      guarda vecindad civil -> 1 (comun)                V4 = gananciales (Art. 1316 CC)
V1 -> escucha activa: "estamos de acuerdo en todo"      V1 = acuerdo (sin pregunta)
V2 -> escucha activa: "la sentencia ya es firme"        V2 = posterior a resolucion firme (sin pregunta)
V3 -> escucha activa: "la casa, que tiene hipoteca"     V3 = vivienda hipotecada (sin pregunta)
Validacion: sociedad YA disuelta (sentencia firme
      15/03/2026) -> bloques de disolucion producida
      y fecha de corte ACTIVADOS
HOJA CONVENIO -> assets/convenio-liquidacion-gananciales.md
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija + V4 (unico vector no resuelto por escucha activa).
- Turnos 2-3: sub-pregunta de capitulaciones y pregunta de guarda de vecindad civil. Al resolverse, la skill informa con el texto fijo del Art. 1316 CC por que el regimen es de gananciales.
- Turno 4: Confirmacion visible (Punto 3) con el texto fijo CONVENIO (Arts. 1392 y 1396 a 1410 CC, y Art. 806 LEC a contrario) + enlaces al BOE + aviso de elevacion a escritura publica por haber inmuebles + eleccion plantilla/documento propio.
- Turnos 5-7: primer conyuge (nombre, NIF, domicilio) con confirmacion agrupada en el turno posterior al ultimo dato.
- Turnos 8-10: segundo conyuge, confirmacion agrupada.
- Turnos 11-14: matrimonio y disolucion (fecha y lugar, registro civil, origen del regimen, fecha y causa de disolucion). Al fijar la disolucion, informa de que el 15/03/2026 es la fecha de corte del inventario (Art. 1397.1.º CC).
- Turno 15 y siguientes: activo (negociacion) — la skill explica primero el Art. 1347 CC, el Art. 1346 CC y **la presuncion del Art. 1361 CC** antes de pedir bienes, y despues pide bien a bien: vivienda 250.000, vehiculo 8.000, cuenta 12.000.
- Creditos de la sociedad contra un conyuge — usuario dice que no hay ninguno: bloque OMITIDO sin dejar rastro.
- Pasivo: deudas — hipoteca, saldo pendiente **certificado por la entidad** 90.000 a 31/08/2026 (la skill rechaza el importe inicial del prestamo y pide el certificado).
- Reintegros del Art. 1358 CC — **preguntados activamente** aunque el cliente no los mencione; usuario confirma que no hubo aportaciones privativas: bloque OMITIDO.
- Liquidacion — la skill NO pregunta cifras: calcula y muestra la operacion completa.
- Vivienda hipotecada (negociacion) — la skill explica PRIMERO que la adjudicacion no libera al otro frente al banco (Arts. 1367 y 1401 CC), confirma que el cliente lo entiende, y solo despues pide datos registrales, valor, entidad, escritura de prestamo, saldo, prestatarios y adjudicatario.
- Adjudicaciones (negociacion) — la skill advierte de que el Art. 1406.4.º CC **no da preferencia sobre la vivienda en un divorcio** (solo por fallecimiento) y de que el uso (Art. 96 CC) es cosa distinta de la propiedad.
- Exceso de adjudicacion — la skill lo calcula sola (70.000), advierte del posible coste fiscal SIN cuantificarlo ni citar preceptos tributarios, expone las cinco alternativas y pide importe, forma y medio de pago.
- Reparto de deudas, gastos e impuestos, eficacia y formalizacion (plazo de escritura publica), lugar y fecha.

### Documento generado (fichero real: `test-local/output/convenio-liquidacion-gananciales-prueba.md`)
```
CONVENIO DE LIQUIDACION DE LA SOCIEDAD DE GANANCIALES DE CONYUGE A Y CONYUGE B
> DRAFT — para revision por un abogado colegiado antes de su firma...
> Version del Codigo Civil y de la LEC verificada en el BOE: 02/09/2026

PRIMERA — activo: vivienda 250.000 + vehiculo 8.000 + cuenta 12.000 = TOTAL ACTIVO 270.000
SEGUNDA — pasivo: hipoteca, saldo pendiente 90.000 a 31/08/2026 segun certificado = TOTAL PASIVO 90.000
TERCERA — haber liquido 180.000; haber de cada conyuge 90.000 (Arts. 1344 y 1404 CC)
CUARTA — lote A: vivienda 250.000 con asuncion de hipoteca 90.000 -> 160.000
         lote B: vehiculo 8.000 + cuenta 12.000 -> 20.000
QUINTA — "...la liberacion de CONYUGE B frente a la entidad acreedora requiere el consentimiento
         expreso de esta, que el presente convenio no puede producir por si mismo tal liberacion
         al no ser la entidad parte en el..." (Arts. 1367 y 1401 CC)
SEXTA — exceso de adjudicacion: CONYUGE A abona 70.000 a CONYUGE B (Art. 1407 CC)
SEPTIMA a DECIMA — deudas y responsabilidad frente a terceros, finiquito, gastos, eficacia
```
Comprobado sobre el fichero real: **cero comentarios HTML**, **cero placeholders sin resolver**, cero HTML crudo, ordinales continuos de PRIMERA a DECIMA sin saltos, y la aritmetica cuadra (160.000 - 70.000 = 90.000; 20.000 + 70.000 = 90.000).

Resultado: **PASA**. Ninguna clausula afirma la liberacion del conyuge no adjudicatario, y la advertencia sobre el banco aparece tanto en la clausula quinta como en las advertencias finales.

---

## Test 2 — Sin acuerdo sobre si un inmueble es privativo o ganancial

**Mensaje inicial:** "Estoy en pleno divorcio, la demanda ya se admitio. Mi mujer dice que el local comercial es suyo porque lo pago con una donacion de su madre, pero se compro estando casados y se pago de la cuenta comun. No nos ponemos de acuerdo en nada del reparto."

### Recorrido del arbol
```
V4 -> PREGUNTA: regimen -> 1 (sociedad de gananciales)  V4 = gananciales
V1 -> escucha activa: "no nos ponemos de acuerdo"       V1 = sin acuerdo (sin pregunta)
V2 -> escucha activa: "estoy en pleno divorcio, la
      demanda ya se admitio"                            V2 = proceso en curso (sin pregunta)
V3 -> PREGUNTA: vivienda hipotecada -> 1 (si)           V3 = vivienda hipotecada
Validacion: sociedad NO disuelta todavia, pero la
      demanda esta ADMITIDA -> Art. 808.1 LEC permite
      el inventario ya -> bloques de "disolucion en
      curso" y "fecha de referencia" ACTIVADOS
HOJA JUDICIAL -> 1º assets/propuesta-inventario.md
                 2º assets/solicitud-formacion-inventario.md
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija + V4.
- Turno 2: V3.
- Turno 3: dialogo previo sobre la via — la skill explica el coste real del procedimiento judicial (dos fases sucesivas, comparecencias, posible juicio verbal, contador y peritos a cargo de la masa, meses o anos) y pregunta si desea intentar el acuerdo antes. Usuario responde que ya lo intento y no fue posible: se mantiene la HOJA JUDICIAL sin presionar.
- Turno 4: Confirmacion visible con el texto fijo JUDICIAL (Arts. 806 a 810 LEC, dos fases, propuesta del Art. 808.2) + nota de la redaccion LO 2/2022 + **nota de que no hay que esperar a la sentencia para el inventario (Art. 808.1) pero si para la liquidacion (Art. 810.1)** + eleccion plantilla/documento propio.
- Turnos 5-10: conyuge solicitante y conyuge contrario, con confirmacion agrupada por parte.
- Turnos 11-14: matrimonio y disolucion en curso (fecha de admision de la demanda 05/05/2026, fecha de referencia del inventario).
- Activo (negociacion) — explicacion previa de los Arts. 1346, 1347 y **1361** CC; despues, bien a bien, con **su documento justificativo** en cada partida: vivienda 250.000, local 95.000, cuenta 14.000.
- Bienes enajenados fraudulentamente (Art. 1397.2.º) — no concurre: bloque OMITIDO.
- Creditos de la sociedad contra un conyuge — si concurre: fondos comunes que amortizaron un prestamo privativo anterior al matrimonio de la contraria; 9.000 originales, actualizados a 11.200 con criterio de IPC explicito.
- Pasivo: deudas — hipoteca 90.000 certificada.
- Reintegros del Art. 1358 — preguntados activamente: 30.000 de una herencia del solicitante aportados a la entrada de la vivienda, actualizados a 38.500 con criterio explicito y dos documentos (escritura de herencia + justificante de la transferencia).
- **Partidas controvertidas (negociacion)** — la skill explica el Art. 809.2 LEC (juicio verbal y sentencia) y **quien soporta la carga de la prueba** conforme al Art. 1361 CC; pide, en turnos separados, descripcion del local, caracter que le atribuye la contraria, motivo concreto de la inclusion en el activo, y prueba disponible.
- Documentos justificativos — recorrido partida por partida, numerados.
- Despues: solicitud judicial — juzgado competente (Art. 807 LEC, **sin preguntar en que juzgado desea presentarlo**), estado del proceso, falta de acuerdo, bienes discutidos volcados sin repreguntar, medidas de administracion, otrosies condicionales, representacion procesal (preceptiva) y cierre.

### Documento generado (fichero real: `test-local/output/propuesta-inventario-prueba.md`)
```
PROPUESTA DE INVENTARIO DE LA SOCIEDAD DE GANANCIALES DE CONYUGE A Y CONYUGE B

Disolucion: "...quedara disuelta de pleno derecho al dictarse la resolucion que le ponga termino...
La formacion de inventario se solicita al amparo del articulo 808.1 LEC, que la permite una vez
admitida la demanda, sin necesidad de esperar a la disolucion."
Fecha de referencia del inventario: 03/09/2026 (no "fecha de corte": la disolucion no se ha producido)

II. ACTIVO   A) vivienda 250.000 + local 95.000 + cuenta 14.000 = 359.000
             B) creditos de la sociedad (Art. 1397.3.º): 9.000 -> actualizado 11.200
             TOTAL ACTIVO 370.200
III. PASIVO  A) hipoteca 90.000
             B) reintegro al solicitante (Art. 1358): 30.000 -> actualizado 38.500
             TOTAL PASIVO 128.500
IV. Haber liquido provisional: 241.700

V. PARTIDAS CONTROVERTIDAS
"...Esta parte lo incluye en el activo ganancial porque fue adquirido a titulo oneroso el 14/04/2016,
constante la sociedad, mediante escritura publica en la que no se hizo constar la procedencia privativa
del precio... No consta acreditada la donacion alegada ni la trazabilidad del dinero donado hasta el
pago del precio.
...se invoca la presuncion del articulo 1361 del Codigo Civil... correspondiendo la carga de dicha
prueba a quien alega el caracter privativo."
```
Comprobado sobre el fichero real: cero comentarios HTML, cero placeholders sin resolver, letras de partida resueltas como **B)** en activo y en pasivo (correcto: el bloque del Art. 1397.2.º no se inserto, luego `{{letra_partida_creditos_sociedad}}` = B y no C), y las citas de documentos del cuerpo coinciden una a una con la relacion final (nº 4 a nº 11).

Resultado: **PASA**. La propuesta no da por pacifica la naturaleza del local: expresa el motivo concreto de su inclusion y la prueba, e invoca la presuncion con su carga probatoria.

---

## Test 3 — Liquidacion posterior a divorcio firme con reintegro de dinero privativo invertido en la vivienda

**Mensaje inicial:** "Me divorcie hace tres anos y nunca liquidamos los gananciales. Cuando compramos el piso yo puse 40.000 euros que heredé de mi padre. Ahora quiero que eso se tenga en cuenta en el reparto."

### Recorrido del arbol
```
V4 -> PREGUNTA: regimen -> 1 (sociedad de gananciales)  V4 = gananciales
V2 -> escucha activa: "me divorcie hace tres anos"      V2 = posterior a resolucion firme (sin pregunta)
V1 -> PREGUNTA: acuerdo -> 1 (si, estamos de acuerdo
      en el reparto y en el reintegro)                  V1 = acuerdo
V3 -> PREGUNTA: vivienda hipotecada -> 2 (la hipoteca
      ya esta pagada)                                   V3 = sin hipoteca pendiente
Validacion: sociedad disuelta desde la firmeza; no hay
      plazo legal para liquidar, la comunidad
      postmatrimonial ha subsistido tres anos
HOJA CONVENIO -> assets/convenio-liquidacion-gananciales.md
                 (bloque de vivienda hipotecada NO se inserta)
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija + V4.
- Turnos 2-3: V1 y V3.
- Turno 4: Confirmacion visible con el texto fijo CONVENIO. La skill informa ademas de que el Codigo Civil no fija plazo para liquidar y de que la comunidad postmatrimonial ha subsistido durante esos tres anos.
- Turnos 5-14: conyuges y datos del matrimonio y de la disolucion, con confirmacion agrupada por parte.
- Activo y pasivo, como en el Test 1.
- **Reintegros del Art. 1358 CC — el nucleo de este escenario.** La skill explica, antes de preguntar: que el articulo 1358 obliga a reembolsar el valor satisfecho **por su importe actualizado al tiempo de la liquidacion**, no por la cifra nominal; que el reintegro **no convierte al aportante en propietario de una cuota mayor** de la vivienda, sino en acreedor de la sociedad; y que hay que poder acreditarlo. Despues pregunta expresamente por dinero propio de herencias, donaciones o ahorros anteriores aportado a bienes comunes, y por la documentacion. Usuario aporta la escritura de herencia y el justificante de la transferencia. La skill pide el criterio de actualizacion, lo hace explicito en el documento y calcula el importe resultante; **no inventa un criterio que las partes no hayan pactado**.
- Liquidacion — el reintegro entra en el **pasivo** (Art. 1398.3.ª) y se cobra **antes de dividir** (Art. 1403), de modo que el remanente que se divide por mitad ya esta minorado en los 40.000 actualizados. La skill muestra la operacion paso a paso.
- Adjudicaciones, gastos, eficacia y cierre.

### Extracto sintetico del documento generado
```
SEGUNDA — pasivo
B) Creditos de los conyuges contra la sociedad. Reintegros y reembolsos (Arts. 1358, 1364 y 1398.3.ª CC)
1. Reintegro a favor de CONYUGE A por la aportacion de dinero privativo, procedente de la herencia de
   su padre, al pago del precio de la vivienda. Importe original aportado: 40.000 euros. Importe
   actualizado: {{importe_actualizado_reintegro}} euros.
Las partes hacen constar que el criterio de actualizacion aplicado es {{criterio_actualizacion_reintegros}}.

TERCERA — liquidacion
Practicadas las compensaciones que corresponden conforme al articulo 1403 del Codigo Civil, el total a
percibir por cada parte queda fijado en: [...]
```
Resultado: **PASA**. El reintegro se coloca en el pasivo y se paga antes de dividir, no como un reparto desigual del haber; el criterio de actualizacion queda explicito; y el bloque de vivienda hipotecada no aparece en el documento (V3 = 2), con los ordinales de clausula recalculados en consecuencia (la clausula de deudas pasa a ser QUINTA, no SEPTIMA).

---

## Contra-caso — Matrimonio en regimen de separacion de bienes

**Mensaje inicial:** "Nos casamos en separacion de bienes y ahora nos divorciamos. Necesito el documento para liquidar los gananciales y repartir el piso que compramos entre los dos."

### Recorrido del arbol
```
V4 -> escucha activa: "nos casamos en separacion de
      bienes"                                           V4 = separacion de bienes
Enrutamiento: V4 = separacion de bienes -> DETENER
      (Arts. 1435 CC y 806 LEC)
```

### Comportamiento esperado
La skill **no pregunta V1, V2 ni V3, no pasa a la Confirmacion ordinaria y no crea ningun documento**. En el mismo turno emite el texto fijo de detencion por separacion de bienes: que en ese regimen no existe masa comun de bienes y derechos, por lo que no hay sociedad conyugal que liquidar (Art. 1435 CC); que el procedimiento de los Arts. 806 y siguientes de la LEC no le resulta aplicable, porque el propio Art. 806 lo circunscribe a los regimenes que determinan la existencia de una masa comun; y que **el piso comprado por ambos les pertenece en proindiviso y su reparto se articula como una division de cosa comun de los Arts. 400 y siguientes del Codigo Civil, que es una operacion distinta y no esta cubierta por esta skill**. Incluye el enlace al BOE y ofrece escalacion.

Es importante que la skill **no se limite a decir "fuera de alcance"**: el cliente tiene un problema real (repartir el piso comun) y la respuesta correcta le explica por que su caso no es una liquidacion de gananciales y cual es la figura que si le corresponde.

**Resultado: PASA.** La deteccion se produce en el primer turno, por escucha activa, antes de cualquier otra pregunta y antes de crear nada.

---

## Verificacion en vivo (no solo sobre el papel)

Ademas del recorrido simulado de los cuatro escenarios, se ejecutaron realmente los Escenarios 1 y 2 como lo haria el agente operacional, sin instalar el plugin como skill invocable de Claude Code (no esta registrado en este entorno):

1. **Verificacion normativa real** contra la API de legislacion consolidada del BOE de los arts. 1315, 1316, 1344 a 1361, 1362 a 1368, 1373, 1392, 1397 a 1411 y 1435 CC y de los arts. 806 a 811 LEC, tomando en cada bloque la ultima `<version>`. Confirmadas palabra por palabra las fechas de vigencia registradas en `references/fuentes-plantillas-validadas.md`, incluida la de la LO 2/2022 (23/03/2022) en los arts. 807, 808 y 810 LEC, y comprobado que los arts. 806, 809 y 811 **no** fueron modificados por esa ley. Verificado tambien en el portal del CGPJ que no existe modelo normalizado para estos escritos.
2. **Punto 4 real**: `Write` de `test-local/output/convenio-liquidacion-gananciales-prueba.md` y de `test-local/output/propuesta-inventario-prueba.md`, `Read` de verificacion y ciclos de `Edit` incremental con el `oldString` copiado literalmente del `Read` previo. Los `Edit` se aplicaron a la primera, sin fallos de coincidencia de texto.
3. **Comprobacion automatizada de los tres assets** contra las cuatro reglas de plantillas render-safe: 82, 43 y 39 placeholders unicos respectivamente, **cero** placeholders con texto de ayuda o espacios dentro de las llaves, cero anidados, cero llaves desparejadas, cero corchetes simples tipo `[DATO]`, cero HTML crudo distinto de comentarios, comentarios HTML balanceados, cero marcadores genericos `{{DATO_FALTANTE}}` y cero saltos de linea blandos en bloques de datos.
4. **Comprobacion de los documentos generados**: cero comentarios HTML residuales, cero placeholders sin resolver, cero HTML crudo, ordinales de clausula continuos, letras de partida correctamente degradadas a B) al omitirse el bloque del Art. 1397.2.º, y citas de documentos coincidentes una a una con la relacion final.

---

## Revision UX

Hallazgos:

1. **Preguntar el regimen economico PRIMERO, antes que el acuerdo.** Es el unico vector que puede dejar el caso enteramente fuera de alcance (separacion de bienes, participacion, derecho foral). Preguntarlo al final habria hecho que el cliente del contra-caso recorriera tres preguntas y una confirmacion para acabar en una detencion. El coste de anteponerlo es nulo.
2. **Muchos clientes no saben su regimen economico.** La pregunta binaria "gananciales / otro" con la tercera opcion "no lo sabe con certeza" y su sub-pregunta de capitulaciones resuelve el caso mayoritario aplicando el Art. 1316 CC, sin obligar al cliente a saber derecho. **Ajuste aplicado:** anadida la pregunta de guarda de vecindad civil antes de aplicar el regimen supletorio, porque en territorio de derecho civil propio el supletorio no es el de gananciales; sin ella, la skill habria dado por gananciales un matrimonio catalan.
3. **Los reintegros del Art. 1358 CC hay que preguntarlos activamente.** Es el concepto que mas dinero mueve y el que el cliente desconoce por completo: nunca lo va a mencionar por su cuenta. **Ajuste aplicado:** la seccion de reintegros lleva la instruccion expresa de que "no se omite nunca por silencio del cliente" y de preguntar en los dos sentidos (dinero privativo a bien comun y dinero comun a bien privativo).
4. **La advertencia sobre el banco va ANTES de redactar, no despues.** Si la clausula se escribe primero y la advertencia llega al final, el cliente ya ha formado la expectativa equivocada. **Ajuste aplicado:** la seccion de vivienda hipotecada exige explicar y confirmar la comprension antes de pedir cualquier dato, y el SKILL.md prohibe expresamente redactar una clausula que afirme la liberacion del otro conyuge, con la redaccion correcta y la prohibida escritas en la reference.
5. **Explicar el coste real de la via judicial antes de crear los escritos, sin presionar.** El Art. 806 LEC hace del procedimiento un cauce subsidiario del acuerdo, y las dos fases con contador y peritos a cargo de la masa son un dato material que el cliente merece conocer. **Ajuste aplicado:** seccion de "dialogo previo sobre la via" con la instruccion expresa de no condicionar la continuacion a que acepte negociar.
6. **No prometer preferencia sobre la vivienda.** El Art. 1406.4.º CC limita esa preferencia al caso de muerte del otro conyuge. Un cliente divorciado que oiga "la ley me da preferencia" tomara decisiones sobre una premisa falsa. **Ajuste aplicado:** guardrail expreso y advertencia en la seccion de adjudicaciones, distinguiendo la adjudicacion de la propiedad de la atribucion del uso del Art. 96 CC.
7. **Fiscalidad: advertir sin cuantificar.** El exceso de adjudicacion tiene coste fiscal potencial, pero su tratamiento depende de la comunidad autonoma y de si el exceso es inevitable. **Ajuste aplicado:** guardrail que prohibe citar tipos, exenciones o preceptos tributarios, cuantificar el impuesto o afirmar que la operacion esta exenta, con derivacion obligatoria a asesor fiscal.

Ajustes aplicados durante el test, ademas de los anteriores:

8. **Error legal corregido — el inventario se puede pedir ANTES de la disolucion.** La primera version de la skill y de los tres assets daba por producida la disolucion en todos los casos ("la sociedad quedo disuelta el..."), lo que es falso cuando el divorcio esta en tramite: el Art. 808.1 LEC permite solicitar la formacion de inventario desde la **admision** de la demanda, y solo la segunda fase, la solicitud de liquidacion del Art. 810.1, exige que la resolucion sea firme. Detectado al montar el Escenario 2. **Fix aplicado:** los tres assets llevan ahora bloques condicionales alternativos de "disolucion ya producida" y "disolucion en curso" (con fecha de referencia del inventario en lugar de fecha de corte); la validacion de presupuestos del SKILL.md distingue las tres situaciones (disuelta / en curso / no disuelta sin demanda ni capitulaciones, esta ultima la unica que detiene); el guardrail 6 y la fila de escalacion se reescribieron para no confundir la separacion de hecho con la disolucion en curso; y la reference de la LEC lleva un apartado propio sobre esta clave.
9. **Cuadre al centimo en importes fraccionados.** Al fraccionar en tres pagos la compensacion de 70.000 euros del Escenario 1, el reparto obvio (23.333,33 x 3) suma 69.999,99. **Fix aplicado:** regla expresa en el Punto 5 del SKILL.md de ajustar la diferencia en el primer pago y verificar la suma antes de la vista previa.
10. **Numeracion unica de documentos en la HOJA JUDICIAL y prohibicion de renumerar en masa.** La propuesta es ella misma uno de los documentos que acompanan a la solicitud, de modo que sus justificantes no pueden empezar en el nº 3. Al renumerarlos, una sustitucion global de texto corrompio una cita doble ("Documentos nº 8 y nº 9" -> "Documentos nº 9 y nº 9"). **Fix aplicado:** el Punto 4 del SKILL.md establece numeracion unica compartida por los dos documentos, obliga a reservar los numeros antes de citarlos y prohibe renumerar mediante sustitucion masiva, exigiendo correccion cita por cita con `Edit` y relectura de comprobacion.
11. **Postulacion tratada como preceptiva.** Los Arts. 806 a 811 LEC no contienen regla propia de postulacion. **Fix aplicado:** posicion conservadora registrada en `references/fuentes-plantillas-validadas.md` (punto 7 de "Verificar manualmente") y en la seccion de representacion procesal: se tratan abogado y procurador como preceptivos y se prohibe afirmar al cliente que puede comparecer por si mismo.

---

## QA en vivo por agente independiente

Ejecutado el 03/09/2026 por un agente sin contexto previo de la skill. Escenario: *"Nos divorciamos el año pasado y ahora queremos repartir. Tenemos el piso con 80.000 euros de hipoteca pendiente, dos coches y unos ahorros. Yo puse 30.000 euros de una herencia mía para la entrada del piso. Estamos de acuerdo en que el piso se lo queda él y me compensa."*

Documento generado de verdad en `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/gananciales-qa-prueba.md` (`Write` + `Read` de verificación + 20 `Edit` incrementales con `oldString` copiado literalmente). Punto 2 ejecutado de verdad contra la API de legislación consolidada del BOE.

### Verificación normativa real (Punto 2)

Consultados bloque a bloque, tomando la última `<version>`: CC arts. 1316, 1358, 1361, 1367, 1392, 1397, 1398, 1401, 1403, 1404, 1406 y 1407; LEC arts. 806, 807, 808 y 810. Coincide al literal con lo registrado en `references/fuentes-plantillas-validadas.md`: art. 1358 vigente desde 08/06/1981 con la fórmula "reintegro de su importe actualizado al tiempo de la liquidación"; art. 1361 y 1404 desde 03/07/2005; art. 1392 desde 23/07/2015; y arts. 807, 808 y 810 LEC con `fecha_vigencia="20220323"` (LO 2/2022), mientras que el 806 conserva una sola versión de 08/01/2001. **No procede auto-actualización.**

### Transcripción literal de los turnos generados

**Turno 1 (carga + introducción + primera pregunta de clasificación):**

> **Skill cargada satisfactoriamente.**
>
> Vamos a proceder a la preparación de los documentos necesarios para repartir el patrimonio común de su matrimonio. Para determinar correctamente el cauce que corresponde a su caso, es necesario precisar antes algunos datos.
>
> El régimen económico de su matrimonio era:
> 1. Sociedad de gananciales
> 2. Otro régimen distinto de la sociedad de gananciales
> 3. No lo sabe con certeza

*Cliente: "No lo sé con certeza, la verdad."* → sub-pregunta de capitulaciones → *"No otorgamos capitulaciones."* → pregunta de guarda de vecindad civil → *"Común, los dos somos de Madrid de toda la vida."*

**Turno 4 (resolución de V4 + Confirmación del Punto 3):**

> A falta de capitulaciones matrimoniales, el régimen económico de su matrimonio es el de sociedad de gananciales, que el Código Civil establece como régimen legal supletorio en su artículo 1316.
>
> A su caso corresponde la liquidación de la sociedad de gananciales de mutuo acuerdo, que se rige por los artículos 1392 y 1396 a 1410 del Código Civil. El artículo 806 de la Ley 1/2000, de Enjuiciamiento Civil, reserva el procedimiento judicial para el caso de falta de acuerdo entre los cónyuges, de modo que, existiendo acuerdo, no es necesario acudir a él. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323
>
> Si el inventario comprende bienes inmuebles, el convenio deberá elevarse a escritura pública notarial para poder inscribir las adjudicaciones en el Registro de la Propiedad.
>
> ¿Qué documento desea utilizar como base?
> 1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
> 2. Adjuntar su propio documento

V1, V2 y V3 quedaron resueltos por Escucha Activa desde el primer mensaje del cliente ("estamos de acuerdo", "nos divorciamos el año pasado", "80.000 euros de hipoteca pendiente") y **no se volvieron a preguntar**.

**Sección 4 — activo, explicación previa y resolución del carácter de la vivienda:**

> Pasamos ahora al inventario del activo: los bienes y derechos comunes.
>
> Antes de relacionarlos conviene que conozca tres reglas que determinan qué entra en este inventario y qué no.
>
> Son gananciales los bienes obtenidos por el trabajo o la industria de cualquiera de ustedes, los frutos, rentas e intereses que produzcan tanto los bienes comunes como los privativos, y lo adquirido a título oneroso a costa del caudal común (artículo 1347 del Código Civil). Son privativos los que ya le pertenecían a cada uno al casarse, los recibidos por herencia o donación y los adquiridos a costa o en sustitución de bienes privativos (artículo 1346 del Código Civil).
>
> El punto de partida legal, sin embargo, es el artículo 1361 del Código Civil: se presumen gananciales todos los bienes existentes en el matrimonio mientras no se pruebe que pertenecen privativamente a uno de los dos. Esto significa que quien sostenga que un bien es suyo debe probarlo, y que la escritura esté a su nombre no basta por sí solo.
>
> Por último, el inventario se cierra a la fecha de disolución de la sociedad, que en su caso es el 2 de abril de 2025: lo que cada uno haya adquirido después no entra en este reparto.
>
> Comencemos por la vivienda. Indíqueme su dirección completa, sus datos registrales y su referencia catastral.

> Antes de fijar el carácter de la vivienda debo precisar un extremo. Me indica usted que aportó 30.000 euros de una herencia propia al pago de la entrada. Cuando el precio de un bien se satisface en parte con dinero común y en parte con dinero privativo, el artículo 1354 del Código Civil lo atribuye pro indiviso a la sociedad y al cónyuge aportante en proporción al valor de sus respectivas aportaciones; y el artículo 1356 hace depender la naturaleza del bien adquirido con precio aplazado de cuál fuera el primer desembolso.
>
> Indíqueme, por tanto, dos extremos: si la entrada se pagó íntegramente con sus 30.000 euros de la herencia o hubo además dinero de la cuenta común, y si figuran ambos como compradores en la escritura, con atribución de cuotas o sin ella.

*Cliente: "La entrada fueron 60.000: 30.000 míos de la herencia y 30.000 de nuestros ahorros. En la escritura compramos los dos, sin decir porcentajes."*

> Con esos datos la vivienda es ganancial. Adquirieron ambos conjuntamente y sin atribución de cuotas, supuesto en el que el artículo 1355 del Código Civil presume la voluntad favorable a la ganancialidad, y la adquisición se hizo a título oneroso con concurrencia de caudal común (artículo 1347.3.º). Sus 30.000 euros no le convierten en titular de una cuota mayor de la vivienda: le convierten en acreedora de la sociedad, y los trataremos como tal más adelante, en la partida de reintegros del pasivo.

**Sección 7 — reintegros (art. 1358 CC):**

> Corresponde ahora determinar los reintegros que la sociedad deba a cada uno de ustedes. Es la partida que más dinero mueve en una liquidación y la que con más frecuencia se pasa por alto, de modo que conviene que la examinemos con detenimiento.
>
> El artículo 1358 del Código Civil establece que, cuando una de las dos masas patrimoniales paga lo que corresponde a la otra, debe reembolsarse el valor satisfecho mediante el reintegro de su importe actualizado al tiempo de la liquidación, no por la cifra nominal de entonces. La regla funciona en los dos sentidos: el dinero privativo invertido en un bien común genera un crédito del cónyuge contra la sociedad, y el dinero común invertido en un bien privativo genera un crédito de la sociedad contra el cónyuge.
>
> Dos precisiones importantes. La primera, que el reintegro no le convierte en propietaria de una cuota mayor del bien: le convierte en acreedora por su importe. La segunda, que debe poder acreditarse documentalmente; una aportación sin rastro documental es una pretensión discutible, no una partida del inventario.
>
> Sus 30.000 euros procedentes de la herencia son exactamente este supuesto. Indíqueme con qué documentación puede acreditar tanto el origen hereditario del dinero como su aplicación al pago de la entrada de la vivienda.

*Cliente: "Tengo la escritura de aceptación de la herencia de mi padre, de marzo de 2009, y el justificante de la transferencia de mayo de 2010 desde mi cuenta."*

> La documentación es suficiente: acredita el origen privativo del dinero y su destino, que son los dos extremos que se discuten en esta partida.
>
> Queda por fijar el importe. El artículo 1358 del Código Civil ordena el reintegro por su importe actualizado al tiempo de la liquidación, y han transcurrido dieciséis años desde la aportación. Esa actualización no la puedo estimar yo: exige un criterio pactado por ambos, como la variación de un índice oficial certificada para el periodo, o, en su defecto, un peritaje. Indíqueme qué criterio desean aplicar.

*Cliente: "Preferimos no complicarlo. Hemos acordado reconocer los 30.000 y ya está."*

> Queda constancia. Debo advertirle expresamente de que reconocer el importe nominal supone renunciar a la actualización que el artículo 1358 del Código Civil le reconocería, y que en dieciséis años esa diferencia puede ser relevante en su contra. Como el acuerdo es de ambos y usted es la parte que renuncia, lo haré constar así en el convenio, con mención expresa de que han sido informados.

**Sección 9 — vivienda hipotecada:**

> Abordamos ahora la vivienda familiar y el préstamo hipotecario que la grava.
>
> Antes de redactar nada necesito que quede claro un punto que suele malinterpretarse y que en su caso es el más importante de todo el convenio.
>
> Este convenio es un contrato entre ustedes dos. El banco no lo firma, no es parte en él y no queda vinculado por lo que ustedes pacten. Que la vivienda se adjudique a CONYUGE B y que él asuma el pago del préstamo no le libera a usted frente a la entidad: si ambos firmaron la escritura de préstamo, ambos siguen obligados frente al banco en los mismos términos, y la entidad podrá reclamarle a usted la totalidad con independencia de quién se quede la casa (artículos 1367 y 1401 del Código Civil).
>
> Lo que sí produce el convenio es un efecto interno entre ustedes: CONYUGE B queda obligado a pagar y a mantenerla a usted indemne, y si usted acabara pagando algo que según el convenio le correspondía a él, tendría acción para repetir contra él. Es una garantía real, pero indirecta y de recuperación posterior: no impide que el banco le reclame, ni que un impago suyo le perjudique a usted en su historial de crédito y le dificulte obtener financiación propia.
>
> La única forma de liberarla de verdad es que la entidad lo acepte mediante una novación subjetiva del préstamo. Esa es una decisión exclusiva del banco: no existe precepto que le obligue a aceptarla, y con frecuencia la deniega cuando la solvencia de quien se queda la vivienda no cubre por sí sola la cuota.
>
> Le pido que me confirme que este punto ha quedado claro antes de continuar.

*Cliente: "Sí, entendido. Pensaba que firmando esto ya me quitaba la hipoteca de encima."*

> Es la expectativa más frecuente, y por eso conviene desmontarla antes de firmar y no después.

Y al preguntar por la novación (*"Todavía no lo hemos consultado"*):

> Le recomiendo consultarlo con la entidad antes de firmar. Si la deniega, usted quedaría obligada frente al banco por un préstamo que grava una vivienda que ya no es suya y de la que no dispone. En ese escenario conviene valorar seriamente la venta del inmueble y el reparto del precio, que elimina de una vez la indivisibilidad y la hipoteca.

**Sección 11 — exceso de adjudicación:**

> Comprobamos si el reparto produce un exceso de adjudicación que deba compensarse. Hecho el cálculo, sí lo produce.
>
> Los bienes que se adjudican a CONYUGE B suman 249.000 euros, pero asume los 80.000 euros pendientes del préstamo hipotecario, de modo que el valor neto de su lote es de 169.000 euros, frente a los 84.500 euros que le corresponden. Recibe, por tanto, 84.500 euros de más, que es exactamente lo que a usted le falta: su lote asciende a 30.000 euros frente a los 114.500 euros que debe percibir.
>
> El artículo 1407 del Código Civil establece que quien recibe bienes por valor superior al de su haber debe abonar la diferencia en dinero. La causa aquí es la habitual: la vivienda es indivisible y concentra la mayor parte del valor del activo.
>
> Debo advertirle de que el exceso de adjudicación puede tener consecuencias fiscales. Su tratamiento depende de la normativa estatal y autonómica aplicable y de si el exceso resulta o no inevitable por la indivisibilidad del bien, y excede el alcance de este servicio: consúltenlo con un asesor fiscal antes de firmar. No puedo indicarle tipos, exenciones ni importes.
>
> Antes de fijar la compensación conviene que conozcan las alternativas: la compensación en metálico, que exige liquidez a CONYUGE B; que asuma más deuda, lo que reduce el exceso pero sigue sin liberarla a usted frente al banco; adjudicarle a usted otros bienes, para lo que aquí no hay patrimonio suficiente; vender el inmueble y repartir el precio, que resuelve de golpe la indivisibilidad y la hipoteca; o mantener la copropiedad temporalmente, que sólo aplaza el conflicto a una futura división de cosa común.

*Cliente: "Compensación en metálico, pero no puede pagarlo de golpe. En tres años."*

> Repartida en tres plazos anuales, la cantidad no admite división exacta, de modo que el primer plazo absorbe la diferencia: 28.166,68 euros el primero y 28.166,66 euros cada uno de los dos restantes, que suman exactamente 84.500 euros.
>
> Debo advertirle además de que la cláusula octava declarará liquidada la sociedad y otorgará finiquito recíproco, mientras que su compensación se cobrará a lo largo de tres años. Sin garantía, su único respaldo sería reclamar judicialmente a quien ya tiene la vivienda en su patrimonio. ¿Desean pactar alguna garantía, como una condición resolutoria expresa inscribible sobre la vivienda, un aval, o el vencimiento anticipado de todo lo pendiente si se impaga un plazo?

---

### Veredicto A — Calidad del texto generado

**Tono: correcto.** Usted en todo momento, verbos precisos del registro exigido ("Indíqueme", "Le pido que me confirme", "Debo advertirle expresamente", "Queda constancia"), cero coloquialismos, cero "vale/perfecto/genial". No se detectó ninguna muletilla.

**Explicación previa a la decisión: suficiente en las cuatro cláusulas de negociación.** La presunción del art. 1361 se explica con la consecuencia práctica ("quien sostenga que un bien es suyo debe probarlo, y que la escritura esté a su nombre no basta por sí solo"), no como cita. El reintegro se explica con la distinción que el cliente lego nunca hace ("no le convierte en propietaria de una cuota mayor del bien: le convierte en acreedora"). La vivienda y el exceso, ver veredicto C.

**Directiva de Invisibilidad: cumplida.** Ni un "V1", ni un "ahora voy a", ni una tabla de progreso, ni un preámbulo antes de una pregunta. La única mención de mecánica es la línea de carga, permitida.

**Invenciones: ninguna.** Todos los importes proceden del cliente; la aritmética es derivada. Cuando el cliente pidió implícitamente una cifra actualizada del reintegro, se rechazó estimarla ("Esa actualización no la puedo estimar yo"). No se citó ninguna sentencia. Todas las citas normativas se contrastaron contra el BOE en esta sesión.

**Un reproche al propio texto:** en la sección 4 la explicación previa ocupa cinco párrafos antes de la primera pregunta. Es correcta pero pesada; un cliente real se pierde. La skill no pone límite de extensión a las explicaciones previas.

### Veredicto B — El asset visto desde el LLM que lo rellena

1. **Placeholders: limpios.** 87 únicos en el convenio, ninguno con texto de ayuda dentro de las llaves, ninguno anidado, ningún `[DATO]` de corchete simple, comentarios balanceados. Ninguno resultó ambiguo al rellenarlo.
2. **DEFECTO REAL — el lote no se podía valorar neto de la deuda asumida.** El asset ofrecía una sola línea, `Valor total del lote adjudicado a X: {{valor_lote_conyuge_x}} euros`, y ni la sección 10 ni la 11 del `SKILL.md` decían que un lote se valora restando la deuda que su titular asume. Siguiendo la plantilla al pie de la letra, el lote de CONYUGE B valdría 249.000 euros y el exceso saldría de 164.500 en lugar de 84.500: **una compensación casi el doble de la debida, sobre el escenario más frecuente de la skill.** La reference sí lo sabía (cuadro del apartado 3: "reduce el exceso al descontar del valor del lote la deuda asumida"), pero eso no llega al documento. Corregido.
3. **DEFECTO REAL — el bloque del art. 1403 produce frases con ceros de relleno.** Literalmente escrito, sale: *"CONYUGE B: haber de 84.500 euros, más reintegros a su favor por 0 euros, menos créditos de la sociedad contra él por 0 euros."* Agramatical no es, pero es lenguaje de formulario en un documento que se firma. Corregido.
4. **DEFECTO REAL — el encabezado de la partida B del pasivo afirmaba lo que el documento luego contradecía.** Decía "por su importe actualizado al tiempo de la liquidación conforme al artículo 1358", pero el guardrail 10 permite el importe nominal si se advierte, y la línea siguiente pide el criterio de actualización, que puede ser "ninguno". El documento habría afirmado que 30.000 euros nominales de 2010 son un importe actualizado a 2026. Corregido.
5. **Numeración: sin huecos.** PRIMERA a DÉCIMA correlativas con las dos cláusulas condicionales insertadas en su turno. La técnica de dejar `{{numero_clausula_deudas}}` sin resolver hasta llegar a ella funciona y evita renumerar. **No se reprodujo el fallo de la cita doble de documentos** que el autor de la skill detectó: en la HOJA CONVENIO no hay relación numerada de documentos, de modo que ese riesgo vive sólo en la HOJA JUDICIAL y aquí no se puede verificar.
6. **AMBIGÜEDAD REAL entre el Punto 4 y la sección 9.** El Punto 4 manda omitir en el `Write` los bloques "que dependan de decisiones aún no tomadas"; V3 ya estaba resuelto desde el primer mensaje, así que por la letra del Punto 4 la cláusula de la vivienda debía escribirse ya, pero la sección 9 prohíbe redactarla antes de explicar el efecto frente al banco. Corregido.
7. **Detalle menor no corregido:** el bloque de la sentencia firme es un párrafo "Que la sentencia..." sin ordinal propio, colgando entre SEGUNDO y TERCERO. Se lee como segundo párrafo de SEGUNDO, pero repite la fecha de firmeza que SEGUNDO ya ha dado.
8. **Leído de corrido, el convenio suena a documento real.** La secuencia inventario → avalúo → liquidación → adjudicaciones → excesos es la del Código, las remisiones internas entre cláusulas ("en los términos de la cláusula quinta") encajan, y no se nota la costura salvo en el punto 7.
9. **Observación de repositorio, no defecto de esta skill:** los assets y este `SKILL.md` están escritos sin tildes ("liquidacion", "articulo"). Los textos fijos del `SKILL.md` son texto que el cliente ve; emitidos literalmente producen un chat sin acentos. `derecho-civil-arrendamiento` ya usa tildes en su `SKILL.md` y esta skill no. No corregido por ser transversal al repositorio y no admitir un `Edit` quirúrgico.

### Veredicto C — Los dos puntos críticos

**C1. Vivienda hipotecada: PASA, y es lo mejor de la skill.** La sección 9 obliga a explicar y a confirmar la comprensión antes de escribir nada, y la explicación cubre los cuatro extremos: que el banco no es parte, que ambos siguen obligados solidariamente, que el efecto del convenio es interno con acción de repetición, y que la única liberación real es la novación subjetiva que sólo el banco puede conceder. La cláusula del asset termina en un párrafo en negrita que dice exactamente lo contrario de lo que el cliente esperaba, y la advertencia nº 4 del pie lo repite. **En ningún punto del documento generado se da a entender lo contrario.** El único refuerzo que añadí de mi cosecha fue el efecto sobre el historial de crédito, que la reference menciona y el `SKILL.md` no.

**C2. Reintegro del dinero privativo: PASA en lo sustantivo, con una arista.** La sección 7 obliga a preguntarlo activamente, lo trata como crédito de la masa privativa contra la ganancial (pasivo, partida B), explica que no da cuota sino crédito, exige acreditación documental, y la sección 8 lo cobra antes de dividir conforme al art. 1403, de modo que CONYUGE A percibe 114.500 y no 84.500. Nada se da por perdido. La arista es la del punto 4 del veredicto B: la skill contempla que las partes pacten el importe nominal, pero el asset afirmaba que todo importe de esa partida está actualizado.

### Correcciones aplicadas

En `assets/convenio-liquidacion-gananciales.md`:
- Encabezado de la partida B del pasivo: "por su importe actualizado al tiempo de la liquidación conforme al artículo 1358" → "por el importe que en cada caso se expresa, determinado conforme al artículo 1358", y "criterio de actualizacion aplicado" → "criterio de determinacion aplicado".
- Las dos líneas de valor de lote sustituidas por "Valor total de los bienes adjudicados a X" más dos bloques condicionales alternativos (con deuda asumida / sin deuda asumida) que fijan el valor neto del lote, con los placeholders nuevos `{{valor_bienes_lote_conyuge_a}}`, `{{deuda_asumida_conyuge_a}}` y sus homólogos de B.

En `SKILL.md`:
- Sección 10 (adjudicaciones): regla expresa de que el lote se valora neto de la deuda asumida que grava un bien del lote, con el ejemplo numérico 240.000 − 80.000 = 160.000, obligación de escribir las dos cifras y de cuadrar la suma de los netos con los totales a percibir.
- Sección 11 (exceso): la comparación es entre el valor **neto** del lote y el total a percibir, con prohibición expresa de comparar el valor bruto.
- Sección 8 (liquidación): suprimir los sumandos de importe cero del bloque del art. 1403 en lugar de escribir "0 euros".
- Sección 11 (exceso): si el pago se aplaza, advertir de que la cláusula de finiquito declara liquidada la sociedad y preguntar por la garantía (condición resolutoria inscribible, aval, prenda o vencimiento anticipado), sin inventarla si el cliente no la quiere.
- Punto 4: los bloques de las cláusulas de negociación (vivienda, exceso, reintegros) se omiten en el `Write` inicial **aunque su condición ya esté resuelta por Escucha Activa**, y se insertan tras la explicación.

Comprobado tras las correcciones: los tres assets siguen con 47, 87 y 39 placeholders únicos, cero malformados, cero anidados, cero corchetes simples y comentarios HTML balanceados. El documento generado cierra con cero placeholders sin resolver, cero comentarios HTML y la aritmética cuadrada al céntimo (279.000 − 110.000 = 169.000; 84.500 cada uno; 114.500 y 84.500 a percibir; lotes netos de 30.000 y 169.000; exceso de 84.500 fraccionado en 28.166,68 + 28.166,66 + 28.166,66 = 84.500,00).

**Resultado global: PASA con cuatro defectos corregidos**, uno de ellos material —el exceso de adjudicación calculado sobre el valor bruto del inmueble hipotecado— que habría producido un documento gravemente erróneo en el escenario más habitual de esta skill.
