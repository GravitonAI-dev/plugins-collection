# Test de ejecucion — skill `derecho-civil-pareja-de-hecho`

Ejecucion manual del arbol de decision sobre cuatro escenarios (3 principales + 1 contra-caso). Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento, la verificacion autonomica y el relleno de los assets.

## Verificacion normativa (Punto 2)

**Fuentes estatales verificadas realmente el 03/09/2026** contra la API de legislacion consolidada del BOE (`Accept: application/xml`):

- Codigo Civil (BOE-A-1889-4763), bloques `art1255`, `art1258`, `art1261`, `art1274`, `art1275`, `art1323`, `art1438`, `art392` a `art401`, `art404`, `art406` y `art1902`. Confirmado que `art1323` habla solo de conyuges (redaccion de la Ley 13/2005) y que `art1438` es norma del regimen de separacion de bienes **del matrimonio** (redaccion de la Ley 11/1981): ninguno de los dos es base directa del pacto de pareja de hecho, y asi queda registrado en las references.
- LGSS (BOE-A-2015-11724), bloque `a221`: redaccion de la Ley 21/2021 vigente desde 01/01/2022, con los cinco anos de convivencia por empadronamiento y la antelacion minima de dos anos de la inscripcion.
- Texto refundido del baremo de circulacion (BOE-A-2004-18911), bloques `a36` y `a62`, en redaccion de la **Ley 35/2015**: el conviviente superviviente de pareja estable sufre el mismo perjuicio resarcible que el conyuge viudo.

**Aviso de formato confirmado en la practica:** el Codigo Civil devolvio 404 con la convencion `aNNN` y 200 con `artNNN`; la LGSS y el baremo, al reves. El `SKILL.md` y la reference recogen ese aviso porque un 404 podria interpretarse erroneamente como fuente inaccesible y disparar el fallback sin necesidad.

**Jurisprudencia verificada en sesion** (via publicaciones oficiales del BOE, no de memoria): STC 81/2013 (BOE-A-2013-4901), STC 93/2013 (BOE-A-2013-5436), STS de 12/09/2005 y STS 17/2018 de 15/01 (ECLI:ES:TS:2018:37), estas dos ultimas a traves de la Biblioteca Juridica del BOE. Ninguna otra sentencia se cita en la skill.

**Verificacion autonomica:** se ejecuto de verdad con `web_search` en los tres escenarios, no se simulo. El detalle de lo obtenido consta en cada test.

---

## Test 1 — Pareja en Madrid que quiere inscribirse

**Mensaje inicial:** "Mi pareja y yo llevamos dos anos viviendo juntos en Madrid y queremos hacernos pareja de hecho. ¿Que necesitamos?"

### Recorrido del arbol
```
V1 -> escucha activa: "queremos hacernos pareja de hecho"   V1 = constituir e inscribir (sin pregunta)
V2 -> escucha activa: "viviendo juntos en Madrid"           V2 = Comunidad de Madrid (sin pregunta)
V3, V4 -> no aplican a la rama de inscripcion
Verificacion autonomica EJECUTADA (no de memoria)
HOJA INSCRIPCION -> assets/checklist-inscripcion-registro.md
```

### Verificacion autonomica realmente ejecutada

`web_search` sobre la normativa madrilena y sobre su registro devolvio, de fuente oficial:

- **Ley 11/2001, de 19 de diciembre, de Uniones de Hecho de la Comunidad de Madrid**, texto consolidado en el BOE (BOE-A-2002-4374), con ultima actualizacion publicada el 26/12/2024 y vigente desde el 27/12/2024.
- **Articulos 4 y 5 declarados inconstitucionales y nulos** por la STC 81/2013, de 11 de abril (BOE-A-2013-4901). El bloque de aviso sobre preceptos anulados del asset se activa por esta razon.
- **Requisito de doce meses de empadronamiento conjunto** en el mismo domicilio inmediatamente anteriores a la solicitud, introducido por la Ley 11/2022 con efectos desde el 23/03/2023, mas residencia en la Comunidad de Madrid.
- Registro competente: **Registro de Uniones de Hecho de la Comunidad de Madrid**, con su sede electronica y su tasa.

