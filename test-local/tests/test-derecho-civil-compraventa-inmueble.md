# Test de ejecucion — skill `derecho-civil-compraventa-inmueble`

Ejecucion manual del arbol de decision sobre cuatro escenarios (3 principales + 1 contra-caso). Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: Codigo Civil (BOE-A-1889-4763), LAU (BOE-A-1994-26003), LOE (BOE-A-1999-21567), ITPAJD (BOE-A-1993-25359), TRLRHL (BOE-A-2004-4214) y LGT (BOE-A-2003-23186).
- **Verificacion real efectuada el 02/09/2026** contra la API de legislacion consolidada del BOE (`.../legislacion-consolidada/id/{ID}/texto/bloque/{bloque}`, cabecera `Accept: application/xml`), leyendo la **ultima** `<version>` de cada bloque:
  - **CC art. 1454**: literal integro confirmado, redaccion originaria de 1889, una sola version. Solo contempla el desistimiento (perder las arras o devolverlas duplicadas). **No clasifica las arras**: la triple calificacion es jurisprudencial. Punto de mayor riesgo de la skill, registrado como tal.
  - CC arts. 1445, 1450, 1455, 1461, 1462, 1465, 1468, 1469, 1474, 1475, 1483, 1489, 1490, 1500, 1502, 1503, **1504**, 1124, 1152, 1255, 1279, 1518, 1875, 1973: verificados, redaccion originaria de 1889 vigente.
  - CC arts. 1484 y 1485: verificados, modificados por la Ley 17/2021 (numeracion y apartado de animales).
  - CC art. 1280: verificados sus dos versiones; la vigente es la de la Ley 11/1981 (que solo altero el apartado 3). El numero 1.º (derechos reales sobre inmuebles en documento publico) es el aplicable aqui.
  - CC art. 1964.2: verificado, redaccion de la Ley 42/2015 (cinco anos).
  - **LAU art. 25**: cinco versiones en el bloque; la vigente es la del Real Decreto-ley 7/2019 (06/03/2019). Verificados los ocho apartados, incluidos los plazos de 30 dias naturales de tanteo y de retracto, la caducidad de 180 dias de los efectos de la notificacion, la no inscribibilidad del 25.5 y la renuncia del 25.8 con su comunicacion de 30 dias.
  - **LAU art. 31**: verificado, redaccion originaria: aplica el art. 25 a los arrendamientos para uso distinto de vivienda. Hallazgo relevante que no estaba en el encargo: **el riesgo de retracto tambien existe si lo arrendado es un local**.
  - **LOE art. 17**: verificado, redaccion originaria: plazos de 10, 3 y 1 ano desde la recepcion de la obra sin reservas o desde la subsanacion; el apartado 9 aclara que no desplaza a los arts. 1484 y siguientes CC.
  - LOE arts. 19 y 20 y **disposicion adicional primera**: verificados; el art. 19 y la DA 1.ª en la redaccion de la Ley 20/2015 (vigencia 01/01/2016). La DA 1.ª exige aval solidario o seguro de caucion individualizado **desde la licencia de edificacion** y cuenta especial separada para las entregas a cuenta. Nota operativa: el bloque de la disposicion responde a `daprimera`; `da1` devuelve 404.
  - ITPAJD art. 8.a): verificado, redaccion originaria. El adquirente es contribuyente "cualesquiera que sean las estipulaciones establecidas por las partes en contrario".
  - TRLRHL art. 106: verificado, redaccion de la Ley 18/2014. En transmision onerosa el sujeto pasivo del IIVTNU es **quien transmite**; el 106.2 solo desplaza al adquirente como sustituto si el contribuyente es persona fisica no residente.
  - **LGT art. 17**: verificado, redaccion del Real Decreto-ley 20/2011. Correccion respecto del encargo: la regla de inalterabilidad de la obligacion tributaria por pacto entre particulares esta hoy en el **apartado 5**, no en el 4 (el antiguo 17.4 se renumero).
- **Modelo oficial: verificado que NO existe.** Consultados el 02/09/2026 el Consejo General del Notariado (publica guias informativas al ciudadano, no modelos de contrato), el Colegio de Registradores (material informativo sobre inscripcion, nota simple y una `Guia de Cargas`, sin modelo de contrato; confirma que el documento privado no sirve para inscribir ni para obtener hipoteca) y los modelos normalizados del CGPJ (solo formularios procesales). Los assets se construyen sobre el contenido legalmente exigido, registrado articulo por articulo en `references/fuentes-plantillas-validadas.md`.
- Pendientes de verificacion manual, registrados en la reference: clasificacion jurisprudencial de las arras, derecho civil foral (especialmente el Llibre sise del Codi civil de Catalunya), tipo autonomico del ITP, cuota del IIVTNU tras la STC 182/2021 y el RDL 26/2021, licencia de primera ocupacion y certificado energetico (norma autonomica), y tanteo/retracto administrativo autonomico.

---

## Test 1 — Arras penitenciales con condicion suspensiva de hipoteca, cliente comprador

**Mensaje inicial:** "Quiero comprar un piso por 200.000 euros y el vendedor me pide firmar unas arras de 12.000. Todavia no tengo la hipoteca concedida y me da miedo perder el dinero si el banco me la deniega. Estoy del lado del comprador."

