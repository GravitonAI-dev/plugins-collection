---
name: derecho-civil-ejecucion-titulos
description: >
  Genera el escrito adecuado para ejecutar forzosamente un titulo ejecutivo dinerario conforme al
  Libro III de la LEC verificado en el BOE: demanda de ejecucion de titulo judicial (sentencia,
  decreto o auto firme, incluido el decreto que pone fin a un proceso monitorio sin oposicion, Art.
  517.2.1º y 9º LEC), demanda de ejecucion de titulo no judicial (escritura publica notarial, laudo
  arbitral o acuerdo de mediacion u otro MASC elevado a escritura publica, Art. 517.2.2º y 4º LEC,
  con el limite de 300 euros del Art. 520), demanda de ejecucion de pensiones y medidas de familia
  con las especialidades del Art. 776 LEC, y solicitud posterior de embargo de bienes designados y de
  investigacion judicial del patrimonio (Arts. 589, 590 y 592 LEC) cuando la ejecucion ya esta
  despachada. NO usar para la ejecucion hipotecaria (Art. 681 LEC), la ejecucion provisional de
  resoluciones no firmes, la oposicion del ejecutado, ni cuando el ejecutado este en concurso de
  acreedores.
when_to_use: |
  - El usuario tiene una sentencia, decreto o auto firme y el deudor no paga voluntariamente.
  - El usuario tiene una escritura publica, un laudo arbitral o un acuerdo de mediacion elevado a
    publico y quiere ejecutarlo por impago.
  - El usuario tiene un monitorio que termino sin oposicion ni pago y quiere instar el despacho de
    la ejecucion.
  - El usuario quiere ejecutar pensiones de alimentos, compensatoria u otras medidas de una sentencia
    o convenio de familia que no se estan pagando.
  - El usuario ya tiene una ejecucion despachada y quiere designar bienes, pedir el embargo o solicitar
    que el juzgado investigue el patrimonio del ejecutado.
inputs:
  - momento: demanda ejecutiva inicial / escrito posterior en ejecucion ya despachada
  - tipo_titulo: judicial (sentencia, decreto, auto, incluido monitorio firme) / no judicial (escritura, laudo, acuerdo MASC) / familia (pensiones y medidas)
  - subtipo_no_judicial: escritura publica notarial / laudo arbitral / acuerdo de mediacion u otro MASC elevado a publico
  - datos_ejecutante: nombre o razon social, NIF/CIF, domicilio, procurador y letrado si proceden
  - datos_ejecutado: nombre o razon social, NIF/CIF, domicilio
  - datos_titulo: descripcion, fecha, organo o notario, numero de autos o de protocolo
  - fecha_firmeza_o_vencimiento: firmeza del titulo judicial, o vencimiento de la obligacion no judicial
  - cantidad: principal, intereses vencidos, cantidad presupuestada para intereses y costas
  - bienes_conocidos: si / no, y su relacion si los hay
  - destinatarios_averiguacion: entidades u organismos a los que se pide oficio, y razon de cada uno
  - datos_familia: concepto (alimentos / compensatoria / mixto), relacion de mensualidades impagadas, si hay gastos extraordinarios no previstos
outputs:
  - demanda_ejecucion_titulo_judicial: demanda ejecutiva de titulo judicial o de familia en markdown, DRAFT
  - demanda_ejecucion_titulo_no_judicial: demanda ejecutiva de titulo no judicial en markdown, DRAFT
  - solicitud_embargo_averiguacion: escrito de designacion de bienes y averiguacion patrimonial en markdown, DRAFT
references:
  - references/lec-titulos-ejecutivos-y-plazos.md
  - references/embargo-averiguacion-inembargabilidad.md
  - references/especialidades-familia-776.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/demanda-ejecucion-titulo-judicial.md
  - assets/demanda-ejecucion-titulo-no-judicial.md
  - assets/solicitud-embargo-averiguacion-patrimonial.md
---

# Ejecucion Forzosa de Titulos Dinerarios

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija que la skill defina y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificacion normativa interna, ejecutala en silencio y continua hasta la primera pregunta o hasta la Confirmacion visible, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

