# Test de ejecucion — skill `derecho-civil-contratos-particulares`

Ejecucion manual del arbol de decision sobre cuatro escenarios (3 principales + 1 contra-caso). Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: Codigo Civil (BOE-A-1889-4763), Ley de 23 de julio de 1908 sobre nulidad de los contratos de prestamos usurarios (BOE-A-1908-5579), LEC arts. 517 y 520 (BOE-A-2000-323) y Ley 31/2022 de PGE, disposicion adicional 42.ª (BOE-A-2022-22128), para el interes legal del dinero.
- Verificacion real efectuada el 03/09/2026 contra la API de legislacion consolidada del BOE (`.../legislacion-consolidada/id/{ID}/texto/bloque/{bloque}`, cabecera `Accept: application/xml`), leyendo la **ultima** `<version>` de cada bloque:
  - Arts. 1088, 1091, 1100, 1101, 1108, 1124, 1154, 1157, 1170, 1196, 1225, 1227, 1255, 1258, 1261, 1273 a 1281, 1289, 1445, 1450, 1461, 1484 a 1486, 1489, 1490, 1500, 1501, 1740 a 1757, 1822, 1830, 1831, 1857, 1863, 1865, 1911, 1962, 1964 y 1973 CC.
  - Art. 1755 CC confirmado literal: "No se deberan intereses sino cuando expresamente se hubiesen pactado."
  - Art. 1964 CC: la version vigente es la de la Ley 42/2015 (**cinco** años para las acciones personales); la version originaria (quince años) es historica y NO debe usarse.
  - Art. 1484 y 1485 CC: version vigente la de la Ley 17/2021 (añade el apartado 2 sobre venta de animales).
  - Ley Azcarate: los metadatos del BOE devuelven `estatus_derogacion = N` y `vigencia_agotada = N` (ultima actualizacion del consolidado 16/12/2025). **Vigente.** Verificados literalmente sus arts. 1, 2, 3, 8 y 9.
  - LEC art. 517.2.4.º en la redaccion de la LO 1/2025 (efectos 03/04/2025) y art. 520 (limite de 300 euros).
- **Interes legal del dinero:** ultima fijacion expresa localizada en el BOE, disposicion adicional 42.ª de la Ley 31/2022 (bloque `da-42`): 3,25 %, literalmente "hasta el 31 de diciembre del año 2023". No consta Ley de Presupuestos aprobada para 2026 (presupuesto prorrogado). **Marcado como pendiente de verificacion manual en cada lanzamiento y NO escrito fijo en ningun asset**: los assets se remiten al "interes legal del dinero vigente en cada momento".

---

## Test 1 — Prestamo de 15.000 euros entre hermanos, sin interes, devolucion en cuotas

**Mensaje inicial:** "Quiero prestarle 15.000 euros a mi hermano. No le voy a cobrar intereses y me los devolvera en cuotas mensuales. Necesito dejarlo por escrito."

### Recorrido del arbol
```
V1  -> escucha activa: "prestarle 15.000 euros"        V1  = entrega con obligacion de devolver (sin pregunta)
V1b -> escucha activa: "15.000 euros"                  V1b = dinero -> prestamo, no comodato (sin pregunta)
V2  -> escucha activa: "no le voy a cobrar intereses"  V2  = sin interes remuneratorio (sin pregunta)
V3  -> no resuelto -> DIFERIDO a la seccion 9 del Punto 5 (negociacion)
V4  -> no resuelto -> DIFERIDO a la seccion 11 del Punto 5 (negociacion)
Validacion: partes particulares; objeto cierto (15.000 euros);
       causa licita; control de usura NO aplica (V2 = sin interes)
HOJA PRESTAMO -> assets/contrato-prestamo-particulares.md
       Clausula TERCERA: Variante A (sin interes, Art. 1755 CC) ACTIVADA
       Clausula CUARTA:  Variante B (cuotas, con tabla) ACTIVADA
```

### Bloques activados y NO activados
- **Activados:** TERCERA Variante A (gratuidad, con cita expresa del Art. 1755 CC); CUARTA Variante B (calendario de cuotas con tabla); QUINTA Variante A del interes de demora (interes legal, Art. 1108 CC), insertada en la seccion 6; forma Variante B (privado con compromiso de elevacion, Art. 1279 CC), insertada en la seccion 11.
- **NO activados:** TERCERA Variante B (interes remuneratorio); CUARTA Variante A (pago unico); QUINTA Variante B (interes de demora pactado); amortizacion anticipada; vencimiento anticipado; fianza (simple y solidaria); prenda; bloque de FIADOR en REUNIDOS y en FIRMAS; forma Variantes A y C; advertencia final de usura; advertencia final de ausencia de fuerza ejecutiva (no aplica: se pacta el compromiso de elevacion).

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija. Los tres vectores que la skill pregunta estan resueltos por escucha activa, y V3 y V4 estan diferidos por diseño, de modo que el Punto 1 no formula ninguna pregunta: la skill pasa a la verificacion normativa (interna) y de ahi a la Confirmacion, todo en el mismo turno.
- Turno 2: Confirmacion visible (Punto 3): texto fijo PRESTAMO con enlace al BOE + el añadido de V2 = sin interes ("conforme al articulo 1.755 del Codigo Civil, no se deberan intereses sino cuando expresamente se hubiesen pactado, de modo que su prestamo sera gratuito") + eleccion plantilla/documento propio.
- Turno 3: creacion del documento (`Write` + `Read`), confirmacion de la ruta absoluta y, **en la misma respuesta**, anuncio de la primera seccion y su primera pregunta. No hay turno de "¿desea empezar?".
- Turnos 4-7: parte prestamista, un dato por turno (nombre, documento, domicilio, telefono y email). Vista previa conjunta y confirmacion agrupada en el turno POSTERIOR a la respuesta del ultimo dato.
- Turnos 8-11: parte prestataria, misma mecanica.
- Turnos 12-14: importe y entrega del capital. La skill recomienda la transferencia frente al efectivo y explica por que (acredita la entrega, que es lo que mas se discute despues).
- Turno 15: intereses remuneratorios (negociacion). La skill **no pregunta el tipo**: V2 ya esta resuelto. Explica el Art. 1755 CC, deja constancia expresa de la gratuidad en el documento (no por omision) y confirma.
- Turnos 16-18: plazo y forma de devolucion (negociacion). Explica antes la diferencia entre vencimiento unico y cuotas. Usuario elige 12 cuotas mensuales de 1.250 euros. La skill construye ella misma la tabla completa del calendario.
- Turno 19: mora e intereses de demora (negociacion). Explica el Art. 1100 (mora automatica pactada) y el Art. 1108 (interes legal a falta de pacto). Usuario elige el interes legal. Se inserta la Variante A.
- Turno 20: amortizacion anticipada (negociacion, condicional) — usuario dice que no. Bloque descartado y clausulas renumeradas.
- Turno 21: vencimiento anticipado (negociacion, condicional) — usuario dice que no. Bloque descartado y renumeracion.
- Turno 22: garantias (negociacion, resuelve V3). La skill explica el fiador, la diferencia entre fianza simple y solidaria (beneficio de excusion, Arts. 1830 y 1831) y la prenda (Arts. 1863 y 1865) **antes** de preguntar. Usuario: ninguna. Bloques descartados y renumeracion.
- Turno 23: gastos e impuestos. Informa de la sujecion y exencion en ITP y AJD y de que la autoliquidacion debe presentarse igualmente.
- Turno 24: forma del contrato (negociacion, resuelve V4). Explicacion comun completa. Usuario elige la opcion 2 (privado con compromiso de elevacion). Se inserta la clausula entera y se renumera.
- Turnos 25-28: notificaciones y cierre.

