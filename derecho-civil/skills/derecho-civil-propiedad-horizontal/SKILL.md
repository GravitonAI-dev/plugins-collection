---
name: derecho-civil-propiedad-horizontal
description: >
  Genera el documento adecuado en materia de propiedad horizontal conforme a la Ley 49/1960 (LPH) y a la LEC
  verificadas en el BOE: certificacion del acuerdo de liquidacion de deuda (Art. 21.3 LPH), peticion inicial del
  proceso monitorio especial de cuotas de comunidad (Art. 21 LPH y Art. 812.2.2º LEC), demanda de juicio ordinario
  de impugnacion de acuerdos de junta (Art. 18 LPH y Art. 249.1.8º LEC) y requerimiento de cesacion de actividad
  prohibida o molesta del presidente al infractor (Art. 7.2 LPH). NO usar para la administracion de fincas
  (contabilidad, presupuestos, convocatorias, actas), para conflictos vecinales sin base en la LPH, para la
  redaccion de la demanda de cesacion ni para obras que afecten a la estructura o al titulo constitutivo.
when_to_use: |
  - Una comunidad de propietarios quiere reclamar judicialmente cuotas impagadas a un propietario.
  - Hace falta la certificacion del acuerdo de liquidacion de deuda para poder acudir al monitorio.
  - Un propietario quiere impugnar un acuerdo adoptado por la junta de propietarios.
  - La comunidad necesita requerir formalmente el cese de una actividad molesta, prohibida o no autorizada.
  - El presidente o el administrador pregunta que pasos previos exige la LPH antes de reclamar o de demandar.
inputs:
  - rol_cliente: la comunidad de propietarios (o su presidente, secretario o administrador) / un propietario a titulo individual
  - asunto_comunidad: impago de cuotas / actividad prohibida o molesta
  - asunto_propietario: impugnacion de un acuerdo de junta / otra cuestion
  - acuerdo_liquidacion: la junta ha aprobado ya la liquidacion de la deuda y autorizado la reclamacion (si / no)
  - datos_comunidad: denominacion, NIF, direccion de la finca, presidente y secretario o administrador
  - datos_deudor: nombre o razon social, NIF/CIF, elemento privativo, cuota de participacion, domicilio designado
  - desglose_deuda: conceptos, periodos, fechas de exigibilidad e importes; total
  - datos_junta_impugnada: fecha, tipo de junta, convocatoria, punto del orden del dia, texto del acuerdo, votacion
  - posicion_votacion: salvo el voto / ausente / privado indebidamente del voto / voto a favor
  - al_corriente_pago: el propietario impugnante esta al corriente o ha consignado (si / no / excepcion del Art. 18.2)
  - fecha_computo_plazo: fecha del acuerdo o, si el propietario estuvo ausente, de su comunicacion
  - datos_infractor: nombre, NIF/CIF, condicion de propietario u ocupante, elemento privativo, domicilio
  - descripcion_actividad: hechos verificables (fechas, horarios, mediciones, denuncias) y medios de acreditacion
  - requerimiento_previo: el presidente ha requerido ya fehacientemente la cesacion (no / si, sin acreditacion / si, acreditado)
outputs:
  - certificacion_deuda: certificacion del acuerdo de liquidacion de deuda en markdown, DRAFT
  - peticion_monitorio_lph: peticion inicial del monitorio especial de cuotas en markdown, DRAFT
  - demanda_impugnacion: demanda de juicio ordinario de impugnacion de acuerdos en markdown, DRAFT
  - requerimiento_cesacion: requerimiento del presidente al infractor en markdown, DRAFT
references:
  - references/lph-reclamacion-y-acuerdos.md
  - references/masc-y-requisitos-previos-lph.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/certificacion-deuda-comunidad.md
  - assets/peticion-monitorio-cuotas-lph.md
  - assets/demanda-impugnacion-acuerdos.md
  - assets/requerimiento-cesacion-actividad.md
---

