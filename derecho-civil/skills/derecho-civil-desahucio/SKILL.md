---
name: derecho-civil-desahucio
description: >
  Genera el documento adecuado para recuperar la posesion de una finca urbana, eligiendo la via
  correcta conforme a la LEC verificada en el BOE: demanda de juicio verbal de desahucio por falta
  de pago de rentas (con opcion de acumular la reclamacion de las rentas debidas, Art. 437.4.3ª LEC),
  demanda de desahucio por expiracion del plazo contractual o legal (Art. 250.1.1º LEC), demanda de
  desahucio por precario (Art. 250.1.2º LEC) y acuerdo extrajudicial de condonacion de rentas a cambio
  de la entrega de llaves (transaccion del Art. 1809 CC, homologable conforme al Art. 19 LEC). Aplica
  la resolucion por impago del Art. 27 LAU, los requisitos de admisibilidad del Art. 439.3 y 439.6 LEC
  (Ley 12/2023), el regimen de enervacion del Art. 22.4 LEC y el requisito de MASC de la LO 1/2025.
  NO usar para la recuperacion de vivienda frente a ocupacion sin titulo previo (Art. 250.1.4º LEC),
  desahucio de finca rustica, ejecucion hipotecaria, ni para redactar la oposicion del demandado.
when_to_use: |
  - El usuario quiere recuperar la posesion de una vivienda o local urbano arrendado o cedido.
  - El arrendatario no paga la renta y el arrendador quiere desahuciarlo, con o sin reclamacion de rentas.
  - El contrato de arrendamiento ha expirado y el arrendatario no desaloja.
  - Un ocupante posee la finca sin titulo ni pago (precario) y el propietario quiere recuperarla.
  - El arrendador quiere pactar la salida del ocupante perdonando la deuda a cambio de las llaves.
  - El usuario pide una demanda de desahucio de finca urbana.
inputs:
  - relacion_ocupante: arrendamiento con renta / cesion gratuita sin renta / entrada sin permiso ni contrato
  - causa: falta de pago de rentas / expiracion del plazo contractual o legal
  - via: demanda judicial / acuerdo extrajudicial de salida pactada
  - destino_inmueble: vivienda habitual de la parte ocupante / uso distinto del de vivienda (Art. 439.6.a LEC)
  - gran_tenedor: la parte actora es gran tenedora de vivienda conforme al Art. 3.k de la Ley 12/2023 (si / no / desconocido)
  - requerimiento_previo: requerimiento fehaciente de pago practicado con 30 dias de antelacion (si / no)
  - masc_intentado: se ha intentado un medio adecuado de solucion de controversias acreditable (si / no)
  - datos_demandante: nombre o razon social, NIF o CIF, domicilio, representante si persona juridica, procurador y letrado
  - datos_demandado: nombre o razon social, NIF o CIF si se conoce, domicilio del inmueble
  - datos_inmueble: direccion completa, referencia catastral, municipio y partido judicial
  - datos_contrato: fecha de firma, renta mensual, duracion pactada
  - rentas_debidas: importe total adeudado, conceptos y periodos impagados
  - fecha_expiracion: fecha en que expiro el contrato y sus prorrogas
  - titulo_precario: descripcion de la cesion gratuita y de su revocacion
  - acumular_rentas: acumular o no la reclamacion de las rentas debidas (si / no)
  - condonacion: alcance de la condonacion pactada (total / parcial) y renuncia reciproca de acciones
outputs:
  - demanda_desahucio_falta_pago: demanda de juicio verbal de desahucio por falta de pago en markdown, DRAFT
  - demanda_desahucio_expiracion: demanda de juicio verbal de desahucio por expiracion del plazo en markdown, DRAFT
  - demanda_desahucio_precario: demanda de juicio verbal de desahucio por precario en markdown, DRAFT
  - acuerdo_condonacion: acuerdo de condonacion de rentas y entrega de llaves en markdown, DRAFT
references:
  - references/lec-juicio-desahucio.md
  - references/lau-resolucion-por-impago.md
  - references/enervacion-y-vulnerabilidad.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/demanda-desahucio-falta-pago.md
  - assets/demanda-desahucio-expiracion-plazo.md
  - assets/demanda-desahucio-precario.md
  - assets/acuerdo-condonacion-entrega-llaves.md
---

# Recuperacion de la Posesion de Finca Urbana

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija que la skill defina y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificacion normativa interna, ejecutala en silencio y continua hasta la primera pregunta o hasta la Confirmacion visible, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

