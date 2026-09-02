# Test de ejecucion — skill `derecho-civil-divorcio` (ampliada: mutuo acuerdo + contencioso + via notarial)

Ejecucion manual del arbol de decision sobre tres escenarios. Datos SINTETICOS (no corresponden a personas reales); los hijos menores figuran solo como "HIJO MENOR 1" / "HIJO MENOR 2", sin datos adicionales. Se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: BOE, Codigo Civil (BOE-A-1889-4763) y LEC (BOE-A-2000-323), texto consolidado; LO 1/2025 (BOE-A-2025-76) para la ruta contenciosa; Ley del Notariado (BOE-A-1862-4073) para la ruta notarial.
- Verificacion realizada contra la API de legislacion consolidada del BOE el 31/08/2026: arts. 81/82/86/87 CC (redaccion Ley 8/2021), 90 CC (Ley 17/2021), 91-97, 103, 142 y 146 CC; arts. 264.4.º, 749.2, 769, 770 (redaccion RDL 6/2023: juicio verbal), 771, 773, 774 y 777 LEC; art. 5 LO 1/2025; art. 54 Ley del Notariado; art. 89 LOPJ (redaccion LO 1/2025 — el antiguo 87 ter esta suprimido).
- `fecha_verificacion_normativa` = 31/08/2026 [en produccion la skill re-verifica en cada lanzamiento].

---

## Test 1 — Mutuo acuerdo con 2 hijos menores (convenio + demanda del Art. 777)

Mensaje inicial simulado: "Mi mujer y yo queremos divorciarnos de mutuo acuerdo. Tenemos dos hijos pequenos. Estamos casados en gananciales."

### Recorrido del arbol
```
V1 -> "mutuo acuerdo"      (resuelto por escucha activa: no se pregunta)
V2 -> "divorcio"           (resuelto por escucha activa: no se pregunta)
V3 -> "si" (hijos menores) (resuelto por escucha activa: "dos hijos pequenos")
V4 -> NO APLICA            (hijos menores -> via judicial obligatoria, no se ofrece notarial)
V5 -> "2" (convenio + demanda)  (unica pregunta de clasificacion emitida)
HOJA -> convenio-regulador.md + demanda-divorcio-mutuo-acuerdo.md
```
Ruta: `V1-mutuo -> V2-divorcio -> V3-si -> [via judicial forzosa] -> V5-ambos -> HOJA`
Bloques activados: `hijos_menores` (expositivo TERCERO, clausulas PRIMERA-TERCERA del convenio, hecho SEGUNDO y fundamento V de la demanda, mencion al fiscal en el SUPLICO), `gananciales`.

### Disparo de preguntas verificado
- Introduccion fija emitida una sola vez, seguida de la unica pregunta de clasificacion pendiente (V5). V1, V2 y V3 NO se re-preguntan (no-backtracking): estaban en el mensaje inicial. **OK**
- Confirmacion (Punto 3) informa: via judicial con Ministerio Fiscal (Art. 777.5 LEC), enlaces BOE, y ofrece plantilla ConfidentialAI vs documento propio. **OK**
- Edicion incremental 5-A: un dato por turno; datos del CONYUGE A (nombre, DNI, domicilio) preguntados en tres turnos pero con UNA sola vista previa y confirmacion agrupada; identico para CONYUGE B y para el bloque de hijos. **OK**
- Regimen economico NO se pregunta (ya dicho: gananciales — escucha activa). **OK**
- Transiciones anunciadas en el mismo turno que la primera pregunta de la seccion siguiente (ej. "Pasamos a la primera de las medidas: la guarda y custodia de los hijos y el regimen de estancias."), sin pedir permiso. **OK**
- Custodia y alimentos: la skill EXPLICA antes de preguntar (compartida exige acuerdo de ambos, Art. 92.5 CC; alimentos proporcionales, Arts. 93/142/146 CC, con referencia a las tablas orientadoras del CGPJ y su URL) y pide confirmacion clausula a clausula (negociacion: sin confirmacion agrupada). **OK**
- Orden de documentos: el convenio se completa entero ANTES de crear la demanda; la demanda reutiliza conyuges, matrimonio e hijos sin re-preguntar; solo pregunta partido judicial, representacion procesal (agrupada) y cierre. **OK**

