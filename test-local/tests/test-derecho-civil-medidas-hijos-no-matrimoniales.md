# Test de ejecucion — skill `derecho-civil-medidas-hijos-no-matrimoniales`

Ejecucion manual del arbol de decision sobre tres escenarios mas un contra-caso. Datos SINTETICOS (no corresponden a personas reales); de los menores figuran unicamente "HIJO MENOR 1" y una fecha de nacimiento ficticia, sin ningun dato adicional. Se usan solo para verificar el enrutamiento, la activacion de bloques condicionales y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: BOE, Codigo Civil (BOE-A-1889-4763) y LEC (BOE-A-2000-323), texto consolidado; LO 1/2025 (BOE-A-2025-76) para el requisito de MASC; LOPJ (BOE-A-1985-12666) y LO 1/2004 (BOE-A-2004-21760) para el guardrail de violencia.
- Verificacion realizada contra la API de legislacion consolidada del BOE el **02/09/2026**, bloque a bloque, tomando la ULTIMA `<version>` de cada bloque: CC arts. 92 (LO 10/2022), 93, 94 y 96 (Ley 8/2021), 142, 143, 146, 148, 152, 154 (LO 8/2021) y 156 (Ley 8/2021); LEC arts. 748, 749, 769, 770 (RDL 6/2023: juicio verbal), 777 y 264; art. 5 LO 1/2025; art. 89 LOPJ (redaccion LO 1/2025). Verificado tambien que el bloque `civ-12` de la LEC devuelve el rotulo "De los procesos matrimoniales y de menores" y que el art. 87 ter LOPJ consta literalmente "(Suprimido)".
- Herramienta del CGPJ: la URL responde HTTP 200, pero el apartado consta "en proceso de revision y actualizacion" y "No hay informacion disponible". **La skill debe advertirlo al citarla**, no remitir al cliente a una calculadora que no esta operativa.
- `fecha_verificacion_normativa` = 02/09/2026 [en produccion la skill re-verifica en cada lanzamiento].
- Puntos registrados como pendientes de verificacion manual y tratados como tales en los tres escenarios: aplicacion de los arts. 770 y 777 LEC a los procesos no matrimoniales (cauce por ubicacion sistematica y practica forense, no por remision expresa) y del art. 96 CC a la vivienda (criterio analogico).

---

## Test 1 — Pareja de hecho con acuerdo total y un hijo de 5 anos (pacto + demanda conjunta)

Mensaje inicial simulado: "Mi pareja y yo nos hemos separado. No estamos casados, eramos pareja de hecho inscrita. Tenemos un hijo de cinco anos y estamos de acuerdo en todo: la custodia, las visitas y la pension."

### Recorrido del arbol
```
V2 (filiacion) -> SE PREGUNTA (primera pregunta del arbol) -> respuesta "1" (ambos inscritos)
V1 (acuerdo)   -> "existe acuerdo"   (resuelto por escucha activa: "estamos de acuerdo en todo")
V3 (medidas)   -> "1" conjunto completo (escucha activa: custodia, visitas y pension)
V3-bis (vivienda) -> SE PREGUNTA -> respuesta "2" (no procede pronunciarse)
V4 (convivencia)  -> "1" pareja inscrita (escucha activa: "pareja de hecho inscrita")
V5 (alcance)      -> SE PREGUNTA -> respuesta "2" (pacto + demanda conjunta)
HOJA -> ACUERDO: pacto-relaciones-familiares.md + demanda-medidas-paternofiliales.md (variante de acuerdo)
```
Ruta: `V2-determinada -> V1-acuerdo -> V3-completo -> V3bis-no -> V4-inscrita -> V5-ambos -> HOJA ACUERDO`

**Bloques ACTIVADOS:** expositivo TERCERO variante "pareja inscrita en un registro" (pacto) y su equivalente en el hecho SEGUNDO con **Documento nº 2** (demanda); pactos de patria potestad, custodia, estancias y alimentos; variante de alimentos de **custodia exclusiva** (pago unidireccional); pacto de sometimiento a aprobacion judicial; en la demanda, titulo y comparecencia conjuntos, hecho CUARTO "Pacto de relaciones familiares alcanzado" con `{{numero_documento_pacto}}` = 3, fundamento del art. 777.5 LEC sobre el informe del fiscal, y SUPLICO de aprobacion del pacto.

**Bloques NO activados (verificado uno a uno):** variantes de convivencia sin inscripcion y de ausencia de convivencia; pacto de vivienda (`{{numero_pacto_vivienda}}` no llega a escribirse); en la demanda, hecho CUARTO de MASC, hecho de situacion economica, apartado "MEDIDAS QUE SE SOLICITAN" completo, OTROSI PRIMERO de prueba, OTROSI SEGUNDO de medidas provisionales, fundamento III de requisito de procedibilidad, fundamento de vivienda por analogia del art. 96, advertencias 6/7/8 de la variante contenciosa.

### Numeracion dinamica resuelta
- Pacto: patria potestad = PRIMERO, custodia = SEGUNDO, estancias = TERCERO, alimentos = CUARTO, sometimiento = QUINTO. Sin vivienda, no queda hueco ni salto.
- Demanda: hechos PRIMERO a CUARTO; fundamentos I Competencia, II Procedimiento, **III Fondo** (sin fundamento de procedibilidad, propio del contencioso), IV Interes superior, V Ministerio Fiscal, VI Audiencia, VII Costas. Documentos: nº 1 certificaciones de nacimiento, nº 2 certificacion del registro de parejas, nº 3 pacto firmado. Advertencia de violencia = nº 7.

### Disparo de preguntas verificado
- **La filiacion se pregunta PRIMERO**, antes de cualquier otro dato, y con texto fijo. **OK**
- Introduccion fija emitida una sola vez, en el mismo mensaje que esa primera pregunta, sin afirmar todavia via ni norma aplicable. **OK**
- V1, V3 y V4 NO se re-preguntan (no-backtracking): estaban en el mensaje inicial. Se emiten solo V2, V3-bis y V5: tres preguntas de clasificacion. **OK**
- Confirmacion (Punto 3) con el texto fijo de la HOJA ACUERDO: cita arts. 154, 156, 92, 93, 94, 142, 146 y 148 CC, el art. 748.4.º LEC y el cauce del 777, informa de la intervencion preceptiva del **Ministerio Fiscal por existir menores (art. 749.2 LEC)**, advierte de que el pacto no queda aprobado por firmarse, y anade el parrafo fijo de que la ausencia de matrimonio no altera los derechos del hijo pero excluye regimen economico y compensatoria. Enlaces al BOE incluidos. **OK**
- Edicion incremental 5-A: un dato por turno; los tres datos de PROGENITOR A (nombre, DNI, domicilio) preguntados en tres turnos con UNA sola vista previa y confirmacion agrupada, emitida **en el turno siguiente** a la respuesta del ultimo dato; identico para PROGENITOR B y para el bloque del hijo. **OK**
- Del menor solo se piden nombre y fecha de nacimiento. Cuando el cliente ofrece espontaneamente el colegio, **no se incorpora al documento**. **OK**
- Patria potestad explicada antes de preguntar, con la distincion respecto de la custodia, el art. 154.3.º sobre el cambio de residencia y el matiz del parrafo final del art. 156 CC (viviendo separados, conviene pactar el ejercicio conjunto expresamente). **OK**
- Alimentos: se cita la referencia del CGPJ **con la advertencia de que el apartado consta en revision**, y se advierte de que una pension irrisoria no seria aprobada. Cuatro sub-apartados en turnos separados, confirmacion una por una (sin agrupacion, por ser negociacion). **OK**
- Orden de documentos: el pacto se completa entero ANTES de crear la demanda; la demanda reutiliza progenitores, hijo, convivencia y fecha/lugar del pacto sin re-preguntar, y solo pregunta juzgado competente, situacion actual del hijo, representacion procesal (agrupada) y cierre. **OK**