Esta linea es, junto con la introduccion fija, la UNICA excepcion a la prohibicion de mencionar la mecanica interna. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, la validacion de admisibilidad, la verificacion normativa y la creacion base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol.
- Resumenes de validacion con checks (ej. "Dato resuelto ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez, en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin:

"Vamos a preparar el documento que le permita recuperar la posesion del inmueble por la via que corresponda a su caso. Para determinarla correctamente, es necesario precisar antes algunos datos."

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:

- **V1 (Relacion con la persona ocupante):** arrendamiento con renta / cesion gratuita sin renta / entrada sin permiso ni contrato previo.
- **V2 (Causa):** falta de pago de rentas / expiracion del plazo contractual o legal. (Solo si V1 = arrendamiento.)
- **V3 (Via):** demanda judicial / acuerdo extrajudicial de salida pactada.
- **V4 (Destino del inmueble):** vivienda habitual de la parte ocupante / uso distinto del de vivienda. (Dato de admisibilidad obligatorio en la rama de demanda, Art. 439.6.a LEC.)
- **V5 (Gran tenedor):** la parte actora es gran tenedora de vivienda / no lo es / no lo sabe. (Dato de admisibilidad obligatorio en la rama de demanda, Art. 439.6.b LEC.)
- **V6 (Requerimiento fehaciente de pago):** practicado con al menos 30 dias de antelacion / practicado sin ese plazo o sin acuse / no practicado. (Solo si V2 = falta de pago.)
- **V7 (MASC):** se ha intentado ya una solucion previa acreditable: si / no. (Solo en la rama de demanda.)

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto (omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama):

* Para V1:
  "La persona que ocupa el inmueble lo hace:
  1. En virtud de un contrato de arrendamiento, pagando o debiendo pagar una renta
  2. Por cesion gratuita suya, sin renta ni contraprestacion
  3. Sin su permiso y sin contrato alguno"

* Para V2 (solo si V1 = 1):
  "El motivo por el que desea recuperar el inmueble es:
  1. La falta de pago de las rentas
  2. El vencimiento del contrato sin que la parte arrendataria lo desaloje"
  → Si concurren ambos, resolver V2 = falta de pago y hacer constar el vencimiento como hecho adicional de la demanda, sin volver a preguntar.

* Para V3:
  "Lo que desea preparar es:
  1. La demanda judicial para recuperar la posesion
  2. Un acuerdo con la parte ocupante para que entregue las llaves sin llegar a juicio"

* Para V4 (solo en la rama de demanda):
  "El inmueble es:
  1. La vivienda habitual de la persona que lo ocupa
  2. Un local, una segunda residencia u otro uso distinto del de vivienda"

* Para V5 (solo en la rama de demanda):
  "En cuanto al numero de inmuebles residenciales de los que usted es titular:
  1. Mas de diez, o mas de 1.500 metros cuadrados construidos de uso residencial
  2. Diez o menos, y menos de 1.500 metros cuadrados
  3. No lo sabe con certeza"

* Para V6 (solo si V2 = falta de pago):
  "Antes de esta consulta, ¿requirio de pago a la parte arrendataria por un medio que deje constancia (burofax con acuse, requerimiento notarial)?
  1. Si, hace mas de treinta dias y conservo el justificante
  2. Si, pero hace menos de treinta dias o no conservo el justificante
  3. No"

* Para V7 (solo en la rama de demanda):
  "Se ha intentado ya una solucion previa con la otra parte que pueda acreditarse documentalmente (requerimiento, negociacion entre abogados, mediacion, conciliacion):
  1. Si
  2. No"

**PRINCIPIO: Preguntas simples, no mega-preguntas.** Cada pregunta resuelve un unico punto de decision. No comprimas V1 y V2 en una sola pregunta ni conviertas V4 y V5 en un cuestionario: son turnos separados.

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = entrada sin permiso ni contrato previo → **DETENER**: el caso corresponde a la recuperacion de la posesion del Art. 250.1.4º de la LEC, con tramitacion propia (Art. 441.1 bis LEC), legitimacion tasada y exceptuada del requisito de MASC (Art. 5.2.e de la LO 1/2025). Fuera del alcance de esta skill. Informar del cauce y ofrecer escalacion. No crear documento.
- Si V3 = acuerdo de salida pactada → **HOJA ACUERDO**: `assets/acuerdo-condonacion-entrega-llaves.md`. V4, V5 y V7 no aplican (no hay demanda que admitir). Si V1 = cesion gratuita, no hay renta debida que condonar: omitir la clausula tercera y adaptar el acuerdo a la entrega de llaves sin condonacion, advirtiendolo al usuario.
- Si V3 = demanda y V1 = arrendamiento y V2 = falta de pago → **HOJA IMPAGO**: `assets/demanda-desahucio-falta-pago.md`.
- Si V3 = demanda y V1 = arrendamiento y V2 = expiracion del plazo → **HOJA EXPIRACION**: `assets/demanda-desahucio-expiracion-plazo.md`.
- Si V3 = demanda y V1 = cesion gratuita sin renta → **HOJA PRECARIO**: `assets/demanda-desahucio-precario.md`.
- En cualquier hoja de demanda, si V7 = no → generar ademas ANTES `assets/acuerdo-condonacion-entrega-llaves.md` NO: el intento previo se documenta con un requerimiento fehaciente. Redactar el requerimiento no forma parte de esta skill; derivar a `derecho-civil-reclamacion-cantidad` (asset `burofax-masc-reclamacion.md`) y advertir de que la demanda no debe presentarse hasta disponer del justificante y de que hayan transcurrido treinta dias naturales sin respuesta (Art. 10.4.a de la LO 1/2025).
- Si la finca es rustica, o el arrendamiento esta excluido de la LAU (Art. 5 LAU), o se pretende la ejecucion hipotecaria → **DETENER**: fuera de alcance. Advertir y escalar.

### Validacion de admisibilidad (interno, antes del Punto 3)

- **TODAS LAS HOJAS DE DEMANDA (Art. 439.6 LEC, redaccion de la Ley 12/2023):** la demanda es inadmisible si no especifica (a) si el inmueble constituye vivienda habitual de la persona ocupante — valor de V4 — y (b) si la parte actora es gran tenedora de vivienda en los terminos del Art. 3.k de la Ley 12/2023 — valor de V5. Si V5 = no es gran tenedora, debe acompanarse certificacion del Registro de la Propiedad con la relacion de propiedades a nombre de la parte actora. Si V5 = no lo sabe, no dar el dato por resuelto: explicar el umbral y pedir que lo confirme antes de redactar.
  **Importante:** las letras c) del apartado 6 y el apartado 7 del Art. 439 (acreditar la vulnerabilidad de la parte demandada y acudir a conciliacion o intermediacion previa cuando la actora es gran tenedora) fueron declarados inconstitucionales y nulos por la Sentencia del Tribunal Constitucional 26/2025, de 29 de enero. NO exigirlos ni incluirlos en la demanda.