**Este es el punto critico del test y lo supera:** ninguno de estos datos — y en particular ni la anulacion de los articulos 4 y 5 ni el requisito de empadronamiento de 2023 — estaba escrito en las references de la skill. Solo aparecen porque la verificacion se hizo en el lanzamiento. Una skill que hubiera "recordado" la Ley 11/2001 habria descrito un regimen que ya no existe.

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija (que advierte ya de que no hay ley estatal) + los dos vectores resueltos por escucha activa, de modo que no se formula ninguna pregunta de clasificacion; se ejecuta la verificacion en silencio.
- Turno 2: Confirmacion visible (Punto 3), texto fijo INSCRIPCION: ausencia de ley estatal, denominacion exacta de la ley madrilena con enlace, denominacion del registro con enlace, y eleccion plantilla/documento propio.
- Turnos 3-6: datos de cada conviviente, con confirmacion agrupada por parte (una vista previa por conviviente, en el turno siguiente al ultimo dato).
- Turnos 7-11: contraste de la situacion de la pareja con **los requisitos verificados, uno por turno**. Al llegar al empadronamiento conjunto, el usuario indica que se empadronaron juntos hace ocho meses.
- Turno 12: validacion bloqueante — la skill calcula que faltan cuatro meses para los doce exigidos, activa el bloque de requisitos pendientes, indica desde cuando podra presentarse la solicitud y advierte de que presentarla antes conduce a la denegacion o al archivo. **No dice que no pueden inscribirse: dice cuando podran.**
- Turno 13: documentacion y tramite (tasa, forma de presentacion, plazo), mas pregunta por el municipio para comprobar si hay registro municipal.
- Turno 14: efectos de la inscripcion — los cuatro puntos de lo que NO produce, explicados sin suavizar.
- Turno 15: pension de viudedad; pregunta por hijos comunes (no los hay), de modo que el bloque de exencion de los cinco anos NO se activa y se explica que rigen los cinco anos de empadronamiento y los dos de antelacion.
- Turno 16: sucesion y testamento, con derivacion a `derecho-civil-testamento-planificacion`.
- Turno 17: recomendacion de pacto de convivencia, ofreciendo prepararlo despues.

### Documento generado (extracto relleno, datos sinteticos)
```
CHECKLIST DE INSCRIPCION EN EL REGISTRO DE PAREJAS DE HECHO
> DRAFT — para revision por un abogado colegiado antes de su firma.
> Normativa autonomica verificada: Ley 11/2001, de 19 de diciembre, de Uniones de Hecho
  de la Comunidad de Madrid — 03/09/2026

1. Marco normativo aplicable
No existe ley estatal de parejas de hecho ni registro estatal. [...] El registro competente
es el Registro de Uniones de Hecho de la Comunidad de Madrid.
Aviso sobre el texto de la ley: los articulos 4 y 5 han sido anulados y no reflejan el
regimen vigente.

2. Requisitos de constitucion
| Empadronamiento conjunto | Doce meses inmediatamente anteriores a la solicitud | CUMPLE
  PARCIALMENTE: ocho meses a la fecha |
Requisitos aun no cumplidos: empadronamiento conjunto de doce meses. La solicitud no
deberia presentarse hasta cumplirse ese plazo.
```

**Bloques ACTIVADOS:** aviso de preceptos anulados; requisitos aun no cumplidos.
**Bloques NO ACTIVADOS:** aviso de verificacion pendiente (la verificacion si funciono); exencion de los cinco anos por hijos comunes (no los hay); registro municipal (el municipio no dispone de uno propio).

Resultado: **PASA**. Los requisitos proceden integramente de la verificacion del lanzamiento, la validacion temporal se aplica antes de dar el tramite por presentable, y la fila de requisito adicional se poda por no haber devuelto la verificacion ninguno.

---

## Test 2 — Pacto de convivencia con vivienda al 50 % y aportaciones desiguales

**Mensaje inicial:** "Vivimos juntos en Valencia desde 2022 y compramos un piso a nombre de los dos al 50 %, pero yo puse 120.000 euros y ella 60.000. Queremos dejarlo por escrito."

### Recorrido del arbol
```
V1 -> escucha activa: "queremos dejarlo por escrito"        V1 = pacto de convivencia (sin pregunta)
V2 -> escucha activa: "en Valencia"                         V2 = Comunitat Valenciana (sin pregunta)
V4 -> escucha activa: "yo puse 120.000 y ella 60.000"       V4 = hay bienes comunes y aportaciones
                                                                 desiguales (sin pregunta)
V3 -> no aplica (solo rama de ruptura)
Verificacion autonomica EJECUTADA
HOJA CONVIVENCIA -> assets/pacto-convivencia.md
```

### Verificacion autonomica realmente ejecutada

