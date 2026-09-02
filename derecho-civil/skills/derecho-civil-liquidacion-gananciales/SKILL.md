---
name: derecho-civil-liquidacion-gananciales
description: >
  Genera los documentos para liquidar la sociedad de gananciales conforme a los Arts. 1392 y 1396 a 1410 del
  Codigo Civil y a los Arts. 806 a 810 de la LEC, verificados en el BOE: (1) CON ACUERDO — convenio de
  liquidacion con la estructura de inventario, avaluo, liquidacion y adjudicaciones, que puede documentarse de
  forma autonoma, elevarse a escritura publica si hay inmuebles, o integrarse en el convenio regulador del
  divorcio (Art. 90.1.e) CC); y (2) SIN ACUERDO — propuesta de inventario del Art. 808.2 LEC y solicitud
  judicial de formacion de inventario ante el juzgado del proceso matrimonial (Arts. 807 y 808 LEC). Explica la
  presuncion de ganancialidad del Art. 1361 CC, los reintegros entre masas del Art. 1358 CC, el efecto real de
  adjudicar una vivienda hipotecada y el exceso de adjudicacion. NO usar en regimen de separacion de bienes (no
  hay masa comun que liquidar), en regimen de participacion (Art. 811 LEC, cauce distinto), en regimenes de
  derecho civil propio o foral, ni cuando haya empresa familiar, sociedades, patrimonio en el extranjero, deudas
  con Hacienda o la Seguridad Social o indicios de ocultacion de bienes: en esos casos se detiene y escala.
when_to_use: |
  - El usuario se esta divorciando o separando y necesita repartir los bienes y deudas del matrimonio.
  - El usuario ya esta divorciado y la sociedad de gananciales sigue sin liquidar.
  - El usuario pide un convenio de liquidacion de gananciales, un inventario de bienes gananciales o una
    solicitud judicial de formacion de inventario.
  - El usuario discute con su conyuge si un bien concreto es privativo o ganancial.
  - El usuario aporto dinero propio (una herencia, una donacion, ahorros anteriores) a un bien comun, o al
    contrario, y quiere recuperarlo en el reparto.
  - El usuario quiere quedarse la vivienda familiar hipotecada, o que se la quede el otro conyuge.
inputs:
  - regimen: sociedad de gananciales / separacion de bienes / participacion / desconocido
  - acuerdo: existe acuerdo sobre el inventario y el reparto / no existe acuerdo
  - momento: liquidacion unida a un proceso matrimonial en curso / posterior a una resolucion ya firme
  - vivienda_hipotecada: existe vivienda familiar con prestamo hipotecario pendiente (si / no)
  - datos_conyuges: nombre, NIF y domicilio de cada conyuge
  - datos_matrimonio: fecha y lugar de celebracion, registro civil, origen del regimen
  - disolucion: estado (ya disuelta / en curso / no disuelta), y fecha y causa de la disolucion o fecha de referencia del inventario (Arts. 1392 y 1397.1.º CC)
  - datos_proceso_matrimonial: juzgado, clase de procedimiento, numero de autos, fecha de admision o de firmeza
  - activo: relacion de bienes gananciales con su valor, y creditos de la sociedad contra un conyuge
  - pasivo: deudas pendientes a cargo de la sociedad, y reintegros debidos a cada conyuge con su actualizacion
  - bienes_discutidos: bienes cuyo caracter privativo o ganancial se discute, y prueba disponible de cada uno
  - datos_vivienda: direccion, datos registrales, referencia catastral, valor, entidad acreedora y saldo pendiente
  - adjudicaciones: bienes que se adjudican a cada conyuge y su valor
  - compensacion: importe, forma y medio de pago del exceso de adjudicacion, si lo hay
  - documentos: documentos justificativos de cada partida del inventario
  - postulacion: procurador y letrado, en la via judicial
outputs:
  - convenio_liquidacion_gananciales: convenio de liquidacion en markdown, DRAFT
  - propuesta_inventario: propuesta de inventario del Art. 808.2 LEC en markdown, DRAFT
  - solicitud_formacion_inventario: solicitud judicial de formacion de inventario en markdown, DRAFT
references:
  - references/cc-activo-pasivo-y-presuncion.md
  - references/cc-liquidacion-division-adjudicacion.md
  - references/lec-procedimiento-liquidacion-806-811.md
  - references/vivienda-hipotecada-y-exceso-adjudicacion.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/convenio-liquidacion-gananciales.md
  - assets/propuesta-inventario.md
  - assets/solicitud-formacion-inventario.md
---

# Liquidacion de la Sociedad de Gananciales

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija del Punto 1 y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificacion normativa interna (Punto 2), ejecutala en silencio y continua hasta la primera pregunta o hasta la Confirmacion visible del Punto 3, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

