# Test de ejecucion — skill `derecho-civil-responsabilidad-civil`

Ejecucion manual del arbol de decision sobre cuatro escenarios (3 principales + 1 contra-caso). Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes verificadas realmente contra la API de legislacion consolidada del BOE el **02/09/2026**: Codigo Civil (BOE-A-1889-4763), arts. 1101, 1103, 1591, 1902, 1903, 1907, 1908, 1964, 1968, 1973 y 1974; LCS (BOE-A-1980-22501), arts. 18, 20, 73 y 76; TRLRCSCVM (BOE-A-2004-18911), arts. 1, 1 bis, 2, 7, 9, 14, 49 y Anexo; Ley 5/2025 (BOE-A-2025-15424), disposiciones adicional primera y final novena; LOE (BOE-A-1999-21567), arts. 17 y 18; LO 1/2025 (BOE-A-2025-76), arts. 4, 5, 7 y 9; LEC (BOE-A-2000-323), arts. 249, 250 y 264.
- **Baremo 2026 verificado**: Resolucion de 3 de febrero de 2026 de la DGSFP, BOE-A-2026-3803, publicada el 18/02/2026, IPC de 2025 aplicado **+2,9 %**. Las tablas se publican en el portal de la DGSFP, **no** en el texto consolidado del BOE, cuyo Anexo esta a 25/07/2025 (Ley 5/2025) sin actualizaciones por IPC.
- **Correccion detectada durante la verificacion**: la disposicion adicional primera de la Ley 5/2025 (seguro obligatorio de vehiculos personales ligeros) **NO** entro en vigor con el resto de la ley el 26/07/2025, sino el **02/01/2026**, por su disposicion final novena, apartado 2. La skill trata esa fecha como frontera de rama (ver Test 2 y la Revision UX).
- En este test la lectura online se ejecuto de verdad; los importes del baremo que aparecen en los extractos son SINTETICOS y no se corresponden con las tablas reales: en un lanzamiento real el operador abre la tabla del ejercicio y lee el importe (guardrail 6).

---

## Test 1 — Colision de trafico con lesiones, aseguradora identificada, dentro de plazo

**Mensaje inicial:** "Me chocaron por detras el 15 de junio de este ano en un semaforo. Tuve un esguince cervical, me dieron el alta el 10 de agosto y el coche quedo con danos en el porton. Se cual es la aseguradora del que me choco. No he reclamado nada todavia."

### Recorrido del arbol
```
V1 -> escucha activa: "me chocaron por detras... en un
       semaforo"                                        V1 = accidente de circulacion (sin pregunta)
V2 -> escucha activa: "el coche" / "el que me choco"     V2 = vehiculo a motor (sin pregunta)
V3 -> no aplica (exclusivo de rama no circulatoria)
FILTRO DE PRESCRIPCION:
       plazo aplicable = 1 ano (arts. 1968.2 CC y 7.1
       TRLRCSCVM); fechas ya en escucha activa
       (hecho 15/06/2026, alta 10/08/2026); ningun acto
       interruptivo -> dies a quo 10/08/2026 ->
       vencimiento 10/08/2027 -> PLAZO VIVO, holgado
V4 -> NO se pregunta (en circulacion el plazo es de un
       ano por ley; V4 solo se pregunta si cambiaria el
       resultado del filtro)
V5 -> escucha activa: "no he reclamado nada todavia"     V5 = primera reclamacion (sin pregunta)
V6 -> escucha activa: "se cual es la aseguradora"        V6 = aseguradora identificada (sin pregunta)
HOJA RECLAMACION -> assets/reclamacion-extrajudicial-danos.md
```
Los seis vectores quedan resueltos por Escucha Activa: **cero preguntas de clasificacion**. El filtro de prescripcion tampoco pregunta, porque las dos fechas venian en el mensaje inicial.

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija. Todos los vectores y las fechas del filtro estan resueltos -> pasa directo a la verificacion normativa (interna) y a la Confirmacion, en el mismo turno.
- Turno 2 (mismo mensaje que el anterior si no hay nada que preguntar): Confirmacion visible con el texto fijo CIRCULACION CON VEHICULO A MOTOR + el plazo calculado (vence el 10/08/2027) + el aviso de que la reclamacion interrumpe la prescripcion y sirve de actividad negociadora previa + eleccion plantilla/documento propio.
- Turnos 3-7: datos del perjudicado (nombre, DNI, domicilio, telefono y email, letrado), un dato por turno; **la vista previa y la confirmacion agrupada se emiten en el turno 8, posterior a la respuesta del ultimo sub-apartado**.
- Turno 9: contra quien se dirige la reclamacion (negociacion) — la skill explica el art. 76 LCS y la inmunidad de la accion directa frente a las excepciones del asegurador contra su asegurado, y **recomienda por defecto dirigirla a ambos**; el usuario acepta.
- Turnos 10-14: datos de los dos destinatarios (causante y aseguradora), con confirmacion agrupada separada por cada uno.
- Turnos 15-18: el hecho danoso — la fecha y hora **no se vuelven a preguntar** (ya conocidas por el filtro); se piden lugar, descripcion, circunstancias relevantes y referencia del atestado. La skill informa de que las Fuerzas y Cuerpos de Seguridad de trafico facilitan gratuitamente copia del atestado a peticion del perjudicado (art. 7.1 TRLRCSCVM) y ofrece dejarlo solicitado en el escrito.
- Turnos 19-20: los danos sufridos, preguntando por cada partida con que documento se acredita. No hay lucro cesante acreditable: la partida se pone a cero, no se estima.
- Turnos 21-23: cuantificacion (negociacion) — la skill explica antes de pedir cifras que el baremo es OBLIGATORIO en este caso (art. 1.4 TRLRCSCVM), cita la Resolucion de la DGSFP de 03/02/2026 y advierte de que una partida sin soporte se elimina.
- Turnos 24-25: requerimiento y propuesta (negociacion) — la skill explica que la aseguradora esta obligada a responder con oferta motivada en tres meses (art. 7.2) y que su silencio devenga los intereses del art. 9 en relacion con el art. 20 LCS (interes legal + 50 %, minimo 20 % anual pasados dos anos); propone 30 dias naturales de plazo, coherente con el art. 7.1 LO 1/2025.
- Turno 26: medio de envio, documentos y cierre — advertencia obligatoria sobre la fehaciencia del envio.

### Documento generado (extracto relleno real, datos sinteticos)
```
RECLAMACION EXTRAJUDICIAL DE DANOS Y PERJUICIOS — PERJUDICADO A frente a RESPONSABLE A
> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico definitivo.
> Version de las normas verificada en el BOE: 02/09/2026

PRIMERO. El 15/06/2026, a las 08:40 horas, en la interseccion de la Avenida Ejemplo con la Calle
Ejemplo 12 de Ciudad Ejemplo, el vehiculo conducido por RESPONSABLE A colisiono por alcance con el
vehiculo en el que circulaba esta parte, que se encontraba detenido ante un semaforo en fase roja.

CUARTO. Desglose: Dano personal 2.487,40 euros. Dano material 1.930,00 euros. Lucro cesante 0,00 euros.
TOTAL RECLAMADO 4.417,40 euros.

QUINTO. [...] este escrito constituye la comunicacion del siniestro y la reclamacion previa de la
indemnizacion, e inicia el plazo de tres meses del que esa entidad dispone para presentar oferta
motivada [...] (arts. 7.1 y 7.2 TRLRCSCVM).
```
Resultado: **PASA**. No aparece ningun bloque de otra rama: sin referencias a vehiculos personales ligeros, a la Ley 5/2025, a la Ley 38/1999, al art. 1903 CC, a la *lex artis*, al art. 1101 CC, al art. 1591 CC ni a la advertencia de videovigilancia (comprobado programaticamente sobre el archivo real).

