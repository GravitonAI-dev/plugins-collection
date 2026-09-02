# Test de ejecucion — skill `derecho-civil-ejecucion-titulos`

Ejecucion manual del arbol de decision sobre cuatro escenarios (3 principales + 1 contra-caso). Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: LEC (BOE-A-2000-323, Libro III), LO 1/2025 (BOE-A-2025-76), TRLC (BOE-A-2020-4859) y RD 126/2026 del SMI (BOE-A-2026-3815).
- Verificacion real efectuada el 31/08/2026: el Art. 5.3 LO 1/2025 excluye expresamente la demanda ejecutiva del requisito de MASC; los Arts. 517.2.2º, 4º, 5º, 7º, 539, 550 y 551 fueron modificados por la LO 1/2025 (efectos 03/04/2025); no existe modelo normalizado del CGPJ para la ejecucion.
- En este test la lectura online se simula como disponible -> version verificada 31/08/2026.

---

## Test 1 — Sentencia firme sin bienes conocidos

**Mensaje inicial:** "Tengo una sentencia firme desde hace 2 meses que condena a un cliente a pagarme 12.000 euros. No ha pagado nada y no se que bienes tiene. Quiero ejecutarla."

### Recorrido del arbol
```
V1 -> escucha activa: "tengo una sentencia firme...
       quiero ejecutarla"                                V1 = demanda ejecutiva inicial (sin pregunta)
V2 -> escucha activa: "sentencia firme"                   V2 = titulo judicial (sin pregunta)
V4 -> escucha activa: "no se que bienes tiene"            V4 = bienes NO conocidos (sin pregunta)
Validacion: firmeza hace 2 meses -> han transcurrido
       los 20 dias del Art. 548 y no los 5 anos del
       Art. 518 -> PROCEDE
HOJA JUDICIAL -> assets/demanda-ejecucion-titulo-judicial.md (bloques de familia DESACTIVADOS)
```
V3 no aplica (exclusivo de titulo no judicial).

### Momento de las preguntas
- Turno 1: introduccion fija; los 3 vectores ya resueltos por escucha activa -> pasa directo a la validacion de plazos (interna) y despues a la Confirmacion.
- Turno 2: Confirmacion visible (Punto 3): texto fijo JUDICIAL + aviso de que no hace falta acreditar MASC para una demanda ejecutiva (Art. 5.3 LO 1/2025) + eleccion plantilla/documento propio.
- Turnos 3-4: parte ejecutante (confirmacion agrupada), incluida la pregunta sobre postulacion en el proceso de origen (juicio ordinario, preceptivos abogado y procurador).
- Turno 5: parte ejecutada (confirmacion agrupada).
- Turno 6: el titulo ejecutivo (tipo de resolucion, organo, numero de autos, contenido de la condena, fecha de firmeza).
- Turno 7: plazos — la skill calcula por si misma que han transcurrido mas de 20 dias y menos de 5 anos; informa de ello sin pedir el dato de nuevo.
- Turno 8: cantidad reclamada (negociacion) — la skill explica el limite del 30% antes de pedir cifras; usuario aporta principal 12.000, intereses vencidos 150, acepta el 30% presupuestado (3.645).
- Turno 9: gastos extraordinarios de familia — SE OMITE (solo aplica a HOJA FAMILIA).
- Turno 10: bienes del ejecutado (negociacion) — ya resuelto que NO se conocen; la skill explica el requerimiento de manifestacion del Art. 589 y pregunta si el usuario puede aportar destinatarios concretos de investigacion (Art. 590); usuario aporta la Agencia Tributaria y la Tesoreria General de la Seguridad Social, con su razon cada uno.
- Turno 11: ampliacion automatica — SE OMITE (la deuda esta integramente vencida, no hay plazos pendientes).
- Turno 12: multas coercitivas — SE OMITE (exclusiva de HOJA FAMILIA).
- Turno 13: inaplicacion del limite de embargo — SE OMITE (exclusiva de HOJA FAMILIA).
- Turno 14: postulacion y documentos.
- Turno 15: juzgado, lugar y fecha.