Esta linea es, junto con la introduccion fija, la UNICA excepcion a la prohibicion de mencionar la mecanica interna. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, la validacion de presupuestos, la verificacion normativa y la creacion base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol.
- Resumenes de validacion con checks (ej. "Regimen: ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez, en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin. No afirma todavia que norma ni que cauce aplica, porque eso depende de una clasificacion aun no resuelta:

"Vamos a proceder a la preparacion de los documentos necesarios para repartir el patrimonio comun de su matrimonio. Para determinar correctamente el cauce que corresponde a su caso, es necesario precisar antes algunos datos."

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:

- **V1 (Acuerdo):** existe acuerdo entre los conyuges sobre el inventario y el reparto / no existe acuerdo.
- **V2 (Momento):** la liquidacion va unida a un proceso de nulidad, separacion o divorcio en curso / es posterior a una resolucion matrimonial ya firme.
- **V3 (Vivienda hipotecada):** existe vivienda familiar con prestamo hipotecario pendiente / no existe.
- **V4 (Regimen economico):** sociedad de gananciales / separacion de bienes / regimen de participacion.

**Vector de guarda (no se pregunta como tal): derecho civil propio o foral.** Si en cualquier momento del flujo aparece que el matrimonio esta sujeto al derecho civil propio de Cataluna, Aragon, Navarra, Baleares, Pais Vasco o Galicia (por la vecindad civil de los conyuges o por capitulaciones sujetas a esa norma), aplica de inmediato el guardrail correspondiente: detener y escalar. Los Arts. 1344 a 1410 del Codigo Civil no son aplicables a esos regimenes.

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto (omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama). **El orden empieza por el regimen economico porque es el unico vector que puede dejar el caso enteramente fuera de alcance**: preguntarlo primero evita que el cliente invierta turnos en un flujo que no le corresponde.

* Para V4 (pregunta principal):
  "El regimen economico de su matrimonio era:
  1. Sociedad de gananciales
  2. Otro regimen distinto de la sociedad de gananciales
  3. No lo sabe con certeza"

* Para V4 (sub-pregunta, solo si la respuesta principal es 2):
  "El regimen distinto de gananciales es:
  1. Separacion de bienes
  2. Regimen de participacion"

* Para V4 (sub-pregunta, solo si la respuesta principal es 3):
  "Respecto de las capitulaciones matrimoniales:
  1. No otorgamos capitulaciones matrimoniales
  2. Si las otorgamos, pero no recuerdo su contenido"

* Para el vector de guarda (solo si la respuesta a la sub-pregunta anterior es 1, antes de aplicar el regimen legal supletorio):
  "Al casarse, la vecindad civil de ambos conyuges era:
  1. Comun (territorio de Codigo Civil)
  2. De Cataluna, Aragon, Navarra, Baleares, Pais Vasco o Galicia
  3. No lo sabe"

* Para V1:
  "Respecto del reparto del patrimonio comun:
  1. Existe acuerdo con su conyuge sobre que bienes y deudas hay y como repartirlos
  2. No existe acuerdo"

* Para V2:
  "La liquidacion se plantea:
  1. Dentro de un proceso de separacion o divorcio que esta en tramite
  2. Despues de una sentencia de separacion o divorcio que ya es firme"

* Para V3:
  "Respecto de la vivienda familiar:
  1. Existe vivienda familiar con un prestamo hipotecario todavia pendiente de pago
  2. No existe vivienda familiar, o existe pero sin prestamo hipotecario pendiente"

**PRINCIPIO: Preguntas simples, no mega-preguntas.** Cada pregunta resuelve un unico punto de decision. No comprimas V1 y V2 en una sola pregunta, ni pidas el regimen y el acuerdo a la vez.

**Resolucion de V4 cuando el cliente no lo sabe.** Si la respuesta a la sub-pregunta de capitulaciones es 1 (no las otorgaron) y la respuesta del vector de guarda es 1 (vecindad civil comun), resuelve **V4 = sociedad de gananciales** e informa de por que, con el texto fijo: "A falta de capitulaciones matrimoniales, el regimen economico de su matrimonio es el de sociedad de gananciales, que el Codigo Civil establece como regimen legal supletorio en su articulo 1316." Si la respuesta del vector de guarda es 2, aplica el guardrail de derecho civil propio: detener y escalar. Si es 3, no des por supuesto el regimen: explica que el regimen supletorio depende de la vecindad civil de los conyuges al casarse y pide que lo verifique en su certificacion literal de matrimonio o en las capitulaciones antes de continuar; no crees ningun documento con el regimen sin resolver. Si la respuesta a la sub-pregunta de capitulaciones es 2 (las otorgaron pero no recuerda el contenido), pide que aporte copia de las capitulaciones y no continues sin conocer el regimen pactado.

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V4 = separacion de bienes → **DETENER**: en el regimen de separacion de bienes no existe masa comun de bienes y derechos (Art. 1435 CC), por lo que **no hay sociedad que liquidar** y el procedimiento de los Arts. 806 y siguientes de la LEC no es aplicable. Explicarlo con el texto fijo del Punto 3 para este supuesto, informar de que si existen bienes adquiridos por ambos en proindiviso su reparto es una division de cosa comun (Arts. 400 y siguientes del Codigo Civil) y no una liquidacion de regimen, y ofrecer escalacion. **No crear ningun documento.**
- Si V4 = regimen de participacion → **DETENER**: el regimen de participacion se liquida por el Art. 811 de la LEC, cuya propuesta exige una estimacion del patrimonio inicial y final de cada conyuge, no un inventario de masa comun. Los assets de esta skill no sirven para ese cauce. Advertir y escalar. **No crear ningun documento.**
- Si concurre el vector de guarda de derecho civil propio o foral → **DETENER**: verificar la norma autonomica aplicable y escalar. **No crear ningun documento.**
- Si V4 = gananciales y V1 = 1 (acuerdo) → **HOJA CONVENIO**: `assets/convenio-liquidacion-gananciales.md`. V2 determina el bloque condicional de eficacia (integracion en el proceso matrimonial en curso, o convenio autonomo) y V3 el bloque condicional de la vivienda hipotecada.
- Si V4 = gananciales y V1 = 2 (sin acuerdo) → **HOJA JUDICIAL**: dos documentos, en este orden: primero `assets/propuesta-inventario.md` (es el contenido sustantivo y la propuesta que el Art. 808.2 LEC exige acompanar) y despues `assets/solicitud-formacion-inventario.md` (el escrito procesal, que se remite a la propuesta). V2 determina el bloque condicional del hecho tercero de la solicitud y V3 el tratamiento de la vivienda dentro del inventario.
- Si V1 = 2 pero el cliente manifiesta que aun no ha intentado el acuerdo → antes de enrutar a la HOJA JUDICIAL, aplica la explicacion de la seccion de dialogo previo descrita mas abajo: no se le impone el acuerdo, pero se le informa del coste real de la via judicial. Si tras la explicacion decide intentar el acuerdo, reenruta a la HOJA CONVENIO.
- Si el usuario pide unicamente la propuesta de inventario como documento de trabajo para remitirsela a su conyuge o a su abogado, sin escrito judicial → generar solo `assets/propuesta-inventario.md`, sin la solicitud.

### Validacion de presupuestos (interno, antes del Punto 3)

- **Estado de la disolucion (Art. 1392 CC), en las dos hojas — distinguir tres situaciones y NO confundirlas.** La causa de disolucion es la disolucion del matrimonio, la declaracion de nulidad, la separacion legal o el pacto de otro regimen en capitulaciones.
  1. **Sociedad ya disuelta** (resolucion matrimonial firme, o capitulaciones ya otorgadas): confirmar la fecha y la causa, y activar en el asset los bloques de disolucion ya producida y de fecha de corte.
  2. **Disolucion en curso** (demanda matrimonial admitida a tramite, aun sin resolucion firme): **la sociedad NO esta todavia disuelta, y eso no impide continuar.** El Art. 808.1 LEC permite expresamente solicitar la formacion de inventario "admitida la demanda de nulidad, separacion o divorcio", es decir, **antes de que la disolucion se produzca**; y en la via de acuerdo, la liquidacion se pacta como extremo del convenio regulador y despliega su eficacia con la aprobacion judicial (Art. 90.1.e) CC). Activar los bloques condicionales de disolucion en curso y de fecha de referencia. **PROHIBIDO escribir que la sociedad "quedo disuelta" cuando aun no lo esta**, y prohibido decirle al cliente que debe esperar a la sentencia para pedir el inventario. Advertir, en cambio, de que **la segunda fase, la solicitud de liquidacion del Art. 810.1 LEC, si exige que sea firme la resolucion que declare disuelto el regimen**: el inventario puede formarse antes, la division no.
  3. **Solo separacion de hecho, sin demanda matrimonial presentada ni capitulaciones:** la sociedad sigue vigente y no hay cauce. Informar de que para liquidarla hace falta antes disolverla (demanda de separacion o divorcio, o capitulaciones pactando otro regimen), **no crear ningun documento** y ofrecer derivacion a `derecho-civil-divorcio`.
- **Fecha de corte o de referencia del inventario (Art. 1397.1.º CC), en las dos hojas.** Si la sociedad ya esta disuelta, fijar la fecha de disolucion como fecha de corte y advertir de que los bienes adquiridos y las deudas contraidas despues no entran en el inventario; si el cliente pretende inventariar un bien posterior, explicarlo y no incluirlo. Si la disolucion esta en curso, fijar una fecha de referencia expresa, advertir de que el activo lo determinara el momento de la disolucion y recoger el compromiso de actualizar el inventario si media alguna alteracion relevante.
- **Presupuesto temporal del Art. 808.1 LEC (HOJA JUDICIAL).** Confirmar que la demanda matrimonial esta admitida a tramite o que el proceso de disolucion esta iniciado. Si el cliente aun no ha presentado ninguna demanda matrimonial y no hay resolucion firme, la solicitud de inventario es prematura: advertirlo y derivar a `derecho-civil-divorcio`. Si el divorcio ya es firme, aplicar la posicion conservadora del punto 1 del apartado "Verificar manualmente" de `references/fuentes-plantillas-validadas.md`: tramitar ante el juzgado que conocio del divorcio y advertir al cliente de que conviene confirmar el criterio del juzgado antes de presentar. **Nunca afirmar que el Art. 808.1 contempla literalmente el supuesto de sentencia ya firme.**
- **Competencia (Art. 807 LEC, HOJA JUDICIAL).** Es competente el juzgado que esta conociendo, ha conocido o hubiera tenido la competencia para conocer del proceso matrimonial. **No hay eleccion de fuero ni sumision posible:** nunca preguntar al cliente en que juzgado desea presentarlo; preguntar cual conocio o esta conociendo de su proceso matrimonial. Si el proceso se siguio ante un Juzgado de Violencia sobre la Mujer, concurren por definicion los presupuestos del guardrail de violencia del plugin: detener y escalar.
- **Masa comun con contenido (Art. 806 LEC), en las dos hojas.** Si tras recorrer el inventario resulta que no existe ningun bien ni deuda ganancial, no hay nada que liquidar: informarlo y no generar un documento vacio.
- **Pasivo superior al activo, en las dos hojas.** Si el pasivo inventariado supera al activo, no hay remanente que dividir conforme al Art. 1404 CC. Advertirlo expresamente, activar el bloque condicional correspondiente del asset y tratar la contribucion de cada conyuge al deficit. **Nunca escribir un haber negativo como si fuera un reparto ordinario.**
- **Supuestos de escalacion patrimonial, en las dos hojas.** Si el inventario incluye empresa familiar, participaciones en sociedades, explotacion economica en funcionamiento o patrimonio situado en el extranjero, detener y escalar antes de valorar esas partidas. Si existen deudas con la Agencia Tributaria o con la Tesoreria General de la Seguridad Social, detener y escalar: su tratamiento en la liquidacion y la responsabilidad de cada conyuge exigen analisis especializado. Si el cliente manifiesta indicios de que el otro conyuge ha ocultado, distraido o enajenado bienes, detener y escalar: la partida del Art. 1397.2.º CC y las medidas de aseguramiento exigen estrategia procesal propia.
- **Documentacion de las partidas (Art. 808.2 LEC, HOJA JUDICIAL).** Cada partida de la propuesta necesita su documento justificativo. Al recorrer el inventario, preguntar por el documento de cada partida y advertir expresamente de las que queden sin justificacion documental. No presentar como acreditada una partida que no lo esta.
- **Prueba del caracter privativo (Art. 1361 CC), en las dos hojas.** Nunca escribir que un bien es privativo por la sola afirmacion del cliente. Preguntar con que documentacion lo acredita y, si no la hay, advertir de que la presuncion de ganancialidad opera contra su pretension y que la carga de la prueba le corresponde.

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del Codigo Civil (arts. 1315 a 1435) y de la LEC (arts. 806 a 811).