### Documento generado (extracto relleno, datos sinteticos)
```
CONTRATO DE PRESTAMO ENTRE PARTICULARES — PRESTAMISTA A / PRESTATARIO A
> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico definitivo.
> Version del Codigo Civil verificada en el BOE: 03/09/2026

PRIMERA. El PRESTAMISTA entrega al PRESTATARIO, en concepto de prestamo, la cantidad de 15.000 euros (quince mil euros).

TERCERA — Intereses remuneratorios
El presente prestamo se concede sin devengo de interes remuneratorio alguno. Las partes hacen constar expresamente que, conforme al articulo 1.755 del Codigo Civil, no se deben intereses sino cuando expresamente se hubiesen pactado, y que en este contrato no se pacta ninguno.

QUINTA — Mora e intereses de demora
[...] Desde que se produzca la mora, la cantidad impagada devengara el interes legal del dinero vigente en cada momento, conforme al articulo 1.108 del Codigo Civil.

SEPTIMA — Forma del contrato
Las partes [...] se obligan reciprocamente a elevarlo a escritura publica a requerimiento de cualquiera de ellas, conforme al articulo 1.279 del Codigo Civil.
```
Resultado: **PASA**. La gratuidad se hace constar de forma expresa y no por omision, que es justo lo que el Art. 1755 CC hace juridicamente relevante. **En ninguna parte del documento figura una cifra concreta de interes legal**: la remision es al "vigente en cada momento", de modo que el contrato no caduca al cambiar el ejercicio.

---

## Test 2 — Reconocimiento de deuda de 4.000 euros con expresion de causa y calendario de pago

**Mensaje inicial:** "Un conocido me debe 4.000 euros de unas obras que le hice en su casa el año pasado. No lo tengo por escrito. Quiere pagarme poco a poco y me gustaria dejarlo firmado."

### Recorrido del arbol
```
V1  -> escucha activa: "me debe 4.000 euros [...] no lo
        tengo por escrito [...] dejarlo firmado"        V1 = deuda ya existente que se reconoce (sin pregunta)
V1b -> no aplica (exclusivo de V1 = 1)
V2  -> no aplica (exclusivo de la HOJA PRESTAMO)
V3  -> no resuelto -> DIFERIDO a la seccion 10 del Punto 5
V4  -> no resuelto -> DIFERIDO a la seccion 12 del Punto 5
Validacion: partes particulares. ATENCION: se comprueba
        que quien hizo las obras no actuaba como
        empresario o profesional (si lo hiciera, seria
        una relacion de consumo -> DETENER). Usuario
        confirma que fue un favor entre conocidos.
        Causa licita y real -> PROCEDE.
HOJA RECONOCIMIENTO -> assets/reconocimiento-deuda.md
        Clausula SEGUNDA: Variante A (causa expresada) ACTIVADA
        Clausula CUARTA:  Variante B (cuotas, con tabla) ACTIVADA
```