`web_search` devolvio, de fuente oficial (Portal de Justicia Abierta de la Generalitat Valenciana): **Ley 5/2012, de 15 de octubre, de Uniones de Hecho Formalizadas de la Comunitat Valenciana**, con inscripcion mediante comparecencia personal y conjunta ante funcionario publico, plazo de resolucion de tres meses, y requisito de convivencia en la Comunitat Valenciana sin exigencia de un periodo minimo previo. La skill vuelca esa denominacion y esa fecha al encabezamiento del pacto, sin afirmar ningun requisito que la busqueda no haya devuelto.

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija; los tres vectores aplicables quedan resueltos por escucha activa, sin ninguna pregunta de clasificacion.
- Turno 2: Confirmacion visible, texto fijo CONVIVENCIA (articulo 1255 y articulos 392 y siguientes, con enlace al Codigo Civil, mas la ley valenciana verificada) + eleccion de base documental.
- Turno 3: creacion del documento con `Write`, `Read` de verificacion, confirmacion de la ruta absoluta y — en la MISMA respuesta — anuncio de la primera seccion y primera pregunta. **No hay turno de "¿empezamos?".**
- Turnos 4-9: datos de cada conviviente, con confirmacion agrupada por parte.
- Turnos 10-12: la convivencia y su situacion registral (inicio 01/03/2022, domicilio comun, inscritos el 15/06/2023).
- Turno 13: regimen de los bienes de cada uno — la skill explica primero que la convivencia no crea regimen alguno; el cliente declina inventariar sus bienes privativos, de modo que ese bloque NO se activa.
- Turnos 14-16: bienes adquiridos en comun y aportaciones desiguales. La skill explica la presuncion de cuotas iguales del articulo 393 y la carga de la prueba **antes** de pedir cifras, y luego ofrece las tres salidas posibles a la desigualdad (credito, ajuste de cuota, liberalidad) explicando cada una. El cliente elige el credito de 30.000 euros — que es la mitad de la diferencia de aportaciones, no la diferencia entera, porque lo que se compensa es el exceso sobre la cuota del 50 %.
- Turno 17: vivienda y prestamo hipotecario; la skill advierte de que el reparto de cuotas no vincula a la entidad prestamista.
- Turno 18: pacto de indivision — la skill explica los articulos 400 y 404 y el cliente pacta cinco anos.
- Turnos 19-20: contribucion a los gastos (proporcional a los ingresos) y cuenta comun.
- Turno 21: deudas.
- Turno 22: dedicacion a la familia y compensacion — la skill pregunta si concurre esa situacion; no concurre, y el bloque NO se activa. Se explica igualmente que la compensacion no seria automatica.
- Turno 23: previsiones para el cese (plazo de liquidacion de seis meses).
- Turno 24: prevision sucesoria, con derivacion a `derecho-civil-testamento-planificacion`.
- Turnos 25-27: duracion, resolucion de controversias, lugar y fecha.

### Documento generado (real, no simulado)

Archivo: `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/pacto-convivencia-pareja-hecho-prueba.md`

```
CUARTO — Aportaciones desiguales a los bienes comunes.
[...] las aportaciones economicas efectivamente realizadas fueron las siguientes:
CONVIVIENTE A aporto 120.000 euros (ciento veinte mil euros) y CONVIVIENTE B aporto
60.000 euros (sesenta mil euros).
El exceso aportado por CONVIVIENTE A, cifrado en 30.000 euros (treinta mil euros),
constituye un credito a su favor frente al otro otorgante, que se hara efectivo en el
momento de la liquidacion de la comunidad sobre dicho bien [...]

SEXTO — Pacto de indivision.
Al amparo del parrafo segundo del articulo 400 del Codigo Civil [...] durante un plazo de
cinco anos [...] sin que dicho plazo pueda exceder de diez anos.
```

**Bloques ACTIVADOS:** expositivo TERCERO en su variante de pareja ya inscrita; relacion de bienes comunes; aportaciones desiguales con la variante de credito; vivienda en propiedad comun; prestamo hipotecario; pacto de indivision; cuenta comun; prevision sucesoria.
**Bloques NO ACTIVADOS:** inventario de bienes privativos; las variantes de ajuste de cuota y de liberalidad (excluidas por la eleccion del cliente); vivienda en propiedad de uno solo; vivienda arrendada; dedicacion y compensacion pactada; hijos comunes.

Resultado: **PASA**. Verificado sobre el archivo real: **cero comentarios HTML** residuales, **cero placeholders sin resolver**, y numeracion correlativa de PRIMERO a DECIMOCUARTO sin saltos ni repeticiones pese a haberse descartado seis bloques condicionales.

---

## Test 3 — Ruptura con desequilibrio economico y sin hijos

**Mensaje inicial:** "Nos separamos despues de once anos juntos en Sevilla. No tenemos hijos. Yo deje mi trabajo para llevar la casa y ayudarle en su negocio, y ahora no tengo nada. ¿Que me corresponde?"

### Recorrido del arbol
```
V1 -> escucha activa: "nos separamos"                       V1 = ruptura (sin pregunta)
V2 -> escucha activa: "en Sevilla"                          V2 = Andalucia (sin pregunta)
V3 -> escucha activa: "no tenemos hijos"                    V3 = sin hijos comunes (sin pregunta)
V4 -> escucha activa: "deje mi trabajo [...] no tengo nada" V4 = hay desequilibrio economico
Verificacion autonomica EJECUTADA
HOJA RUPTURA -> assets/pacto-ruptura-pareja-hecho.md
```

### Verificacion autonomica realmente ejecutada

`web_search` devolvio, de fuente oficial (BOE y Junta de Andalucia): **Ley 5/2002, de 16 de diciembre, de Parejas de Hecho** (BOE-A-2003-771) y **Decreto 35/2005, de 15 de febrero**, que constituye y regula el Registro de Parejas de Hecho de Andalucia; la inscripcion se practica por comparecencia personal y exige residencia habitual en un municipio andaluz de al menos uno de los miembros. Ese dato es el que sostiene la clausula de cancelacion de la inscripcion; nada mas se afirma de la normativa andaluza.