### Recorrido del arbol
```
V1 -> escucha activa: "el vendedor me pide firmar
       unas arras"                                     V1 = contrato de arras (sin pregunta)
V2 -> escucha activa: "estoy del lado del comprador"   V2 = comprador (sin pregunta)
V4 -> PREGUNTA: situacion del inmueble -> 1            V4 = libre de arrendatarios y ocupantes
V3 -> escucha activa: "todavia no tengo la hipoteca
       concedida"                                      V3 = depende de financiacion (sin pregunta)
Validacion: cliente comprador, inmueble vivienda,
       parada de tanteo/retracto NO aplica (libre);
       cargas -> el cliente dispone de nota simple de
       28/08/2026 que refleja hipoteca del vendedor;
       clase de arras -> BLOQUEANTE, se resuelve en la
       seccion 6
HOJA ARRAS -> assets/contrato-arras.md
```
Sub-pregunta de V4 no aplica (solo si V4 = 2).

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija + V4 (unico vector no resuelto por escucha activa).
- Turno 2: Confirmacion visible (Punto 3): texto fijo ARRAS, que **ya advierte en el primer contacto** de que el art. 1454 solo contempla el desistimiento y de que la triple calificacion es jurisprudencial, con enlace al BOE + eleccion plantilla/documento propio.
- Turnos 3-8: parte vendedora (nombre, NIF, domicilio, estado civil y regimen, titulo de adquisicion), un dato por turno; vista previa unica y confirmacion agrupada en el turno siguiente al ultimo dato. Al declarar el vendedor regimen de gananciales y ser vivienda habitual, la skill activa el bloque de comparecencia del conyuge sin que el cliente lo pida.
- Turnos 9-12: parte compradora (confirmacion agrupada).
- Turnos 13-17: el inmueble (direccion, superficie y descripcion, referencia catastral, datos registrales, anejos).
- Turnos 18-20: precio y forma de pago (negociacion) — la skill explica cifra/letra y el desglose por medios de pago antes de pedir cifras.
- Turno 21: importe de las arras (negociacion) — explica la horquilla habitual del 5-10 % y que 12.000 sobre 200.000 es el 6 %, dentro de lo usual.
- Turno 22: **clase de arras (negociacion, seccion critica)** — la skill explica los tres puntos en orden: (a) que el art. 1454 solo contempla el desistimiento y que la clasificacion es jurisprudencial; (b) que ocurre con cada clase; (c) que el silencio se presume confirmatorio. Al ser el cliente comprador con hipoteca pendiente, le advierte de que las penitenciales le hacen **perder** los 12.000 si desiste, y que para recuperarlos necesita ademas la condicion suspensiva. Cliente elige penitenciales.
- Turnos 23-25: plazo y notaria para la escritura (30/11/2026, notario elegido por el comprador, 10 dias de antelacion).
- Turnos 26-27: cargas (negociacion) — nota simple aportada; hipoteca de 40.000 con ENTIDAD FINANCIERA A; se pacta cancelacion con retencion del precio, no subrogacion.
- Turno 28: estado posesorio — libre; ocupado por el vendedor, que desalojara antes de la escritura.
- Turnos 29-32: **financiacion (negociacion, V3 = 2)** — los cuatro elementos en turnos separados: importe minimo 160.000 y fecha limite 15/10/2026; devolucion integra de las arras (por defecto, aceptado); acreditacion mediante denegacion escrita de al menos 2 entidades solicitadas en 10 dias y comunicada en 5; prorroga por escrito si vence sin respuesta.
- Turno 33: impuestos y gastos (negociacion) — se mantiene el reparto legal; la skill advierte igualmente de que un pacto en contra no vincularia a la Administracion.
- Turno 34: notificaciones.
- Turno 35: lugar, fecha y ejemplares.
- Bucle final: la skill elimina el apartado "CLAUSULAS ADICIONALES" al no haberse pedido ninguna, y verifica cero comentarios HTML y cero placeholders.

### Documento generado (extracto relleno, datos sinteticos)
```
CONTRATO DE ARRAS O SENAL SOBRE BIEN INMUEBLE — VENDEDOR A / COMPRADOR A
> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico definitivo.
> Version del Codigo Civil y de la LAU verificada en el BOE: 02/09/2026

CUARTA — Clase de arras y consecuencias
Las arras entregadas conforme a la clausula tercera tienen el caracter de arras penitenciales [...]
Las arras se entregan como precio de la facultad de desistir, en los terminos del articulo 1.454 del Codigo Civil.
Cualquiera de las partes podra desistir licitamente [...]: si desiste el COMPRADOR, perdera la cantidad entregada;
si desiste el VENDEDOR, devolvera al COMPRADOR la cantidad recibida duplicada, esto es, 24.000 euros.

OCTAVA — Financiacion de la compraventa
[...] condicion suspensiva de que el COMPRADOR obtenga [...] un importe minimo de 160.000 euros, a mas tardar el
15 de octubre de 2026 [...] presentando la solicitud en al menos 2 entidades [...] acompanando la denegacion
escrita [...] el VENDEDOR devolvera al COMPRADOR las arras entregadas en los siguientes terminos: devolucion
integra de los 12.000 euros en el plazo de siete dias.
```
Resultado: **PASA**. Ningun bloque de las otras ramas aparece en el documento: no hay texto de arras confirmatorias ni penales, no hay clausula de arrendatario ni de renuncia al retracto, no hay bloque de obra nueva ni de IVA/AJD, y no hay bloque de subrogacion en el prestamo (se pacto cancelacion). Numeracion de clausulas correcta y sin huecos: PRIMERA a DECIMOSEGUNDA.

---

## Test 2 — Contrato privado de compraventa de vivienda libre de cargas, cliente vendedor

**Mensaje inicial:** "Vendo mi vivienda, libre de cargas y sin hipoteca, por 180.000 euros. El comprador ya tiene el dinero. Quiero el contrato de compraventa antes de ir al notario. Yo soy el vendedor."