---

## Test 2 — Atropello por patinete electrico (VMP)

**Mensaje inicial:** "El mes pasado, el 20 de agosto, me atropello un patinete electrico en un carril bici y me fracture la muneca. Todavia estoy en rehabilitacion. El chico se identifico y me dijo que tenia el patinete registrado y con seguro. Quiero reclamarle."

### Recorrido del arbol
```
V1 -> escucha activa: "me atropello un patinete"          V1 = accidente de circulacion
V2 -> escucha activa: "patinete electrico"                V2 = vehiculo personal ligero
FILTRO DE PRESCRIPCION:
       plazo = 1 ano; hecho 20/08/2026; SIN alta aun
       ("todavia estoy en rehabilitacion") -> la skill
       computa desde el hecho (hipotesis desfavorable) y
       advierte de que el dies a quo se desplazara al alta
       -> vencimiento provisional 20/08/2027 -> VIVO
V4 -> NO se pregunta (circulacion)
V5 -> escucha activa: "quiero reclamarle"                 V5 = primera reclamacion
V6 -> escucha activa: "me dijo que tenia... seguro"       V6 = aseguradora identificada, PERO no consta
                                                          la compania -> la skill lo trata como
                                                          identificable, no identificada
COMPROBACION DE RAMA VMP (enrutamiento):
       fecha del hecho 20/08/2026 > 02/01/2026 -> el
       seguro obligatorio de VMP SI estaba en vigor
       -> se comprueban los tres requisitos del apdo. 1
       de la DA 1.ª Ley 5/2025
HOJA RECLAMACION -> assets/reclamacion-extrajudicial-danos.md (bloque VMP activado)
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija. V1, V2, V5 resueltos por escucha activa. El filtro de prescripcion **si** pregunta aqui: "Indique la fecha del alta medica o del informe de estabilizacion de las secuelas, si ya se ha producido." El usuario responde que sigue en tratamiento.
- Turno 2: la skill informa del computo provisional y de que el plazo se desplazara al alta, y pregunta si ha remitido alguna reclamacion previa por escrito. El usuario dice que no.
- Turno 3: **pregunta especifica de la rama VMP**, antes de la Confirmacion: "Indique si el patinete contaba con certificado de circulacion, estaba inscrito en el Registro de Vehiculos de la Direccion General de Trafico y llevaba etiqueta identificativa con su numero de inscripcion o matricula." El usuario confirma que el conductor le mostro la etiqueta.
- Turno 4: Confirmacion visible con el texto fijo CIRCULACION CON VEHICULO PERSONAL LIGERO — cita la disposicion adicional primera de la Ley 5/2025, su vigencia desde el 02/01/2026 y las coberturas minimas de 6.450.000 y 1.300.000 euros — + eleccion plantilla/documento propio.
- Turnos 5 y siguientes: igual estructura que el Test 1. En la seccion "Datos del destinatario", como no se conoce la compania, la skill activa el requerimiento del ultimo inciso del art. 76 LCS (el asegurado debe manifestar la existencia y el contenido de su seguro) y menciona el fichero de vehiculos asegurados del Consorcio (art. 2.2 TRLRCSCVM).
- Seccion de cuantificacion: al estar el patinete dentro del ambito del seguro obligatorio, **el baremo es obligatorio igual que en un accidente de coche**. Como el proceso curativo no ha terminado, la skill explica que la reclamacion del art. 7.1 TRLRCSCVM **no requiere estar cuantificada**, que no conviene retrasar el envio para cuantificar y activa el bloque de reserva expresa de la diferencia.

### Documento generado (extracto relleno, datos sinteticos)
```
RECLAMACION EXTRAJUDICIAL DE DANOS Y PERJUICIOS — PERJUDICADO B frente a RESPONSABLE B
> DRAFT — para revision por un abogado colegiado antes de su firma.
> Version de las normas verificada en el BOE: 02/09/2026

SEGUNDO. Conforme a la disposicion adicional primera de la Ley 5/2025, de 24 de julio, los vehiculos
personales ligeros quedan sujetos al regimen de responsabilidad civil y seguro del texto refundido de
la Ley sobre responsabilidad civil y seguro en la circulacion de vehiculos a motor, y su propietario
esta obligado a suscribir y mantener en vigor el seguro obligatorio de responsabilidad civil.

CUARTO. La cuantificacion anterior tiene caracter provisional, al no haberse producido aun el alta o la
estabilizacion de las secuelas. Esta parte se reserva expresamente la reclamacion de la diferencia que
resulte de la valoracion definitiva del dano.

QUINTO. Le requiero igualmente para que, conforme al ultimo inciso del articulo 76 de la Ley 50/1980,
de Contrato de Seguro, me manifieste la existencia del contrato de seguro que cubra su responsabilidad
civil por estos hechos y su contenido, a los efectos del ejercicio de la accion directa.
```
Resultado: **PASA**. El bloque de vehiculo a motor del art. 1 TRLRCSCVM queda desactivado en favor del bloque VMP; no aparece ningun bloque de rama no circulatoria; la cuantificacion queda expresamente provisional.

### Sub-caso de control de la frontera temporal
Con el mismo relato pero con el hecho fechado el **15/11/2025** (anterior al 02/01/2026), la skill **no** afirma que exista seguro obligatorio: reconduce al art. 1902 CC con culpa probada frente al patrimonio del causante, pregunta si el causante tenia algun seguro voluntario de responsabilidad civil (a menudo el del hogar) y advierte de que el baremo del Anexo pasa a ser **solo orientativo**, lo que exige informe pericial propio. **PASA**: la frontera del 02/01/2026 discrimina correctamente y evita afirmar una cobertura inexistente.

---

## Test 3 — Caida en supermercado, con pericial, sin acuerdo previo

**Mensaje inicial:** "Me resbale en un supermercado en marzo, el dia 12, porque el suelo estaba mojado y no habia ningun cartel. Me rompi el codo. Reclame por burofax en abril y la aseguradora del supermercado me contesto que no se hacen responsables. Quiero demandarles. Tengo el alta de mayo y un informe de un medico forense privado."

### Recorrido del arbol
```
V1 -> escucha activa: "me resbale en un supermercado"     V1 = otro suceso
V2 -> no aplica
V3 -> escucha activa: "en un supermercado... suelo
       mojado"                                            V3 = caida en establecimiento
FILTRO DE PRESCRIPCION:
       plazo = 1 ano (art. 1968.2 CC, posicion
       conservadora); hecho 12/03/2026; alta 05/2026;
       acto interruptivo acreditado: burofax de 04/2026
       -> el plazo se reinicia desde el burofax ->
       VIVO con holgura
V4 -> NO se pregunta: el filtro con el plazo de un ano
       NO daria plazo agotado, luego V4 no cambiaria el
       resultado
V5 -> escucha activa: "quiero demandarles"                V5 = demanda
V6 -> escucha activa: "la aseguradora del supermercado
       me contesto"                                       V6 = aseguradora identificada