### Bloques activados y NO activados
- **Activados:** SEGUNDA Variante A (causa expresada); CUARTA Variante B (calendario de cuotas); QUINTA Variante A (interes legal de demora); forma Variante A (documento privado); advertencia final de ausencia de fuerza ejecutiva.
- **NO activados:** SEGUNDA Variante B (sin expresion de causa); tabla de desglose por conceptos (la deuda tiene un solo concepto); CUARTA Variante A (pago unico); QUINTA Variante B (interes pactado); parrafo de interes remuneratorio del aplazamiento; vencimiento anticipado; fianza; compensacion de creditos reciprocos; parrafo de finiquito de la relacion; forma Variantes B y C; bloque de FIADOR en REUNIDOS y en FIRMAS.

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija. V1 resuelto por escucha activa; el Punto 1 no pregunta nada, pero **si ejecuta la validacion de la condicion de particulares**, que en este escenario es la unica que puede desviar el flujo.
- Turno 2: pregunta de validacion, en prosa y con las dos opciones en la misma frase: si quien realizo las obras lo hizo en el ejercicio de una actividad empresarial o profesional, o como un favor entre particulares. Usuario: fue un favor. (Si hubiera respondido lo primero, la skill habria detenido el flujo aplicando el guardrail 6, sin crear documento.)
- Turno 3: Confirmacion visible con el texto fijo RECONOCIMIENTO y enlace al BOE + eleccion plantilla/documento propio.
- Turno 4: creacion del documento, ruta absoluta y, en la misma respuesta, anuncio de la primera seccion y su primera pregunta.
- Turnos 5-12: parte acreedora y parte deudora, un dato por turno, con confirmacion agrupada por parte en el turno posterior al ultimo dato de cada una.
- Turnos 13-15: importe de la deuda. La skill escribe 4.000 euros en cifra y en letra y pregunta si procede de un solo concepto o de varios. Un solo concepto: la tabla de desglose no se activa.
- Turno 16: **causa de la deuda (negociacion — el punto clave de esta hoja)**. La skill explica, antes de preguntar, que el documento no crea la deuda sino que la reconoce; que por el Art. 1277 CC la causa se presume existente y licita aunque no se exprese, de modo que un reconocimiento abstracto es valido y traslada la carga de la prueba al deudor; y que aun asi conviene expresarla, porque si el deudor prueba que no habia causa o que era ilicita, un reconocimiento abstracto cae entero (Arts. 1275 y 1276), mientras que uno con causa veraz expresada resiste. Usuario decide expresarla: obras de reforma realizadas en el domicilio del deudor en {{fecha}}.
- Turno 17: naturaleza declarativa y prescripcion (informativo). La skill informa de que la firma interrumpe la prescripcion (Art. 1973 CC) y de que el plazo de cinco años de las acciones personales (Art. 1964.2 CC) vuelve a contarse desde hoy. Como quien encarga el documento es el **acreedor**, esto le beneficia y se informa sin advertencia adicional.
- Turnos 18-20: forma y plazo de pago (negociacion). Usuario elige 8 cuotas mensuales de 500 euros. La skill construye la tabla.
- Turno 21: mora e intereses (negociacion). Usuario elige el interes legal y **no** pacta interes remuneratorio por el aplazamiento. La skill hace notar que, de haberlo pactado, el conjunto habria vuelto a quedar sujeto al control de usura por el Art. 9 de la Ley Azcarate.
- Turno 22: vencimiento anticipado (condicional) — usuario dice que no. Descartado y renumeracion.
- Turno 23: compensacion de creditos reciprocos (condicional) — no hay deudas en sentido contrario. Descartado sin mas preguntas.
- Turno 24: garantias (resuelve V3) — usuario: ninguna. Descartado y renumeracion.
- Turno 25: efectos del pago integro (negociacion). La skill explica la diferencia entre carta de pago y finiquito de la relacion y advierte al acreedor de que el finiquito le impediria reclamar despues otros conceptos de la misma relacion. Usuario elige solo carta de pago: el parrafo de finiquito no se inserta.
- Turno 26: forma del documento (resuelve V4). Explicacion comun completa. Usuario elige documento privado. Se inserta la Variante A y **se activa la advertencia final** de que el documento no es titulo ejecutivo.
- Turnos 27-30: notificaciones y cierre.

### Documento generado (extracto relleno, datos sinteticos)
```
RECONOCIMIENTO DE DEUDA Y COMPROMISO DE PAGO — ACREEDOR A / DEUDOR A
> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico definitivo.

PRIMERA. El DEUDOR reconoce expresamente adeudar al ACREEDOR la cantidad de 4.000 euros (cuatro mil euros).

SEGUNDA — Causa de la deuda
La deuda reconocida en la clausula anterior trae causa de las obras de reforma realizadas por el ACREEDOR en el domicilio del DEUDOR entre {{fecha_inicio_obras}} y {{fecha_fin_obras}}.
Las partes hacen constar que la causa asi expresada es real y licita, y que el importe reconocido se corresponde exactamente con lo efectivamente debido por dicho concepto [...]

TERCERA — Naturaleza y efectos del reconocimiento
[...] el presente documento no crea una deuda nueva: reconoce y documenta una deuda ya existente [...]
Conforme al articulo 1.973 del Codigo Civil, el presente reconocimiento interrumpe la prescripcion [...]

CUARTA. 8 cuotas mensuales de 500 euros (quinientos euros), con tabla de calendario.

Advertencia 5. Este documento privado no es titulo ejecutivo [...]
```
Resultado: **PASA**. La clausula TERCERA deja escrito, con esas palabras, que el documento **no crea la deuda sino que la reconoce**, que es el punto que el cliente entiende mal con mas frecuencia. La tabla de desglose por conceptos no aparece (un solo concepto), y el parrafo de finiquito tampoco.

---

## Test 3 — Comodato de un local a un familiar, gratuito y con plazo

**Mensaje inicial:** "Tengo un local vacio y voy a dejarselo a mi sobrino dos años para que monte su taller. No le voy a cobrar nada, solo que se haga cargo de la luz y el agua. Quiero un contrato."

### Recorrido del arbol
```
V1  -> escucha activa: "dejarselo [...] dos años"       V1  = entrega con obligacion de devolver (sin pregunta)
V1b -> escucha activa: "un local [...] no le voy a
        cobrar nada"                                    V1b = cosa concreta de uso gratuito -> comodato (sin pregunta)
V2  -> no aplica (exclusivo de la HOJA PRESTAMO)
V3  -> no aplica (exclusivo de PRESTAMO y RECONOCIMIENTO)
V4  -> no resuelto -> DIFERIDO a la seccion 9 del Punto 5
Validacion de gratuidad (Arts. 1740 y 1741 CC): el sobrino
        asume los suministros individualizados (luz, agua),
        que son gastos ordinarios de uso del Art. 1743 CC
        y NO constituyen contraprestacion -> SIGUE SIENDO
        COMODATO. No se deriva a arrendamiento.
HOJA COMODATO -> assets/contrato-comodato.md
        Clausula PRIMERA: bloque de identificacion de INMUEBLE ACTIVADO
        Clausula TERCERA: Variante A (plazo determinado, Art. 1749 CC) ACTIVADA
```

