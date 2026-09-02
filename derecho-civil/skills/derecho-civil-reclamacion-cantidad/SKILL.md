---
name: derecho-civil-reclamacion-cantidad
description: >
  Genera el documento adecuado para reclamar (o defenderse de la reclamacion de) una cantidad de dinero,
  eligiendo la via procesal correcta conforme a la LEC verificada en el BOE: peticion inicial de proceso
  monitorio (deuda documentada, liquida, vencida y exigible, cualquier cuantia), demanda de juicio verbal
  (hasta 15.000 euros o rentas de arrendamiento), demanda de juicio ordinario (mas de 15.000 euros, incluida
  la posterior a la oposicion de un monitorio, Art. 818.2 LEC), escrito de oposicion al monitorio (posicion
  de deudor) y burofax de requerimiento previo (MASC, LO 1/2025). NO usar para pretensiones no dinerarias,
  materias del Art. 249.1 LEC cuya pretension principal no sea el pago, reclamaciones frente a
  Administraciones Publicas, desahucios ni ejecuciones.
when_to_use: |
  - El usuario quiere reclamar judicialmente una cantidad de dinero y no sabe (o no indica) por que via.
  - El usuario quiere iniciar la reclamacion de una deuda con o sin documentos que la acrediten.
  - El usuario ha iniciado un monitorio, el deudor se ha opuesto y la cuantia obliga a demandar en ordinario.
  - El cliente ha recibido un requerimiento de pago de un proceso monitorio y quiere oponerse.
  - El usuario necesita el burofax de requerimiento previo (intento de MASC) antes de reclamar.
inputs:
  - rol: el cliente reclama una cantidad (acreedor) / ha recibido un requerimiento de monitorio (deudor)
  - estado_reclamacion: sin reclamacion judicial iniciada / monitorio propio con oposicion del deudor
  - deuda_documentada: existen documentos que acreditan la deuda (si / no)
  - deuda_vencida_liquida: la cantidad esta vencida y su importe es fijo o calculable (si / no; si no, subclasificar en discutida o no vencida)
  - cuantia: importe reclamado en euros (determina verbal u ordinario en el declarativo)
  - es_arrendamiento: la cantidad deriva de rentas o cantidades debidas por arrendamiento de inmueble (si / no)
  - masc_intentado: se ha intentado un medio adecuado de solucion de controversias (si / no)
  - datos_parte_reclamante: nombre o razon social, NIF/CIF, domicilio, representante si persona juridica
  - datos_parte_contraria: nombre o razon social, NIF/CIF, domicilio o lugar donde pueda ser hallado
  - origen_deuda: descripcion del origen y relacion de documentos acreditativos
  - intereses: legales o pactados, y fecha desde la que se devengan
  - deudor_consumidor: la deuda se funda en un contrato entre empresario y consumidor (si / no)
  - partido_judicial: para la competencia territorial
  - datos_monitorio_previo: juzgado, numero de autos y cuantia (solo oposicion o demanda del Art. 818.2)
  - motivos_oposicion: alcance (total / parcial) y razones fundadas (solo oposicion)
outputs:
  - peticion_monitorio: peticion inicial de proceso monitorio en markdown, DRAFT
  - demanda_juicio_verbal: demanda de juicio verbal de reclamacion de cantidad en markdown, DRAFT
  - demanda_juicio_ordinario: demanda de juicio ordinario de reclamacion de cantidad en markdown, DRAFT
  - oposicion_monitorio: escrito de oposicion a proceso monitorio en markdown, DRAFT
  - burofax_masc: opcional, burofax de requerimiento previo de pago en markdown, DRAFT
references:
  - references/lec-vias-reclamacion-cantidad.md
  - references/masc-requisito-procedibilidad-lo1-2025.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/peticion-monitorio.md
  - assets/demanda-juicio-verbal.md
  - assets/demanda-juicio-ordinario.md
  - assets/oposicion-monitorio.md
  - assets/burofax-masc-reclamacion.md
---

# Reclamacion de Cantidad

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija que la skill defina y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificacion normativa interna, ejecutala en silencio y continua hasta la primera pregunta o hasta la Confirmacion visible, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