- **HOJA IMPAGO (Art. 439.3 LEC):** la demanda es inadmisible si no se indican las circunstancias concurrentes que permiten o impiden la enervacion en el caso concreto. Ese pronunciamiento se construye con el valor de V6 y es obligatorio.
- **HOJA IMPAGO (Art. 27.2.a LAU):** confirmar que lo impagado es la renta o cantidades asimiladas cuyo pago corresponde a la parte arrendataria.
- **HOJA EXPIRACION:** confirmar que el contrato y sus prorrogas legales han vencido (Arts. 9, 10 y 11 LAU) y que no procede prorroga obligatoria ni tacita.
- **HOJA PRECARIO:** confirmar la titularidad de la parte actora y la ausencia de titulo y de renta en la parte ocupante. Si media contraprestacion de cualquier clase, no hay precario: reconducir a la hoja que corresponda.
- **POSTULACION:** en el desahucio, la clase de juicio se determina por razon de la materia (Art. 250.1.1º y 2º), no por la cuantia, por lo que las excepciones de los Arts. 23.2.1º y 31.2.1º de la LEC no operan: abogado y procurador son preceptivos. La cuantia, a los efectos que procedan, es la de una anualidad de renta (Art. 251.9ª LEC).
- **MASC:** el desahucio no figura entre las materias exceptuadas del Art. 5.2 de la LO 1/2025, por lo que el intento previo es requisito de procedibilidad en las tres hojas de demanda. Solo la recuperacion de la posesion del Art. 250.1.4º esta exceptuada (letra e).
- **COMPETENCIA (Art. 52.1.7 LEC):** juzgado del lugar en que este sita la finca, sin sumision posible a otro fuero.

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" de la LEC, de la LAU, de la LO 1/2025, de la Ley 12/2023 y del regimen de suspension por vulnerabilidad.

**2.2 — Consultar la fuente oficial vigente.** La API de legislacion consolidada del BOE devuelve el bloque de un articulo concreto sin descargar la norma entera (requiere la cabecera `Accept: application/xml`):
```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a250
```
Consultar de la LEC (BOE-A-2000-323) los bloques: `a22` (enervacion), `a52` (competencia), `a250` (ambito), `a251` (cuantia), `a437` (forma de la demanda, compromiso de condonacion y acumulacion), `a438` (admision, requerimiento y lanzamiento), `a439` (inadmision en casos especiales), `a441` (vulnerabilidad y suspension), `a447` (sentencia y cosa juzgada), `a549` (ejecucion directa del lanzamiento), `a264` y `a403` (MASC).

Consultar la LAU (BOE-A-1994-26003), bloque `a27`; la LO 1/2025 (BOE-A-2025-76), bloques `a5` y `a1-2` (articulo 10); y la Ley 12/2023 (BOE-A-2023-12203), bloque `a3` (definicion de gran tenedor) y `dt-3`.

