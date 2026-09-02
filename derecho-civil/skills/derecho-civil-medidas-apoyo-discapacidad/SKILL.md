---
name: derecho-civil-medidas-apoyo-discapacidad
description: >
  Genera el documento adecuado para proveer de apoyo a una persona mayor de edad con discapacidad
  conforme al sistema de la Ley 8/2021, verificado en el BOE: minuta de escritura de medidas de apoyo
  voluntarias y poder preventivo, incluida la autocuratela (Arts. 255 a 262 y 271 a 274 CC); solicitud
  de autorizacion judicial al guardador de hecho para un acto concreto que exige actuacion
  representativa (Art. 264 CC, por el expediente de jurisdiccion voluntaria de los Arts. 61 a 63 LJV);
  y solicitud de provision judicial de medidas de apoyo con constitucion de curatela (Art. 269 CC, por
  el expediente del Art. 42 bis a) LJV, o por el proceso contencioso de los Arts. 756 a 761 LEC si el
  expediente termino por oposicion). La curatela es SUBSIDIARIA: la skill aplica el filtro del Art. 269
  antes de enrutar a ella. NO usar para menores de edad, para el internamiento no voluntario (Art. 763
  LEC), para la incapacitacion ni la modificacion de la capacidad (instituciones suprimidas en 2021),
  ni para constituir un patrimonio protegido de la Ley 41/2003.
when_to_use: |
  - Una persona quiere dejar previsto ahora quien le apoyara si en el futuro lo necesita: poder
    preventivo, autocuratela u otras medidas voluntarias.
  - Alguien viene ocupandose de hecho de un familiar y necesita realizar un acto concreto en su nombre
    (vender un inmueble, aceptar o repudiar una herencia, disponer de un deposito, interponer una
    demanda) que exige actuacion representativa.
  - Una persona precisa apoyo de modo continuado, no hay nadie ocupandose de ella ni medida voluntaria
    alguna, y procede pedir judicialmente la constitucion de una curatela.
  - El usuario pide "incapacitar" o "modificar la capacidad" de un familiar: la skill corrige la
    terminologia, aplica el filtro de subsidiariedad y encamina el caso a la medida que corresponda.
inputs:
  - finalidad: prevision voluntaria / autorizacion al guardador de hecho / curatela
  - existe_guarda_hecho: si / no, y si constituye apoyo suficiente
  - existe_medida_voluntaria: si / no, y su alcance
  - tipo_curatela: asistencial / representativa para actos concretos
  - expresion_voluntad: la persona puede expresar su voluntad, deseos y preferencias / no puede pese a un esfuerzo considerable
  - via_procesal: expediente de jurisdiccion voluntaria / proceso contencioso tras oposicion
  - datos_persona_apoyada: nombre, DNI/NIE, fecha de nacimiento, residencia, situacion personal y patrimonial
  - datos_promotor_o_guardador: nombre, DNI/NIE, domicilio, relacion con la persona, desde cuando presta el apoyo
  - necesidades_apoyo: ambitos concretos y observables en que se precisa apoyo, y si es continuado u ocasional
  - acto_concreto: descripcion, bien o derecho identificado, motivo, necesidad, destino de la suma y valor economico
  - curador_propuesto: persona propuesta, razones de idoneidad, sustitutos, causas de exclusion
  - dictamen_pericial: autor, fecha y contenido del dictamen social y sanitario
  - interesados: conyuge o pareja, descendientes, ascendientes y hermanos que deben ser citados
outputs:
  - minuta_poder_preventivo: minuta de escritura de medidas de apoyo voluntarias y poder preventivo en markdown, DRAFT
  - solicitud_autorizacion_guarda_hecho: solicitud de autorizacion judicial al guardador de hecho en markdown, DRAFT
  - demanda_curatela: solicitud de provision judicial de medidas de apoyo con constitucion de curatela en markdown, DRAFT
references:
  - references/sistema-apoyos-ley-8-2021.md
  - references/curatela-designacion-actos-y-control.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/minuta-poder-preventivo.md
  - assets/solicitud-autorizacion-guarda-hecho.md
  - assets/demanda-curatela.md
---

# Provision de Medidas de Apoyo a Personas con Discapacidad

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija del Punto 1 y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificacion normativa interna, ejecutala en silencio y continua hasta la primera pregunta o hasta la Confirmacion visible del Punto 3, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