Esta linea es, junto con la introduccion fija, la UNICA excepcion a la prohibicion de mencionar la mecanica interna. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores, la validacion de procedibilidad, la verificacion normativa y la creacion base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2") o de hojas del arbol.
- Resumenes de validacion con checks (ej. "Dato resuelto ✔").
- Fases de instruccion (ej. "Ahora voy a crear el documento", "Pasemos al punto 4").
- Preambulos conversacionales antes de hacer preguntas. Si es tu turno de preguntar, emite unicamente la pregunta exacta — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez, en el primer turno de toda la conversacion, y de los anuncios de seccion del Punto 5.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de clasificacion, y solo la primera vez, anade en el mismo mensaje esta introduccion fija, en el registro formal del plugin:

"Vamos a preparar la reclamacion de la cantidad adeudada por la via procesal que corresponda a su caso. Para determinarla correctamente, es necesario precisar antes algunos datos."

(Si el cliente indica desde el primer mensaje que ha RECIBIDO un requerimiento de monitorio, usa en su lugar: "Vamos a preparar su escrito de oposicion al proceso monitorio. Para ajustarlo correctamente a su caso, es necesario precisar antes algunos datos.")

Tu primer objetivo es resolver los siguientes vectores de manera SILENCIOSA usando Escucha Activa:

- **V1 (Posicion del cliente):** acreedor que reclama / deudor requerido en un monitorio.
- **V2 (Estado de la reclamacion):** sin reclamacion judicial iniciada / monitorio propio ya iniciado con oposicion del deudor. (Solo si V1 = acreedor.)
- **V3 (Acreditacion documental):** existen documentos que acreditan la deuda: si / no. (Solo si V1 = acreedor y V2 = sin iniciar.)
- **V4 (Liquidez y vencimiento):** la cantidad esta vencida y su importe es fijo o calculable con una simple operacion / esta discutida, por determinar o pendiente de vencer. (Solo si V1 = acreedor y V2 = sin iniciar.)
- **V5 (Cuantia y arrendamiento):** importe en euros; y si deriva de rentas o cantidades debidas por arrendamiento de inmueble. (Solo si la via es declarativa: verbal u ordinario.)
- **V6 (MASC):** se ha intentado un medio de solucion previa: si / no. (Solo si V1 = acreedor y el escrito es iniciador; NO aplica a la oposicion ni a la demanda del Art. 818.2.)

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto (omitiendo las que la Escucha Activa ya haya resuelto o las que no apliquen a la rama):

* Para V1:
  "Su situacion es la siguiente:
  1. Desea reclamar una cantidad que le adeudan
  2. Ha recibido un requerimiento de pago de un juzgado (proceso monitorio) y desea oponerse"

* Para V2 (solo si V1 = 1). **Valor por defecto — no preguntar en frio:** V2 se resuelve como "sin reclamacion iniciada" salvo que el mensaje del usuario contenga algun indicio de procedimiento previo (menciones a un juzgado, numero de autos, requerimiento judicial u oposicion). Solo si existe ese indicio y el estado no queda claro, formula:
  "La reclamacion se encuentra en este punto:
  1. Aun no se ha presentado ninguna reclamacion judicial
  2. Ya se presento una peticion de proceso monitorio y el deudor se ha opuesto"

* Para V3 (solo si V2 = 1):
  "Dispone de documentos que acrediten la deuda (contrato, facturas, albaranes, reconocimiento de deuda, certificaciones):
  1. Si
  2. No"

* Para V4 (solo si V2 = 1):
  "El importe que reclama:
  1. Esta vencido y es una cifra fija o calculable con una simple operacion
  2. Esta discutido, por determinar o pendiente de vencer"
  → Solo si la respuesta es 2 y no queda claro cual de los casos es: "La situacion del importe es:
  1. El deudor lo discute o esta por determinar
  2. La deuda todavia no ha vencido"

* Para V5 (solo en via declarativa; la cuantia se pregunta en prosa, no con opciones):
  "Indique la cantidad total que desea reclamar, en euros."
  → Solo si la cuantia supera 15.000 euros y no consta el origen: "La cantidad deriva de rentas o de otras cantidades debidas por el arrendamiento de un inmueble:
  1. Si
  2. No"