VALIDACION DE PROCEDIBILIDAD (enrutamiento):
       V5 = 3 y V1 = 2 -> se exige actividad negociadora
       previa (art. 5 LO 1/2025). CONSTA: burofax de abril
       con respuesta negativa por escrito -> requisito
       cumplido y acreditable -> se puede demandar
HOJA DEMANDA -> assets/demanda-responsabilidad-civil.md (bloques 1902 + 1903 activados)
```

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija. V1, V3, V5, V6 y las fechas del filtro estan en el mensaje inicial. La skill **si** pregunta lo unico que falta del filtro: la fecha exacta del burofax y su medio, para acreditar la interrupcion.
- Turno 2: **advertencia urgente y proactiva** sobre las grabaciones de videovigilancia. La skill informa de que se sobreescriben en dias y, dado que han pasado casi seis meses, pregunta si en su momento se requirio su conservacion. Es la pregunta que decide la viabilidad probatoria del caso y por eso se hace antes de invertir turnos en el escrito.
- Turno 3: Confirmacion visible con el texto fijo CAIDA O SUCESO EN ESTABLECIMIENTO — incluye la advertencia de que **la caida por si sola no genera responsabilidad** y que habra que acreditar la omision del deber de cuidado — + el aviso del requisito de procedibilidad del art. 5 LO 1/2025 y del art. 264.4.º LEC + eleccion plantilla/documento propio.
- Turnos 4-5: **requisito de procedibilidad (seccion 1 de la HOJA DEMANDA, va PRIMERO)**: fecha, medio y destinatario del burofax, justificante de que se dispone, y resultado (respuesta negativa por escrito).
- Turnos 6-10: parte demandante, con confirmacion agrupada. La skill calcula que la cuantia superara los 2.000 euros, luego abogado y procurador son preceptivos y no pregunta por la comparecencia personal.
- Turnos 11-15: parte demandada (negociacion + datos) — la skill explica de nuevo la accion directa del art. 76 LCS, esta vez subrayando que convierte a la aseguradora en demandada por derecho propio, y **recomienda demandar a ambos solidariamente**: al titular del establecimiento por los arts. 1902 y 1903 CC y a la aseguradora por el art. 76 LCS.
- Turnos 16-19: el hecho danoso, con numero de documento por cada elemento.
- Turno 20: la imputacion — la skill explica que **aqui es el demandante quien debe probar la culpa o negligencia** (a diferencia del Test 1, donde la responsabilidad es por riesgo creado y la carga se invierte), y pide la concrecion de la omision del deber de cuidado: suelo mojado sin senalizar, ausencia de cartel, hora y frecuencia de la limpieza si se conocen. Activa el bloque del art. 1903 CC porque la limpieza la realizaba un dependiente del establecimiento.
- Turnos 21-23: los danos, con el desglose detallado de dias de perjuicio temporal (muy grave, grave, moderado y basico), intervenciones y puntos de secuela.
- Turno 24: nexo causal y prueba pericial (negociacion) — la skill confirma que existe informe pericial y pregunta si se anuncia la proposicion de pericial y testifical.
- Turnos 25-27: cuantificacion (negociacion) — **la skill explica expresamente que aqui el baremo NO es de aplicacion directa** y que se cita como referencia orientativa, apoyando la cifra en el informe pericial. Advierte tambien de la culpa concurrente (la propia falta de atencion del perjudicado es la defensa habitual) y de la moderacion judicial del art. 1103 CC.
- Turno 28: no prescripcion — redacta el hecho y el fundamento con las fechas y el burofax como acto interruptivo.
- Turno 29: intereses (negociacion) — art. 20 LCS, impuesto de oficio, interes legal + 50 %, desde la fecha del siniestro. **No** se invoca el art. 9 TRLRCSCVM: no es un caso de circulacion.
- Turno 30: procedimiento, cuantia y juzgado — la skill calcula el procedimiento por la cuantia (verbal hasta 15.000 euros, art. 250.2 LEC; ordinario por encima, art. 249.2 LEC) y confirma el fuero del lugar del hecho danoso.
- Turnos 31-32: documentos (con verificacion propia de que estan el poder y el documento del art. 264.4.º LEC) y lugar y fecha.

### Documento generado (extracto relleno, datos sinteticos)
```
DEMANDA DE RESPONSABILIDAD CIVIL — PERJUDICADO C contra ESTABLECIMIENTO EJEMPLO SA
> DRAFT — para revision por un abogado colegiado antes de su firma.

SEGUNDO. El demandado responde conforme al articulo 1902 del Codigo Civil, por haber omitido el deber
de cuidado que le incumbia. Concretamente: mantuvo el pavimento de la zona de acceso mojado tras su
limpieza sin colocar senalizacion alguna de advertencia. El demandado responde ademas conforme al
parrafo quinto del articulo 1903 del Codigo Civil, en su condicion de titular del establecimiento, por
los perjuicios causados por su dependiente con ocasion de sus funciones, sin que haya empleado toda la
diligencia exigible para prevenir el dano.

QUINTO. Los danos personales se cuantifican tomando como referencia orientativa el sistema de valoracion
del Anexo del texto refundido de la Ley sobre responsabilidad civil y seguro en la circulacion de
vehiculos a motor, sin que dicho sistema resulte de aplicacion directa a este supuesto, y quedan
acreditados en su realidad y alcance por el informe pericial aportado.

SEPTIMO. Con caracter previo a la interposicion de esta demanda, esta parte desarrollo la actividad
negociadora que se acredita con los Documentos n.º 8 y 9, a los efectos del articulo 5 de la Ley
Organica 1/2025, de 2 de enero, y del articulo 264.4.º de la Ley de Enjuiciamiento Civil.
```
Resultado: **PASA**. El bloque de circulacion (arts. 1 y 7 TRLRCSCVM) queda desactivado por completo, incluido el fundamento del art. 9 y el bloque del art. 7.8; el baremo se cita en su formula orientativa y no en la obligatoria; y el bloque del art. 1903 CC se activa solo porque el dano lo causo un dependiente.

---

## Contra-caso — Hecho de hace dos anos sin reclamacion previa

**Mensaje inicial:** "Hace dos anos, en julio de 2024, me cai en la escalera de un edificio comercial por un peldano roto y me lesione la rodilla. Nunca reclame nada porque pensaba que no valia la pena, pero ahora me han dicho que si. Quiero reclamar."

### Recorrido del arbol
```
V1 -> escucha activa: "me cai en la escalera de un
       edificio comercial"                               V1 = otro suceso
V3 -> escucha activa: mismo mensaje                       V3 = caida en establecimiento
FILTRO DE PRESCRIPCION:
       plazo = 1 ano (art. 1968.2 CC)
       hecho: julio de 2024
       actos interruptivos: NINGUNO ("nunca reclame nada")
       -> transcurridos mas de dos anos desde el dies a
       quo mas favorable -> PLAZO AGOTADO -> DETENER
V4 -> se pregunta ANTES de detener, porque V3 = 1 admite
       la calificacion contractual y, si la hubiera, el
       plazo seria de cinco anos (art. 1964.2 CC).
       Respuesta: no habia ningun contrato -> confirmado
       el plazo de un ano -> DETENER