**2.2 — Consultar la fuente oficial vigente.** La API de legislacion consolidada del BOE devuelve el bloque de un articulo concreto (requiere cabecera `Accept: application/xml`). **La redaccion vigente es la ULTIMA `<version>` del bloque devuelto:**
```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero}
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a{numero}
```
El Codigo Civil (BOE-A-1889-4763) usa bloques `artNNNN`; la LEC (BOE-A-2000-323) usa `aNNN`.

Consultar siempre:
- Del Codigo Civil: 1316 (regimen supletorio), 1346 y 1347 (privativos y gananciales), 1354, 1356, 1357 (precio aplazado y vivienda familiar), 1358 (reintegros), 1359 (mejoras), **1361 (presuncion de ganancialidad)**, 1362 a 1368 y 1373 (cargas y responsabilidad), **1392 (disolucion)**, 1397 y 1398 (activo y pasivo), 1399 a 1410 (liquidacion, division y adjudicacion) y, en la rama de detencion, 1411 (participacion) y 1435 (separacion de bienes).
- De la LEC: **806, 807, 808, 809, 810 y 811**. Los arts. **807, 808 y 810 estan en la redaccion de la Ley Organica 2/2022, de 21 de marzo (BOE-A-2022-4516), en vigor desde el 23/03/2022**: es una redaccion reciente y su verificacion en cada lanzamiento es OBLIGATORIA, sin excepcion.

**2.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar `Write`/`Edit` para:
- Actualizar `references/cc-activo-pasivo-y-presuncion.md`, `references/cc-liquidacion-division-adjudicacion.md`, `references/lec-procedimiento-liquidacion-806-811.md` y/o `references/vivienda-hipotecada-y-exceso-adjudicacion.md` con la redaccion vigente.
- Si cambia la estructura legal exigida a la propuesta de inventario (Art. 808.2) o a la de liquidacion (Art. 810.2), actualizar los assets afectados.
- Actualizar las tablas "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**2.5 — Verificar el modelo normalizado del CGPJ.** Comprobar en https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/ si se ha publicado un modelo normalizado para la solicitud de formacion de inventario o para la liquidacion del regimen economico matrimonial. **Verificado el 02/09/2026: no existe.** Si apareciera, actualizar `references/fuentes-plantillas-validadas.md` y adaptar el asset al modelo oficial.

**2.6 — Fallback si la fuente no es accesible.** Si la lectura falla (error HTTP, timeout):
```
web_search("liquidacion sociedad gananciales articulos 1392 1397 1398 1404 Codigo Civil texto consolidado BOE")
web_search("articulos 806 807 808 809 810 LEC liquidacion regimen economico matrimonial texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del Codigo Civil y de la Ley de Enjuiciamiento Civil en el BOE. El documento se genera con la version de referencia. Verifique manualmente antes de firmarlo o presentarlo."

**Prohibido dar por vigente lo que no se ha podido verificar.**

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa el cauce y la fuente aplicable.** Textos fijos por hoja:
   - CONVENIO: "A su caso corresponde la liquidacion de la sociedad de gananciales de mutuo acuerdo, que se rige por los articulos 1392 y 1396 a 1410 del Codigo Civil. El articulo 806 de la Ley 1/2000, de Enjuiciamiento Civil, reserva el procedimiento judicial para el caso de falta de acuerdo entre los conyuges, de modo que, existiendo acuerdo, no es necesario acudir a el. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - JUDICIAL: "A su caso corresponde el procedimiento de liquidacion del regimen economico matrimonial de los articulos 806 a 810 de la Ley 1/2000, de Enjuiciamiento Civil, que se desarrolla en dos fases sucesivas: primero la formacion del inventario y despues la liquidacion y division. La solicitud de formacion de inventario debe acompanarse de una propuesta con las partidas debidamente separadas y de los documentos que las justifiquen, conforme al articulo 808.2 de dicha ley. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - En la HOJA JUDICIAL, anadir: "Los articulos 807, 808 y 810 de la Ley de Enjuiciamiento Civil se encuentran en la redaccion dada por la Ley Organica 2/2022, de 21 de marzo, vigente desde el 23 de marzo de 2022, que ha sido la verificada."
   - En la HOJA JUDICIAL, si V2 = 1 (proceso matrimonial en curso), anadir: "No es necesario esperar a la sentencia para iniciar esta primera fase: el articulo 808.1 de la Ley de Enjuiciamiento Civil permite solicitar la formacion de inventario desde que la demanda de separacion o divorcio ha sido admitida a tramite. Lo que si requiere que la resolucion sea firme es la segunda fase, la solicitud de liquidacion y division del articulo 810.1 de la misma ley."
   - En la HOJA CONVENIO, si V2 = 1 (proceso matrimonial en curso), anadir: "Al encontrarse su proceso matrimonial en tramite, la liquidacion puede incorporarse al convenio regulador como uno de sus extremos, conforme al articulo 90.1.e) del Codigo Civil."
   - En la HOJA CONVENIO, si el inventario comprende inmuebles, anadir: "Si el inventario comprende bienes inmuebles, el convenio debera elevarse a escritura publica notarial para poder inscribir las adjudicaciones en el Registro de la Propiedad."
   - **Texto fijo de DETENCION por separacion de bienes** (V4 = separacion de bienes; se emite en lugar de todo lo anterior y no se ofrece plantilla ni se crea documento): "En el regimen de separacion de bienes no existe una masa comun de bienes y derechos, por lo que no hay sociedad conyugal que liquidar: cada conyuge conserva la titularidad de lo que le pertenece, conforme al articulo 1435 del Codigo Civil, y el procedimiento de los articulos 806 y siguientes de la Ley de Enjuiciamiento Civil no le resulta aplicable, pues ese articulo lo circunscribe a los regimenes que determinan la existencia de una masa comun. Si durante el matrimonio adquirieron bienes conjuntamente, esos bienes les pertenecen en proindiviso y su reparto se articula como una division de cosa comun de los articulos 400 y siguientes del Codigo Civil, que es una operacion distinta. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - **Texto fijo de DETENCION por regimen de participacion** (V4 = participacion): "El regimen de participacion no se liquida mediante el inventario de una masa comun, porque no existe tal masa: en el, cada conyuge conserva su propio patrimonio y lo que se liquida es un derecho de credito a participar en las ganancias del otro, conforme al articulo 1411 del Codigo Civil. Su liquidacion se rige por el articulo 811 de la Ley de Enjuiciamiento Civil y exige una propuesta con la estimacion del patrimonio inicial y final de cada conyuge, de contenido distinto al de las plantillas de que disponemos. Le recomiendo la intervencion de un abogado especializado. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
2. **Ofrece la plantilla o pide el documento propio.** Solo si la hoja no es de detencion. En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio. Si el documento adjuntado contiene una clausula que afirma la liberacion de un conyuge frente a la entidad acreedora, o un reparto distinto de la mitad sin compensacion, adviertelo expresamente antes de continuar.

### Dialogo previo sobre la via cuando no se ha intentado el acuerdo

Si V1 = 2 (sin acuerdo) y el cliente no ha intentado realmente negociar, antes de crear los documentos judiciales explicaselo con este contenido (redactalo con tus palabras, en registro formal, sin listas numeradas ni mecanica interna): el procedimiento judicial se desarrolla en dos fases sucesivas —primero se determina que bienes y deudas componen la masa comun, y solo despues se reparte—; cada fase tiene su comparecencia, su posible juicio verbal o su nombramiento de contador y peritos, y su propia via de recurso; los plazos de diez dias que fija la ley son los de senalamiento por el Letrado de la Administracion de Justicia, no la duracion del procedimiento, que en la practica se mide en meses o anos; y el coste del contador y de los peritos recae sobre la propia masa a repartir. Anade que el acuerdo, cuando es posible, se documenta en semanas y deja el reparto en manos de los conyuges en lugar de en las de un contador. Termina preguntando si desea intentar el acuerdo antes o prefiere preparar ya la via judicial. **No presiones ni condiciones la continuacion a que acepte negociar:** informado el cliente, respeta su decision.

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento:

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa e investigacion: incluida `fecha_verificacion_normas` del Punto 2). Los faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{fecha_disolucion}}`, `{{saldo_pendiente_hipoteca}}`); usa un marcador generico solo para un hueco suelto sin placeholder propio, y nunca repitas el mismo marcador generico dos veces en el mismo documento (`Edit` necesita un `oldString` unico).
3. Utiliza `Write` para guardar el archivo en disco (nombre en `snake_case.md`, ej. `convenio_liquidacion_gananciales_conyuge_a.md`, `propuesta_inventario_conyuge_a.md`, `solicitud_formacion_inventario_conyuge_a.md`).
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. En esa MISMA respuesta, sin turno intermedio y sin preguntar si desea empezar, emite el anuncio fijo de la primera seccion y formula ya su primera pregunta, para que el flujo no se detenga (regla del `CLAUDE.md` raiz, seccion 6.1, punto 5, y coherencia con el Punto 0: la skill esta en ejecucion desde que se carga).