Esta linea es, junto con la introduccion fija, la UNICA excepcion a la prohibicion de mencionar la mecanica interna. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, la validacion de presupuestos, la verificacion normativa y la creacion base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol.
- Resumenes de validacion con checks (ej. "Caducidad: ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez, en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin:

"Vamos a preparar el escrito que corresponda para hacer efectivo su derecho por la via de la ejecucion forzosa. Para determinarlo correctamente, es necesario precisar antes algunos datos."

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:

- **V1 (Momento del escrito):** demanda ejecutiva inicial / escrito posterior de embargo o investigacion patrimonial en una ejecucion que ya esta despachada.
- **V2 (Tipo de titulo — solo si V1 = demanda inicial):** titulo judicial o asimilado (sentencia, decreto, auto firme, incluido el decreto de un monitorio sin oposicion) / titulo no judicial (escritura, laudo, acuerdo de mediacion u otro MASC elevado a publico) / pensiones o medidas de una sentencia o convenio de familia.
- **V3 (Subtipo del titulo no judicial — solo si V2 = no judicial):** escritura publica notarial / laudo arbitral / acuerdo de mediacion u otro MASC elevado a escritura publica.
- **V4 (Bienes conocidos — en las tres hojas de demanda):** se conocen bienes concretos del ejecutado que se estiman suficientes / no se conocen o no se estiman suficientes.

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto (omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama):

* Para V1:
  "Lo que necesita preparar es:
  1. La demanda ejecutiva inicial
  2. Un escrito para pedir el embargo de bienes o la investigacion del patrimonio del deudor, en una ejecucion que ya esta despachada"

* Para V2 (solo si V1 = 1):
  "El titulo con el que cuenta es:
  1. Una sentencia, un decreto o un auto judicial firme (incluido el decreto que pone fin a un monitorio sin oposicion)
  2. Una escritura publica, un laudo arbitral o un acuerdo de mediacion u otro medio de solucion de controversias elevado a publico
  3. Una sentencia o un convenio de familia que reconoce una pension u otra medida economica que no se esta pagando"

* Para V3 (solo si V2 = 2):
  "El titulo no judicial es:
  1. Una escritura publica notarial
  2. Un laudo arbitral
  3. Un acuerdo de mediacion u otro medio de solucion de controversias elevado a escritura publica"

* Para V4 (en las tres hojas de demanda):
  "Respecto de los bienes del deudor:
  1. Conozco bienes concretos y los estimo suficientes para cubrir la deuda
  2. No conozco bienes suficientes y necesito que el juzgado los investigue"

**PRINCIPIO: Preguntas simples, no mega-preguntas.** Cada pregunta resuelve un unico punto de decision. No comprimas V2 y V3 en una sola pregunta.

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = 2 → **HOJA AVERIGUACION**: `assets/solicitud-embargo-averiguacion-patrimonial.md`. V2, V3 y V4 no se preguntan como vectores: los datos del titulo y de los bienes se recogen en prosa en la Seccion 5 de esta hoja.
- Si V1 = 1 y V2 = 1 → **HOJA JUDICIAL**: `assets/demanda-ejecucion-titulo-judicial.md`, con los bloques condicionales de familia DESACTIVADOS.
- Si V1 = 1 y V2 = 3 → **HOJA FAMILIA**: el mismo asset `assets/demanda-ejecucion-titulo-judicial.md`, con los bloques condicionales de familia ACTIVADOS (relacion de mensualidades, especialidades del Art. 776, Art. 608 si son alimentos o compensatoria).
- Si V1 = 1 y V2 = 2 → **HOJA NO-JUDICIAL**: `assets/demanda-ejecucion-titulo-no-judicial.md`, activando segun V3 el bloque de escritura publica, laudo o acuerdo de MASC elevado a publico.
- Si V1 = 1 y V2 = 2 y el titulo alegado es un titulo al portador o un certificado de anotaciones en cuenta (Art. 517.2.6º y 7º LEC) → estos supuestos no tienen bloque propio en el asset: recoger la descripcion en prosa, advertir de que es un supuesto poco frecuente y ofrecer escalacion si el usuario no esta seguro de que el documento lleve aparejada ejecucion.
- Si en cualquier momento consta o se sospecha que el ejecutado esta en concurso de acreedores → **DETENER**: no pueden iniciarse ejecuciones singulares contra la masa activa y las que estuvieran en curso quedan en suspenso y son nulas las actuaciones posteriores a la declaracion (Arts. 142 y 143 TRLC). Advertir y escalar a concursal. No crear documento.
- Si lo que se pretende es la ejecucion hipotecaria, la ejecucion provisional de una resolucion no firme, o redactar la oposicion del ejecutado → **DETENER**: fuera de alcance. Advertir y escalar.

### Validacion de presupuestos (interno, antes del Punto 3)

- **HOJA JUDICIAL y HOJA FAMILIA (Art. 518 LEC):** confirmar la fecha de firmeza y calcular si han transcurrido menos de cinco anos. Si el plazo esta agotado, **detener y advertir**: no crear el documento. En pensiones periodicas, cada mensualidad tiene su propio vencimiento: la caducidad puede afectar solo a las mensualidades mas antiguas; en caso de duda sobre mensualidades concretas, escalar.
- **HOJA JUDICIAL y HOJA FAMILIA (Art. 548 LEC):** confirmar que han transcurrido veinte dias desde la firmeza (o desde la notificacion de la aprobacion del convenio). Si no han transcurrido, advertir de que el juzgado no despachara la ejecucion todavia y ofrecer esperar. En familia, aplicar la misma regla de forma conservadora (ver `references/especialidades-familia-776.md`, apartado 6, y la nota de verificacion manual de `references/fuentes-plantillas-validadas.md`): no afirmar que el plazo no aplica a las pensiones sin haberlo verificado.
- **HOJA NO-JUDICIAL (Art. 520 LEC):** confirmar que la cantidad reclamada excede de 300 euros y es liquida (Art. 572.1). Si no llega a 300 euros con un unico titulo, preguntar si hay otros titulos ejecutivos de la misma naturaleza para sumarlos (Art. 520.2). Si aun asi no se alcanza el limite, **detener**: no procede esta via, advertir y ofrecer el juicio declarativo que corresponda por cuantia (derivar a `derecho-civil-reclamacion-cantidad`).
- **HOJA NO-JUDICIAL:** si el titulo es un laudo o un acuerdo de mediacion, si se aplica el plazo de espera de veinte dias del Art. 548; si es escritura publica notarial, NO se aplica y puede ejecutarse desde el vencimiento.
- **HOJA FAMILIA (Art. 776.4ª LEC):** si el cliente incluye un gasto extraordinario que NO figura en el titulo con su reparto ya fijado, ese concepto NO puede reclamarse en esta misma demanda: requiere antes una declaracion judicial de que tiene la consideracion de gasto extraordinario. Separar ese concepto, advertir de la doble via y no incluirlo en el desglose de la demanda ejecutiva salvo que el cliente confirme que ya cuenta con esa declaracion previa.
- **TODAS LAS HOJAS (Art. 538 LEC):** verificar que el despacho se pide solo frente a quien figura como deudor en el titulo, o frente a quien responda personalmente por ley o afianzamiento en documento publico, o frente al titular de bienes especialmente afectos. Nunca dirigir la ejecucion contra un tercero no amparado por el titulo: genera responsabilidad por danos y perjuicios (Art. 538.4).
- **HOJA NO-JUDICIAL, titulo de consumo (Arts. 551.2.5º y 552 LEC):** si el titulo deriva de un contrato entre empresario o profesional y consumidor, advertir del control de oficio de clausulas abusivas y, si alguna clausula que determina la cantidad exigible es potencialmente abusiva (intereses moratorios desproporcionados, vencimiento anticipado, comisiones), ofrecer revision por especialista antes de cerrar la cuantia.
- **MASC:** no es requisito de procedibilidad de ninguna demanda ejecutiva (Art. 5.3 LO 1/2025). No preguntar por el intento de solucion previa en ninguna hoja de esta skill.

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" de la LEC (Libro III), de la LO 1/2025, del TRLC y del Real Decreto del SMI del ejercicio en curso.

**2.2 — Consultar la fuente oficial vigente.** La API de legislacion consolidada del BOE devuelve el bloque de un articulo concreto (requiere cabecera `Accept: application/xml`):
```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a{numero_articulo}
```
Consultar de la LEC (BOE-A-2000-323) los bloques de los arts. 517, 518, 520, 538, 539, 545, 548, 549, 550, 571 a 576, 578, 589, 590, 592, 605 a 608 y, si la hoja es de familia, 776. Consultar ademas el TRLC (BOE-A-2020-4859), arts. 142 y 143, y verificar si existe un Real Decreto del SMI mas reciente que el registrado en `references/embargo-averiguacion-inembargabilidad.md`.

**2.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar Write/Edit para:
- Actualizar `references/lec-titulos-ejecutivos-y-plazos.md`, `references/embargo-averiguacion-inembargabilidad.md` y/o `references/especialidades-familia-776.md` con la redaccion vigente.
- Si cambia el SMI del ejercicio, actualizar la tabla de tramos de `references/embargo-averiguacion-inembargabilidad.md`.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada, y nunca calcular un embargo de sueldo con un SMI de un ejercicio anterior sin haberlo verificado.

**2.5 — Fallback si la fuente no es accesible.** Si la lectura falla (error HTTP, timeout):
```
web_search("Ley Enjuiciamiento Civil ejecucion titulos judiciales articulos 517 518 548 549 575 texto consolidado BOE")
web_search("salario minimo interprofesional [ano en curso] Real Decreto BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. El documento se genera con la version de referencia. Verificar manualmente antes de presentar."

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Textos fijos por hoja:
   - JUDICIAL: "A su caso corresponde la ejecucion de un titulo judicial, conforme a los articulos 517.2 y 549 de la Ley 1/2000, de Enjuiciamiento Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - NO-JUDICIAL: "A su caso corresponde la ejecucion de un titulo no judicial, conforme a los articulos 517.2, 520 y 549 de la Ley 1/2000, de Enjuiciamiento Civil. Solo procede si la cantidad reclamada excede de 300 euros. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - FAMILIA: "A su caso corresponde la ejecucion de pensiones o medidas de familia, que se tramita conforme al Libro III de la Ley 1/2000, de Enjuiciamiento Civil, con las especialidades de su articulo 776. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - AVERIGUACION: "Corresponde un escrito de designacion de bienes y de solicitud de investigacion patrimonial dentro de la ejecucion ya despachada, conforme a los articulos 589, 590 y 592 de la Ley 1/2000, de Enjuiciamiento Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - En las tres hojas de demanda, anadir: "No es necesario acreditar el intento de una solucion extrajudicial previa para presentar una demanda ejecutiva (articulo 5.3 de la Ley Organica 1/2025)."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio.

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento:

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa e investigacion: incluida `fecha_verificacion_lec` del Punto 2). Los faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{fecha_firmeza}}`, `{{numero_autos_origen}}`); usa un marcador generico solo para un hueco suelto sin placeholder propio, y nunca repitas el mismo marcador generico dos veces en el mismo documento (`Edit` necesita un `oldString` unico).
3. Utiliza `Write` para guardar el archivo en disco (nombre en `snake_case.md`, ej. `demanda_ejecucion_titulo_judicial_ejecutante_a.md`, `demanda_ejecucion_titulo_no_judicial_ejecutante_a.md`, `solicitud_embargo_averiguacion_ejecucion_123.md`).
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. Inmediatamente despues, en la misma respuesta, pregunta si desea empezar a completar los datos del documento. Solo tras la confirmacion, formula la primera pregunta de la edicion incremental (Punto 5).