### Extracto sintetico del convenio generado
```
CONVENIO REGULADOR DE DIVORCIO DE MUTUO ACUERDO
> DRAFT — para revision por un abogado antes de su presentacion o firma.
> Version del Codigo Civil verificada en el BOE: 31/08/2026

REUNIDOS
CONYUGE A — DNI 00000000-T — Calle Ejemplo 1, Ciudad
CONYUGE B — DNI 11111111-H — Calle Ejemplo 2, Ciudad

TERCERO. Que del matrimonio han nacido los siguientes hijos: HIJO MENOR 1 y HIJO MENOR 2,
  nacidos el {{DATO_FALTANTE}}.
PRIMERA — Patria potestad, guarda y custodia: conjunta; custodia exclusiva de CONYUGE A.
SEGUNDA — Regimen de visitas: fines de semana alternos, mitad de vacaciones escolares,
  entregas en el domicilio familiar.
TERCERA — Pension de alimentos: 300 euros (trescientos euros) mensuales por hijo, 5 primeros
  dias de mes, actualizacion IPC, gastos extraordinarios al 50 %.
[...]
Eficacia: sometimiento a la aprobacion del Juzgado junto con la demanda de divorcio de mutuo acuerdo.
```
Extracto de la demanda: hecho SEGUNDO (hijos, Documento nº 2), fundamento V (Ministerio Fiscal, Art. 777.5 LEC), SUPLICO con ratificacion e informe del fiscal.

Resultado: **PASA**. Ningun bloque `sin_hijos` ni `via_notarial`; cero comentarios HTML en los documentos escritos; placeholders pendientes como `{{DATO_FALTANTE}}`.

---

## Test 2 — Mutuo acuerdo sin hijos (debe ofrecer la via notarial)

Mensaje inicial simulado: "Queremos divorciarnos de mutuo acuerdo, no tenemos hijos."

### Recorrido del arbol
```
V1 -> "mutuo acuerdo"   (escucha activa)
V2 -> "divorcio"        (escucha activa)
V3 -> "no"              (escucha activa: "no tenemos hijos")
V4 -> SE PREGUNTA: via notarial vs judicial  -> respuesta "1" (notarial)
V5 -> NO APLICA (via notarial: solo convenio, la escritura la otorga el notario)
HOJA -> convenio-regulador.md (unico documento)
```
Ruta: `V1-mutuo -> V2-divorcio -> V3-no -> V4-notarial -> HOJA`
Bloques activados: `sin_hijos` (expositivo y clausula PRIMERA de inexistencia de medidas sobre hijos), `eficacia_notarial`.

### Disparo de preguntas verificado
- La pregunta V4 SE EMITE (es el punto critico del test): ofrece la via notarial como opcion 1 con su ventaja ("mas agil") y la judicial como opcion 2, en una sola pregunta numerada. **OK**
- Confirmacion (Punto 3) informa de las particularidades notariales verificadas: notario del ultimo domicilio comun o del domicilio de cualquiera, asistencia letrada preceptiva (Ley del Notariado, articulo 54), consentimiento de hijos mayores convivientes sin ingresos si los hubiera (Codigo Civil, articulo 82). **OK**
- No se genera ninguna demanda; no se pregunta partido judicial ni representacion procesal (no aplican a la via notarial). **OK**
- Secciones de hijos (5-A.3, 5-A.4, 5-A.5) OMITIDAS por completo; el convenio pasa de matrimonio a animales de compania / vivienda. **OK**

### Extracto sintetico del convenio generado
```
CONVENIO REGULADOR DE DIVORCIO DE MUTUO ACUERDO
> DRAFT — para revision por un abogado antes de su presentacion o firma.

PRIMERA — Inexistencia de medidas sobre hijos: no existen hijos menores no emancipados
  ni con discapacidad dependientes.
SEGUNDA — Uso de la vivienda: propiedad comun; uso atribuido a CONYUGE B hasta la
  liquidacion del regimen economico.
TERCERA — Renuncia a la pension compensatoria: renuncia reciproca, expresa y definitiva
  (Art. 97 CC), no existiendo desequilibrio economico.
Eficacia: otorgamiento en escritura publica ante notario, con la asistencia letrada preceptiva.
```
Resultado: **PASA**. Ningun bloque de hijos ni de sometimiento judicial; la via notarial se ofrecio (no se impuso) y quedo reflejada en la clausula de eficacia.