### Extracto sintetico del pacto generado
```
PACTO DE RELACIONES FAMILIARES
> DRAFT — para revision por un abogado colegiado antes de su firma.
> Version del Codigo Civil y de la LEC verificada en el BOE: 02/09/2026

REUNIDOS
PROGENITOR A — DNI 00000000-T — Calle Ejemplo 1, Ciudad
PROGENITOR B — DNI 11111111-H — Calle Ejemplo 2, Ciudad

PRIMERO. Progenitores de HIJO MENOR 1, nacido el 14/03/2021, con filiacion determinada
  respecto de ambos e inscrita en el Registro Civil.
SEGUNDO. Los otorgantes no estan ni han estado unidos por vinculo matrimonial.
TERCERO. Convivencia inscrita en el Registro de Parejas de Hecho de la Comunidad de Ejemplo
  el 02/05/2019, cesada el 15/06/2026.

PRIMERO — Patria potestad: ejercicio conjunto; requieren acuerdo de ambos el cambio de
  residencia habitual (art. 154.3.º CC), centro escolar, tratamientos no urgentes, formacion
  religiosa, viajes al extranjero y documentacion. Desacuerdos: art. 156 CC.
SEGUNDO — Guarda y custodia: exclusiva a favor de PROGENITOR A.
TERCERO — Estancias: fines de semana alternos de viernes a las 18:00 a domingo a las 20:00,
  martes y jueves de 17:00 a 20:00, mitad de vacaciones escolares (primera mitad para
  PROGENITOR B en anos pares). Entregas en el centro escolar.
CUARTO — Alimentos: 250 euros (doscientos cincuenta euros) mensuales por hijo, 5 primeros
  dias de mes, cuenta ES00 0000 0000 0000 0000 0000, actualizacion anual conforme al IPC;
  gastos extraordinarios al 50 %, con comunicacion, justificacion y acuerdo previo si no
  son urgentes.
QUINTO — Sometimiento a la aprobacion del Juzgado competente (art. 769.3 LEC), con
  intervencion preceptiva del Ministerio Fiscal (art. 749.2 LEC).
```
Extracto de la demanda conjunta: titulo "DEMANDA CONJUNTA DE MEDIDAS PATERNOFILIALES DE MUTUO ACUERDO", hecho CUARTO con el pacto como Documento nº 3, fundamento II por el cauce del art. 777 LEC, fundamento V con el informe del fiscal del art. 777.5, y SUPLICO de citacion para ratificacion y aprobacion por sentencia.

Resultado: **PASA**. Cero comentarios HTML en los documentos escritos; ningun bloque contencioso; ninguna clausula de contenido matrimonial (sin liquidacion de regimen ni compensatoria); numeracion continua sin saltos.

---

## Test 2 — Sin acuerdo: se piden custodia exclusiva y alimentos (demanda contenciosa con MASC)

Mensaje inicial simulado: "El padre de mi hija y yo nunca nos casamos y ahora no nos ponemos de acuerdo en nada. Quiero pedir la custodia de la nina y que pague una pension."

### Recorrido del arbol
```
V2 (filiacion) -> SE PREGUNTA -> respuesta "1" (ambos inscritos)
V1 (acuerdo)   -> "no existe acuerdo"  (escucha activa: "no nos ponemos de acuerdo en nada")
V3 (medidas)   -> "1" conjunto completo (escucha activa: custodia + pension)
V3-bis (vivienda) -> SE PREGUNTA -> respuesta "2"
V4 (convivencia)  -> SE PREGUNTA -> respuesta "2" (convivencia sin inscripcion)
V5 (alcance)      -> NO APLICA (no hay acuerdo)
HOJA -> CONTENCIOSA: demanda-medidas-paternofiliales.md (variante contenciosa)
```
Ruta: `V2-determinada -> V1-sin acuerdo -> V3-completo -> V3bis-no -> V4-sin inscripcion -> HOJA CONTENCIOSA`

**Bloques ACTIVADOS:** titulo y comparecencia contenciosos ("A contra B"); hecho SEGUNDO variante "convivencia sin inscripcion registral"; hecho CUARTO de intento de MASC con la sub-variante de **MASC intentado** y `{{numero_documento_masc}}` = 2; hecho de situacion economica con `{{numero_documento_economicos}}` = 3; hecho de medidas cuya adopcion se interesa; fundamento III de requisito de procedibilidad; fundamento de Ministerio Fiscal con la variante del informe previo del art. 92.6 CC; fundamento de audiencia con la regla 4.ª del art. 770 LEC; medidas 1 a 4 (patria potestad, custodia, estancias, alimentos); OTROSI PRIMERO de prueba; OTROSI SEGUNDO de medidas provisionales; advertencias 6, 7 y 8.

**Bloques NO activados (verificado uno a uno):** todos los de la variante de acuerdo (titulo conjunto, comparecencia conjunta, hecho CUARTO del pacto, fundamento del art. 777, SUPLICO de aprobacion, advertencia 6 de la variante de acuerdo); sub-variante de **declaracion responsable** del art. 264.4.º (descartada al haberse intentado el MASC); variantes de convivencia inscrita y de ausencia de convivencia, y con ellas el Documento nº 2 del registro de parejas; medida de vivienda y fundamento de vivienda por analogia del art. 96 CC. **No se creo ningun pacto de relaciones familiares.**

### Numeracion dinamica resuelta
Hechos: PRIMERO Filiacion, SEGUNDO Convivencia y cese, TERCERO Situacion actual, CUARTO MASC, **QUINTO Situacion economica**, **SEXTO Medidas**. Fundamentos: I Competencia, II Procedimiento, III Requisito de procedibilidad, **IV Fondo**, V Interes superior, VI Ministerio Fiscal, VII Audiencia, VIII Costas. Documentos: nº 1 certificacion de nacimiento, nº 2 acreditacion del MASC, nº 3 documentacion economica. Medidas: 1 patria potestad, 2 custodia, 3 estancias, 4 alimentos. Advertencia de violencia = nº 9.

### Disparo de preguntas verificado
- La filiacion se pregunta primero, tambien aqui. Solo tres preguntas de clasificacion (V2, V3-bis, V4): V1 y V3 vinieron por escucha activa. **OK**
- Confirmacion (Punto 3) con el texto fijo de la HOJA CONTENCIOSA: art. 748.4.º LEC, tramites del **juicio verbal** del art. 770 (no juicio ordinario: la redaccion vigente es la del RDL 6/2023), competencia del art. 769.3, fiscal preceptivo del art. 749.2, y advertencia del requisito de MASC con riesgo de inadmision. Tres enlaces al BOE. **OK**
- MASC: la skill explica el requisito ANTES de preguntar, aclara que basta la negociacion entre abogados y que debe haber identidad de objeto; respuesta "negociacion entre letrados sin acuerdo" → activa el bloque de acreditacion documental y descarta el de declaracion responsable. **OK**
- **Riesgo de reconvencion (seccion 5-C.5): se advierte ANTES de concretar las medidas**, citando la regla 2.ª, letra d), del art. 770 LEC y los 10 dias para contestarla. El cliente responde que cree que el padre pedira custodia compartida; la skill lo registra y mantiene la peticion de custodia exclusiva, ya incluida en V3. **OK**
- Custodia compartida: al explicar la seccion 5-C.8, la skill advierte de que **a instancia de una sola parte es excepcional (art. 92.8 CC)** y exige informe del fiscal, sin prometer resultado. **OK**
- Alimentos: se anade la explicacion del **art. 148 CC** (no se abonan sino desde la interposicion de la demanda; retrasarla tiene coste economico) y se rechaza la peticion del cliente de reclamar los ocho meses anteriores, explicando por que no procede por esta via. **OK**
- Hija nacida el 20/01/2013: la skill **calcula por su cuenta** que ha cumplido doce anos e informa de que sera oida en todo caso (regla 4.ª del art. 770 LEC), sin que el cliente lo pregunte. **OK**
- Documentacion economica: se explica que la regla 1.ª del art. 770 LEC obliga a **ambas** partes a aportarla, no solo al demandante. **OK**
- Medidas provisionales: se explican en los terminos verificados (cauce de los arts. 771 y 773 LEC aplicado por analogia, no por remision expresa) y se pregunta si/no → "si" activa el OTROSI SEGUNDO. **OK**
- Validacion de sentido: el cliente propone "una pension de lo que el pueda, ya veremos"; la skill NO lo escribe, explica que una medida sin importe no es ejecutable y pide una cifra concreta. **OK**