### Tratamiento de la pregunta "¿que me corresponde?" — el punto delicado del test

La skill **no** responde que le corresponde una compensacion. En el turno de la compensacion economica explica, antes de pedir ninguna cifra, que la ley no reconoce automaticamente compensacion alguna al conviviente, que las normas del matrimonio — incluida la compensacion por trabajo domestico — no se aplican por analogia, y que la unica via en defecto de pacto es el enriquecimiento injusto, que exige prueba y cuyo resultado es incierto porque el propio Tribunal Supremo la ha rechazado cuando esa prueba falta. Y concluye con lo unico que da certeza: pactarla ahora.

Enunciado literal de la correccion cuando el cliente insiste ("pero once anos son once anos, algo me tendra que dar"): la skill no valida la premisa ni la ridiculiza; explica que la duracion de la convivencia por si sola no genera derecho a compensacion, que lo que puede generarlo es haber acreditado una dedicacion que enriquecio al otro, y que por eso conviene documentar en el propio pacto en que consistio esa dedicacion.

### Momento de las preguntas
- Turno 1: linea de carga + introduccion fija; los cuatro vectores resueltos por escucha activa.
- Turno 2: Confirmacion visible, texto fijo RUPTURA (no hay regimen economico matrimonial que liquidar ni cabe convenio regulador) + ley andaluza verificada + eleccion de base documental. Al no haber hijos, **no** se emite el parrafo de advertencia sobre medidas de hijos.
- Turno 3: creacion del documento y, en la misma respuesta, anuncio de la primera seccion y primera pregunta.
- Turnos 4-9: datos de cada conviviente (confirmacion agrupada).
- Turnos 10-13: convivencia, cese, situacion registral y plazo de cancelacion de la inscripcion; se pregunta tambien si existe pacto de convivencia previo (no existe).
- Turno 14: hijos comunes — **seccion omitida por completo**, sin pregunta, al estar V3 resuelto.
- Turnos 15-17: liquidacion de bienes comunes; la skill explica que solo se liquida la comunidad de bienes y que, sin acuerdo, el desenlace es la division y eventual venta.
- Turno 18: aportaciones desiguales — no las hubo; bloque NO activado.
- Turnos 19-21: vivienda, uso, fecha de desalojo y prestamo hipotecario, con la advertencia de que el reparto no vincula a la entidad.
- Turno 22: cuentas y deudas.
- Turno 23: **compensacion economica**, con la explicacion completa descrita arriba. Se pacta una compensacion de 24.000 euros pagaderos en veinticuatro mensualidades, y la clausula se redacta expresando la causa (dedicacion al hogar y al negocio del otro, articulos 1274 y 1275 del Codigo Civil).
- Turno 24: muebles, ajuar y animales de compania.
- Turno 25: alcance de la liquidacion — la skill explica que el finiquito cierra tambien la via del enriquecimiento injusto, y por eso solo debe firmarse si la liquidacion se considera completa. El cliente lo acepta con conocimiento de causa.
- Turnos 26-27: controversias y eficacia, lugar y fecha.

### Documento generado (extracto relleno, datos sinteticos)
```
PACTO DE EXTINCION DE LA CONVIVENCIA Y LIQUIDACION DE LA PAREJA DE HECHO
> DRAFT — para revision por un abogado colegiado antes de su firma.

SEGUNDO (expositivo). Que los otorgantes no estan ni han estado unidos entre si por
vinculo matrimonial, por lo que no existe entre ellos regimen economico matrimonial
alguno que liquidar ni cabe convenio regulador.

SEPTIMO — Compensacion economica.
[...] CONVIVIENTE A dedico su tiempo y esfuerzo principalmente al cuidado del hogar
comun y a la colaboracion en el negocio de CONVIVIENTE B [...] Esa dedicacion constituye
la causa de la presente prestacion, en el sentido de los articulos 1274 y 1275 del Codigo
Civil. En su virtud, CONVIVIENTE B abonara a CONVIVIENTE A la cantidad de 24.000 euros
(veinticuatro mil euros) [...] Ambos otorgantes declaran conocer que esta compensacion NO
les viene impuesta por la ley [...] y que es este pacto el que la crea y la hace exigible.
```

**Bloques ACTIVADOS:** expositivo de pareja inscrita; cancelacion de la inscripcion; compensacion economica; vivienda; cuentas y deudas.
**Bloques NO ACTIVADOS:** pacto de convivencia previo; hijos comunes; aportaciones desiguales; animales de compania; adjudicacion sin acuerdo.

Resultado: **PASA**. La compensacion se presenta en todo momento como creada por el pacto, nunca como reconocida por la ley, y el documento lo hace constar literalmente para que no quepa equivoco al releerlo meses despues.

---

## Contra-caso — Pareja con dos hijos que pregunta por la custodia