### Recorrido del arbol
```
V1 -> escucha activa: "quiero el contrato de
       compraventa antes de ir al notario"             V1 = contrato privado de compraventa
V2 -> escucha activa: "yo soy el vendedor"             V2 = vendedor
V4 -> PREGUNTA: situacion del inmueble -> 1            V4 = libre de arrendatarios y ocupantes
V3 -> escucha activa: "el comprador ya tiene el
       dinero"                                         V3 = no depende de financiacion
Validacion: parada de tanteo/retracto NO aplica;
       cargas -> el cliente afirma "libre de cargas"
       pero NO tiene nota simple -> se aplica el
       guardrail 4: se redacta como manifestacion del
       vendedor y se recomienda la comprobacion
HOJA COMPRAVENTA -> assets/contrato-compraventa-vivienda.md
       (Bloque A de financiacion; bloques de arrendamiento,
        obra nueva, IVA/AJD y subrogacion DESACTIVADOS)
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija + V4.
- Turno 2: Confirmacion visible con texto fijo COMPRAVENTA, que advierte desde el primer contacto de que el contrato privado **no transmite la propiedad frente a terceros ni permite inscribir** (art. 1280.1.º CC) + eleccion plantilla/documento propio.
- Turnos 3-9: parte vendedora, con el sub-apartado de consentimiento del conyuge (el cliente declara estar soltero: el bloque de comparecencia del conyuge se omite).
- Turnos 10-14: parte compradora, con la proporcion de adquisicion (adquiere una sola persona: no se activa el bloque de cocompradores).
- Turnos 15-20: el inmueble, incluida superficie util, linderos y venta como cuerpo cierto. La skill pregunta expresamente si la venta se hace con expresion de cabida y precio por unidad de medida; el cliente dice que como cuerpo cierto, y la skill **no** introduce el regimen del art. 1469 CC.
- Turno 21: precio (negociacion) — 180.000 euros, con la manifestacion de que es el realmente convenido.
- Turnos 22-25: forma de pago (negociacion) — 5.000 entregados como senal el 20/08/2026, 15.000 a la firma, 160.000 al otorgamiento; medios de pago y cuenta de cada partida; recordatorio de conservar justificantes.
- Turnos 26-27: **cargas (negociacion)** — el cliente insiste en "libre de cargas" sin nota simple. La skill **no lo escribe como hecho**: lo redacta como manifestacion del vendedor, con la consecuencia pactada si resulta inexacta, y anade la obligacion de aportar antes del otorgamiento la certificacion de la comunidad y el ultimo recibo del IBI. Advierte de que las cargas o servidumbres no aparentes no mencionadas dan al comprador solo un ano desde la escritura (art. 1483 CC).
- Turno 28: estado posesorio — libre.
- Turnos 29-31: otorgamiento de la escritura (fecha limite, notario, antelacion), con la mencion del art. 1279 CC.
- Turno 32: entrega de la posesion (negociacion) — se entrega en el otorgamiento; la skill explica el art. 1462 y **no** activa el bloque de precario.
- Turno 33: financiacion — al ser V3 = 1, la skill **no formula las preguntas de la seccion** y activa solo el Bloque A (no hay condicion suspensiva).
- Turno 34: impuestos y gastos (negociacion) — reparto legal; al ser el cliente el vendedor, la skill le concreta que la plusvalia municipal es suya (art. 106.1.b) TRLRHL) y que no puede desplazarla por pacto frente al ayuntamiento (art. 17.5 LGT).
- Turnos 35-36: **estado de la vivienda y saneamiento (negociacion)** — al ser el cliente el vendedor, la skill le recomienda declarar los defectos que conoce, porque ocultarlos sabiendolos abre la indemnizacion de danos del art. 1486; el cliente declara una humedad en el bano, que se recoge en el bloque de defectos conocidos. Se informa del plazo de seis meses del art. 1490 y se pregunta por la modulacion de la eviccion (art. 1475): no se pacta ninguna.
- Turno 37: obra nueva — SE OMITE (vivienda de segunda mano).
- Turno 38: documentacion que aportara el vendedor.
- Turno 39: incumplimiento y remedios (negociacion) — la skill explica el art. 1124 y, al ser el cliente el vendedor, le advierte de que **un burofax no cierra el plazo de pago del comprador** (art. 1504 CC). Se pacta clausula penal de 10.000 euros y se pregunta expresamente si sustituye o se acumula: el cliente elige que se acumule, y se redacta asi (a falta de pacto, sustituiria, art. 1152).
- Turnos 40-41: notificaciones, lugar, fecha y ejemplares.

### Documento generado (extracto relleno)
```
CONTRATO PRIVADO DE COMPRAVENTA DE VIVIENDA — VENDEDOR B / COMPRADOR B

CUARTA — Cargas, gravamenes y deudas
El VENDEDOR manifiesta que la vivienda se encuentra libre de cargas y gravamenes segun su propia
manifestacion, no habiendose aportado nota simple registral a la fecha de este contrato [...]
Si con posterioridad a la firma resultasen cargas [...] no manifestadas en este contrato, el COMPRADOR podra
optar entre exigir su cancelacion o pago a costa del VENDEDOR [...] o resolver el presente contrato [...]

DECIMA — Estado de la vivienda y saneamiento
El VENDEDOR pone en conocimiento del COMPRADOR los siguientes defectos, que este declara conocer y aceptar:
humedad en el bano principal, de origen conocido y no reparada.

DUODECIMA — Incumplimiento y resolucion
[...] el COMPRADOR podra pagar el precio aun despues de expirado el plazo pactado, en tanto no haya sido
requerido judicialmente o por acta notarial, conforme al articulo 1.504 del Codigo Civil [...]
Las partes pactan como pena convencional [...] 10.000 euros [...] Dicha pena se acumulara a la indemnizacion
de danos y perjuicios [...] a los efectos del articulo 1.152 del Codigo Civil.
```
Resultado: **PASA**. Ninguna fuga: no aparece el bloque de condicion suspensiva de financiacion, ni el de arrendamiento, ni el de obra nueva y garantias de la Ley 38/1999, ni el de IVA y AJD, ni el de subrogacion hipotecaria, ni el de ocupacion en precario, ni el regimen del art. 1469 CC. La afirmacion "libre de cargas" **no** se escribio como hecho verificado.

---

## Test 3 — Requerimiento al comprador que no acude a la notaria (art. 1504 CC)

**Mensaje inicial:** "Firme la venta de mi piso hace dos meses y el comprador no aparecio en la notaria el dia pactado ni ha pagado los 150.000 euros que quedaban. Quiero requerirle formalmente. Soy el vendedor."

### Recorrido del arbol
```
V1 -> escucha activa: "quiero requerirle formalmente"
       sobre un contrato ya firmado                    V1 = requerimiento de cumplimiento
V2 -> escucha activa: "soy el vendedor"                V2 = vendedor
V4 -> PREGUNTA: situacion del inmueble -> 1            V4 = libre (solo informativo en esta hoja)
V3 -> NO se pregunta (no aplica a la hoja de requerimiento)
Validacion: prescripcion art. 1964.2 -> el vencimiento
       fue hace 2 meses, muy dentro de los 5 anos ->
       PROCEDE. No se reclaman vicios ocultos: el plazo
       de 6 meses del art. 1490 no aplica.
       Via del requerimiento -> BLOQUEANTE: el requirente
       es vendedor y busca resolver por impago, luego
       ACTA NOTARIAL o requerimiento judicial (art. 1504)