### Extracto sintetico de la demanda generada
```
DEMANDA DE MEDIDAS PATERNOFILIALES — PROGENITOR A contra PROGENITOR B
> DRAFT — para revision por un abogado colegiado antes de su firma.
> Proceso del articulo 748.4.º LEC. Tramites del juicio verbal, articulo 770 LEC.

AL JUZGADO DE PRIMERA INSTANCIA DE Ciudad
HECHOS
PRIMERO — Filiacion: HIJO MENOR 1, nacida el 20/01/2013. Certificacion literal de
  nacimiento como Documento nº 1.
SEGUNDO — Sin vinculo matrimonial; convivencia sin inscripcion desde 2011 hasta su cese
  el 10/02/2026. No hay regimen economico matrimonial que liquidar ni cabe compensatoria.
TERCERO — Situacion actual: la hija convive con PROGENITOR A desde el cese.
CUARTO — Intento de MASC: negociacion entre letrados, iniciada el 03/04/2026 y concluida
  sin acuerdo el 20/05/2026 (Documento nº 2, articulo 264.4.º LEC).
QUINTO — Situacion economica: nominas y declaracion de la renta (Documento nº 3).
SEXTO — Medidas cuya adopcion se interesa.
FUNDAMENTOS DE DERECHO
I. Competencia: articulo 769.3 LEC (ultimo domicilio comun de los progenitores).
II. Procedimiento: articulos 748.4.º y 770 LEC (juicio verbal).
III. Requisito de procedibilidad: articulo 5.2 LO 1/2025 y articulo 264.4.º LEC.
IV. Fondo: articulos 154, 156, 92, 93, 94, 142, 146 y 148 CC.
V. Interes superior de los hijos: articulo 92.2 CC.
VI. Ministerio Fiscal: articulo 749.2 LEC; informe previo del articulo 92.6 CC.
VII. Audiencia de los hijos: articulo 154 CC y regla 4.ª del articulo 770 LEC.
VIII. Costas.
MEDIDAS QUE SE SOLICITAN: 1 patria potestad conjunta; 2 custodia exclusiva de
  PROGENITOR A; 3 estancias de fines de semana alternos y mitad de vacaciones;
  4 alimentos de 300 euros (trescientos euros) mensuales, devengo desde la interposicion
  de la demanda (articulo 148 CC), actualizacion IPC, extraordinarios al 50 %.
SUPLICO [...] OTROSI PRIMERO: prueba (interrogatorio, documental y pericial psicosocial).
OTROSI SEGUNDO: medidas provisionales.
```
Resultado: **PASA**. La demanda no contiene ningun bloque de mutuo acuerdo: sin propuesta de pacto, sin cita del art. 777, sin ratificacion por separado, sin SUPLICO de aprobacion. Ningun rastro de terminologia matrimonial ("conyuges", "convenio regulador", "cargas del matrimonio").

---

## Test 3 — Vivienda propiedad exclusiva de un progenitor y custodia del otro (punto de discusion de la vivienda)

Mensaje inicial simulado: "Nunca estuvimos casados y nos hemos separado de buenas. Tenemos un hijo de 3 anos. Nos hemos puesto de acuerdo en todo, y quiero que quede claro que yo me quedo viviendo en el piso con el nino, aunque el piso esta a nombre de el solo. Entiendo que me corresponde por tener la custodia."

Este es el escenario critico del test: **el cliente llega con una expectativa juridicamente incorrecta** (cree que la vivienda le corresponde automaticamente por tener la custodia, por analogia con lo que ha oido de los divorcios). La skill debe corregirla antes de escribir nada.

### Recorrido del arbol
```
V2 (filiacion) -> SE PREGUNTA -> respuesta "1"
V1 (acuerdo)   -> "existe acuerdo"  (escucha activa: "nos hemos puesto de acuerdo en todo")
V3 (medidas)   -> SE PREGUNTA -> respuesta "1" (conjunto completo)
V3-bis (vivienda) -> "1" se solicita el uso  (escucha activa: "yo me quedo viviendo en el piso")
V4 (convivencia)  -> SE PREGUNTA -> respuesta "2" (convivencia sin inscripcion)
V5 (alcance)      -> SE PREGUNTA -> respuesta "1" (solo el pacto)
HOJA -> ACUERDO: pacto-relaciones-familiares.md (unico documento)
```
Ruta: `V2-determinada -> V1-acuerdo -> V3-completo -> V3bis-si -> V4-sin inscripcion -> V5-solo pacto -> HOJA ACUERDO`

**Bloques ACTIVADOS:** expositivo TERCERO variante "convivencia sin inscripcion"; pactos de patria potestad, custodia, estancias y alimentos (variante de custodia exclusiva); **pacto de uso de la vivienda**; pacto de sometimiento a aprobacion judicial.

**Bloques NO activados:** variantes de convivencia inscrita y de ausencia de convivencia; variante de alimentos para custodia compartida; **todo el asset de la demanda** (V5 = 1: no se crea ningun documento judicial).

### Numeracion dinamica resuelta
Patria potestad = PRIMERO, custodia = SEGUNDO, estancias = TERCERO, alimentos = CUARTO, **vivienda = QUINTO**, sometimiento = SEXTO. Contraste con el Test 1, donde el sometimiento fue QUINTO al no existir pacto de vivienda: el marcador `{{numero_pacto_sometimiento}}` se resuelve correctamente en ambos casos y no queda ningun ordinal repetido ni salto.

### Disparo de preguntas verificado
- La expectativa del cliente sobre la vivienda aparece en el mensaje inicial, pero la skill **no la corrige ahi**: resuelve V3-bis por escucha activa y deja la explicacion para su seccion, respetando el orden del flujo y la prohibicion de preambulos. **OK**
- Al abrir la seccion de vivienda (5-A.8), la skill emite el anuncio fijo y **explica antes de preguntar, con detalle**: (a) que aqui no hay regimen economico matrimonial que liquidar; (b) que el art. 96 CC, que en los divorcios atribuye el uso al progenitor custodio, esta redactado para los conyuges y para los supuestos de nulidad, separacion y divorcio, y **no se aplica de forma directa**; (c) que sin matrimonio la vivienda se rige por las reglas ordinarias de la propiedad, de modo que si es privativa de un progenitor, es suya; (d) que lo que si opera es el interes del menor, cuya necesidad de habitacion forma parte de los alimentos (art. 142 CC), y por esa via se invoca el criterio del art. 96.1 **por analogia**. **OK — la expectativa incorrecta queda corregida antes de escribir cualquier clausula.**
- Al constar que la vivienda es **propiedad exclusiva del otro progenitor**, la skill aplica la fila correspondiente de la tabla de Escalacion: advierte de que la atribucion del uso es una limitacion de la facultad dispositiva del titular y de resultado incierto, **ofrece escalacion a un especialista antes de redactar la medida**, y pone sobre la mesa las cuatro alternativas de la reference: plazo cerrado en lugar de indefinido, compensacion economica al titular, cuantificar la habitacion dentro de la pension, o venta o extincion del condominio si el inmueble fuera comun. **OK**
- Resultado de la negociacion en la prueba: el cliente declina la escalacion y opta por un **plazo cerrado de tres anos** con reparto de gastos. La skill lo escribe con la titularidad real consignada, sin afirmar en ningun punto que el uso corresponda por tener la custodia. **OK**
- Ninguna seccion pregunta por liquidacion de bienes ni por pension compensatoria. Cuando el cliente pregunta de pasada "y una compensacion para mi por los anos que deje de trabajar?", la skill **rechaza la instruccion**, explica que el art. 97 CC es privativo del matrimonio y no cabe en este procedimiento, y ofrece escalacion; **no lo escribe en el pacto**. **OK**