# Propiedad Horizontal

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, la validacion de presupuestos, la verificacion normativa y la creacion base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol.
- Resumenes de validacion con checks (ej. "Dato resuelto ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la introduccion fija del Punto 1, que solo se usa una vez, en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin:

"Vamos a preparar el documento que corresponda a su asunto de comunidad de propietarios. Para determinarlo correctamente, es necesario precisar antes algunos datos."

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:

- **V1 (Posicion del cliente):** la comunidad de propietarios (presidente, secretario, administrador o la propia junta) / un propietario a titulo individual.
- **V2 (Asunto de la comunidad):** impago de cuotas / actividad prohibida o molesta. (Solo si V1 = comunidad.)
- **V3 (Asunto del propietario):** impugnacion de un acuerdo de junta / otra cuestion. (Solo si V1 = propietario.)
- **V4 (Acuerdo de liquidacion):** la junta ha aprobado ya la liquidacion de la deuda y autorizado su reclamacion: si / no. (Solo si V2 = impago.)
- **V5 (Legitimacion y plazo de la impugnacion):** posicion del cliente en la votacion (salvo el voto, ausente, privado indebidamente del voto, voto a favor); fecha del acuerdo o de su comunicacion si estuvo ausente; y si esta al corriente de pago. (Solo si V3 = impugnacion.)
- **V6 (Requerimiento previo del presidente):** no se ha requerido / se requirio de palabra o sin poder acreditarlo / se requirio de forma fehaciente y el infractor persiste. (Solo si V2 = actividad.)

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto (omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama):

* Para V1:
  "Actua usted en nombre de:
  1. La comunidad de propietarios
  2. Un propietario a titulo individual"

* Para V2 (solo si V1 = 1):
  "El asunto de la comunidad es:
  1. El impago de cuotas por un propietario
  2. Una actividad molesta, prohibida o no autorizada en un piso o local"

* Para V3 (solo si V1 = 2):
  "Lo que desea es:
  1. Impugnar un acuerdo adoptado por la junta de propietarios
  2. Otra cuestion relacionada con la comunidad"

* Para V4 (solo si V2 = 1):
  "La junta de propietarios ha aprobado ya la liquidacion de la deuda y ha autorizado su reclamacion judicial:
  1. Si
  2. No, aun no se ha celebrado o no se ha tratado ese punto"

* Para V5 (solo si V3 = 1). Se resuelve en dos preguntas sucesivas, nunca en una sola:
  - V5.a: "En esa junta usted:
    1. Voto en contra y lo hizo constar en el acta
    2. No asistio
    3. Asistio pero se le impidio votar
    4. Voto a favor o se abstuvo sin dejar constancia"
  - V5.b (solo si V5.a es 1, 2 o 3): "Respecto de las cuotas y derramas vencidas de la comunidad, usted:
    1. Esta al corriente de pago
    2. Tiene cantidades pendientes"

* Para V6 (solo si V2 = 2):
  "El presidente ha requerido ya al infractor para que cese en la actividad:
  1. No
  2. Si, pero de palabra o sin poder acreditarlo documentalmente
  3. Si, por escrito y con acreditacion, y el infractor persiste"

**PRINCIPIO: Preguntas simples, no mega-preguntas.** Cada pregunta resuelve un unico punto de decision. La fecha del acuerdo impugnado, la fecha de su comunicacion al ausente y el importe de la deuda NO se preguntan aqui: se resuelven por Escucha Activa o se piden en la edicion incremental (Punto 5), en prosa natural y sin opciones numeradas.

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = comunidad y V2 = impago:
  - **V4 = si → HOJA CUOTAS**: se generan DOS documentos, en este orden: `assets/certificacion-deuda-comunidad.md` y despues `assets/peticion-monitorio-cuotas-lph.md`.
  - **V4 = no → HOJA CUOTAS-SIN-ACUERDO**: advertir de que el acuerdo de la junta que aprueba la liquidacion y autoriza la reclamacion es un requisito legal previo (articulos 21.1 a 21.3 de la Ley de Propiedad Horizontal) y de que sin el no cabe emitir la certificacion ni presentar la peticion. Generar unicamente `assets/certificacion-deuda-comunidad.md` como borrador, dejando como placeholders los datos del acuerdo, para emitirlo cuando la junta lo adopte. **NO** generar la peticion de monitorio en esta rama.
- Si V1 = comunidad y V2 = actividad:
  - **V6 = 1 o 2 → HOJA CESACION**: `assets/requerimiento-cesacion-actividad.md`. (En V6 = 2 se advierte de que el requerimiento anterior no sirve como presupuesto de la accion por no ser acreditable, y de que este lo sustituye.)
  - **V6 = 3 → DETENER**: el requerimiento ya esta cumplido y el paso siguiente es la accion de cesacion, que exige autorizacion de la junta debidamente convocada al efecto y se sustancia por juicio ordinario. Informar de la secuencia del articulo 7.2 de la Ley de Propiedad Horizontal, derivar a la skill `derecho-civil-juicio-ordinario` y ofrecer escalacion. No crear documento.
- Si V1 = propietario y V3 = impugnacion:
  - **V5.a = 4 → DETENER**: quien voto a favor o se abstuvo sin salvar su voto no esta legitimado para impugnar (articulo 18.2 de la Ley de Propiedad Horizontal). Explicarlo y ofrecer escalacion. No crear documento.
  - **V5.a = 1, 2 o 3 y plazo vigente → HOJA IMPUGNACION**: `assets/demanda-impugnacion-acuerdos.md`.
  - **Plazo caducado → DETENER**: la accion caduca a los tres meses de adoptarse el acuerdo, o al año si es contrario a la ley o a los estatutos; para el ausente el computo arranca de la comunicacion del acuerdo (articulo 18.3). Advertir de la caducidad, no dar falsas expectativas y ofrecer escalacion. No crear documento.
  - **V5.b = 2 (deudas pendientes)**: no detiene el flujo, pero es un obstaculo. Ver la validacion de presupuestos.
- Si V1 = propietario y V3 = otra cuestion → **DETENER Y DERIVAR**: identificar la materia y derivar sin crear documento. Casos frecuentes: requerimiento de pago de un monitorio de la comunidad ya recibido (skill `derecho-civil-reclamacion-cantidad`, escrito de oposicion, plazo de veinte dias); reclamacion de cantidad frente a la comunidad por daños (skill `derecho-civil-reclamacion-cantidad`); cuestiones arrendaticias del piso (skills `derecho-civil-arrendamiento` o `derecho-civil-desahucio`). Si no encaja en ninguna, ofrecer escalacion.

### Validacion de presupuestos (interno, antes del Punto 3)

- **HOJA CUOTAS:** comprobar que existe acuerdo de junta aprobando la liquidacion y autorizando la reclamacion; que quien va a firmar la certificacion ejerce las funciones de secretario; y si el visto bueno del presidente es necesario o concurre la excepcion del articulo 21.3 (secretario-administrador con cualificacion profesional legalmente reconocida que no vaya a intervenir profesionalmente en la reclamacion). Comprobar que la deuda puede desglosarse por concepto y periodo. Si el deudor no ha designado domicilio, anotar la regla del articulo 815.2 de la LEC (notificacion en el propio piso o local) para explicarla en el Punto 5.
- **HOJA CUOTAS-SIN-ACUERDO:** ademas de lo anterior, advertir de que la junta debe incluir el punto en el orden del dia y de que la certificacion no puede emitirse antes.
- **HOJA IMPUGNACION:** verificar la legitimacion (articulo 18.2), el plazo de caducidad (articulo 18.3, computado desde el acuerdo o desde su comunicacion al ausente) y el requisito de estar al corriente de pago, con la excepcion legal de los acuerdos sobre establecimiento o alteracion de las cuotas de participacion del articulo 9. Si el cliente estuvo ausente, comprobar si comunico su discrepancia dentro de los treinta dias naturales del articulo 17.8 y advertir de las consecuencias si no lo hizo. Abogado y procurador son preceptivos.
- **HOJA CESACION:** verificar que quien requiere es el presidente (o que actua por su cuenta a iniciativa de un propietario u ocupante) y que la conducta encaja en alguno de los tres supuestos del articulo 7.2, o en el articulo 7.3 si se trata de alquiler de uso turistico sin aprobacion de la comunidad. Comprobar si el infractor es propietario u ocupante.
- **MASC:** en la HOJA IMPUGNACION es exigible el intento previo de solucion (articulos 264.4º y 403.2 de la LEC). En la HOJA CUOTAS la cuestion es discutida: posicion conservadora, aprovechar la notificacion de la deuda y advertir. Ver `references/masc-y-requisitos-previos-lph.md`.

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" de la LPH, de la LEC y de la LO 1/2025.

**2.2 — Consultar la fuente oficial vigente.** Consultar el texto consolidado de la LPH y los articulos de la LEC que apliquen a la hoja enrutada. La via preferente es la API de legislacion consolidada del BOE, que devuelve el texto bloque a bloque:

```
read_document(path: "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1960-10906/metadatos", format: "text")
read_document(path: "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1960-10906/texto/bloque/aveintiuno", format: "text")
read_document(path: "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a813", format: "text")
```

Bloques a consultar segun la hoja (en cada bloque, la version vigente es la ULTIMA `<version>` que aparece):

| Hoja | LPH (BOE-A-1960-10906) | LEC (BOE-A-2000-323) |
|---|---|---|
| CUOTAS y CUOTAS-SIN-ACUERDO | `aveintiuno` (art. 21), `anoveno` (art. 9) | `a812`, `a813`, `a814`, `a815`, `a818` |
| IMPUGNACION | `adieciocho` (art. 18), `adiecisiete` (art. 17) | `a249`, `a264`, `a403` |
| CESACION | `aseptimo` (art. 7), `adiecisiete` (art. 17) | `a249` |

Anotar la fecha de actualizacion del texto consolidado (`fecha_actualizacion` de los metadatos) como `{{fecha_verificacion_normativa}}`.

**2.3 — Comparar.** Contrastar la redaccion oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si el texto consolidado es posterior o la redaccion de los articulos ha cambiado, usar Write/Edit para:
- Actualizar `references/lph-reclamacion-y-acuerdos.md` y/o `references/masc-y-requisitos-previos-lph.md` con la redaccion vigente.
- Actualizar el asset afectado si la reforma altera un requisito documental (por ejemplo, el contenido de la certificacion del articulo 21.3 o el regimen de mayorias del articulo 17).
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**2.5 — Fallback si la fuente no es accesible.** Si la lectura falla (error HTTP, timeout), intentar la version HTML del texto consolidado:
```
read_document(path: "https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906", format: "text")
```
Si tambien falla:
```
web_search("Ley 49/1960 propiedad horizontal articulo [el de la hoja enrutada] texto consolidado BOE")
```
Si tampoco: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la Ley de Propiedad Horizontal en el BOE. El documento se genera con la version de referencia. Verificar manualmente antes de presentarlo."

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa el cauce y la fuente aplicable.** Indica que documento corresponde a su caso y por que, citando la norma con nombre completo y articulo, con el enlace del BOE consultado. Textos fijos por hoja:
   - CUOTAS: "A su caso corresponde el proceso monitorio especial de comunidades de propietarios, regulado en el articulo 21 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal, en relacion con el articulo 812.2.2º de la Ley 1/2000, de Enjuiciamiento Civil. Prepararemos primero la certificacion del acuerdo de liquidacion de la deuda, que es el documento que la ley exige acompanar, y despues la peticion inicial. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"
   - CUOTAS-SIN-ACUERDO: anadir al texto anterior "Tenga en cuenta que la reclamacion requiere un acuerdo previo de la junta que apruebe la liquidacion de la deuda y autorice su reclamacion judicial, conforme a los articulos 21.1 y 21.2 de la misma ley. Prepararemos ahora la certificacion para que pueda emitirse en cuanto la junta lo adopte; la peticion inicial no debe presentarse antes."
   - IMPUGNACION: "A su caso corresponde la impugnacion de acuerdos de la junta, regulada en el articulo 18 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal, que se sustancia por los tramites del juicio ordinario conforme al articulo 249.1.8º de la Ley 1/2000, de Enjuiciamiento Civil, cualquiera que sea la cuantia. La accion caduca a los tres meses desde la adopcion del acuerdo, o al año si el acuerdo es contrario a la ley o a los estatutos. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"
   - CESACION: "A su caso corresponde el requerimiento previo de cesacion del articulo 7.2 de la Ley 49/1960, de 21 de julio, sobre propiedad horizontal, que el presidente debe dirigir al infractor antes de que la comunidad pueda ejercitar la accion de cesacion. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"
   - En IMPUGNACION, anadir siempre: "Antes de presentar la demanda debera acreditarse el intento de solucion extrajudicial exigido por la Ley Organica 1/2025 (articulos 264 y 403.2 de la Ley de Enjuiciamiento Civil). La solicitud de negociacion suspende el plazo de caducidad, pero no conviene apurarlo."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (advierte si el documento adjuntado los incumple, en particular si la certificacion carece de desglose o de las firmas exigidas por el articulo 21.3).

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento. En la HOJA CUOTAS se crean DOS documentos: primero la certificacion, con su ciclo completo de edicion incremental, y despues la peticion inicial, que reutiliza sin volver a preguntarlos todos los datos ya recogidos (comunidad, deudor, acuerdo, desglose, notificacion).

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa e investigacion: incluida `fecha_verificacion_normativa` del Punto 2). Los faltantes conservan el nombre propio del placeholder del asset; usa un marcador generico solo para un hueco suelto sin placeholder propio, y nunca repitas el mismo marcador generico dos veces en el mismo documento (`Edit` necesita un `oldString` unico).
3. Utiliza `Write` para guardar el archivo en disco (nombre en `snake_case.md`, ej. `certificacion_deuda_comunidad_a.md`, `peticion_monitorio_cuotas_comunidad_a.md`, `demanda_impugnacion_acuerdos_propietario_a.md`, `requerimiento_cesacion_actividad_infractor_a.md`).
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. Inmediatamente despues, en la misma respuesta, pregunta si desea empezar a completar los datos del documento. Solo tras la confirmacion, formula la primera pregunta de la edicion incremental (Punto 5).