Los bloques condicionales del asset que dependan de decisiones aun no tomadas se OMITEN en este `Write` y se insertan durante el Punto 5, releyendo el asset y copiando el bloque **sin el envoltorio de comentario**. Se omiten tambien en este `Write`, aunque su condicion ya este resuelta por Escucha Activa, los bloques de las clausulas de negociacion que el Punto 5 obliga a explicar antes de redactar —vivienda hipotecada, exceso de adjudicacion y reintegros entre masas—: esos se insertan en su turno, despues de la explicacion y de la confirmacion del cliente. Que el cliente haya mencionado la hipoteca en su primer mensaje no autoriza a escribir la clausula de la vivienda antes de haberle explicado que la adjudicacion no le libera frente a la entidad. El documento escrito en disco no contiene ningun comentario HTML en ningun momento.

**Orden en la HOJA JUDICIAL (dos documentos).** Crea y completa PRIMERO la propuesta de inventario entera (lista 5-B). Solo cuando la propuesta quede cerrada, crea la solicitud de formacion de inventario (que se remite a la propuesta) y completa su lista 5-C, reutilizando sin volver a preguntar todos los datos ya recogidos.

### Resolucion de la numeracion dinamica (OBLIGATORIO)

Varios apartados y documentos de los assets solo existen si se cumple su condicion. Sus ordinales y numeros **no son texto fijo**, son placeholders que debes resolver contando unicamente los apartados efectivamente presentes en el documento en ese momento. Nunca dejes un salto en la numeracion ni un placeholder de ordinal sin resolver.

- `{{letra_partida_creditos_sociedad}}` (activo, Arts. 1397.3.º CC): vale **B** si el bloque de bienes enajenados por negocio fraudulento (Art. 1397.2.º) NO se ha insertado, y **C** si si se ha insertado.
- `{{letra_partida_creditos_conyuges}}` (pasivo, Art. 1398.3.ª CC): vale **B** si el bloque de bienes privativos gastados en interes de la sociedad (Art. 1398.2.ª) NO se ha insertado, y **C** si si se ha insertado.
- `{{numero_clausula_vivienda}}`, `{{numero_clausula_exceso}}`, `{{numero_clausula_deudas}}`, `{{numero_clausula_finiquito}}`, `{{numero_clausula_gastos}}` y `{{numero_clausula_eficacia}}` (convenio): se resuelven como el ordinal en letras (QUINTA, SEXTA, SEPTIMA...) que corresponda a la posicion real de esa clausula entre las que estan efectivamente presentes. Las clausulas PRIMERA a CUARTA existen siempre. La de vivienda solo si V3 = 1; la de exceso solo si hay exceso de adjudicacion. Como las secciones se recorren en el orden fijo de la lista 5-A, al llegar al turno de cada clausula ya sabes cuantas la preceden: resuelvela en ese momento y **no renumeres clausulas ya escritas**.
- `{{numero_documento_sentencia}}`, `{{numero_documento_propuesta}}` y los numeros de la relacion final de documentos: **numeracion UNICA y compartida por los dos documentos de la HOJA JUDICIAL**, porque la propuesta es ella misma uno de los documentos que acompanan a la solicitud y sus justificantes se aportan en el mismo escrito. El nº 1 es siempre el poder, el nº 2 la certificacion de matrimonio, y a continuacion, en el orden en que se citan en los hechos, el testimonio de la sentencia si procede, la propia propuesta de inventario y despues sus justificantes. **Reserva los numeros de la propuesta y de sus justificantes ANTES de empezar a citarlos**, y no los cites dentro de la propuesta hasta haber fijado en que numero empiezan: asi se evita tener que renumerar despues.
- **Nunca renumeres documentos ya escritos mediante una sustitucion masiva de texto.** Si un numero cambia, corrigelo cita por cita con `Edit`, verificando cada una: una sustitucion global de "Documento nº 8" por "Documento nº 9" corrompe las citas que mencionan dos documentos seguidos (convierte "Documentos nº 8 y nº 9" en "Documentos nº 9 y nº 9"). Tras cualquier ajuste de numeracion, releer el documento y comprobar que la relacion final y las citas del cuerpo coinciden una a una.
- `{{ordinal_hecho_administracion}}` (solicitud): el ordinal en letras del hecho (SEXTO, SEPTIMO...) segun cuantos hechos le precedan efectivamente, contando que el bloque de bienes de caracter discutido puede no existir.
- `{{ordinal_otrosi_documentacion}}` (solicitud): "OTROSI PRIMERO" si el otrosi de medida de aseguramiento no se ha insertado, "OTROSI SEGUNDO" si si.

## 5. EDICION INCREMENTAL DE SECCIONES

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas de negociacion se explican y se confirman una a una. **La vista previa y la confirmacion agrupada de una parte se emiten en el turno SIGUIENTE a la respuesta del ultimo sub-apartado, nunca en el mismo turno en que aun se esta preguntando ese ultimo dato**: primero se pregunta y se recibe la respuesta, y solo despues, en el turno posterior, se muestra la vista previa conjunta y se pide la confirmacion.

**Validacion de sentido, no solo de formato.** Eres un LLM, no un formulario. Antes de escribir una respuesta en el documento, razona si tiene sentido: una fecha de disolucion anterior a la del matrimonio, un valor de vivienda de 300 euros, un saldo hipotecario superior al importe inicial del prestamo, un total de adjudicaciones que no cuadra con el haber, o unos bienes gananciales adquiridos despues de la fecha de corte no se escriben: senala por que no encaja y pide aclaracion.

**Aritmetica: la haces tu, los datos los aporta el cliente.** Los totales, las diferencias, el haber liquido, la mitad de cada conyuge y el exceso de adjudicacion los calculas y los muestras en la vista previa, sin pedirselos al cliente. Pero **nunca estimes ni inventes un valor de partida**: si el cliente no aporta el valor de un bien o el saldo de una deuda, esa partida queda con su placeholder y se advierte de que sin ella el haber no puede cerrarse. Sigue el guion de operaciones de `references/cc-liquidacion-division-adjudicacion.md`, apartado 6.

**Cuadre al centimo en los importes fraccionados.** Cuando un importe se reparta en varios pagos, en varias partidas o entre dos lotes y la division no sea exacta, **la suma de las fracciones tiene que coincidir exactamente con el total, al centimo**. Ajusta la diferencia en el primer pago o partida (p. ej. 70.000 euros en tres plazos son 23.333,34 + 23.333,33 + 23.333,33, nunca tres de 23.333,33, que suman 69.999,99) y verifica la suma antes de mostrar la vista previa. Un documento patrimonial cuyos importes no suman el total es un documento defectuoso.

### Secciones — HOJA CONVENIO (`convenio-liquidacion-gananciales.md`)