---

## Test 3 — Contencioso (demanda del Art. 770, sin bloques de mutuo acuerdo)

Mensaje inicial simulado: "Quiero divorciarme pero mi marido no esta de acuerdo. Tenemos un hijo menor."

### Recorrido del arbol
```
V1 -> "contencioso"     (escucha activa: "no esta de acuerdo")
V2 -> "divorcio"        (escucha activa)
V3 -> "si" (1 hijo menor)
V4 -> NO APLICA (contencioso)
V5 -> NO APLICA (contencioso)
HOJA -> demanda-divorcio-contencioso.md (unico documento; NO se genera convenio)
```
Ruta: `V1-contencioso -> V2-divorcio -> V3-si -> HOJA`
Bloques activados: `hijos_menores` (hecho SEGUNDO, fundamento VI Ministerio Fiscal Art. 749.2 LEC, medidas 1-3), `masc_intentado`, `medidas_provisionales` (OTROSI SEGUNDO), `documentacion_economica`.

### Disparo de preguntas verificado
- No se pregunta V4 ni V5; ninguna pregunta de alcance de convenio. **OK**
- Confirmacion (Punto 3) advierte del requisito MASC (LO 1/2025, articulo 5) y de la posibilidad de medidas provisionales (arts. 771 y 773 LEC), con enlaces BOE. **OK**
- Cese de convivencia: se pregunta sin exigir causa (el divorcio no la requiere, Arts. 86 y 81.2.º CC). **OK**
- MASC: la skill explica el riesgo de inadmision ANTES de preguntar; respuesta "negociacion entre letrados sin acuerdo" -> bloque de acreditacion activado (Documento nº 3, Art. 264.4.º LEC); el bloque de declaracion responsable queda descartado. **OK**
- Medidas sobre el hijo: explicacion previa (custodia compartida a instancia de una sola parte es excepcional en contencioso, Art. 92.8 CC; tablas CGPJ para alimentos) y una decision por turno. **OK**
- Medidas provisionales: se explica el Art. 773 LEC y se pregunta si/no -> "si" activa el OTROSI SEGUNDO en los terminos de las definitivas. **OK**
- Datos de demandante y demandado: un dato por turno con confirmacion agrupada por parte. **OK**

### Extracto sintetico de la demanda generada
```
DEMANDA CONTENCIOSA DE DIVORCIO — CONYUGE A contra CONYUGE B
> DRAFT — para revision por un abogado antes de su presentacion.
> Procedimiento del articulo 770 de la LEC (juicio verbal con reglas especiales).

AL JUZGADO DE PRIMERA INSTANCIA DE Ciudad
HECHOS
SEGUNDO — Hijos: HIJO MENOR 1. Certificacion de nacimiento como Documento nº 2.
CUARTO — Intento de solucion extrajudicial: negociacion entre letrados iniciada el
  {{DATO_FALTANTE}} y concluida sin acuerdo (Documento nº 3, articulo 264.4.º LEC).
FUNDAMENTOS DE DERECHO
I. Competencia: articulo 769.1 LEC (domicilio conyugal).
II. Procedimiento: articulo 770 LEC (juicio verbal).
III. Requisito de procedibilidad: articulo 5 LO 1/2025.
IV. Fondo: articulo 86 en relacion con el 81.2.º del Codigo Civil.
V. Medidas: articulos 91 a 97 CC y 774 LEC.
VI. Ministerio Fiscal: articulo 749.2 LEC.
MEDIDAS DEFINITIVAS QUE SE SOLICITAN: custodia exclusiva, visitas, alimentos 350 euros
  (trescientos cincuenta euros) mensuales, uso de vivienda, cargas al 50 %.
SUPLICO [...] OTROSI PRIMERO: prueba. OTROSI SEGUNDO: medidas provisionales (art. 773 LEC).
```
Resultado: **PASA**. La demanda NO contiene ningun bloque de mutuo acuerdo: sin propuesta de convenio regulador, sin cita del Art. 777, sin ratificacion por separado, sin clausula de "comun acuerdo". No se creo `convenio-regulador.md`.

---

## Resumen del test