### Extracto sintetico del pacto generado
```
QUINTO — Uso de la vivienda en que residen los hijos.
La vivienda en que residen los hijos comunes, sita en Calle Ejemplo 3, Ciudad, es propiedad
privativa de PROGENITOR B, segun escritura publica de compraventa anterior al inicio de la
convivencia. No existiendo entre los otorgantes vinculo matrimonial ni, por tanto, regimen
economico matrimonial que liquidar, la atribucion del uso de la vivienda se acuerda
atendiendo a la titularidad del inmueble y al interes de los hijos comunes en los
siguientes terminos: su uso se atribuye a PROGENITOR A y al hijo menor que queda en su
compania, por un plazo de tres anos a contar desde la firma de este pacto, transcurrido
el cual cesara sin necesidad de requerimiento. Los gastos derivados de la vivienda se
asumiran conforme a lo siguiente: PROGENITOR A abonara los suministros y la comunidad
ordinaria; PROGENITOR B, el impuesto sobre bienes inmuebles y las derramas
extraordinarias.
```
Resultado: **PASA**. La clausula consigna la titularidad real, no invoca el art. 96 CC como regla automatica, fija un plazo cerrado y no contiene ninguna institucion matrimonial. La escalacion se ofrecio antes de redactar.

---

## Contra-caso — El otro progenitor no ha reconocido al hijo (debe DETENER por filiacion)

Mensaje inicial simulado: "Quiero que el padre de mi hijo pague una pension. Nunca lo reconocio, no aparece en el libro de familia, y ademas necesito que se fije un regimen de visitas y que se decida sobre el piso."

### Recorrido del arbol
```
V2 (filiacion) -> SE PREGUNTA (primera y UNICA pregunta emitida) -> respuesta "2"
                  (el otro progenitor no lo ha reconocido)
V1, V3, V3-bis, V4, V5 -> NO SE PREGUNTAN NUNCA
HOJA -> NINGUNA. No se crea documento alguno.
```

### Comportamiento verificado
- La primera y unica pregunta emitida es la de la filiacion. **La skill no pregunta por el acuerdo, ni por las medidas, ni por la vivienda, ni por la convivencia**, pese a que el mensaje inicial menciona pension, visitas y piso: eran datos suficientes para resolver V1 y V3 por escucha activa, pero el enrutamiento evalua V2 **antes** que cualquier otro vector y detiene el flujo. **OK — este es el punto critico del contra-caso.**
- Se emite el texto fijo del Guardrail 1, explicando que sin filiacion determinada no existe patria potestad del otro progenitor, ni deber de alimentos exigible frente a el, ni parte contra la que dirigir las medidas, y que el procedimiento previo y necesario es el de determinacion de la filiacion. **OK**
- Se ofrece escalacion a un especialista y **no se ejecuta ningun `Write`**: no se crea archivo, ni vacio ni parcial. **OK**
- La skill no ofrece un "documento provisional" ni una demanda con la filiacion como placeholder pendiente: eso habria sido el fallo tipico. **OK**
- Variante probada de la sub-pregunta: repetido el contra-caso con respuesta "3" (no lo se) a la primera pregunta, la skill emite la sub-pregunta de desambiguacion con su texto fijo (comprobacion en la certificacion literal de nacimiento). Respuesta "3" (no dispongo del documento) → **DETIENE igualmente**, sin dar por determinada una filiacion no acreditada. **OK**

### Extracto de la respuesta emitida
```
Antes de poder fijar cualquier medida es necesario que la filiacion de su hijo conste
determinada respecto de ambos progenitores. Mientras no lo este, no existe patria potestad
del otro progenitor, ni deber de alimentos exigible frente a el, ni parte contra la que
dirigir estas medidas: el procedimiento previo y necesario es el de determinacion de la
filiacion, que es distinto de este y que le corresponde llevar a un especialista. Le derivo
para que se lo preparen.
```
Resultado: **PASA**. Cero archivos creados, cero preguntas posteriores, cero expectativas falsas.

---

## Resumen del test

| Test | Ruta | Documentos generados | Puntos criticos verificados | Resultado |
|---|---|---|---|---|
| 1 | filiacion-ok / acuerdo / completo / sin vivienda / inscrita / pacto+demanda | pacto + demanda conjunta | fiscal 749.2, cauce 777 como analogico, patria potestad distinguida de custodia, agrupacion por parte, orden pacto→demanda, CGPJ advertido en revision | PASA |
| 2 | filiacion-ok / sin acuerdo / completo / sin vivienda / sin inscripcion | demanda contenciosa | juicio verbal del 770 (no ordinario), MASC acreditado, reconvencion advertida, art. 148 CC, audiencia del mayor de 12 anos calculada sola, 92.8 sin promesas | PASA |
| 3 | filiacion-ok / acuerdo / completo / con vivienda / sin inscripcion / solo pacto | solo pacto | expectativa del cliente sobre la vivienda corregida, art. 96 CC no aplicado como automatico, escalacion ofrecida, compensatoria rechazada, numeracion del pacto sin saltos | PASA |
| Contra-caso | filiacion NO determinada | ninguno | detencion antes de cualquier otro dato, texto fijo del Guardrail 1, sin `Write`, sub-pregunta de desambiguacion | PASA |

---

## Revision UX

**¿Se explican los puntos de discusion antes de pedir la decision?** Si. Las cuatro secciones marcadas *[negociacion]* anteponen la explicacion del regimen por defecto y de sus consecuencias a la pregunta, con base en `references/cc-medidas-hijos-no-matrimoniales.md`: patria potestad (arts. 154 y 156, con el matiz del parrafo final del 156), custodia y estancias (arts. 92 y 94), alimentos (arts. 93, 142, 146 y 148, mas las tablas del CGPJ como orientadoras y su estado de revision) y vivienda (art. 96 como criterio analogico, no como regla). La vivienda es la que recibe la explicacion mas extensa, por ser la que mas se aparta de lo que el cliente espera.

**¿Lenguaje funcional?** Las preguntas de clasificacion hablan del caso ("estan reconocidos legalmente por ambos progenitores", "existe acuerdo entre ambos sobre las medidas relativas a los hijos"), nunca de mecanica interna. La primera pregunta evita el termino "filiacion determinada" en la opcion y lo traduce a "reconocidos legalmente por ambos progenitores y ambos figuran inscritos en el Registro Civil", que es lo que el cliente puede comprobar.

**Numero de turnos (estimacion del recorrido completo):**
- Test 1 (pacto + demanda, caso mas largo): 3 clasificacion + 1 confirmacion de plantilla + ~21 turnos de datos (6 de progenitores con 2 confirmaciones agrupadas, 2 del hijo con 1 agrupada, 3 de convivencia, ~9 de negociacion, 4 procesales de la demanda) ≈ 25-27 turnos.
- Test 2: ≈ 22-24 turnos (una seccion informativa adicional, la de reconvencion, que no genera texto).
- Test 3: ≈ 20-22 turnos (sin demanda, con la seccion de vivienda completa).
- Contra-caso: **2 turnos** (pregunta de filiacion y detencion), o 3 si se recorre la sub-pregunta.