### Documento generado (extracto relleno, datos sinteticos)
```
DEMANDA EJECUTIVA DE TITULO JUDICIAL — EJECUTANTE A contra EJECUTADO A
> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico definitivo.
> Version de la LEC verificada en el BOE: 31/08/2026

HECHOS
SEGUNDO. La resolucion adquirio firmeza el {{fecha, hace 2 meses}}. Han transcurrido los veinte dias posteriores a la firmeza previstos en el articulo 548 LEC, y no han transcurrido los cinco anos de caducidad del articulo 518 LEC.
CUARTO. Principal: 12.000 euros. Intereses vencidos: 150 euros. Cantidad presupuestada (30%): 3.645 euros. TOTAL: 15.795 euros.
QUINTO. Esta parte no puede designar bienes del ejecutado suficientes, por lo que se interesan las medidas de localizacion e investigacion patrimonial del OTROSI PRIMERO.

OTROSI PRIMERO: oficios a la Agencia Estatal de Administracion Tributaria y a la Tesoreria General de la Seguridad Social, con la razon de cada uno.
```
Resultado: **PASA**. Ningun bloque de familia (relacion de mensualidades, Art. 776, Art. 608) aparece en el documento.

---

## Test 2 — Escritura de prestamo notarial de 12.000 euros

**Mensaje inicial:** "Preste 12.000 euros a un conocido mediante escritura publica ante notario hace 8 meses. El plazo de devolucion vencio hace 2 meses y no me ha pagado nada. Quiero ejecutar la escritura."

### Recorrido del arbol
```
V1 -> escucha activa: "quiero ejecutar la escritura"      V1 = demanda ejecutiva inicial
V2 -> escucha activa: "escritura publica"                 V2 = titulo no judicial
V3 -> escucha activa: "escritura publica ante notario"    V3 = escritura publica notarial
V4 -> PREGUNTA: bienes conocidos -> 1 (si, un vehiculo
       y una cuenta bancaria conocida)                    V4 = bienes conocidos y suficientes
Validacion: 12.000 euros > 300 euros, liquida -> PROCEDE.
       Plazo de espera del Art. 548 NO aplica a escritura
       notarial: puede ejecutarse ya.
HOJA NO-JUDICIAL -> assets/demanda-ejecucion-titulo-no-judicial.md (bloque escritura publica)
```

### Momento de las preguntas
- Turno 1: introduccion fija + V4 (unico vector no resuelto por escucha activa, ya que V3 se dedujo del mismo mensaje sin ambiguedad).
- Turno 2: Confirmacion visible con texto fijo NO-JUDICIAL (limite de 300 euros) + advertencia MASC no exigible.
- Turnos 3-4: parte ejecutante (abogado y procurador preceptivos SIEMPRE en escritura notarial, sin preguntar el umbral de 2.000 euros que solo aplica a laudo/mediacion) y parte ejecutada.
- Turno 5: el titulo no judicial (notario, plaza, fecha de la escritura, numero de protocolo).
- Turno 6: obligacion y vencimiento (descripcion del prestamo, fecha de vencimiento hace 2 meses).
- Turno 7: liquidacion por saldo — SE OMITE (no hay pacto de liquidacion unilateral en un simple prestamo).
- Turno 8: cantidad reclamada (negociacion) — principal 12.000, intereses pactados si los hay, presupuesto del 30%.
- Turno 9: bienes del ejecutado (negociacion) — ya resuelto que SI se conocen; usuario designa el vehiculo (matricula) y la cuenta bancaria (IBAN), y la skill explica el orden del Art. 592 antes de fijarlos (dinero en cuenta antes que el vehiculo).
- Turno 10: clausulas abusivas — SE OMITE (el ejecutado no es consumidor en una relacion de prestamo entre particulares con empresario/profesional; verificado que no aplica).
- Turno 11: reserva de partidas dudosas — SE OMITE.
- Turno 12: ampliacion automatica — SE OMITE (deuda integramente vencida).
- Turno 13: juzgado (eleccion del ejecutante entre lugar de cumplimiento y lugar de bienes embargables, Art. 545.3), lugar y fecha.