## 5. EDICION INCREMENTAL DE SECCIONES

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las secciones marcadas como de negociacion se explican y se confirman una a una.

### Secciones — HOJA CUOTAS y HOJA CUOTAS-SIN-ACUERDO

1. **Datos de la comunidad** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la comunidad de propietarios." Sub-apartados, uno por turno: a) denominacion; b) NIF; c) direccion completa de la finca; d) nombre y NIF de quien ejerce las funciones de secretario o secretario-administrador, y su cargo exacto; e) nombre del presidente. Antes de cerrar el bloque, si el secretario es un administrador profesional, pregunta si va a intervenir profesionalmente en la reclamacion, porque de ello depende que sea o no necesario el visto bueno del presidente (articulo 21.3). Al completar el ultimo, vista previa unica con todos los datos y una sola confirmacion antes del `Edit`.
2. **Datos del propietario deudor** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion del propietario deudor." Sub-apartados: a) nombre o razon social; b) NIF o CIF si se conoce; c) elemento privativo (piso, letra, planta, plaza o local); d) cuota de participacion; e) domicilio designado por el deudor para las notificaciones de la comunidad. Si no ha designado ninguno, explicar que el requerimiento judicial se practicara en el propio piso o local (articulo 815.2 de la LEC) y hacerlo constar. Confirmacion agrupada.
3. **Acuerdo de la junta y notificacion de la deuda** *(dato objetivo con validacion)*. Anuncio fijo: "Abordamos ahora el acuerdo de la junta y su notificacion al deudor." Sub-apartados, uno por turno: a) fecha y tipo de la junta y punto del orden del dia; b) persona facultada por la junta para reclamar; c) fecha y medio de notificacion del acuerdo al deudor; d) solo si la notificacion personal fracaso: fechas de inicio y fin de la publicacion en el tablon de anuncios, verificando que cubre al menos tres dias. En la HOJA CUOTAS-SIN-ACUERDO, los datos a) y b) quedan como placeholders y se advierte de ello sin preguntarlos.
4. **Desglose de la deuda** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a determinar la deuda y su desglose." Antes de pedir cifras, explica que pueden reclamarse todas las cantidades debidas por gastos comunes, ordinarios o extraordinarios, generales o individualizables, y las aportaciones al fondo de reserva (articulo 21.2), asi como las cuotas aprobadas que se devenguen hasta la notificacion de la deuda (articulo 21.3); y explica que la ley exige el desglose y no admite un importe global. Recoge despues, concepto a concepto, periodo, fecha de exigibilidad e importe, y calcula el total. Verifica que la suma cuadra antes de escribirla.
5. **Intereses y gastos de la reclamacion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos ahora los intereses y los gastos de la reclamacion." Explica antes de pedir la decision: los creditos de la comunidad devengan intereses desde el momento en que debio hacerse cada pago (articulo 21.1), sin necesidad de requerimiento; la junta puede haber acordado medidas disuasorias, que no pueden ser abusivas ni desproporcionadas ni retroactivas; y pueden repercutirse al deudor los gastos y costes de la reclamacion, incluidos los del secretario administrador (articulo 21.3). Confirmacion una a una (intereses primero, gastos despues).
6. **Contra quien se dirige la reclamacion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos contra quien se dirige la reclamacion." Explica antes de decidir: cabe demandar al titular registral a efectos de soportar la ejecucion sobre el inmueble (articulo 21.2); si el piso cambio de manos, el adquirente responde con el propio inmueble de lo debido en la anualidad en curso y los tres años naturales anteriores, por la afeccion real del articulo 9.1.e); y el propietario anterior que no comunico la transmision responde solidariamente de las deudas posteriores (articulo 9.1.i). Pregunta despues si el piso ha cambiado de titularidad y si desea dirigir la reclamacion tambien contra alguno de ellos.
7. **Juzgado competente** *(decision con explicacion)*. Anuncio fijo: "Determinamos ahora el juzgado competente." Explica que la comunidad puede elegir entre el juzgado del domicilio o residencia del deudor y el del lugar donde se halla la finca (articulo 813 de la LEC), que no cabe sumision a otro fuero, y pide la eleccion. Si el usuario propone un fuero distinto, advertir y corregir.
8. **Postulacion y embargo preventivo** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Cerramos con la intervencion profesional y las medidas frente a una eventual oposicion." Explica: no son preceptivos abogado ni procurador para la peticion inicial, pero si se utilizan sus honorarios y derechos son repercutibles al deudor con los limites del articulo 394.3 de la LEC (articulo 21.5); y que, si el deudor se opone, cabe pedir el embargo preventivo de sus bienes, que el tribunal acordara en todo caso y sin caucion (articulo 21.4). Pregunta si intervienen procurador y letrado y si desea anunciar el embargo preventivo. Confirmacion una a una.
9. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del documento." Lugar de firma; la fecha por defecto es la del dia, salvo indicacion en contrario.