**Ajustes aplicados tras la revision:**
1. **Se reordeno el arbol para preguntar la filiacion primero.** En el diseno inicial seguia el orden natural del brief (acuerdo → filiacion → medidas), pero al ejecutar el contra-caso el cliente respondia dos o tres preguntas antes de que la skill le dijera que su caso no entra por esta via. La guia de autoria permite adelantar los vectores que actuan como filtro de alcance cuando eso ahorra trabajo al usuario, y este es el caso paradigmatico: se dejo V2 como primera pregunta del orden estricto, manteniendo la numeracion del brief.
2. **Se anadio una sub-pregunta de desambiguacion a la filiacion.** La respuesta realista de muchos clientes es "no lo se". Sin la sub-pregunta, el LLM operacional tendria que improvisar; con ella, se le indica exactamente como orientar la comprobacion (certificacion literal de nacimiento) y que la falta de acreditacion detiene igual. Sin este ajuste, el riesgo era el contrario al del contra-caso: dar por determinada una filiacion no acreditada y redactar una demanda contra alguien que no es legalmente progenitor.
3. **La vivienda se pregunta en un vector aparte (V3-bis) y no como cuarta opcion de las medidas.** El brief enumeraba cuatro medidas posibles en un mismo punto de decision; comprimirlas en una pregunta habria producido la mega-pregunta que la guia prohibe. Se dividio en una pregunta binaria de alcance (conjunto completo o solo alguna), una sub-pregunta de desambiguacion, y una pregunta binaria propia para la vivienda, que ademas es la decision con regimen mas distinto.
4. **Se anadio una seccion informativa de riesgo de reconvencion (5-C.5) que no genera texto en el documento.** Al ejecutar el Test 2 se vio que el cliente decidia las medidas sin saber que la otra parte puede pedir la custodia compartida con la contestacion. La advertencia llega antes de concretar las medidas, precisamente para que pueda ampliarlas si le conviene abrir el debate el mismo.
5. **La numeracion de pactos y de fundamentos se convirtio integramente en placeholders.** El Test 3 (con vivienda) y el Test 1 (sin vivienda) producen ordinales distintos para el mismo pacto de sometimiento, y la HOJA ACUERDO y la CONTENCIOSA producen ordinales romanos distintos para el mismo fundamento de fondo, porque el fundamento de procedibilidad solo existe en el contencioso. Con ordinales fijos, uno de los dos escenarios habria quedado con un salto o con un ordinal repetido; la regla de resolucion se documento en el Punto 4 del `SKILL.md`.
6. **Se marcaron como pendientes de verificacion manual tres puntos que era tentador afirmar como remisiones legales.** La verificacion en el BOE mostro que el art. 770 LEC delimita su ambito en las demandas fundadas en el titulo IV del libro I del Codigo Civil (el matrimonio), que el art. 777 esta redactado para la separacion y el divorcio, y que el art. 96 CC habla de conyuges. La skill los presenta como cauce habitual o criterio analogico y advierte de que conviene confirmar el criterio del juzgado. Sin esta verificacion, la skill habria afirmado una remision que la ley no contiene, que es el mismo tipo de error que el art. 87 ter en la skill de divorcio.
7. **La cita del CGPJ lleva advertencia de estado.** La URL responde, pero el apartado consta en revision y sin informacion disponible: remitir al cliente a una calculadora inoperativa es peor que no citarla. La skill cita la referencia y advierte del estado mientras siga siendo el verificado.

Conclusion: el arbol enruta correctamente las dos vias y el contra-caso, activa unicamente los bloques de la rama recorrida, resuelve la numeracion dinamica sin saltos en los dos escenarios que la ponen a prueba, y respeta el protocolo conversacional (una pregunta por turno, agrupacion por parte, anuncio de seccion, no re-preguntar, explicacion antes de decidir). Los guardrails de menores se cumplen: solo nombre y fecha de nacimiento, ninguna pension irrisoria, ningun pacto danoso, y detencion inmediata en el contra-caso de filiacion. Pendiente en produccion: re-verificacion en vivo del BOE, del estado de la herramienta del CGPJ y del criterio procesal de los arts. 770 y 777 en cada lanzamiento (Punto 2).

---

# QA en vivo por agente independiente

Ejecucion **real** (no simulada sobre el papel) del `SKILL.md` por un agente que no habia visto antes esta skill. Se ejecuto el flujo turno a turno en el papel del LLM operativo, se creo el documento con `Write` en `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/medidas-hijos-qa-prueba.md`, se verifico con `Read` y se aplicaron **17 `Edit` incrementales reales** con `oldString` copiado del contenido en disco. Fecha: 03/09/2026.

## Verificacion normativa realmente ejecutada (Punto 2)

Consultas en vivo a la API de legislacion consolidada del BOE, tomando la ultima `<version>` de cada bloque:

- `LEC a769` → devuelve literalmente el apartado 3 registrado en la reference ("sera competente el Juzgado de Primera Instancia del lugar del ultimo domicilio comun de los progenitores..."). **Coincide.**
- `CC art148` → "no se abonaran sino desde la fecha en que se interponga la demanda". **Coincide.**
- `LOPJ aochentaynueve` → apartado 9: "vedada la utilizacion de los medios adecuados de solucion de controversias". **Coincide.**
- `LOPJ aochentaysieteter` → el bloque devuelve "Suprimido". **Coincide.**
- `LO 1/2025 a5` → HTTP 200. CGPJ (calculo de pensiones alimenticias) → HTTP 200, apartado en revision: se mantiene la advertencia.
- **Defecto encontrado al hacerlo:** el Punto 2.2 solo daba el patron de bloque del CC (`art{n}`) y de la LEC (`a{n}`) y pedia "el art. 89 de la LOPJ". Un LLM operativo construye `.../BOE-A-1985-12666/texto/bloque/a89` y recibe **HTTP 404** (comprobado). La LOPJ identifica sus bloques con el ordinal en letras. Sin el id correcto, la verificacion del articulo que sostiene el guardrail de violencia caia siempre al fallback de `web_search`. **Corregido** (ver "Correcciones aplicadas").

## Escenario del cliente

"Me he separado de mi pareja, no estabamos casados. Tenemos una hija de 4 anos, los dos la reconocimos al nacer. El quiere verla pero no nos ponemos de acuerdo en cuanto tiempo ni en el dinero. El piso donde vivo con la nina es de el."

Clasificacion resuelta por Escucha Activa: **V2** = filiacion determinada ("los dos la reconocimos al nacer"); **V1** = no existe acuerdo; **V3** = conjunto completo ("cuanto tiempo" = custodia y estancias; "el dinero" = alimentos). Se preguntan solo **V3-bis** y **V4**. V5 no aplica. Ruta: `V2-determinada → V1-sin-acuerdo → V3-completo → V3bis-si → V4-sin-inscripcion → HOJA CONTENCIOSA`.

Datos sinteticos: PROGENITOR A (demandante, DNI 00000000-T), PROGENITOR B (demandado, DNI 11111111-H), HIJO MENOR 1 nacida el 12/05/2022 — **unicamente nombre y fecha de nacimiento**.

## Transcripcion literal de los turnos generados

Los textos fijos del `SKILL.md` se reproducen **tal como estan almacenados** (sin tildes); la prosa generada por el agente va con ortografia normal. Vease la observacion O1.

**Turno 1 — agente (carga + introduccion + primera pregunta pendiente):**

> **Skill cargada satisfactoriamente.**
>
> Vamos a proceder a la preparacion de los documentos necesarios para fijar las medidas relativas a sus hijos. Para ajustarlos correctamente a su caso, es necesario precisar antes algunos datos.
>
> Sobre la vivienda en que residen los hijos:
> 1. Se solicita tambien que se atribuya su uso
> 2. No es necesario pronunciarse sobre ella

*Cliente:* "La 1. Es donde vivimos la nina y yo."

**Turno 2 — agente:**

> La relacion entre ambos progenitores fue:
> 1. Pareja de hecho inscrita en un registro
> 2. Convivencia estable sin inscripcion en ningun registro
> 3. Sin convivencia estable

*Cliente:* "La 2. Vivimos juntos desde septiembre de 2018 y lo dejamos el 15 de marzo de este ano."

**Turno 3 — agente (Confirmacion, Punto 3):**

> A su caso corresponde una demanda de medidas paternofiliales en el proceso del articulo 748.4.º de la Ley 1/2000, de Enjuiciamiento Civil, que se sustancia por los tramites del juicio verbal conforme a su articulo 770, siendo competente el Juzgado que determina su articulo 769.3. Las medidas se fundan en los articulos 154, 156, 92, 93, 94, 142, 146 y 148 del Codigo Civil. Al existir hijos menores de edad, la intervencion del Ministerio Fiscal es preceptiva (articulo 749.2 de la Ley de Enjuiciamiento Civil). Debe acreditarse el intento previo de un medio adecuado de solucion de controversias: sin ese requisito la demanda puede ser inadmitida (articulo 5 de la Ley Organica 1/2025 y articulo 264.4.º de la Ley de Enjuiciamiento Civil). Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763, https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 y https://www.boe.es/buscar/act.php?id=BOE-A-2025-76
>
> Le confirmo que el hecho de que ustedes no hayan estado casados no altera en nada los derechos de sus hijos ni los deberes de ambos progenitores: se fija exactamente lo mismo que se fijaria en un divorcio en cuanto a los hijos. Lo unico que no existe aqui es el vinculo matrimonial y, con el, ni regimen economico matrimonial que liquidar ni pension compensatoria.
>
> ¿Que documento desea utilizar como base?
> 1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
> 2. Adjuntar su propio documento

*Cliente:* "1"