### Bloques activados y NO activados
- **Activados:** bloque de identificacion de inmueble en la clausula PRIMERA (direccion, municipio, codigo postal, referencia catastral, superficie); parrafo de elementos accesorios (llaves); TERCERA Variante A (plazo determinado con la regla del Art. 1749); forma Variante A (documento privado); advertencia final adicional sobre la proximidad al precario en la cesion de inmuebles.
- **NO activados:** bloque de identificacion generica de bien mueble; TERCERA Variantes B y C (sin plazo); parrafo de tasacion del Art. 1745; parrafo de pluralidad de comodatarios del Art. 1748; parrafo de restitucion propio de vehiculos; clausula de seguro; forma Variante B; bloques de representacion de persona juridica.

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija. V1 y V1b resueltos por escucha activa. **La skill ejecuta la validacion de gratuidad sin preguntar**, porque el usuario ya ha precisado que lo unico que asume el cesionario son los suministros: son gastos ordinarios del Art. 1743 CC y no rompen la gratuidad. Pasa a la verificacion normativa y a la Confirmacion.
- Turno 2: Confirmacion visible con el texto fijo COMODATO ("Se trata de un contrato esencialmente gratuito") y enlace al BOE + eleccion plantilla/documento propio.
- Turno 3: creacion del documento, ruta absoluta y, en la misma respuesta, anuncio de la primera seccion y su primera pregunta.
- Turnos 4-11: comodante y comodatario, un dato por turno, con confirmacion agrupada por parte.
- Turnos 12-15: el bien cedido. Al ser inmueble, la skill pide direccion, municipio, codigo postal, referencia catastral y superficie, no marca y numero de serie. Recomienda documentar el estado con fotografias en el anexo y explica por que (poder discutir despues si un deterioro deriva del uso normal o de un uso indebido).
- Turno 16: **gratuidad (negociacion)**. Aunque la validacion interna ya la ha resuelto, la skill la explica igualmente al cliente antes de confirmarla: que el comodato es gratuito por definicion (Art. 1740, parrafo segundo), que si mediara cualquier emolumento por el uso la convencion dejaria de ser comodato y pasaria a regirse como arrendamiento (Art. 1741), y que asumir los gastos ordinarios no es contraprestacion (Art. 1743). Confirma con el cliente que no hay ninguna otra cantidad.
- Turno 17: **destino y duracion (negociacion — el punto clave de esta hoja)**. La skill explica las tres situaciones antes de preguntar: con plazo pactado, el comodante no puede reclamar el local antes de esa fecha salvo urgente necesidad justificada (Art. 1749); sin plazo pero con uso concreto, hasta que concluya ese uso; sin plazo ni uso, a su voluntad en cualquier momento (Art. 1750), con la advertencia de que en un inmueble esa tercera situacion se aproxima al precario. Usuario confirma los dos años y el destino de taller.
- Turno 18: obligaciones y gastos (negociacion). Explica el reparto legal (ordinarios al comodatario, Art. 1743; extraordinarios de conservacion al comodante previo aviso, Art. 1751). Usuario mantiene el reparto legal y prohibe la cesion a terceros.
- Turno 19: tasacion y seguro (condicional) — usuario no quiere ninguna de las dos. Bloques descartados y renumeracion.
- Turnos 20-21: restitucion. Lugar y documento acreditativo de la devolucion. La skill recuerda al hilo que el comodatario no puede retener el local alegando que el comodante le debe algo, ni siquiera por gastos (Art. 1747).
- Turno 22: forma del contrato (resuelve V4). La skill aplica la explicacion comun **omitiendo la parte de fuerza ejecutiva**, porque en un comodato no hay deuda dineraria que ejecutar, y **no recomienda** escritura publica por defecto. Usuario elige documento privado.
- Turnos 23-25: notificaciones y cierre, mas el anexo de estado del bien.

### Documento generado (extracto relleno, datos sinteticos)
```
CONTRATO DE COMODATO (PRESTAMO DE USO GRATUITO) — COMODANTE A / COMODATARIO A
> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico definitivo.

SEGUNDA — Gratuidad
El presente contrato es esencialmente gratuito, conforme al articulo 1.740, parrafo segundo, del Codigo Civil.
[...] si mediara cualquier emolumento a cargo de quien adquiere el uso, la convencion dejaria de ser comodato y quedaria sometida al regimen del arrendamiento.
La obligacion del COMODATARIO de asumir los gastos ordinarios prevista en la clausula CUARTA no constituye contraprestacion y no altera el caracter gratuito de este contrato.

TERCERA — Destino y duracion
El COMODATARIO destinara el bien exclusivamente a taller [...]
El comodato se pacta por un plazo de dos años [...]
Conforme al articulo 1.749 del Codigo Civil, el COMODANTE no podra reclamar el bien antes de dicha fecha, salvo que tuviera urgente necesidad de el [...]
```
Resultado: **PASA**. La gratuidad se afirma con su consecuencia (si hay emolumento deja de ser comodato), y el plazo pactado activa la regla correcta del Art. 1749 en lugar de la del Art. 1750. Las clausulas de tasacion, seguro y pluralidad de comodatarios estan **ausentes por completo** del documento, no vacias ni comentadas.

---

## Contra-caso — Prestamo de 3.000 euros a devolver 6.000 en seis meses

**Mensaje inicial:** "Le voy a prestar 3.000 euros a un conocido que esta muy apurado y me los devuelve en seis meses, pero me tiene que devolver 6.000. Preparame el contrato."

### Recorrido del arbol
```
V1  -> escucha activa: "le voy a prestar 3.000 euros"   V1  = entrega con obligacion de devolver
V1b -> escucha activa: "3.000 euros"                    V1b = dinero -> HOJA PRESTAMO
V2  -> escucha activa: "me tiene que devolver 6.000"    V2  = se pacta interes (implicito en el diferencial)
Validacion de usura (Punto 1, BLOQUEANTE):
       coste real total = 3.000 euros sobre un principal
       de 3.000 euros en 6 meses = 100 % en medio año,
       del orden de un 300 % anualizado.
       Contraste: el interes legal del dinero, ultima
       fijacion expresa verificada, 3,25 %.
       Añadido: "un conocido que esta muy apurado"
       = indicio de la situacion angustiosa del Art. 1
       de la Ley Azcarate.
       -> DESPROPORCION MANIFIESTA -> ADVERTIR ANTES DE REDACTAR
```