Los bloques condicionales del asset que dependan de decisiones aun no tomadas se OMITEN en este `Write` y se insertan durante el Punto 5, releyendo el asset y copiando el bloque sin el envoltorio de comentario.

## 5. EDICION INCREMENTAL DE SECCIONES

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas de negociacion se explican y se confirman una a una. **La vista previa y la confirmacion agrupada de una parte se emiten en el turno SIGUIENTE a la respuesta del ultimo sub-apartado, nunca en el mismo turno en que aun se esta preguntando ese ultimo dato**: primero se pregunta y se recibe la respuesta, y solo despues, en el turno posterior, se muestra la vista previa conjunta y se pide la confirmacion.

### Secciones — HOJA JUDICIAL y HOJA FAMILIA

1. **Parte ejecutante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte ejecutante." Sub-apartados, uno por turno: a) nombre completo o razon social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) nombre del procurador y del letrado, si intervienen. Pregunta antes, en prosa y con las dos opciones en la misma frase: "En el procedimiento de origen del titulo, ¿eran preceptivos abogado y procurador, o se trata de un decreto de monitorio sin oposicion o de un laudo o acuerdo de mediacion por una cantidad que no supera 2.000 euros?" y activa segun la respuesta el parrafo de comparecencia con o sin representacion. Al completar el ultimo dato, vista previa unica y una sola confirmacion antes del `Edit`.
2. **Parte ejecutada** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte ejecutada." Sub-apartados: a) nombre o razon social; b) NIF o CIF; c) domicilio. Confirmacion agrupada.
3. **El titulo ejecutivo** *(dato objetivo con validacion)*. Anuncio fijo: "Describimos ahora el titulo en que se funda la ejecucion." Sub-apartados, uno por turno: a) tipo de resolucion (sentencia, decreto o auto) y organo que la dicto; b) numero de autos del procedimiento de origen; c) contenido de la condena tal como figura en el fallo; d) fecha de firmeza. Si el titulo es el decreto de un monitorio sin oposicion, sustituye el hecho por la variante del asset (terminacion del monitorio, Art. 816 LEC) y pide la fecha del decreto en lugar de la de firmeza.
4. **Plazos** *(dato objetivo con validacion bloqueante)*. Anuncio fijo: "Verificamos ahora los plazos de la ejecucion." Con la fecha de firmeza ya conocida, calcula tu mismo si han transcurrido los veinte dias del Art. 548 y si no han pasado los cinco anos del Art. 518. Si el primero no se ha cumplido, informa de la fecha en que se cumplira y pregunta si desea continuar preparando el escrito para presentarlo entonces. Si el segundo esta agotado, aplica el guardrail correspondiente y detente.
5. **Cantidad reclamada** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a determinar la cantidad por la que se despachara la ejecucion." Explica antes de pedir cifras: se reclama el principal, los intereses ya vencidos y una cantidad presupuestada para intereses de la ejecucion y costas que no puede superar el 30 % de lo anterior (Art. 575 LEC), salvo justificacion excepcional; si el bien a ejecutar es la vivienda habitual del ejecutado, las costas exigibles no pueden superar el 5 %. En HOJA FAMILIA, sustituye la pregunta de principal por la relacion mensualidad a mensualidad (mes e importe) siguiendo `references/especialidades-familia-776.md`, apartado 3, y pregunta si el titulo prevee actualizacion periodica antes de aplicarla. Pide despues, en turnos separados: a) principal (o relacion de mensualidades); b) intereses vencidos y su fundamento de calculo; c) porcentaje presupuestado para intereses y costas (por defecto, ofrece el 30 %, o el 5 % si es vivienda habitual, y pregunta si desea un porcentaje menor). Confirmacion propia de cada uno.
6. **Gastos extraordinarios de familia** *(clausula de negociacion — solo HOJA FAMILIA, condicional)*. Anuncio fijo: "Concretamos si existen gastos extraordinarios que reclamar." Explica antes de preguntar: solo pueden incluirse en esta demanda los gastos extraordinarios que el titulo ya prevea con su reparto; los demas exigen una declaracion judicial previa (Art. 776.4ª LEC) y no pueden mezclarse en este escrito. Pregunta si hay gastos extraordinarios y, para cada uno, si figura en el titulo con su reparto. Los que no lo esten, apartalos, adviertelo expresamente y no los incluyas en el desglose.
7. **Bienes del ejecutado** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora los bienes sobre los que actuara la ejecucion." El valor de V4 ya esta resuelto. Si se conocen bienes: explica el orden del Art. 592 LEC (mayor facilidad de enajenacion y menor onerosidad primero; la escala de nueve rangos solo si eso no es posible, y recuerda que los inmuebles ocupan el puesto 7 y los sueldos el 8) y pide la relacion de bienes con datos identificativos suficientes para trabarlos sin nueva investigacion. Si no se conocen: explica que se pedira el requerimiento de manifestacion de bienes del Art. 589 y, si el cliente puede indicar destinatarios concretos de oficios de investigacion (Art. 590), pide cada destinatario y la razon por la que se cree que dispone de informacion; si no tiene ninguno, deja el OTROSI con la peticion generica de manifestacion de bienes y advierte de que la investigacion patrimonial exige destinatarios concretos que podra completar mas adelante con el escrito de la HOJA AVERIGUACION.
8. **Ampliacion automatica** *(clausula de negociacion — explicar antes de decidir; solo si quedan plazos pendientes de vencer)*. Anuncio fijo: "Valoramos si interesa que la ejecucion se amplie automaticamente con los proximos vencimientos." Aplica solo si la obligacion es de tracto sucesivo (pensiones, rentas, plazos pendientes). Explica el Art. 578 LEC: evita presentar un escrito nuevo cada vez que venza una mensualidad y no se pague. Pregunta si desea solicitarla; si la deuda esta integramente vencida, omite la seccion sin preguntar.
9. **Multas coercitivas** *(clausula de negociacion — solo HOJA FAMILIA, condicional)*. Anuncio fijo: "Valoramos si procede pedir multas coercitivas por el incumplimiento reiterado." Explica que son acumulativas al cobro de lo debido, no sustitutivas (Art. 776.1ª LEC), y que requieren incumplimiento reiterado, no un unico impago. Pregunta si el incumplimiento ha sido reiterado y, si es asi, incluye el OTROSI.
10. **Inaplicacion del limite de embargo de sueldos** *(clausula de negociacion — solo HOJA FAMILIA y solo si se reclaman alimentos o compensatoria)*. Anuncio fijo: "Determinamos el regimen de embargo de sueldos aplicable." Si es alimentos: explica que el Art. 607 no se aplica por ministerio de la ley (Art. 608) y que sera el tribunal quien fije la cantidad embargable; no requiere mas dato. Si es compensatoria: explica que la exclusion es rogada y exige acreditar una necesidad economica; pregunta si puede acreditarla y con que medios, y si no puede, informa de que se aplicara la escala ordinaria del Art. 607.
11. **Clausulas abusivas** *(informativo, solo si el titulo no judicial deriva de un contrato con consumidor — se resuelve realmente en la HOJA NO-JUDICIAL, pero si el titulo de familia incorporase un pacto de esa naturaleza, adviertelo igual)*.
12. **Postulacion y documentos** *(dato objetivo)*. Anuncio fijo: "Cerramos con los documentos que se acompanaran." Pregunta que documentos se aportaran ademas del titulo (poder, testimonios, certificaciones) y numeralos correlativamente con los hechos.
13. **Juzgado, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Determinamos el juzgado competente y cerramos con el lugar y la fecha." El competente es el que conocio del asunto en primera instancia o el que homologo la transaccion o acuerdo (Art. 545.1 LEC): confirma con el usuario cual fue y no admitas sumision a otro fuero. Lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA NO-JUDICIAL