**Turno 4 — agente (tras `Write` y `Read`):**

> He creado el documento en /Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/medidas-hijos-qa-prueba.md. ¿Desea que empecemos a completar los datos del escrito?

*Cliente:* "Si."

**Turno 5 — agente (anuncio de seccion 5-C.1 + primera pregunta):**

> Procedemos a la identificación de la parte demandante. Indíqueme, por favor, su nombre y apellidos completos, tal como figuran en su documento de identidad.

*Cliente:* "PROGENITOR A."

**Turnos 6 y 7:** "Indíqueme su número de DNI o NIE." / "Indíqueme su domicilio actual completo, con calle, número, piso, código postal y localidad."

**Turno 8 — vista previa agrupada de la parte demandante (sin `Edit` intermedio):**

> Estos son los datos de la parte demandante que se harán constar en el encabezamiento del escrito:
>
> PROGENITOR A, mayor de edad, con DNI 00000000-T y domicilio en la calle Ejemplo, número 7, 3.º B, 28001 Ciudad Ejemplo.
>
> ¿Confirmamos esta cláusula?

*Cliente:* "Sí." → `Edit` (2 llamadas: nombre en las tres apariciones y el fragmento de DNI y domicilio del comparecendo).

**Turno 9 — agente (anuncio + primera pregunta de la parte demandada):**

> Identificada la parte demandante, pasamos a la parte demandada. Indíqueme el nombre y apellidos completos del otro progenitor.

*Turnos 10 y 11:* DNI y domicilio del demandado. *Turno 12:* vista previa agrupada y confirmación única → `Edit`.

**Turno 13 — agente:**

> Corresponde identificar a los hijos comunes. Indíqueme el nombre de su hija y su fecha de nacimiento. No necesito ningún otro dato de la menor.

*Cliente:* "HIJO MENOR 1, nació el 12 de mayo de 2022. ¿Le paso el colegio y el número de la cartilla sanitaria?"

**Turno 14 — agente (rechazo del dato excedente + vista previa agrupada):**

> No es necesario y no se incorporarán al escrito: para fijar las medidas basta el nombre y la fecha de nacimiento, y cualquier otro dato de la menor quedaría expuesto en un documento que se presenta ante el Juzgado y se traslada a la parte contraria.
>
> En el hecho primero se hará constar: HIJO MENOR 1, nacida el 12 de mayo de 2022, cuya filiación consta determinada respecto de ambos progenitores e inscrita en el Registro Civil.
>
> ¿Confirmamos esta cláusula?

**Turno 15 — agente (5-C.4; las fechas de convivencia ya constaban por Escucha Activa, no se vuelven a preguntar):**

> Pasamos a los hechos: el cese de la convivencia y el intento de solución extrajudicial. Sus fechas de convivencia ya me constan y quedarán recogidas como antecedente, de modo que no se las vuelvo a pedir.
>
> Antes de preguntarle, debo explicarle un requisito que condiciona la admisión del escrito. El artículo 5.2 de la Ley Orgánica 1/2025 exige acreditar que, antes de demandar, se ha intentado un medio adecuado de solución de controversias, y la guarda, la custodia y los alimentos de los hijos menores no figuran entre las materias exceptuadas. Basta la actividad negociadora desarrollada directamente por ustedes o entre sus abogados, siempre que lo negociado coincida con lo que se pide en el pleito. Sin acreditarlo, la demanda puede ser inadmitida.
>
> Dígame si ha existido ese intento previo con el otro progenitor.

*Cliente:* "Sí, nuestros abogados negociaron. Empezamos el 20 de abril y se rompió el 5 de junio."

**Turno 16 — agente (riesgo de reconvención, 5-C.5, no genera texto):**

> Antes de concretar las medidas, debo advertirle de un riesgo del procedimiento. Conforme a la regla 2.ª, letra d), del artículo 770 de la Ley de Enjuiciamiento Civil, la parte demandada puede reconvenir al contestar y pedir medidas que usted no haya solicitado —señaladamente, la custodia compartida—, y usted dispondría entonces de diez días para contestar a esa reconvención. Indíqueme si prevé que el otro progenitor formule esa pretensión y si desea, en previsión de ello, ampliar las medidas que se solicitan en la demanda.

*Cliente:* "Creo que pedirá más tiempo con ella, pero no la custodia compartida. Dejémoslo como está."

**Turno 17 — agente (patria potestad, 5-C.7):**

> Pasamos a la primera de las medidas que se solicitarán: el ejercicio de la patria potestad. Conviene que distinga dos cosas que suelen confundirse. La patria potestad corresponde a ambos progenitores por el solo hecho de la filiación y no depende de con quién viva la niña; la guarda y custodia es la convivencia diaria. Que usted tenga la custodia no priva al otro progenitor de la patria potestad, ni al revés.
>
> Hay un matiz importante en su caso: el párrafo final del artículo 156 del Código Civil prevé que, viviendo los progenitores separados, la patria potestad la ejerza aquel con quien la hija conviva, salvo que el Juzgado atribuya expresamente el ejercicio conjunto. Por eso conviene solicitarlo de forma expresa en lugar de darlo por supuesto. Además, el artículo 154.3.º exige el consentimiento de ambos, o autorización judicial, para cambiar el lugar de residencia habitual de la menor, y los desacuerdos puntuales se resuelven acudiendo al artículo 156.
>
> Indíqueme si desea que se solicite el ejercicio conjunto y qué decisiones quiere que queden expresamente reservadas al acuerdo de ambos.

*Cliente:* "Sí, conjunto. Colegio, médicos y viajes al extranjero."

**Turno 18 — agente (custodia y estancias, 5-C.8):**

> Corresponde concretar la guarda y custodia y el régimen de estancias que se solicitarán. No existe preferencia legal automática por ninguna modalidad. La custodia compartida se acuerda cuando la piden ambos progenitores (artículo 92.5 del Código Civil) y el Juzgado valora expresamente la relación que ustedes mantengan entre sí (artículo 92.6); a instancia de una sola parte es excepcional y exige informe del Ministerio Fiscal y una motivación de que solo así se protege el interés de la menor (artículo 92.8), de modo que no puedo prometerle su concesión ni la del otro progenitor. La custodia exclusiva atribuye la convivencia diaria a un progenitor, y el otro conserva la patria potestad y un régimen de estancias, comunicación y visitas (artículo 94). El único criterio que decide es el interés superior de la menor, y el hecho de que ustedes no se casaran es indiferente.
>
> Le anticipo algo que le ahorrará conflictos: un régimen "amplio y flexible" es la fuente más habitual de incidentes de ejecución. Cuanto más concreto sea el calendario, menos discusiones tendrá su hija delante.
>
> Indíqueme qué modalidad de custodia desea solicitar.

*Cliente:* "Exclusiva para mí, pero con un régimen generoso para él, que la niña lo necesita."

*Turnos 19 a 21:* calendario ordinario, reparto de vacaciones y lugar de entregas y recogidas, uno por turno, con vista previa y confirmación cada uno → `Edit`.

**Turno 22 — agente (alimentos, 5-C.9):**

> Pasamos a la pensión de alimentos que se solicitará. El deber de alimentos nace de la filiación y existe exactamente igual sin matrimonio (artículo 143.2.º del Código Civil). No hay tarifa legal: la cuantía debe ser proporcionada a los medios de quien los da y a las necesidades de quien los recibe (artículo 146). El Consejo General del Poder Judicial publica unas tablas orientadoras, no vinculantes, en https://www.poderjudicial.es/cgpj/es/Servicios/Utilidades/Calculo-de-pensiones-alimenticias/, pero debo advertirle de que a día de hoy ese apartado consta en proceso de revisión y sin información disponible, de modo que no puedo remitirle a una calculadora que no está operativa.
>
> Tres precisiones más. La pensión cubre los gastos ordinarios y previsibles; los extraordinarios son los imprevisibles y no periódicos, y lo habitual es repartirlos por mitad, con comunicación y justificación previas y acuerdo previo cuando no sean urgentes. Conviene pactar una actualización anual para que la pensión no se degrade. Y debe saber que los alimentos no se abonan sino desde la fecha de interposición de la demanda (artículo 148 del Código Civil): no cabe reclamar mensualidades anteriores por esta vía, de modo que retrasar la presentación tiene un coste económico.
>
> Indíqueme el importe mensual que solicita por la hija común y en qué ingresos del otro progenitor lo funda.