### Comportamiento esperado
La skill **no crea el documento** en ese turno. Antes de cualquier pregunta de relleno de datos y antes de la Confirmacion del Punto 3, aplica el guardrail 3 y emite la advertencia, explicando los cuatro puntos:

1. Que la Ley de 23 de julio de 1908 sobre nulidad de los contratos de prestamos usurarios **sigue vigente** (verificado en el BOE en este mismo lanzamiento), y que su articulo 1 declara nulo el prestamo con interes notablemente superior al normal del dinero y manifiestamente desproporcionado, o aceptado por el prestatario a causa de su situacion angustiosa.
2. Que **la consecuencia no es una rebaja del interes**: el articulo 3 obliga al prestatario a entregar **tan solo la suma recibida**, es decir, los 3.000 euros; y si hubiera pagado de mas, el prestamista tendria que devolverle el exceso. El articulo 8 añade la condena en costas al prestamista.
3. Que la referencia mencionada por el cliente ("esta muy apurado") es precisamente uno de los elementos que el articulo 1 valora, y que agrava el riesgo en lugar de justificarlo.
4. Que **no existe un porcentaje legal seguro**: el articulo 2 remite la apreciacion al tribunal caso por caso, de modo que la skill no puede ofrecer un tipo "por debajo del limite" como si lo hubiera.

A continuacion pregunta si, conocida la advertencia, desea mantener el planteamiento o modificar el tipo, y ofrece la escalacion de la matriz. Si el usuario insiste en un tipo que sigue siendo manifiestamente desproporcionado, la skill no presenta el contrato como seguro y deja constancia de la advertencia en las advertencias finales del documento.

**Comprobacion adicional del Art. 1, parrafo 2.º:** la skill verifica ademas que los 3.000 euros que figurarian como prestados se entregan efectivamente. Si el planteamiento fuera entregar menos de lo que consta como prestado (por descuento del interes en la entrega), la skill **detiene el flujo por completo** y no redacta, porque ese supuesto es de nulidad directa por el propio precepto.

**Resultado: PASA.** La deteccion se produce en el **primer turno**, por escucha activa, antes de la Confirmacion y antes de pedir un solo dato de relleno. El usuario recibe la advertencia correcta —nulidad, no rebaja— antes de invertir turnos en un contrato que un tribunal podria anular entero y con costas a su cargo.

---

## Verificacion en vivo (no solo sobre el papel)

Ademas del recorrido simulado de los cuatro escenarios, se ejecuto realmente el Escenario 1 como lo haria el agente operacional, sin instalar el plugin como skill invocable de Claude Code (no esta registrado en este entorno):

1. Se leyeron en vivo, contra la API de legislacion consolidada del BOE, los articulos del Codigo Civil, la Ley Azcarate completa (arts. 1 a 16) y los arts. 517 y 520 LEC listados en el apartado de verificacion normativa, tomando en cada bloque la **ultima** `<version>`. Se confirmo palabra por palabra el contenido de `references/fuentes-plantillas-validadas.md` y de `references/usura-y-limites-del-interes.md`, incluido el literal del art. 3 de la Ley Azcarate.
2. Se localizo el interes legal del dinero en el BOE (Ley 31/2022, bloque `da-42`) y se comprobo que **no consta Ley de Presupuestos aprobada para 2026**, dejandolo registrado como pendiente de verificacion manual en lugar de escribirlo como cifra vigente del ejercicio.
3. Se aplico el Punto 4 de forma real con `Write` en `test-local/output/contrato_prestamo_prestamista_a_prestatario_a.md`, `Read` de verificacion, y tres ciclos de `Edit` incremental (datos de la parte prestamista con confirmacion agrupada; insercion de la variante de interes de demora en la seccion 6; insercion de la clausula de forma y renumeracion tras descartar amortizacion anticipada, vencimiento anticipado y garantias).

Resultado verificado sobre el archivo real, no sobre un extracto manual: **cero comentarios HTML residuales**; los bloques no activados (interes remuneratorio, pago unico, fianza, prenda, FIADOR) ausentes por completo; los `Edit` aplicados a la primera, sin fallos de coincidencia de texto; y la numeracion final de clausulas **consecutiva y sin saltos** (PRIMERA a NOVENA), sin ningun placeholder de ordinal sin resolver. Los placeholders que persisten (datos del prestatario, calendario de cuotas, IBAN, lugar y fecha) son exactamente los que el `SKILL.md` deja para turnos posteriores del Punto 5, no datos inventados ni omitidos por error.

### Dos defectos reales detectados en esta ejecucion, y sus correcciones

1. **Cabecera de clausula sin cuerpo.** Al escribir el documento base en el Punto 4, la clausula "Forma del contrato" quedo como una cabecera suelta (`### {{ordinal_forma}} — Forma del contrato`) seguida directamente de la siguiente clausula, porque **sus tres variantes son condicionales** y todas se omiten hasta que V4 se resuelve en el Punto 5. El cliente que abriera el documento en la GUI entre ambos momentos veria una seccion vacia y la leeria como un error. **Fix aplicado** en el `SKILL.md`, Punto 4: si todo el cuerpo de una clausula es condicional, se omite la clausula **entera, cabecera incluida**, y se inserta completa cuando la decision se toma.

2. **Dato repetido resuelto en un solo sitio.** El nombre de cada parte aparece en **tres** lugares del asset: el titulo del documento, el bloque REUNIDOS y el bloque de FIRMAS. Tras el `Edit` de confirmacion agrupada de la parte prestamista, el nombre quedo resuelto en REUNIDOS pero seguia como `{{nombre_prestamista}}` en el titulo y en la firma. El mismo riesgo afecta al importe (expositivo y clausula PRIMERA) y a la fecha de verificacion (cabecera y advertencias finales). **Fix aplicado** en el `SKILL.md`, Punto 4 (regla "Dato repetido: se rellena en TODAS sus apariciones") y en el guardrail 13, que ahora exige comprobar con `Read` que no queda ninguna aparicion rezagada de un placeholder ya resuelto en otra parte del documento.

