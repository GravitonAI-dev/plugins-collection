---
name: derecho-civil-herencia
description: >
  Cubre el ciclo completo de la herencia conforme al Codigo Civil (BOE-A-1889-4763) y a la LEC
  (BOE-A-2000-323) en su version consolidada vigente verificada en el BOE: aceptacion de herencia
  (pura y simple o a beneficio de inventario), renuncia (minuta para escritura notarial, Art. 1008 CC),
  interpelacion notarial al heredero que no se pronuncia (Art. 1005 CC, plazo de 30 dias naturales),
  cuaderno particional con inventario, avaluo, liquidacion y adjudicaciones respetando la legitima
  (Arts. 806-808 CC), y solicitud de division judicial de la herencia a falta de acuerdo (Arts. 782 y ss. LEC).
  Advierte del Impuesto de Sucesiones (autonomico, plazo de 6 meses) y de la plusvalia municipal.
  NO usar para redactar testamentos, para tramitar el acta notarial de declaracion de herederos,
  ni para litigios sucesorios contenciosos distintos de la division judicial.
when_to_use: |
  - El usuario quiere documentar la aceptacion de una herencia (pura y simple o a beneficio de inventario).
  - El usuario quiere renunciar a una herencia y necesita la minuta para la escritura notarial.
  - Un heredero no responde y otro interesado quiere requerirle notarialmente para que acepte o repudie (Art. 1005 CC).
  - Hay acuerdo entre todos los herederos y se necesita el cuaderno particional.
  - No hay acuerdo entre los herederos y procede solicitar la division judicial de la herencia (Art. 782 LEC).
inputs:
  - existe_testamento: si / no (sucesion intestada, con o sin acta de declaracion de herederos)
  - actuacion: aceptar / renunciar / interpelar a heredero silente / partir (con o sin acuerdo)
  - modo_aceptacion: pura y simple / a beneficio de inventario
  - datos_causante: nombre, NIF, fecha y lugar de fallecimiento, ultimo domicilio, estado civil y regimen economico
  - titulo_sucesorio: testamento (notario, fecha, protocolo) o acta de declaracion de herederos
  - herederos_o_partes: nombre, NIF, domicilio y condicion de cada interviniente segun la hoja del arbol
  - inventario_bienes_deudas: bienes con su valor, deudas y cargas, donaciones colacionables (hojas de particion)
  - masc: actividad negociadora previa intentada (solo division judicial, LO 1/2025)
  - comunidad_autonoma: para la advertencia del Impuesto de Sucesiones
outputs:
  - aceptacion_herencia: documento de aceptacion (pura y simple o a beneficio de inventario), markdown, DRAFT
  - renuncia_herencia: minuta de renuncia para elevar a escritura notarial, markdown, DRAFT
  - requerimiento_1005: solicitud de interpelacion notarial al heredero silente, markdown, DRAFT
  - cuaderno_particional: cuaderno particional completo, markdown, DRAFT
  - solicitud_division_judicial: solicitud de division judicial de la herencia (Arts. 782 y ss. LEC), markdown, DRAFT
references:
  - references/cc-sucesiones-y-legitima.md
  - references/cc-particion-herencia.md
  - references/cc-aceptacion-renuncia-division.md
  - references/impuesto-sucesiones-y-plazos.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/aceptacion-herencia.md
  - assets/renuncia-herencia.md
  - assets/requerimiento-1005-cc.md
  - assets/cuaderno-particional.md
  - assets/solicitud-division-judicial-herencia.md
---

# Tramitar la Herencia: Aceptacion, Renuncia, Interpelacion y Particion

> DRAFT — para revision por un abogado y, cuando proceda, elevacion a escritura notarial antes de su firma o presentacion. No constituye asesoramiento juridico ni fiscal.

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija que la skill defina y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificacion normativa interna, ejecutala en silencio y continua hasta la primera pregunta o hasta la Confirmacion visible, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

Esta linea es, junto con la introduccion fija, la UNICA excepcion a la prohibicion de mencionar la mecanica interna. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

## Guardrails