Comprobar ademas el estado del regimen extraordinario de suspension de lanzamientos por vulnerabilidad en los articulos 1 y 1 bis del Real Decreto-ley 11/2020 (BOE-A-2020-4208, bloques `a1` y `a1-12`) y si alguna norma posterior lo ha prorrogado y ha sido convalidada por el Congreso. La fecha limite que figure en el texto consolidado es el dato decisivo; una prorroga aprobada por real decreto-ley y no convalidada queda sin efecto.

**2.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar Write/Edit para:
- Actualizar `references/lec-juicio-desahucio.md`, `references/lau-resolucion-por-impago.md` y/o `references/enervacion-y-vulnerabilidad.md` con la redaccion vigente.
- Ajustar la estructura de los assets si cambian los tramites (plazos del requerimiento, senalamiento del lanzamiento, requisitos de admisibilidad del Art. 439).
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion.

**2.5 — Fallback si la fuente no es accesible.** Si la lectura falla (error HTTP, timeout):
```
web_search("Ley Enjuiciamiento Civil desahucio articulos 250 437 438 439 441 texto consolidado BOE")
web_search("suspension extraordinaria lanzamientos vulnerabilidad Real Decreto-ley 11/2020 vigencia BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. El documento se genera con la version de referencia. Verificar manualmente antes de presentar."

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Textos fijos por hoja:
   - IMPAGO: "A su caso corresponde el juicio verbal de desahucio por falta de pago, conforme al articulo 250.1.1º de la Ley 1/2000, de Enjuiciamiento Civil, cualquiera que sea la cuantia, con fundamento sustantivo en el articulo 27.2.a) de la Ley 29/1994, de Arrendamientos Urbanos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - EXPIRACION: "A su caso corresponde el juicio verbal de desahucio por expiracion del plazo, conforme al articulo 250.1.1º de la Ley 1/2000, de Enjuiciamiento Civil, en relacion con los articulos 9 y 10 de la Ley 29/1994, de Arrendamientos Urbanos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - PRECARIO: "A su caso corresponde el juicio verbal de desahucio por precario, conforme al articulo 250.1.2º de la Ley 1/2000, de Enjuiciamiento Civil, en relacion con el articulo 348 del Codigo Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - ACUERDO: "Su caso se resolvera mediante un contrato de transaccion, regulado en el articulo 1809 del Codigo Civil, con condonacion de la deuda condicionada a la entrega de la posesion (articulos 1156 y 1187 del Codigo Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - En las tres hojas de demanda, anadir: "El desahucio no figura entre las materias exceptuadas del articulo 5.2 de la Ley Organica 1/2025, de 2 de enero, por lo que debera acreditarse el intento previo de una solucion extrajudicial para que la demanda sea admitida (articulos 264.4º y 403.2 de la Ley de Enjuiciamiento Civil). Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2025-76"
   - En las tres hojas de demanda, anadir: "En el desahucio son preceptivos abogado y procurador, porque la clase de juicio viene determinada por la materia y no por la cuantia."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (advierte si el documento adjuntado los incumple, en especial las menciones obligatorias del Art. 439.3 y 439.6 LEC).

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento:

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa e investigacion: incluida `fecha_verificacion_normativa` del Punto 2). Los faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{fecha_firmeza}}`, `{{importe_pagos_parciales}}`); usa un marcador generico solo para un hueco suelto sin placeholder propio, y nunca repitas el mismo marcador generico dos veces en el mismo documento (`Edit` necesita un `oldString` unico).
3. Utiliza `Write` para guardar el archivo en disco (nombre en `snake_case.md`, ej. `demanda_desahucio_falta_pago_arrendador_a.md`, `demanda_desahucio_precario_propietario_a.md`, `acuerdo_condonacion_entrega_llaves_arrendador_a.md`).
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. En esa MISMA respuesta, sin turno intermedio y sin preguntar si desea empezar, emite el anuncio fijo de la primera seccion y formula ya su primera pregunta, para que el flujo no se detenga (regla del `CLAUDE.md` raiz, seccion 6.1, punto 5, y coherencia con el Punto 0: la skill esta en ejecucion desde que se carga).

Los bloques condicionales del asset que dependan de decisiones aun no tomadas (acumulacion de rentas, compromiso de condonacion, renuncia de acciones, homologacion) se OMITEN en este `Write` y se insertan durante el Punto 5, releyendo el asset y copiando el bloque sin el envoltorio de comentario.

## 5. EDICION INCREMENTAL DE SECCIONES

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas de negociacion se explican y se confirman una a una.

### Secciones — HOJA IMPAGO / HOJA EXPIRACION / HOJA PRECARIO