*Cliente:* "300 euros. Él gana unos 2.100 netos; yo, 1.250."

*Turnos 23 a 25:* día de pago y cuenta de abono, criterio de actualización y reparto de gastos extraordinarios → `Edit` en cada uno.

**Turno 26 — agente (vivienda, 5-C.10 — el punto critico del caso):**

> Corresponde ahora la atribución del uso de la vivienda en que reside la menor, y quiero explicárselo con detalle porque su caso no funciona como un divorcio.
>
> Aquí no hay régimen económico matrimonial que liquidar: no hay nada que repartir entre ustedes. El artículo 96 del Código Civil, que en los divorcios atribuye el uso de la vivienda familiar al progenitor con quien quedan los hijos, está redactado para los cónyuges y para los supuestos de nulidad, separación y divorcio, de modo que **no se le aplica de forma directa**. Sin matrimonio, la vivienda se rige por las reglas ordinarias de la propiedad y de los contratos: si es privativa de un progenitor, es suya; si fuera de ambos, cualquiera podría pedir la división; si fuera de alquiler, mandaría el contrato.
>
> Lo que sí opera a favor de su hija es su interés: la necesidad de habitación forma parte del contenido de los alimentos (artículo 142 del Código Civil), y por esa vía se invoca el criterio del artículo 96.1 por analogía. Pero no puedo decirle que usted tenga derecho al uso por el solo hecho de tener la custodia: eso no es así.
>
> Debo advertirle expresamente de que, siendo el piso propiedad exclusiva del otro progenitor, lo que se pide es una limitación de su facultad de disponer de un bien propio, y el resultado es incierto. Le recomiendo que un abogado especialista revise este punto antes de presentar el escrito, y le pongo sobre la mesa las alternativas: pedir el uso por un plazo cerrado en lugar de indefinido, compensarle económicamente por ese uso, o cuantificar la necesidad de habitación dentro de la pensión de alimentos en lugar de atribuir el uso.
>
> Indíqueme, en primer lugar, la dirección exacta de la vivienda.

*Cliente:* "Es la misma en la que vivo, calle Ejemplo 7, 3.º B. Es suya, la compró antes de que empezáramos a vivir juntos. Prefiero pedir un plazo cerrado: tres años, para que la niña no cambie de casa y de colegio de golpe."

*Turnos 27 a 29:* titularidad y cómo se acredita, atribución solicitada y plazo → `Edit`.

**Turno 30 — agente (documentación económica, 5-C.11):**

> Corresponde relacionar la documentación económica que se acompañará. La regla 1.ª del artículo 770 de la Ley de Enjuiciamiento Civil obliga a **ambas partes** a aportar los documentos de que dispongan que permitan evaluar su situación económica: declaraciones tributarias, nóminas, certificaciones bancarias y títulos de propiedad o certificaciones registrales. Indíqueme qué documentos podrá aportar usted.

*Turnos 31 a 34:* descripción de ingresos y gastos, medidas provisionales, prueba adicional, costas, representación procesal (agrupada) y cierre. En la representación, el cliente indica que aún no tiene procurador designado: **`{{nombre_procurador}}` se conserva con su nombre propio en el documento**, y así se le advierte.

**Turno 35 — agente (medidas provisionales, 5-C.12):**

> Procede decidir si se interesan medidas que rijan mientras se sustancia el procedimiento. Pueden pedirse en la propia demanda para que la custodia, las estancias y los alimentos rijan desde el principio y no solo desde la sentencia, con comparecencia de las partes e intervención del Ministerio Fiscal. Le señalo, para que lo valore con precisión, que este cauce se aplica a estos procesos por analogía con los artículos 771 y 773 de la Ley de Enjuiciamiento Civil y no por remisión expresa de la ley. Indíqueme si desea que se interesen.

## Veredicto A — Calidad del texto generado por el agente

**Tono y tratamiento: correcto.** Todo el texto visible usa "usted" y verbos de registro formal: "Indíqueme, por favor, su nombre y apellidos completos", "Dígame si ha existido ese intento previo", "debo advertirle expresamente". No aparece ni un "vale", "perfecto" o "genial", ni una muletilla de relleno. Las citas normativas van con nombre completo y artículo, como exige el `CLAUDE.md` del plugin ("artículo 5.2 de la Ley Orgánica 1/2025", "regla 2.ª, letra d), del artículo 770 de la Ley de Enjuiciamiento Civil").

**Explicación antes de la decisión: correcta y con sensibilidad suficiente.** Las cuatro secciones marcadas *[negociación]* explican el régimen legal antes de preguntar. Dos frases concretas hacen el trabajo de sensibilidad sin caer en el paternalismo: "Cuanto más concreto sea el calendario, menos discusiones tendrá su hija delante" y, en la vivienda, la alternativa se argumenta con "para que la niña no cambie de casa y de colegio de golpe" recogida del propio cliente. El turno de custodia dice expresamente que no puede prometerse la concesión de la compartida a instancia de una sola parte.

**Invisibilidad: sin fugas.** Reviso mi propio texto: no aparece "V1", "V3-bis", "hoja", "vector", "fase", "voy a", ni ningún resumen de validación con checks. La única línea de mecánica es la de carga del Punto 0, que está permitida. Los anuncios de sección nombran materia jurídica ("Procedemos a la identificación de la parte demandante", "Pasamos a la pensión de alimentos que se solicitará"), no mecánica interna.

**Cero invenciones: correcto.** No se inventó ningún importe (los 300 euros los fija el cliente), ninguna fecha, ninguna cita jurisprudencial. Las tablas del CGPJ se citaron **con** la advertencia de que el apartado consta en revisión, que es exactamente lo que la reference exige. De la menor solo se pidieron nombre y fecha de nacimiento, y cuando el cliente ofreció espontáneamente el colegio y la cartilla sanitaria, el agente los rechazó y explicó por qué.

**Un punto donde el texto generado se queda corto:** en el turno de medidas provisionales fue necesario decir que el cauce de los artículos 771 y 773 se aplica "por analogía y no por remisión expresa". Es literalmente lo que exige el guardrail 12, pero al cliente le suena a que su abogado no sabe qué procedimiento se sigue. Sugerencia (no aplicada, es criterio del autor): reformularlo como "es el cauce que los juzgados aplican en estos procesos" y dejar el matiz técnico para la advertencia final del documento.

## Veredicto B — El asset visto desde el LLM que lo rellena

**Placeholders: limpios.** Los 79 placeholders de los dos assets son `{{snake_case}}` desnudos, sin texto de ayuda dentro de las llaves, sin anidamientos y sin ningún `[DATO]` de corchete simple (verificado con `grep` sobre ambos assets). Ninguno resultó ambiguo al rellenarlo: `{{criterio_competencia}}`, `{{titularidad_vivienda}}` y `{{descripcion_situacion_economica}}` son de texto libre pero su contexto en la frase dice exactamente qué va.

**Numeración dinámica: funciona, sin huecos ni repeticiones.** Verificado sobre el documento realmente escrito: hechos PRIMERO a SEXTO correlativos (`{{ordinal_hecho_economica}}` = QUINTO, `{{ordinal_hecho_medidas}}` = SEXTO); fundamentos I a VIII (el fondo cae en el IV porque el III de procedibilidad sí existe en la vía contenciosa); documentos nº 1 nacimiento, nº 2 MASC, nº 3 económicos (el nº 2 de parejas de hecho no se escribe porque V4 = 2, y el MASC ocupa su lugar sin dejar hueco); medidas 1 a 5; advertencia de violencia = 9. **Ningún ordinal quedó sin resolver y ninguno se repite.**

**Bloques condicionales: dos problemas reales.**