**Mensaje inicial:** "Nos hemos separado. Tenemos dos hijos de 6 y 9 anos. Quiero saber como queda la custodia y cuanto tiene que pagarme de manutencion, y tambien repartir el piso que compramos juntos."

### Recorrido del arbol
```
V1 -> escucha activa: "nos hemos separado [...] repartir
       el piso"                                            V1 = ruptura
V2 -> PREGUNTA: comunidad autonoma
V3 -> escucha activa: "tenemos dos hijos"                  V3 = hay hijos comunes
V4 -> escucha activa: "el piso que compramos juntos"       V4 = hay bienes comunes
HOJA RUPTURA (solo para lo patrimonial)
+ DERIVACION a derecho-civil-medidas-hijos-no-matrimoniales (para custodia y alimentos)
```

### Comportamiento esperado

La skill **no intenta regular la custodia ni los alimentos, y tampoco abandona al cliente**. Hace las dos cosas a la vez:

1. En la Confirmacion visible (Punto 3) advierte ya, en el mismo turno, de que la guarda y custodia, el regimen de estancias y la pension de alimentos no pueden regularse en este pacto porque tienen cauce propio, exigen la intervencion del Ministerio Fiscal y no producen efecto sin aprobacion judicial.
2. Abre la seccion de hijos comunes **pronto, antes de entrar en lo economico**, precisamente para que el cliente no invierta turnos creyendo que la custodia se esta tratando. Activa el bloque de remision del asset — que ademas deja constancia de que ninguna clausula economica puede condicionar ni compensar los derechos de los hijos — y **no recaba ningun dato de los menores**: ni nombres, ni fechas de nacimiento, ni centro escolar.
3. Continua con la liquidacion del piso, que si es su materia.
4. Al cerrar el documento en el bucle final, y solo entonces, ofrece continuar con `derecho-civil-medidas-hijos-no-matrimoniales`.

Extracto del bloque de remision activado:
```
OCTAVO — Hijos comunes.
Las medidas relativas a los hijos comunes de los otorgantes [...] NO son objeto del
presente pacto y no quedan afectadas por el. [...] Ninguna clausula de este pacto puede
interpretarse en el sentido de condicionar, compensar o limitar los derechos de los hijos
comunes.
```

**Resultado: PASA.** La skill separa con nitidez su materia de la ajena, no deja al cliente sin respuesta sobre la parte que no le corresponde, y evita el error inverso — abandonar tambien la liquidacion patrimonial, que si puede resolver — que habria obligado al cliente a repetir todos sus datos en otra skill.

---

## Verificacion en vivo (no solo sobre el papel)

Ademas del recorrido simulado de los cuatro escenarios, se ejecuto realmente el Escenario 2 como lo haria el agente operacional, sin instalar el plugin como skill invocable de Claude Code (no esta registrado en este entorno):

1. **Fuentes estatales leidas en vivo** contra la API de legislacion consolidada del BOE, articulo por articulo, confirmando palabra por palabra el contenido de `references/fuentes-plantillas-validadas.md` y de `references/regimen-pareja-hecho-derecho-comun.md` — incluida la redaccion vigente del articulo 1323 (solo conyuges) y del 1438 (regimen de separacion del matrimonio), que es justo lo que impide usarlos como base del pacto.
2. **Verificacion autonomica ejecutada de verdad** con `web_search` para Madrid, Comunitat Valenciana y Andalucia. Los tres devolvieron ley y registro identificables en fuente oficial. En el caso de Madrid, la busqueda devolvio dos datos que ninguna reference contenia (anulacion de los articulos 4 y 5 por la STC 81/2013 y requisito de doce meses de empadronamiento desde 2023), que es exactamente la prueba de que el patron de verificacion en lanzamiento aporta algo real.
3. **Punto 4 aplicado de forma real**: `Write` en `test-local/output/pacto-convivencia-pareja-hecho-prueba.md`, `Read` de verificacion, y un ciclo de `Edit` incremental (criterio de contribucion a los gastos) con el `oldString` copiado literalmente del `Read` previo. El `Edit` aplico a la primera, sin fallo de coincidencia.

Resultado verificado sobre el archivo real, no sobre un extracto manual: cero comentarios HTML residuales, cero placeholders sin resolver, catorce clausulas correlativas sin saltos tras descartar seis bloques condicionales, y los bloques condicionales insertados como texto plano sin el envoltorio de comentario.

## Calidad de la respuesta del LLM (turnos reales generados, Escenario 3)

Se genero el texto que el agente operativo produciria en los turnos criticos del Escenario 3, para juzgar tono y claridad, no solo el mecanismo.

**Turno 1 (mensaje inicial del cliente, transcrito arriba)**