1. **Parte demandante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte que reclama la posesion." Sub-apartados, uno por turno: a) nombre completo o razon social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) solo si es persona juridica: nombre, documento y cargo del representante; e) nombre del procurador y del letrado (preceptivos, no preguntar si son necesarios). Al completar el ultimo, vista previa unica con todos los datos y una sola confirmacion antes del `Edit`.
2. **Parte demandada** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte demandada." Sub-apartados: a) nombre o razon social; b) NIF o CIF si se conoce; c) domicilio, que en el desahucio suele ser el propio inmueble. Confirmacion agrupada.
3. **El inmueble y su destino** *(dato objetivo con mencion obligatoria)*. Anuncio fijo: "Describimos ahora el inmueble objeto del procedimiento." Sub-apartados: a) direccion completa; b) referencia catastral; c) municipio y partido judicial. El destino del inmueble ya quedo resuelto en la clasificacion: no volver a preguntarlo, pero hacerlo constar expresamente en el documento porque su omision determina la inadmision (Art. 439.6.a LEC).
4. **Condicion de gran tenedor** *(dato objetivo con consecuencia documental)*. Anuncio fijo: "Debemos hacer constar en la demanda su condicion respecto de la tenencia de vivienda." El valor ya quedo resuelto en la clasificacion. Explica antes de continuar: la mencion es obligatoria y su omision determina la inadmision (Art. 439.6.b LEC); si la parte actora NO es gran tenedora, debe acompanarse certificacion del Registro de la Propiedad con la relacion de sus propiedades, y hay que confirmar con el usuario que la solicitara. Aclara tambien, si el usuario lo plantea, que el deber de acreditar la vulnerabilidad de la parte demandada y de acudir a conciliacion previa fue anulado por la Sentencia del Tribunal Constitucional 26/2025.
5. **Contrato y causa del desahucio** *(dato objetivo, con contenido propio de cada hoja)*.
   - IMPAGO. Anuncio fijo: "Pasamos al contrato y a la deuda de rentas." Sub-apartados, uno por turno: a) fecha del contrato; b) renta mensual; c) periodos impagados; d) importe total adeudado y conceptos que lo componen (rentas y cantidades asimiladas del Art. 27.2.a LAU); e) relacion de documentos que se aportaran.
   - EXPIRACION. Anuncio fijo: "Pasamos al contrato y a su vencimiento." Sub-apartados: a) fecha del contrato; b) duracion pactada; c) fecha en que expiro el contrato y sus prorrogas; d) si se comunico la voluntad de no renovar, y con que antelacion y por que medio.
   - PRECARIO. Anuncio fijo: "Pasamos al origen de la ocupacion y a su revocacion." Sub-apartados: a) titulo de propiedad de la parte actora y documento que lo acredita; b) como y cuando se cedio el uso gratuito y que relacion une a las partes; c) como y cuando se revoco la tolerancia y se requirio la restitucion. Verifica expresamente que no media renta ni contraprestacion de ninguna clase.
6. **Requerimiento previo y enervacion** *(clausula de negociacion — explicar antes de decidir; solo HOJA IMPAGO)*. Anuncio fijo: "Abordamos ahora el requerimiento previo de pago y sus efectos sobre la enervacion." Explica antes de pedir la decision: la parte demandada puede enervar la accion pagando o consignando lo debido y dejar sin efecto el desahucio (Art. 22.4 LEC), salvo que ya enervara en una ocasion anterior o que se le requiriera de pago por medio fehaciente con al menos treinta dias de antelacion a la demanda sin haber pagado. Segun el valor resuelto en la clasificacion:
   - Requerimiento con mas de treinta dias y justificante: si aun no se conocen, pide el medio empleado (burofax, requerimiento notarial) y su fecha exacta, y se hace constar en la demanda que no procede la enervacion, acompanando el requerimiento y su acuse.
   - Requerimiento sin ese plazo, o sin justificante, o inexistente: la enervacion sera posible. Explica que existe la alternativa de practicar ahora un requerimiento fehaciente y esperar treinta dias antes de presentar la demanda, con la ventaja de que el mismo burofax puede servir para acreditar el intento de solucion previa exigido por la Ley Organica 1/2025, y pide al usuario que decida entre presentar ya la demanda asumiendo la enervacion o requerir primero. Confirma la decision antes de escribirla.
   En todo caso, la demanda debe pronunciarse sobre las circunstancias que permiten o impiden la enervacion: su omision determina la inadmision (Art. 439.3 LEC).