### Documento generado (extracto relleno)
```
DEMANDA EJECUTIVA DE TITULO NO JUDICIAL — EJECUTANTE B contra EJECUTADO B
> DRAFT — para revision por un abogado colegiado antes de su firma.

HECHOS
PRIMERO. Se acompana como Documento nº 2 la copia de la escritura publica matriz expedida con caracter ejecutivo, otorgada ante el Notario de {{plaza}} el {{fecha}}, numero {{protocolo}}, que lleva aparejada ejecucion conforme al Art. 517.2.4º LEC.
QUINTO (bienes). Esta parte designa: 1) saldo en cuenta {{IBAN}} de {{entidad}}; 2) vehiculo {{matricula}}, por el orden del Art. 592 LEC.
```
Resultado: **PASA**. No aparece el bloque de plazo de espera de 20 dias (correctamente omitido: no aplica a escritura notarial).

---

## Test 3 — Pensiones de alimentos impagadas 6 meses

**Mensaje inicial:** "Tengo una sentencia de divorcio que fija 350 euros mensuales de alimentos para mi hija. Llevan 6 meses sin pagarme nada. Quiero ejecutar la deuda."

### Recorrido del arbol
```
V1 -> escucha activa: "quiero ejecutar la deuda"          V1 = demanda ejecutiva inicial
V2 -> PREGUNTA: tipo de titulo -> 3                       V2 = pensiones o medidas de familia
V4 -> PREGUNTA: bienes conocidos -> 2 (no)                V4 = bienes NO conocidos
Validacion: se aplica de forma conservadora el plazo
       de 20 dias del Art. 548 (verificado que la
       sentencia es firme desde hace mas de 6 meses,
       plazo cumplido de sobra); no hay gastos
       extraordinarios que separar en este caso.
HOJA FAMILIA -> assets/demanda-ejecucion-titulo-judicial.md (bloques de familia ACTIVADOS)
```

### Momento de las preguntas
- Turno 1: introduccion fija + V2 (la skill no asume "familia" solo por mencionar "sentencia de divorcio" en el contexto de alimentos, ya que tambien podria tratarse de una compensatoria o de gananciales: pregunta para confirmar el tipo exacto).
- Turno 2: V4.
- Turno 3: Confirmacion visible con texto fijo FAMILIA (Art. 776 LEC) + advertencia MASC no exigible.
- Turnos 4-5: parte ejecutante y parte ejecutada (confirmacion agrupada).
- Turno 6: el titulo ejecutivo (sentencia de divorcio, juzgado, fecha de firmeza).
- Turno 7: plazos.
- Turno 8: cantidad reclamada (negociacion) — la skill sustituye la pregunta de principal por la relacion mensualidad a mensualidad: 6 meses x 350 euros = 2.100 euros; pregunta si el titulo prevee actualizacion (usuario dice que no) y por tanto NO se aplica ninguna.
- Turno 9: gastos extraordinarios de familia (condicional) — usuario dice que no hay ninguno pendiente: seccion omitida sin mas preguntas.
- Turno 10: bienes del ejecutado (negociacion) — no conocidos; se activa el OTROSI de manifestacion de bienes.
- Turno 11: ampliacion automatica (negociacion) — la skill explica que las pensiones son de tracto sucesivo y recomienda pedir la ampliacion automatica del Art. 578 para no tener que volver a demandar cada mes; usuario acepta.
- Turno 12: multas coercitivas (negociacion) — usuario confirma que el impago ha sido reiterado (6 meses seguidos): se incluye el OTROSI.
- Turno 13: inaplicacion del limite de embargo — al ser alimentos, la skill explica que el Art. 608 excluye por ministerio de la ley el Art. 607 y que sera el tribunal quien fije la cantidad embargable; no requiere acreditacion adicional (a diferencia de la compensatoria).
- Turno 14: postulacion y documentos, juzgado (el que dicto la sentencia de divorcio, sin sumision posible), lugar y fecha.