> **Skill cargada satisfactoriamente.**
>
> Vamos a preparar la documentacion que corresponda a su situacion de pareja de hecho. Debo advertirle de entrada que esta materia no tiene una ley estatal: cada comunidad autonoma la regula de forma distinta, de modo que necesitare precisar algunos datos antes de empezar.
>
> Al no haber existido matrimonio entre ustedes, no hay regimen economico matrimonial que liquidar ni cabe un convenio regulador. Lo que vamos a preparar es un pacto otorgado al amparo del articulo 1255 del Codigo Civil, que liquida la comunidad de bienes sobre lo adquirido conjuntamente conforme a los articulos 392 y siguientes. Puede consultar el texto oficial en https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763. En cuanto a su comunidad autonoma, he verificado hoy la Ley 5/2002, de 16 de diciembre, de Parejas de Hecho de Andalucia: https://www.boe.es/buscar/doc.php?id=BOE-A-2003-771
>
> ¿Que documento desea utilizar como base?
> 1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
> 2. Adjuntar su propio documento

**Turno 23 (seccion de compensacion economica)**

> Abordamos ahora si procede una compensacion economica entre ustedes.
>
> Debo ser claro con usted en este punto, porque es donde mas expectativas suelen frustrarse. La ley no reconoce automaticamente ninguna compensacion al conviviente en la ruptura: las normas del matrimonio no se aplican por analogia a la pareja de hecho, de modo que ni la pension compensatoria ni la compensacion por trabajo domestico le corresponden por el hecho de haber convivido once anos. Si existe un criterio jurisprudencial que permite reclamar por enriquecimiento injusto cuando la dedicacion de uno ha enriquecido al otro, pero exige acreditarlo con prueba solida y su resultado es incierto: el Tribunal Supremo la ha rechazado en casos en que esa prueba faltaba. Por eso lo unico que le da certeza es acordarla ahora en este pacto.
>
> Indiqueme en que consistio exactamente su dedicacion al hogar y al negocio de su pareja durante esos anos.

### Valoracion

- **Tono**: formal, "usted" sostenido, sin coloquialismos. Cumple.
- **Cita normativa**: norma completa con articulo y enlace verificable, no siglas sueltas. Cumple.
- **Directiva de invisibilidad**: ningun turno menciona vectores, hojas ni fases de la instruccion. Cumple.
- **Cero falsas expectativas**: el turno 23 es el que decide la calidad de esta skill, y dice la verdad incomoda antes de pedir dato alguno. Cumple.
- **Punto debil detectado y corregido**: al redactar el documento real del Escenario 2 se escribio una remision numerica entre clausulas ("mediante cargo mensual en la cuenta comun a que se refiere la clausula octava"). Con numeracion dinamica, descartar un bloque condicional convierte esa remision en un error silencioso que apunta a otra clausula. **Fix aplicado** en el `SKILL.md`, Punto 4: prohibidas las remisiones numericas entre clausulas; se remite siempre por el nombre de la materia.
- **Segundo punto debil detectado y corregido**: la tabla de requisitos del checklist incluye una fila de requisito adicional que, si la verificacion no devuelve ninguno, quedaria con el placeholder a la vista dentro de una tabla — donde un hueco pendiente no se lee como pendiente, sino como error. **Fix aplicado** en el `SKILL.md`, Punto 4 y seccion 2 de la HOJA INSCRIPCION: podar la tabla y eliminar la fila entera.

**Veredicto: PASA con dos correcciones aplicadas.**

## Revision UX

Hallazgos:

1. **La comunidad autonoma se pregunta en prosa, no con diecisiete opciones numeradas.** Es una desviacion deliberada del formato de alternativas numeradas, justificada en el propio `SKILL.md`: una lista de diecisiete opciones seria precisamente la mega-pregunta que el estandar prohibe, y este vector no enruta a ningun asset sino a la verificacion. Si el usuario responde con un municipio, la skill deduce la comunidad y la confirma dentro de la siguiente pregunta, sin gastar un turno.
2. **La advertencia de que no hay ley estatal va en la introduccion fija, no al final.** El cliente llega con la creencia contraria, y descubrirlo en el turno catorce, despues de haber contestado a todo, seria mucho peor que oirlo en el primero.
3. **En la rama de inscripcion, la validacion temporal se ejecuta antes de relacionar la documentacion.** Saber que faltan cuatro meses para poder presentar la solicitud cambia lo que el cliente hace hoy; descubrirlo tras haber reunido los papeles no.
4. **La seccion de hijos se abre pronto en la rama de ruptura**, antes de lo economico, para que el cliente que viene preguntando por la custodia sepa de inmediato que esa parte se trata en otro sitio, en lugar de esperar a un final que no llega.
5. **La explicacion del regimen por defecto precede siempre a la pregunta en las clausulas de negociacion.** En esta materia el regimen por defecto es casi siempre "nada", y es justo lo que el cliente no sabe: preguntarle que quiere pactar sin decirle antes que ocurre si no pacta es pedirle que decida a ciegas.
6. **Las tres salidas a la aportacion desigual se ofrecen explicadas, no como una pregunta abierta.** "¿Que quiere hacer con esa diferencia?" no es respondible por un cliente; "puede generar un credito, ajustar la cuota o considerarse una liberalidad, y esto significa cada cosa" si lo es.
7. **La compensacion nunca se enuncia en positivo antes de la advertencia.** El orden importa: primero que la ley no se la da, despues que el pacto si puede darsela. Invertirlo dejaria al cliente con la impresion contraria aunque las dos frases estuvieran presentes.