Las secciones 1 a 6 rellenan la certificacion (comunidad, deudor, acuerdo y notificacion, desglose, intereses y gastos, contra quien se dirige la reclamacion). Las secciones 7 (juzgado competente) y 8 (postulacion y embargo preventivo) no tienen campo alguno en la certificacion: se preguntan por primera vez al construir la peticion inicial, inmediatamente despues de cerrar la certificacion. La seccion 9 (lugar y fecha) se responde dos veces con sentido distinto: la fecha de la certificacion al cerrar esta, y la fecha de la peticion al construirla, que puede no coincidir; el lugar, si no cambia, no se vuelve a preguntar. Al terminar la certificacion, encadenar con la creacion de la peticion inicial (solo en la HOJA CUOTAS) sin repetir ninguna pregunta ya respondida: los datos de las secciones 1 a 6 se vuelcan directamente.

### Secciones — HOJA IMPUGNACION

1. **Datos del propietario demandante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por su identificacion como parte demandante." Sub-apartados, uno por turno: a) nombre completo o razon social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) elemento privativo y cuota de participacion; e) nombre del procurador y del letrado, preceptivos en el juicio ordinario. Confirmacion agrupada.
2. **Datos de la comunidad demandada** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la comunidad demandada." Sub-apartados: a) denominacion; b) NIF si se conoce; c) direccion de la finca; d) nombre del presidente, que es quien la representa en juicio. Confirmacion agrupada.
3. **La junta y el acuerdo impugnado** *(dato objetivo con validacion)*. Anuncio fijo: "Abordamos ahora la junta y el acuerdo que se impugna." Sub-apartados, uno por turno: a) fecha y tipo de junta; b) fecha y medio de la convocatoria; c) punto del orden del dia; d) texto literal del acuerdo tal como consta en el acta; e) resultado de la votacion (votos a favor, en contra, abstenciones y cuotas que representan). Valida el sentido de las respuestas: si el resultado de la votacion no cuadra con el acuerdo descrito, dialoga y pide aclaracion antes de escribirlo.
4. **Legitimacion y plazo** *(dato objetivo con validacion y advertencia)*. Anuncio fijo: "Verificamos ahora su legitimacion y el plazo para impugnar." La posicion en la votacion ya esta resuelta y NO se vuelve a preguntar. Sub-apartados que si se piden: a) si consta en el acta la constancia de su voto en contra, o la fecha en que se le comunico el acuerdo si estuvo ausente; b) solo si estuvo ausente: si comunico su discrepancia al secretario dentro de los treinta dias naturales siguientes, explicando antes que, de no hacerlo, su voto se computa como favorable (articulo 17.8) y ello debilita la impugnacion. Calcula el plazo y adviertelo expresamente: tres meses desde el acuerdo, o un año si es contrario a la ley o a los estatutos.
5. **Situacion de pago** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Tratamos ahora el requisito de estar al corriente de pago." Explica: para impugnar hay que estar al corriente de todas las deudas vencidas o consignarlas judicialmente antes de demandar (articulo 18.2), con la unica excepcion de los acuerdos sobre establecimiento o alteracion de las cuotas de participacion del articulo 9. Si el cliente tiene deudas pendientes, explica las dos salidas (pagar o consignar) y sus consecuencias antes de continuar; no redactes la demanda dando por resuelto el requisito.
6. **Motivos de la impugnacion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a los motivos de la impugnacion." Explica los tres supuestos del articulo 18.1 (acuerdo contrario a la ley o a los estatutos; gravemente lesivo para la comunidad en beneficio de uno o varios propietarios; grave perjuicio para un propietario sin obligacion de soportarlo o adoptado con abuso de derecho) y, si el motivo es de mayorias, contrasta el acuerdo con el cuadro del articulo 17 recogido en `references/lph-reclamacion-y-acuerdos.md`. Elige con el cliente el supuesto y recoge despues los motivos concretos en prosa y los documentos que los acreditan. Confirmacion una a una.
7. **Suspension cautelar del acuerdo** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Valoramos ahora si conviene pedir la suspension del acuerdo." Explica: la impugnacion NO suspende la ejecucion del acuerdo; la suspension debe pedirse como medida cautelar, se acuerda oida la comunidad, exige justificar apariencia de buen derecho y peligro por la mora procesal, y normalmente conlleva prestar caucion (articulo 18.4 y articulos 721 y siguientes de la LEC). Pregunta despues si desea solicitarla y con que justificacion.
8. **Peticion adicional del suplico** *(clausula de negociacion)*. Anuncio fijo: "Concretamos que mas debe pedirse en la demanda ademas de la nulidad del acuerdo." Ejemplos que puedes ofrecer: devolucion de derramas ya cobradas, reposicion a la situacion anterior, condena a adoptar un nuevo acuerdo con la mayoria correcta. Si no hay ninguna, retirar el punto del suplico en lugar de dejarlo vacio.
9. **Intento de solucion previa** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Cerramos con el intento de solucion previa exigido antes de demandar." Explica que debe acreditarse el intento de negociacion (articulos 264.4º y 403.2 de la LEC) y que la solicitud de negociacion, si define bien su objeto, suspende el plazo de caducidad (articulo 7.1 de la Ley Organica 1/2025), pero que el computo se reanuda si no hay respuesta en treinta dias naturales. Recoge el tipo de intento y su fecha; si aun no se ha hecho, dejalo como placeholder y advierte de que la demanda no debe presentarse sin ese documento.
10. **Juzgado, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el juzgado, el lugar y la fecha del escrito." Partido judicial en el que radica la finca; lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA CESACION