V5 y V6 -> NO se preguntan
```

### Comportamiento esperado
La skill no llega a la Confirmacion, no crea documento y **no pide ningun dato identificativo**. En cuanto calcula que han transcurrido mas de doce meses desde el hecho sin acto interruptivo alguno, formula la unica pregunta que aun podria cambiar el resultado (la naturaleza contractual o extracontractual del vinculo) y, confirmada la respuesta, detiene el flujo en ese mismo turno informando de que:

1. La accion para exigir la responsabilidad civil por las obligaciones derivadas de la culpa o negligencia del art. 1902 CC prescribe por el transcurso de **un ano** desde que lo supo el agraviado (art. 1968.2.º CC).
2. El computo concreto: desde julio de 2024 han transcurrido mas de dos anos sin ningun acto interruptivo de los tres del art. 1973 CC.
3. Que la prescripcion es la primera excepcion que opondra la contraparte, y que **una reclamacion presentada ahora no revive un plazo ya consumido**.
4. Texto fijo de cierre, con la derivacion: "Antes de dar el asunto por perdido conviene que un especialista revise si existe alguna circunstancia que desplace el inicio del computo. Si lo desea, le derivo."

**Resultado: PASA.** La detencion ocurre antes de la Confirmacion y antes de pedir un solo dato de relleno. La unica pregunta que se formula (V4) es la que podria salvar el caso, no una pregunta inutil: si el usuario hubiera respondido que existia un contrato, el plazo habria pasado a cinco anos y el flujo habria continuado.

### Sub-caso de control — plazo a punto de agotarse
Con el mismo relato pero con el hecho fechado el **20/10/2025** y sin reclamacion previa, el filtro devuelve "quedan menos de 60 dias" (vencimiento 20/10/2026). La skill **no** continua con la demanda que el usuario pediria: advierte con prioridad sobre todo lo demas, informa de la fecha de vencimiento y **propone la reclamacion extrajudicial fehaciente como primer documento**, explicando que interrumpe la prescripcion en dias y que la demanda puede prepararse despues con el plazo reiniciado desde cero. **PASA**: la skill anticipa la perdida del derecho en lugar de redactar un escrito que llegaria tarde.

---

## Verificacion en vivo (no solo sobre el papel)

Ademas del recorrido simulado de los cuatro escenarios, se ejecuto realmente el Escenario 1 como lo haria el agente operacional, sin instalar el plugin como skill invocable de Claude Code (no esta registrado en este entorno):

**Punto 2 real.** Se leyeron en vivo contra la API de legislacion consolidada del BOE (`https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{ID}/texto/bloque/{bloque}`, cabecera `Accept: application/xml`, tomando la ULTIMA `<version>` de cada bloque) los articulos 1101, 1103, 1591, 1902, 1903, 1907, 1908, 1964, 1968, 1973 y 1974 del Codigo Civil; 18, 20, 73 y 76 de la LCS; 1, 1 bis, 2, 7, 9, 14 y 49 y el Anexo del TRLRCSCVM; las disposiciones adicional primera y final novena de la Ley 5/2025; 17 y 18 de la LOE; 4, 5, 7 y 9 de la LO 1/2025; y 249, 250 y 264 de la LEC. Se confirmo palabra por palabra el contenido registrado en `references/fuentes-plantillas-validadas.md`, incluidos los literales del art. 76 LCS ("La accion directa es inmune a las excepciones que puedan corresponder al asegurador contra el asegurado"), del art. 1968.2.º CC ("desde que lo supo el agraviado") y del art. 7.8 TRLRCSCVM ("No se admitiran a tramite [...] las demandas en las que no se acompanen los documentos que acrediten la oferta o respuesta motivada").

**Verificaciones que corrigieron una premisa de partida.** Dos hallazgos reales, no cosmeticos:

1. La **disposicion adicional primera de la Ley 5/2025** (seguro obligatorio de VMP) entra en vigor el **02/01/2026**, no el 26/07/2025 como el resto de la ley: lo dice su disposicion final novena, apartado 2. Se registro como frontera de rama en el enrutamiento del `SKILL.md` y se probo con el sub-caso de control del Test 2.
2. El **Anexo del texto consolidado del BOE esta a 25/07/2025** (`fecha_actualizacion` 20250725, modificado por el art. 1.51 de la Ley 5/2025) y **no incorpora las actualizaciones anuales por IPC**. Las cuantias de 2026 estan en la Resolucion de la DGSFP de 03/02/2026 (BOE-A-2026-3803, +2,9 %), verificada tambien en vivo, cuyas tablas se publican en el portal de la DGSFP. De ahi el guardrail 6, que prohibe cifrar con el texto consolidado y prohibe calcular una cuantia aplicando un porcentaje a un importe recordado.

**Puntos 4 y 5 reales.** Se aplico el Punto 4 con `Write` real en `test-local/output/reclamacion-extrajudicial-danos-prueba.md`, `Read` de verificacion, y **tres ciclos de `Edit` incremental** (cuantificacion, dano material y requerimiento) con el `oldString` copiado literalmente del `Read` previo.

Resultado verificado sobre el archivo real, no sobre un extracto manual: **cero comentarios HTML residuales**; los bloques condicionales que aplican insertados como texto plano sin el envoltorio de comentario; los bloques de las demas ramas ausentes por completo (comprobado programaticamente buscando "personal ligero", "Ley 5/2025", "Ley 38/1999", "articulo 1903", "lex artis", "articulo 1101", "articulo 1591" y "videovigilancia": cero coincidencias); y los `Edit` aplicados sin fallos de coincidencia de texto. Los placeholders que persisten tras los `Edit` (`{{nombre_letrado}}`, `{{numero_colegiado}}`, `{{referencia_siniestro}}`, `{{referencia_atestado}}`, `{{documento_1}}`, `{{documento_2}}`, `{{documentos_adicionales}}`) son exactamente los datos que el `SKILL.md` deja para los turnos posteriores del Punto 5, no datos inventados ni omitidos por error. **PASA.**

**Validacion mecanica de los tres assets contra las cuatro reglas de la seccion 4 de la guia.** Ejecutada programaticamente sobre los archivos: cero placeholders con texto de ayuda o lista de opciones embebida (`{{x: a / b}}`), cero placeholders anidados, llaves balanceadas, cero comentarios HTML que envuelvan unicamente un placeholder, cero identificadores en corchete simple (`[DATO]`), cero HTML crudo distinto de los comentarios condicionales, header DRAFT literal presente en los tres, cero usos de `{{DATO_FALTANTE}}`, y saltos duros (dos espacios) en todos los bloques de lineas consecutivas — las unicas lineas consecutivas sin salto duro son items de listas ordenadas markdown (`1.`, `2.`, `3.`), donde el salto lo aporta el propio renderizado de lista. **PASA.**

---

## Verificacion en vivo + calidad LLM (Escenario 1)

Ademas de la verificacion mecanica, se genero el texto real que el agente operativo produciria en los primeros turnos, jugando el papel del LLM gobernado por el `SKILL.md`, para juzgar tono y claridad — no solo que el mecanismo funcione.

### Turnos reales generados

**Turno 1** (mensaje inicial del cliente: el del Test 1)

> **Skill cargada satisfactoriamente.**
>
> Vamos a preparar el escrito que corresponda para reclamar la indemnizacion de los danos que ha sufrido. Antes de redactarlo es necesario precisar algunos datos, y en particular comprobar que la reclamacion esta todavia en plazo.
>
> A su caso corresponde el regimen de responsabilidad civil por los danos causados con motivo de la circulacion de vehiculos a motor, conforme al articulo 1 del texto refundido de la Ley sobre responsabilidad civil y seguro en la circulacion de vehiculos a motor, aprobado por Real Decreto Legislativo 8/2004. Los danos personales se cuantifican obligatoriamente con el sistema de valoracion de su Anexo, en las cuantias del ejercicio 2026. La accion prescribe al ano (articulo 1968.2.º del Codigo Civil y articulo 7.1 del citado texto refundido). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2004-18911
>
> Computando desde el 10 de agosto de 2026, fecha de su alta, el plazo vence el 10 de agosto de 2027. La reclamacion extrajudicial fehaciente interrumpe ese plazo, que vuelve a contarse de cero desde su recepcion (articulo 1973 del Codigo Civil), y constituye la actividad negociadora previa que la ley exige antes de demandar (articulo 5 de la Ley Organica 1/2025).
>
> ¿Que documento desea utilizar como base?
> 1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
> 2. Adjuntar su propio documento

**Turno 2** (cliente: "1")

> He creado el documento en `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/reclamacion-extrajudicial-danos-prueba.md`. ¿Desea que empecemos a completar los datos del escrito?
>
> Comenzamos por sus datos identificativos. Indique su nombre y apellidos completos.

**Turno 3** (cliente: "PERJUDICADO A")

> Indique su DNI.

**Turnos 4-6** (domicilio, telefono y correo, letrado — un dato por turno)

**Turno 7** (cliente responde el ultimo sub-apartado: el letrado)

> Sus datos quedan asi: PERJUDICADO A, DNI 00000000-T, con domicilio en Calle Ejemplo 1, 28001 Ciudad Ejemplo, telefono 600 000 000 y correo perjudicado.a@ejemplo.test, actuando bajo la direccion del Letrado indicado. ¿Confirmamos estos datos?

**Turno 8** (cliente: "si")

> Determinamos ahora a quien debe dirigirse la reclamacion.
>
> Cabe dirigirla unicamente al conductor causante, unicamente a su aseguradora, o a ambos. Dirigirla solo al causante obliga a cobrar contra su patrimonio, con el riesgo de insolvencia. Dirigirla a la aseguradora tiene una ventaja practica decisiva: el articulo 76 de la Ley 50/1980, de Contrato de Seguro, le concede a usted una accion directa que es inmune a las excepciones que la compania pudiera oponer a su propio asegurado, como el impago de la prima o el incumplimiento de los deberes de la poliza. La compania si puede oponerle, en cambio, su culpa exclusiva. Dirigirla a ambos cubre ademas el exceso sobre el limite de la poliza y evita que se quede sin nada si se discutiera la vigencia del seguro.
>
> Le recomiendo dirigirla a ambos. ¿Esta de acuerdo?

### A) Calidad de la respuesta del LLM

- **Tono**: formal, "usted" sostenido, sin coloquialismos ("indique" en vez de "dime", "¿desea...?" en vez de "¿quieres...?"). Cumple.
- **Claridad de la cita normativa**: la Confirmacion dice qué norma aplica, por qué, con enlace verificable y con el plazo traducido a una fecha concreta. No es una cita vacía. Cumple.
- **Directiva de invisibilidad**: ningún turno menciona "V1", "V2", "hoja", "vector", "filtro" ni fases de la instrucción. La línea de carga se emite una sola vez y en el MISMO turno que la ejecución arranca. Cumple.
- **Confirmación agrupada**: la vista previa conjunta llega en el turno 7, POSTERIOR a la respuesta del último sub-apartado, no en el mismo turno en que se pregunta. Cumple.
- **Explicación antes de la decisión de negociación**: el turno 8 explica el régimen y sus consecuencias prácticas, y recomienda, antes de pedir la decisión. No se limita a preguntar "¿a quién se la dirigimos?". Cumple.
- **Cero datos inventados**: la cuantía del baremo no se afirma en el turno 1; se anuncia que se cuantificará con las tablas del ejercicio y la cifra concreta llega en su sección, leída de la tabla.

### B) El asset visto desde el LLM que lo rellena

- Los placeholders son inequívocos y todos con nombre propio. Ninguno lleva texto de ayuda embebido (verificado programáticamente).
- **Punto débil real detectado ahora**: varios placeholders con nombre propio aparecen deliberadamente **dos veces** en el mismo asset porque el dato es el mismo (`{{importe_dano_material}}` en la descripción del daño y en el desglose; `{{importe_total_reclamado}}` en la cuantificación y en el requerimiento). Al aplicar el primer `Edit` del ciclo real, un `oldString` consistente sólo en el placeholder habría sido ambiguo y el `Edit` habría fallado o —peor— el operador podría haber recurrido a `Write`, que la sección 6.3 del `CLAUDE.md` raíz prohíbe expresamente como reacción a un `Edit` fallido. **Fix aplicado**: añadido al `SKILL.md`, Punto 4, un párrafo que enumera los placeholders repetidos de estos assets, obliga a que el `oldString` incluya suficiente texto de contexto para ser único, y advierte de que la persistencia de un placeholder tras el `Edit` de otra sección es el comportamiento esperado y no un fallo.
- **Segundo punto débil detectado y corregido**: el texto fijo de la Confirmación de la HOJA OFERTA contenía un placeholder incrustado dentro de una palabra (`venci{{terminacion_verbal_plazo}}`), que habría producido texto roto en el chat si no se resolvía. **Fix aplicado**: reescrita la frase para que el placeholder quede desnudo y en posición de complemento (`cuyo vencimiento en su caso es el {{fecha_vencimiento_nuevo_plazo}}`).
- El documento, leído de corrido con los datos ya insertados, suena a escrito real de despacho: no hay artefactos de plantilla mal encajada ni frases que delaten un relleno automático.

**Veredicto: PASA con dos correcciones aplicadas.**

---

## Revision UX

Hallazgos:

1. **El filtro de prescripción va antes de todo, y la única pregunta que se permite antes de detener es la que podría salvar el caso.** En el contra-caso, la skill no pide un solo dato identificativo: calcula, formula V4 (contractual o extracontractual) porque es lo único que cambiaría el resultado, y detiene. El usuario recibe la mala noticia en el segundo turno, no después de haber completado un escrito inútil. Y a la inversa: en circulación V4 no se pregunta nunca, porque el plazo es de un año por ley y la pregunta sería ruido.

2. **El estado "quedan menos de 60 días" es más útil que un binario vivo/agotado.** Un plazo técnicamente vivo pero a punto de vencer exige un comportamiento distinto: la skill invierte la petición del usuario y propone la reclamación extrajudicial antes de la demanda, porque interrumpe el plazo en días. Sin ese estado intermedio, la skill habría redactado obedientemente una demanda que llega tarde.

3. **La frontera del 02/01/2026 en la rama de patinetes evita el error más caro de esta materia.** La premisa de partida situaba el seguro obligatorio de VMP en vigor desde el 26/07/2025; la verificación en el BOE lo desplazó al 02/01/2026. Sin esa comprobación, la skill habría afirmado a un cliente con un accidente de noviembre de 2025 que existía una cobertura obligatoria inexistente, y habría cuantificado con un baremo que en su caso es sólo orientativo. Se añadió además la comprobación de los tres requisitos acumulativos del apartado 1 (certificado, inscripción en la DGT y etiqueta), porque la obligación de asegurar no alcanza a todo patinete.

4. **Separar "el baremo es obligatorio" de "el baremo es orientativo" cambia la redacción, no sólo la cifra.** El Test 1 y el Test 3 producen fórmulas distintas y excluyentes en el mismo hueco del documento. Escribir "procede aplicar el baremo" en una caída en supermercado es un error de fondo que un lector técnico detecta de inmediato, y la skill lo previene con un bloque condicional por rama y con un guardrail propio.

5. **La advertencia sobre las grabaciones de videovigilancia se emite en el segundo turno del Test 3, no al final.** Es la prueba más decisiva y la más perecedera de una caída en establecimiento: preguntarlo cuando el escrito ya está redactado no sirve de nada. Se colocó deliberadamente antes de la Confirmación, junto con la pregunta de si se requirió su conservación en su momento.

6. **La sección de posición frente a la oferta motivada explica cuatro cosas antes de pedir la decisión, y ninguna es omitible.** Que aceptar no obliga a renunciar (art. 7.3.d), que se puede aceptar a cuenta, que la exoneración de intereses se limita a lo ofertado y satisfecho (art. 9.a), y que el silencio de tres meses devenga intereses (art. 7.2). Un cliente que decide sin saber esas cuatro cosas no está decidiendo: está firmando.

7. **El requisito de procedibilidad es la primera sección de la HOJA DEMANDA, no la última.** Si no se cumple, todo lo demás es trabajo perdido: la demanda no se admite. En circulación se acumula un segundo requisito (art. 7.8 TRLRCSCVM) y el enrutamiento redirige a la reclamación extrajudicial en lugar de generar una demanda inadmisible. Se recogió también la salida del art. 264.4.º LEC (declaración responsable cuando se desconoce el domicilio del demandado), para no bloquear un caso que la ley sí permite llevar a juicio.

8. **Cinco supuestos de detención por falta de competencia material, no sólo uno.** Responsabilidad penal, responsabilidad patrimonial de la Administración (incluidas la sanidad pública y la vía pública municipal), daños laborales, Consorcio de Compensación de Seguros y producto defectuoso. Las tres primeras son las que un cliente confunde con más facilidad con la vía civil, y detenerse en ellas evita redactar un escrito dirigido a la jurisdicción equivocada.

Ajustes aplicados:

1. Añadido al `SKILL.md`, Punto 4, el párrafo sobre placeholders con nombre propio repetidos y la obligación de que el `oldString` del `Edit` lleve contexto suficiente para ser único (hallazgo del ciclo real de `Edit`).
2. Corregido en el `SKILL.md`, Punto 3, el placeholder incrustado dentro de una palabra en el texto fijo de la Confirmación de la HOJA OFERTA.
3. Registrada en `references/fuentes-plantillas-validadas.md` la fecha real de entrada en vigor de la disposición adicional primera de la Ley 5/2025 (02/01/2026) y la advertencia de que el Anexo del texto consolidado no incorpora las actualizaciones anuales por IPC, con las cinco notas de "verificar manualmente" que la verificación dejó abiertas.

---

## QA en vivo por agente independiente

> Ejecución real (no simulada sobre el papel) del `SKILL.md` por un agente sin contexto previo de la skill.
> Fecha: 03/09/2026. Caso: **ciclista embestido por turismo, esguince cervical, 20 días de baja, bicicleta destrozada, oferta de la aseguradora de 900 euros.**
> Documento generado: `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/rc-qa-prueba.md` (1 `Write` + 9 `Edit` reales, todos con `oldString` copiado del `Read` previo).
> Rama recorrida: V1 = 1 (circulación), V2 = 1 (vehículo a motor), V5 = 2 → **HOJA OFERTA**, asset `assets/respuesta-oferta-motivada.md`.

### Verificación normativa realmente ejecutada (Punto 2)

No se dio por buena ninguna cuantía de memoria. Recorrido real:

1. `BOE-A-2026-3803` (texto y PDF): confirma Resolución DGSFP de 03/02/2026 e IPC de 2025 del **+2,9 %**, pero **no incorpora las tablas**: remite al portal de la DGSFP.
2. `https://dgsfp.mineco.gob.es/es/Regulacion/Paginas/BaremoAutos.aspx` → **HTTP 404**. La raíz del portal no expone el documento de tablas.
3. Búsqueda restringida al dominio oficial → `https://dgsfp.mineco.gob.es/es/Regulacion/DocumentosRegulacion/Tablas Resolución Actualización Baremo 2026.pdf`, del que se extrajo el texto y se **leyeron** los importes:
   - Tabla 3.A, perjuicio personal básico: **39,20 € / día**.
   - Tabla 3.B, pérdida temporal de calidad de vida: muy grave 130,69 €, grave 98,02 €, **moderado 67,96 €**; intervención quirúrgica de 522,76 € a 2.091,05 €.
   - Tabla 2.A.2, 42 años: 1 punto 1.017,26 €; **2 puntos 2.091,95 €**.