1. **Primer conyuge** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de ambos conyuges." Sub-apartados, uno por turno: a) nombre completo; b) NIF; c) domicilio. Al recibir la respuesta al ultimo, vista previa unica y una sola confirmacion antes del `Edit`.
2. **Segundo conyuge** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Identificado el primer conyuge, pasamos al segundo." Sub-apartados: a) nombre completo; b) NIF; c) domicilio. Confirmacion agrupada.
3. **Matrimonio y disolucion de la sociedad** *(dato objetivo con validacion)*. Anuncio fijo: "Pasamos a los datos del matrimonio y a la disolucion de la sociedad de gananciales." Sub-apartados, uno por turno: a) fecha y lugar de celebracion; b) registro civil de inscripcion; c) origen del regimen (por defecto legal a falta de capitulaciones, o por capitulaciones que lo pactaron); d) segun V2, fecha y causa de la disolucion ya producida, o fecha de admision de la demanda matrimonial y fecha de referencia del inventario si la disolucion esta en curso. Aplica la validacion del estado de la disolucion en sus tres situaciones: si la sociedad ya esta disuelta, informa de que la fecha de disolucion es la fecha de corte del inventario (Art. 1397.1.º CC) y de que lo adquirido despues no entra; si la disolucion esta en curso, activa los bloques condicionales correspondientes y explica que el inventario se formula con una fecha de referencia sujeta a actualizacion; si solo hay separacion de hecho sin demanda ni capitulaciones, detente.
4. **Activo: bienes gananciales** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos ahora al inventario del activo: los bienes y derechos comunes." Explica antes de pedir la relacion, con base en `references/cc-activo-pasivo-y-presuncion.md`: que son gananciales los bienes obtenidos por el trabajo de cualquiera de ellos, los frutos y rentas tanto de los bienes comunes como de los privativos y lo adquirido a titulo oneroso a costa del caudal comun (Art. 1347 CC); que son privativos los anteriores al matrimonio, los recibidos por herencia o donacion y los adquiridos a costa de privativos (Art. 1346 CC); y **que el punto de partida legal es el articulo 1361 del Codigo Civil: se presumen gananciales todos los bienes existentes en el matrimonio mientras no se pruebe que pertenecen privativamente a uno de los dos, de modo que quien sostenga que un bien es suyo debe probarlo, y que la escritura este a su nombre no basta por si solo.** Despues pide los bienes **uno por turno**: descripcion y valor. En los inmuebles, pide tambien datos registrales y referencia catastral. Por cada bien cuyo caracter pueda discutirse, pregunta con que documentacion se acredita y, si no la hay, advierte de que la presuncion opera en contra. Si concurre alguno de los supuestos especiales, aplicalo y explicalo: vivienda familiar comprada a plazos antes del matrimonio (Art. 1357, parrafo 2.º, y Art. 1354: cotitularidad pro indiviso, no privativa sin mas), bien comprado a plazos durante el matrimonio (Art. 1356: decide el primer desembolso), o mejora en bien privativo pagada con fondos comunes (Art. 1359: el credito es el aumento de valor, no el coste).
5. **Activo: creditos de la sociedad contra un conyuge** *(clausula de negociacion — explicar antes de decidir; condicional)*. Anuncio fijo: "Determinamos si la sociedad tiene algun credito frente a uno de ustedes." Explica el Art. 1397.3.º CC: si la sociedad pago con dinero comun algo que era de cargo de uno solo (la hipoteca de un piso privativo, una deuda personal, una mejora en un bien privativo), la sociedad tiene un credito contra el, que entra en el activo por su importe **actualizado** al tiempo de la liquidacion. Pregunta si concurre algun supuesto y, por cada uno, concepto, importe original, criterio de actualizacion e importe resultante. Si no hay ninguno, omite el bloque sin dejar rastro.
6. **Pasivo: deudas pendientes a cargo de la sociedad** *(dato objetivo con validacion)*. Anuncio fijo: "Pasamos al pasivo: las deudas pendientes a cargo de la sociedad." Pide las deudas una por turno: concepto, acreedor y **saldo pendiente a una fecha concreta**. En el prestamo hipotecario, exige el saldo certificado por la entidad, no el importe inicial del prestamo ni una estimacion. Recuerda que son de cargo de la sociedad los gastos del Art. 1362 CC.
7. **Pasivo: reintegros y reembolsos a favor de un conyuge** *(clausula de negociacion — explicar antes de decidir; la seccion que mas dinero mueve)*. Anuncio fijo: "Corresponde ahora determinar los reintegros que la sociedad deba a cada uno de ustedes." **Esta seccion no se omite nunca por silencio del cliente: el cliente no la conoce y no la va a mencionar por su cuenta, de modo que hay que preguntarla activamente.** Explica antes de preguntar, con base en `references/cc-activo-pasivo-y-presuncion.md`, apartado 4: que el articulo 1358 del Codigo Civil establece que, cuando una masa paga lo que corresponde a la otra, hay que reembolsar el valor satisfecho **por su importe actualizado al tiempo de la liquidacion**, no por la cifra nominal de entonces; que funciona en los dos sentidos; que el reintegro no convierte al aportante en propietario de una cuota mayor del bien, sino en acreedor; y que hay que poder acreditarlo documentalmente. Despues pregunta expresamente, en turnos separados: a) si alguno de ustedes aporto dinero propio —de una herencia, de una donacion o de ahorros anteriores al matrimonio— a la compra, la entrada, la hipoteca o la reforma de un bien comun, y con que documentacion puede acreditarlo; b) si alguno pago con dinero propio deudas o gastos que eran de cargo de la sociedad (Art. 1364 CC). Por cada reintegro reconocido: concepto, importe original, criterio de actualizacion pactado e importe resultante. Si el cliente no puede acreditar una aportacion, adviertele de que sin justificacion documental el reintegro es una pretension discutible y registra el dato solo si ambos conyuges lo reconocen expresamente en el convenio.
8. **Liquidacion y haber de cada conyuge** *(dato objetivo calculado — no se pregunta, se muestra)*. Anuncio fijo: "Con el inventario cerrado, procedemos a la liquidacion y a la determinacion del haber de cada uno." No pidas ninguna cifra nueva: calcula el total del activo, el total del pasivo, el haber liquido y la mitad de cada conyuge (Arts. 1344 y 1404 CC), aplica las compensaciones del Art. 1403 CC por reintegros y creditos, y muestra la operacion completa paso a paso en la vista previa para que el cliente pueda comprobarla. Al escribir el bloque del Art. 1403 en el documento, **suprime los sumandos cuyo importe sea cero en lugar de escribir "0 euros"**: si un conyuge no tiene reintegros a su favor ni creditos de la sociedad en su contra, se hace constar asi en una frase, no con una enumeracion de ceros. Explica que **la division por mitad es el resultado legal y no un punto negociable**: si un conyuge quiere ceder valor al otro, eso es un negocio distinto (una donacion) con su propio tratamiento, y debes advertirlo. Si el pasivo supera el activo, aplica la validacion correspondiente y trata la contribucion al deficit.
9. **Vivienda familiar y prestamo hipotecario** *(clausula de negociacion — explicar antes de decidir; solo si V3 = 1)*. Anuncio fijo: "Abordamos ahora la vivienda familiar y el prestamo hipotecario que la grava." **Explica PRIMERO, y confirma que el cliente lo ha entendido, antes de escribir cualquier clausula**, con base en `references/vivienda-hipotecada-y-exceso-adjudicacion.md`: que adjudicar la vivienda a uno de los conyuges **no libera al otro frente al banco**; que la entidad no firma el convenio, no es parte en el y no queda vinculada por lo que ambos pacten; que si firmaron el prestamo los dos, los dos siguen obligados frente a ella y puede reclamar a cualquiera de los dos con independencia de quien se quede la casa; que lo que si produce el convenio es un efecto interno, la obligacion del adjudicatario de pagar y de mantener indemne al otro, con accion de repeticion si este acaba pagando (Arts. 1367 y 1401 CC); y que **la unica forma de liberar de verdad al otro conyuge es que la entidad lo acepte mediante una novacion subjetiva del prestamo, decision que corresponde solo a la entidad y que puede denegar.** Solo despues pide, en turnos separados: a) direccion, datos registrales y referencia catastral; b) valor atribuido de comun acuerdo; c) entidad acreedora y datos de la escritura de prestamo; d) saldo pendiente certificado y su fecha; e) quienes figuran como prestatarios en la escritura de prestamo; f) a quien se adjudica la vivienda; g) si ya se ha consultado a la entidad la novacion subjetiva y cual fue su respuesta. **Esta PROHIBIDO redactar una clausula que afirme que el conyuge no adjudicatario queda liberado frente a la entidad.** Usa siempre la estructura del asset: asuncion interna, obligacion de mantener indemne, compromiso de solicitar la novacion y advertencia expresa de que la liberacion depende de la entidad.
10. **Adjudicaciones** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos al reparto: la adjudicacion concreta de los bienes a cada uno de ustedes." Explica antes de preguntar: que se procura la igualdad de los lotes (Art. 1410 CC, por remision a la particion de herencia); que cada conyuge tiene derecho a que se incluyan con preferencia en su haber sus bienes de uso personal, la explotacion economica que gestione efectivamente y el local donde ejerza su profesion (Art. 1406 CC); y **que la preferencia legal sobre la vivienda habitual del Art. 1406.4.º opera solo en caso de fallecimiento del otro conyuge, no en el divorcio: en un divorcio ningun conyuge tiene derecho legal preferente a que se le adjudique la vivienda familiar.** No afirmes nunca lo contrario. Advierte tambien de que la atribucion del **uso** de la vivienda es una medida del divorcio (Art. 96 CC), distinta de la adjudicacion de la **propiedad** que aqui se decide. Despues pide bien por bien, en turnos separados, a quien se adjudica, y ve mostrando el valor acumulado de cada lote frente al haber de cada uno. **Un lote se valora NETO de la deuda pendiente que su titular asume y que grava un bien de ese lote**: el valor que se contrasta con el haber es el de los bienes adjudicados menos esa deuda, no el valor bruto del bien. Adjudicar una vivienda de 240.000 euros con 80.000 euros de hipoteca pendiente que el adjudicatario asume supone un lote de 160.000 euros, no de 240.000. Escribe siempre las dos cifras en el documento —valor de los bienes y valor neto tras deducir la deuda asumida— para que la operacion sea verificable, y comprueba que la suma de los valores netos de los dos lotes coincide con la suma de los totales a percibir de la clausula tercera.
11. **Exceso de adjudicacion y compensacion** *(clausula de negociacion — explicar antes de decidir; condicional)*. Anuncio fijo: "Comprobamos si el reparto produce un exceso de adjudicacion que deba compensarse." Calcula tu mismo si el valor **neto** de un lote —el de los bienes adjudicados menos la deuda pendiente que su titular asume y que los grava— supera el total a percibir por su titular segun la clausula tercera. **Nunca compares el valor bruto de los bienes con el haber: en una vivienda hipotecada eso multiplica el exceso y arruina el reparto.** Si no hay exceso, informalo y omite la clausula sin dejar rastro. Si lo hay: explica el Art. 1407 CC (quien recibe mas de su haber abona la diferencia en dinero) y su causa habitual, la indivisibilidad de la vivienda; **advierte de que el exceso puede tener consecuencias fiscales, que su tratamiento depende de la normativa estatal y autonomica aplicable y de si el exceso resulta o no inevitable por la indivisibilidad del bien, y que debe consultarse con un asesor fiscal antes de firmar**; y expon las alternativas del cuadro de `references/vivienda-hipotecada-y-exceso-adjudicacion.md`, apartado 3 (compensacion en metalico, asuncion de mas deuda, adjudicacion de otros bienes, venta del inmueble y reparto del precio, o mantener la copropiedad temporalmente, advirtiendo de que esto ultimo solo aplaza el conflicto a una futura division de cosa comun). Despues pide, en turnos separados: importe de la compensacion (calculado por ti, a confirmar por el cliente), forma de pago y medio de pago. **Si el pago se aplaza, advierte expresamente al conyuge acreedor de que la clausula de finiquito declara liquidada la sociedad y de que, sin garantia, su unico respaldo es una accion de reclamacion frente a un obligado que ya ha recibido el bien**, y pregunta si desean pactar alguna garantia (condicion resolutoria expresa inscribible sobre el inmueble adjudicado, aval, prenda o vencimiento anticipado por impago de un plazo). Si el cliente la quiere, recogela en la clausula; si no, dejalo constar y no la inventes. **PROHIBIDO cuantificar el impuesto, citar tipos o exenciones, o afirmar que la operacion esta exenta.**
12. **Reparto de las deudas pendientes** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Corresponde ahora el reparto interno de las deudas pendientes." Explica, con la misma logica que en la vivienda, que el reparto pactado rige entre ellos pero **no vincula a los acreedores, que conservan sus creditos frente al conyuge deudor** (Arts. 1401 y 1402 CC), y que quien pague algo que segun el convenio correspondia al otro podra repetir contra el. Pregunta el reparto deuda por deuda. Si aparece una deuda con la Agencia Tributaria o con la Seguridad Social, aplica el guardrail: detener y escalar.
13. **Gastos e impuestos del convenio** *(clausula de negociacion)*. Anuncio fijo: "Determinamos como se reparten los gastos e impuestos derivados de este convenio." Explica que el pacto no altera las normas imperativas que determinan el sujeto pasivo de cada tributo. Pregunta el reparto (por mitad por defecto).
14. **Eficacia y formalizacion** *(dato objetivo con explicacion)*. Anuncio fijo: "Cerramos determinando como se formalizara el convenio." Segun V2 y el contenido del inventario, activa los bloques que correspondan: si el proceso matrimonial esta en curso, el sometimiento a aprobacion judicial como extremo del convenio regulador (Art. 90.1.e) CC); si es autonomo, la eficacia entre las partes desde la firma; y si el inventario comprende inmuebles, el compromiso de elevacion a escritura publica, preguntando el plazo. Si el cliente aun no tiene convenio regulador y su proceso matrimonial esta en curso, informale de que las demas medidas del divorcio (custodia, alimentos, uso de la vivienda, pension compensatoria) se documentan en el convenio regulador y ofrece derivacion a `derecho-civil-divorcio`: esta skill cubre solo la parte patrimonial.
15. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Por ultimo, el lugar y la fecha de la firma." Lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA JUDICIAL, documento 1: propuesta de inventario (`propuesta-inventario.md`)