Ambos defectos son de mecanica del asset, no de contenido juridico, y ambos habrian llegado al cliente. Verificado tras la correccion: el archivo final no tiene cabeceras vacias ni apariciones rezagadas de `{{nombre_prestamista}}`.

---

## Revision UX

Hallazgos:

1. **Separar V1 de V1b en dos preguntas, en lugar de una unica pregunta de cuatro opciones, es lo que hace correcta la clasificacion.** La frontera entre prestamo y comodato no es intuitiva para el cliente —depende de si lo entregado es fungible o no (Art. 1740 CC)— y comprimirla en una lista de cuatro opciones obligaria al cliente a hacer esa distincion juridica por su cuenta. Preguntando primero "algo que debera devolverse / una deuda que ya existe / una venta" y solo despues "dinero o una cosa concreta", el cliente responde en terminos que entiende y la skill hace la calificacion.

2. **No preguntar V3 y V4 en el Punto 1 es una decision deliberada, no una omision.** La garantia y la forma del documento son decisiones con consecuencias economicas y procesales serias (renuncia al beneficio de excusion; acceso o no a la via ejecutiva). Preguntarlas en frio como vectores de clasificacion produciria una respuesta desinformada. Diferirlas a sus secciones `[negociacion]` del Punto 5, donde se explica el regimen antes de pedir la decision, cuesta cero turnos adicionales —se preguntan igual, solo que mas tarde y con contexto— y mejora sustancialmente la calidad de la decision.

3. **La deteccion de usura ocurre en el primer turno, no al final.** Igual que la caducidad en la skill de ejecucion, la mala noticia llega antes de que el cliente haya invertido tiempo. En el contra-caso, la advertencia se emite por escucha activa del mensaje inicial, sin haber pedido un solo dato de relleno.

4. **La advertencia de usura se formula por su consecuencia, no por su definicion.** Decir "esto podria ser usurario" no cambia la conducta de nadie; decir "el contrato se anula, su hermano le devolveria solo los 3.000 euros que recibio, usted tendria que reintegrar lo cobrado de mas y pagaria las costas" si. El `SKILL.md` fija esa formulacion de forma explicita, precisamente porque el prestamista da por hecho que como mucho le rebajarian el tipo.

5. **En el Test 1 la skill hace constar la gratuidad de forma expresa, en lugar de limitarse a no escribir clausula de intereses.** Juridicamente es lo correcto (el Art. 1755 CC hace que la ausencia de pacto tenga consecuencia), y practicamente evita que el prestatario sospeche despues que "faltaba" una clausula.

6. **En el Test 2 la validacion de la condicion de particulares se ejecuta antes que nada.** Unas obras hechas "a un conocido" son el caso tipico en que el cliente no se da cuenta de que puede estar actuando como profesional. Una unica pregunta, formulada en prosa natural y con las dos opciones en la misma frase, evita generar un documento que se regiria por la normativa de consumo.

7. **En el Test 3 la skill no pregunta por la gratuidad como si dudara, pero la explica igualmente.** La validacion interna ya esta resuelta (los suministros son gastos ordinarios del Art. 1743), asi que la seccion no pide un dato que ya tiene; lo que hace es explicar la regla y su consecuencia, para que el cliente sepa que si mas adelante le cobra algo al sobrino, el contrato deja de ser el que ha firmado.

8. **La explicacion de la forma se adapta a la hoja.** En el comodato se omite el bloque de fuerza ejecutiva, porque no hay deuda dineraria que ejecutar, y no se recomienda notario por defecto. Recitar la misma explicacion en las cuatro hojas habria sido mas simple de escribir y peor para el cliente.

Ajustes aplicados: los dos fixes de mecanica descritos en la verificacion en vivo (cabecera de clausula sin cuerpo, y dato repetido resuelto en todas sus apariciones). Ninguno adicional: el diferimiento de V3 y V4, la deteccion temprana de usura y la explicacion de la forma adaptada por hoja ya estaban recogidos en el `SKILL.md` desde su redaccion.

---

## QA en vivo por agente independiente

Ejecutado el 03/09/2026 por un agente sin contexto previo de la skill. Escenario del cliente, literal:

> "Le voy a prestar 20.000 euros a un amigo para que monte un negocio. Me los devuelve en dos años y hemos hablado de que me pague algo de interes, un 12% anual. Quiere que se lo de este viernes. ¿Con un papel firmado entre los dos vale?"

Datos simulados: PRESTAMISTA A / PRESTATARIO A, NIF 00000000-T. Documento generado en `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/contratos-qa-prueba.md` con `Write`, verificado con `Read` y editado con doce `Edit` incrementales reales.

### Verificacion normativa: ejecutada de verdad, no simulada

La API del BOE del Punto 2 responde y los identificadores de bloque de la skill son correctos:

- `art1755` de BOE-A-1889-4763 devuelve, literalmente, "No se deberán intereses sino cuando expresamente se hubiesen pactado". Coincide con la reference.
- `a1` de BOE-A-1908-5579 devuelve el texto del Art. 1 de la Ley Azcarate, y sus metadatos `estatus_derogacion = N` y `vigencia_agotada = N`. La ley sigue vigente, como afirma la skill.
- `da-42` de BOE-A-2022-22128 confirma el 3,25 % "hasta el 31 de diciembre del año 2023", exactamente como lo describe `references/fuentes-plantillas-validadas.md`.

**Ninguna cifra de interes legal aparece fija en ningun asset.** Los cuatro se remiten al "interes legal del dinero vigente en cada momento". Las unicas cifras del 3,25 % viven en las references y estan correctamente etiquetadas como ultima fijacion expresa de 2023, con la advertencia de que no hay Presupuestos para el ejercicio en curso. Punto C2: **correcto**.

### A) Mi propio texto

**Tono.** Formal y de usted en todos los turnos. Extractos literales:

> "Indique el numero de su DNI, NIE o CIF."

> "Conviene que sepa cual es la consecuencia, porque no es la que se suele suponer: no se trata de que un juez le rebaje el tipo."

> "Le expongo el efecto del tipo que mantiene."