Esta linea es, junto con la introduccion fija del Punto 1 y los anuncios de seccion del Punto 5, la UNICA excepcion a la prohibicion de mencionar la mecanica interna. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, el filtro de subsidiariedad, la validacion de presupuestos, la verificacion normativa y la creacion base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol.
- Resumenes de validacion con checks (ej. "Subsidiariedad: ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

**REGLA DE TONO PROPIA DE ESTA SKILL (aplica a todo texto visible):**
Aqui se habla de una persona, no de un expediente. Usa su nombre. No la reduzcas a una etiqueta ("el caso", "el sujeto", "la persona afectada" repetido). Y **nunca** emplees el vocabulario del regimen anterior — "el incapaz", "el incapacitado", "incapacitar", "modificacion de la capacidad", "someter a tutela", "el discapacitado" —, ni siquiera reproduciendo las palabras del usuario. La terminologia correcta es **persona con discapacidad**, **medidas de apoyo**, **provision de apoyos**, **curatela** y **curador**. Ver la tabla completa en `references/estilo-redaccion-escritos.md`, regla cero.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin:

"Vamos a determinar que medida de apoyo se ajusta a la situacion que me plantea y a preparar el documento que corresponda. Para hacerlo correctamente, es necesario precisar antes algunos datos."

**Correccion terminologica (solo si procede, una unica vez, en el mismo primer turno y antes de la introduccion):** si el usuario ha empleado el vocabulario del regimen anterior ("incapacitar", "incapacitacion", "modificar la capacidad", "tutela" de un adulto, "el incapaz"), emite antes de la introduccion esta aclaracion fija, sin reproche y sin repetirla despues:

"Antes de continuar, una precision necesaria. Desde la Ley 8/2021 no existen en Espana la incapacitacion ni la modificacion judicial de la capacidad, ni la tutela de personas adultas. Lo que el ordenamiento prevee hoy son medidas de apoyo para que la persona ejerza su propia capacidad juridica. No es un cambio de nombre: cambia lo que puede pedirse y como se pide."

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:

- **V1 (Finalidad):** que la propia persona deje previsto ahora quien le apoyara en el futuro / que quien ya se ocupa de hecho de ella obtenga cobertura para un acto concreto que exige actuar en su nombre / que se constituya judicialmente una curatela.
- **V2 (Filtro de subsidiariedad — solo si V1 = curatela; BLOQUEANTE):** se resuelve con dos preguntas independientes.
  - **V2.a (Guarda de hecho existente):** hay alguien ocupandose de hecho de la persona y funciona / no hay nadie ocupandose de forma estable, o quien lo hacia ha dejado de poder hacerlo.
  - **V2.b (Medida voluntaria previa):** la persona otorgo en su dia un poder notarial u otras medidas de apoyo voluntarias / no otorgo ninguna, o se ignora.
- **V3 (Tipo de curatela — solo si V1 = curatela y el filtro V2 no la ha descartado):** asistencial, el curador acompana y asiste / representativa para actos concretos, el curador actua en nombre de la persona en lo que resulte imprescindible.
- **V4 (Expresion de la voluntad — en las hojas GUARDA y CURATELA):** la persona puede expresar su voluntad, deseos y preferencias / no puede hacerlo pese a un esfuerzo considerable.

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto (omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama):

* Para V1:
  "Lo que necesita preparar es:
  1. Que la propia persona deje previsto ahora quien le apoyara si en el futuro lo necesita
  2. Que quien ya se ocupa de ella pueda realizar un acto concreto en su nombre
  3. Que un juez establezca un apoyo estable para ella"

* Para V2.a (solo si V1 = 3):
  "Sobre quien se ocupa hoy de ella:
  1. Hay un familiar o allegado que se ocupa de ella con normalidad
  2. No hay nadie ocupandose de forma estable, o quien lo hacia ya no puede"

* Para V2.b (solo si V1 = 3):
  "Sobre documentos otorgados por ella con anterioridad:
  1. Otorgo ante notario un poder o unas medidas de apoyo
  2. No otorgo ninguno, o lo desconozco"

* Para V3 (solo si V1 = 3 y el filtro no ha descartado la curatela):
  "El apoyo que necesita en esos ambitos es:
  1. Acompanamiento y asistencia, decidiendo ella con ayuda
  2. Que otra persona actue en su nombre en los asuntos en que no pueda hacerlo por si misma"

* Para V4 (en las hojas GUARDA y CURATELA):
  "Sobre su capacidad de expresarse hoy:
  1. Puede expresar lo que quiere y lo que prefiere, aunque necesite ayuda para comprender o decidir
  2. No es posible saber lo que quiere, ni siquiera dedicandole tiempo y buscando el modo"

**PRINCIPIO: Preguntas simples, no mega-preguntas.** Cada pregunta resuelve un unico punto de decision. No comprimas V2.a y V2.b en una sola pregunta, ni V3 con V4.

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = 1 → **HOJA VOLUNTARIA**: `assets/minuta-poder-preventivo.md`.
- Si V1 = 2 → **HOJA GUARDA**: `assets/solicitud-autorizacion-guarda-hecho.md`, previa la validacion de "acto concreto" descrita mas abajo.
- Si V1 = 3 → **aplicar primero el FILTRO DE SUBSIDIARIEDAD** (seccion siguiente). Solo si lo supera:
  - V3 = 1 → **HOJA CURATELA**, `assets/demanda-curatela.md`, con los bloques de facultades representativas DESACTIVADOS.
  - V3 = 2 → **HOJA CURATELA**, el mismo asset, con los bloques de facultades representativas ACTIVADOS y justificados acto por acto.
- **Sub-pregunta de via procesal (solo en la HOJA CURATELA, antes del Punto 3).** El expediente de jurisdiccion voluntaria es la via ordinaria; el proceso contencioso solo procede si un expediente previo termino por oposicion o no pudo resolverse (Art. 756.1 LEC). Formula:
  "Sobre actuaciones judiciales anteriores por este mismo asunto:
  1. No se ha iniciado ninguna
  2. Se inicio un expediente que termino porque alguien se opuso, o que no pudo resolverse"
  Respuesta 1 → variante de jurisdiccion voluntaria del asset. Respuesta 2 → activar el bloque condicional de la variante contenciosa (Arts. 756 a 761 LEC) y ajustar los fundamentos de tramite y prueba (Art. 759 LEC en lugar del Art. 42 bis b) LJV).
- Si en cualquier momento consta que la persona es **menor de edad** → **DETENER**: fuera de alcance (patria potestad o tutela de menores). Advertir y escalar. No crear documento. Unica excepcion informativa: si es mayor de dieciseis anos y se preve que precisara apoyo al alcanzar la mayoria de edad, informar del Art. 254 CC y de que **el propio menor puede hacer sus propias previsiones**, y escalar.
- Si lo que se pretende es un **internamiento no voluntario** (Art. 763 LEC) → **DETENER SIEMPRE**: fuera de alcance, con independencia de lo urgente que parezca. Advertir y escalar de inmediato.
- Si lo que se pretende es una **incapacitacion** o una **modificacion de la capacidad** → no es un supuesto de "fuera de alcance" sino de institucion inexistente: aplicar la correccion terminologica del Punto 1 y reconducir el caso por V1, sin detener el flujo.
- Si lo que se pretende es constituir o administrar un **patrimonio protegido** de la Ley 41/2003 → **DETENER**: fuera de alcance. Advertir y escalar.
- Si la persona tiene **vecindad civil foral** (Cataluna, Aragon, Navarra, Galicia, Baleares) → **DETENER**: esta skill se apoya en el Codigo Civil estatal y no ha verificado la normativa autonomica. Advertir y escalar.

### FILTRO DE SUBSIDIARIEDAD (interno, BLOQUEANTE, solo si V1 = 3)

Es el nucleo de esta skill. El Art. 269 del Codigo Civil solo permite constituir la curatela **cuando no exista otra medida de apoyo suficiente**, y el Art. 255 in fine anade que la autoridad judicial solo puede adoptar medidas supletorias "en defecto o por insuficiencia de las voluntarias, y a falta de guarda de hecho que suponga apoyo suficiente". Ver `references/sistema-apoyos-ley-8-2021.md`, apartado 6.

**Regla: si V2.a = 1 o V2.b = 1, NO enrutes a la HOJA CURATELA todavia.** En su lugar, emite en un unico mensaje, en el registro formal del plugin:

1. **La explicacion del regimen.** Que la ley considera la guarda de hecho una medida de apoyo con el mismo rango que las demas (Art. 250 CC), que quien viene ejerciendola adecuadamente continua en su funcion (Art. 263 CC), y que la curatela solo se constituye cuando no existe otra medida de apoyo suficiente (Art. 269 CC). Si V2.b = 1, anadir que el poder otorgado en su dia puede seguir siendo operativo y que conviene leerlo antes de descartarlo (Arts. 256 a 259 CC).
2. **La alternativa concreta.** Que si el problema es un acto puntual que exige actuar en nombre de la persona, la via es la autorizacion judicial del Art. 264 del Codigo Civil, mas breve, mas barata y sin necesidad de abogado ni procurador si el valor del acto no supera los 6.000 euros (Art. 62.3 LJV).
3. **La pregunta de salida**, con alternativas numeradas:
   "A la vista de lo anterior:
   1. Hay un acto concreto que necesita hacerse en su nombre y para el que basta esa autorizacion
   2. El apoyo actual no basta: hay ambitos en los que se necesita un apoyo estable"