1. **Datos de la comunidad y del presidente** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la comunidad y de quien firma el requerimiento." Sub-apartados: a) denominacion de la comunidad; b) NIF; c) direccion de la finca; d) nombre y NIF del presidente. Confirmacion agrupada.
2. **Datos del infractor** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de quien desarrolla la actividad." Sub-apartados: a) nombre o razon social; b) NIF o CIF si se conoce; c) si es propietario u ocupante del elemento privativo; d) elemento privativo; e) domicilio a efectos de notificaciones. Si es ocupante y no propietario, advierte de que conviene remitir copia al propietario, porque la eventual demanda debe dirigirse contra ambos (articulo 7.2). Confirmacion agrupada.
3. **Descripcion de la actividad** *(dato objetivo con validacion de sentido)*. Anuncio fijo: "Abordamos ahora la descripcion de la actividad." Pide los hechos con concrecion: en que consiste, desde cuando, con que frecuencia, en que horario y a quien afecta. No aceptes calificativos como unica respuesta ("es un escandalo", "son unos incivicos"): si la respuesta no aporta hechos verificables, explica por que no sirve y pide datos concretos antes de escribirla.
4. **Acreditacion** *(dato objetivo)*. Anuncio fijo: "Pasamos a los medios con los que se acredita." Recoge que pruebas existen: denuncias presentadas, actas de la policia local, mediciones sonometricas, informes tecnicos, actas de junta, comunicaciones previas, testimonios de vecinos.
5. **Fundamento de la prohibicion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora en que se apoya la prohibicion." Explica las tres vias del articulo 7.2 (actividad prohibida en los estatutos; actividad dañosa para la finca; actividad que contraviene las disposiciones generales sobre actividades molestas, insalubres, nocivas, peligrosas o ilicitas) y, si se trata de alquiler de uso turistico, el regimen del articulo 7.3 y la mayoria de tres quintos del articulo 17.12. Elige con el cliente la via y recoge su justificacion. Si invoca los estatutos, pide la clausula concreta.
6. **Plazo de cesacion y medidas solicitadas** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos el plazo y las medidas que se le exigen." Explica que la ley habla de cesacion inmediata, y que fijar ademas un plazo breve y razonable (practica habitual: entre diez y quince dias) refuerza la posicion de la comunidad sin debilitar la exigencia. Recoge el plazo y las medidas concretas que se piden.
7. **Ofrecimiento de solucion negociada** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Incluimos un ofrecimiento de solucion negociada." Explica que incorporar un ofrecimiento expreso de dialogo y un canal de contacto permite que el mismo documento sirva como intento de solucion previa si la comunidad tiene que demandar despues. Recoge la via de contacto.
8. **Consecuencias que se advierten** *(informativo, sin pregunta)*. Anuncio fijo: "Le informo de las consecuencias que se advertiran en el requerimiento." Expon lo que la sentencia estimatoria puede acordar: cesacion definitiva, indemnizacion de daños y perjuicios, privacion del derecho al uso de la vivienda o local por tiempo no superior a tres años y, si el infractor no es el propietario, extincion de sus derechos y lanzamiento inmediato. Recuerda ademas que el paso siguiente exige autorizacion de la junta debidamente convocada al efecto. No requiere dato del usuario; encadenar con la seccion siguiente.
9. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del requerimiento."

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo, hechos numerados con una idea por apartado, documentos relacionados y numerados, desglose en tabla en lugar de prosa, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5, muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una seccion existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