Ninguna cifra del documento se obtuvo aplicando el 2,9 % a un importe recordado, que es lo que la skill prohíbe.

### Extractos LITERALES del texto que el agente generó

**Turno 1 — línea de carga, introducción fija y primera pregunta pendiente.** V1 quedó resuelto por Escucha Activa ("un coche me dio un golpe"), así que la primera pregunta emitida fue V2, no V1:

> **Skill cargada satisfactoriamente.**
>
> Vamos a preparar el escrito que corresponda para reclamar la indemnizacion de los danos que ha sufrido. Antes de redactarlo es necesario precisar algunos datos, y en particular comprobar que la reclamacion esta todavia en plazo.
>
> El vehiculo que causo el accidente era:
> 1. Un vehiculo a motor: coche, moto, furgoneta, camion o autobus
> 2. Un vehiculo personal ligero o un patinete electrico

**Turnos 2 a 4 — filtro de prescripción, una pregunta por turno y sin preámbulos:**

> Indique la fecha en que ocurrio el hecho.

> Indique la fecha del alta medica o del informe de estabilizacion de las secuelas, si ya se ha producido.

> Indique si ha remitido alguna reclamacion previa por escrito al responsable o a su aseguradora y, en tal caso, la fecha y el medio empleado.

Respuesta del cliente: *"No he mandado nada por escrito. Me llamaron ellos el 30 de julio y luego me llegó la carta con los 900 euros el 24 de agosto."*