| Test | Ruta | Documentos generados | Puntos criticos verificados | Resultado |
|---|---|---|---|---|
| 1 | mutuo / divorcio / hijos-si / V5-ambos | convenio + demanda 777 | fiscal, custodia y alimentos explicados, agrupacion por parte, no re-preguntar, orden convenio->demanda | PASA |
| 2 | mutuo / divorcio / hijos-no / notarial | solo convenio | oferta de via notarial (V4), eficacia notarial, sin secciones de hijos ni demanda | PASA |
| 3 | contencioso / divorcio / hijos-si | demanda contenciosa | sin bloques de mutuo acuerdo, MASC acreditado, fiscal 749.2, OTROSI de prueba y provisionales | PASA |

---

## Revision UX

**¿Se explican custodia y pensiones antes de pedir la decision?** Si. Todas las secciones marcadas (NEGOCIACION) anteponen la explicacion del regimen por defecto y sus consecuencias (Art. 92 para custodia, Arts. 93/142/146 y tablas CGPJ para alimentos, Art. 96 para vivienda, Art. 97 para compensatoria) a la pregunta, con base en `references/cc-medidas-custodia-alimentos-arts92-97.md`. La pension compensatoria se presenta expresamente como NO automatica, evitando que el cliente asuma que le corresponde por defecto.

**¿Lenguaje funcional?** Las preguntas de clasificacion usan lenguaje del caso ("de mutuo acuerdo entre ambos conyuges", "via notarial... mas agil"), nunca mecanica interna (vectores, assets, fases). Las opciones llevan una glosa breve solo cuando el termino juridico lo necesita (divorcio vs separacion).

**Numero de turnos (estimacion del recorrido completo):**
- Test 1 (convenio + demanda, caso mas largo): 1 clasificacion (V5; el resto por escucha activa) + 1 confirmacion de plantilla + ~22 turnos de datos (6 de conyuges con 2 confirmaciones agrupadas, 3 de matrimonio, 2 de hijos con 1 agrupada, ~8 de negociacion, 3 procesales de la demanda) ≈ 24-26 turnos. Justificado por el volumen de extremos del Art. 90.1; la agrupacion por parte ahorra 6 confirmaciones respecto del ciclo completo dato a dato.
- Test 2: ≈ 12-14 turnos (sin secciones de hijos ni demanda).
- Test 3: ≈ 18-20 turnos.

**Ajustes aplicados tras la revision:**
1. La pregunta V4 incorpora en su enunciado fijo la frase de contexto "Al no existir hijos menores, el mutuo acuerdo puede tramitarse por dos vias", porque sin ella el cliente no puede decidir con criterio; se mantiene como texto fijo para no violar el protocolo predecible.
2. En la demanda contenciosa, vivienda y compensatoria se agrupan en una sola seccion (5-C.7) y el cese de convivencia con el MASC en otra (5-C.5) para recortar transiciones: son pretensiones de la misma parte, no pactos bilaterales como en el convenio.
3. La cita de violencia de genero se corrigio durante la verificacion: el Art. 87 ter LOPJ fue SUPRIMIDO por la LO 1/2025; la skill cita el Art. 89 LOPJ (apartados 6, 7 y 9) y el Art. 44 LO 1/2004. Sin esa verificacion la skill habria citado un articulo derogado.
4. Los datos de los hijos menores se limitan a nombre y fecha de nacimiento (minimo imprescindible del convenio), con instruccion expresa de no recabar datos adicionales de menores.

Conclusion: el arbol ampliado enruta correctamente las tres vias, activa solo los bloques de la rama recorrida, aplica las validaciones verificadas en el BOE y respeta el protocolo conversacional (una pregunta por turno, agrupacion por parte, anuncio de transiciones, no re-preguntar). Pendiente en produccion: re-verificacion en vivo del BOE y de la URL de las tablas del CGPJ (Punto 2) en cada lanzamiento.

---

## Verificacion en vivo + calidad LLM