HOJA REQUERIMIENTO -> assets/requerimiento-cumplimiento.md
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija + V4.
- Turno 2: Confirmacion visible con texto fijo REQUERIMIENTO, que ya menciona el art. 1124 y la ventana del art. 1504 + eleccion plantilla/documento propio.
- Turnos 3-6: parte requirente (confirmacion agrupada). La skill **no pregunta su condicion en el contrato**: V2 ya la resolvio.
- Turnos 7-9: parte requerida (confirmacion agrupada).
- Turnos 10-12: el contrato y el inmueble (tipo y fecha del contrato, direccion y datos registrales, precio total).
- Turnos 13-16: la obligacion incumplida (otorgamiento de escritura y pago del resto del precio con vencimiento el 15/07/2026; descripcion del incumplimiento; 150.000 euros pendientes; convocatoria previa de 30/06/2026 por burofax, a la que no comparecio).
- Turno 17: **via del requerimiento (negociacion, seccion critica)** — la skill explica la diferencia con precision: el burofax constituye en mora, fija fecha e interrumpe la prescripcion (art. 1973), pero **el art. 1504 exige requerimiento judicial o por acta notarial para cerrar la facultad del comprador de pagar tardiamente**. Al ser V2 = vendedor con impago del precio, **recomienda expresamente el acta notarial**. El cliente acepta: se activa el bloque de intervencion notarial y el bloque de constancia del art. 1504.
- Turnos 18-20: conducta exigida y plazo (otorgamiento de escritura y pago simultaneo, plazo de 10 dias, notaria, dia y hora, documentacion a aportar).
- Turno 21: opcion del art. 1124 (negociacion) — el cliente quiere desvincularse: elige la **resolucion** con reclamacion de danos. La skill confirma que entiende que, hecho el requerimiento notarial, el comprador ya no podra pagar para evitarla y el Juez no podra concederle nuevo termino.
- Turno 22: clausula penal o arras (negociacion, condicional) — el contrato preveia arras confirmatorias de 9.000 euros; la skill advierte de que a falta de pacto la pena **sustituye** a la indemnizacion de danos (art. 1152) y que reclamarla puede cerrar la via del dano real si este es mayor. El cliente decide reclamar el dano real y no la pena: el bloque **no** se inserta.
- Turno 23: suspension del pago — SE OMITE (exclusiva de V2 = comprador).
- Turno 24: lugar y fecha, con recordatorio de su relevancia para la mora y la interrupcion de la prescripcion.

### Documento generado (extracto relleno)
```
REQUERIMIENTO DE CUMPLIMIENTO DE CONTRATO DE COMPRAVENTA DE INMUEBLE — VENDEDOR C a COMPRADOR C

Se requiere la intervencion del Notario NOTARIO C para la practica del presente requerimiento mediante acta
notarial, a los efectos del articulo 1.504 del Codigo Civil.

ANTECEDENTES
IV. Con fecha 30 de junio de 2026 esta parte convoco al destinatario, mediante burofax, al otorgamiento de la
escritura publica de compraventa [...] sin que compareciese ni justificase su ausencia.
VI. A la fecha del presente requerimiento, la cantidad pendiente de pago asciende a 150.000 euros [...]

CONSECUENCIAS DEL INCUMPLIMIENTO DEL PRESENTE REQUERIMIENTO
[...] optando por la resolucion del contrato, con reclamacion del resarcimiento de los danos y perjuicios [...]
Se hace constar expresamente que el presente requerimiento se practica a los efectos del articulo 1.504 del
Codigo Civil [...] Practicado el requerimiento, no podra concedersele nuevo termino para el pago.
```
Resultado: **PASA**. No aparece el bloque del art. 1279 (exclusivo de V2 = comprador reclamando el otorgamiento), ni el del art. 1502 (suspension del pago, exclusivo del comprador), ni el bloque de clausula penal (descartado por el cliente). La advertencia numero 2 del pie, sobre el burofax y el art. 1504, se mantiene incluso habiendose elegido el acta notarial, porque documenta la razon de la eleccion.

---

## Contra-caso — Vivienda arrendada sin notificar la venta al arrendatario

**Mensaje inicial:** "Quiero vender un piso que tengo alquilado. El inquilino lleva tres anos y le queda contrato, pero no le he dicho nada porque no quiero que se ponga nervioso. Necesito el contrato de compraventa. Soy el vendedor."

### Recorrido del arbol
```
V1 -> escucha activa: "necesito el contrato de
       compraventa"                                    V1 = contrato privado de compraventa
V2 -> escucha activa: "soy el vendedor"                V2 = vendedor
V4 -> escucha activa: "un piso que tengo alquilado"    V4 = ARRENDADO
Sub-pregunta V4 -> PREGUNTA: tipo de arrendamiento -> 1 sub-V4 = arrendamiento de vivienda
Validacion: PARADA BLOQUEANTE del art. 25 LAU.
       El cliente confirma que NO ha notificado nada
       -> salida 2 del guardrail: advertir y ofrecer
       las dos vias antes de continuar
```
V3 no se pregunta todavia: la parada bloqueante se aplica antes.

### Comportamiento esperado
La skill **no** pasa a la Confirmacion ni empieza a pedir datos del inmueble. En el mismo turno en que resuelve el sub-vector, informa de que:

1. Al estar la vivienda arrendada, el arrendatario tiene derecho de tanteo y retracto (art. 25 de la Ley 29/1994), y hay que notificarle de forma fehaciente la decision de vender, el precio y las demas condiciones esenciales, con un plazo de **treinta dias naturales** para ejercitar el tanteo.
2. Si se vende sin esa notificacion, el arrendatario podra ejercitar el **retracto sobre la vivienda ya vendida**, subrogandose en la posicion del comprador con reembolso del precio y de los gastos (art. 25.3 en relacion con el art. 1518 CC). El comprador pierde el inmueble.
3. La escritura de venta de vivienda arrendada **no sera inscribible** sin justificar la notificacion (art. 25.5), y declarar en la escritura que no estaba arrendada seria falsedad en documento publico.
4. Los efectos de la notificacion **caducan a los ciento ochenta dias naturales**: si la firma se retrasa mas alla, hay que volver a notificar.

Y ofrece dos vias, sin continuar hasta que el cliente elija: (a) practicar la notificacion y esperar los treinta dias antes de firmar; o (b) firmar condicionando la eficacia del contrato a la notificacion y al transcurso del plazo, activando el bloque condicional del asset.

La skill **no acepta** la razon del cliente ("no quiero que se ponga nervioso") como motivo para omitir la notificacion, y **no** ofrece la renuncia del art. 25.8 como salida, porque la renuncia debe constar en el contrato de arrendamiento ya firmado y ademas exige comunicar la intencion de vender con treinta dias de antelacion.