### Documento generado (extracto relleno)
```
DEMANDA EJECUTIVA DE TITULO JUDICIAL (especialidades del Art. 776 LEC) — PROGENITOR G contra PROGENITOR H
> DRAFT — para revision por un abogado colegiado antes de su firma.

HECHOS
CUARTO. El principal se compone de las siguientes mensualidades vencidas e impagadas de alimentos, fijadas en 350 euros mensuales: marzo 2026 (350), abril 2026 (350), mayo 2026 (350), junio 2026 (350), julio 2026 (350), agosto 2026 (350). Total: 2.100 euros.

FUNDAMENTOS DE DERECHO
X. Resulta de aplicacion el Art. 776 LEC [...] entre ellas la imposicion de multas coercitivas al obligado que incumple de manera reiterada.
XI. Conforme al Art. 608 LEC, los limites del Art. 607 no son de aplicacion a la ejecucion de alimentos, correspondiendo al tribunal fijar la cantidad embargable.

OTROSI SEGUNDO: ampliacion automatica del Art. 578 LEC.
OTROSI TERCERO: multas coercitivas del Art. 776.1ª LEC.
```
Resultado: **PASA**. Informativamente, como el impago alcanza 6 meses consecutivos (mas de los "dos meses consecutivos o cuatro no consecutivos" del Art. 227 CP), la skill anade una advertencia de posible relevancia penal y ofrece escalacion, sin redactar denuncia ni afirmar la existencia de delito.

---

## Contra-caso — Sentencia de hace 6 anos

**Mensaje inicial:** "Tengo una sentencia firme de hace 6 anos que me reconoce 8.000 euros. Nunca la ejecute. Ahora quiero hacerlo."

### Recorrido del arbol
```
V1 -> escucha activa: "quiero ejecutarla"                 V1 = demanda ejecutiva inicial
V2 -> escucha activa: "sentencia firme"                   V2 = titulo judicial
Validacion: firmeza hace 6 anos > 5 anos del Art. 518
       LEC -> CADUCADA -> DETENER
```

### Comportamiento esperado
La skill no pregunta V4 ni pasa a la Confirmacion: en cuanto calcula que han transcurrido mas de cinco anos desde la firmeza, aplica el guardrail 3 (caducidad) y detiene el flujo en el mismo turno, informando de que la accion ejecutiva de ese titulo ha caducado conforme al Art. 518 LEC, que el plazo es de caducidad (no se interrumpe por gestiones extrajudiciales) y ofreciendo escalacion. No se crea ningun documento.

**Resultado: PASA.** La caducidad se detecta antes de la Confirmacion y antes de pedir ningun dato adicional, evitando que el usuario invierta turnos en un escrito que el juzgado no admitiria.

---

## Verificacion en vivo (no solo sobre el papel)

Ademas del recorrido simulado de los 4 escenarios, se ejecuto realmente el Escenario 1 como lo haria el agente operacional, sin instalar el plugin como skill invocable de Claude Code (no esta registrado en este entorno): se leyeron los articulos 517, 518, 539, 548 y 608 LEC en vivo contra la API de legislacion consolidada del BOE (`https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2000-323/texto/bloque/a{articulo}`, cabecera `Accept: application/xml`), confirmando palabra por palabra el contenido de `references/lec-titulos-ejecutivos-y-plazos.md` y `references/fuentes-plantillas-validadas.md` (incluida la fecha de vigencia de la LO 1/2025, 03/04/2025, en los arts. 517, 539 y 608). Despues se aplico el Punto 4 (creacion del documento base) de forma real con `Write` en `test-local/output/demanda-ejecucion-titulo-judicial-prueba.md`, `Read` de verificacion, y dos ciclos de `Edit` incremental (cantidad, Turno 8) con el `oldString` copiado literalmente del `Read` previo.