**Turno 6 — Confirmación (Punto 3), con el plazo computado y su dependencia declarada:**

> A su caso corresponde el regimen de responsabilidad civil por los danos causados con motivo de la circulacion de vehiculos a motor, conforme al articulo 1 del texto refundido de la Ley sobre responsabilidad civil y seguro en la circulacion de vehiculos a motor, aprobado por Real Decreto Legislativo 8/2004. Los danos personales se cuantifican obligatoriamente con el sistema de valoracion de su Anexo, en las cuantias del ejercicio 2026. La accion prescribe al ano (articulo 1968.2.º del Codigo Civil y articulo 7.1 del citado texto refundido). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2004-18911
>
> La aseguradora esta obligada a presentar oferta motivada de indemnizacion en el plazo de tres meses desde su reclamacion, o respuesta motivada si no puede ofertar (articulo 7.2 del texto refundido citado). La notificacion fehaciente de una u otra inicia un nuevo plazo de prescripcion de un ano, cuyo vencimiento en su caso es el 24 de agosto de 2027.
>
> Computando desde el alta medica de 18 de agosto de 2026, el plazo del articulo 1968.2.º venceria el 18 de agosto de 2027; si la fecha en que usted conocio el alcance real del dano fuera posterior, el plazo se desplazaria en la misma medida. Su plazo esta vivo y no corre riesgo inmediato.
>
> ¿Que documento desea utilizar como base?
> 1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
> 2. Adjuntar su propio documento