## Guardrails

1. Verificar siempre la LPH y la LEC en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder.
2. Si se detecta una version del texto consolidado posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar. No usar una version desactualizada.
3. La reclamacion de cuotas exige acuerdo previo de la junta que apruebe la liquidacion y autorice la reclamacion (articulos 21.1 y 21.2). Sin ese acuerdo no se genera la peticion inicial, por mucho que el usuario insista.
4. La certificacion debe expresar el importe adeudado Y SU DESGLOSE (articulo 21.3). Nunca emitir una certificacion con un importe global.
5. El visto bueno del presidente solo puede omitirse en el supuesto tasado del articulo 21.3 (secretario-administrador con cualificacion profesional legalmente reconocida que no vaya a intervenir profesionalmente en la reclamacion). No admitir otras excepciones.
6. La legitimacion para impugnar es tasada (articulo 18.2): quien voto a favor o se abstuvo sin salvar su voto no puede impugnar. No redactar la demanda en ese caso.
7. El requisito de estar al corriente de pago del articulo 18.2 solo decae para los acuerdos sobre establecimiento o alteracion de las cuotas de participacion del articulo 9. No extender la excepcion a otros acuerdos.
8. Los plazos del articulo 18.3 son de CADUCIDAD y no se interrumpen por reclamacion extrajudicial. Calcularlos siempre y advertir de su vencimiento; nunca dar por buena una impugnacion fuera de plazo.
9. Nunca afirmar que la impugnacion suspende el acuerdo: la suspension es cautelar, se pide, se justifica y suele exigir caucion (articulo 18.4).
10. El requerimiento del presidente es presupuesto de la accion de cesacion y debe ser fehaciente (articulo 7.2). Nunca presentar el requerimiento como si fuera ya la demanda, ni prometer la privacion del uso como resultado seguro.
11. Nunca inventar datos, importes, cuotas de participacion, fechas de junta, contenido de estatutos ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.
12. Si el usuario invoca estatutos o titulo constitutivo con reglas distintas de las legales, no suponer su contenido: pedirlos o escalar.