7. **Acumulacion de la reclamacion de rentas** *(clausula de negociacion — explicar antes de decidir; HOJA IMPAGO y HOJA EXPIRACION)*. Anuncio fijo: "Decidimos ahora si reclamamos las rentas debidas en la misma demanda." Explica antes de pedir la decision: cabe acumular a la accion de desahucio la reclamacion de las rentas y cantidades analogas vencidas y no pagadas, con independencia de su importe, y tambien la accion contra el fiador o avalista solidario previo requerimiento de pago no satisfecho (Art. 437.4.3ª LEC); los pronunciamientos sobre las acciones acumuladas si producen cosa juzgada, a diferencia del desahucio en si (Art. 447.2 LEC); acumular evita un segundo procedimiento posterior. Pide la decision, y si es afirmativa, el importe y los periodos, e inserta los bloques condicionales de acumulacion del asset. Confirmacion propia.
8. **Solicitud anticipada del lanzamiento** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos la solicitud de senalamiento del lanzamiento." Explica antes de pedir la decision: puede interesarse ya en la demanda que se tenga por solicitada la ejecucion del lanzamiento en la fecha y hora que fije el juzgado (Art. 437.3 in fine LEC); con esa solicitud, la sentencia condenatoria o el decreto que ponga fin al desahucio se ejecutan directamente el dia y hora senalados, sin necesidad de ningun otro tramite ni de nueva notificacion (Art. 549.3 LEC). Es la opcion habitual y acorta materialmente los plazos. Confirmacion propia.
9. **Compromiso de condonacion por desalojo voluntario** *(clausula de negociacion — explicar antes de decidir; HOJA IMPAGO y HOJA EXPIRACION)*. Anuncio fijo: "Valoramos si desea ofrecer una condonacion a cambio del desalojo voluntario." Explica antes de pedir la decision: puede anunciarse en la demanda el compromiso de condonar toda o parte de la deuda y de las costas, con expresion de la cantidad concreta, condicionado a que la parte demandada desaloje voluntariamente dentro del plazo que se indique, que no podra ser inferior a quince dias desde la notificacion de la demanda (Art. 437.3 LEC); ese compromiso se le pone de manifiesto en el requerimiento y su aceptacion equivale a un allanamiento (Art. 438.5 LEC), con senalamiento subsidiario del lanzamiento directo (Art. 447.1 LEC). Si el usuario prefiere pactarlo fuera del proceso, indicaselo y ofrece el acuerdo de condonacion y entrega de llaves como documento alternativo o complementario. Si declina, omitir el bloque. Confirmacion propia.
10. **Vivienda habitual y actuacion de los servicios sociales** *(informativo, sin pregunta; solo si V4 = vivienda habitual)*. Anuncio fijo: "Le informo de las consecuencias procesales de que el inmueble sea la vivienda habitual de la parte ocupante." Informar: el juzgado comunicara de oficio la existencia del procedimiento a las Administraciones competentes en vivienda y servicios sociales, que pueden verificar la situacion de vulnerabilidad y proponer alternativa habitacional; si se confirma, el tribunal puede suspender el proceso por un maximo de dos meses si la parte demandante es persona fisica y de cuatro meses si es persona juridica, ponderando tambien la vulnerabilidad de la parte actora (Art. 441.5, 441.6 y 441.7 LEC). No requiere dato del usuario; encadenar con la seccion siguiente. Informar tambien de que el regimen extraordinario de suspension de lanzamientos ligado a la crisis sanitaria dejo de surtir efecto y de que su estado debe verificarse en cada caso, junto con la normativa autonomica de vivienda aplicable.
11. **Solucion previa (MASC)** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos por ultimo los terminos del intento de solucion previa." Si ya se intento, pedir el medio empleado, la fecha y el documento que lo acredita, y describir el proceso de negociacion en la demanda (Art. 399.3 LEC). Si no se intento, explica: la acreditacion puede consistir en un documento firmado por ambas partes o en cualquier documento que pruebe que la otra parte recibio la solicitud o la propuesta (Art. 10.2 de la LO 1/2025); el proceso se entiende terminado sin acuerdo si transcurren treinta dias naturales desde la recepcion sin reunion ni respuesta escrita (Art. 10.4.a); y la demanda debe presentarse dentro del ano siguiente (Art. 7.3). Advierte de que la demanda no debe presentarse hasta disponer del justificante y de que los campos correspondientes quedan como placeholders hasta entonces. Confirmacion propia.
12. **Juzgado competente** *(dato objetivo con validacion)*. Anuncio fijo: "Determinamos ahora el juzgado competente." Es el del lugar en que este sita la finca (Art. 52.1.7 LEC). Si el usuario propone otro fuero o invoca una clausula de sumision del contrato, advertir de que no cabe y corregirlo.
13. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Lugar de firma; la fecha por defecto es la del dia, salvo indicacion en contrario.

### Secciones — HOJA ACUERDO