1. Verificar siempre el Codigo Civil (y la LEC, si la hoja es judicial) en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Punto 2). No usar una version desactualizada.
3. Respeto absoluto de la legitima (Arts. 806 a 808 CC). No redactar una particion que perjudique la legitima de un heredero forzoso: advertir, recalcular y, si el usuario insiste, escalar.
4. La renuncia es IRREVOCABLE (Art. 997 CC) y solo vale otorgada ante Notario en instrumento publico (Art. 1008 CC). Nunca generar la minuta de renuncia sin haber advertido antes ambas cosas y la fiscalidad del Art. 28 de la Ley 29/1987 (renuncia pura frente a traslativa).
5. Si existen deudas del causante o duda razonable sobre el pasivo, recomendar la aceptacion a beneficio de inventario antes de registrar una aceptacion pura y simple (Arts. 1003 y 1023 CC). No bloquear la eleccion del cliente: advertir, confirmar que lo entiende, y continuar.
6. La particion definitiva con inmuebles suele requerir escritura publica notarial para su inscripcion; el acta de declaracion de herederos abintestato es un tramite notarial previo que esta skill NO tramita. Los documentos generados son borradores de trabajo.
7. Guardar la posible igualdad en los lotes (Art. 1061 CC); los bienes indivisibles se adjudican a un heredero abonando el exceso en dinero (Art. 1062 CC).
8. Nunca omitir la advertencia del Impuesto de Sucesiones y Donaciones (autonomico, plazo de 6 meses, Art. 67 RD 1629/1991) ni de la plusvalia municipal cuando haya inmuebles urbanos.
9. Los datos faltantes conservan el nombre propio del placeholder del asset (p. ej. `{{plaza_notario}}`, `{{numero_protocolo}}`); usa el marcador generico `{{DATO_FALTANTE}}` solo para un hueco suelto dentro de una frase ya redactada que no tenga placeholder propio. Nunca generes dos `{{DATO_FALTANTE}}` en el mismo documento: al repetirse el mismo texto literal, `Edit` ya no puede localizar uno sin el otro por `oldString` unico. Nunca inventar bienes, valores, cuotas, fechas ni protocolos. Nunca afirmar cuotas sin base en el titulo sucesorio. Nunca inventar clausulas testamentarias ni jurisprudencia.
10. En la solicitud de division judicial, no omitir el requisito de procedibilidad MASC (Art. 5 LO 1/2025 y Art. 403.2 LEC): sin intento previo acreditado, advertir del riesgo de inadmision.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la logica descrita en este documento (la clasificacion de vectores V1-V3, las secuencias numeradas, la verificacion normativa y la creacion del documento base) es un flujo de ejecucion ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2").
- Resumenes de validacion con checks (ej. "Testamento: ✔").
- En que fase de la instruccion te encuentras (ej. "Ahora pasaremos al punto 4", "Voy a proceder a crear el documento").
- Preambulos conversacionales antes de las preguntas de clasificacion. Si es tu turno de preguntar, emite unicamente la pregunta exacta y nada mas — con la unica excepcion de la linea de carga del Punto 0, de la introduccion fija del Punto 1, que solo se usa una vez, en el primer turno de toda la conversacion.

## 1. CLASIFICACION DINAMICA (Vectores de Estado)

**Introduccion (solo en el primer turno, una unica vez):** antes de la primera pregunta de este arbol, y solo la primera vez, añade en el mismo mensaje esta introduccion fija, con tono de abogado (usted, formal, sin coloquialismos). No afirmes todavia que documento se generara ni que articulos aplican (dependen de vectores aun no resueltos):

"Vamos a proceder a preparar la documentacion de la herencia. Para ajustarla correctamente a su caso, es necesario precisar antes algunos datos."

No repitas esta introduccion en turnos posteriores.

Tu primer objetivo es resolver estos vectores de manera SILENCIOSA usando Escucha Activa. Si extraes un dato con exito, registralo en tu memoria en silencio.

- **V1 (Titulo sucesorio):** Testada (hay testamento) / Intestada (sin testamento). Si intestada, V1-b: acta de declaracion de herederos abintestato ya otorgada / pendiente.
- **V2 (Actuacion):** Aceptar / Renunciar / Interpelar a un heredero que no se pronuncia (Art. 1005 CC).
- **V2-b (Modo de aceptacion, solo si V2 = Aceptar):** Pura y simple / A beneficio de inventario.
- **V3 (Particion, solo si V2 = Aceptar):** Acuerdo entre todos los herederos / Sin acuerdo / Solo documentar la aceptacion.

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si te falta resolver uno o mas vectores, TIENES PROHIBIDO inventar la redaccion. Formula UNA SOLA PREGUNTA por turno usando EXACTAMENTE este texto, en este orden estricto, sin preambulos ni resumenes de lo que ya sabes. El usuario responde con el numero o con la palabra:

*   **Para V1 (Titulo sucesorio):**
    "El causante:
    1. Otorgo testamento
    2. Fallecio sin testamento"
*   **Para V1-b (solo si V1 = sin testamento):**
    "El acta notarial de declaracion de herederos abintestato:
    1. Ya esta otorgada
    2. Aun no se ha tramitado"
    → Si la respuesta es 2, emite en el mismo turno de la siguiente pregunta esta advertencia fija (visible): "La declaracion de herederos abintestato es un acta notarial que debe tramitarse ante Notario; sin ella no queda acreditado el llamamiento. Puedo preparar la documentacion de partida dejando pendientes los datos del acta, pero el acta misma debera otorgarla el Notario."
*   **Para V2 (Actuacion):**
    "La actuacion que desea documentar es:
    1. Aceptar la herencia
    2. Renunciar a la herencia
    3. Requerir a otro heredero que no se pronuncia sobre la herencia"
*   **Para V2-b (solo si V2 = Aceptar):**
    "La aceptacion sera:
    1. Pura y simple (el heredero responde de las deudas de la herencia tambien con su patrimonio personal, articulo 1003 del Codigo Civil)
    2. A beneficio de inventario (responde solo hasta donde alcancen los bienes de la herencia, articulo 1023 del Codigo Civil)"
    → Regla de dialogo (Guardrail 5): si el cliente ha mencionado deudas del causante o duda sobre el pasivo y elige la opcion 1, antes de registrar el vector adviertale en un turno que la aceptacion pura y simple le hace responder de esas deudas con su propio patrimonio y que el beneficio de inventario limita esa responsabilidad (Arts. 1003 y 1023 CC); pida confirmacion expresa de su eleccion.
*   **Para V3 (solo si V2 = Aceptar):**
    "Respecto del reparto de los bienes entre los herederos:
    1. Hay acuerdo entre todos para partir ahora
    2. No hay acuerdo entre los herederos
    3. Solo desea documentar la aceptacion, sin partir todavia"

*(Si el usuario ya proporciono la respuesta a un vector, OMITE la pregunta correspondiente y evalua el siguiente. Si responde con el numero, interpreta la opcion igual que si hubiera escrito la palabra).*

### Enrutamiento de Estado (Routing)

Una vez resueltos los vectores necesarios, evalua:
- Si [V2 = Renunciar] -> Plantilla: `assets/renuncia-herencia.md`.
- Si [V2 = Interpelar] -> Plantilla: `assets/requerimiento-1005-cc.md`.
- Si [V2 = Aceptar] y [V3 = Acuerdo] -> Plantilla: `assets/cuaderno-particional.md` (incluye la aceptacion de todos los herederos).
- Si [V2 = Aceptar] y [V3 = Sin acuerdo] -> Plantilla: `assets/solicitud-division-judicial-herencia.md`. Si el cliente ademas necesita documentar su propia aceptacion, puede generarse despues un segundo documento con `assets/aceptacion-herencia.md`.
- Si [V2 = Aceptar] y [V3 = Solo aceptacion] -> Plantilla: `assets/aceptacion-herencia.md`.
- V1 no enruta a plantilla: determina los bloques condicionales testada/intestada de todos los assets y, si el acta esta pendiente (V1-b = 2), los datos del titulo sucesorio quedan como `{{DATO_FALTANTE}}`.
- **Regla de no-contaminacion entre hojas:** el bloque opcional "RENUNCIA" de `assets/aceptacion-herencia.md` NO se usa nunca (la renuncia tiene su propio asset): al crear el documento de aceptacion, omite ese bloque completo, incluido su encabezado. En todos los assets, los bloques condicionales de la rama no elegida se omiten sin dejar rastro (regla global de Comment resolution).

---

## 2. VERIFICACION Y AUTO-ACTUALIZACION NORMATIVA BOE (Interno)

Una vez completado el Enrutamiento (Punto 1), no hagas mas preguntas al usuario. La skill se actualiza a si misma en cada lanzamiento. Ejecuta SIEMPRE esta secuencia:

**2.1 — Leer la version registrada localmente.** Abre `references/fuentes-plantillas-validadas.md` y anota la "Version registrada" del Codigo Civil y, si la hoja es la division judicial, tambien la de la LEC y la LO 1/2025.

**2.2 — Consultar la fuente oficial vigente.** Lee, en formato texto, https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y extrae la fecha del texto consolidado vigente y la redaccion actual de los articulos de la hoja enrutada:
- Aceptacion: 988-1004, 1010-1015 y 1023 (si beneficio de inventario).
- Renuncia: 997, 1000, 1008-1009.
- Interpelacion: 1005 y 1003.
- Cuaderno particional: 806-808, 834 y ss., 1035 y ss., 1051-1068.
- Division judicial: 1051-1062; y ademas https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 (arts. 52.1.4, 399.3, 403.2 y 782-789) y https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 (art. 5).

**2.3 — Comparar.** Contrasta la version oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o la redaccion cambio, usa `Write`/`Edit` para actualizar las references afectadas (`cc-sucesiones-y-legitima.md`, `cc-particion-herencia.md`, `cc-aceptacion-renuncia-division.md`) y la tabla de `fuentes-plantillas-validadas.md`, e informa brevemente al usuario (norma y fecha). No redactes ningun documento hasta completar la actualizacion.

**2.5 — Fallback si la fuente no es accesible.** Si la lectura del BOE falla, busca en la web: "Codigo Civil aceptacion repudiacion herencia articulos 997 1005 1008 texto consolidado BOE" (y "LEC division judicial herencia articulos 782 789 texto consolidado BOE" si aplica). Si tambien falla, usa las references locales y notifica: "No se pudo verificar la version vigente en el BOE. Los documentos se generan con la version de referencia. Verificar manualmente antes de firmar."

---

## 3. CONFIRMACION (visible al usuario)

A diferencia de los Puntos 1 y 2, esta seccion es visible para el usuario. Tras completar la verificacion normativa (Punto 2), en un unico mensaje:

**3.1 — Informa la norma aplicable a la hoja enrutada,** con la version vigente verificada y el enlace del BOE consultado en el Punto 2.2. Registro formal (usted), tono de abogado. Ejemplos segun hoja:
- Renuncia: "A la renuncia de la herencia le resultan de aplicacion los articulos 988, 997 y 1008 del Codigo Civil: debe otorgarse ante Notario en instrumento publico y es irrevocable. Puede consultar el texto oficial en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
- Interpelacion: "Al requerimiento le resulta de aplicacion el articulo 1005 del Codigo Civil: el Notario comunicara al heredero que dispone de treinta dias naturales para aceptar o repudiar, y que su silencio supondra la aceptacion pura y simple. Puede consultar el texto oficial en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763"
- Division judicial: citar los articulos 782 y siguientes y 52.1.4 de la Ley 1/2000, de Enjuiciamiento Civil, y el requisito de actividad negociadora previa del articulo 5 de la Ley Organica 1/2025, con ambos enlaces del BOE.
- Aceptacion y cuaderno: citar los articulos del Codigo Civil de la hoja (988 y siguientes; 806-808, 1035 y siguientes, 1051 y siguientes) con el enlace del BOE.

**3.2 — Ofrece la plantilla o pide el documento propio** (alternativas numeradas, decision que cambia el flujo):

"¿Que documento desea utilizar como base?
1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
2. Adjuntar su propio documento"

**3.3 — Enrutamiento segun la respuesta:** si elige la plantilla, continua con el Punto 4 usando el asset de la hoja; si elige adjuntar el suyo, pide que lo adjunte o pegue, leelo con `Read` y usalo como documento base en el Punto 4, sin dejar de aplicar los Guardrails (si el documento adjuntado los incumple — p. ej. una renuncia sin advertencia de irrevocabilidad, una particion que vulnera la legitima —, adviertelo antes de continuar).

---

## 4. CREACION DEL DOCUMENTO BASE (Cero Vacios)