## Como NO se usa esta skill

- No es una herramienta de administracion de fincas: no elabora presupuestos, contabilidad, cuentas anuales, cuotas ni derramas.
- No convoca juntas, no redacta ordenes del dia ni levanta actas.
- No resuelve conflictos vecinales que carezcan de base en la Ley de Propiedad Horizontal (ruidos entre viviendas sin infraccion, discusiones personales, animales de compania sin prohibicion estatutaria ni infraccion administrativa): advertir y, en su caso, derivar.
- No redacta la demanda de la accion de cesacion del articulo 7.2 ni la demanda de juicio ordinario posterior a la oposicion en el monitorio: derivar a `derecho-civil-juicio-ordinario` y escalar.
- No redacta la oposicion del propietario al monitorio de la comunidad: derivar a `derecho-civil-reclamacion-cantidad` (plazo de veinte dias, que debe advertirse de inmediato).
- No se usa para reclamar cantidades que no sean gastos comunes ni fondo de reserva (por ejemplo, daños causados por un propietario a otro): derivar a `derecho-civil-reclamacion-cantidad`.
- No emite dictamenes sobre la validez de estatutos, la interpretacion del titulo constitutivo ni la naturaleza de un elemento comun o privativo: escalar.
- No sustituye la lectura de los estatutos ni del titulo constitutivo, que pueden alterar el regimen legal supletorio.