**Resultado: PASA.** La advertencia se emite **antes** de la Confirmacion y antes de pedir un solo dato de relleno, de modo que el cliente no invierte turnos en un contrato que hay que replantear, y el riesgo mas grave de la operacion (perder el inmueble por retracto) se pone sobre la mesa en el primer turno util.

---

## Verificacion en vivo (no solo sobre el papel)

Ademas del recorrido simulado de los cuatro escenarios, se ejecuto realmente el Escenario 1 como lo haria el agente operacional, sin instalar el plugin como skill invocable de Claude Code (no esta registrado en este entorno):

1. **Punto 2 real:** se leyeron en vivo, contra la API de legislacion consolidada del BOE, los bloques `art1445`, `art1450`, `art1454`, `art1455`, `art1461`, `art1462`, `art1465`, `art1468`, `art1469`, `art1474`, `art1475`, `art1483`, `art1484`, `art1485`, `art1486`, `art1489`, `art1490`, `art1500`, `art1502`, `art1503`, `art1504`, `art1505`, `art1124`, `art1152`, `art1255`, `art1279`, `art1280`, `art1518`, `art1875`, `art1964` y `art1973` del Codigo Civil; `a25` y `a31` de la LAU; `a17`, `a19`, `a20` y `daprimera` de la LOE; `a8` del ITPAJD; `a106` del TRLRHL; y `a17` de la LGT. Cada uno confirmado leyendo la **ultima** version del bloque, y volcado literalmente a `references/fuentes-plantillas-validadas.md`.
2. **Punto 4 real:** se aplico el `Write` en `test-local/output/contrato_arras_qa_prueba.md` con los datos sinteticos del Escenario 1, resolviendo los bloques condicionales (Bloque C de arras penitenciales, Bloque B de financiacion, bloque de hipoteca a cancelar, bloque de comparecencia del conyuge, bloque de anejos) **sin el envoltorio de comentario**, y omitiendo por completo los bloques de las ramas no aplicables.
3. **Punto 5 real:** dos ciclos de `Edit` incremental (notario de la clausula quinta, correos de la clausula decima) con el `oldString` copiado literalmente del `Read` previo. Ambos aplicados a la primera, sin fallos de coincidencia.
4. **Bucle final real:** un tercer `Edit` elimino el apartado "CLAUSULAS ADICIONALES" al no haberse pedido ninguna.

Resultado verificado en el archivo real, no en un extracto manual: **cero comentarios HTML residuales, cero placeholders sin resolver, cero HTML crudo (`<br>`, `<div>`, `<span>`, entidades), 31 lineas con salto duro de dos espacios en los bloques de datos, y numeracion de clausulas PRIMERA a DECIMOSEGUNDA sin huecos ni saltos**. Verificado tambien por `grep` que no se filtro ni una linea de las ramas no aplicables (arras confirmatorias, arras penales, arrendamiento, renuncia al retracto, obra nueva, Ley 38/1999, IVA/AJD, subrogacion hipotecaria). **PASA.**

Auditoria mecanica de los tres assets contra la seccion 4 de la guia de autoria: cero placeholders con texto de ayuda o lista de opciones dentro de las llaves, cero placeholders anidados, cero marcadores genericos del tipo `{{DATO_FALTANTE}}` (73 placeholders distintos en `contrato-arras.md`, 98 en `contrato-compraventa-vivienda.md`, 44 en `requerimiento-cumplimiento.md`, todos con nombre propio), cero corchetes simples del tipo `[DATO]` que colisionarian con los identificadores de privacidad, y cero HTML crudo distinto de los comentarios condicionales internos. **PASA.**

---

## Revision UX

Hallazgos:

1. **La advertencia sobre las arras llega en el primer contacto, no en la seccion 6.** El texto fijo de Confirmacion de la hoja ARRAS ya dice que el art. 1454 solo contempla el desistimiento y que la triple calificacion es jurisprudencial. Un cliente que llega con la idea de que "las arras se pierden y ya esta" recibe la correccion antes de invertir treinta turnos en el documento.
2. **V4 se pregunta antes que V3.** El estado arrendaticio puede dejar el caso fuera de alcance (local) o forzar una parada bloqueante que cambia el deliverable; la financiacion solo anade o quita una clausula. Preguntar primero lo que puede replantear el documento evita trabajo perdido. Queda escrito en el `SKILL.md` como decision explicita, no como orden accidental.
3. **La parada del art. 25 LAU se ejecuta antes de la Confirmacion**, igual que la caducidad en la skill de ejecucion: el contra-caso demuestra que el cliente recibe la mala noticia en el primer turno util y con dos salidas concretas, no con un "consulte a un abogado".
4. **La seccion de clase de arras explica en un orden fijo de tres pasos** (que dice la ley, que pasa con cada clase, y que el silencio se presume confirmatorio) en lugar de dejar el orden al criterio del operador. Sin ese orden, la tentacion es empezar por la tabla de los tres tipos, que es exactamente el error de presentarlos como categorias legales.
5. **La orientacion por V2 esta escrita punto por punto, no como principio general.** Cada `[negociacion]` dice como se explica al comprador y como al vendedor. Un "adapta la explicacion segun quien sea el cliente" generico se habria traducido en la practica en la misma explicacion neutra para los dos.
6. **En la seccion de financiacion, cuando V3 = 1 la skill no formula las preguntas**, solo activa el bloque de que no hay condicion suspensiva. Sin esa instruccion explicita, el operador tenderia a preguntar "¿necesita financiacion?" a un cliente que ya dijo que tiene el dinero.
7. **La clausula penal se pregunta siempre con el "¿sustituye o se acumula?"** en vez de dejarlo al silencio. El art. 1152 hace que el silencio sustituya, que es lo contrario de lo que la mayoria de las partes cree haber pactado.

Ajustes aplicados durante el test:

1. **Falta detectada en el asset de arras: no tenia clausula de condicion suspensiva de financiacion**, pese a ser V3 un vector de la hoja. Se anadio como clausula OCTAVA con **dos bloques alternativos** (con financiacion pendiente / sin ella), de modo que la clausula existe siempre y la numeracion no deja hueco cuando no aplica, y se renumeraron las cuatro clausulas siguientes.
2. **Gramatica rota por placeholder mal encajado.** En ambos contratos, la frase "el VENDEDOR devolvera [...] conforme a `{{destino_arras_si_denegacion}}`" producia texto agramatical al rellenarse ("conforme a la devolucion integra de los 12.000 euros"). Reescrita como "en los siguientes terminos: `{{destino_arras_si_denegacion}}`", y lo mismo con `{{consecuencia_vencimiento_condicion}}`. Detectado al leer el documento real, no el asset.
3. **Placeholder residual visible al cliente al cerrar el documento.** El apartado "CLAUSULAS ADICIONALES" dejaba `{{clausulas_adicionales_solicitadas_por_el_usuario}}` en el archivo cuando no se pedia ninguna clausula extra. Se anadio al bucle de realimentacion final una verificacion con `Read` que obliga a eliminar el apartado completo en ese caso, y a informar al cliente de cualquier otro placeholder que quede pendiente en vez de cerrarlo en silencio.
4. **Hallazgo normativo no previsto en el encargo: el art. 31 LAU** extiende el tanteo y retracto del art. 25 a los arrendamientos para uso distinto de vivienda. Registrado en la reference y en el enrutamiento: aunque la compraventa de local esta fuera de alcance, la skill advierte del riesgo de retracto **antes** de escalar, en lugar de escalar sin decir nada.
5. **Correccion de numeracion normativa respecto del encargo:** la regla de que el pacto fiscal no vincula a la Administracion esta en el **art. 17.5** LGT, no en el 17.4 (el antiguo apartado 4 se renumero como 5 por el RDL 20/2011). Todos los assets y references citan el 17.5.

---

## QA en vivo por agente independiente

Ejecutado el 03/09/2026 por un agente sin contexto previo de la skill. Escenario del cliente, en su literal: *"Voy a comprar un piso por 210.000 euros. El vendedor me pide 10.000 de senal esta semana. Todavia no tengo la hipoteca concedida, me la contestan en un mes. El piso esta alquilado, creo que al inquilino le queda un ano de contrato."*

Es el **primer recorrido completo de la rama arrendada hasta documento en disco**. El contra-caso anterior se detuvo en la advertencia y no llego a escribir contrato, y el Escenario 1 en vivo se ejecuto sobre vivienda libre. Esa combinacion es la que dejo sin destapar los defectos 1 y 2 de esta seccion.

Artefactos reales: verificacion BOE en vivo (`art1454`, `art1124`, `art1152`, `a25`, `a31` y `a14` de la LAU, `a36` LAU), un `Write` y trece `Edit` incrementales con `oldString` copiado del `Read` previo, todos aplicados a la primera. Documento resultante en `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/compraventa-qa-prueba.md`.

### Recorrido real y texto literal generado

**Turno 1** — la escucha activa resolvio de un solo mensaje V1 (arras, por "senal"), V2 (comprador, por "voy a comprar"), V3 (financiacion pendiente) y V4 (arrendado). Solo quedo abierta la sub-pregunta de V4, porque de ella depende una parada de alcance:

> **Skill cargada satisfactoriamente.**
>
> Vamos a preparar el documento que corresponda a su operacion sobre el inmueble. Para ajustarlo a su caso, es necesario precisar antes algunos datos.
>
> El arrendamiento es:
> 1. De vivienda
> 2. De local o para un uso distinto de vivienda

**Turno 2** — resuelto el sub-vector como vivienda, parada bloqueante del art. 25 LAU antes de la Confirmacion:

> Al estar la vivienda arrendada, el arrendatario tiene un derecho de adquisicion preferente: la ley le reconoce la posibilidad de comprarla el mismo, en las mismas condiciones que usted, antes de que la venta se cierre con un tercero. Es el derecho de tanteo, previsto en el articulo 25 de la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos. Para que ese derecho quede correctamente agotado, el vendedor debe notificar al arrendatario, de forma fehaciente, su decision de vender, el precio y las demas condiciones esenciales de la operacion, y esperar treinta dias naturales.
>
> ¿Le consta que el vendedor haya practicado ya esa notificacion al arrendatario y, en su caso, en que fecha?

Respuesta simulada del cliente: *"No, no se ha notificado nada. El vendedor dice que el inquilino no tiene derecho a nada porque el contrato esta a punto de acabar."*

**Turno 3** — salida 2 del guardrail, con las dos vias y sin continuar:

> Debo advertirle de que esa afirmacion del vendedor no es correcta, y de que la omision de la notificacion tiene dos consecuencias graves, ambas contra usted como comprador.
>
> La primera es el derecho de retracto. Si la venta se firma sin haber notificado al arrendatario, este podra, una vez efectuada la compraventa, subrogarse en la posicion de usted como comprador reembolsandole el precio y los gastos del contrato, conforme al articulo 25.3 de la Ley 29/1994 en relacion con el articulo 1.518 del Codigo Civil. Dicho de otro modo: usted habria pagado 210.000 euros y podria perder la vivienda, quedandose unicamente con la devolucion de lo pagado.
>
> La segunda es registral. La escritura de venta de una vivienda arrendada no puede inscribirse en el Registro de la Propiedad sin justificar que la notificacion se ha practicado, conforme al articulo 25.5 de la misma Ley. Si el vendedor pretendiese sortearlo declarando en la escritura que la vivienda no estaba arrendada, esa declaracion se hace bajo pena de falsedad en documento publico.
>
> Que el contrato de arrendamiento este proximo a su vencimiento no elimina ninguno de los dos efectos: mientras el arrendamiento este vigente en el momento de la venta, el derecho existe.
>
> Caben dos vias, y necesito que elija una:
> 1. Que el vendedor practique la notificacion y se esperen los treinta dias naturales antes de firmar el contrato de arras.
> 2. Firmar ahora el contrato de arras, condicionando expresamente su eficacia a que el vendedor practique la notificacion y transcurra ese plazo sin que el arrendatario ejercite el tanteo.

**Turno 6, seccion 6 — clase de arras.** Es el punto critico de la skill y el que mas texto genera:

> Determinamos ahora la clase de arras y sus consecuencias, que es el punto mas relevante de este contrato.
>
> El articulo 1.454 del Codigo Civil dice unicamente que, si median arras o senal en una compraventa, el contrato podra rescindirse allanandose el comprador a perderlas o el vendedor a devolverlas duplicadas. Eso es todo lo que dice la ley. La clasificacion de las arras en confirmatorias, penales y penitenciales no figura en el Codigo Civil: la ha construido la jurisprudencia, y por eso el contrato tiene que decir expresamente de que clase son.
>
> Si son confirmatorias, los 10.000 euros son senal de que el contrato existe y anticipo del precio, y no facultan a nadie para retirarse. Si usted no llegase a comprar, estaria incumpliendo: el vendedor podria exigirle el cumplimiento o resolver el contrato, y en ambos casos reclamarle danos e intereses, conforme al articulo 1.124 del Codigo Civil. Su perdida podria superar los 10.000 euros.
>
> Si son penales, tampoco facultan para retirarse, pero se anade una pena convencional: el vendedor retendria los 10.000 euros como pena si usted incumple, y le devolveria 20.000 si incumple el. Salvo que se pacte lo contrario, esa pena sustituye a la indemnizacion de danos, conforme al articulo 1.152 del Codigo Civil.
>
> Si son penitenciales, los 10.000 euros son el precio de poder retirarse: usted podria desistir perdiendo esa cantidad, y el vendedor podria desistir devolviendole 20.000 euros, quedando el contrato sin efecto sin nada mas que reclamar por ninguna de las dos partes. Son las unicas que encajan en el articulo 1.454.
>
> Debe saber ademas que el silencio juega en su contra: si el contrato no dice de que clase son, la jurisprudencia tiende a presumir que son confirmatorias, que es precisamente la clase que no permite retirarse.
>
> En su situacion concreta, y dado que la hipoteca aun no esta concedida, le advierto de que las arras penitenciales no le devuelven el dinero: le permiten retirarse, pero perdiendo los 10.000 euros. Para recuperarlos si el banco le deniega el prestamo necesita ademas la condicion suspensiva de financiacion. Son dos protecciones distintas y le conviene tener las dos.
>
> ¿De que clase desea que sean las arras: confirmatorias, penales o penitenciales?

**Seccion 10 — financiacion**, orientada a V2 = comprador:

> Valoramos como protegerle si la financiacion no llega a concederse.
>
> Sin una clausula especifica, la denegacion del prestamo no le exime de pagar: si el banco le dice que no y usted no puede reunir los 200.000 euros restantes, el incumplidor es usted, no el vendedor. Con arras penitenciales eso significa perder los 10.000 euros. La condicion suspensiva convierte la denegacion en un supuesto previsto y no culpable: si se produce, el contrato queda sin efecto y usted recupera lo entregado.
>
> Indique el importe minimo de financiacion que necesita obtener y la fecha limite para obtenerla.

### A) Calidad del texto generado por el agente

- **Tono y tratamiento: PASA.** "usted" en todos los turnos ("le advierto de que", "necesito que elija una", "Indique el importe minimo"). Cero coloquialismos, cero "vale/perfecto/genial". Normas citadas con nombre completo y articulo ("articulo 25.3 de la Ley 29/1994 en relacion con el articulo 1.518 del Codigo Civil"), como exige el `CLAUDE.md` del plugin.
- **Explicacion antes de la decision: PASA, y con margen.** Los cuatro puntos `[negociacion]` que tocaba el escenario (clase de arras, cargas, condicion suspensiva, derecho del arrendatario) se explicaron con la consecuencia economica traducida a la cifra concreta del caso — "usted habria pagado 210.000 euros y podria perder la vivienda", "el vendedor le devolveria 20.000" — antes de pedir ninguna decision. El orden fijo de tres pasos de la seccion 6 funciona: obliga a empezar por lo que dice la ley y no por la tabla de los tres tipos.
- **Directiva de Invisibilidad: PASA con una salvedad.** Cero menciones de vectores, hojas o fases. La unica frase de proceso que se colo fue "Para recuperarlos [...] necesita ademas la condicion suspensiva de financiacion, que trataremos despues", con la coletilla final eliminada al revisar. Es una tentacion real del punto 6, porque la explicacion de arras penitenciales exige remitirse a una clausula que aun no se ha negociado; conviene que el `SKILL.md` prevea esa remision como contenido sustantivo, no como anuncio de agenda.
- **Cero invenciones: PASA.** Ni un importe, plazo ni cita normativa sin origen. Los articulos citados al cliente se leyeron en vivo en el BOE en este mismo test. Referencia catastral, datos registrales, IBAN, notario y numero de protocolo quedaron como placeholder porque el cliente no los tenia, y se le informo de ello al cerrar, tal como manda el bucle final.
- **Friccion detectada, no defecto legal.** El paso 4 del Punto 4 obliga a preguntar "¿desea empezar a completar los datos del documento?" tras confirmar la ruta. Es un turno muerto: el cliente ya eligio plantilla en el turno anterior. Contradice ademas el espiritu del Punto 0, que prohibe expresamente detenerse a preguntar si desea empezar. **No corregido**: afecta a la estructura comun de las skills del plugin y merece decision del lead, no un parche local.

### B) El asset visto desde el LLM que lo rellena

- **Numeracion: PASA.** PRIMERA a DECIMOSEGUNDA sin huecos en el documento real (`grep '^### '` sobre el archivo generado). Los bloques condicionales viven dentro de clausulas, no como clausulas propias, de modo que ninguna rama no aplicable deja un salto de ordinal.
- **Cero comentarios HTML y cero corchetes simples** en el documento generado, verificado por `grep`.
- **Placeholder ambiguo detectado (corregido).** `{{importe_pena_vendedor}}` en el Bloque B de arras penales: la frase pide "el total a satisfacer", que es el **doble** de las arras, pero el nombre del placeholder induce a escribir solo la pena. Con arras de 10.000 euros, un LLM que se fie del nombre escribe 10.000 donde el contrato exige 20.000, y el vendedor incumplidor paga la mitad de lo pactado.
- **Placeholder que rompia la frase (corregido).** `{{situacion_cargas}}` se insertaba dentro de "el inmueble se encuentra {{situacion_cargas}}, y se obliga a entregarlo...". Al necesitar dos oraciones (manifestacion del vendedor + advertencia de que no hay nota simple), hubo que romper el texto fijo de la plantilla para que la frase cerrase. Un placeholder que obliga a reescribir el molde esta mal colocado.
- **Frase forzada en la clausula OCTAVA (corregida).** El parrafo de cierre decia "la falta de obtencion de financiacion **no prevista expresamente en esta clausula** constituiria un incumplimiento del COMPRADOR". Leido detras de la condicion suspensiva, un cliente lego entiende lo contrario de lo que dice.
- **Lectura de corrido: aprueba tras las correcciones, suspendia antes.** Con el texto original, el contrato decia en la clausula sexta que el vendedor entrega el inmueble "libre de cargas y gravamenes, **de arrendatarios y ocupantes**" y en la septima que el inmueble esta arrendado hasta 2027 y que el comprador se subroga. Dos clausulas seguidas que se contradicen: eso no suena a contrato real, suena a plantilla mal encajada.