Cero coloquialismos, cero muletillas, cero menciones de vectores, hojas, fases o validaciones. La linea de carga y la introduccion fija se emiten una sola vez y en el mismo turno, sin detenerse a preguntar si desea empezar.

**Explicacion antes de la decision.** La seccion de intereses explica el regimen completo antes de pedir el tipo:

> "Abordamos ahora los intereses del prestamo.
>
> Antes de que decida, conviene que conozca el regimen. Conforme al articulo 1.755 del Codigo Civil, sin pacto expreso no se deben intereses: si no los pacta, el prestamo es gratuito. Si decide pactarlos, la Ley de 23 de julio de 1908 sobre nulidad de los contratos de prestamos usurarios sigue vigente y declara nulo el prestamo cuyo interes sea notablemente superior al normal del dinero y manifiestamente desproporcionado con las circunstancias del caso.
>
> Conviene que sepa cual es la consecuencia, porque no es la que se suele suponer: no se trata de que un juez le rebaje el tipo. El contrato se anula, el prestatario queda obligado a entregar tan solo la suma recibida, usted habria de reintegrarle todo lo que hubiera percibido por encima de ese capital y la sentencia lleva condena en costas (articulos 1, 3 y 8 de esa ley).
>
> No existe ningun porcentaje que la ley declare seguro: los Tribunales resuelven caso por caso.
>
> Indiqueme, con esto presente, si mantiene el 12 por ciento anual que me ha señalado o prefiere otro tipo."

Lo mismo en garantias (fianza simple frente a solidaria, con el beneficio de excusion explicado) y en la forma del documento. **Nada inventado**: ni una sentencia, ni un umbral porcentual, ni un coste notarial cifrado.

**Defecto A1 — la pregunta directa del cliente se quedaba sin respuesta.** El cliente pregunta literalmente "¿con un papel firmado entre los dos vale?" en su primer mensaje. Siguiendo el `SKILL.md` tal como estaba, esa pregunta no se responde hasta la seccion 11 del Punto 5, una docena de turnos despues: la Directiva de invisibilidad prohibe todo lo que no sea la pregunta exacta del turno, y no habia excepcion para responder al cliente. Un cliente que pregunta a su abogado y no obtiene nada durante doce turnos es un defecto de servicio, no una virtud de disciplina. **Corregido**: nueva regla `PREGUNTA DIRECTA DEL CLIENTE: SE RESPONDE` en el Punto 0, que obliga a contestar breve en el primer turno con fundamento, remitiendo a su seccion, sin sustituir la explicacion completa del Punto 5 y sin contar como preambulo prohibido.

**Friccion menor, no corregida.** La introduccion fija dice "Para determinar el documento adecuado, es necesario precisar antes algunos datos" y, en este escenario, la escucha activa ya ha resuelto V1, V1b y V2, de modo que el turno siguiente no precisa ningun dato: informa directamente del tipo de contrato. No es incoherente (el turno termina en una pregunta), pero la frase promete mas de lo que ocurre. Se deja como esta: reescribirla obligaria a dos variantes de introduccion y el coste supera al beneficio.

### B) El asset

**Defecto B1 — bloque condicional que produce una frase contradictoria (corregido).** La clausula SEGUNDA tenia el IBAN cosido al parrafo fijo:

> "La entrega del capital se realiza mediante {{medio_entrega_capital}}, con fecha {{fecha_entrega_capital}}, a la cuenta con IBAN {{iban_prestatario}} de la que es titular el PRESTATARIO."

Con entrega en efectivo —variante que el propio asset contempla— el documento decia "se realiza mediante entrega en efectivo... a la cuenta con IBAN", y a continuacion el parrafo de efectivo. Contradiccion directa. **Corregido**: el parrafo fijo termina en la fecha y el detalle bancario pasa a bloque condicional propio ("Si la entrega se realiza por transferencia o ingreso bancario, insertar como parrafo propio: El importe se abona en la cuenta con IBAN {{iban_prestatario}}...").

**Defecto B2 — frase forzada por bloque condicional (corregido).** La Variante B de la clausula TERCERA fijaba "Los intereses se liquidaran y abonaran {{periodicidad_liquidacion_intereses}}, **junto con la amortizacion del capital prevista en la clausula CUARTA**". Con devolucion en pago unico —que es justo este escenario— no hay amortizacion periodica de capital a la que acompañar: la frase remite a algo que la clausula CUARTA no contiene. **Corregido** a "conforme al calendario de devolucion previsto en la clausula CUARTA", que es veraz en las dos variantes de la CUARTA.

**Defecto B3 — hueco de numeracion, la zona señalada (corregido).** El agente anterior detecto la cabecera sin cuerpo de "Forma del contrato" y el `SKILL.md` la resolvio omitiendo la clausula entera. Esa regla, aplicada literalmente, tiene un segundo efecto que no estaba cubierto: `### TERCERA — Intereses remuneratorios` tambien tiene el cuerpo integramente condicional, pero su ordinal es **fijo**. Al omitirla en el `Write`, el documento que el cliente ve en la GUI entre turnos va PRIMERA, SEGUNDA, **CUARTA**. Lo reproduje: mi documento base tenia ese salto. Identica patologia en `### SEGUNDA — Causa de la deuda` de la HOJA RECONOCIMIENTO, y ahi es peor, porque la causa se decide en la seccion 4 del Punto 5 y el hueco dura casi todo el flujo.

**Corregido en dos frentes.** En los assets, la cabecera pasa a estar **dentro** de cada variante, de modo que "insertala completa" sea copia literal y no reconstruccion de memoria. En el `SKILL.md`, regla nueva `Clausulas de ordinal fijo: ni huecas ni saltadas`: si la variante ya esta determinada por un vector resuelto en el Punto 1 (V2 para TERCERA, la causa para SEGUNDA), la clausula **se escribe ya en el `Write`** con sus placeholders desnudos; solo se difiere si el control de usura lo impone; y las clausulas de ordinal fijo posteriores **no se renumeran** nunca.