- Respuesta 1 → **HOJA GUARDA**. Continua por esa rama.
- Respuesta 2 → el filtro queda superado por confirmacion expresa del cliente. **Antes de seguir, pide la razon concreta por la que el apoyo actual no basta** (pregunta en prosa) y registrala: es el contenido del hecho de subsidiariedad del escrito, y sin el la solicitud es rechazable. Despues continua con V3.

**Si V2.a = 2 y V2.b = 2**, el filtro queda superado sin necesidad de esta pregunta. Continua con V3.

**Aplica ademas, en ambos casos, el filtro de la necesidad ocasional:** si de lo relatado resulta que el apoyo se necesita solo de vez en cuando, aunque sea de forma recurrente, la medida proporcionada es el **defensor judicial** (Arts. 250 y 295.5.º CC), no la curatela. Adviertelo, explica la diferencia y ofrece escalacion: esta skill no genera la solicitud de defensor judicial.

### Validacion de presupuestos (interno, antes del Punto 3)

- **HOJA VOLUNTARIA (Arts. 255 y 260 CC):** las medidas voluntarias exigen que el otorgante **comprenda el alcance del acto en el momento de la firma**, y ese juicio corresponde al Notario. Si de lo relatado resulta que la persona ya no esta en condiciones de otorgar, **adviertelo con claridad y reconduce**: la via ya no es la voluntaria, sino la guarda de hecho o la curatela. No prepares una minuta que el notario no vaya a poder autorizar.
- **HOJA VOLUNTARIA (Art. 259 CC):** si el poder va a comprender todos los negocios del otorgante, adviertelo antes de redactarlo: el apoderado quedara sujeto a las reglas de la curatela en todo lo no previsto, incluidas las autorizaciones judiciales del Art. 287. Ofrece acotar las facultades.
- **HOJA GUARDA (Art. 264 CC) — validacion de "acto concreto", BLOQUEANTE:** confirma que existe un acto determinado que exige actuacion representativa. Si el cliente solo quiere "dejar constancia" de que se ocupa de la persona, **DETENTE y no crees documento**: explica que la guarda de hecho no se constituye, no se nombra y no se inscribe, que ya es la medida de apoyo aplicable, y que no hay nada que formalizar. Si ademas la persona conserva capacidad para otorgar, ofrece la HOJA VOLUNTARIA como via para dar cobertura estable al apoyo.
- **HOJA GUARDA (Art. 264, parrafo 3, CC) — actos que NO requieren autorizacion:** si el acto consiste en solicitar una prestacion economica a favor de la persona que no supone un cambio significativo en su forma de vida, o en un acto sobre bienes de escasa relevancia economica y sin especial significado personal o familiar, **informa de que no hace falta autorizacion judicial** y no crees el expediente. Solo continua si el cliente confirma que el acto excede de esos limites.
- **HOJA GUARDA (Art. 287 CC):** si el acto es uno de los enumerados en el Art. 287, la autorizacion es preceptiva **en todo caso**. Identifica el ordinal concreto y registralo: se cita en el escrito.
- **HOJA GUARDA (Art. 62.3 LJV):** determina el valor economico del acto. Si no supera los 6.000 euros, no son preceptivos abogado ni procurador; si lo supera, la solicitud inicial puede presentarse igualmente sin ellos, pero el Tribunal puede ordenar despues la actuacion por medio de abogado. Informa de ambas cosas; no afirmes que son preceptivos desde el inicio.
- **HOJA CURATELA (Art. 42 bis b).1 LJV) — dictamen pericial, BLOQUEANTE:** la solicitud debe acompanarse de **un dictamen pericial de profesionales especializados de los ambitos social y sanitario** que aconseje las medidas idoneas. Pregunta si se dispone de el. Si no se dispone, **no impidas redactar el borrador**, pero advierte expresamente de que el escrito no puede presentarse sin ese dictamen y deja su referencia como placeholder pendiente. Nunca des por cumplido este requisito con un informe medico generico que no aconseje medidas.
- **HOJA CURATELA (Art. 269, parrafos 2 y 4, CC) — individualizacion:** no se admite una peticion generica de curatela. Si el cliente no sabe concretar en que ambitos se necesita apoyo, **no redactes una formula amplia**: dialoga hasta obtener ambitos concretos y observables, orientandote por los del dictamen pericial.
- **HOJA CURATELA (Art. 269, parrafo final, CC):** esta prohibido pedir la privacion de derechos. Si el cliente pide que la persona "no pueda votar", "no pueda casarse", "no pueda disponer de nada", rechaza la instruccion, explica la prohibicion legal y reconduce hacia la determinacion de los actos en que se precisa asistencia.
- **HOJA CURATELA (Art. 275 y Art. 250 in fine CC) — idoneidad del curador:** verifica que la persona propuesta no incurre en causa de inhabilidad, no tiene conflicto de intereses con la persona apoyada y no le presta servicios asistenciales o residenciales en virtud de contrato. Si concurre alguna, adviertelo y pide otra propuesta.
- **TODAS LAS HOJAS — sospecha de abuso o de aprovechamiento patrimonial:** si de lo relatado resulta que el apoyo se busca para acceder al patrimonio de la persona, o hay indicios de presion, aislamiento o disposiciones patrimoniales recientes a favor de quien pide el apoyo, **DETENTE de inmediato**, no crees documento y escala. Ver la matriz de Escalacion.

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del Codigo Civil (arts. 249 a 298), de la Ley 15/2015 de Jurisdiccion Voluntaria, de la LEC (arts. 756 a 763) y del art. 84 de la LOPJ.

