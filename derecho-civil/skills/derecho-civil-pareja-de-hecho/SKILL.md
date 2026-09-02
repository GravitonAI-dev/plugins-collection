---
name: derecho-civil-pareja-de-hecho
description: >
  Genera la documentacion propia de la pareja de hecho en sus tres momentos: (1) CONSTITUCION —
  checklist de inscripcion en el registro autonomico de parejas de hecho, con los requisitos, la
  documentacion y el tramite verificados en el lanzamiento contra la normativa de la comunidad
  autonoma concreta; (2) CONVIVENCIA — pacto de convivencia otorgado al amparo del articulo 1255 del
  Codigo Civil, que regula el regimen de los bienes de cada uno, los bienes adquiridos en comun y las
  aportaciones desiguales (arts. 392 a 406 CC), la vivienda, la contribucion a los gastos, las deudas
  y, si asi se pacta expresamente, una compensacion economica por la dedicacion a la familia o al
  negocio del otro; y (3) RUPTURA — pacto de extincion de la convivencia y liquidacion de la comunidad
  de bienes, con la cancelacion de la inscripcion registral, el destino de la vivienda y del prestamo
  hipotecario, las deudas y la compensacion que en su caso se convenga. NO existe ley estatal de
  parejas de hecho ni registro estatal: la skill pregunta SIEMPRE la comunidad autonoma y verifica su
  ley y su registro con `web_search` en cada lanzamiento, sin afirmar nunca un requisito autonomico de
  memoria. NO regula custodia, alimentos ni visitas de los hijos comunes (deriva a
  `derecho-civil-medidas-hijos-no-matrimoniales`), NO cubre matrimonio, separacion ni divorcio, NO
  tramita la inscripcion ante el registro, NO cubre extranjeria ni reagrupacion familiar y NO resuelve
  el derecho a la pension de viudedad, del que solo informa.
when_to_use: |
  - Una pareja quiere constituirse e inscribirse como pareja de hecho y necesita saber que requisitos y
    que documentacion exige el registro de su comunidad autonoma.
  - Una pareja que convive quiere regular por escrito los aspectos economicos de su convivencia
    (bienes, vivienda, gastos, deudas, compensaciones).
  - Han comprado juntos una vivienda con aportaciones desiguales y quieren dejar constancia de ello.
  - Una pareja de hecho se separa y quiere liquidar de comun acuerdo lo que tienen en comun.
  - El usuario pregunta que derechos le da inscribirse como pareja de hecho, si hereda de su pareja o
    si tendra derecho a una compensacion si se separan.
inputs:
  - finalidad: constituir e inscribir la pareja / regular la convivencia mediante pacto / regular la ruptura
  - comunidad_autonoma: comunidad de residencia de la pareja (vector obligatorio en todas las ramas)
  - hijos_comunes: si / no (determina la derivacion a la skill de medidas de hijos no matrimoniales)
  - bienes_o_desequilibrio: hay bienes adquiridos en comun o desequilibrio economico entre ellos / no
  - datos_conviviente_a: nombre, documento de identidad, domicilio
  - datos_conviviente_b: nombre, documento de identidad, domicilio
  - datos_convivencia: fecha de inicio, domicilio comun, situacion registral y, en su caso, fecha de cese
  - bienes_comunes: relacion de bienes adquiridos conjuntamente, titularidad formal y aportaciones reales
  - vivienda: situacion juridica, titularidad, prestamo hipotecario y destino del uso
  - gastos_y_deudas: criterio de contribucion, cuenta comun, deudas conjuntas
  - dedicacion: dedicacion de uno a la familia o al negocio del otro y compensacion que se pacte
  - liquidacion: acuerdo de adjudicacion, venta o compensacion de cuotas (solo ruptura)
outputs:
  - checklist_inscripcion_registro: checklist de requisitos, documentacion y tramite del registro
    autonomico, en markdown, DRAFT, con la fecha de verificacion de la normativa autonomica
  - pacto_convivencia: pacto de convivencia en markdown, DRAFT
  - pacto_ruptura_pareja_hecho: pacto de extincion de la convivencia y liquidacion en markdown, DRAFT
references:
  - references/regimen-pareja-hecho-derecho-comun.md
  - references/verificacion-normativa-autonomica.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/checklist-inscripcion-registro.md
  - assets/pacto-convivencia.md
  - assets/pacto-ruptura-pareja-hecho.md
---

# Constitucion, Convivencia y Ruptura de la Pareja de Hecho

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija del Punto 1 y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

**Si la Escucha Activa no deja ninguna pregunta de clasificacion pendiente** — situacion frecuente en la rama de inscripcion, donde V3 y V4 no se preguntan y basta con que el usuario haya dicho que quiere inscribirse y donde vive —, no te quedes sin pregunta ni saltes en silencio a la verificacion. Cierra el turno pidiendo que confirme la residencia habitual de ambos, que es a la vez la confirmacion de la comunidad autonoma que has deducido y un requisito de constitucion que tendras que contrastar de todos modos: "Confirmeme que ambos tienen su residencia habitual en {{municipio_deducido}}, y por tanto en {{comunidad_autonoma}}, para verificar la normativa que les resulta de aplicacion." Nunca des por buena una comunidad deducida de un municipio sin que el usuario la haya confirmado: de ella depende toda la verificacion del Punto 2.3.