1. **Conyuge solicitante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por su identificacion como parte solicitante." Sub-apartados: a) nombre completo; b) NIF; c) domicilio. Confirmacion agrupada. Si el solicitante es heredero de un conyuge fallecido, pide ademas los datos del conyuge fallecido, la fecha del fallecimiento y el titulo que acredita la condicion de heredero, y activa el bloque condicional correspondiente (legitimacion del Art. 808.1 LEC en la redaccion de la LO 2/2022).
2. **Conyuge contrario** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion del otro conyuge." Sub-apartados: a) nombre completo; b) NIF; c) domicilio. Confirmacion agrupada.
3. **Matrimonio y disolucion** *(dato objetivo con validacion)*. Igual que la seccion 3 de la HOJA CONVENIO, con el mismo anuncio y las mismas validaciones de disolucion previa y fecha de corte.
4. **Activo: bienes gananciales** *(clausula de negociacion — explicar antes de decidir)*. Igual que la seccion 4 de la HOJA CONVENIO, con una diferencia esencial: aqui la propuesta se presenta frente a un conyuge que discute, de modo que por cada partida hay que recoger tambien **el documento que la justifica** (Art. 808.2, parrafo segundo, LEC) y advertir de las que queden sin justificacion.
5. **Activo: bienes enajenados por negocio ilegal o fraudulento** *(clausula de negociacion — condicional)*. Anuncio fijo: "Determinamos si algun bien comun fue enajenado de forma irregular y debe reintegrarse a la masa." Explica el Art. 1397.2.º CC: si un bien comun fue enajenado mediante negocio ilegal o fraudulento y no se ha recuperado, su valor actualizado se incluye en el activo. Advierte de que esta partida exige documentacion de la enajenacion y de su valor, y de que **no puede calificarse de fraudulenta la conducta del otro conyuge sin base documental**. Si el cliente manifiesta indicios de ocultacion o distraccion de bienes, aplica el guardrail: detener y escalar antes de redactar la partida. Si no concurre el supuesto, omite el bloque sin dejar rastro.
6. **Activo: creditos de la sociedad contra un conyuge** *(clausula de negociacion)*. Igual que la seccion 5 de la HOJA CONVENIO, anadiendo el documento justificativo de cada partida.
7. **Pasivo: deudas pendientes a cargo de la sociedad** *(dato objetivo con validacion)*. Igual que la seccion 6 de la HOJA CONVENIO, anadiendo el documento justificativo de cada deuda.
8. **Pasivo: reintegros y reembolsos** *(clausula de negociacion — explicar antes de decidir)*. Igual que la seccion 7 de la HOJA CONVENIO, con la misma obligacion de preguntarla activamente, anadiendo el documento justificativo de cada reintegro. Aqui la exigencia probatoria es mayor: sin acuerdo del otro conyuge, un reintegro no documentado sera rechazado en la comparecencia.
9. **Partidas controvertidas** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Identificamos ahora las partidas que previsiblemente seran discutidas." Explica el Art. 809.2 LEC: si en la comparecencia se suscita controversia sobre la inclusion o exclusion de una partida o sobre su importe, el procedimiento continua por los tramites del juicio verbal y se resuelve por sentencia. Explica de nuevo la presuncion del Art. 1361 CC y, sobre todo, **quien tiene la carga de la prueba**: el conyuge que sostiene el caracter privativo de un bien debe probarlo, y en defecto de prueba el bien queda en el activo ganancial. Por cada bien discutido pregunta, en turnos separados: descripcion, caracter que le atribuye la parte contraria, motivo concreto por el que esta parte lo incluye en el activo, y prueba disponible. Aplica la regla de estilo de `references/estilo-redaccion-escritos.md`: no dar por pacifica la naturaleza de un bien discutido, y expresar el motivo concreto de la calificacion, no una formula generica.
10. **Documentos justificativos** *(dato objetivo con validacion)*. Anuncio fijo: "Relacionamos los documentos que justifican cada partida del inventario." Recorre las partidas ya recogidas y confirma el documento de cada una, numerandolos correlativamente. Advierte expresamente de las partidas que queden sin documento y de la debilidad que eso supone ante la comparecencia. Recuerda tambien la consecuencia del Art. 809.1 LEC: **la incomparecencia injustificada de un conyuge le tiene por conforme con la propuesta del que si comparece**, en ambos sentidos.
11. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos la propuesta con el lugar y la fecha."