1. **Parte ejecutante** *(dato objetivo — confirmacion agrupada por parte)*. Igual que en la HOJA JUDICIAL, pero la pregunta de postulacion se formula solo si V3 = laudo o acuerdo de mediacion: "¿La cantidad por la que va a despachar la ejecucion supera los 2.000 euros?" (si supera, preceptivos; si no, no preceptivos). Si V3 = escritura publica notarial, abogado y procurador son siempre preceptivos: no preguntar.
2. **Parte ejecutada** *(dato objetivo — confirmacion agrupada por parte)*. Igual que en la HOJA JUDICIAL.
3. **El titulo no judicial** *(dato objetivo con validacion, segun V3)*. Anuncio fijo: "Describimos ahora el titulo en que se funda la ejecucion." Segun V3: escritura publica (notario, plaza, fecha, numero de protocolo), laudo arbitral (fecha, arbitro o institucion, referencia del procedimiento, y confirmar que se aportaran el convenio arbitral y la acreditacion de notificacion), o acuerdo de mediacion u otro MASC elevado a publico (tipo de MASC, fecha del acuerdo, notario, fecha y numero de protocolo de la escritura, y confirmar que se aportaran las actas de la sesion constitutiva y final).
4. **Obligacion y vencimiento** *(dato objetivo)*. Anuncio fijo: "Pasamos a la obligacion documentada y a su vencimiento." Sub-apartados: a) descripcion de la obligacion; b) fecha de vencimiento. Verifica que la cantidad supera los 300 euros (Art. 520 LEC); si no, aplica la validacion de presupuestos ya descrita.
5. **Liquidacion por saldo** *(clausula de negociacion — solo si el titulo pacto liquidacion unilateral, Art. 572.2 LEC)*. Anuncio fijo: "Abordamos la liquidacion del saldo prevista en el titulo." Explica los requisitos acumulativos: notificacion previa al ejecutado y al fiador, y los tres documentos del Art. 573.1. Pregunta la clausula que lo pacta, el saldo resultante y si se acredita la notificacion. Si el interes es variable, pide ademas las operaciones de calculo del Art. 574.
6. **Cantidad reclamada** *(clausula de negociacion — explicar antes de decidir)*. Igual estructura que en la HOJA JUDICIAL (principal, intereses, porcentaje presupuestado con el limite del 30 %).
7. **Bienes del ejecutado** *(clausula de negociacion — explicar antes de decidir)*. Igual que en la HOJA JUDICIAL.
8. **Clausulas abusivas** *(clausula de negociacion — solo si el titulo deriva de un contrato con un consumidor)*. Anuncio fijo: "Verificamos si el titulo esta sujeto al control de clausulas abusivas." Explica que el juzgado examinara de oficio si las clausulas que fundan la ejecucion y determinan la cantidad exigible son abusivas (Arts. 551.2.5º y 552 LEC). Pregunta si el ejecutado es consumidor y, si lo es, si alguna clausula relevante (intereses moratorios, vencimiento anticipado, comisiones) podria ser desproporcionada; si hay duda razonable, advierte y ofrece revision por especialista antes de continuar.
9. **Reserva de partidas dudosas** *(clausula de negociacion — solo si hay liquidacion por saldo y el acreedor duda de alguna partida)*. Anuncio fijo: "Valoramos si conviene reservar alguna partida dudosa." Explica el Art. 573.3: cabe pedir el despacho por la cantidad indubitada y reservar el resto para el declarativo. Pregunta si desea acogerse a esta reserva.
10. **Ampliacion automatica** *(clausula de negociacion — solo si quedan plazos pendientes de vencer)*. Igual que en la HOJA JUDICIAL.
11. **Juzgado, lugar y fecha** *(dato objetivo con explicacion)*. Anuncio fijo: "Determinamos el juzgado competente y cerramos con el lugar y la fecha." Explica la regla del Art. 545.2 y 545.3 LEC segun V3 (laudo o mediacion: lugar donde se dicto o se firmo; demas titulos: a eleccion del ejecutante, el de los Arts. 50-51, el del lugar de cumplimiento o el de donde haya bienes embargables, sin sumision posible) y pide la eleccion. Lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA AVERIGUACION