Esta linea es, junto con la introduccion fija del Punto 1 y los anuncios de seccion del Punto 5, la UNICA excepcion a la Directiva de Invisibilidad. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, la verificacion normativa, la validacion de presupuestos y la creacion base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol.
- Resumenes de validacion con checks (ej. "Comunidad autonoma: ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin. No afirmes todavia que normativa aplica: la comunidad autonoma aun no se ha resuelto y **no existe una regulacion estatal comun** que puedas anticipar.

"Vamos a preparar la documentacion que corresponda a su situacion de pareja de hecho. Debo advertirle de entrada que esta materia no tiene una ley estatal: cada comunidad autonoma la regula de forma distinta, de modo que necesitare precisar algunos datos antes de empezar."

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:

- **V1 (Finalidad):** constituir e inscribir la pareja / regular la convivencia mediante pacto / regular la ruptura.
- **V2 (Comunidad autonoma):** comunidad de residencia de la pareja. **Vector OBLIGATORIO en las tres ramas, sin excepcion.** Determina la ley aplicable, el registro competente, los requisitos de constitucion y los efectos, y **se verifica siempre con `web_search` en el Punto 2, nunca se da por sabido**.
- **V3 (Hijos comunes — solo si V1 = ruptura):** si / no. Determina la derivacion a `derecho-civil-medidas-hijos-no-matrimoniales` y la activacion del bloque de remision del asset.
- **V4 (Bienes comunes o desequilibrio economico — solo si V1 = convivencia o ruptura):** hay bienes adquiridos en comun, aportaciones desiguales o desequilibrio economico entre ellos / no hay ninguna de las tres cosas. Determina los bloques de comunidad de bienes y de compensacion.

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto (omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama):

* Para V1:
  "Lo que necesita es:
  1. Constituir e inscribir su pareja de hecho en el registro que corresponda
  2. Regular por escrito los aspectos economicos de su convivencia
  3. Regular la ruptura y liquidar lo que tienen en comun"

* Para V2, **en prosa y con respuesta libre**, no en lista numerada:
  "Indique la comunidad autonoma en la que residen."

  *(Justificacion interna de la excepcion al formato de alternativas numeradas: hay diecisiete comunidades autonomas y una lista de diecisiete opciones seria precisamente la mega-pregunta que el estandar prohibe. Ademas V2 no enruta a ningun asset — enruta la verificacion del Punto 2 — y su respuesta es un dato unico que el usuario conoce sin necesidad de opciones. Si el usuario responde con un municipio o una provincia, deduce la comunidad y **confirmala en la misma frase de la siguiente pregunta**, sin gastar un turno propio. Si responde que cada uno reside en una comunidad distinta, aplica la escalacion correspondiente.)*

* Para V3 (solo si V1 = 3):
  "Respecto de los hijos:
  1. Tienen hijos en comun
  2. No tienen hijos en comun"

* Para V4 (solo si V1 = 2 o 3):
  "Respecto de lo economico:
  1. Han adquirido algun bien conjuntamente, o uno ha aportado mas que el otro, o existe desequilibrio economico entre ustedes
  2. Cada uno conserva lo suyo y no hay bienes comunes ni desequilibrio"

**PRINCIPIO: Preguntas simples, no mega-preguntas.** Cada pregunta resuelve un unico punto de decision. No agrupes V3 y V4 en una sola pregunta, ni preguntes por los datos de las partes en esta fase.

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = 1 → **HOJA INSCRIPCION**: `assets/checklist-inscripcion-registro.md`. V3 y V4 no se preguntan como vectores; la existencia de hijos comunes se recaba en la seccion de pension de viudedad porque altera sus requisitos.
- Si V1 = 2 → **HOJA CONVIVENCIA**: `assets/pacto-convivencia.md`. V4 determina si se activan los bloques de bienes comunes, aportaciones desiguales y compensacion pactada.
- Si V1 = 3 → **HOJA RUPTURA**: `assets/pacto-ruptura-pareja-hecho.md`. V3 activa el bloque de remision sobre hijos comunes y dispara la derivacion; V4 determina los bloques de liquidacion y compensacion.
- Si V1 = 3 y V3 = 1 → ademas de la HOJA RUPTURA, **DERIVAR** expresamente para todo lo relativo a los hijos: custodia, regimen de estancias y visitas, y alimentos se regulan en `derecho-civil-medidas-hijos-no-matrimoniales`, exigen la intervencion del Ministerio Fiscal y no producen efecto sin aprobacion judicial. **Esta skill no los regula ni los incluye en el pacto**: activa el bloque de remision del asset y ofrece continuar con esa skill al cerrar el documento.
- Si lo que se pretende es un matrimonio, una separacion o un divorcio, o la liquidacion de un regimen economico matrimonial → **DETENER**: fuera de alcance. Derivar a `derecho-civil-divorcio` o a `derecho-civil-liquidacion-gananciales` segun corresponda.
- Si lo que se pretende es tramitar la inscripcion ante el registro, o presentar la solicitud en nombre del cliente → **DETENER** esa pretension concreta: la skill prepara la documentacion y el checklist, pero la solicitud la presenta la propia pareja. Continuar con la HOJA INSCRIPCION advirtiendolo.
- Si aparecen indicios de violencia entre los convivientes → **DETENER de inmediato**, en el mismo turno, sin crear ni continuar ningun documento. Advertir y escalar a asistencia juridica especializada.

### Validacion de presupuestos (interno, antes del Punto 3)

- **TODAS LAS HOJAS:** ninguno de los convivientes puede estar unido por vinculo matrimonial con otra persona ni tener otra pareja de hecho constituida. Si consta que si, advertir de que la constitucion de la pareja no es posible y de que un pacto entre ellos puede afectar a derechos de terceros; detener la rama de inscripcion y escalar.
- **TODAS LAS HOJAS:** si los convivientes residen en comunidades autonomas distintas, tienen vecindad civil distinta, o concurre elemento internacional (residencia fuera de Espana, pareja constituida en el extranjero) → advertir de que la determinacion de la ley aplicable y del registro competente excede de lo que puede resolverse aqui, y escalar. En la rama de inscripcion, no continuar sin esa aclaracion.
- **HOJA INSCRIPCION:** si de la verificacion del Punto 2 resulta un requisito temporal (tiempo minimo de convivencia previa o de empadronamiento conjunto) que la pareja aun no cumple, **no dar por presentable la solicitud**: hacerlo constar en el checklist, indicar desde cuando podra presentarse y advertir de que la presentacion anticipada conduce a la denegacion o al archivo.
- **HOJA RUPTURA:** si existe un pacto de convivencia previo, pedirlo y leerlo con `Read` antes de redactar la liquidacion: sus previsiones para el cese son ley entre las partes y el pacto de ruptura las desarrolla o las sustituye expresamente, nunca las contradice en silencio.
- **HOJA RUPTURA:** si el cliente pide que el pacto incluya medidas sobre los hijos, rechazarlo y explicar por que (cauce propio, Ministerio Fiscal, aprobacion judicial). Recoger la remision, no la medida.
- **HOJA CONVIVENCIA y HOJA RUPTURA:** si el cliente pide una clausula que pretenda crear entre ellos una sociedad de gananciales, unas capitulaciones matrimoniales o un convenio regulador, rechazarla: son instituciones privativas del matrimonio. Explicar la alternativa valida (comunidad de bienes pactada sobre bienes concretos, o el propio pacto) y ofrecerla.

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento. Tiene dos mitades, y **ninguna de las dos es omisible**.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del Codigo Civil, de la LGSS y del texto refundido del baremo de accidentes de circulacion.

**2.2 — Verificar las fuentes estatales.** La API de legislacion consolidada del BOE devuelve el bloque de un articulo concreto (requiere cabecera `Accept: application/xml`):
```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-1889-4763/texto/bloque/art{numero_articulo}
```
Consultar del Codigo Civil (BOE-A-1889-4763) los bloques `art1255`, `art1258`, `art1261`, `art1274`, `art1275`, `art392` a `art400`, `art404`, `art406` y `art1902`, y — solo para citarlos correctamente como normas del matrimonio que NO se aplican a la pareja de hecho — `art1323` y `art1438`. Consultar ademas, si la rama es de inscripcion o si el cliente pregunta por viudedad, el bloque `a221` de la LGSS (BOE-A-2015-11724), y los bloques `a36` y `a62` del texto refundido del baremo (BOE-A-2004-18911). **Aviso de formato:** el Codigo Civil usa `artNNN` y las otras dos normas usan `aNNN`; un 404 con una convencion no significa que la norma no exista, prueba la otra antes de declarar la fuente inaccesible.

**2.3 — VERIFICACION DE LA NORMATIVA AUTONOMICA (bloqueante, en CADA lanzamiento).** Con la comunidad autonoma ya resuelta (V2), ejecuta el protocolo de `references/verificacion-normativa-autonomica.md`:

```
web_search("ley parejas de hecho [comunidad autonoma] texto consolidado requisitos inscripcion registro")
web_search("registro parejas de hecho [comunidad autonoma] sede electronica documentacion tasa solicitud")
web_search("[comunidad autonoma] ley parejas de hecho articulos anulados Tribunal Constitucional")
```

Extrae unicamente lo que la fuente oficial diga: denominacion exacta de la ley y enlace, caracter constitutivo o declarativo de la inscripcion, requisitos de constitucion, preceptos anulados, denominacion y enlace del registro, documentacion, forma de solicitud, tasa y plazos. Anota la fecha de la verificacion como `fecha_verificacion_normativa_autonomica`.

**Esta reference NO almacena los requisitos de las diecisiete comunidades y no debes anadirlos.** Tampoco debes completarlos con lo que creas saber: si la busqueda no lo devuelve, no lo afirmas.

**2.4 — Auto-actualizar los archivos del plugin (obligatorio si hay cambios en las fuentes ESTATALES).** Si la version oficial de una norma estatal es posterior a la registrada o su texto ha cambiado, usa `Write`/`Edit` para actualizar `references/regimen-pareja-hecho-derecho-comun.md` y la tabla "Version registrada" y las fechas de `references/fuentes-plantillas-validadas.md`, e informa brevemente al usuario de la norma y la fecha detectadas. **Lo autonomico no se vuelca a las references**: vive en el documento generado, con su fecha de verificacion. No redactar hasta haber completado esta actualizacion.

**2.5 — Fallback si una fuente estatal no es accesible.** Intentar `web_search("Codigo Civil articulos 392 400 404 comunidad de bienes texto consolidado BOE")`. Si tampoco: usar las references locales y notificar: "No se pudo verificar la version vigente del Codigo Civil en el BOE. El documento se genera con la version de referencia. Verifiquela manualmente antes de la firma."

**2.6 — Fallback si la verificacion AUTONOMICA falla.** No se sustituye por conocimiento propio bajo ninguna circunstancia. Informar con este contenido: "No he podido verificar en fuente oficial la normativa de parejas de hecho de {{comunidad_autonoma}} ni los requisitos de su registro. No voy a afirmarle unos requisitos que no he comprobado. Continuo con el documento dejando ese punto expresamente pendiente, y debera confirmarlo en la sede del registro antes de presentar la solicitud." Dejar los placeholders autonomicos sin resolver y activar el bloque de aviso de verificacion pendiente del asset. En la HOJA CONVIVENCIA y en la HOJA RUPTURA se continua con normalidad, porque su base es el Codigo Civil; en la HOJA INSCRIPCION se advierte con especial claridad, porque el objeto mismo del documento es la parte autonomica.

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la normativa aplicable, ya verificada.** Empieza siempre por la advertencia de ausencia de ley estatal, sigue con la ley autonomica concreta verificada en este lanzamiento y su enlace, y cierra con la base de derecho comun del documento. Textos fijos por hoja:
   - INSCRIPCION: "No existe una ley estatal de parejas de hecho ni un registro estatal: la materia la regula cada comunidad autonoma. A su caso le resulta de aplicacion {{denominacion_ley_autonomica}}, que he verificado hoy en su fuente oficial: {{enlace_ley_autonomica}}. El registro competente es el {{denominacion_registro}}: {{enlace_registro}}."
   - CONVIVENCIA: "No existe una ley estatal de parejas de hecho, y la convivencia no crea entre ustedes ningun regimen economico. El pacto que vamos a preparar se otorga al amparo del articulo 1255 del Codigo Civil, y a los bienes que hayan adquirido conjuntamente les resultan de aplicacion los articulos 392 y siguientes del mismo cuerpo legal, sobre la comunidad de bienes. Puede consultar el texto oficial en https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763. En cuanto a su comunidad autonoma, he verificado hoy {{denominacion_ley_autonomica}}: {{enlace_ley_autonomica}}."
   - RUPTURA: "Al no haber existido matrimonio entre ustedes, no hay regimen economico matrimonial que liquidar ni cabe un convenio regulador. Lo que vamos a preparar es un pacto otorgado al amparo del articulo 1255 del Codigo Civil, que liquida la comunidad de bienes sobre lo adquirido conjuntamente conforme a los articulos 392 y siguientes. Puede consultar el texto oficial en https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763. En cuanto a su comunidad autonoma, he verificado hoy {{denominacion_ley_autonomica}}: {{enlace_ley_autonomica}}."
   - Si la verificacion autonomica fallo, sustituye la parte autonomica por el texto del Punto 2.6. **Nunca inventes una denominacion de ley ni un enlace.**
   - **Correccion inmediata del malentendido, si el cliente ya lo ha planteado.** Si en sus mensajes ha preguntado o dado por supuesto que inscribirse equipara al matrimonio, que crea gananciales, que da derecho a heredar o que garantiza una compensacion, **respondele aqui, en este mismo mensaje**, sin esperar a la seccion de la edicion incremental que trate esa materia. Diez turnos despues es tarde: el cliente esta tomando su decision ahora. Di con todas las letras que no, y por que: la inscripcion no crea ningun regimen economico, lo adquirido en comun se rige por los articulos 392 y siguientes del Codigo Civil segun la titularidad, y **el conviviente no hereda sin testamento** salvo lo que prevea la normativa civil aplicable que hayas verificado. Si ha preguntado por heredar, anade que la unica via es otorgar testamento ante notario, con el limite de las legitimas, y ofrece continuar despues con `derecho-civil-testamento-planificacion`. Esta correccion no sustituye a la seccion correspondiente del Punto 5: la anticipa.
   - Si V1 = 3 y V3 = 1 (hay hijos comunes), anade en el mismo mensaje: "Le adelanto que todo lo relativo a sus hijos — guarda y custodia, regimen de estancias y pension de alimentos — no puede regularse en este pacto: tiene un cauce propio, exige la intervencion del Ministerio Fiscal y no produce efecto sin aprobacion judicial. Lo trataremos en un documento aparte cuando cerremos este."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (adviertele si el documento adjuntado los incumple, y en particular si contiene clausulas que presupongan un regimen economico inexistente o que regulen medidas sobre los hijos).

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento:

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa y verificacion del Punto 2: incluidas `fecha_verificacion_normativa`, `fecha_verificacion_normativa_autonomica`, `comunidad_autonoma`, `denominacion_ley_autonomica`, `enlace_ley_autonomica`, `denominacion_registro` y `enlace_registro`). Los faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{fecha_inicio_convivencia}}`, `{{relacion_bienes_comunes}}`); nunca sustituyas un placeholder con nombre propio por un marcador generico, y nunca repitas el mismo marcador generico dos veces en el mismo documento (`Edit` necesita un `oldString` unico).
3. Utiliza `Write` para guardar el archivo en disco, con nombre en `snake_case.md` (ej. `pacto_convivencia_conviviente_a_conviviente_b.md`, `pacto_ruptura_conviviente_a_conviviente_b.md`, `checklist_inscripcion_pareja_hecho.md`).
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. En esa MISMA respuesta, sin turno intermedio y **sin preguntar si desea empezar**, emite el anuncio fijo de la primera seccion y formula ya su primera pregunta, para que el flujo no se detenga (regla del `CLAUDE.md` raiz, seccion 6.1, punto 5, y coherencia con el Punto 0: la skill esta en ejecucion desde que se carga). Un turno que solo diga "he creado el documento, ¿empezamos?" esta PROHIBIDO.

Los bloques condicionales del asset que dependan de decisiones aun no tomadas se OMITEN en este `Write` y se insertan durante el Punto 5, releyendo el asset y copiando el bloque **sin el envoltorio de comentario**. El documento escrito en disco no contiene ningun `<!-- ... -->`.

**Numeracion dinamica.** Los assets numeran sus clausulas con placeholders (`{{numero_pacto_objeto}}`, `{{numero_apartado_requisitos}}`...) precisamente porque hay bloques condicionales. Al insertar o descartar un bloque, renumera todas las clausulas de forma correlativa desde la primera, y resuelve tambien el ordinal del expositivo variable (`{{ordinal_expositivo_finalidad}}`). No dejes saltos ni numeros repetidos: es el defecto que mas delata un documento generado.

**Prohibidas las remisiones numericas entre clausulas.** Nunca escribas "conforme a la clausula octava" ni "segun lo previsto en el pacto sexto": con numeracion dinamica, insertar o descartar un bloque condicional convierte esa remision en un error silencioso que apunta a la clausula equivocada. Remite siempre por el nombre de la materia ("la cuenta comun regulada en este pacto", "el pacto de indivision"), que sobrevive a cualquier renumeracion.

**Filas de tabla con placeholder no resuelto.** La regla distingue tres situaciones, y confundirlas destruye informacion util:

- **Fila que ya sabes que nunca se resolvera → eliminar entera.** Es el caso de la fila de requisito adicional (`{{requisito_adicional}}`), prevista para el supuesto de que la verificacion devuelva un requisito propio de esa comunidad: si no lo devuelve, **elimina la fila entera**, no la dejes con el placeholder a la vista. Dejarla equivaldria a insinuar un requisito que no existe.
- **Fila cuyo valor esta pendiente de una pregunta que aun vas a hacer → conservar con su placeholder.** Las celdas `{{situacion_*}}` de la tabla de requisitos estan pendientes por definicion en el momento del `Write`, porque se recaban en el Punto 5. **Prohibido borrar esas filas en el `Write`**: se rellenan por `Edit` a medida que el cliente responde. La tabla solo queda libre de placeholders al cerrar la seccion, no antes.
- **Fila cuyo concepto existe pero cuyo valor no ha podido verificarse → conservar, con el hueco declarado.** Es el caso de la tasa, el plazo de resolucion o el efecto del silencio cuando la fuente oficial no los publica. Borrar la fila oculta la laguna en el unico documento donde el cliente iba a buscarla. Escribe en su lugar: "No consta en la fuente oficial consultada el {{fecha_verificacion_normativa_autonomica}}; confirmelo en la sede del registro antes de presentar la solicitud." Un hueco declarado es informacion; una fila borrada es una omision silenciosa.

## 5. EDICION INCREMENTAL DE CLAUSULAS

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas marcadas `[negociacion]` se explican y se confirman una a una. **La vista previa y la confirmacion agrupada de una parte se emiten en el turno SIGUIENTE a la respuesta del ultimo sub-apartado, nunca en el mismo turno en que aun se esta preguntando ese ultimo dato.**

**Regla propia de esta materia para las clausulas `[negociacion]`:** antes de pedir la decision, explica siempre **cual es el regimen por defecto si no se pacta nada** y que consecuencia tiene. En pareja de hecho el regimen por defecto es casi siempre "nada", y el cliente no lo sabe: si no se le explica, decide a ciegas. Esta explicacion es breve — dos o tres frases — y va en el mismo turno que la pregunta.

### Secciones — HOJA CONVIVENCIA

1. **Datos de cada conviviente** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de ambos convivientes." Sub-apartados, uno por turno, primero los del conviviente A y despues los del B: a) nombre completo; b) tipo y numero de documento de identidad; c) domicilio. Al recibir la respuesta al ultimo dato de cada conviviente, vista previa unica de esa parte y una sola confirmacion antes del `Edit`.
2. **La convivencia y su situacion registral** *(dato objetivo)*. Anuncio fijo: "Concretamos ahora los datos de su convivencia y su situacion registral." Sub-apartados, uno por turno: a) fecha de inicio de la convivencia; b) domicilio comun; c) si la pareja esta inscrita, tiene previsto inscribirse o no piensa hacerlo — y, si esta inscrita, fecha de inscripcion. Activa segun la respuesta el expositivo TERCERO que corresponda, en su unica variante.
3. **Regimen de los bienes de cada uno** *(negociacion)*. Anuncio fijo: "Abordamos ahora el regimen de sus bienes." Explica antes de preguntar: la convivencia no crea ningun regimen economico, cada uno conserva lo suyo y lo que gane durante la convivencia, y la ley no impone participacion alguna en lo del otro; eso seguira siendo asi salvo que lo pacten de otro modo. Pregunta despues si desean ademas inventariar en el pacto los bienes privativos de cada uno para facilitar la prueba de la titularidad, y activa o descarta ese bloque.
4. **Bienes adquiridos en comun y aportaciones desiguales** *(negociacion — la seccion mas importante del documento)*. Anuncio fijo: "Pasamos a los bienes que hayan adquirido conjuntamente." Explica antes: lo adquirido en comun se rige por la comunidad de bienes de los articulos 392 y siguientes del Codigo Civil, **las cuotas se presumen iguales salvo prueba en contrario** (articulo 393) y quien aporto mas dinero del que refleja la titularidad tiene la carga de probarlo. Sub-apartados, uno por turno: a) relacion de bienes adquiridos en comun, con su titularidad formal; b) si las aportaciones economicas reales coincidieron con esa titularidad y, si no, cuanto aporto cada uno. Si hubo desigualdad, pregunta despues cual de los tres efectos quieren darle, explicando los tres: que genere un credito exigible en la liquidacion, que se ajuste la cuota de titularidad a la aportacion real, o que se considere una liberalidad sin credito alguno. Advierte de que la tercera opcion es irreversible en la practica y de que la segunda exige otorgar despues la escritura que rectifique la titularidad. Confirmacion propia de cada decision.
5. **Vivienda que constituye el domicilio comun** *(negociacion)*. Anuncio fijo: "Determinamos ahora la situacion de la vivienda en la que conviven." Sub-apartados: a) situacion juridica (propiedad de uno, propiedad comun o arrendamiento), activando la variante correspondiente; b) si existe prestamo hipotecario y como se reparten las cuotas. Explica siempre que el reparto pactado **no vincula a la entidad prestamista**, frente a la cual ambos siguen respondiendo. Si la vivienda es propiedad de uno solo, explica que el otro la ocupa por tolerancia y sin derecho arrendaticio, y pregunta que plazo de desalojo quieren fijar para el caso de cese.
6. **Pacto de indivision** *(negociacion — condicional, solo si hay bienes comunes)*. Anuncio fijo: "Valoramos si les conviene pactar que algun bien comun no pueda dividirse durante un tiempo." Explica el articulo 400 del Codigo Civil: por defecto cualquiera de los dos puede pedir la division en cualquier momento, y si el bien es indivisible — una vivienda lo es — el desenlace legal es la venta y el reparto del precio (articulo 404); cabe pactar la indivision por un plazo no superior a diez anos. Pregunta si desean pactarla, sobre que bien y por cuanto tiempo.
7. **Contribucion a los gastos y cuenta comun** *(negociacion)*. Anuncio fijo: "Pasamos a la contribucion a los gastos de la convivencia." Explica: entre convivientes no existe deber legal de contribuir a las cargas, a diferencia del matrimonio; lo que se pacte aqui es lo unico que les obligara. Sub-apartados: a) criterio de contribucion (por mitades, proporcional a los ingresos u otro); b) si van a usar una cuenta comun y con que aportacion mensual.
8. **Deudas** *(negociacion)*. Anuncio fijo: "Concretamos ahora el regimen de las deudas." Explica: cada uno responde de lo que contrae a su nombre y el otro no queda obligado, salvo lo contraido conjuntamente o lo que derive de los bienes y gastos comunes. Pregunta si existe alguna deuda conjunta que quieran identificar.
9. **Dedicacion a la familia o al negocio del otro y compensacion pactada** *(negociacion — trato especialmente cuidadoso)*. Anuncio fijo: "Abordamos ahora la dedicacion de uno de ustedes a la familia o a la actividad del otro." Explica, sin prometer nada: si uno de los dos deja o reduce su actividad profesional para dedicarse a la casa, a los hijos o al negocio del otro, **la ley no le reconoce ninguna compensacion automatica** — las normas del matrimonio, incluida la compensacion por trabajo domestico, no se aplican por analogia a la pareja de hecho, y la unica via en defecto de pacto es el enriquecimiento injusto, que exige prueba y tiene resultado incierto; por eso, si esa dedicacion existe o va a existir, la forma segura de protegerla es pactar ahora la compensacion. Pregunta si concurre esa situacion y, si concurre: quien se dedica y a que, y que compensacion e importe acuerdan, con su forma de pago. Al redactar, **expresa siempre la causa** de la compensacion en la propia clausula (articulos 1274 y 1275 del Codigo Civil). Si el cliente pregunta si "le corresponde" una compensacion, responde que no le corresponde por ley y que lo que se esta creando es el derecho, no reconociendolo.
10. **Previsiones para el cese de la convivencia** *(negociacion)*. Anuncio fijo: "Preveamos ahora que ocurrira si la convivencia cesa." Explica que un pacto sin clausula de liquidacion deja a las partes igual que si no existiera. Pregunta el plazo que quieren fijar para liquidar los bienes comunes y las cuentas pendientes tras el cese.
11. **Hijos comunes** *(informativo con derivacion — condicional)*. Anuncio fijo: "Una precision sobre sus hijos comunes." Solo si existen. Explica que las medidas sobre los hijos no pueden regularse en este pacto, activa el bloque de remision del asset y ofrece tratarlas despues con `derecho-civil-medidas-hijos-no-matrimoniales`. No pidas ningun dato de los hijos aqui.
12. **Prevision sucesoria** *(negociacion)*. Anuncio fijo: "Le informo de un punto que suele pasarse por alto: la sucesion." Explica: salvo lo que prevea la normativa civil aplicable, **el conviviente no hereda sin testamento**, por larga que sea la convivencia y este o no inscrita la pareja; para protegerse mutuamente hay que otorgar testamento ante notario, con el limite de las legitimas si hay descendientes o ascendientes. Ofrece continuar despues con `derecho-civil-testamento-planificacion`, que prepara la minuta de testamento abierto para llevar a la notaria, advirtiendo de que esa skill cubre unicamente derecho civil comun y no vecindad civil foral. Pregunta si desean incluir en el pacto la clausula de prevision sucesoria, dejando constancia de esa voluntad.
13. **Duracion, controversias y eficacia** *(dato objetivo con explicacion)*. Anuncio fijo: "Cerramos con la vigencia del pacto y la forma de resolver discrepancias." Sub-apartados: a) fecha de entrada en vigor; b) medio de solucion de controversias al que se comprometen antes de acudir a los tribunales. Explica al cerrar que el documento privado carece de fuerza ejecutiva y que elevarlo a escritura publica le da fecha cierta y facilita su prueba.
14. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del pacto." Lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA RUPTURA

1. **Datos de cada conviviente** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de ambos convivientes." Igual estructura que en la HOJA CONVIVENCIA.
2. **La convivencia, su cese y la situacion registral** *(dato objetivo)*. Anuncio fijo: "Concretamos ahora las fechas de la convivencia y su situacion registral." Sub-apartados, uno por turno: a) fecha de inicio; b) fecha de cese; c) si la pareja estaba inscrita y, en tal caso, fecha de inscripcion y plazo en que se comprometen a solicitar la cancelacion; d) si existe un pacto de convivencia previo (si lo hay, pedirlo y leerlo con `Read` antes de continuar). Explica al tratar la cancelacion que, mientras no se practique, la inscripcion sigue produciendo sus efectos.
3. **Hijos comunes** *(informativo con derivacion — condicional, se trata pronto a proposito)*. Anuncio fijo: "Antes de entrar en lo economico, una precision sobre sus hijos." Solo si V3 = 1. Explica que la guarda y custodia, el regimen de estancias y la pension de alimentos no se regulan en este pacto porque tienen cauce propio, exigen la intervencion del Ministerio Fiscal y no producen efecto sin aprobacion judicial; que ninguna clausula economica de este documento puede condicionar ni compensar los derechos de los hijos; y que al cerrar este pacto se puede continuar con `derecho-civil-medidas-hijos-no-matrimoniales`. Activa el bloque de remision del asset. **No recabes ningun dato de los hijos**: nombres, edades o cualquier otro dato corresponden a la otra skill.
4. **Liquidacion de los bienes adquiridos en comun** *(negociacion)*. Anuncio fijo: "Pasamos a liquidar los bienes que adquirieron conjuntamente." Explica antes: no hay regimen economico matrimonial que liquidar, solo la comunidad de bienes sobre lo que figure a nombre de ambos; por defecto, si no hay acuerdo, cualquiera puede pedir la division y, si el bien es indivisible, se vende y se reparte el precio (articulos 400 y 404). Sub-apartados, uno por turno: a) relacion de bienes comunes y titularidad; b) para cada bien, si se adjudica a uno compensando al otro, si se vende, o si no hay acuerdo. Confirmacion por cada bien.
5. **Aportaciones desiguales** *(negociacion — condicional)*. Anuncio fijo: "Verificamos si las aportaciones a esos bienes fueron desiguales." Explica la presuncion de cuotas iguales del articulo 393 y la carga de la prueba. Pregunta cuanto aporto cada uno realmente y, si hubo desigualdad, si reconocen un credito, por que importe y con que forma de pago. Redacta el reconocimiento **expresando su causa**.
6. **Vivienda y prestamo hipotecario** *(negociacion)*. Anuncio fijo: "Determinamos ahora el destino de la vivienda que fue su domicilio." Sub-apartados: a) situacion juridica y titularidad; b) a quien se atribuye el uso y en que fecha desaloja el otro; c) reparto de los gastos a partir del cese; d) si hay prestamo hipotecario, capital pendiente, reparto de cuotas y hasta que hito. Explica siempre que el reparto **no vincula a la entidad prestamista** y que la liberacion de un prestatario exige su consentimiento expreso, que no esta obligada a dar. Si la vivienda es arrendada, trata la posicion arrendaticia y la fianza, advirtiendo de que puede requerir el consentimiento del arrendador.
7. **Cuentas y deudas** *(negociacion — condicional)*. Anuncio fijo: "Pasamos a las cuentas y deudas comunes." Sub-apartados: a) cuenta comun, plazo de cancelacion y reparto del saldo; b) deudas contraidas conjuntamente y como se atienden. Explica que el reparto interno no libera a ninguno frente al acreedor.
8. **Compensacion economica** *(negociacion — trato especialmente cuidadoso)*. Anuncio fijo: "Abordamos ahora si procede una compensacion economica entre ustedes." Explica, sin prometer nada: la ley **no reconoce automaticamente** una compensacion al conviviente en la ruptura; las normas del matrimonio no se aplican por analogia, y en defecto de pacto la unica via es el enriquecimiento injusto, que exige acreditar que la dedicacion de uno produjo un enriquecimiento correlativo del otro y cuyo resultado es incierto — el propio Tribunal Supremo la ha rechazado cuando falta esa prueba. Por eso, lo que da certeza es pactarla ahora. Pregunta si existio esa dedicacion, en que consistio y si acuerdan una compensacion, con importe y forma de pago. Redacta siempre **expresando la causa**. Si el cliente insiste en que "le corresponde por ley", corrigelo con claridad y sin dar falsas expectativas.
9. **Bienes muebles, ajuar y animales de compania** *(negociacion)*. Anuncio fijo: "Repartimos ahora los bienes muebles y el ajuar." Sub-apartados: a) reparto de muebles y ajuar y fecha de retirada; b) si hay animales de compania, su destino — explicando que el articulo 404 del Codigo Civil prohibe dividirlos mediante venta salvo acuerdo unanime y que, a falta de acuerdo, decide el juez atendiendo al bienestar del animal.
10. **Alcance de la liquidacion** *(negociacion)*. Anuncio fijo: "Precisamos el alcance de la liquidacion que estan acordando." Explica que la clausula de finiquito cierra cualquier reclamacion economica futura entre ellos derivada de la convivencia, incluida la fundada en enriquecimiento injusto, y que por eso solo debe firmarse cuando ambos consideren que la liquidacion es completa; explica tambien que **no alcanza a los derechos de los hijos**, que son irrenunciables. Pregunta si la aceptan en esos terminos.
11. **Controversias y eficacia** *(dato objetivo con explicacion)*. Anuncio fijo: "Cerramos con la forma de resolver discrepancias y la eficacia del pacto." Pregunta el medio de solucion de controversias. Explica que el documento privado carece de fuerza ejecutiva y que, si el pacto incluye pagos aplazados o adjudicacion de inmuebles, la elevacion a escritura publica es necesaria para el Registro de la Propiedad y muy recomendable en todo caso.
12. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del pacto."

### Secciones — HOJA INSCRIPCION

1. **Datos de cada conviviente** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de ambos convivientes." Igual estructura que en las otras hojas.
2. **Situacion de la pareja frente a los requisitos verificados** *(dato objetivo con validacion bloqueante)*. Anuncio fijo: "Contrastamos ahora su situacion con los requisitos que exige el registro." Recorre uno por uno **solo los requisitos que la verificacion del Punto 2.3 haya devuelto**, preguntando por cada uno la situacion de la pareja: edad, ausencia de vinculo, parentesco, tiempo de convivencia previa, empadronamiento conjunto, residencia. **Prohibido preguntar por un requisito que no conste en la verificacion, y prohibido dar por exigido uno que no se haya verificado.** Poda la tabla del asset conforme a la regla de tres situaciones del Punto 4: elimina entera la fila de requisito adicional si la verificacion no devolvio ninguno, y al cerrar la seccion ninguna fila puede quedar con un placeholder a la vista. **Un requisito que la verificacion devuelve como NO exigido no se borra: se conserva diciendo que no se exige.** Que la comunidad no imponga tiempo minimo de convivencia previa o empadronamiento conjunto es informacion que el cliente necesita — suele creer lo contrario — y borrar la fila se la oculta. Si algun requisito temporal no se cumple todavia, calcula desde cuando podra presentarse la solicitud, hazlo constar y advierte de que presentarla antes conduce a la denegacion o al archivo.
3. **Documentacion y tramite** *(dato objetivo)*. Anuncio fijo: "Relacionamos la documentacion y el tramite." Vuelca la documentacion, la forma de presentacion, el organo competente, la tasa y los plazos tal como los haya devuelto la verificacion. Pregunta el municipio de residencia y comprueba si existe ademas registro municipal; si lo hay, activa ese bloque y advierte de que los efectos de uno y otro pueden no coincidir.
4. **Que produce y que no produce la inscripcion** *(negociacion — es el nucleo pedagogico del documento)*. Anuncio fijo: "Le explico ahora que efectos tiene realmente la inscripcion." Explica los cuatro puntos, sin suavizarlos: no equipara la pareja al matrimonio, no crea ningun regimen economico, no genera derecho automatico a compensacion en caso de ruptura, y no convierte al conviviente en heredero. Explica tambien lo que si aporta: prueba de la existencia y de la fecha de la pareja, que es justo lo que despues exigen otras normas. Pregunta si desea que se incluyan en el documento los efectos que la ley autonomica verificada atribuye a la inscripcion.

**Trampa al volcar `{{efectos_inscripcion}}`: "sucesiones" casi nunca significa heredar.** Los portales autonomicos suelen listar la equiparacion al matrimonio "en materia de sucesiones", y se refieren al **Impuesto sobre Sucesiones y Donaciones**, que es un tributo cedido, no a los derechos sucesorios civiles. Copiar esa frase tal cual convierte el documento en autocontradictorio: afirmaria en este apartado lo que niega en el apartado de sucesion, y sobre el punto que mas le importa al cliente. Al volcar los efectos, **separa siempre lo fiscal de lo civil** y di expresamente si la comunidad tiene o no derecho civil propio que reconozca derechos sucesorios al conviviente. Si no lo has verificado, no lo afirmes en ninguno de los dos sentidos.
5. **Pension de viudedad** *(informativo con derivacion)*. Anuncio fijo: "Le informo de los requisitos propios de la pension de viudedad, que no son los del registro." Explica los cuatro requisitos del articulo 221 de la Ley General de la Seguridad Social, y en particular las dos consecuencias practicas: la antelacion minima de dos anos de la inscripcion respecto del fallecimiento, y que los cinco anos de convivencia se acreditan con el empadronamiento conjunto y no con la inscripcion. Pregunta si tienen hijos en comun, porque exime del requisito de los cinco anos, y activa el bloque correspondiente. Advierte de que la skill informa pero **no tramita ni valora** el derecho a la pension, y deriva al Instituto Nacional de la Seguridad Social o a un especialista.
6. **Sucesion y testamento** *(informativo)*. Anuncio fijo: "Un punto que suele pasarse por alto: la sucesion." Explica que el conviviente no hereda sin testamento salvo lo que prevea la normativa civil aplicable, y que la unica via de proteccion mutua es otorgar testamento ante notario, con el limite de las legitimas. Ofrece continuar despues con `derecho-civil-testamento-planificacion`, advirtiendo de que esa skill cubre unicamente derecho civil comun y no vecindad civil foral, y de que el testamento se otorga siempre ante notario.
7. **Recomendacion de pacto de convivencia** *(negociacion)*. Anuncio fijo: "Por ultimo, le recomiendo valorar un pacto de convivencia." Explica que la inscripcion prueba que la pareja existe pero no regula nada entre ellos, y que todo lo economico solo queda regulado si se pacta. Ofrece preparar el pacto de convivencia a continuacion; si acepta, al cerrar este documento reinicia el flujo por la HOJA CONVIVENCIA reutilizando los datos ya recabados, **sin volver a preguntarlos**.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: expositivos numerados y breves, una idea por clausula, importes en cifra y letra, causa expresada en toda prestacion economica, sin latinismos, y ninguna clausula sobre una materia que el cliente no haya decidido.

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5, muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una seccion existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

Si la hoja era la de RUPTURA y hay hijos comunes, o la de INSCRIPCION y el cliente acepto el pacto de convivencia, ofrece esa continuacion **despues** de que elija la opcion 5, nunca antes.

## Guardrails

1. **Nunca afirmar un requisito, un registro, un plazo o un efecto autonomico que no se haya verificado en este mismo lanzamiento** (Punto 2.3). No existe ley estatal de parejas de hecho: cualquier afirmacion autonomica no verificada es una invencion. Si la verificacion falla, decirlo con las palabras del Punto 2.6, dejar el punto pendiente en el documento y no afirmarlo.
2. **Nunca dar a entender que la pareja registrada equivale al matrimonio.** No hay equiparacion general: cada efecto tiene su propia norma y sus propios requisitos. Corregir activamente el malentendido cuando aparezca, aunque el cliente no pregunte.
3. **Nunca decir que la convivencia crea un regimen economico.** No nacen gananciales ni ningun otro regimen; cada uno conserva lo suyo y lo comun se rige por la comunidad de bienes segun la titularidad. Nadie queda sometido a un regimen por el mero hecho de convivir.
4. **Nunca prometer una compensacion economica como si fuera automatica.** Las normas del matrimonio, incluida la compensacion por trabajo domestico del articulo 1438 del Codigo Civil, **no se aplican por analogia** a la pareja de hecho. La via del enriquecimiento injusto existe solo en defecto de pacto, exige prueba de sus requisitos y tiene resultado incierto. Explicar que lo que da certeza es el pacto, y que el pacto crea el derecho, no lo reconoce.
5. **Nunca citar una sentencia que no se haya verificado en esta sesion.** Las unicas verificadas y registradas en `references/fuentes-plantillas-validadas.md` son la STC 81/2013, la STC 93/2013, la STS de 12 de septiembre de 2005 y la STS 17/2018, de 15 de enero. Cualquier otra se enuncia como criterio jurisprudencial sin atribucion, o no se enuncia.
6. **Nunca afirmar que el conviviente hereda.** Salvo lo que prevea la normativa civil aplicable y verificada, no hereda sin testamento. Advertirlo siempre en las tres hojas.
7. **Nunca resolver el derecho a la pension de viudedad.** Informar de los requisitos del articulo 221 de la Ley General de la Seguridad Social y derivar. No calcular, no valorar el caso, no anticipar el resultado.
8. **Nunca regular en estos pactos custodia, alimentos, estancias ni visitas de los hijos comunes.** Cauce propio, Ministerio Fiscal y aprobacion judicial. Derivar a `derecho-civil-medidas-hijos-no-matrimoniales`, activar el bloque de remision y no recabar datos de los hijos.
9. **Nunca redactar clausulas que presupongan instituciones matrimoniales** (gananciales, capitulaciones, convenio regulador, pension compensatoria del articulo 97 del Codigo Civil): son privativas del matrimonio y una clausula asi seria ineficaz. Rechazar, explicar y ofrecer la alternativa valida.
10. **Nunca afirmar efectos frente a terceros que el pacto no puede producir.** El reparto de cuotas hipotecarias o de deudas no vincula al acreedor; la subrogacion arrendaticia puede requerir el consentimiento del arrendador; los efectos fiscales dependen de normativa que la skill no verifica y se derivan a asesor fiscal.
11. **Violencia entre los convivientes: detener y escalar de inmediato**, en el mismo turno y sin crear ni continuar documento alguno.
12. **Nunca inventar datos, importes, fechas, denominaciones de registro ni enlaces.** Los campos no proporcionados quedan como `{{dato}}` con su nombre propio. Un enlace inventado a una sede electronica es especialmente grave: el cliente lo seguira.
13. **Documento escrito sin comentarios HTML y con numeracion correlativa.** Resolver todos los bloques condicionales y renumerar las clausulas tras insertar o descartar cualquiera de ellos.

## Como NO se usa esta skill

- **No regula la guarda y custodia, la pension de alimentos ni el regimen de estancias y visitas de los hijos comunes**: derivar a `derecho-civil-medidas-hijos-no-matrimoniales`. Esta skill se ocupa exclusivamente de lo patrimonial entre los convivientes.
- **No tramita la inscripcion ante el registro autonomico ni municipal**: genera la documentacion y el checklist del tramite, pero la solicitud la presenta la propia pareja.
- **No cubre el matrimonio, la separacion ni el divorcio**, ni la liquidacion de un regimen economico matrimonial: derivar a `derecho-civil-divorcio` o a `derecho-civil-liquidacion-gananciales`.
- **No cubre extranjeria ni reagrupacion familiar**, aunque la pareja registrada tenga efectos en esa normativa: es derecho administrativo, fuera del plugin.
- **No resuelve el derecho a la pension de viudedad ni a ninguna otra prestacion de la Seguridad Social**: informa de los requisitos y deriva.
- **No redacta testamentos ni planifica la sucesion**: advertir de la necesidad del testamento y derivar a `derecho-civil-testamento-planificacion`, que prepara la minuta para la notaria. `derecho-civil-herencia` tampoco sirve para esto: excluye expresamente la redaccion de testamentos.
- **No presta asesoramiento fiscal** sobre las adjudicaciones, donaciones o transmisiones entre convivientes.
- **No se usa para reclamar judicialmente una compensacion frente al otro conviviente**: si no hay acuerdo, el pacto no es la via. Escalar.

## Escalacion

| Situacion | Accion |
|---|---|
| Indicios de violencia entre los convivientes | Detener de inmediato, no crear ni continuar documento, y derivar a asistencia juridica especializada |
| Uno de los convivientes esta casado con un tercero o tiene otra pareja de hecho constituida | Detener la rama de inscripcion, advertir de la imposibilidad de constituir la pareja y del posible perjuicio a terceros, y escalar |
| Los convivientes residen en comunidades autonomas distintas, o tienen vecindad civil distinta | Advertir de que la ley aplicable y el registro competente no pueden determinarse aqui, y escalar |
| Elemento internacional: residencia fuera de Espana o pareja constituida en el extranjero | Escalar: excede el alcance de esta skill |
| La verificacion de la normativa autonomica falla y el objeto del encargo era precisamente la inscripcion | Entregar el checklist con los requisitos marcados como pendientes, advertirlo expresamente y remitir a la sede del registro |
| El cliente pretende que el pacto regule medidas sobre los hijos | Rechazar, explicar el cauce propio y derivar a `derecho-civil-medidas-hijos-no-matrimoniales` |
| El cliente pregunta si tiene derecho a una compensacion y no hay acuerdo con el otro conviviente | No prometer resultado; explicar que la via del enriquecimiento injusto exige prueba y es incierta, y escalar via `escalate_to_attorney` |
| Existe litigio ya iniciado entre los convivientes | Escalar: el pacto extrajudicial no es la via cuando el asunto ya esta judicializado |
| Consulta sobre efectos fiscales de las adjudicaciones o de la inscripcion | Derivar a asesor fiscal; no afirmar reducciones ni exenciones |
| Uno de los convivientes es menor de edad o tiene la capacidad modificada judicialmente | Detener y escalar: exige verificacion de capacidad y, en su caso, medidas de apoyo |