Inmediatamente despues de la Confirmacion (Punto 3), estas OBLIGADO a crear el documento en disco:
1. Utiliza `Read` para leer el documento base decidido en el Punto 3.
2. Reemplaza en memoria las variables de clasificacion (incluidos los bloques testada/intestada segun V1 y el modo de aceptacion segun V2-b) y CUALQUIER OTRO DATO que ya poseas por escucha activa, mas la fecha de verificacion normativa del Punto 2. Resuelve los comentarios condicionales de la rama elegida y omite por completo los de las ramas no elegidas (incluido el bloque RENUNCIA del asset de aceptacion).
3. Utiliza `Write` para guardar el archivo completo en disco. Los datos faltantes conservan el nombre del placeholder del asset (ver Guardrail 9); no los sustituyas todos por el mismo `{{DATO_FALTANTE}}` generico.
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. En esa MISMA respuesta, sin turno intermedio y sin preguntar si desea empezar, emite el anuncio fijo de la primera seccion y formula ya su primera pregunta, para que el flujo no se detenga (regla del `CLAUDE.md` raiz, seccion 6.1, punto 5, y coherencia con el Punto 0: la skill esta en ejecucion desde que se carga).

---

## 5. EDICION INCREMENTAL DE SECCIONES

Recorre secuencialmente las secciones de la hoja enrutada. Por cada seccion incompleta, aplica el Ciclo de Edicion Incremental global (Formular Pregunta -> Vista Previa en texto plano -> Confirmacion -> `Edit` en disco). Estas son preguntas de relleno: prosa natural y respuesta en texto libre, nunca listas numeradas (salvo un dato puntual con respuestas cerradas, que se ofrece en la misma frase). **Un dato por turno**, con esta excepcion:

**Confirmacion agrupada por persona:** los datos puramente identificativos de una misma persona (nombre, NIF, domicilio, y en su caso parentesco o condicion) se preguntan igualmente uno por turno, pero SIN vista previa ni `Edit` tras cada uno: acumulalos en memoria y, al completar el ultimo dato de esa persona, muestra una unica vista previa con todos sus datos juntos, pide una unica confirmacion conjunta y aplica un unico `Edit`. Lo mismo vale para el bloque registral del titulo sucesorio (notario, fecha, protocolo). Esta excepcion NO aplica a las decisiones y pactos (modo de aceptacion, alcance de la renuncia, adjudicaciones, MASC), que se confirman una a una.

**Validacion de sentido, no solo de formato:** no aceptes mecanicamente cualquier respuesta. Si un dato es absurdo, imposible o no responde a lo preguntado (un NIF con forma de nombre, una fecha de fallecimiento futura, un "bien" que no es un bien), no lo escribas: señala por que no encaja y pide aclaracion.

**Dialogo y acuerdo en las decisiones con consecuencias:** las secciones marcadas como (NEGOCIACION) implican una decision con consecuencias legales o fiscales. En ellas no te limites a registrar la respuesta: explica brevemente el regimen legal o la implicacion, y confirma que el cliente lo entiende y esta de acuerdo antes de escribirlo.

**Anuncio de seccion (visible, sin esperar confirmacion aparte):** al terminar una seccion y antes de la primera pregunta de la siguiente, añade en el mismo mensaje el anuncio fijo indicado en cada seccion (tono de abogado, usted). No pidas permiso para pasar de seccion: informa y continua en el mismo turno. El anuncio es de la seccion SUSTANTIVA del documento, nunca de la mecanica interna.

### Secciones comunes a todas las hojas

1. **Causante (dato objetivo — confirmacion agrupada).** Anuncio: "Comenzamos por la identificacion del causante y las circunstancias de su fallecimiento." Sub-apartados, uno por turno: a) nombre completo; b) NIF; c) fecha de fallecimiento; d) lugar de fallecimiento; e) ultimo domicilio. Solo en las hojas de cuaderno particional y division judicial: f) estado civil al fallecer y regimen economico matrimonial (para la liquidacion previa de gananciales).
2. **Titulo sucesorio (dato objetivo registral — confirmacion agrupada del bloque).** Anuncio: "Pasamos a reflejar el titulo sucesorio que fundamenta el llamamiento." Segun V1: a) notario autorizante y su plaza; b) fecha del testamento o del acta; c) numero de protocolo. Si V1-b = acta pendiente, no preguntes: deja `{{DATO_FALTANTE}}` y recuerda la advertencia del acta en la vista previa.

### Hoja: Aceptacion (`aceptacion-herencia.md`)