1. **Datos de la ejecucion en curso** *(dato objetivo)*. Anuncio fijo: "Comenzamos por identificar la ejecucion ya despachada." Sub-apartados, uno por turno: a) juzgado y numero de autos de la ejecucion; b) fecha del auto de despacho; c) cantidad total por la que se despacho, desglosada en principal, intereses vencidos y cantidad presupuestada; d) estado del cobro (nada cobrado, o cantidad ya obtenida y pendiente restante).
2. **Parte ejecutante** *(dato objetivo — confirmacion agrupada por parte)*. Igual estructura que en las otras hojas, con la pregunta de postulacion si procede.
3. **Bienes designados** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos los bienes que se designan para el embargo." Igual explicacion del orden del Art. 592 LEC. Si no hay bienes que designar, pide una breve descripcion de las gestiones ya realizadas para localizarlos.
4. **Insuficiencia y peticion de investigacion** *(dato objetivo con validacion)*. Anuncio fijo: "Justificamos ahora por que es necesaria la investigacion patrimonial." Recuerda que el requerimiento del Art. 589 solo se acuerda si el ejecutante no ha senalado bienes suficientes: si los designados en la seccion anterior ya cubren la cantidad, adviertelo y desactiva esta seccion.
5. **Destinatarios de los oficios** *(dato objetivo con validacion de sentido)*. Anuncio fijo: "Relacionamos los destinatarios de los oficios de investigacion y la razon de cada uno." Por cada destinatario, uno por turno: nombre de la entidad u organismo y razon concreta por la que se cree que dispone de informacion (usa `references/embargo-averiguacion-inembargabilidad.md`, apartado 3, para orientar al cliente si no sabe que destinatarios proponer). Rechaza una razon generica del tipo "por si acaso": pide que la concrete antes de escribirla, porque el Art. 590 exige expresarla sucintamente.
6. **Limites de inembargabilidad** *(informativo, con excepcion condicional)*. Anuncio fijo: "Le informo de los limites de inembargabilidad aplicables." Si la ejecucion es de alimentos o de compensatoria con necesidad acreditada, aplica la excepcion del Art. 608 y explica que es el tribunal quien fija la cantidad embargable; en los demas casos, recuerda la escala del Art. 607 sobre el SMI vigente verificado en el Punto 2. No requiere mas dato salvo, en compensatoria, la acreditacion de la necesidad economica.
7. **Multas coercitivas por incumplimiento del Art. 589** *(clausula de negociacion — condicional, solo si el ejecutado ya fue requerido y no respondio)*. Anuncio fijo: "Valoramos si procede pedir multas coercitivas por no haber manifestado bienes." Pregunta la fecha del requerimiento anterior y el detalle del incumplimiento.
8. **Ampliacion de la ejecucion por nuevos vencimientos** *(clausula de negociacion — condicional)*. Anuncio fijo: "Valoramos si han vencido nuevos plazos que ampliar." Si la obligacion es de tracto sucesivo y han vencido nuevos plazos desde el despacho, pregunta su importe y detalle.
9. **Juzgado, lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito."

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve (una ejecucion no reargumenta el pleito), HECHOS o ALEGACIONES numerados con una idea por apartado, documentos relacionados y numerados, desglose siempre por conceptos, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5, muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una seccion existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