### Secciones — HOJA JUDICIAL, documento 2: solicitud de formacion de inventario (`solicitud-formacion-inventario.md`)

Al crear este documento, vuelca sin volver a preguntar todos los datos ya recogidos en la propuesta (conyuges, matrimonio, disolucion, bienes discutidos).

1. **Juzgado competente y proceso matrimonial** *(dato objetivo con explicacion)*. Anuncio fijo: "Pasamos al escrito judicial: determinamos primero el juzgado competente." Explica el Art. 807 LEC: es competente el Juzgado de Primera Instancia que esta conociendo, ha conocido o hubiera tenido la competencia para conocer del proceso de nulidad, separacion o divorcio, **sin que sea posible elegir otro fuero ni someterse expresa o tacitamente a un juzgado distinto**. No preguntes en que juzgado desea presentarlo. Pregunta, en turnos separados: a) que juzgado conocio o esta conociendo de su proceso matrimonial; b) clase de procedimiento y numero de autos; c) segun V2, fecha de admision a tramite de la demanda matrimonial, o fecha de la sentencia y de su firmeza. Activa el bloque condicional del hecho tercero que corresponda a V2. Si V2 = 2, advierte de la posicion conservadora sobre el cauce recogida en `references/fuentes-plantillas-validadas.md`, punto 1 de "Verificar manualmente": conviene confirmar el criterio del juzgado antes de presentar.
2. **Falta de acuerdo** *(dato objetivo)*. Anuncio fijo: "Concretamos en que ha consistido la falta de acuerdo." Pregunta brevemente en que puntos no ha sido posible el acuerdo. Aplica la regla de estilo: se describe el desacuerdo patrimonial de forma objetiva, **no se narra el conflicto conyugal ni se formulan reproches**. Redacta el hecho en una o dos frases.
3. **Bienes de caracter discutido** *(dato objetivo, condicional)*. Anuncio fijo: "Trasladamos al escrito los bienes cuyo caracter se discute." Ya resuelto en la propuesta: vuelca la informacion sin volver a preguntarla y activa el bloque condicional con la invocacion del Art. 1361 CC y su carga de la prueba. Si no habia bienes discutidos, omite el bloque.
4. **Medidas sobre administracion y disposicion de los bienes** *(clausula de negociacion — condicional)*. Anuncio fijo: "Valoramos si conviene pedir al Juzgado que resuelva sobre la administracion y disposicion de los bienes comunes." Explica el Art. 809.1, parrafo cuarto, LEC: el Tribunal resuelve lo procedente sobre administracion y disposicion de los bienes inventariados el mismo dia de la comparecencia o el siguiente. Pregunta si existe riesgo concreto sobre algun bien comun (que se venda, se grave o se vacie una cuenta) y en que consiste. Si no hay riesgo concreto, omite el bloque: **no formules una peticion generica de medidas sin justificacion**.
5. **Otrosi de aseguramiento** *(clausula de negociacion — condicional)*. Anuncio fijo: "Valoramos si procede solicitar alguna medida de aseguramiento." Solo si de la seccion anterior resulta un riesgo concreto y acreditable. Pregunta la medida que se interesa y su justificacion. Si el riesgo es serio o requiere medidas cautelares, escala: la estrategia cautelar excede el alcance de esta skill.
6. **Otrosi de requerimiento de documentacion economica** *(clausula de negociacion — condicional)*. Anuncio fijo: "Valoramos si es necesario que el Juzgado requiera documentacion a la parte contraria." Pregunta si hay documentacion economica necesaria para determinar las partidas que obra en poder del otro conyuge y a la que esta parte no tiene acceso. Pide la descripcion concreta de esa documentacion: **rechaza una peticion generica del tipo "toda su documentacion bancaria"**, y pide que concrete entidad, periodo y concepto.
7. **Representacion procesal** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Corresponde identificar la representacion procesal." Sub-apartados: a) nombre del procurador; b) nombre del letrado. Confirmacion agrupada. Trata abogado y procurador como preceptivos y redacta el fundamento de postulacion en consecuencia (ver punto 7 de "Verificar manualmente" en `references/fuentes-plantillas-validadas.md`). Si el cliente pregunta si puede comparecer por si mismo, indicale que lo confirme con su abogado o en el propio juzgado; **no afirmes que puede hacerlo**. Si aun no estan designados, cada uno queda con su propio placeholder del asset, nunca ambos con el mismo marcador generico.
8. **Documentos, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con la relacion de documentos, el lugar y la fecha." Numera los documentos correlativamente (nº 1 poder, nº 2 certificacion de matrimonio, y a continuacion los demas en el orden en que se citan en los hechos, incluida la propuesta de inventario y sus justificantes). Lugar de firma; fecha del dia salvo indicacion en contrario.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: separacion estricta entre activo y pasivo, cada partida numerada con su valor y su documento, operaciones de liquidacion completas y verificables, precision terminologica entre disolucion y liquidacion y entre reintegro y compensacion por exceso, HECHOS numerados con una idea por apartado, sin narrar el conflicto conyugal, y SUPLICO ajustado a lo estrictamente pedido.

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5 (y, en la HOJA JUDICIAL, tras completar AMBOS documentos), muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una clausula o seccion existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

## Guardrails