1. **Parte arrendadora** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte arrendadora." Sub-apartados, uno por turno: a) nombre completo o razon social; b) documento de identidad o CIF; c) domicilio a efectos de notificaciones; d) solo si es persona juridica: representante y titulo de su representacion. Confirmacion agrupada.
2. **Parte arrendataria u ocupante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte que ocupa el inmueble." Sub-apartados: a) nombre o razon social; b) documento de identidad o CIF; c) domicilio. Confirmacion agrupada.
3. **Inmueble y contrato que se extingue** *(dato objetivo)*. Anuncio fijo: "Describimos el inmueble y el contrato que se va a extinguir." Sub-apartados: a) direccion completa y referencia catastral; b) titulo de la parte arrendadora; c) fecha del contrato y renta mensual; d) si existe ya un procedimiento judicial en curso, juzgado y numero de autos.
4. **Deuda que se reconoce** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a fijar la deuda que se reconoce." Explica antes de pedir la cifra: el reconocimiento de deuda fija el importe sobre el que operara la condonacion y, si el acuerdo se incumple, es la cantidad que renace; conviene que incluya todos los conceptos vencidos (rentas y cantidades asimiladas) y que se cierre a una fecha concreta. Pide el importe, los conceptos y los periodos. Confirmacion propia.
5. **Alcance de la condonacion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Abordamos ahora el alcance de la condonacion." Explica antes de pedir la decision: la condonacion puede ser total o parcial; si es parcial hay que fijar la cantidad que subsiste, su forma de pago y su plazo; la condonacion se pacta como contraprestacion del desalojo dentro de una transaccion (Art. 1809 CC) y por eso debe quedar condicionada a la entrega efectiva, de modo que una condonacion incondicionada extinguiria la deuda aunque el inmueble no se entregase (Arts. 1156 y 1187 CC); y la operacion puede tener consecuencias tributarias para ambas partes que conviene verificar con un asesor fiscal. Confirmacion propia.
6. **Entrega de llaves y de la posesion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos la entrega de las llaves y de la posesion." Explica antes de pedir los datos: la fecha y la hora deben ser ciertas, porque de ellas depende la eficacia de la condonacion, y conviene levantar acta con el numero de llaves, el estado del inmueble y las lecturas de los contadores. Sub-apartados, uno por turno: a) fecha y hora de la entrega; b) lugar; c) tratamiento de las rentas que se devenguen hasta la entrega. Confirmacion de cada uno.
7. **Fianza, garantias y suministros** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos el destino de la fianza y de las garantias." Explica: la fianza puede devolverse, aplicarse a la deuda subsistente o compensarse con los danos que resulten del acta; conviene decidirlo ahora para evitar una controversia posterior. Pide el importe de la fianza, su destino y, si existen, el tratamiento de las garantias adicionales. Confirmacion propia.
8. **Renuncia reciproca de acciones** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Valoramos la renuncia reciproca de acciones." Explica antes de pedir la decision: una renuncia amplia cierra el asunto pero impide reclamar despues los danos en el inmueble; la posicion conservadora es exceptuar de la renuncia los danos que consten en el acta de entrega y los danos ocultos. Ofrece las dos redacciones del asset y pide la decision. Confirmacion propia.
9. **Consecuencias del incumplimiento** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Fijamos las consecuencias del incumplimiento del acuerdo." Explica: si no se entrega en la fecha pactada, la condonacion queda sin efecto, renace la deuda integra y la parte arrendadora puede ejercitar sin mas tramite las acciones de desahucio y de reclamacion; si hay procedimiento en curso, puede instar su continuacion. Confirma la redaccion antes de aplicarla.
10. **Fuerza ejecutiva del acuerdo** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Decidimos como dotar de fuerza ejecutiva al acuerdo." Explica las tres opciones y sus consecuencias: si hay procedimiento en curso, la homologacion judicial (Art. 19 LEC) le da los efectos de la transaccion judicial y permite ejecutarlo como una sentencia (Art. 517.2.3º LEC); sin procedimiento, la elevacion a escritura publica lo convierte en titulo ejecutivo (Art. 517.2.2º LEC); si no se hace ninguna de las dos, el acuerdo obliga entre las partes (Art. 1816 CC) pero su incumplimiento obliga a un nuevo pleito. Recomienda la homologacion o la escritura publica. Confirmacion propia.
11. **Lugar, fecha y firma** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del acuerdo." Lugar de firma; la fecha por defecto es la del dia, salvo indicacion en contrario.

Al rellenar cualquier hoja de demanda, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5, muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una seccion existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

## Guardrails