1. La medida de patria potestad estaba condicionada a *"Si no hay acuerdo y se piden guarda y custodia y regimen de estancias"*, pero la sección 5-C.7 del `SKILL.md` pregunta por la patria potestad **siempre**, sin condición de V3. Un caso de solo alimentos habría recogido la decisión del cliente sobre el ejercicio conjunto y luego no habría tenido dónde escribirla. **Corregido.**
2. El hecho CUARTO de la vía contenciosa tiene el encabezado en un bloque condicional y el cuerpo (MASC intentado / declaración responsable) en otro. Al crear el documento en el Punto 4, cuando el dato del MASC todavía no existe, el escrito queda con un encabezado de hecho vacío hasta la sección 5-C.4. Es transitorio y se resuelve solo, pero conviene saberlo: **no es corrupción del archivo**.

**Coherencia tipográfica: defecto encontrado.** Los fundamentos fijos estaban rotulados `**I. Competencia.**` y `**II. Procedimiento.**` (punto) mientras los que llevan ordinal en placeholder salen como `**IV — Fondo.**` (raya), y los HECHOS usan raya. El documento final mezclaba las dos convenciones en la misma lista numerada. **Corregido**: los tres fijos pasan a raya.

**Lectura de corrido: suena a escrito real.** Leído completo, el documento se sostiene como demanda: encabezamiento, seis hechos con una idea cada uno, ocho fundamentos, cinco medidas ejecutables, suplico ajustado y dos otrosíes. Dos asperezas menores: la medida de alimentos dice "300 euros mensuales **por cada hijo**" cuando hay una sola hija (correcto pero algo mecánico), y `{{plazo_uso_solicitado}}` va entre comas en la medida de vivienda, de modo que un valor escueto ("tres años") produciría una frase agramatical; se salva escribiendo una frase preposicional ("por el plazo de tres años a contar desde la fecha de la sentencia"), que es lo que hizo el agente.

## Veredicto C — Los dos puntos criticos

**C1. Vivienda propiedad del otro progenitor: la skill lo trata correctamente, el asset no del todo.**

El `SKILL.md` acierta de pleno. La sección 5-C.10 (y su gemela 5-A.8), el guardrail 8 y la reference dicen exactamente lo que hay que decir: que no hay régimen económico matrimonial que liquidar, que el artículo 96 está redactado para los cónyuges y **no se aplica de forma directa**, que sin matrimonio manda la titularidad del inmueble y el interés de la menor por la vía del artículo 142, que el 96.1 se invoca **por analogía**, y que nunca se afirme que el custodio tiene derecho al uso por serlo. La escalación es obligatoria cuando la vivienda es privativa del otro progenitor y las cuatro alternativas (plazo cerrado, compensación, cuantificar la habitación en la pensión, extinción del condominio) están enumeradas. Nada de esto es un traslado mecánico del régimen del divorcio.

El defecto estaba en el asset: el fundamento de derecho decía *"La atribucion que se interesa se funda en la titularidad del inmueble, que se acredita, y en el interes de los hijos comunes"*. Cuando la titularidad es **del demandado** —el caso que la propia skill señala como conflictivo— eso es fundar la pretensión en el hecho que juega en contra: el escrito estaría diciendo al Juzgado que pide el uso porque el piso es del otro. **Corregido**: ahora funda la atribución en el interés de la menor y presenta la titularidad como circunstancia acreditada que el Juzgado pondera para fijar el alcance y la duración del uso.

**C2. Violencia de género: el guardrail existe, es correcto y NO cita el artículo 87 ter.**

`grep -rn "87 ter"` sobre toda la skill devuelve tres apariciones y las tres son **prohibiciones** de citarlo: el guardrail 3 ("PROHIBIDO citar el art. 87 ter LOPJ: fue suprimido por el art. 1.26 de la LO 1/2025"), la fila de la tabla de escalación y el registro de la reference. Ningún asset lo menciona. Comprobado además contra el BOE en esta ejecución: el bloque `aochentaysieteter` de la LOPJ devuelve "Suprimido".

El contenido sustantivo del guardrail es correcto y está verificado en vivo: competencia de la Sección de Violencia sobre la Mujer (artículo 89, apartados 6.a, 6.b, 6.e y 7, LOPJ, y artículo 44 de la LO 1/2004), **MASC y mediación vedados** (artículo 89.9 LOPJ, texto literal confirmado en el BOE en esta ejecución), improcedencia de la guarda conjunta (artículo 92.7 CC) y del régimen de visitas en los supuestos del artículo 94 CC. La detención opera "en cualquier punto del flujo", incluida la conversación libre, y la advertencia nº 9 del documento la reproduce.

Dos matices que dejo apuntados, ninguno de ellos un defecto que haya corregido:

- La skill **no hace cribado**: por diseño no existe pregunta de clasificación sobre violencia (el "vector de guarda"), de modo que el guardrail depende por completo de que el cliente mencione algo. Me parece la decisión correcta —preguntar "¿hay violencia?" en el turno 2 a quien viene a fijar unas estancias es invasivo y produce falsos negativos—, pero conviene que quien mantenga la skill sepa que esa es la elección que se hizo.
- La interacción entre el guardrail y el requisito de MASC está bien resuelta en el texto (guardrail 10: nunca proponer un MASC si hay indicios), y en la vía contenciosa es donde más importa, porque el flujo empuja al cliente a negociar antes de demandar.

## Correcciones aplicadas

| # | Archivo | Cambio |
|---|---|---|
| 1 | `SKILL.md` (Punto 2.2) | Añadido el endpoint de la LOPJ y el aviso de que sus bloques van con el ordinal **en letras**: `aochentaynueve` (art. 89) y `aochentaysieteter` (art. 87 ter); se advierte de que `a89` devuelve 404. Añadido el bloque `a5` para la LO 1/2025. Sin esto, la verificación del artículo que sostiene el guardrail de violencia fallaba siempre |
| 2 | `references/fuentes-plantillas-validadas.md` | Añadidos los tres endpoints reales y un aviso sobre los identificadores de bloque de la LOPJ, para que la próxima verificación no repita el 404 |
| 3 | `assets/demanda-medidas-paternofiliales.md` | La medida de **patria potestad** deja de estar condicionada a que se pidan custodia y estancias: pasa a `Si no hay acuerdo entre los progenitores`, en coherencia con la sección 5-C.7, que la pregunta siempre |
| 4 | `assets/demanda-medidas-paternofiliales.md` | Fundamentos fijos `I.`, `II.` y `III.` reescritos como `I —`, `II —`, `III —`, para no mezclar dos convenciones tipográficas con los ordinales resueltos por placeholder |
| 5 | `assets/demanda-medidas-paternofiliales.md` | Fundamento de la **vivienda** reescrito: la atribución se funda en el interés de los hijos (artículo 142 CC, criterio del 96.1 por analogía) y la titularidad pasa a presentarse como circunstancia acreditada que el Juzgado pondera, en lugar de como fundamento de la pretensión |

Los cambios 4 y 5 se propagaron al documento generado para que refleje el asset corregido.

## Observaciones no corregidas (criterio del autor de la skill)

- **O1. Los textos fijos están almacenados sin tildes.** El Punto 0, la introducción del Punto 1 y los textos de confirmación del Punto 3 se emiten literalmente al cliente: "Vamos a proceder a la preparacion de los documentos necesarios...". En un registro de abogado formal, la falta de tildes se lee como descuido. Afecta a todo el plugin, no solo a esta skill, así que no lo he tocado: es una decisión de repositorio.
- **O2. V2 es bloqueante pero se resuelve por inferencia.** "Los dos la reconocimos al nacer" basta razonablemente para dar la filiación por determinada, pero la skill no fija un umbral: "él es el padre" no debería bastar y la regla de no-backtracking empuja a no preguntar. Convendría una línea en el Punto 1 diciendo que V2 solo se da por resuelto por Escucha Activa si el cliente afirma el reconocimiento o la inscripción, y no la mera paternidad biológica.
- **O3. Encabezado del hecho CUARTO sin cuerpo** durante la fase de creación (ver Veredicto B).
- **O4. `{{plazo_uso_solicitado}}` entre comas** puede producir una frase agramatical con un valor escueto (ver Veredicto B).
- **O5. El nombre del archivo generado** en esta prueba (`medidas-hijos-qa-prueba.md`) lo impuso el encargo de QA; en producción la convención del Punto 4 es `snake_case`, del tipo `demanda_medidas_paternofiliales_progenitor_a.md`.