**Defecto B4 — placeholder desnudo que sobrevive al documento final (corregido).** El bloque `## CLAUSULAS ADICIONALES` con `{{clausulas_adicionales_solicitadas_por_el_usuario}}` no estaba marcado como condicional en ninguno de los cuatro assets. Si el cliente no pide clausulas adicionales —lo normal—, el contrato firmado sale con una cabecera y un placeholder crudo debajo. Era el unico `{{...}}` sin resolver en mi documento terminado, y contradice el guardrail 13. **Corregido en los cuatro assets** envolviendolo en bloque condicional, separador incluido. **Nota para el equipo:** el mismo patron existe en `derecho-civil-arrendamiento` (4 assets) y `derecho-civil-compraventa-inmueble` (2 assets); no los toco porque exceden mi encargo, pero conviene propagarlo.

**Observacion menor.** `references/usura-y-limites-del-interes.md` prescribe el placeholder `{{tipo_interes_legal_vigente}}`, que no existe en ningun asset. Es instruccion muerta, no defecto: los assets usan la formula "vigente en cada momento", que es la solucion correcta. No se toca.

**Lectura de corrido.** Con B1 a B4 aplicados, el contrato resultante suena a contrato real: nueve clausulas correlativas sin saltos, sin placeholders, sin comentarios HTML, importes en cifra y letra, remisiones internas correctas y advertencias finales coherentes con lo pactado.

### C) Los tres puntos criticos

**C1 — Usura: correcto, con un agujero que he tapado.** La skill explica que la consecuencia es la **nulidad del prestamo** y no una rebaja del tipo, lo dice con esas palabras, cita los arts. 1, 3 y 8, prohibe expresamente afirmar umbrales numericos y deja constancia de la advertencia en la advertencia 5 del documento. Nada de eso da el 12 % por bueno.

Pero el guardrail solo se activaba "si la desproporcion es manifiesta". Un 12 % anual sobre 20.000 euros a dos años no lo es, y por tanto, tras recibir el tipo, la skill no obligaba a decir **nada**: se pasaba a la siguiente seccion. Ese silencio, despues de una explicacion larga sobre la usura, el cliente lo lee como aprobacion. **Corregido**: la seccion 4 incorpora ahora la franja intermedia, con prohibicion expresa de las formulas de validacion. Mi turno post-fix:

> "Le expongo el efecto del tipo que mantiene. Sobre 20.000 euros a dos años, el interes asciende a 4.800 euros, de modo que su amigo le devolveria 24.800 euros en total.
>
> Ese 12 por ciento anual esta claramente por encima del interes normal del dinero. Eso no lo convierte por si solo en usurario: la ley no fija ningun umbral y la desproporcion se aprecia caso por caso atendiendo a las circunstancias de la operacion (articulo 2 de la Ley de 23 de julio de 1908). Por esa misma razon tampoco puedo garantizarle que un tribunal lo respalde. Es una decision suya, y queda advertida en el documento."

**C2 — Interes legal: correcto.** Ver la verificacion normativa mas arriba. Ninguna cifra fija en ningun asset; el contrato generado dice "el interes legal del dinero vigente en cada momento".

**C3 — Documento privado frente a escritura publica: correcto.** La explicacion distingue las tres cosas que aporta la escritura sin mezclarlas, y recomienda por el importe. Extracto literal:

> "El documento privado es plenamente valido y les obliga a ambos: no hace falta notario para que el contrato exista (articulos 1.278 y 1.225 del Codigo Civil). Lo que le falta son dos cosas. La primera, fecha cierta frente a terceros: un tercero puede negar que se firmara el dia que dice, salvo en los tres supuestos del articulo 1.227. La segunda, y mas importante para usted, fuerza ejecutiva: si su amigo no le devuelve los 20.000 euros, con el documento privado tendria que ganar antes un pleito declarativo para obtener un titulo con el que embargar. La copia de la escritura publica matriz expedida con caracter ejecutivo si es titulo ejecutivo (articulo 517.2.4.º de la Ley 1/2000, de Enjuiciamiento Civil) y permite acudir directamente a la ejecucion, siempre que la cantidad exceda de 300 euros (articulo 520).
>
> Por el importe, 20.000 euros, y por el plazo de dos años, le recomiendo la escritura publica o, cuando menos, el compromiso de elevacion. Conviene que sepa lo que la escritura no arregla: no convalida un contrato nulo, no crea solvencia donde no la hay y hay que pedir expresamente en la notaria la copia con caracter ejecutivo."

El coste notarial se menciona sin cifrar, como manda la reference. Se acata la eleccion del cliente (opcion 2) y el contrato queda con la clausula de elevacion del Art. 1279 CC.

### Correcciones aplicadas

| # | Donde | Que |
|---|---|---|
| A1 | `SKILL.md`, Punto 0 | Regla nueva: la pregunta juridica directa del cliente se responde en el primer turno con fundamento, no se difiere en silencio hasta su seccion |
| B1 | `assets/contrato-prestamo-particulares.md` | IBAN sacado del parrafo fijo de la clausula SEGUNDA a bloque condicional propio: con entrega en efectivo producia una frase contradictoria |
| B2 | `assets/contrato-prestamo-particulares.md` | Variante B de TERCERA: "junto con la amortizacion del capital" pasa a "conforme al calendario de devolucion", veraz con pago unico y con cuotas |
| B3 | `SKILL.md` Punto 4 + `contrato-prestamo-particulares.md` + `reconocimiento-deuda.md` | Clausulas de ordinal fijo con cuerpo integramente condicional: se escriben en el `Write` si su variante ya esta determinada, cabecera incluida dentro de cada variante, sin renumerar las posteriores |
| B4 | los cuatro assets | `## CLAUSULAS ADICIONALES` convertido en bloque condicional: evitaba que un placeholder crudo llegara al contrato firmado |
| C1 | `SKILL.md`, Punto 5 seccion 4 | Franja intermedia de usura: obligacion de pronunciarse cuando el tipo supera el interes normal sin ser manifiestamente desproporcionado, con prohibicion expresa de validarlo |

Veredicto: skill solida en lo juridico —el tratamiento de la usura, del interes legal y de la forma del documento resiste el escenario— y con la mecanica de bloques condicionales como punto debil, que era donde estaban los cuatro defectos reales.