1. Verificar siempre la LEC, la LAU y la LO 1/2025 en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder.
2. Si se detecta una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar. No usar una version desactualizada.
3. Las menciones del Art. 439.6.a) y b) de la LEC (destino del inmueble y condicion de gran tenedor de la parte actora) son obligatorias en toda demanda que pretenda recuperar la posesion de una finca por las vias del Art. 250.1.1º, 2º, 4º y 7º. Su omision determina la inadmision. Nunca redactar una demanda sin ellas.
4. Las letras c) del apartado 6 y el apartado 7 del Art. 439 de la LEC fueron declarados inconstitucionales y nulos por la STC 26/2025, de 29 de enero. No exigir al usuario acreditar la vulnerabilidad de la parte demandada ni acudir a conciliacion o intermediacion previa por ser gran tenedor, ni incluir esas menciones en la demanda.
5. En el desahucio por falta de pago, la demanda debe pronunciarse sobre las circunstancias que permiten o impiden la enervacion (Art. 439.3 LEC). Nunca omitir ese pronunciamiento.
6. La enervacion (Art. 22.4 LEC) solo cabe en el desahucio por falta de pago, una sola vez, y no procede si se requirio de pago por medio fehaciente con al menos treinta dias de antelacion sin resultado. No cabe enervacion en expiracion del plazo ni en precario. Informar siempre de esta regla y nunca afirmar que la enervacion esta excluida sin justificante del requerimiento.
7. El intento previo de un medio adecuado de solucion de controversias es requisito de procedibilidad en las tres hojas de demanda: el desahucio no figura entre las materias exceptuadas del Art. 5.2 de la LO 1/2025. Solo la recuperacion de la posesion del Art. 250.1.4º esta exceptuada (letra e).
8. Competencia exclusiva del tribunal del lugar en que este sita la finca (Art. 52.1.7 LEC). No admitir sumision a otro fuero aunque el contrato la contenga.
9. En el desahucio, abogado y procurador son preceptivos: la clase de juicio se determina por la materia, no por la cuantia, y las excepciones de los Arts. 23.2.1º y 31.2.1º de la LEC no operan.
10. El regimen extraordinario de suspension de lanzamientos por vulnerabilidad tiene vigencia temporal y ha sido objeto de prorrogas no siempre convalidadas. Nunca afirmar que esta vigente ni que esta derogado sin haberlo comprobado en el texto consolidado en el Punto 2. Lo que si es permanente es el mecanismo de los Arts. 441.5 a 441.7 de la LEC en desahucios de vivienda habitual.
11. Nunca redactar clausulas o pretensiones que contravengan normas imperativas de la LAU (Art. 6 LAU) ni afirmar la resolucion del contrato sin base en el Art. 27 LAU.
12. En el acuerdo de condonacion, la condonacion debe quedar siempre condicionada a la entrega efectiva de la posesion. Nunca redactar una condonacion incondicionada previa al desalojo.
13. Nunca inventar datos, rentas, fechas, referencias catastrales ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.

## Como NO se usa esta skill

- No usar para la recuperacion de la posesion de una vivienda frente a quien entro en ella sin titulo ni relacion previa (Art. 250.1.4º LEC): tiene legitimacion tasada, tramitacion propia (Art. 441.1 bis LEC) y esta exceptuada del MASC. Advertir y escalar.
- No usar para la efectividad de derechos reales inscritos frente a quien los perturba (Art. 250.1.7º LEC).
- No usar para desahucio de finca rustica ni de arrendamientos excluidos de la LAU (Art. 5 LAU).
- No usar para la ejecucion hipotecaria ni para el lanzamiento derivado de ella.
- No usar para redactar la oposicion de la parte demandada, el escrito de enervacion ni el incidente de suspension por vulnerabilidad: advertir y escalar.
- No usar para reclamar solo rentas sin recuperar la posesion: derivar a `derecho-civil-reclamacion-cantidad`.
- No usar para redactar el burofax de requerimiento previo: el asset esta en `derecho-civil-reclamacion-cantidad`.
- No usar si el usuario pide opinion juridica sobre la estrategia de un litigio: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Entrada en el inmueble sin titulo ni relacion previa (Art. 250.1.4º LEC) | Informar del cauce y de su legitimacion tasada, y escalar: fuera del alcance de la skill |
| La parte actora no sabe si es gran tenedora y no puede confirmarlo | Detener antes de redactar: sin ese dato la demanda es inadmisible (Art. 439.6.b LEC). Indicar que lo verifique en el Registro de la Propiedad |
| Vulnerabilidad acreditada de la parte demandada o inmueble que es su vivienda habitual con menores o personas dependientes | Advertir de la suspension de los Arts. 441.5 a 441.7 LEC y de la normativa autonomica, y ofrecer escalacion |
| Plazo de un ano desde la solicitud de negociacion previa vencido (Art. 7.3 LO 1/2025) | Advertir de que el requisito de procedibilidad debera reiterarse y escalar |
| Contrato de arrendamiento inscrito con pacto de resolucion de pleno derecho (Art. 27.4 LAU) | Advertir de la via notarial o judicial de requerimiento previa a la cancelacion registral y escalar |
| Litigio previo entre las partes, reconvencion previsible o concurso de la parte arrendataria | Escalar via escalate_to_attorney |
| Caso con componente penal (coacciones, usurpacion, danos) | Escalar a abogado via escalate_to_attorney |
| Duda sobre normativa autonomica de vivienda o sobre zona de mercado residencial tensionado | Usar web_search para verificar y advertir al usuario |