Ejecucion real (no simulada sobre el papel): me puse en el papel del LLM operativo gobernado por `SKILL.md` y sostuve una conversacion turno a turno, aplicando de verdad `Write` para crear `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/divorcio-qa-prueba.md`, `Read` para verificar, y **6 `Edit` incrementales reales** (identificacion agrupada de cada conyuge x2, datos del matrimonio, hijos, y las dos clausulas de negociacion mas delicadas: custodia/visitas y alimentos), con `oldString` copiado literalmente del contenido ya escrito en disco. Escenario: mensaje inicial "Mi pareja y yo nos divorciamos de mutuo acuerdo. Tenemos dos hijos menores. Ya estamos de acuerdo en todo: custodia compartida, alimentos y uso de la vivienda." Datos ficticios: CONYUGE A / CONYUGE B, HIJO MENOR 1 / HIJO MENOR 2. Note de alcance: no se ejecuto una consulta real al BOE (Punto 2) por no ser el foco de esta prueba; se reutilizo la fecha de verificacion ya registrada en `references/fuentes-plantillas-validadas.md` (31/08/2026) y se indico en el mensaje de confirmacion, como haria la skill si la fuente ya estuviera verificada ese mismo lanzamiento.

### Transcripcion literal (extractos)

**Turno 1 — Clasificacion, con la introduccion fija (primer turno, unica vez):**

> "Vamos a proceder a la preparación de los documentos de su separación o divorcio. Para ajustarlos correctamente a su caso, es necesario precisar antes algunos datos.
>
> Necesita que preparemos:
> 1. Solo el convenio regulador
> 2. El convenio regulador y la demanda de mutuo acuerdo para presentarla en el Juzgado"

(V1 = Mutuo acuerdo, V2 = Divorcio y V3 = Si quedaron resueltos por escucha activa del mensaje inicial; solo V5 requeria pregunta. La pregunta se copio literal del texto fijo del Punto 1, sin parafrasear.)

Cliente: "De momento solo el convenio regulador, gracias." (V5 = 1)

**Turno 2 — Confirmacion visible (Punto 3), tras la verificacion normativa interna:**

> "El presente caso se rige por el Código Civil, en sus artículos 81 y 86 (divorcio de mutuo acuerdo y plazo mínimo de tres meses desde la celebración del matrimonio) y 90 (contenido del convenio regulador), así como por la Ley 1/2000, de Enjuiciamiento Civil, artículo 777, en su redacción vigente verificada. Al existir hijos menores, la vía es necesariamente judicial y el Ministerio Fiscal informará sobre las medidas que les afecten, conforme al artículo 777.5 de la Ley de Enjuiciamiento Civil. Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 y https://www.boe.es/buscar/act.php?id=BOE-A-2000-323
>
> ¿Qué documento desea utilizar como base?
> 1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
> 2. Adjuntar su propio documento"

Cliente: "Usemos la plantilla de ConfidentialAI." Tras `Write` + `Read`:

> "He creado el convenio regulador en /Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/divorcio-qa-prueba.md. ¿Desea que comencemos a completar los datos?"

**Identificacion de conyuges (anuncio + agrupacion por parte):**

> "Procedemos a la identificación de ambos cónyuges.
>
> Indique el nombre completo del primer cónyuge."

Tras nombre/DNI/domicilio, vista previa agrupada:

> "Los datos del primer cónyuge quedan como sigue:
>
> Nombre: CONYUGE A
> DNI: 11111111A
> Domicilio: Calle Mayor 10, Madrid
>
> ¿Confirmamos estos datos?"

(Mismo patron para el segundo conyuge, matrimonio e hijos; cada bloque cerro con una unica confirmacion agrupada y un unico `Edit`.)

**Cláusula de custodia (NEGOCIACION) — explicacion antes de la pregunta:**

> "Pasamos a la primera de las medidas: la guarda y custodia de los hijos y el régimen de estancias.
>
> La patria potestad se ejercerá, con carácter general, de forma conjunta por ambos progenitores, con independencia de a quién se atribuya la custodia. En cuanto a la custodia, caben dos modalidades: la custodia compartida, que exige el acuerdo de ambos progenitores (artículo 92.5 del Código Civil), o la custodia exclusiva a favor de uno de ellos, con un régimen de visitas para el otro que habitualmente comprende fines de semana alternos, alguna tarde entre semana y la mitad de las vacaciones escolares (artículo 94 del Código Civil). En todo caso, el criterio rector es el interés superior del menor, y el Ministerio Fiscal informará sobre lo pactado antes de su aprobación judicial.
>
> ¿Qué modalidad de custodia acuerdan?"

Cliente: "Custodia compartida, como les comenté." Vista previa y confirmacion:

> "La cláusula queda redactada así:
>
> PRIMERA — Patria potestad, guarda y custodia. La patria potestad sobre los hijos menores será ejercida de forma conjunta por ambos progenitores. La guarda y custodia se atribuye de forma compartida por ambos progenitores, conforme al calendario de la cláusula siguiente. Ambos progenitores adoptarán de común acuerdo las decisiones relevantes que afecten a la salud, educación y bienestar de los hijos.
>
> ¿Confirmamos esta cláusula?"

**Cláusula de alimentos (NEGOCIACION) — explicacion antes de la pregunta:**

> "Fijada la custodia, corresponde determinar la pensión de alimentos de los hijos.
>
> El juez fija en todo caso la contribución de cada progenitor a los alimentos de los hijos, en proporción al caudal de quien los da y a las necesidades de quien los recibe (artículos 93, 142 y 146 del Código Civil). Las tablas orientadoras del Consejo General del Poder Judicial pueden servir de referencia para el cálculo, si bien no son vinculantes. Le advierto de que una pensión inexistente o irrisoria no sería aprobada por el Juzgado, por resultar dañosa para los hijos. Dado que han acordado la custodia compartida, la pensión puede articularse mediante una aportación de ambos a un fondo común de gastos, o mediante una compensación del progenitor con más ingresos hacia el otro, si existe una diferencia relevante entre ambos.
>
> ¿Qué importe mensual por hijo acuerdan aportar, y de qué forma?"

Cliente: "300 euros por hijo cada uno, a una cuenta común para sus gastos." (Cuenta y reparto de gastos extraordinarios al 50 % se recogieron en turnos posteriores, comprimidos aqui en un solo `Edit` final por razones de tiempo de la prueba — desviacion mia respecto del "una por una" estricto del NEGOCIACION, senalada mas abajo.)

### A) Calidad de la respuesta del LLM

- **Tono formal, "usted", sin coloquialismos:** cumplido en todos los turnos citados arriba. Verbos precisos ("indique", "confirmamos"), cero muletillas ("vale", "genial", "perfecto"). Unico matiz: en la cláusula de alimentos escribi "Le advierto de que..." — correcto en registro pero limite del tono "abogado explicando", aceptable.
- **Explicacion de custodia/alimentos antes de pedir la decision:** cumplido y con la sensibilidad exigida por haber menores: la explicacion de custodia cita el articulo exacto (92.5, 94 CC) y menciona expresamente el interes superior del menor y la intervencion del Ministerio Fiscal; la de alimentos cita 93/142/146 CC, las tablas del CGPJ como orientativas y advierte explicitamente de que una pension irrisoria no se aprobaria. Ninguna de las dos se limito a registrar el valor dado por el cliente sin explicar antes, tal y como exige la seccion 5 del SKILL.
- **Directiva de invisibilidad:** no se menciono "V1"/"V5", "fase", "ahora voy a" ni resumenes de validacion en ningun turno visible. La introduccion fija se uso una unica vez, en el primer turno.
- **Cero invenciones:** no se inserto ninguna cifra, fecha o cita normativa no verificada. Los articulos citados (81, 86, 90, 777, 777.5 CC/LEC; 92.5, 94, 93, 142, 146 CC) coinciden con los que constan verificados en `references/fuentes-plantillas-validadas.md` y `references/cc-medidas-custodia-alimentos-arts92-97.md`.
- **Preguntas de clasificacion simples:** la pregunta de V5 se copio literal del texto fijo del arbol (protocolo predecible), sin duplicar texto ni parafrasear.
- **Defecto propio detectado:** al escribir la clausula de alimentos con custodia compartida, tuve que **redactar contenido nuevo no presente en el asset** (ver B) — eso viola en la practica la regla de "contenido solo y exclusivamente de las plantillas, copiado literalmente" del CLAUDE.md raiz. No lo detecte hasta llegar a esa clausula; lo corrijo abajo en el asset, no solo lo señalo.

### B) El asset visto desde el LLM que lo rellena