## Escalacion

| Situacion | Accion |
|---|---|
| Titulo constitutivo o estatutos con reglas que contradicen el regimen legal (cuotas, mayorias, usos permitidos, exenciones de gastos) | Detener la redaccion, pedir el documento y escalar: la skill no interpreta titulos constitutivos |
| Acuerdo u obra que afecta a la estructura, a la fabrica del edificio o a elementos comunes esenciales, o que implica modificacion del titulo constitutivo | Advertir del regimen de unanimidad y de los tres quintos del articulo 17 y escalar a especialista |
| Deudor en concurso de acreedores o con ejecucion hipotecaria en curso sobre el elemento privativo | Detener y escalar: la deuda queda sujeta a la normativa concursal o al orden de preferencia de la ejecucion |
| Plazo del articulo 18.3 vencido o a punto de vencer | Advertir de la caducidad, no dar falsas expectativas y escalar |
| Propietario impugnante con deudas vencidas que no puede pagar ni consignar | Advertir del obstaculo del articulo 18.2 y escalar antes de redactar |
| Actividad que puede constituir infraccion penal o administrativa grave (actividad ilicita, riesgo para la seguridad, insalubridad severa) | Advertir de la via penal o administrativa paralela y escalar |
| Infractor que es a la vez arrendatario y hay contrato de arrendamiento en juego | Advertir de la concurrencia con la LAU y coordinar con `derecho-civil-arrendamiento` o `derecho-civil-desahucio`; si hay litigio abierto, escalar |
| Alquiler de uso turistico con normativa autonomica o municipal en juego | Advertir de que la normativa sectorial turistica condiciona el caso y no es verificable desde una fuente estatal; escalar si es determinante |
| Discrepancia sobre si el acuerdo es nulo de pleno derecho o meramente anulable (con impacto en el plazo) | Advertir de que la distincion no esta cerrada y escalar |
| Litigio activo entre la comunidad y el propietario, o antecedentes de violencia | Escalar via escalate_to_attorney conforme a la matriz del plugin |