## Guardrails

1. Verificar siempre la LEC, la LO 1/2025 y el TRLC en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder.
2. Si se detecta una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar. No usar una version desactualizada, y nunca calcular un tramo de embargo de sueldo con un SMI de un ejercicio anterior sin verificarlo.
3. La accion ejecutiva de titulos judiciales, laudos y acuerdos de mediacion caduca a los cinco anos desde la firmeza (Art. 518 LEC). Si el plazo esta agotado, no redactar la demanda: advertir y ofrecer escalacion. Este plazo NO se aplica a la escritura publica notarial.
4. No se despachara ejecucion de titulos judiciales, laudos o acuerdos de mediacion dentro de los veinte dias posteriores a la firmeza o notificacion (Art. 548 LEC). Advertir siempre de esta espera; no aplica a los demas titulos no judiciales.
5. Solo cabe despachar ejecucion frente a quien figure como deudor en el titulo o se encuentre en los supuestos tasados de los Arts. 538 a 544 LEC. Nunca dirigir la ejecucion contra un tercero no amparado por el titulo: genera responsabilidad por danos y perjuicios (Art. 538.4).
6. En titulo no judicial, la cantidad debe exceder de 300 euros y ser liquida (Art. 520 LEC). Sin ese minimo, no procede esta via.
7. La cantidad presupuestada para intereses de la ejecucion y costas no puede superar el 30 % de lo reclamado (5 % si es vivienda habitual del ejecutado, Art. 575.1 bis LEC), salvo justificacion excepcional. Nunca redactar un desglose sin esta cantidad ni por encima de estos limites sin justificarlo.
8. En familia, los gastos extraordinarios no previstos expresamente en el titulo con su reparto NO pueden incluirse en la demanda ejecutiva sin la previa declaracion judicial del Art. 776.4ª LEC. Separarlos siempre y no mezclarlos con el resto de la deuda.
9. En alimentos, el limite del Art. 607 no se aplica por ministerio de la ley (Art. 608). En pension compensatoria, esa exclusion es rogada y exige acreditar necesidad economica: nunca aplicarla sin que el cliente la acredite.
10. Si consta o se sospecha que el ejecutado esta en concurso de acreedores, detener de inmediato: no pueden iniciarse ejecuciones singulares contra la masa activa (Arts. 142 y 143 TRLC).
11. No es exigible acreditar el intento de un medio adecuado de solucion de controversias para presentar una demanda ejecutiva (Art. 5.3 LO 1/2025). Nunca pedir ese dato en esta skill.
12. Nunca inventar datos, cuantias, fechas, numeros de protocolo ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.
13. Cuando el impago de pensiones de familia alcance dos meses consecutivos o cuatro no consecutivos, informar de que la conducta puede tener relevancia penal (Art. 227 del Codigo Penal) y ofrecer escalacion a un especialista en penal. Nunca redactar denuncia ni querella: excede el alcance de esta skill.