Resultado verificado en el archivo real (no en un extracto manual): cero comentarios HTML residuales, bloques de familia ausentes por completo (no es HOJA FAMILIA), el OTROSI SEGUNDO de ampliacion automatica correctamente omitido (deuda integramente vencida), el bloque de "bienes no conocidos" insertado como texto plano sin el envoltorio de comentario, y los `Edit` aplicados a la primera sin fallos de coincidencia de texto. Los placeholders que persisten tras el `Edit` (juzgado, numero de autos, fecha de sentencia, postulacion, destinatarios de investigacion, documentos, lugar y fecha) son exactamente los datos que el SKILL.md deja para turnos posteriores del Punto 5, no datos inventados ni omitidos por error. **PASA.**

## Verificacion en vivo + calidad LLM (Escenario 1, generado por el team-lead)

Ademas de la verificacion mecanica ya registrada arriba (BOE en vivo + Write/Read/Edit reales), se genero el texto real que el agente operativo produciria en los primeros turnos, jugando el papel del LLM gobernado por el `SKILL.md`, para juzgar tono y claridad — no solo que el mecanismo funcione.

### Turnos reales generados

**Turno 1 (mensaje inicial del cliente: "Tengo una sentencia firme desde hace 2 meses que condena a un cliente a pagarme 12.000 euros. No ha pagado nada y no se que bienes tiene. Quiero ejecutarla.")**

> Vamos a preparar el escrito que corresponda para hacer efectivo su derecho por la via de la ejecucion forzosa. Para determinarlo correctamente, es necesario precisar antes algunos datos.
>
> A su caso corresponde la ejecucion de un titulo judicial, conforme a los articulos 517.2 y 549 de la Ley 1/2000, de Enjuiciamiento Civil. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323. No es necesario acreditar el intento de una solucion extrajudicial previa para presentar una demanda ejecutiva (articulo 5.3 de la Ley Organica 1/2025).
>
> ¿Que documento desea utilizar como base?
> 1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
> 2. Adjuntar su propio documento

**Turno 2 (cliente: "1")**

> He creado el documento en `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/demanda-ejecucion-titulo-judicial-prueba.md`. ¿Desea que empecemos a completar los datos del escrito?
>
> Comenzamos por la identificacion de la parte ejecutante. Indique el nombre completo o la razon social de quien va a ejecutar la sentencia.

**Turno 3 (cliente: "si, EJECUTANTE A")**

> Indique su NIF o CIF.

**Turno 4 (cliente: "00000000-T")**

> Indique el domicilio a efectos de notificaciones.

**Turno 5 (cliente: "Calle Ejemplo 1, Ciudad Ejemplo")**

> En el procedimiento de origen del titulo, ¿eran preceptivos abogado y procurador, o se trata de un decreto de monitorio sin oposicion o de un laudo o acuerdo de mediacion por una cantidad que no supera 2.000 euros?

**Turno 6 (cliente: "fue un juicio ordinario, asi que si eran preceptivos")**

> Indique el nombre del procurador y del letrado que le representan.
>
> [vista previa] Parte ejecutante: EJECUTANTE A, NIF 00000000-T, domicilio en Calle Ejemplo 1, Ciudad Ejemplo, representado por procurador y letrado conforme a la regla general del articulo 539.1 LEC. ¿Confirmamos estos datos?

### A) Calidad de la respuesta del LLM