### C) Los dos puntos criticos

**C1 — Arras. PASA en lo sustantivo, con un defecto latente corregido.**

La skill nunca presenta la triple calificacion como categoria legal. El texto fijo de la Confirmacion, el guardrail 3, el punto 2.5 de la verificacion normativa y la reference dicen los cuatro que es construccion jurisprudencial, y la seccion 6 impone el orden de explicacion correcto. La clase es bloqueante y el documento no puede cerrarse sin ella. El literal del art. 1454 se comprobo en vivo: sigue sin clasificar nada.

El defecto latente estaba en el asset, no en el discurso: la clausula **DECIMOSEGUNDA** decia, sin condicion alguna, "El presente contrato se rige por el Codigo Civil, y en particular por sus articulos 1.445 y siguientes, **y por el articulo 1.454 en cuanto a las arras entregadas**". Con arras confirmatorias o penales ese contrato cita el 1.454 como norma reguladora de las arras, que es exactamente lo que el guardrail 3 del propio `SKILL.md` prohibe. En este test no salto porque las arras pactadas fueron penitenciales; con cualquiera de las otras dos clases el documento se contradice con su propia skill.

**C2 — Inmueble arrendado. PASA en la advertencia, FALLABA en el documento.**

La advertencia sale sola y en el primer turno util, sin que el cliente pregunte: el agente paro antes de la Confirmacion, explico tanteo y retracto, la no inscribibilidad del art. 25.5 y la falsedad en documento publico, rebatio el argumento del vendedor ("el contrato esta a punto de acabar") y ofrecio las dos vias sin continuar. Eso funciona.

Lo que no funcionaba es el paso siguiente. El `SKILL.md` promete tres bloques del asset por nombre —notificacion practicada, renuncia comprobada y condicion de eficacia— y el contra-caso de este mismo fichero remata con "activando **el bloque condicional del asset**". En `contrato-arras.md` solo existia uno de los tres. Elegida la via 2 por el cliente, la unica que permite firmar esta semana, el agente se encontro sin bloque que insertar y tuvo que improvisar la clausula de condicion suspensiva de eficacia: precisamente la clausula que sostiene toda la advertencia anterior. Una skill que advierte de un riesgo y despues no tiene el texto que lo cubre deja al cliente peor que si no hubiera advertido.

### Correcciones aplicadas

En `assets/contrato-arras.md`:

1. **Clausula SEXTA** reescrita con dos bloques alternativos. Solo el de inmueble libre obliga a entregar "libre de arrendatarios y ocupantes"; el de inmueble arrendado dice que se transmite con el arrendamiento subsistente. De paso, `{{situacion_cargas}}` pasa a frase propia ("El VENDEDOR manifiesta la siguiente situacion de cargas del inmueble: ...") y deja de romper el molde.
2. **Clausula QUINTA** con los mismos dos bloques: entrega de llaves si esta libre; entrega del contrato de arrendamiento, el justificante de la fianza y la relacion de rentas si esta arrendado, con la remision al art. 1.462 CC.
3. **Clausula SEPTIMA**: anadidos los dos bloques que el `SKILL.md` prometia y no existian — notificacion ya practicada (con fecha, medio y recordatorio de la caducidad de ciento ochenta dias) y condicion suspensiva de eficacia por notificacion al arrendatario (plazo para notificar, devolucion de arras si el arrendatario ejercita el tanteo, resolucion a favor del comprador si el vendedor no notifica, y prohibicion de otorgar escritura antes de acreditar el cumplimiento). Al bloque de arrendamiento existente se le anadio la subrogacion del comprador en la posicion de arrendador y en la fianza (art. 14 LAU, verificado en vivo).
4. **Clausula DECIMOSEGUNDA**: la mencion del art. 1.454 pasa a bloque condicional, insertable solo si las arras son penitenciales, con la instruccion expresa de no insertarlo en las otras dos clases.
5. `{{importe_pena_vendedor}}` renombrado a `{{importe_total_a_satisfacer_por_el_vendedor}}`, con "equivalente al doble de las arras entregadas" en el propio texto.
6. Parrafo de cierre de la clausula OCTAVA reescrito: "fuera de los supuestos expresamente previstos en esta clausula, la falta de pago del precio por no disponer el COMPRADOR de financiacion constituira un incumplimiento suyo".

En `SKILL.md`:

7. Seccion 9 de la HOJA ARRAS: se advierte de que V4 gobierna ademas las clausulas quinta y sexta, que hay que insertar el mismo bloque en las tres, y que un contrato que obligue a entregar libre de arrendatarios mientras describe un arrendamiento vigente es contradictorio y no puede cerrarse.
8. Bucle de realimentacion final: dos comprobaciones nuevas en el `Read` de cierre — que el art. 1.454 no aparece en ninguna clausula si las arras no son penitenciales, y que el estado posesorio es coherente en todo el documento.

### Observaciones sin corregir

- **Los assets del plugin se escriben sin tildes** ("clausula", "senal", "articulo", "danos"). Es convencion de todo el repositorio, no de esta skill, pero el destinatario final es un contrato que firma un cliente: ahi la falta de tildes se lee como un error de redaccion del despacho. Decision de alcance global.
- **`{{municipio_inmueble}}` aparece dos veces** en el asset (clausula primera y fuero de la decimosegunda). Al editar la seccion 3 se resolvio solo la primera y el fuero se quedo con el placeholder crudo hasta el `Read` de cierre. El bucle final lo caza, pero conviene que la seccion 3 del Punto 5 recuerde que ese dato alimenta dos clausulas.
- **La clausula TERCERA fija "En este acto, el COMPRADOR entrega [...] sirviendo el presente documento como carta de pago"** aunque el medio pactado sea transferencia, que puede no estar abonada el dia de la firma. El riesgo es del vendedor, no del cliente de este escenario, pero es una carta de pago por dinero posiblemente no recibido.
- **Transicion abrupta en el primer turno.** Tras la introduccion fija, la primera pregunta que vio el cliente fue si el arrendamiento es de vivienda o de local, cuando el ya habia dicho "piso" e "inquilino". Es correcto preguntarlo, porque de la respuesta depende una parada de alcance, pero al cliente le parece que no le han leido. La Directiva de Invisibilidad impide el puente de una linea que lo arreglaria.