## Como NO se usa esta skill

- No usar para la ejecucion hipotecaria ni para el lanzamiento derivado de ella (Art. 681 LEC y siguientes): proceso especial, fuera de alcance.
- No usar para la ejecucion provisional de resoluciones no firmes (Art. 524 LEC).
- No usar para redactar la oposicion del ejecutado (Arts. 556 y 557 LEC): posicion contraria, fuera de alcance.
- No usar para el extenso de vivienda y ejecuciones de desahucio: derivar a `derecho-civil-desahucio`.
- No usar para reclamar una deuda que aun no tiene titulo ejecutivo: derivar a `derecho-civil-reclamacion-cantidad` (monitorio, verbal u ordinario segun cuantia).
- No usar para modificar el regimen de custodia o visitas por incumplimiento reiterado (Art. 776, especialidad 3ª): derivar a `derecho-civil-modificacion-medidas` si existe en el marketplace, o escalar.
- No usar si el usuario pide opinion juridica sobre la estrategia de la ejecucion: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Ejecutado en concurso de acreedores, declarado o indiciario | Detener de inmediato: no pueden iniciarse ejecuciones singulares contra la masa activa (Arts. 142 y 143 TRLC) |
| Caducidad de la accion ejecutiva agotada (Art. 518 LEC) | Advertir de que no procede la ejecucion y ofrecer escalacion; no dar falsas expectativas |
| Bienes del ejecutado en el extranjero | Escalar: la ejecucion transfronteriza excede el alcance de esta skill |
| Impago de pensiones de dos meses consecutivos o cuatro no consecutivos | Informar de la posible relevancia penal (Art. 227 CP) y ofrecer escalacion a especialista en penal |
| Duda sobre si un gasto de familia es ordinario o extraordinario | Adoptar la posicion conservadora, no incluirlo en la demanda y ofrecer escalacion |
| Titulo derivado de contrato de consumo con clausula potencialmente abusiva y determinante de la cuantia | Advertir del control de oficio del Art. 552 LEC y ofrecer revision por especialista |
| Ejecucion hipotecaria o de otro proceso especial de realizacion de garantia | Escalar: fuera de alcance |
| Titulo al portador o certificado de anotaciones en cuenta (Art. 517.2.6º y 7º LEC) | Supuesto poco frecuente sin bloque propio en el asset: recoger la descripcion, advertir y ofrecer escalacion si hay duda sobre si lleva aparejada ejecucion |
| Pluralidad de deudores solidarios con titulo obtenido solo frente a alguno de ellos | Advertir de la limitacion del Art. 542 LEC (titulos judiciales) y escalar si hay duda |
| Litigio conexo, reconvencion previsible u oposicion ya anunciada por el ejecutado | Escalar via `escalate_to_attorney` |