**Turno 12 — posición frente a la oferta (la decisión central de esta hoja), explicada antes de pedirla:**

> Determinamos la posicion que va a adoptar frente a la oferta recibida.
>
> Antes de que decida, conviene que conozca cuatro reglas que condicionan el resultado.
>
> La primera: aceptar no le obliga a renunciar a nada. El articulo 7.3.d) del texto refundido de la Ley sobre responsabilidad civil y seguro en la circulacion de vehiculos a motor impide que el pago se condicione a que usted renuncie a ejercitar acciones futuras. Si junto con el pago le proponen firmar un finiquito o una renuncia total, no lo firme sin que un abogado lo revise.
>
> La segunda: puede cobrar ahora sin conformarse. Cabe aceptar los 900 euros a cuenta de la indemnizacion que en derecho corresponda, sin aceptarlos como liquidacion total y sin renunciar a reclamar la diferencia. Es la opcion mas prudente cuando se discute la valoracion pero no se discute que la cantidad ofrecida es, al menos, un minimo.
>
> La tercera: la oferta presentada en plazo y con el contenido que exige el articulo 7.3 exonera a la aseguradora de los intereses de demora, pero solo respecto de la cantidad ofertada y efectivamente pagada o consignada (articulo 9.a) del mismo texto refundido). La diferencia entre lo ofertado y lo que finalmente se le reconozca sigue devengando el interes del articulo 20 de la Ley 50/1980, de Contrato de Seguro: el interes legal del dinero incrementado en un cincuenta por ciento, con un minimo del veinte por ciento anual transcurridos dos anos desde el siniestro.
>
> La cuarta: en su caso la comunicacion recibida no reune ese contenido, porque expresa una cantidad global sin valoracion separada de los danos personales y de los danos en los bienes y sin entrega del informe medico pericial definitivo. Ese incumplimiento impide a la aseguradora aportar despues en juicio los documentos que no le entrego (articulo 7.3.c)) y hace decaer la exoneracion de intereses.
>
> Su posicion frente a la oferta es:
> 1. Aceptarla en su integridad
> 2. Aceptar el importe a cuenta, sin conformidad con el total y sin renunciar a la diferencia
> 3. Rechazarla y mantener su reclamacion

**Turno 13 — cuantificación partida por partida, con la fuente de cada cifra:**

> Concretamos los motivos de disconformidad, partida por partida.
>
> La discusion con una aseguradora no se gana diciendo que la cifra es baja, sino demostrando partida por partida cual es la que corresponde. En un accidente de circulacion los danos personales se cuantifican obligatoriamente con el sistema de valoracion del Anexo del texto refundido citado (articulo 1.4), y las cuantias aplicables son las del ejercicio del accidente: las de 2026, publicadas por la Resolucion de 3 de febrero de 2026 de la Direccion General de Seguros y Fondos de Pensiones, que aplico sobre las de 2025 el indice general de precios al consumo de ese ano, un 2,9 por ciento. Los danos en los bienes quedan fuera del sistema de valoracion y se indemnizan conforme a los articulos 1902 y siguientes del Codigo Civil.
>
> Conforme al informe de alta que usted me ha facilitado, y leidas las tablas de ese ejercicio, las partidas acreditadas son estas:
>
> - 20 dias de perjuicio personal particular moderado, a 67,96 euros por dia (tabla 3.B): 1.359,20 euros.
> - 12 dias de perjuicio personal basico, a 39,20 euros por dia (tabla 3.A): 470,40 euros.
> - 2 puntos de secuela, en lesionado de 42 anos de edad (tabla 2.A.2): 2.091,95 euros.
>
> El dano personal acreditado suma 3.921,55 euros, frente a los 900 euros que le han ofrecido.
>
> Dos advertencias antes de cerrar la cifra. Una partida sin documento que la respalde no se rebaja: se elimina, porque una sola cantidad no justificada da a la aseguradora el argumento para rechazar el escrito entero. Y si de los hechos resultara que usted contribuyo al dano, la reduccion alcanzaria a todas las partidas y podria llegar al 75 por ciento (articulo 1.2 del texto refundido citado): por eso necesito saber si llevaba casco y si el atestado le atribuye alguna infraccion.
>
> Indique el importe de reparacion o de reposicion de la bicicleta y con que documento lo acredita.

**Turno 15 — partida eliminada por falta de soporte, dicho sin rodeos:**

> Entonces no se incluye partida de lucro cesante. Percibio integra la prestacion de incapacidad temporal y no existe una perdida efectiva de ingresos que pueda acreditar con un documento; reclamarla debilitaria el resto del escrito. Queda constancia de ello en el propio documento.

---

### A) Calidad del texto generado por el agente

**Tono y tratamiento: correcto.** Usted en todos los turnos ("indique", "conviene que conozca", "no lo firme sin que un abogado lo revise"), verbos precisos y ningún coloquialismo. No aparece un solo "vale", "perfecto" ni "genial", ni preámbulos del tipo "para empezar necesito saber". Las preguntas del filtro se emiten desnudas, como exige la Directiva de Invisibilidad.

**Cláusulas de negociación: suficientes para un lego, con una salvedad.** Las cuatro consecuencias de aceptar o rechazar se explican antes de pedir la decisión, en frases cortas y con el efecto económico dicho en euros, no en abstracto. La cuantificación no se limita a dar un total: enseña la tabla, el importe unitario, el número de días y de puntos, y de dónde sale cada uno. **Salvedad honesta:** el `SKILL.md` obliga a explicar cuatro puntos "sin omitir ninguno", y el cuarto (intereses por silencio de tres meses, art. 7.2) era **inaplicable** en este caso, porque sin reclamación del perjudicado ese plazo no llega a iniciarse. Lo sustituí por el incumplimiento del art. 7.3, que sí concurría. La instrucción, tal como está redactada, obliga a decir algo falso o a desviarse de ella.

**Directiva de Invisibilidad: sin fugas.** Ninguna mención a vectores, hojas, fases ni "ahora voy a". La única mecánica visible fue la línea de carga del Punto 0, que está permitida.

**Cero invenciones: verificado como propio fiscal.** Las tres cuantías del baremo se leyeron del PDF oficial de la DGSFP y se comprobaron a mano (20 × 67,96 = 1.359,20; 12 × 39,20 = 470,40; suma con 2.091,95 = 3.921,55; con 890,00 = 4.811,55). El interés legal del dinero **no** se cifró, porque se fija en la Ley de Presupuestos y no se consultó: sólo se enunció la regla del art. 20 LCS. No se citó ninguna sentencia. La única afirmación que puse bajo sospecha propia es la del art. 7.3.c) sobre la imposibilidad de aportar en juicio los documentos no entregados: está en la reference verificada, no en mi memoria.

### B) El asset visto desde el LLM que lo rellena

**Defecto 1 (grave, corregido) — `PRIMERO` daba por hecha una reclamación previa que no existía.** El párrafo era texto fijo: *"Esta parte dirigio a esa entidad reclamacion de la indemnizacion el {{fecha_reclamacion_previa}}, mediante {{medio_reclamacion_previa}}..."*. En el escenario más común de esta materia —la aseguradora abre el expediente con el parte de su asegurado y el atestado, y oferta a la baja sin que el perjudicado haya reclamado— **el asset obliga a afirmar por escrito, ante la aseguradora, un hecho falso**, o a dejar dos placeholders desnudos en un escrito que se envía por burofax. No había ninguna salida prevista. **Corregido:** el párrafo pasa a ser bloque condicional y se añade el bloque alternativo de apertura de expediente sin reclamación previa.