- **Tono**: formal, "usted" sostenido en los 6 turnos, sin coloquialismos ("indique" en vez de "dime", "¿desea...?" en vez de "¿quieres...?"). Cumple.
- **Claridad de la cita normativa**: la Confirmacion del Turno 1 dice qué norma aplica y por qué, con enlace verificable — no es una cita vacía. Cumple.
- **Directiva de invisibilidad**: ningún turno menciona "V1", "V2", "hoja", "vector" ni fases de la instrucción ("ahora voy a"). Cumple.
- **Cero datos inventados**: el nombre del procurador/letrado se pregunta, no se asume; la postulación se pregunta explícitamente en vez de asumir la regla general. Cumple.
- **Punto débil real detectado ahora**: el Turno 6 mezcla en un mismo mensaje la pregunta de un dato nuevo (procurador/letrado) con la vista previa y confirmación agrupada de los datos YA completados (nombre/NIF/domicilio). Releyendo el SKILL.md, la sección 5 dice que la confirmación agrupada llega "al completar el ultimo dato" de la parte — y el procurador/letrado es justo ese último sub-apartado (d). El texto generado es correcto, pero linda con la ambigüedad: un operador menos cuidadoso podría pedir el procurador/letrado y mostrar la vista previa en el MISMO turno sin esperar la respuesta, mezclando pregunta y confirmación antes de tener el dato. **Fix aplicado**: aclarado en el SKILL.md, sección 5, primer párrafo, que la vista previa y confirmación agrupada se emiten en el turno SIGUIENTE a la respuesta del último sub-apartado, nunca en el mismo turno en que se pregunta ese último dato.

### B) El asset visto desde el LLM que lo rellena

- Los placeholders usados hasta ahora (`{{denominacion_juzgado}}`, `{{partido_judicial}}`, `{{numero_autos_origen}}`, `{{nombre_procurador}}`, `{{nombre_letrado}}`) son inequívocos, todos con nombre propio (ya verificado el 31/08/2026 que no hay ninguno con texto de ayuda embebido en esta skill).
- El fundamento de postulación (`{{fundamento_postulacion}}`) exige que el operador redacte una frase completa a partir de la respuesta del cliente ("si eran preceptivos" -> "Son preceptivos abogado y procurador conforme a la regla general del articulo 539.1 LEC, por no concurrir ninguna de las excepciones de dicho precepto."), lo cual es correcto pero implica que el asset delega en el LLM una redacción no trivial en vez de ofrecer 2-3 variantes fijas como hacen otros fundamentos de la misma plantilla (compárese con el Fundamento III, de redacción fija). Es una asimetría menor, no un defecto: queda anotada para una futura iteración si se detectan redacciones inconsistentes entre operadores.
- El documento, leído de corrido con los datos ya insertados, suena a escrito procesal real (ver extracto del Test 1 más arriba): no hay artefactos de plantilla mal encajada.

**Veredicto: PASA con una corrección aplicada** (orden de la confirmación agrupada, sección 5).

## Revision UX

Hallazgos:
1. Preguntar V2 explicitamente en el Test 3 (en vez de asumir "familia" por la sola mencion de "sentencia de divorcio") evita clasificar mal un titulo que podria referirse a gananciales o a otra medida no alimenticia; el coste de la pregunta es bajo (una unica pregunta) frente al riesgo de activar el asset equivocado.
2. La validacion de caducidad (contra-caso) se ejecuta ANTES de cualquier pregunta de relleno de datos, no al final del proceso: el usuario recibe la mala noticia en el primer o segundo turno, no despues de haber invertido tiempo completando un escrito inutil.
3. Separar la pregunta de postulacion segun el tipo de titulo (Test 1: origen del proceso; Test 2: preceptivos siempre en escritura notarial, sin preguntar; Test 3: igual que Test 1) evita hacer una pregunta irrelevante cuando la respuesta es fija por ley (escritura notarial).
4. En el Test 3, activar automaticamente la sugerencia de la ampliacion automatica del Art. 578 para pensiones (en vez de esperar a que el usuario la pida) aporta valor practico real y evita que tenga que volver a demandar cada mes.
5. La advertencia de relevancia penal (Art. 227 CP) se ofrece de forma puramente informativa y con derivacion a especialista, nunca como un tramite que la propia skill inicia: evita extralimitarse fuera del alcance civil del plugin.

Ajustes aplicados: ninguno adicional a los ya reflejados en el SKILL.md (pregunta explicita V2 para el subtipo de familia, orden "validacion de caducidad antes de cualquier pregunta de relleno", y sugerencia proactiva de la ampliacion automatica en pensiones).