3. **Heredero aceptante (dato objetivo — confirmacion agrupada).** Anuncio: "Procedemos a la identificacion del heredero aceptante." a) nombre completo; b) NIF; c) domicilio.
4. **Modo de aceptacion e inventario (NEGOCIACION).** Anuncio: "Corresponde ahora dejar constancia del modo de aceptacion." El modo ya esta resuelto (V2-b): NO vuelvas a preguntarlo; refleja el bloque correspondiente. Si es a beneficio de inventario, explica que la declaracion debe hacerse ante Notario (Art. 1011 CC) y que rige el plazo de treinta dias para pedir la formacion de inventario (Arts. 1014-1015 CC), y pide: a) relacion del activo; b) relacion del pasivo.
5. **Otorgamiento (dato objetivo).** Anuncio: "Por ultimo, fijamos el lugar y la fecha de otorgamiento." a) lugar; b) fecha. Pregunta ademas la comunidad autonoma de residencia del causante para la advertencia del Impuesto de Sucesiones (dato puntual, misma seccion).

### Hoja: Renuncia (`renuncia-herencia.md`)

3. **Renunciante (dato objetivo — confirmacion agrupada).** Anuncio: "Procedemos a la identificacion del renunciante." a) nombre completo; b) NIF; c) domicilio.
4. **Alcance de la renuncia (NEGOCIACION — critica).** Anuncio: "Antes de reflejar la renuncia, es necesario que conozca sus efectos." Explica y confirma, en este orden: que la renuncia es irrevocable una vez otorgada (Art. 997 CC); que solo vale ante Notario en instrumento publico (Art. 1008 CC); y la diferencia fiscal (Art. 28 Ley 29/1987): la renuncia pura, simple y gratuita hace tributar a los beneficiarios, mientras que la renuncia a favor de persona determinada implica aceptacion tacita (Art. 1000 CC) y doble tributacion. Confirma que la renuncia es pura, simple y gratuita, y que el renunciante no ha realizado actos de aceptacion tacita. Si el cliente quiere renunciar a favor de persona determinada, advierte que ese acto es civil y fiscalmente una aceptacion con cesion y que esta plantilla no lo cubre; si insiste, escala.
5. **Otorgamiento (dato objetivo).** Anuncio: "Por ultimo, fijamos el lugar y la fecha de otorgamiento." a) lugar; b) fecha; y comunidad autonoma del causante (dato puntual, misma seccion).

### Hoja: Interpelacion del Art. 1005 CC (`requerimiento-1005-cc.md`)

3. **Requirente (dato objetivo — confirmacion agrupada).** Anuncio: "Procedemos a la identificacion del requirente y del interes que acredita." a) nombre completo; b) NIF; c) domicilio; d) interes que acredita (coheredero, legatario, acreedor de la herencia o del llamado — valida que sea un interes real en que el heredero acepte o repudie).
4. **Heredero requerido (dato objetivo — confirmacion agrupada).** Anuncio: "Pasamos a identificar al heredero requerido." a) nombre completo; b) domicilio donde practicar la comunicacion; c) llamamiento que ostenta segun el titulo sucesorio.
5. **Requerimiento (NEGOCIACION).** Anuncio: "Corresponde ahora concretar el requerimiento y sus efectos." Explica el efecto legal antes de confirmar: el Notario comunicara el plazo de treinta dias naturales y, si el requerido calla, la herencia se entendera aceptada PURA Y SIMPLEMENTE (Arts. 1005 y 1003 CC) — lo que puede convenir o no al requirente segun su interes. Pide: a) plaza del Notario al que se dirigira la solicitud; b) consecuencia que la falta de pronunciamiento causa al requirente (para el hecho TERCERO).
6. **Cierre (dato objetivo).** Anuncio: "Por ultimo, fijamos el lugar y la fecha de la solicitud." a) lugar; b) fecha.

### Hoja: Cuaderno particional (`cuaderno-particional.md`)