* Para V6:
  "Se ha intentado ya una solucion previa con la otra parte (burofax de requerimiento, negociacion, mediacion):
  1. Si, y puede acreditarse documentalmente
  2. No"

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores aplicables, evalua en este orden:

- Si V1 = deudor requerido → **HOJA OPOSICION**: `assets/oposicion-monitorio.md`. V3-V6 no aplican.
- Si V1 = acreedor y V2 = monitorio con oposicion:
  - Cuantia > 15.000 euros → **HOJA ORDINARIO-818**: `assets/demanda-juicio-ordinario.md` (activar los bloques condicionales del Art. 818.2; V6 no aplica: la demanda trae causa del monitorio).
  - Cuantia <= 15.000 euros → **DETENER**: tras la oposicion, el asunto continua como juicio verbal dentro del mismo procedimiento (impugnacion de la oposicion en 10 dias, Art. 818.1 LEC); no procede una nueva demanda. Informar del cauce y del plazo, y ofrecer escalacion. No crear documento.
- Si V1 = acreedor, V2 = sin iniciar, V3 = si y V4 = vencida y liquida → **HOJA MONITORIO**: `assets/peticion-monitorio.md` (cualquier cuantia). Si V6 = no → generar ademas ANTES `assets/burofax-masc-reclamacion.md`.
- Si V1 = acreedor, V2 = sin iniciar y (V3 = no, o V4 = discutida/por determinar) → via declarativa:
  - Cuantia <= 15.000 euros, o rentas/cantidades de arrendamiento de inmueble (cualquier cuantia, Art. 250.1.1º LEC) → **HOJA VERBAL**: `assets/demanda-juicio-verbal.md`.
  - Cuantia > 15.000 euros (no arrendamiento) o interes economico imposible de calcular → **HOJA ORDINARIO**: `assets/demanda-juicio-ordinario.md`.
  - En ambas, si V6 = no → generar ademas ANTES `assets/burofax-masc-reclamacion.md` (requisito de procedibilidad, Arts. 264 y 403.2 LEC).
- Si V4 = pendiente de vencer → **DETENER**: la deuda no es exigible todavia; no cabe reclamarla judicialmente. Advertir y no crear documento.
- Si la pretension principal NO es el pago de una cantidad (materia del Art. 249.1 LEC, obligaciones de hacer, entrega de cosa) → **DETENER**: fuera de alcance; derivar a la skill correspondiente (`derecho-civil-juicio-ordinario`) o a escalacion.

### Validacion de procedibilidad (interno, antes del Punto 3)

- **HOJA MONITORIO:** confirmar deuda dineraria, liquida, determinada, vencida y exigible con documento del Art. 812; competencia del Juzgado de Primera Instancia del domicilio del deudor (Art. 813, sin sumision); si el deudor es ilocalizable, advertir de la limitacion. Si la deuda se funda en contrato empresario-consumidor, anotar el control de oficio del Art. 815.4 para explicarlo en el Punto 5.
- **HOJA VERBAL / ORDINARIO:** verificar que la cuantia se puede fijar (Arts. 251-253); en verbal <= 2.000 euros, informar de que no son preceptivos abogado ni procurador (Arts. 23.2.1º y 31.2.1º) y de que existe formulario normalizado del CGPJ; en ordinario, abogado y procurador preceptivos.
- **HOJA ORDINARIO-818:** verificar que esta dentro del plazo de UN MES desde el traslado del escrito de oposicion (Art. 818.2). Si el plazo esta vencido o proximo a vencer, advertirlo de inmediato.
- **HOJA OPOSICION:** verificar que esta dentro del plazo de VEINTE DIAS desde el requerimiento (Art. 815.1). Si el plazo esta vencido, advertir del riesgo de despacho de ejecucion (Art. 816) y ofrecer escalacion. Si la cuantia reclamada excede de 2.000 euros, informar de que la oposicion requiere abogado y procurador.
- **MASC:** en las hojas iniciadoras con V6 = no, integrar el burofax previo (posicion conservadora, ver `references/masc-requisito-procedibilidad-lo1-2025.md`).

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA (Interno, OBLIGATORIO antes de redactar)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar.

**2.1 — Leer la version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" de la LEC, de la LO 1/2025 y de los modelos del CGPJ.