**Defecto 2 (grave, corregido, en el `SKILL.md`) — el filtro de prescripción podía matar un asunto vivo.** El filtro es bloqueante y se ejecuta **antes de V5**, es decir, antes de saber que existe una oferta motivada. Sus tres preguntas cubrían la fecha del hecho, la del alta y las reclamaciones **del perjudicado**, pero no la comunicación **de la aseguradora**. Consecuencia: un accidente de hace catorce meses con oferta motivada notificada hace tres se clasifica como PLAZO AGOTADO y el flujo se detiene, cuando el art. 7.1 TRLRCSCVM abrió un plazo nuevo de un año desde esa notificación. Es un falso negativo que cierra la puerta a un caso perfectamente reclamable. **Corregido:** cuarta pregunta dentro del filtro y regla expresa en el Paso 4 de no declarar prescripción sin haber preguntado por esa comunicación.

**Defecto 3 (de secuencia, resuelto por el anterior) — el Punto 3 pedía un dato que el Punto 5 aún no había recogido.** El texto fijo de la Confirmación de la HOJA OFERTA incluye `{{fecha_vencimiento_nuevo_plazo}}`, pero la fecha de notificación de la oferta sólo se pedía en la sección 3.b del Punto 5, posterior. El operador quedaba ante tres salidas y dos son malas: preguntar fuera de orden, imprimir un placeholder crudo en el chat, o inventar la fecha. Con la pregunta ya dentro del filtro, el dato está disponible cuando la Confirmación lo necesita.

**Defecto 4 (menor, corregido) — aceptar a cuenta sin decir cuánto se reclama.** El bloque de aceptación a cuenta no contenía la cantidad que se sigue reclamando: el escrito salía reservándose "la diferencia" sin decir la diferencia respecto de qué. **Corregido:** el bloque incorpora `{{importe_reclamado}}` y la reserva expresa.

**Defecto 5 (de diseño, corregido en el `SKILL.md`) — placeholder genérico y bloques condicionales para el mismo hueco.** `{{posicion_perjudicado}}`, `{{motivos_disconformidad}}` y `{{solicitudes_escrito}}` van seguidos de los bloques que redactan exactamente ese contenido. El asset no dice si el placeholder se rellena **además** del bloque o **con** el bloque. Rellenar ambos duplica el mismo argumento y delata la plantilla. Mismo patrón en `reclamacion-extrajudicial-danos.md` con `{{fundamento_imputacion}}`. **Corregido:** regla explícita en el Punto 4 de que el bloque sustituye al placeholder.

**Bloque condicional que produce frase forzada (no corregido, se documenta).** El bloque de días y puntos —*"Los dias de perjuicio temporal y los puntos de secuela reconocidos por esa entidad no se corresponden con la documentacion medica..."*— presupone que la aseguradora desglosó. Cuando la oferta es una cifra global, que es la forma habitual de la oferta a la baja, la aseguradora no ha "reconocido" días ni puntos y la frase queda descolocada. Lo omití y cubrí la discrepancia con el bloque de partidas del baremo, que sí encaja. Recomendación para el autor: añadir una variante para oferta sin desglose.

**Numeración: sin huecos, comprobado en el documento real.** El asset no numera hechos: usa rúbricas fijas (PRIMERO a QUINTO), de modo que omitir bloques condicionales no abre huecos. Verificado en el documento generado: cinco rúbricas correlativas, la enumeración interna del QUINTO intacta (1, 2, 3) y los seis documentos numerados de forma continua. Comprobación automática sobre el fichero final: **0 placeholders sin resolver, 0 comentarios HTML, 0 corchetes simples**.

**Fricción menor de la relación de documentos.** El asset ofrece `{{documento_1}}`, `{{documento_2}}` y un cajón de sastre `{{documentos_adicionales}}` en el que el operador tiene que escribir a mano "Documento n.º 3 — ...", con su propio formato y sus propios saltos de línea. Funciona, pero la numeración correlativa queda a cargo del operador justo en el punto donde un error es más visible.

**Redundancia de plantilla.** El párrafo de entrada y el segundo párrafo de PRIMERO afirman lo mismo (fecha de recepción y naturaleza de la comunicación). Se nota levemente al leer de corrido; no llega a defecto.

**¿Suena a escrito jurídico real?** Sí. Leído de corrido, el documento se sostiene: antecedentes, posición, disconformidad partida por partida con tabla y precepto, solicitudes y advertencias de plazo. El punto que más lo delataría —el desglose— es precisamente el mejor, porque las cifras son reales y trazables.

### C) Punto crítico: cuantías fijas del baremo en el asset

**Verificado: no hay ninguna cuantía del baremo escrita en `respuesta-oferta-motivada.md`.** El único importe fijo del asset es la cobertura mínima del seguro de vehículos personales ligeros, que es de ley y no del baremo, y aparece en el `SKILL.md`, no en la plantilla. Las cuantías se resuelven en el turno correspondiente citando `{{ejercicio_baremo}}` y `{{resolucion_dgsfp}}`. La obligación de verificar en cada lanzamiento está en el Punto 2.3, en el guardrail 6 y en el apartado 5 de la reference. **Cumple.**

**Pero la verificación es más frágil de lo que la skill supone, y conviene decirlo.** La Resolución del BOE **no contiene las tablas**; el `SKILL.md` sólo registra la raíz `https://dgsfp.mineco.gob.es/`, y la ruta previsible del portal devuelve 404. Sin la búsqueda restringida al dominio oficial que localizó el PDF, el operador habría caído en el fallback del Punto 2.6 y habría dejado el daño personal sin cifrar en un caso en el que la cifra es todo el asunto. Recomendación: registrar en `fuentes-plantillas-validadas.md` la URL directa del documento de tablas del ejercicio.

### Correcciones aplicadas en esta pasada

| Archivo | Corrección |
|---|---|
| `assets/respuesta-oferta-motivada.md` | `PRIMERO` convertido en bloques condicionales, con bloque nuevo para expediente abierto sin reclamación previa del perjudicado |
| `assets/respuesta-oferta-motivada.md` | El bloque de aceptación a cuenta incorpora la cantidad que se sigue reclamando y la reserva expresa de la diferencia |
| `SKILL.md`, Punto 1, filtro, Paso 2 | Cuarta pregunta obligatoria sobre la comunicación de la aseguradora y su fecha, dentro del filtro |
| `SKILL.md`, Punto 1, filtro, Paso 4 | Prohibición de declarar plazo agotado sin haber preguntado por esa comunicación y sin aplicar el nuevo plazo del art. 7.1 TRLRCSCVM |
| `SKILL.md`, Punto 1, V5 | Reformulada la opción 2 y la descripción del vector: dejan de presuponer una reclamación previa del perjudicado |
| `SKILL.md`, Punto 4 | Regla nueva: un bloque condicional **sustituye** al placeholder genérico de contenido de su sección, no se suma a él |
| `SKILL.md`, Punto 5, HOJA OFERTA, sección 3.a | Contempla la ausencia de reclamación previa, indica qué bloque activar y qué explicar sobre el plazo del art. 7.2 |

**Veredicto: PASA con cinco correcciones aplicadas y dos recomendaciones abiertas** (variante del bloque de días y puntos para ofertas sin desglose; registro de la URL directa de las tablas del ejercicio).