Ajustes aplicados: los dos fixes descritos en la seccion anterior (prohibicion de remisiones numericas entre clausulas y poda de filas de tabla con placeholder no resuelto). El resto de hallazgos ya estaba reflejado en el diseno del `SKILL.md`.

---

## QA en vivo por agente independiente

Ejecucion real (no simulada sobre el papel) del 03/09/2026, por un agente sin contexto previo de la skill.
Escenario: pareja en Sevilla, seis anos de convivencia, quieren inscribirse, piso comprado por los dos con la
entrada aportada casi enteramente por ella, y dos preguntas explicitas del cliente: "si nos registramos,
quedamos como casados?" y "sobre todo por si le pasa algo, que yo herede".

Rama recorrida: HOJA INSCRIPCION. Documento generado en
`/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/pareja-qa-prueba.md` con un `Write`, un `Read` de
verificacion y seis `Edit` incrementales con `oldString` copiado literalmente.

### Verificacion autonomica: ejecutada de verdad

Se lanzaron las busquedas del Punto 2.3 y se contrastaron las fuentes oficiales:

- BOE, texto consolidado de la **Ley 5/2002, de 16 de diciembre, de Parejas de Hecho** de Andalucia
  (https://www.boe.es/buscar/act.php?id=BOE-A-2003-771), desarrollada por el **Decreto 35/2005, de 15 de febrero**.
- Portal y preguntas frecuentes del **Registro de Parejas de Hecho de Andalucia** (Junta de Andalucia).

Resultado contrastado con lo que la skill afirma: **coincide, y no afirma nada de memoria**. Los requisitos
volcados al documento salieron todos de la verificacion, incluidos los dos negativos relevantes — Andalucia
**no** exige tiempo minimo de convivencia previa ni empadronamiento conjunto, solo residencia habitual de al
menos uno en un municipio andaluz (art. 2 Ley 5/2002) — y el caracter **declarativo** de la inscripcion
(art. 6: presuncion de convivencia salvo prueba en contrario). La tasa, el plazo de resolucion y el efecto del
silencio **no constan** en la fuente oficial consultada y quedaron declarados como no verificados, no inventados.

### A) Mi propio texto

**Tono.** Formal y de "usted" de forma sostenida. Extractos literales emitidos:

> "Confirmeme que ambos tienen su residencia habitual en Sevilla, y por tanto en Andalucia, para verificar la
> normativa que les resulta de aplicacion."

> "Debo corregirle un punto antes de seguir, porque de el depende lo que mas le preocupa. **Inscribirse no les
> deja como casados.**"

> "Si ella falleciera sin haber otorgado testamento, usted no recibiria nada, por larga que fuese la convivencia
> y este o no inscrita la pareja."

Ninguna mencion de vectores, hojas ni fases. Ningun preambulo del tipo "para empezar necesito saber". Ningun
dato, requisito autonomico ni cita inventados: la unica sentencia mencionable no llego a citarse, y los enlaces
son los efectivamente consultados.

**Explicacion antes de la decision.** Correcta en la clausula de negociacion que llego a ejercitarse (apartado
de efectos): se explico el regimen por defecto — "no crea ningun regimen economico", "el conviviente no hereda
sin testamento" — antes de pedir nada.

### B) El asset

- **Numeracion:** ocho apartados correlativos 1 a 8, sin saltos ni repeticiones. Los bloques condicionales del
  checklist son avisos internos a apartados, no clausulas numeradas, asi que la poda no abre huecos.
- **Remisiones numericas:** ninguna. El asset remite por materia ("el apartado anterior", "la constitucion de la
  pareja"), nunca por ordinal. Regla cumplida de verdad.
- **Placeholders:** desnudos, con nombre propio, sin texto de ayuda dentro y sin anidar. Se verifico que el
  `{{via_domicilio_comun}}` pendiente sobrevive como placeholder legible en parrafo, que es lo previsto.
- **Tras el `Write` NO hay turno "desea empezar?":** la skill encadena el anuncio de seccion y su primera
  pregunta en la misma respuesta. Cumplido.
- **Frase forzada detectada (defecto 8, corregido):** el apartado 1 encadenaba
  `{{denominacion_ley_autonomica}}` + ", de la comunidad autonoma de " + `{{comunidad_autonoma}}`, y como casi
  toda ley autonomica lleva ya el nombre de la comunidad en su denominacion oficial, el documento salio con
  *"Ley 5/2002 (...) de la Comunidad Autonoma de Andalucia (...) de la comunidad autonoma de Andalucia"*.
  Reescrito a "Por residir la pareja en la comunidad autonoma de {{comunidad_autonoma}}, a este caso le resulta
  de aplicacion {{denominacion_ley_autonomica}}...".

Leido de corrido, el checklist suena a documento real de despacho.

### C) Los tres puntos criticos

**C1 — Verificacion autonomica: APROBADO.** La skill obliga a verificar y no almacena requisitos de ninguna
comunidad. Ejecutada la verificacion de forma independiente, lo afirmado coincide punto por punto con la fuente.
Ningun requisito afirmado sin verificar.

**C2 — "quedamos como casados?": APROBADO EN EL FONDO, DEFECTUOSO EN EL MOMENTO.** El contenido es
inequivocamente correcto: no equiparacion, no gananciales, no heredero ab intestato, testamento ante notario y
derivacion a `derecho-civil-testamento-planificacion`. Pero el **texto fijo del Punto 3 no contenia esa
respuesta**: el guardrail 2 obliga a corregir el malentendido y el flujo prescrito solo lo hacia en la seccion 4
de la edicion incremental, unos diez turnos despues de que el cliente preguntara. Corregido (defecto 1).

**C3 — Compensacion economica: APROBADO.** En ningun punto se promete compensacion automatica. Se dice
expresamente que las normas del matrimonio no se aplican por analogia y que el enriquecimiento injusto exige
prueba y tiene resultado incierto. Lo que si faltaba era enlazar eso con el hecho concreto de este cliente —
entrada desigual sobre un piso titulado por mitades — y se anadio (defecto 7).

### Defectos corregidos

| # | Donde | Defecto | Correccion |
|---|---|---|---|
| 1 | `SKILL.md` Punto 3 | El texto fijo de la confirmacion no respondia al malentendido que el cliente ya habia planteado; la respuesta llegaba diez turnos tarde | Regla nueva: si el cliente ya pregunto por equiparacion, gananciales, herencia o compensacion, se le responde en ese mismo mensaje, con la derivacion a testamento |
| 2 | `SKILL.md` Punto 4 | La regla de poda de filas, leida literalmente, borra en el `Write` la tabla de requisitos entera, porque todas las celdas `{{situacion_*}}` estan pendientes por diseno hasta el Punto 5 | Regla reescrita en tres supuestos: fila que nunca se resolvera (borrar), fila pendiente de una pregunta futura (conservar con placeholder), fila con concepto real y valor no verificado (conservar declarando el hueco) |
| 3 | `SKILL.md` Punto 4 | La misma regla borraba en silencio las filas de tasa, plazo y silencio no verificadas, ocultando la laguna en el unico documento donde el cliente iba a buscarla. Ocurrio de verdad en esta ejecucion: el checklist quedo sin fila "Tasa" | Texto fijo "No consta en la fuente oficial consultada el {{fecha_verificacion_normativa_autonomica}}; confirmelo en la sede del registro" |
| 4 | `SKILL.md` Punto 5, HOJA INSCRIPCION seccion 2 | "Poda hasta dejar unicamente las filas de los requisitos verificados" se lee como borrar el requisito verificado como NO exigido, que es justo el que desmiente lo que el cliente cree | Un requisito verificado como no exigido se conserva diciendo que no se exige |
| 5 | `SKILL.md` Punto 0 | Cuando la Escucha Activa resuelve todos los vectores — habitual en la rama de inscripcion, donde V3 y V4 no se preguntan — no queda "primera pregunta" que emitir, y la deduccion municipio → comunidad se queda sin la frase donde debia confirmarse | Turno prescrito de confirmacion de residencia habitual, que sirve a la vez de confirmacion de la comunidad y de contraste de un requisito de constitucion |
| 6 | `SKILL.md` Punto 5, HOJA INSCRIPCION seccion 4 | Trampa real y no advertida: las fuentes oficiales autonomicas listan la equiparacion al matrimonio "en materia de sucesiones" refiriendose al Impuesto sobre Sucesiones y Donaciones. Volcarlo tal cual en `{{efectos_inscripcion}}` hace que el apartado 5 contradiga al 7 sobre el punto que mas importa al cliente | Instruccion de separar siempre lo fiscal de lo civil y de decir si la comunidad tiene o no derecho civil propio |
| 7 | `assets/checklist-inscripcion-registro.md` | El apartado de recomendacion del pacto no mencionaba la presuncion de cuotas iguales del art. 393 CC ni la carga de la prueba, que es exactamente el riesgo de este cliente | Parrafo nuevo sobre aportacion desigual, carga de la prueba y las tres opciones de efecto |
| 8 | `assets/checklist-inscripcion-registro.md` | Frase forzada por duplicacion del nombre de la comunidad | Apartado 1 reescrito |

### Lo que no se toco

El nucleo doctrinal de la skill es solido: la ausencia de regimen economico legal, el no heredar ab intestato,
la negativa a la analogia con el matrimonio y el tratamiento de la compensacion como algo que el pacto **crea**
y no reconoce estan bien planteados y bien situados. Los ocho defectos son de momento, de redaccion de reglas
operativas y de una trampa de fuente, no de doctrina.