3. **Herederos (dato objetivo — confirmacion agrupada POR CADA heredero).** Anuncio: "Procedemos a la identificacion de los herederos y demas intervinientes." Por cada heredero, uno por turno: a) nombre completo; b) NIF; c) domicilio; d) parentesco; e) cuota o institucion segun el titulo sucesorio (valida que tenga base en el titulo, Guardrail 9). Confirmacion agrupada al completar cada heredero, luego pasa al siguiente. Pregunta despues si existe conyuge viudo (cuota usufructuaria, Arts. 834 y ss. CC) y si hay contador-partidor designado.
4. **Liquidacion de gananciales (NEGOCIACION, solo si el regimen era gananciales).** Anuncio: "Procede liquidar previamente la sociedad de gananciales." Explica que la mitad de los gananciales corresponde al conyuge viudo y solo la otra mitad mas los privativos integra el caudal; confirma la relacion de bienes gananciales y privativos.
5. **Inventario — activo (dato objetivo con validacion).** Anuncio: "Pasamos a formar el inventario del caudal hereditario, comenzando por el activo." Relacion numerada de bienes con su valor (inmuebles con referencia catastral, cuentas, valores, vehiculos, ajuar), cifras en numero y letra.
6. **Inventario — pasivo (dato objetivo con advertencia).** Anuncio: "Continuamos con el pasivo de la herencia." Deudas, cargas y gastos deducibles. Si el pasivo es relevante y la aceptacion pactada es pura y simple, recuerda la advertencia del Guardrail 5 y la oposicion de acreedores (Arts. 1082-1083 CC).
7. **Colacion (NEGOCIACION).** Anuncio: "Corresponde determinar si existen donaciones colacionables." Explica el Art. 1035 CC (bienes recibidos en vida por herederos forzosos se traen a la masa para el computo) y sus excepciones (Art. 1036); pregunta si existen y, en su caso, su relacion y valor.
8. **Liquidacion y legitimas (calculo interno con confirmacion).** Anuncio: "Con el inventario cerrado, procedemos a la liquidacion del haber y al calculo de cuotas." Calcula: haber liquido = activo + colacionables - pasivo; verifica que la legitima de los herederos forzosos queda cubierta (descendientes: dos tercios, Art. 808 CC; conyuge viudo: usufructo, Arts. 834 y ss.). Si una disposicion es inoficiosa, advierte y propone la reduccion (Guardrail 3). Muestra el calculo en la vista previa y confirma.
9. **Adjudicaciones (NEGOCIACION).** Anuncio: "Por ultimo, procedemos a las adjudicaciones en pago de las cuotas." Explica la igualdad posible de los lotes (Art. 1061 CC) y la compensacion en metalico de los excesos por bienes indivisibles (Art. 1062 CC). Recoge las adjudicaciones heredero por heredero y verifica el cuadre: suma de adjudicaciones = haber liquido partible. Sin cuadre, no confirmes la seccion.
10. **Cierre (dato objetivo).** Anuncio: "Fijamos el lugar y la fecha del otorgamiento." a) lugar; b) fecha; y comunidad autonoma del causante (dato puntual, misma seccion, para la advertencia del ISD).

### Hoja: Division judicial (`solicitud-division-judicial-herencia.md`)

3. **Solicitante (dato objetivo — confirmacion agrupada).** Anuncio: "Procedemos a la identificacion del solicitante." a) nombre completo; b) NIF; c) domicilio; d) condicion en la sucesion (coheredero o legatario de parte alicuota; si es un acreedor, DETEN el proceso: los acreedores no pueden instar la division, Art. 782.3 LEC — advierte y escala).
4. **Procedencia de la via (verificacion, respuestas cerradas).** Anuncio: "Debemos verificar que procede la via judicial." Pregunta si existe comisario o contador-partidor designado por el testador, por acuerdo de los coherederos, por el Letrado de la Administracion de Justicia o por Notario (si/no/no lo sabe). Si existe, DETEN el proceso: la division judicial no procede (Art. 782.1 LEC); advierte y escala.
5. **Demas interesados (dato objetivo — confirmacion agrupada POR CADA interesado).** Anuncio: "Pasamos a identificar a los demas interesados en la herencia." Por cada coheredero, legatario de parte alicuota o conyuge sobreviviente: a) nombre; b) NIF si se conoce; c) domicilio de citacion; d) condicion.
6. **Desacuerdo (dato objetivo con validacion).** Anuncio: "Corresponde dejar constancia del desacuerdo que motiva la solicitud." Descripcion breve y objetiva del desacuerdo (hecho CUARTO), sin valoraciones.
7. **Caudal conocido (dato objetivo).** Anuncio: "Pasamos a relacionar el caudal hereditario conocido." Bienes y derechos identificables y, si se conocen, deudas y cargas.
8. **MASC (NEGOCIACION — requisito de procedibilidad).** Anuncio: "Debemos acreditar la actividad negociadora previa que exige la ley." Explica que la Ley Organica 1/2025 (articulo 5) exige el intento previo de un medio adecuado de solucion de controversias tambien en este procedimiento, y que sin justificante la solicitud puede inadmitirse (articulo 403.2 de la LEC). Pregunta que actividad se intento (tipo y fecha). Si no se intento ninguna, recomienda realizarla antes de presentar (p. ej. requerimiento fehaciente con propuesta de particion, mediacion o conciliacion) y ofrece dejar el hecho SEXTO con `{{DATO_FALTANTE}}` mientras tanto.
9. **Juzgado y postulacion (dato objetivo).** Anuncio: "Determinamos el Juzgado competente y la postulacion procesal." El partido judicial se deriva del ultimo domicilio del causante ya recogido (Art. 52.1.4 LEC): proponlo en la vista previa sin volver a preguntarlo y confirma. Pide: a) nombre del Procurador; b) nombre del Letrado. Si aun no estan designados, quedan como `{{DATO_FALTANTE}}`. Pregunta si desea solicitar la intervencion del caudal y la formacion de inventario (Art. 783.1 LEC, si/no) y, en su caso, el motivo (bloque OTROSI).
10. **Cierre (dato objetivo).** Anuncio: "Por ultimo, fijamos el lugar y la fecha del escrito." a) lugar; b) fecha.