**2.2 — Consultar la fuente oficial vigente.** Consultar el texto consolidado de la LEC:
```
read_document(path: "https://www.boe.es/buscar/act.php?id=BOE-A-2000-323", format: "text")
```
Extraer: fecha del texto consolidado vigente; redaccion actual de los articulos que apliquen a la hoja enrutada (812-818 y 815.4 para monitorio y oposicion; 249.2, 250 y 437 y ss. para verbal; 249.2 y 399 y ss. para ordinario; 264 y 403.2 para el MASC en todas las hojas iniciadoras).

Consultar los modelos normalizados del CGPJ segun la hoja:
```
read_document(path: "https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/El-proceso-monitorio", format: "text")
read_document(path: "https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/El-juicio-verbal-", format: "text")
```

**2.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar Write/Edit para:
- Actualizar `references/lec-vias-reclamacion-cantidad.md` y/o `references/masc-requisito-procedibilidad-lo1-2025.md` con la redaccion vigente.
- Si el CGPJ publica un modelo posterior, actualizar la estructura del asset afectado (`peticion-monitorio.md` o `demanda-juicio-verbal.md`).
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**2.5 — Fallback si la fuente no es accesible.** Si la lectura falla (error HTTP, timeout):
```
web_search("Ley Enjuiciamiento Civil articulos [los de la hoja enrutada] texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. El documento se genera con la version de referencia. Verificar manualmente antes de presentar."

## 3. CONFIRMACION (visible al usuario)

Tras completar la verificacion (Punto 2), en un unico mensaje:

1. **Informa la via y la fuente aplicable.** Indica al usuario que via procesal corresponde a su caso y por que, citando la norma con nombre completo y articulo, con el enlace del BOE consultado. Textos fijos por hoja (adaptar solo el dato de cuantia):
   - MONITORIO: "A su caso corresponde el proceso monitorio, regulado en los articulos 812 y siguientes de la Ley 1/2000, de Enjuiciamiento Civil, al tratarse de una deuda dineraria, liquida, vencida y exigible acreditada documentalmente, cualquiera que sea su cuantia. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - VERBAL: "A su caso corresponde el juicio verbal, conforme al articulo 250 de la Ley 1/2000, de Enjuiciamiento Civil, por no exceder la cuantia de 15.000 euros [o: por tratarse de rentas o cantidades debidas por arrendamiento de inmueble, articulo 250.1.1º]. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - ORDINARIO: "A su caso corresponde el juicio ordinario, conforme al articulo 249.2 de la Ley 1/2000, de Enjuiciamiento Civil, por exceder la cuantia de 15.000 euros. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - ORDINARIO-818: anadir ademas "Al haberse opuesto el deudor en el proceso monitorio, la demanda debe interponerse en el plazo de un mes desde el traslado del escrito de oposicion, conforme al articulo 818 de la misma ley."
   - OPOSICION: "Su escrito se rige por los articulos 815 y 818 de la Ley 1/2000, de Enjuiciamiento Civil: dispone de veinte dias desde el requerimiento para formular una oposicion fundada y motivada. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323"
   - Si la hoja incluye burofax previo (V6 = no), anadir: "Con caracter previo se preparara un burofax de requerimiento de pago, que acredita el intento de solucion extrajudicial exigido por la Ley Organica 1/2025 (articulos 264 y 403.2 de la Ley de Enjuiciamiento Civil). Tenga en cuenta que la demanda no debe presentarse hasta disponer del justificante del envio del burofax y haber dejado un plazo razonable de respuesta."
2. **Ofrece la plantilla o pide el documento propio.** En el mismo mensaje:
   "¿Que documento desea utilizar como base?
   1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
   2. Adjuntar su propio documento"
3. **Enruta segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte, leelo con `Read` y usalo como documento base en el Punto 4 en lugar del asset, sin dejar de aplicar los guardrails del dominio (advierte si el documento adjuntado los incumple).

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente tras la Confirmacion (Punto 3), estas OBLIGADO a crear el documento (si la hoja incluye burofax previo, crear PRIMERO el burofax y despues el escrito judicial, cada uno con su ciclo completo; los campos que dependen del envio del burofax — `{{fecha_masc}}`, `{{fecha_burofax}}`, numero del documento justificante — quedan como placeholders y se recuerda al usuario que el escrito judicial no debe presentarse hasta disponer del justificante):

1. Utiliza `Read` para leer el documento base decidido (el asset de la hoja, o el que adjunto el usuario).
2. Reemplaza en memoria TODOS los datos que ya poseas (vectores, escucha activa e investigacion: incluida `fecha_verificacion_lec` del Punto 2). Los faltantes conservan el nombre propio del placeholder del asset; usa un marcador generico solo para un hueco suelto sin placeholder propio, y nunca repitas el mismo marcador generico dos veces en el mismo documento (`Edit` necesita un `oldString` unico).
3. Utiliza `Write` para guardar el archivo en disco (nombre en `snake_case.md`, ej. `peticion_monitorio_acreedor_a.md`, `demanda_juicio_verbal_actor_a.md`, `oposicion_monitorio_deudor_a.md`).
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. Inmediatamente despues, en la misma respuesta, pregunta si desea empezar a completar los datos del documento. Solo tras la confirmacion, formula la primera pregunta de la edicion incremental (Punto 5).

## 5. EDICION INCREMENTAL DE SECCIONES

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion, no lances en frio la pregunta de la siguiente. En el mismo mensaje, antes de esa pregunta, emite el anuncio fijo de la seccion que se abre y, a continuacion, su primera pregunta. Un dato por turno; los datos identificativos de una misma parte se acumulan y se confirman con una unica vista previa conjunta (confirmacion agrupada por parte); las clausulas de negociacion se explican y se confirman una a una.

**Propagacion de un dato confirmado (regla global de Edit):** varios datos (nombre y NIF de cada parte, cuantia) aparecen repetidos literalmente en mas de un punto del asset (encabezamiento/titulo, bloque de datos, cuerpo del EXPONE/HECHOS, SUPLICO y firma). Al confirmar el dato, sustituyelo mediante `Edit` en TODAS sus apariciones del documento, no solo en el bloque de datos donde se pregunto; verifica con `Read` que no queden placeholders sueltos del mismo dato ya confirmado.

### Secciones — HOJA MONITORIO / HOJA VERBAL / HOJA ORDINARIO / HOJA ORDINARIO-818

1. **Parte reclamante** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Comenzamos por la identificacion de la parte que reclama." Sub-apartados, uno por turno: a) nombre completo o razon social; b) NIF o CIF; c) domicilio a efectos de notificaciones; d) solo si es persona juridica: nombre, NIF y cargo del representante; e) solo en ORDINARIO y ORDINARIO-818 (y en VERBAL si la cuantia excede de 2.000 euros): nombre del procurador y del letrado. Al completar el ultimo, vista previa unica con todos los datos y una sola confirmacion antes del `Edit`.
2. **Parte deudora / demandada** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a la identificacion de la parte deudora." Sub-apartados: a) nombre o razon social; b) NIF o CIF si se conoce; c) domicilio o lugar donde pueda ser hallada. Confirmacion agrupada.
3. **Origen de la deuda y prueba documental** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Abordamos ahora el origen de la deuda y su acreditacion documental." Antes de registrar la relacion de documentos, explica que documentos sirven para acreditar la deuda (en monitorio, los del articulo 812 de la LEC: firmados por el deudor, o facturas, albaranes y certificaciones habituales del trafico; en las demandas, los documentos fundamentales del articulo 265, con preclusion del 269) y confirma con el usuario cuales aportara y en que orden se numeraran. El origen y la fecha de vencimiento ya aportados en el mensaje inicial (escucha activa) no se vuelven a preguntar en bruto: se dan por confirmados y solo se solicitan los datos concretos que falten (numero e importe de cada documento, fecha exacta de cada vencimiento, fecha del contrato). Si hay mas de un documento con vencimientos distintos, recoge la fecha de cada uno y numeralos correlativamente en `{{relacion_documentos}}`; no fuerces una unica fecha de vencimiento cuando existan varias. Si no se desprende ya del origen descrito si el deudor actua como consumidor frente a un empresario, pregunta directamente: "¿El deudor contrato como consumidor particular o actuaba tambien como empresario o profesional?". Si la deuda se funda en un contrato entre empresario y consumidor, explica aqui el control de oficio de clausulas abusivas (articulo 815.4 LEC en el monitorio) y sus consecuencias antes de continuar.
4. **Cuantia, intereses y costas** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Pasamos a la determinacion de la cuantia, los intereses y las costas." El principal ya resuelto en la clasificacion se reutiliza sin volver a preguntarlo. Explica la eleccion de intereses antes de pedir la decision: interes legal del dinero desde la constitucion en mora (articulos 1100 y 1108 del Codigo Civil, normalmente desde el requerimiento o el vencimiento) o interes pactado en el contrato si existe; y desde que fecha se devengan. Explica que las costas se solicitan conforme al articulo 394 de la LEC. En HOJA MONITORIO no incluyas una peticion expresa de costas en el SUPLICO: la peticion inicial no es todavia un procedimiento contencioso con sentencia; limitate a advertir de que, si el deudor se opone (paso a verbal u ordinario) o hay que instar la ejecucion, las costas de esas fases posteriores se rigen por sus normas especificas. Confirmacion una a una (intereses primero, costas despues).
5. **Juzgado competente** *(dato objetivo con validacion)*. Anuncio fijo: "Determinamos ahora el juzgado competente." En MONITORIO: partido judicial del domicilio o residencia del deudor (articulo 813 LEC, sin sumision a otro fuero: si el usuario propone otro, advertir y corregir). En VERBAL y ORDINARIO: fuero general del domicilio del demandado (articulos 50 y 51 LEC) salvo fuero especial aplicable. En ORDINARIO-818: el mismo juzgado que conocio del monitorio.
6. **Solucion previa (MASC)** *(solo si la hoja incluye burofax, clausula de negociacion)*. Anuncio fijo: "Concretamos por ultimo los terminos del requerimiento previo de pago." Sub-datos del burofax, uno por turno: plazo de pago que se concede (explicar que es practica habitual conceder 10 dias habiles), medio de pago (cuenta IBAN u otro) y via de contacto para negociar. Confirmacion una a una.
7. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Lugar de firma; la fecha por defecto es la del dia, salvo indicacion en contrario.

### Secciones — HOJA OPOSICION

1. **Datos del procedimiento** *(dato objetivo — confirmacion agrupada)*. Anuncio fijo: "Comenzamos por los datos del procedimiento que consta en el requerimiento recibido." Sub-apartados, uno por turno: a) juzgado (numero y partido judicial); b) numero de autos del monitorio; c) nombre del acreedor que reclama; d) cantidad reclamada; e) fecha en que recibio el requerimiento (para validar el plazo de veinte dias: si esta vencido, advertir y ofrecer escalacion antes de continuar). Confirmacion agrupada.
2. **Datos del cliente (deudor)** *(dato objetivo — confirmacion agrupada por parte)*. Anuncio fijo: "Pasamos a su identificacion como parte." Sub-apartados: a) nombre completo o razon social; b) NIF o CIF; c) domicilio; d) solo si la cuantia reclamada excede de 2.000 euros: nombre del procurador y del letrado (preceptivos; si no los tiene, advertir de que debe designarlos). Confirmacion agrupada.
3. **Alcance y motivos de la oposicion** *(clausula de negociacion — explicar antes de decidir)*. Anuncio fijo: "Abordamos ahora el contenido de la oposicion." Explica antes de pedir la decision: la oposicion debe ser fundada y motivada (articulo 815.1 LEC), una negativa generica puede ser rechazada; puede ser total o parcial (pluspeticion: reconocer una parte y discutir el exceso); si la deuda deriva de un contrato con un empresario siendo el cliente consumidor, pueden alegarse clausulas abusivas. Pide el alcance (total o parcial, y en su caso la cantidad reconocida), despues los motivos concretos (prosa) y los documentos de apoyo. Confirmacion una a una (alcance, motivos, documentos).
4. **Efectos y via posterior** *(informativo, sin pregunta)*. Anuncio fijo: "Le informo de los efectos de la oposicion." Informar: hasta 15.000 euros el asunto sigue como juicio verbal (el acreedor podra impugnar la oposicion en diez dias); por encima, el acreedor debera demandar en juicio ordinario en un mes (articulo 818 LEC). No requiere dato del usuario; encadenar con la seccion siguiente.
5. **Lugar y fecha** *(dato objetivo)*. Anuncio fijo: "Cerramos con el lugar y la fecha del escrito." Igual que en las demas hojas.

Al rellenar cualquier hoja, aplica el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo, HECHOS o ALEGACIONES numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos, y SUPLICO ajustado a lo estrictamente pedido.

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5, muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una seccion existente.
2. Anadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

## Guardrails

1. Verificar siempre la LEC en el BOE antes de redactar (Punto 2). Sin verificacion, no proceder.
2. Si se detecta una version de la LEC o un modelo del CGPJ posterior al registrado en las references, actualizar los archivos del plugin antes de redactar. No usar una version desactualizada.
3. El monitorio solo procede con deuda dineraria, liquida, determinada, vencida y exigible acreditada con documento (Art. 812). Si falla cualquier requisito, enrutar al declarativo o detener; nunca forzar la via.
4. El umbral entre verbal y ordinario es 15.000 euros (Arts. 249.2 y 250.2); las rentas de arrendamiento van a verbal cualquiera que sea la cuantia (Art. 250.1.1º). No admitir elecciones de via contrarias a estos articulos aunque el usuario las pida.
5. Competencia del monitorio: exclusiva del Juzgado de Primera Instancia del domicilio del deudor (Art. 813). No admitir sumision a otro fuero.
6. Posicion conservadora sobre el MASC: en todo escrito iniciador sin intento previo acreditado, recomendar e integrar el burofax y advertir de la cuestion (LO 1/2025).
7. Plazos criticos: 20 dias para oponerse (Art. 815.1) y 1 mes para la demanda de ordinario tras la oposicion (Art. 818.2). Validarlos antes de redactar; si estan vencidos, advertir y no dar falsas expectativas.
8. Nunca inventar datos, cuantias, fechas ni jurisprudencia. Los campos no proporcionados quedan como `{{dato}}`.
9. Nunca afirmar que la deuda es exigible o incontrovertida sin base documental; nunca garantizar el resultado del procedimiento.
10. Si el deudor es consumidor y la deuda nace de un contrato con un empresario, informar siempre del control de oficio de clausulas abusivas (Art. 815.4 LEC) antes de cerrar la cuantia.

## Como NO se usa esta skill

- No usar para pretensiones no dinerarias (entrega de cosa, obligaciones de hacer o no hacer) ni declarativas puras.
- No usar para materias del Art. 249.1 LEC cuya pretension principal no sea la condena al pago: derivar a la skill `derecho-civil-juicio-ordinario`.
- No usar para reclamar a una Administracion Publica.
- No usar para desahucios por falta de pago (skill `derecho-civil-desahucio`) ni para la ejecucion de titulos.
- No usar para redactar la impugnacion de la oposicion en el verbal transformado (Art. 818.1) ni la contestacion a una demanda: advertir y escalar.
- No usar si el usuario pide opinion juridica sobre la estrategia de un litigio: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Deuda no vencida o pretension no dineraria | Advertir que no cabe la reclamacion por esta via y ofrecer escalacion |
| Oposicion recibida en monitorio propio de cuantia <= 15.000 euros | Informar del cauce del Art. 818.1 (impugnacion en 10 dias) y escalar: fuera del alcance de la skill |
| Plazo de oposicion (20 dias) o de demanda del Art. 818.2 (1 mes) vencido | Advertir de las consecuencias (ejecucion / sobreseimiento con costas) y escalar |
| Deudor ilocalizable (sin domicilio ni lugar donde ser hallado) | Advertir de la limitacion del Art. 813 y ofrecer escalacion |
| Deudor consumidor con clausulas potencialmente abusivas determinantes de la cuantia | Advertir del Art. 815.4 LEC y ofrecer revision por especialista (ver skill `derecho-civil-reclamacion-clausulas-abusivas`) |
| Duda sobre la exigibilidad del MASC en el caso concreto | Advertir y recomendar confirmar con el juzgado competente |
| Litigio conexo, reconvencion previsible o concurso del deudor | Escalar via escalate_to_attorney |