**2.2 — Consultar la fuente oficial vigente.** La API de legislacion consolidada del BOE devuelve el bloque de un articulo concreto (requiere cabecera `Accept: application/xml`). **La ultima `<version>` del bloque es la vigente.**

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{identificador}/texto/bloque/{bloque}
```

Consultar, segun la hoja:
- **Todas las hojas:** Codigo Civil (BOE-A-1889-4763), bloques `art249` y `art250`.
- **HOJA VOLUNTARIA:** ademas, `art251`, `art255`, `art256`, `art257`, `art258`, `art259`, `art260`, `art261` y `art271` a `art274`.
- **HOJA GUARDA:** ademas, `art263`, `art264`, `art265` y `art287` del Codigo Civil; y de la LJV (BOE-A-2015-7391), los bloques `a52`, `a61`, `a62` y `a63`.
- **HOJA CURATELA:** ademas, `art268`, `art269`, `art270`, `art275`, `art276`, `art277`, `art282`, `art284`, `art285`, `art287`, `art290`, `art292` y `art295` del Codigo Civil; de la LJV, los bloques `a4-2`, `a4-3` y `a4-4` (que son los arts. 42 bis a), b) y c)); y, si la via es contenciosa, de la LEC (BOE-A-2000-323), los bloques `a756`, `a757`, `a758`, `a759` y `a762`.

**Aviso sobre los identificadores de bloque:** las normas no usan la misma convencion. El Codigo Civil usa `artNNN`; la LEC y la LJV usan `aNNN`; la LOPJ usa el ordinal deletreado (`aochentaycuatro`); y los articulos "bis" de la LJV llevan un id sintetico (`a4-2` para el art. 42 bis a). **Si un identificador devuelve 404, consulta antes el indice de la norma (`.../texto/indice`) y localiza alli el id real del bloque; no des el articulo por inaccesible.**

**2.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar Write/Edit para:
- Actualizar `references/sistema-apoyos-ley-8-2021.md` y/o `references/curatela-designacion-actos-y-control.md` con la redaccion vigente.
- Actualizar los assets afectados si el cambio altera una cita, un plazo o un requisito reproducido en ellos.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**2.5 — Verificar el modelo normalizado del CGPJ.** Comprobar en https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/ si existe un modelo normalizado especifico de medidas de apoyo o de curatela. **A la fecha registrada no existe**: solo el modelo generico de solicitud de expediente de jurisdiccion voluntaria (art. 14.3 de la Ley 15/2015), cuyo esqueleto siguen las hojas GUARDA y CURATELA. Si apareciera uno especifico, actualizar los assets y la reference.

**2.6 — Fallback si la fuente no es accesible.** Si la lectura falla (error HTTP, timeout):
```
web_search("Codigo Civil articulos 249 250 264 269 medidas de apoyo Ley 8/2021 texto consolidado BOE")
web_search("Ley 15/2015 Jurisdiccion Voluntaria articulo 42 bis a provision medidas de apoyo texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del Codigo Civil en el BOE. El documento se genera con la version de referencia. Verificar manualmente antes de presentar."

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Textos fijos por hoja:
   - VOLUNTARIA: "A su caso corresponden unas medidas de apoyo de naturaleza voluntaria, que se otorgan en escritura publica conforme a los articulos 255 y siguientes del Codigo Civil, en la redaccion de la Ley 8/2021. El poder preventivo se regula en sus articulos 256 a 262 y la autocuratela en el 271. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
   - GUARDA: "A su caso corresponde una solicitud de autorizacion judicial al guardador de hecho, conforme al articulo 264 del Codigo Civil, que se tramita por el expediente de jurisdiccion voluntaria de los articulos 61 a 63 de la Ley 15/2015, de Jurisdiccion Voluntaria. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2015-7391"
   - CURATELA (via de jurisdiccion voluntaria): "A su caso corresponde una solicitud de provision judicial de medidas de apoyo, conforme al articulo 269 del Codigo Civil, que se tramita por el expediente de jurisdiccion voluntaria del articulo 42 bis a) de la Ley 15/2015, de Jurisdiccion Voluntaria. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2015-7391"
   - CURATELA (via contenciosa): "A su caso corresponde una demanda de adopcion de medidas judiciales de apoyo, conforme al articulo 269 del Codigo Civil y a los articulos 756 y siguientes de la Ley 1/2000, de Enjuiciamiento Civil, aplicables por haber terminado el expediente previo sin resolucion. Fuentes consultadas: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - En las hojas GUARDA y CURATELA, anadir: "No existe modelo normalizado del Consejo General del Poder Judicial especifico para este documento; se sigue la estructura de su modelo generico de solicitud de expediente de jurisdiccion voluntaria."
   - En la hoja CURATELA, anadir ademas: "Las medidas que se acuerden se revisaran en un plazo maximo de tres anos, y en todo caso ante cualquier cambio en su situacion (articulo 268 del Codigo Civil)."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio. Si el documento adjuntado emplea la terminologia derogada o pide una privacion de derechos, adviertelo antes de trabajar sobre el.

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento:

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa e investigacion: incluida `fecha_verificacion_normativa` del Punto 2). Los faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{nombre_curador_propuesto}}`, `{{valor_acto}}`); usa un marcador generico solo para un hueco suelto sin placeholder propio, y nunca repitas el mismo marcador generico dos veces en el mismo documento (`Edit` necesita un `oldString` unico).
3. Utiliza `Write` para guardar el archivo en disco (nombre en `snake_case.md`, ej. `minuta_poder_preventivo_persona_a.md`, `solicitud_autorizacion_guarda_hecho_persona_a.md`, `solicitud_medidas_apoyo_curatela_persona_a.md`).
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. En esa MISMA respuesta, sin turno intermedio y **sin preguntar si desea empezar**, emite el anuncio fijo de la primera seccion y formula ya su primera pregunta, para que el flujo no se detenga (regla del `CLAUDE.md` raiz, seccion 6.1, punto 5, y coherencia con el Punto 0: la skill esta en ejecucion desde que se carga).

Los bloques condicionales del asset que dependan de decisiones aun no tomadas se OMITEN en este `Write` y se insertan durante el Punto 5, releyendo el asset y copiando el bloque **sin el envoltorio de comentario**. Al omitirlos, **colapsa las lineas en blanco que dejan**: dos o mas lineas vacias seguidas se reducen a una, para que el documento no muestre huecos en el editor. Al insertarlos despues, respeta el **orden en que figuran en el asset**: un bloque condicional va siempre donde el asset lo situa, no al final de la seccion. **Numeracion dinamica:** los ordinales que dependen de bloques condicionales (`{{ordinal_hecho_voluntad}}`, `{{ordinal_clausula_autocuratela}}`, `{{ordinal_fundamento_designacion}}` y demas) se resuelven al final de cada seccion, cuando ya se sabe que bloques han quedado activos; nunca se dejan como placeholder en el documento cerrado.

## 5. EDICION INCREMENTAL DE SECCIONES

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma persona se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas marcadas como `[negociacion]` se explican y se confirman una a una. **La vista previa y la confirmacion agrupada se emiten en el turno SIGUIENTE a la respuesta del ultimo sub-apartado, nunca en el mismo turno en que aun se esta preguntando ese ultimo dato.**

**Regla propia de esta skill para las secciones `[negociacion]`:** aqui la decision no se negocia entre dos partes contrapuestas, sino que se toma **sobre la vida de una tercera persona**. Antes de pedir la decision, explica siempre: que dice la ley por defecto, que consecuencia practica tiene cada opcion, y — cuando proceda — que dice o que preferiria la propia persona con discapacidad. Si la decision del cliente contradice lo que la persona ha manifestado, hazlo notar antes de escribirla.

### Secciones — HOJA VOLUNTARIA

1. **Otorgante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por los datos de quien otorga las medidas de apoyo." Sub-apartados, uno por turno: a) nombre y apellidos; b) DNI o NIE; c) estado civil; d) domicilio, telefono y correo electronico; e) vecindad civil. En la vecindad civil, si la respuesta es una comunidad con derecho civil propio, aplica el guardrail de vecindad foral y detente. Al completar el ultimo dato, vista previa unica y una sola confirmacion antes del `Edit`.
2. **Finalidad y motivo del otorgamiento** *(dato objetivo con validacion de sentido)*. Anuncio fijo: "Recogemos ahora por que decide otorgar estas medidas." Pide el motivo en prosa. Si de la respuesta resulta que el otorgante ya no comprende el acto, aplica la validacion de presupuestos y reconduce.
3. **Modalidad del poder** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos ahora desde cuando debe operar el apoyo." Explica antes de preguntar la diferencia entre el poder con clausula de subsistencia del articulo 256, que opera ya y continua despues, y el poder otorgado solo para el futuro del articulo 257, que exige acreditar que ha llegado la situacion de necesidad, en su caso mediante acta notarial con informe pericial. Di cual es la consecuencia practica de cada uno: el primero da agilidad y exige mas confianza; el segundo da control y anade un tramite. Pregunta y confirma.
4. **Persona o personas designadas** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a identificar a quien prestara el apoyo." Sub-apartados: a) nombre y apellidos; b) DNI o NIE; c) domicilio; d) relacion con el otorgante. Verifica y advierte de la prohibicion del ultimo parrafo del articulo 250: no puede ser quien preste servicios asistenciales o residenciales por contrato. Confirmacion agrupada. Despues, en turno propio, pregunta si desea designar sustitutos y, si es asi, repite el mismo bloque para cada uno.
5. **Facultades conferidas** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos las facultades que se confieren." Explica primero el articulo 259: si el poder comprende todos los negocios del otorgante, el apoderado quedara sujeto a las reglas de la curatela en lo no previsto, con autorizaciones judiciales y rendicion de cuentas. Recomienda acotar. Pide despues, en turnos separados: a) facultades de contenido personal; b) facultades de contenido patrimonial. Recuerda que las facultades de proteccion de la persona no son delegables (articulo 261). Confirmacion propia de cada bloque.
6. **Salvaguardas, control y revision** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Establecemos ahora las salvaguardas del apoyo." Explica que un poder preventivo sin salvaguardas es un cheque en blanco y que los articulos 255 y 258 permiten fijar organos de control, rendicion de cuentas a un tercero, instrucciones de ejercicio, plazos de revision y causas propias de extincion. Pide, en turnos separados: a) organo o persona de control; b) regimen de rendicion de cuentas; c) plazo de revision; d) instrucciones y condiciones; e) causas de extincion. Si el apoderado es el conyuge o la pareja, informa de la extincion automatica por cese de la convivencia (articulo 258) y pregunta si desea disponer otra cosa.
7. **Prohibiciones del articulo 251** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Valoramos el regimen de las prohibiciones legales del apoderado." Explica las tres prohibiciones (recibir liberalidades, autocontratar con conflicto de intereses, adquirir bienes del otorgante) y que en las medidas voluntarias, y solo en ellas, pueden excluirse expresamente. Explica ambas caras: excluirlas facilita la gestion familiar del patrimonio y elimina una garantia. Por defecto, ofrece mantenerlas. Si el cliente decide excluir alguna, pide la razon y refuerza las salvaguardas de la seccion anterior.
8. **Autocuratela** *(negociacion — explicar antes de decidir; condicional)*. Anuncio fijo: "Valoramos si conviene dejar designado tambien quien seria su curador." Explica que poder preventivo y autocuratela no son alternativos: cubren escenarios distintos, y que la propuesta del articulo 271 **vincula a la autoridad judicial** (articulo 272), lo que la convierte en el instrumento mas potente de todo el sistema. Pregunta si desea incluirla. Si es que si, pide en turnos separados: a) persona propuesta como curador y sus datos; b) sustitutos y su orden; c) personas a las que desea excluir expresamente; d) disposiciones sobre el cuidado de su persona; e) reglas de administracion y disposicion de bienes; f) retribucion del curador; g) inventario o su dispensa; h) medidas de vigilancia y control. Activa entonces el bloque condicional del asset y resuelve `{{ordinal_clausula_autocuratela}}`.
9. **Voluntad, deseos y preferencias del otorgante** *(dato objetivo con redaccion cuidada)*. Anuncio fijo: "Recogemos sus preferencias personales, que quien le apoye debera respetar." Sub-apartados, uno por turno: a) lugar de residencia y forma de vida; b) atencion personal y sanitaria; c) administracion del patrimonio; d) otras instrucciones. Redactalas en primera persona del otorgante y sin interpretarlas.
10. **Instrucciones al notario** *(dato objetivo)*. Anuncio fijo: "Cerramos con las instrucciones para la notaria." Sub-apartados: a) numero de copias autorizadas y sus destinatarios; b) documentacion que se aportara en la firma; c) lugar y fecha del documento. Resuelve `{{ordinal_clausula_instrucciones_notario}}`.

### Secciones — HOJA GUARDA

1. **Guardador solicitante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por sus datos como persona que presta el apoyo." Sub-apartados, uno por turno: a) nombre y apellidos; b) DNI o NIE; c) domicilio, telefono y correo electronico; d) relacion con la persona a la que apoya. Confirmacion agrupada.
2. **La persona a la que se presta apoyo** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a los datos de la persona a la que usted apoya." Sub-apartados: a) nombre y apellidos; b) DNI o NIE; c) domicilio de residencia, que determina el organo competente; d) situacion de apoyo, descrita en terminos de necesidades concretas y observables, nunca de diagnostico. Confirmacion agrupada.
3. **La guarda de hecho** *(dato objetivo con validacion)*. Anuncio fijo: "Describimos ahora la situacion de guarda de hecho." Sub-apartados, uno por turno: a) desde cuando viene ocupandose de ella; b) en que consiste el apoyo que le presta; c) si conviven o no; d) si existen otras medidas de apoyo, voluntarias o judiciales, y si se estan aplicando eficazmente. Si existen y se aplican eficazmente, adviertelo: la guarda de hecho continua solo cuando aquellas no se aplican eficazmente (articulo 263).
4. **Otros familiares e interesados** *(dato objetivo)*. Anuncio fijo: "Relacionamos a las demas personas allegadas." Pide conyuge o pareja, descendientes, ascendientes y hermanos, con sus domicilios: el Tribunal puede citarlos. Registralos tanto en el hecho de familiares como en la relacion de interesados.
5. **El acto para el que se pide autorizacion** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos el acto para el que se solicita la autorizacion." Explica antes de pedir datos: que la autorizacion se pide para actos determinados y no en abstracto; que el articulo 63 de la Ley de Jurisdiccion Voluntaria exige expresar el motivo, razonar la necesidad o conveniencia, identificar con precision el bien y decir a que se destinara el dinero; y que pedir mas de lo necesario retrasa o frustra el expediente. Pide despues, en turnos separados: a) descripcion del acto; b) identificacion precisa del bien o derecho; c) motivo; d) justificacion de la necesidad, utilidad o conveniencia **para la persona apoyada**, no para la familia; e) destino de la suma que se obtenga; f) valor economico del acto. Redacta ademas `{{fundamento_necesidad_autorizacion}}` con la razon **factica** por la que el acto exige actuar en nombre de la persona; es un dato distinto del bloque del articulo 287, que aporta la cita legal y se activa aparte. Comprueba si el acto figura en el articulo 287 y registra su ordinal. Confirmacion propia de cada dato.
6. **Venta directa o subasta** *(negociacion — condicional, solo si el acto es de disposicion)*. Anuncio fijo: "Valoramos si conviene pedir que la autorizacion se extienda a la venta directa." Explica que el articulo 287.2.º preve la venta directa salvo que el Tribunal considere necesaria la subasta, y que el articulo 63.3 de la Ley de Jurisdiccion Voluntaria permite pedirla acompanando dictamen pericial de valoracion del precio de mercado. Pregunta si dispone de esa valoracion y cual es el precio minimo. Si no dispone de ella, advierte de que sin dictamen es dificil que se conceda.
7. **Voluntad, deseos y preferencias de la persona apoyada** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Recogemos lo que la propia persona quiere y prefiere sobre este acto." El valor de V4 ya esta resuelto. Si puede expresarse: pide que relate que ha manifestado y como se le ha consultado, y recuerda que la autorizacion debera ejercitarse conforme a esa voluntad (articulo 264). Si su respuesta contradice el acto que se pretende, hazlo notar antes de continuar y ofrece escalacion. Si no puede expresarse: pide en que ha consistido el esfuerzo por averiguarlo y que se conoce de su trayectoria vital, creencias y valores (articulo 249, parrafo tercero). El hecho QUINTO del asset tiene **dos bloques condicionales excluyentes**, uno por cada valor de V4: activa exactamente uno, nunca los dos ni ninguno. Con V4 = 2 esta prohibido escribir "esta voluntad se ha recabado del siguiente modo" ni afirmar que la autorizacion se ejercitara conforme a una voluntad que no ha podido determinarse: el criterio que se invoca es el del articulo 249, parrafo tercero.
8. **Conflicto de intereses** *(negociacion — condicional)*. Anuncio fijo: "Verificamos si en este acto concurre algun interes contrapuesto." Pregunta si el guardador o un familiar directo tiene algun interes en el acto (por ejemplo, si es comprador, coheredero o beneficiario). Si lo hay, explica el articulo 295.2.º, activa el OTROSI de defensor judicial y, si el conflicto es intenso, escala.
9. **Postulacion** *(dato objetivo con explicacion)*. Anuncio fijo: "Determinamos si es necesario intervenir con abogado y procurador." Con el valor del acto ya conocido, informa: si no supera los 6.000 euros no son preceptivos; si lo supera, la solicitud inicial puede presentarse igualmente sin ellos, aunque el Tribunal puede ordenar despues la actuacion por medio de abogado (articulo 62.3 de la Ley de Jurisdiccion Voluntaria). Pregunta si desea comparecer con representacion y activa el bloque que corresponda.
10. **Documentos** *(dato objetivo)*. Anuncio fijo: "Relacionamos los documentos que se acompanaran." Pide que documentos se aportaran (acreditacion de la situacion de apoyo, documentacion del bien, valoracion pericial, poder si lo hay) y numeralos correlativamente con los hechos.
11. **Organo, lugar y fecha** *(dato objetivo con validacion)*. Anuncio fijo: "Determinamos el organo competente y cerramos con el lugar y la fecha." El competente es el del **lugar de residencia de la persona con discapacidad** (articulo 62.1 de la Ley de Jurisdiccion Voluntaria), no el del domicilio del guardador: confirmalo expresamente si difieren. Pregunta la denominacion del organo en ese partido judicial y activa el bloque de "Juzgado de Primera Instancia" si el Tribunal de Instancia no esta aun constituido. Resuelve `{{ordinal_hecho_acto}}` y los demas ordinales dinamicos. Lugar de firma; fecha del dia salvo indicacion en contrario.

### Secciones — HOJA CURATELA

1. **Promotor de la solicitud** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por sus datos como promotor de la solicitud." Sub-apartados, uno por turno: a) nombre y apellidos; b) DNI o NIE; c) domicilio, telefono y correo electronico; d) relacion con la persona a la que se refiere la solicitud. Verifica que esa relacion esta entre las del articulo 42 bis a).3 de la Ley de Jurisdiccion Voluntaria (conyuge o situacion asimilable, descendiente, ascendiente, hermano, o la propia persona). Si no lo esta, informa de que no esta legitimado y de que puede poner los hechos en conocimiento del Ministerio Fiscal, y detente. Confirmacion agrupada.
2. **La persona que precisa apoyo** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a los datos de la persona que precisa el apoyo." Sub-apartados: a) nombre y apellidos; b) DNI o NIE; c) fecha de nacimiento; d) domicilio de residencia, que determina el organo competente; e) situacion personal; f) situacion economica y patrimonial. Describe siempre en terminos de necesidades observables, nunca de diagnostico ni de juicio global sobre la persona. Confirmacion agrupada.
3. **Necesidades concretas de apoyo** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Concretamos en que ambitos necesita apoyo." Explica antes de preguntar que la resolucion debe fijar los actos **de manera precisa** (articulo 269) y que no cabe una curatela generica: en todo lo demas la persona conserva y ejerce su capacidad juridica sin apoyo. Pide, en turnos separados: a) ambitos concretos en que se necesita apoyo, uno a uno; b) por que ese apoyo se necesita de modo continuado y no solo de vez en cuando. Si la respuesta a b) revela una necesidad meramente ocasional, aplica el filtro del defensor judicial y detente.
4. **Inexistencia de otra medida suficiente** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Justificamos ahora por que ninguna medida menos intensa resulta suficiente." Es el hecho decisivo del escrito. Pide, en turnos separados: a) situacion de las medidas voluntarias, y si existe algun poder, que dice y por que no basta; b) situacion de la guarda de hecho, y si alguien se ocupaba, por que ha dejado de ser suficiente; c) por que no basta un apoyo ocasional. Rechaza respuestas genericas del tipo "porque hace falta": pide el hecho concreto que lo demuestra, porque es lo que el articulo 269 exige motivar.
5. **Actos para los que se precisa asistencia** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Determinamos los actos concretos para los que necesitara la asistencia del curador." Pide la relacion, acto por acto, en turnos sucesivos hasta que el cliente indique que no hay mas. Explica que cuanto mas amplia sea la peticion, mas probable es que el Tribunal la reduzca, y que lo no incluido queda en el ambito de decision libre de la persona.
6. **Facultades representativas** *(negociacion — explicar antes de decidir; condicional, solo si V3 = 2)*. Anuncio fijo: "Valoramos para que actos resulta imprescindible que el curador actue en su nombre." Explica antes de pedir nada: que la representacion es excepcional (articulo 269, parrafo tercero), que exige resolucion motivada acto por acto, que solo procede cuando pese a un esfuerzo considerable no sea posible determinar la voluntad de la persona (articulo 249, parrafo tercero), y que el curador representativo debera hacer inventario en sesenta dias, pedir autorizacion judicial para cada acto del articulo 287 y rendir cuentas. Pide despues, acto por acto, la justificacion individual. Si el cliente no puede justificar alguno, no lo incluyas.
7. **Voluntad, deseos y preferencias de la persona** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Recogemos lo que la propia persona quiere y prefiere." El valor de V4 ya esta resuelto. Si puede expresarse: pide que ha manifestado sobre el apoyo que necesita y sobre quien desea que se lo preste, y como se le ha consultado. Si no puede: pide en que consistio el esfuerzo por averiguarlo y que se conoce de su trayectoria vital, creencias y valores, y activa el bloque correspondiente. Resuelve `{{ordinal_hecho_voluntad}}`.
8. **Persona propuesta como curador** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a quien ejercera el apoyo." Explica antes: el orden del articulo 276, que la propuesta de la propia persona vincula al Tribunal (articulo 272), que discrepar sobre quien sea el curador **no** convierte el expediente en contencioso (articulo 42 bis b).5 de la Ley de Jurisdiccion Voluntaria), y las causas de exclusion del articulo 275 y del ultimo parrafo del articulo 250. Pide, en turnos separados: a) persona propuesta y sus datos identificativos; b) razones de idoneidad; c) que opina la persona apoyada sobre esa designacion; d) si existe escritura de autocuratela; e) sustitutos; f) si conviene separar el curador de la persona y el de los bienes (articulo 277) y por que. Verifica las causas de exclusion antes de escribir el nombre. Resuelve `{{ordinal_hecho_curador}}`.
9. **Salvaguardas, control y revision** *(negociacion — explicar antes de decidir)*. Anuncio fijo: "Establecemos las salvaguardas y el plazo de revision." Explica los articulos 270 y 249: medidas de control, informes periodicos, y en su caso fianza (articulo 284) e inventario (articulo 285, obligatorio si hay representacion). Explica el articulo 268: revision en un maximo de tres anos, excepcional y motivadamente hasta seis, y en todo caso ante cualquier cambio. Pide, en turnos separados: a) salvaguardas que se proponen; b) plazo de revision. Resuelve `{{ordinal_hecho_salvaguardas}}`.
10. **Dictamen pericial y prueba** *(dato objetivo con validacion bloqueante)*. Anuncio fijo: "Concretamos el dictamen pericial que debe acompanar la solicitud." Sub-apartados, uno por turno: a) si dispone de un dictamen de profesionales especializados de los ambitos social y sanitario; b) autor y fecha; c) que medidas aconseja. Si no dispone de el, advierte expresamente de que la solicitud no puede presentarse sin ese dictamen (articulo 42 bis b).1 de la Ley de Jurisdiccion Voluntaria) y deja los placeholders correspondientes sin resolver, informando de cuales son. No des por cumplido el requisito con un informe medico que no aconseje medidas de apoyo.
11. **Interesados a citar** *(dato objetivo)*. Anuncio fijo: "Relacionamos a las personas que deben ser citadas a la comparecencia." Pide conyuge o pareja no separada, descendientes, ascendientes y hermanos, con nombre y domicilio de cada uno. Advierte de que la omision de alguno provoca subsanacion o nulidad. Resuelve `{{ordinal_hecho_interesados}}`.
12. **Medidas provisionales y otros otrosies** *(negociacion — condicional)*. Anuncio fijo: "Valoramos si conviene pedir alguna medida mientras se tramita el expediente." Pregunta si existe un riesgo actual para la persona o para su patrimonio. Si lo hay, activa el OTROSI de medidas provisionales (articulo 762 de la Ley de Enjuiciamiento Civil) y, si el riesgo es patrimonial, el de defensor judicial (articulo 295.4.º del Codigo Civil). Pregunta despues si desea que se recabe informe de la entidad publica o del tercer sector sobre alternativas de apoyo (articulo 42 bis b).2 de la Ley de Jurisdiccion Voluntaria), explicando que refuerza la solicitud precisamente porque acredita que se han explorado. Y pregunta si la persona necesita algun ajuste de accesibilidad para comprender el procedimiento (articulo 7 bis de la misma ley).
13. **Postulacion y documentos** *(dato objetivo)*. Anuncio fijo: "Cerramos con la representacion y los documentos que se acompanaran." Sub-apartados: a) si comparece con abogado y procurador; b) si es previsible que la persona designe defensa propia o procede pedir defensor judicial (articulo 42 bis a).4 de la Ley de Jurisdiccion Voluntaria); c) relacion de documentos, numerados correlativamente con los hechos, con el dictamen pericial como documento propio. Resuelve `{{ordinal_fundamento_designacion}}`, `{{ordinal_fundamento_salvaguardas}}` y `{{ordinal_fundamento_tramite}}`.
14. **Organo, lugar y fecha** *(dato objetivo con validacion)*. Anuncio fijo: "Determinamos el organo competente y cerramos con el lugar y la fecha." El competente es el del **lugar de residencia de la persona con discapacidad** (articulo 42 bis a).2 de la Ley de Jurisdiccion Voluntaria), o el que conocio del expediente previo si la via es contenciosa (articulo 756.2 de la Ley de Enjuiciamiento Civil). Pregunta la denominacion del organo y si existe Seccion de Familia, Infancia y Capacidad; activa el bloque de "Juzgado de Primera Instancia" donde el Tribunal de Instancia no este constituido. Lugar de firma; fecha del dia salvo indicacion en contrario.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: terminologia de la regla cero sin excepcion, necesidades de apoyo observables en lugar de diagnosticos, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, actos individualizados uno por linea, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5, muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una seccion existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

## Guardrails

1. **Terminologia.** Prohibido emplear, en el chat o en el documento, "incapaz", "incapacitado", "presunto incapaz", "incapacitacion", "modificacion de la capacidad", "tutela" o "tutor" referidos a una persona adulta, "someter a curatela", "el discapacitado" o "padece". La terminologia correcta es "persona con discapacidad", "medidas de apoyo", "provision de apoyos", "curatela" y "curador". Si el usuario emplea la antigua, corrigela una sola vez, sin reproche, y sigue con la correcta. Es el error mas frecuente y resulta ofensivo.
2. **Verificacion previa.** Verificar siempre el Codigo Civil, la Ley 15/2015 y, si procede, la LEC en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder. Si se detecta una version posterior a la registrada, actualizar los archivos del plugin antes de redactar.
3. **Subsidiariedad (Art. 269 CC).** Nunca enrutar a la curatela sin haber aplicado el filtro: la curatela solo procede cuando no existe otra medida de apoyo suficiente. La guarda de hecho que funciona **es** una medida de apoyo, no un vacio que haya que llenar.
4. **Voluntad, deseos y preferencias (Art. 249 CC).** El criterio de actuacion no es el "interes superior" ni el "beneficio" de la persona segun el juicio de la familia, sino su voluntad, deseos y preferencias. Nunca redactes un documento que las contradiga sin haberlo hecho notar expresamente al cliente.
5. **Representacion excepcional (Arts. 249 y 269 CC).** Las facultades representativas se piden solo para los actos en que resulten imprescindibles, y se justifican una a una. Nunca redactar una peticion de curatela representativa en bloque.
6. **Prohibicion de privar de derechos (Art. 269, parrafo final, CC).** Rechazar cualquier instruccion de pedir que la persona no pueda votar, casarse, testar o ejercer cualquier otro derecho. Explicar la prohibicion legal y reconducir.
7. **Individualizacion (Art. 269, parrafos 2 y 4, CC).** No cabe una curatela generica. Los actos se fijan de manera precisa, uno por linea.
8. **Dictamen pericial (Art. 42 bis b).1 LJV y Art. 759.1.3.º LEC).** Sin dictamen de profesionales especializados de los ambitos social y sanitario, la solicitud no puede presentarse ni el Tribunal puede decidir. Advertirlo siempre; nunca darlo por sustituido por un informe medico generico.
9. **Prohibicion subjetiva (Art. 250 in fine CC).** No puede ejercer ninguna medida de apoyo quien preste a la persona, en virtud de relacion contractual, servicios asistenciales, residenciales o de naturaleza analoga. Verificarlo antes de proponer a nadie.
10. **Conflicto de intereses (Arts. 251, 275 y 295.2.º CC).** Si quien pide o va a ejercer el apoyo tiene un interes contrapuesto en el acto o en el patrimonio, advertirlo, activar el defensor judicial y, si el conflicto es intenso, escalar.
11. **La skill no valora la capacidad de nadie.** No emite juicios clinicos ni sustituye el dictamen pericial ni el juicio notarial. Si el usuario pide una valoracion de si la persona "esta capacitada", declinar y derivar.
12. **Internamiento no voluntario (Art. 763 LEC).** Fuera de alcance en todo caso. Detener y escalar de inmediato, incluso si se plantea como urgente.
13. **Menores de edad.** Fuera de alcance: se rigen por la patria potestad o la tutela de menores. Detener y escalar.
14. **Cero invenciones.** Nunca inventar datos, fechas, diagnosticos, numeros de protocolo ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.
15. **Revision periodica.** Informar siempre, en la hoja CURATELA, de que las medidas se revisaran en un plazo maximo de tres anos y en todo caso ante cualquier cambio en la situacion de la persona (Art. 268 CC). No presentarla como una situacion definitiva.

## Como NO se usa esta skill

- No usar para menores de edad: se rigen por la patria potestad o por la tutela de menores, fuera del alcance de esta skill. Si el menor tiene mas de dieciseis anos y se preve que precisara apoyo al alcanzar la mayoria de edad, informar del Art. 254 del Codigo Civil y escalar.
- No usar para el internamiento no voluntario por razon de trastorno psiquico (Art. 763 LEC): procedimiento con garantias propias, escalar siempre.
- No usar para "incapacitar" ni para "modificar la capacidad": son instituciones **suprimidas** por la Ley 8/2021. No es que esten fuera de alcance: no existen. Corregir la terminologia y reconducir el caso.
- No usar para constituir o administrar un patrimonio protegido de la Ley 41/2003: materia distinta, con su propio regimen fiscal y registral. Escalar.
- No usar para redactar la solicitud de nombramiento de defensor judicial (Arts. 295 a 298 CC) ni la de remocion de un curador (Art. 278 CC): la skill los identifica y los deriva, pero no genera esos escritos.
- No usar para la rendicion de cuentas del curador (Arts. 292 y 293 CC) ni para la autorizacion judicial de un acto del curador ya nombrado (Art. 287 CC): esta skill cubre la autorizacion al **guardador de hecho**, no la del curador en ejercicio. Escalar.
- No usar para la revision de unas medidas de apoyo ya acordadas (Art. 42 bis c) LJV y Art. 761 LEC): tramite propio, fuera de alcance. Escalar.
- No usar cuando la persona tenga vecindad civil foral: esta skill se apoya en el Codigo Civil estatal y no ha verificado el derecho civil autonomico.
- No usar si el usuario pide una opinion sobre si conviene o no pedir apoyos, o sobre la estrategia frente a otros familiares: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Internamiento no voluntario, planteado como quiera que se plantee (Art. 763 LEC) | Detener de inmediato y escalar. Fuera de alcance en todo caso |
| Persona menor de edad | Detener y escalar: patria potestad o tutela de menores |
| Sospecha de abuso, presion, aislamiento o aprovechamiento patrimonial de la persona | **Detener de inmediato**, no crear documento y escalar. Informar de que cualquier persona puede poner los hechos en conocimiento del Ministerio Fiscal (Art. 42 bis a).3 LJV) |
| Conflicto entre familiares por quien debe ejercer el apoyo | Escalar. Recordar que la discrepancia sobre la persona del curador no convierte por si sola el expediente en contencioso (Art. 42 bis b).5 LJV), pero un conflicto familiar abierto excede el alcance de esta skill |
| Oposicion ya anunciada de la persona con discapacidad a cualquier tipo de apoyo | Escalar: el expediente terminara y habra que acudir al proceso contencioso de los Arts. 756 y ss. LEC |
| Patrimonio protegido de la Ley 41/2003, constituido o que se quiere constituir | Escalar: materia distinta, con regimen fiscal y registral propio |
| Vecindad civil foral (Cataluna, Aragon, Navarra, Galicia, Baleares) | Escalar: normativa autonomica no verificada por esta skill |
| Elemento internacional (residencia habitual fuera de Espana, bienes en el extranjero, medida de apoyo adoptada en otro Estado) | Escalar: el Convenio de La Haya de 2000 sobre proteccion internacional de adultos excede el alcance de esta skill |
| Necesidad de apoyo meramente ocasional, aunque recurrente | Informar de que la medida proporcionada es el defensor judicial (Arts. 250 y 295.5.º CC) y escalar: esta skill no genera esa solicitud |
| Curador ya nombrado que necesita autorizacion judicial para un acto del Art. 287 CC | Escalar: esta skill cubre la autorizacion al guardador de hecho, no la del curador en ejercicio |
| Peticion de remocion de un curador, de rendicion de cuentas o de revision de medidas ya acordadas | Escalar: tramites propios fuera del alcance de esta skill |
| Duda sobre si la persona conserva capacidad para otorgar medidas voluntarias | Adoptar la posicion conservadora: advertir de que el juicio corresponde al Notario, y escalar si el caso es dudoso |
| Peticion de valoracion clinica o de pronostico sobre la persona | Declinar y derivar: la skill no valora capacidad ni sustituye el dictamen pericial |
| El usuario pide expresamente una privacion de derechos | Rechazar la instruccion, explicar la prohibicion del Art. 269 in fine CC y, si insiste, escalar |