1. Verificar siempre el Codigo Civil y la LEC en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder. **Los arts. 807, 808 y 810 LEC estan en la redaccion de la LO 2/2022 (vigencia 23/03/2022) y su verificacion en cada lanzamiento es obligatoria.**
2. Si se detecta una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar. No usar una version desactualizada.
3. **Separacion de bienes → DETENER.** En el regimen de separacion de bienes no hay masa comun y no hay sociedad que liquidar (Arts. 1435 CC y 806 LEC). Explicarlo, informar de que el reparto de bienes en proindiviso es una division de cosa comun (Arts. 400 y ss. CC) y no crear documento de liquidacion.
4. **Regimen de participacion → DETENER.** Se liquida por el Art. 811 LEC, con propuesta de estimacion de patrimonio inicial y final de cada conyuge. Los assets de esta skill no sirven. Advertir y escalar.
5. **Derecho civil propio o foral → DETENER.** Cataluna, Aragon, Navarra, Baleares, Pais Vasco y Galicia tienen regimenes economicos matrimoniales propios con reglas de composicion y liquidacion distintas. Verificar la norma autonomica y escalar. Nunca aplicar los Arts. 1344 a 1410 CC a un matrimonio sujeto a derecho civil propio.
6. **La separacion de hecho no disuelve la sociedad de gananciales** (Art. 1392 CC). Si no hay demanda matrimonial presentada ni capitulaciones, no hay cauce: informar, derivar a `derecho-civil-divorcio` o a capitulaciones y no crear el documento. **En cambio, la disolucion ya en curso no es obstaculo:** el Art. 808.1 LEC permite pedir la formacion de inventario con la demanda matrimonial ya admitida, antes de que la disolucion se produzca, y solo la segunda fase, la solicitud de liquidacion del Art. 810.1 LEC, exige que sea firme la resolucion que declare disuelto el regimen. Nunca escribir que la sociedad "quedo disuelta" cuando aun no lo esta, ni decir al cliente que debe esperar a la sentencia para pedir el inventario.
7. **La adjudicacion de un bien hipotecado NO libera al otro conyuge frente a la entidad acreedora** (Arts. 1367 y 1401 CC). Explicarlo siempre antes de redactar la clausula y confirmar que el cliente lo ha entendido. **PROHIBIDO redactar una clausula que afirme esa liberacion.** Solo cabe la asuncion interna del pago, la obligacion de mantener indemne al otro y el compromiso de solicitar de la entidad la novacion subjetiva, cuya eficacia depende del consentimiento de la entidad.
8. **El remanente se divide por mitad** (Arts. 1344 y 1404 CC). La mitad es el resultado legal de la division, no un punto negociable. Un reparto desigual sin compensacion es un negocio distinto (donacion) con su propio tratamiento: advertirlo y no redactarlo como si fuera una liquidacion ordinaria.
9. **La presuncion de ganancialidad del Art. 1361 CC opera siempre.** Nunca calificar un bien de privativo por la sola afirmacion del cliente: preguntar por la documentacion que lo acredita y, en su defecto, advertir de que la carga de la prueba le corresponde y de que el bien quedara en el activo comun.
10. **Los reintegros del Art. 1358 CC se expresan por su importe actualizado al tiempo de la liquidacion**, con el criterio de actualizacion explicito en el documento. Nunca escribir un reintegro por su valor nominal historico sin advertirlo, ni inventar un criterio de actualizacion que las partes no hayan pactado.
11. **La preferencia sobre la vivienda habitual del Art. 1406.4.º CC opera solo en caso de fallecimiento del otro conyuge**, no en el divorcio. Nunca decirle a un cliente divorciado que la ley le da preferencia sobre la vivienda familiar. La atribucion del **uso** de la vivienda es una medida del divorcio (Art. 96 CC), distinta de la adjudicacion de la **propiedad**.
12. **Fiscalidad: advertir sin cuantificar.** El exceso de adjudicacion puede tener coste fiscal y su tratamiento depende de la normativa estatal y autonomica y de si el exceso es inevitable por la indivisibilidad del bien. **PROHIBIDO citar tipos, exenciones o articulos tributarios, cuantificar el impuesto o afirmar que la operacion esta exenta.** Remitir siempre a asesor fiscal antes de la firma.
13. **La competencia del Art. 807 LEC no es elegible.** Nunca preguntar en que juzgado desea presentarlo ni admitir sumision a otro fuero.
14. **Cada partida de la propuesta necesita su documento justificativo** (Art. 808.2 LEC). Advertir expresamente de las partidas sin justificacion y no presentarlas como acreditadas.
15. **La fecha de disolucion es la fecha de corte del inventario** (Art. 1397.1.º CC). No inventariar bienes adquiridos ni deudas contraidas despues de esa fecha.
16. **No estimar valores.** El avaluo lo aportan los conyuges o un peritaje. La skill calcula la aritmetica, pero nunca estima ni inventa el valor de un inmueble, de una empresa, de un vehiculo ni el saldo de una deuda: esas partidas conservan su placeholder.
17. Nunca inventar datos, cuantias, fechas, numeros de protocolo, datos registrales ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}` con el nombre propio del placeholder del asset.
18. **Indicios de violencia de genero o domestica → DETENER SIEMPRE y escalar**, conforme al guardrail del plugin. Si el proceso matrimonial se siguio ante un Juzgado de Violencia sobre la Mujer (Art. 807 LEC), concurren por definicion esos presupuestos.
19. El documento escrito en disco no contiene ningun comentario HTML. Los bloques condicionales se insertan sin su envoltorio de comentario, y los ordinales y numeros de documento de los bloques condicionales se resuelven en el momento de insertarlos, sin dejar saltos en la numeracion.

## Como NO se usa esta skill

- No usar en regimen de separacion de bienes: no hay masa comun que liquidar (Guardrail 3). Si lo que se quiere es repartir un bien adquirido por ambos en proindiviso, eso es una division de cosa comun de los Arts. 400 y siguientes del Codigo Civil, que esta skill no cubre.
- No usar en regimen de participacion: cauce distinto del Art. 811 LEC (Guardrail 4).
- No usar en matrimonios sujetos a derecho civil propio o foral (Guardrail 5).
- No usar para tramitar el divorcio o la separacion en si, ni para las medidas personales (custodia, visitas, alimentos, uso de la vivienda, pension compensatoria): derivar a `derecho-civil-divorcio`. Esta skill cubre exclusivamente la parte patrimonial y es la que debe usarse cuando la liquidacion del regimen tiene contenido real; el convenio regulador se limita a incorporarla como uno de sus extremos (Art. 90.1.e) CC).
- No usar para modificar medidas ya acordadas: derivar a `derecho-civil-modificacion-medidas` si existe en el marketplace.
- No usar para ejecutar un convenio de liquidacion incumplido ni para reclamar una compensacion pactada y no pagada: derivar a `derecho-civil-ejecucion-titulos`.
- No usar para liquidar la sociedad de gananciales por fallecimiento de un conyuge dentro de una particion de herencia: derivar a `derecho-civil-herencia`, cuyo cuaderno particional incorpora la liquidacion previa de gananciales como operacion antecedente.
- No usar para valorar una empresa familiar, participaciones sociales o una explotacion economica en funcionamiento: escalar.
- No usar cuando haya patrimonio situado en el extranjero: escalar.
- No usar cuando existan deudas con la Agencia Tributaria o con la Tesoreria General de la Seguridad Social: escalar.
- No usar cuando haya indicios de que un conyuge ha ocultado o distraido bienes: escalar.
- No usar para calcular la tributacion de la operacion ni para planificacion fiscal: derivar a asesor fiscal.
- No usar si el usuario pide opinion juridica sobre la estrategia del reparto o sobre sus posibilidades en el pleito: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Regimen de separacion de bienes | Detener: no hay masa comun que liquidar (Arts. 1435 CC y 806 LEC). Explicar la diferencia con la division de cosa comun y ofrecer escalacion. No crear documento |
| Regimen de participacion | Detener: cauce del Art. 811 LEC, con propuesta de patrimonio inicial y final. Advertir y escalar. No crear documento |
| Matrimonio sujeto a derecho civil propio o foral (Cataluna, Aragon, Navarra, Baleares, Pais Vasco, Galicia) | Detener: verificar la norma autonomica aplicable con `web_search` y escalar. No aplicar los Arts. 1344 a 1410 CC |
| Empresa familiar, participaciones sociales o explotacion economica en el inventario | Escalar antes de valorar la partida: la valoracion y la adjudicacion de una empresa exceden el alcance de esta skill |
| Patrimonio situado en el extranjero | Escalar: la ley aplicable y la eficacia registral transfronteriza exceden el alcance de esta skill |
| Deudas con la Agencia Tributaria o con la Tesoreria General de la Seguridad Social | Escalar: el tratamiento de la deuda publica en la liquidacion y la responsabilidad de cada conyuge exigen analisis especializado |
| Indicios de ocultacion, distraccion o enajenacion fraudulenta de bienes por un conyuge | Escalar: la partida del Art. 1397.2.º CC y las medidas de aseguramiento exigen estrategia procesal propia. No calificar de fraudulenta una conducta sin base documental |
| Indicios de violencia de genero o domestica, o proceso matrimonial seguido ante un Juzgado de Violencia sobre la Mujer | DETENER SIEMPRE y escalar via `escalate_to_attorney`, conforme al guardrail del plugin |
| Sociedad no disuelta y sin demanda matrimonial ni capitulaciones: solo separacion de hecho | Detener: no hay cauce (Art. 1392 CC). Derivar a `derecho-civil-divorcio` o a capitulaciones. No confundir con la disolucion en curso, que si permite pedir el inventario (Art. 808.1 LEC) |
| Solicitud de inventario sin demanda matrimonial admitida ni resolucion firme | Detener: la solicitud es prematura (Art. 808.1 LEC). Derivar a `derecho-civil-divorcio` |
| Liquidacion posterior a sentencia firme y duda sobre el cauce del Art. 808.1 LEC | Adoptar la posicion conservadora, advertir de que conviene confirmar el criterio del juzgado y ofrecer escalacion |
| Pasivo superior al activo | Advertir de que no hay remanente que dividir (Art. 1404 CC) y tratar la contribucion al deficit. Ofrecer escalacion si la insolvencia es relevante |
| Entidad acreedora que ya ha denegado la novacion subjetiva y conyuge que no puede asumir la cuota en solitario | Advertir de que la adjudicacion no le libera y exponer la venta del inmueble como alternativa realista. Ofrecer escalacion |
| Cliente que pide el calculo de la tributacion del exceso de adjudicacion | Informar de que excede el alcance de la skill y derivar a asesor fiscal. No cuantificar ni citar preceptos tributarios |
| Conyuge con discapacidad o con medidas de apoyo, o herederos menores de edad entre los solicitantes | Advertir de las normas de proteccion y de representacion aplicables y ofrecer escalacion |
| Bien discutido cuya calificacion depende de prueba que el cliente no puede aportar | Adoptar la posicion conservadora (presuncion de ganancialidad del Art. 1361 CC), advertir del riesgo y ofrecer escalacion |
| Cliente que pide una clausula que afirme la liberacion de un conyuge frente al banco | Rechazar la instruccion, explicar por que el convenio no puede producir ese efecto (Arts. 1367 y 1401 CC) y ofrecer la redaccion correcta |