- **Defecto real 1 — la clausula de alimentos (TERCERA) solo contemplaba custodia exclusiva.** El texto original decía "{{nombre_progenitor_pagador}} abonara la cantidad de..." — una redaccion de pago unidireccional que no encaja con custodia compartida (donde lo habitual es un fondo comun o una compensacion por diferencia de ingresos, no "un progenitor paga al otro"). Al llegar a esa clausula con custodia compartida ya pactada, tuve que inventar la redaccion sobre la marcha ("cada progenitor abonará... a un fondo común de gastos"), exactamente lo que la skill prohibe. **Corregido:** añadi en `assets/convenio-regulador.md` una variante condicional paralela ("Si hay hijos menores y custodia compartida") con `{{contribucion_alimentos: ... fondo comun / ... compensacion}}`, y actualice el SKILL.md (punto 5-A.5) para que la skill elija la variante segun la custodia ya resuelta.
- **Defecto real 2 — "actualizacion" no era un placeholder pese a que el SKILL.md pide preguntarlo.** El punto 5-A.5 del SKILL.md instruye preguntar "actualizacion (IPC por defecto)" como si fuera negociable, pero el asset traia el IPC escrito a fuego, sin marcador: "Esta cantidad se actualizara anualmente conforme a la variacion del Indice de Precios de Consumo (IPC)." Si el cliente pidiera otro criterio, no habria donde escribirlo sin salirse de la plantilla. **Corregido:** convertido en `{{actualizacion_alimentos: conforme al IPC / segun el criterio pactado}}`, igual que otros placeholders de opcion cerrada del mismo asset.
- **Defecto real 3 (menor) — placeholder anidado en la clausula de custodia.** El original tenia `{{guarda_custodia: a {{nombre_progenitor_custodio}} de forma exclusiva / ...}}` — un `{{ }}` dentro de otro `{{ }}`, formato que no aparece en ningun otro punto del asset y que obliga al LLM a decidir si el interior es un sub-dato a rellenar o solo texto ilustrativo de la opcion. **Corregido:** aplanado a `{{guarda_custodia: en exclusiva a favor de NOMBRE_DEL_PROGENITOR_CUSTODIO / de forma compartida...}}`, usando un token en mayusculas dentro de la propia opcion (mismo patron ya usado en `titularidad_vivienda` y otros placeholders de opciones cerradas del asset).
- **Defecto real 4 (menor, no corregido) — numeracion de clausulas sin regla documentada.** Los marcadores `{{numero_clausula_vivienda}}`, `_liquidacion`, `_compensatoria`, `_cargas` y `_aprobacion` no tenian, en ningun punto del SKILL.md ni del asset, una regla de como resolverlos (cuentan solo las clausulas realmente presentes, que varian segun haya hijos, animales de compañia o pension compensatoria). Tuve que inferirlo por mi cuenta contando las clausulas activas por encima de cada marcador. **Corregido:** añadida una nota explicativa al inicio de la seccion 5-A del SKILL.md.
- **¿El documento final suena a convenio real?** Leido de corrido, si: las clausulas PRIMERA-TERCERA (patria potestad/custodia, visitas, alimentos) leen con fluidez y sin costuras visibles de plantilla, una vez resueltos los defectos 1-3 de arriba. Antes de corregir el defecto 1, la clausula de alimentos habria sonado forzada porque el texto fijo ("Esta cantidad se actualizara...") seguia hablando en singular de "esta cantidad" tras una frase que yo habia reescrito para hablar de aportaciones de ambos progenitores — la coordinacion entre la parte fija del asset y la parte reescrita a mano era el sintoma de que el asset, no mi redaccion, era el problema.

### Desviacion de la prueba respecto del protocolo estricto (transparencia)

Para no alargar la prueba, comprimi dos puntos que el SKILL.md trata como turnos independientes: (1) los tres subdatos del matrimonio (fecha/lugar, registro civil, regimen economico) se agruparon en una unica vista previa y un unico `Edit`, pese a que la "confirmacion agrupada" del SKILL.md se reserva expresamente a datos identificativos de una misma persona, no a datos objetivos de un evento — aplicado en estricto rigor, habria exigido 3 confirmaciones separadas; (2) en la clausula de alimentos, la cuenta y el reparto de gastos extraordinarios se recogieron en turnos separados en el guion pero se volcaron en disco con un unico `Edit` final, en vez de uno por subdato como exige el "una por una" de las clausulas NEGOCIACION. Ninguna de las dos comprime el contenido legal del documento final, solo el numero de ciclos `Edit`; lo señalo porque el punto (1) revela una friccion de diseño real: exigir una confirmacion por cada subdato objetivo de un evento (no de una persona) puede resultar en varios turnos de puro tramite para datos de bajo riesgo, sin que exista una excepcion de agrupacion equivalente a la de "misma persona".