---

## BUCLE DE REALIMENTACION FINAL

Tras completar el Punto 5, muestra el siguiente menu y espera instrucciones (aplicando `Edit` segun corresponda):
1. Ajustar una seccion existente.
2. Añadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

Al cerrar, añade al final estas advertencias (ademas de las propias del asset):
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado y, cuando proceda (renuncia, beneficio de inventario, particion con inmuebles), elevado a escritura publica notarial.
2. Version del Codigo Civil (y de la LEC, si aplica) verificada: fecha extraida en el Punto 2.
3. Impuesto de Sucesiones y Donaciones: tributo autonomico, plazo de 6 meses desde el fallecimiento, prorrogable si se solicita en los 5 primeros meses (Arts. 67 y 68 del RD 1629/1991). Verificar la normativa de la comunidad autonoma con web_search antes de liquidar.
4. Plusvalia municipal (IIVTNU): si hay inmuebles urbanos, liquidar en el ayuntamiento correspondiente, tambien en 6 meses.

## Como NO se usa esta skill

- No usar para redactar testamentos ni codicilos.
- No usar para tramitar el acta notarial de declaracion de herederos abintestato (tramite notarial previo; la skill solo advierte de el y deja los datos pendientes).
- No usar para liquidar el Impuesto de Sucesiones ni la plusvalia municipal: la skill advierte de los plazos, no presenta autoliquidaciones.
- No usar para litigios sucesorios contenciosos distintos de la division judicial (accion de peticion de herencia, impugnacion de testamento o de particion, reduccion de donaciones inoficiosas por via judicial): derivar a `escalate_to_attorney`.
- No usar para herencias sujetas a derecho foral o autonomico especial (Cataluña, Aragon, Navarra, Pais Vasco, Baleares, Galicia) sin verificar antes la normativa civil propia con web_search y advertir al usuario.

## Escalacion

| Situacion | Accion |
|---|---|
| Disposicion o particion que perjudica la legitima de un heredero forzoso | Advertir, recalcular y, si el usuario insiste, escalar via escalate_to_attorney |
| Herederos menores de edad o con discapacidad sin representacion clara | Advertir (defensor judicial, aprobacion del Art. 1060 CC, intervencion del Ministerio Fiscal) y escalar |
| Testamento impugnado, preterision o desheredacion controvertida | Detener y escalar via escalate_to_attorney |
| Herencia con empresa familiar o patrimonio complejo (participaciones societarias, activos en el extranjero) | Advertir de la necesidad de valoracion especializada y escalar |
| Renuncia a favor de persona determinada (traslativa) en la que el cliente insiste | Advertir (Arts. 1000 CC y 28 Ley 29/1987) y escalar |
| Acreedor que pretende instar la division judicial | Detener (Art. 782.3 LEC), advertir de las vias declarativas y escalar |
| Deudas de la herencia superiores al activo (herencia dudosa) | Recomendar aceptacion a beneficio de inventario y ofrecer escalacion |
| Sucesion sujeta a derecho foral o autonomico especial | Advertir, verificar con web_search y escalar si excede el Codigo Civil comun |
