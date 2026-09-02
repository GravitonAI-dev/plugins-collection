# Test de ejecucion — skill `derecho-civil-reclamacion-cantidad`

Ejecucion manual del arbol de decision sobre tres escenarios. Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: BOE, Ley 1/2000 (LEC), texto consolidado (BOE-A-2000-323) y LO 1/2025 (BOE-A-2025-76); modelos normalizados del CGPJ (monitorio y juicio verbal).
- Verificacion real efectuada el 31/08/2026 al construir la skill: LEC consolidada con ultima modificacion 28/02/2025; umbral verbal/ordinario de 15.000 euros vigente (Arts. 249.2 y 250.2, RDL 6/2023, no modificado por LO 1/2025); modelos del CGPJ de juicio verbal actualizados a 01/08/2025.
- En este test la lectura online se simula como disponible -> `fecha_verificacion_lec` = 28/02/2025 (verificado 31/08/2026).

---

## Test 1 — Deuda documentada de 3.000 euros -> MONITORIO

**Mensaje inicial del usuario:** "Quiero reclamar 3.000 euros de dos facturas impagadas a un cliente. Tengo las facturas y el contrato de servicios. Vencieron en marzo."

### Recorrido del arbol
```
N0 (V1) -> escucha activa: "quiero reclamar"            V1 = acreedor (sin pregunta)
N1 (V2) -> escucha activa: sin mencion de juzgado        V2 = sin iniciar (sin pregunta)*
N2 (V3) -> escucha activa: "tengo facturas y contrato"   V3 = si (sin pregunta)
N3 (V4) -> escucha activa: "vencieron en marzo",
           importe fijo 3.000                             V4 = vencida y liquida (sin pregunta)
N4 (V6) -> PREGUNTA: "Se ha intentado ya una solucion
           previa..." -> respuesta: 2 (no)                V6 = no
HOJA -> MONITORIO + burofax previo
```
*Ajuste UX aplicado (ver Revision UX, hallazgo 1): V2 se infiere como "sin iniciar" salvo indicio en contra; no se pregunta en frio.

Ruta: `V1-acreedor -> V2-sin-iniciar -> V3-si -> V4-liquida -> V6-no -> HOJA MONITORIO (+burofax)`
Assets cargados: `assets/burofax-masc-reclamacion.md` (primero) y `assets/peticion-monitorio.md`.

### Momento de las preguntas
- Turno 1 (respuesta al mensaje inicial): introduccion fija + UNICA pregunta pendiente de clasificacion (V6). V1-V4 no se re-preguntan: resueltos por escucha activa. Correcto: una pregunta por turno.
- Turno 2: confirmacion visible (Punto 3): via monitorio con cita del Art. 812 y enlace BOE + anuncio del burofax previo + eleccion plantilla/documento propio.
- Turnos 3-6: datos del acreedor uno a uno (nombre, NIF, domicilio; persona fisica -> no se pide representante) con UNA sola vista previa y confirmacion agrupada al final. Sin `Edit` intermedios.
- Turnos 7-9: datos del deudor uno a uno + confirmacion agrupada.
- Turno 10: seccion de origen y prueba (negociacion): la skill explica los documentos del Art. 812 antes de pedir la relacion. La cuantia (3.000) y el vencimiento (marzo) NO se re-preguntan: ya constaban del mensaje inicial.
- Turno 11: intereses (negociacion): la skill explica interes legal (Arts. 1100 y 1108 CC) vs pactado antes de pedir la decision; costas explicadas (Art. 394).
- Turno 12: partido judicial del deudor (Art. 813; se valida que no se pacta otro fuero).
- Turnos 13-14: terminos del burofax (plazo de pago, IBAN, via de contacto) y lugar/fecha.

### Documento generado (extracto relleno, datos sinteticos)
```
PETICION INICIAL DE PROCESO MONITORIO — ACREEDOR A contra DEUDOR A
> DRAFT — para revision por un abogado colegiado antes de su firma.
> Version de la LEC verificada en el BOE: 28/02/2025

AL JUZGADO DE PRIMERA INSTANCIA DE CIUDAD EJEMPLO

DATOS DEL PETICIONARIO (ACREEDOR)
Nombre / Razon social: ACREEDOR A
NIF / CIF: 00000000-T
Domicilio a efectos de notificaciones: Calle Ejemplo 1, Ciudad Ejemplo

DATOS DEL DEUDOR
Nombre / Razon social: DEUDOR A
NIF / CIF: 11111111-H
Domicilio o lugar donde puede ser hallado: Calle Ejemplo 2, Ciudad Ejemplo

HECHOS
PRIMERO — Origen de la deuda. Contrato de servicios de 10/01/2026 y facturas nº 1 y nº 2.
SEGUNDO — Cuantia. El importe adeudado asciende a 3.000 euros de principal.
TERCERO — Vencimiento y exigibilidad. La deuda vencio el 31/03/2026...
CUARTO — Documentos... Documento nº 1 - Contrato de servicios; Documento nº 2 - Factura nº 1; Documento nº 3 - Factura nº 2.
QUINTO — Intento de solucion previa. ...burofax de fecha {{fecha_burofax}}...
```
Verificaciones negativas: el documento NO contiene bloques de otras ramas (sin encabezado de procurador — no preceptivo y no solicitado —, sin bloque del Art. 818.2, sin alegaciones de oposicion). Los comentarios HTML condicionales del asset no aparecen en el documento escrito. El bloque QUINTO (MASC) se inserto sin el envoltorio de comentario porque la hoja incluye burofax.

Resultado: **PASA**.

---

## Test 2 — Deuda discutida de 8.000 euros -> JUICIO VERBAL

**Mensaje inicial del usuario:** "Un cliente me debe 8.000 euros de una obra, pero dice que la obra tiene defectos y que no piensa pagar. No le he mandado nada por escrito todavia."

### Recorrido del arbol
```
N0 (V1) -> escucha activa                                 V1 = acreedor
N1 (V2) -> escucha activa (sin procedimiento previo)      V2 = sin iniciar
N2 (V3) -> PREGUNTA V3: documentos -> respuesta: 1 (si)   V3 = si
N3 (V4) -> escucha activa: "dice que no piensa pagar"
           -> importe discutido                            V4 = discutida (sin pregunta)
N4 (V5) -> cuantia 8.000 ya dada -> <= 15.000              VERBAL (sin sub-pregunta
           (no se pregunta arrendamiento: solo se          de arrendamiento)
           formula si la cuantia supera 15.000)
N5 (V6) -> escucha activa: "no le he mandado nada"         V6 = no (sin pregunta)
HOJA -> VERBAL + burofax previo
```
Ruta: `V1-acreedor -> V2-sin-iniciar -> V3-si -> V4-discutida -> V5-8000 -> V6-no -> HOJA VERBAL (+burofax)`
Assets cargados: `assets/burofax-masc-reclamacion.md` (primero) y `assets/demanda-juicio-verbal.md`.
Clave de la rama: aunque hay documentos (V3 = si), la deuda esta CONTROVERTIDA (V4), por lo que NO se enruta a monitorio: la skill respeta el guardrail 3 y va al declarativo por cuantia.

### Momento de las preguntas
- Turno 1: introduccion fija + pregunta V3 (unica de clasificacion pendiente; V4 y V6 se resolvieron del propio mensaje). Una pregunta por turno.
- Turno 2: confirmacion visible: juicio verbal por cuantia <= 15.000 euros (Art. 250 LEC, enlace BOE) + anuncio del burofax previo (Arts. 264 y 403.2) + advertencia de que la demanda no debe presentarse hasta poder acreditar el intento de MASC + eleccion de plantilla.
- Validacion de postulacion: 8.000 > 2.000 -> la skill informa de que son preceptivos abogado y procurador y los pide en la seccion 1 (sub-apartado e).
- Resto del flujo igual que el Test 1: partes con confirmacion agrupada, origen/prueba y luego cuantia-intereses-costas como negociacion, fuero de los Arts. 50-51 LEC, terminos del burofax, lugar y fecha. La cuantia (8.000) no se re-pregunta en ningun turno.

### Documento generado (extracto relleno, datos sinteticos)
```
DEMANDA DE JUICIO VERBAL (RECLAMACION DE CANTIDAD) — ACREEDOR B contra DEUDOR B
> DRAFT — para revision por un abogado colegiado antes de su firma.
> Version de la LEC verificada en el BOE: 28/02/2025

AL JUZGADO DE PRIMERA INSTANCIA DE CIUDAD EJEMPLO
PROCURADOR EJEMPLO, Procurador de los Tribunales, en nombre y representacion de ACREEDOR B...
bajo la direccion del Letrado LETRADO EJEMPLO...

HECHOS
PRIMERO — Relacion entre las partes y origen de la deuda. Contrato de obra de 15/02/2026...
SEGUNDO — Cuantia reclamada. El importe adeudado asciende a 8.000 euros de principal.
CUARTO — Intento de solucion previa (MASC). ...mediante burofax de fecha {{fecha_masc}}...

FUNDAMENTOS DE DERECHO
II. Procedimiento. ...juicio verbal, conforme al articulo 250.2 de la LEC.
IV. ...Se comparece con Procurador y Abogado conforme a los articulos 23 y 31 de la LEC.
```
Verificaciones negativas: NO se cargo `peticion-monitorio.md` pese a existir documentos; el documento NO contiene el bloque "sin abogado ni procurador" (cuantia > 2.000) ni referencias al Art. 812, al Art. 818.2 ni a rentas de arrendamiento (Art. 250.1.1º). Cero comentarios HTML en el documento escrito.

Resultado: **PASA**.

---

## Test 3 — Deuda discutida de 40.000 euros -> JUICIO ORDINARIO

**Mensaje inicial del usuario:** "Mi empresa reclama 40.000 euros a un proveedor por un anticipo que no ha devuelto tras resolver el contrato. El proveedor sostiene que el anticipo no es devolvible. Ya le enviamos un burofax en junio y tenemos el acuse."

### Recorrido del arbol
```
N0 (V1) -> escucha activa                                 V1 = acreedor
N1 (V2) -> escucha activa (sin procedimiento previo)      V2 = sin iniciar
N2 (V3) -> PREGUNTA V3: documentos -> respuesta: 1 (si)   V3 = si
N3 (V4) -> escucha activa: "sostiene que no es
           devolvible" -> importe discutido                V4 = discutida (sin pregunta)
N4 (V5) -> cuantia 40.000 > 15.000 -> sub-pregunta de
           arrendamiento -> respuesta: 2 (no)              V5 = ordinario
N5 (V6) -> escucha activa: "burofax en junio con acuse"    V6 = si (sin pregunta)
HOJA -> ORDINARIO (sin burofax adicional)
```
Ruta: `V1-acreedor -> V2-sin-iniciar -> V3-si -> V4-discutida -> V5-40000-no-arrendamiento -> V6-si -> HOJA ORDINARIO`
Asset cargado: `assets/demanda-juicio-ordinario.md`. NO se genera burofax (MASC ya acreditado).

### Momento de las preguntas
- Turno 1: introduccion fija + pregunta V3. Una pregunta.
- Turno 2: sub-pregunta de arrendamiento de V5 (aplica: cuantia > 15.000 y el origen "anticipo de contrato con proveedor" no lo descarta formalmente). Una pregunta.
- Turno 3: confirmacion visible: juicio ordinario por cuantia > 15.000 euros (Art. 249.2 LEC, enlace BOE); NO se anuncia burofax (V6 = si). Eleccion de plantilla.
- Seccion 1 con sub-apartado d (representante: la actora es persona juridica -> se piden nombre, NIF y cargo del representante sin re-preguntar la naturaleza, resuelta por escucha activa "mi empresa") y sub-apartado e (procurador y letrado, preceptivos).
- Seccion de origen/prueba: se registra el burofax de junio como documento acreditativo del MASC (hecho especifico y fundamento V con el bloque de MASC intentado); no se pregunta de nuevo si hubo intento.
- Resto igual: cuantia/intereses/costas como negociacion, fuero, lugar y fecha.

### Documento generado (extracto relleno, datos sinteticos)
```
DEMANDA DE JUICIO ORDINARIO (RECLAMACION DE CANTIDAD) — ACREEDOR C, S.L. contra DEUDOR C, S.A.
> DRAFT — para revision por un abogado colegiado antes de su firma.
> Version de la LEC verificada en el BOE: 28/02/2025

AL JUZGADO DE PRIMERA INSTANCIA DE CIUDAD EJEMPLO
PROCURADOR EJEMPLO, Procurador de los Tribunales, en nombre y representacion de ACREEDOR C, S.L. ...

HECHOS
PRIMERO — Relacion entre las partes y origen de la deuda. Contrato de suministro de 05/01/2026,
resuelto el 30/04/2026, con anticipo de 40.000 euros pendiente de devolucion...
HECHO — Intento de solucion previa. ...mediante burofax de fecha 15/06/2026, conforme a los
articulos 403.2 y 264 de la LEC, sin acuerdo...

FUNDAMENTOS DE DERECHO
II. Procedimiento. ...juicio ordinario, conforme al articulo 249.2 de la LEC, por exceder la
cuantia de 15.000 euros.
V. Requisito de procedibilidad (MASC). Se ha intentado la actividad negociadora previa...
```
Verificaciones negativas: NO se cargo el asset de burofax; el documento NO contiene el bloque del Art. 818.2 (no hay monitorio precedente) ni el bloque alternativo del fundamento V para demandas que traen causa de un monitorio. Cero comentarios HTML en el documento escrito.

Resultado: **PASA**.

---

## Resumen del test

| Test | Ruta | Hoja / assets | Validaciones clave | Resultado |
|---|---|---|---|---|
| 1 | V3-si / V4-liquida / V6-no | MONITORIO + burofax | Art. 812, competencia 813, MASC conservador | PASA |
| 2 | V3-si / V4-discutida / <=15.000 / V6-no | VERBAL + burofax | Guardrail 3 (controvertida -> declarativo), postulacion >2.000 | PASA |
| 3 | V3-si / V4-discutida / >15.000 / V6-si | ORDINARIO | Art. 249.2, MASC ya acreditado, persona juridica | PASA |

Ramas no cubiertas por estos tres escenarios (pendientes de un test futuro): HOJA OPOSICION (V1 = deudor), HOJA ORDINARIO-818 (monitorio propio con oposicion > 15.000), parada por oposicion <= 15.000 (Art. 818.1) y parada por deuda no vencida.

---

## Revision UX

### Hallazgos y ajustes aplicados a la skill

1. **V2 preguntado en frio resultaba antinatural.** En el borrador inicial, un usuario que decia "quiero reclamar una deuda" recibia como segunda pregunta "¿Ya se presento una peticion de monitorio...?", desconcertante para el caso mayoritario (nada iniciado). Ajuste aplicado: V2 se resuelve por escucha activa con valor por defecto "sin iniciar" salvo indicio en contra (menciones a juzgado, autos, requerimiento u oposicion); la pregunta literal de V2 se conserva solo para cuando el mensaje sugiere un procedimiento previo pero no queda claro su estado.
2. **La sub-pregunta de arrendamiento solo se formula cuando cambia el resultado.** Si la cuantia no excede de 15.000 euros la via ya es verbal, y preguntar por el arrendamiento no altera nada: la skill la limita al caso > 15.000 (donde el Art. 250.1.1º puede reconducir a verbal). Ahorra un turno en la rama mas comun.
3. **Riesgo de presentar la demanda sin poder acreditar el MASC.** En las hojas VERBAL/ORDINARIO con burofax previo, el justificante del burofax aun no existe cuando se redacta la demanda. Ajuste aplicado: la confirmacion del Punto 3 y la creacion del Punto 4 advierten expresamente de que la demanda no debe presentarse hasta disponer del justificante del burofax (y de un plazo razonable de respuesta), y los campos `{{fecha_masc}}`/`{{fecha_burofax}}` quedan como placeholders hasta entonces.
4. **Lenguaje funcional en las preguntas de clasificacion.** Las opciones evitan tecnicismos innecesarios ("¿Esta vencido y es una cifra fija o calculable...?" en lugar de "¿la deuda es liquida y exigible?"). El unico termino procesal que aparece es "proceso monitorio" en V1, porque es el que figura literalmente en el requerimiento que el cliente tiene delante.
5. **Numero de turnos razonable.** Con escucha activa, el caso mayoritario (Test 1) resuelve la clasificacion en 1 turno de pregunta y completa el documento en unos 14 turnos, con las dos partes agrupadas en una sola confirmacion cada una. Sin la confirmacion agrupada serian 6 confirmaciones adicionales.
6. **Orden natural de las secciones.** Partes -> origen/prueba -> cuantia/intereses -> juzgado -> burofax -> lugar/fecha refleja el orden del propio escrito y deja las decisiones "de negociacion" (intereses, costas, terminos del burofax) despues de los datos objetivos, cuando el usuario ya tiene contexto.

---

## Verificacion en vivo + calidad LLM

Ejecucion real (no simulada sobre el papel): me puse en el papel del LLM operativo gobernado por `SKILL.md` y sostuve la conversacion completa, turno a turno, generando yo mismo el texto que vería el cliente y aplicando `Write`/`Read`/`Edit` reales sobre archivos en disco. Escenario: "Quiero reclamar 3.000 euros de dos facturas impagadas a un cliente. Tengo las facturas y el contrato de servicios. Vencieron en marzo. No he intentado nada previo con él." Datos sinteticos: ACREEDOR A (NIF 00000000-T) contra DEUDOR A (NIF 11111111-H). Documentos generados: `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/reclamacion-cantidad-qa-prueba.md` (peticion de monitorio) y `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/burofax-qa-prueba.md` (burofax MASC previo, generado primero por V6 = No).

### Transcripcion real (extractos literales de mi propio texto)

**Turno 1 — clasificacion resuelta sin preguntas.** Los seis vectores (V1 acreedor, V2 sin iniciar por defecto, V3 documentos si, V4 vencida y liquida, V6 MASC no intentado) quedaron resueltos por escucha activa desde el primer mensaje, sin indicios de procedimiento previo. No hubo ninguna pregunta de clasificacion. Mi primera respuesta visible fue directamente la Confirmacion del Punto 3:

> "A su caso corresponde el proceso monitorio, regulado en los artículos 812 y siguientes de la Ley 1/2000, de Enjuiciamiento Civil, al tratarse de una deuda dineraria, líquida, vencida y exigible acreditada documentalmente, cualquiera que sea su cuantía. Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323
>
> Con carácter previo se preparará un burofax de requerimiento de pago, que acredita el intento de solución extrajudicial exigido por la Ley Orgánica 1/2025 (artículos 264 y 403.2 de la Ley de Enjuiciamiento Civil). Tenga en cuenta que la demanda no debe presentarse hasta disponer del justificante del envío del burofax y haber dejado un plazo razonable de respuesta.
>
> ¿Qué documento desea utilizar como base?
> 1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
> 2. Adjuntar su propio documento"

**Turno 3 — anuncio de seccion + pregunta, sin re-preguntar el origen ya dado.** Tras crear ambos documentos, en la seccion "Origen de la deuda" apliqué el ajuste que introduje en esta misma revision (ver Defecto 2 mas abajo): en vez de "describa el origen de la deuda" en bruto, mi texto fue:

> "Abordamos ahora el origen de la deuda y su acreditación documental. Para el proceso monitorio sirven como prueba, conforme al artículo 812 de la LEC, los documentos firmados por el deudor o las facturas, albaranes y certificaciones habituales del tráfico entre las partes. Según nos indica, dispone del contrato de servicios y de las dos facturas: confírmeme el número e importe de cada factura, la fecha exacta de su vencimiento y la fecha del contrato, y las incorporamos numeradas como documentos del hecho cuarto."

**Turno sobre consumidor (ajuste aplicado en esta revision, ver Defecto 4):**

> "¿El deudor contrató como consumidor particular o actuaba también como empresario o profesional?"

(Respuesta simulada: cliente profesional, no consumidor — evita invocar sin base el control de oficio del art. 815.4, que solo aplica a deudores consumidores.)

**Fragmento del documento final (extracto literal del archivo, no resumido):**

```
PRIMERO — Origen de la deuda.
La deuda trae causa del contrato de prestacion de servicios de consultoria suscrito
entre las partes el 10 de enero de 2026, en cuya virtud el peticionario presto al
deudor los servicios facturados en los documentos nº 2 y nº 3 relacionados en el
hecho cuarto, sin que el deudor haya abonado su importe.

TERCERO — Vencimiento y exigibilidad.
La deuda vencio en la fecha o fechas que constan en los documentos relacionados en
el hecho cuarto (5 de marzo de 2026 y 20 de marzo de 2026), y es liquida, determinada,
vencida y exigible, sin que el deudor la haya satisfecho pese a haber sido requerido
de pago.

CUARTO — Documentos que acreditan la deuda.
1. Contrato de prestacion de servicios de consultoria, de fecha 10 de enero de 2026.
2. Factura nº 1, por importe de 1.500 euros, con vencimiento el 5 de marzo de 2026.
3. Factura nº 2, por importe de 1.500 euros, con vencimiento el 20 de marzo de 2026.
```

### A) Calidad de la respuesta del LLM

- **Tono.** Se mantuvo "usted" y registro de despacho en todos los turnos ("confírmeme", "según nos indica", "abordamos ahora"). No detecté coloquialismos ni muletillas. Cumple.
- **Explicacion antes de decidir (clausulas de negociacion).** Antes de pedir la relacion de documentos expliqué qué acredita el art. 812 en lenguaje llano ("documentos firmados por el deudor o las facturas, albaranes y certificaciones habituales del tráfico"), y antes de la pregunta sobre consumidor no usé jerga. Suficientemente claro para un cliente lego.
- **Invisibilidad.** Revisando mis propios turnos: no aparecio "V1", "vector", "hoja", "fase" ni "ahora voy a" en ningún mensaje visible. Cumple la directiva de invisibilidad.
- **Invencion de datos.** No inventé cifras, fechas ni citas normativas: la fecha de verificación de la LEC (31/08/2026) la tomé del registro existente en `references/fuentes-plantillas-validadas.md` en vez de simular una llamada real al BOE — **esto es una limitación de esta sesión de QA, no del propio SKILL.md**: no ejecuté el Punto 2 (verificación real contra el BOE) porque no es practicable dentro de esta prueba; lo señalo explícitamente en vez de fingir que lo hice. El interés de demora no se incluyó en el documento porque el cliente (simulado) decidió no reclamarlo y yo no tenía un tipo de interés vigente verificado que aplicar sin inventarlo.
- **Preguntas de clasificación.** En este escenario no hubo ninguna, porque los seis vectores se resolvieron por escucha activa desde el primer mensaje — es la mejor demostración posible de que el diseño evita cuestionarios cuando el mensaje inicial ya es completo.

### B) El asset visto desde el LLM que lo rellena — defectos reales encontrados y corregidos

Encontré cinco defectos reales ejecutando el flujo (no imaginados sobre el papel), los cinco reproducibles y corregidos con `Edit` quirúrgico:

1. **Placeholder repetido sin instrucción de propagarlo (el mas grave, con evidencia directa).** `{{nombre_acreedor}}` y `{{nombre_deudor}}` aparecen en el título, en el bloque DATOS, en el SUPLICO y en la firma — cuatro sitios distintos con el mismo dato. El `SKILL.md` no instruía sustituirlo en todas sus apariciones. Prueba de que esto rompe en la práctica: al rellenar el bloque DATOS con `Edit` de alcance limitado, se me quedó huérfano `{{nombre_deudor}}` en pleno SUPLICO ("requiera al deudor {{nombre_deudor}} para que...") hasta que lo detecté releyendo el archivo completo. **Fix aplicado:** añadida una regla global en `SKILL.md` ("Propagación de un dato confirmado") que obliga a sustituir el dato en todas sus apariciones y a verificarlo con `Read`.
2. **Sección 3 no reconocía datos ya aportados en el mensaje inicial.** A diferencia de la Sección 4 (que sí dice "el principal ya resuelto... se reutiliza sin volver a preguntarlo"), la Sección 3 no tenía esa salvedad para el origen de la deuda y la fecha de vencimiento, pese a que el cliente ya los mencionó ("facturas... vencieron en marzo"). Redactada tal cual, un operador literal reabriría con "describa el origen de la deuda" como si nada se supiera. **Fix aplicado:** añadida la instrucción de dar por confirmado lo ya aportado y pedir solo los datos concretos que falten.
3. **Una sola fecha de vencimiento para una deuda de varios documentos.** El asset (`peticion-monitorio.md` y `burofax-masc-reclamacion.md`) asumía un único `{{fecha_vencimiento}}`, pero el caso típico de "dos facturas impagadas" tiene dos vencimientos distintos. Forzar una sola fecha habría sido inexacto. **Fix aplicado:** reescrita la frase del HECHO TERCERO (y su equivalente en el burofax) para anclar el vencimiento a "los documentos relacionados", admitiendo una fecha o varias sin necesidad de inventar un dato unificado.
4. **Dato `deudor_consumidor` sin pregunta que lo recoja.** Aparece en el frontmatter (`inputs`) y el Guardrail 10 exige conocerlo antes de cerrar la cuantía (control de oficio de cláusulas abusivas, art. 815.4 LEC), pero ninguna sección de la Sección 5 lo preguntaba explícitamente; solo se mencionaba "si la deuda se funda en un contrato empresario-consumidor", dando por hecho que ya se sabría. En mi ejecución tuve que decidir yo mismo cómo cubrir el hueco. **Fix aplicado:** añadida una pregunta directa en la Sección 3 para los casos en que la condición de consumidor no se desprenda ya del origen descrito.
5. **Costas conforme al art. 394 LEC aplicado sin matiz a la hoja de monitorio.** La Sección 4 instruye "explica que las costas se solicitan conforme al art. 394 LEC" para todas las hojas por igual, pero el propio asset `peticion-monitorio.md` no tiene ninguna cláusula de costas en el SUPLICO — con razón, porque el art. 394 rige la condena en costas de una sentencia, y la petición inicial de monitorio no es todavía un procedimiento contencioso resuelto por sentencia. La instrucción, tal cual estaba, podía llevar a inventar una petición de costas sin encaje en el propio documento. **Fix aplicado (conservador, sin inventar doctrina):** aclarado en `SKILL.md` que en HOJA MONITORIO no se incluye petición expresa de costas en el SUPLICO, limitándose a advertir que las costas de fases posteriores (oposición, ejecución) se rigen por sus normas propias. Señalo esto como punto a verificar por un abogado colegiado, no como afirmación jurídica cerrada de mi parte.

**Placeholders ambiguos menores (no corregidos, solo señalados):** `{{naturaleza_acreedor}}` no tiene sub-apartado propio en la Sección 5 (a diferencia de NIF/domicilio); pude inferirlo razonablemente del formato del NIF ("persona física"), pero un operador menos cuidadoso podría dejarlo como placeholder sin saber qué poner. `{{cuantia_en_letras}}` tampoco tiene instrucción explícita de cálculo, aunque es una transformación mecánica sin ambigüedad real.

**Lectura de corrido del documento final:** con las dos correcciones de redacción aplicadas (vencimiento plural, propagación de nombres), el documento se lee como un escrito real, sin conectores forzados ni frases "de plantilla mal encajada". Antes del fix del vencimiento, la frase habría sido gramaticalmente forzada o factualmente imprecisa (afirmar una única fecha de vencimiento para una deuda con dos vencimientos reales).

### Resultado

**Ejecución en vivo: PASA con 5 defectos reales corregidos in situ** (ver arriba) sobre `SKILL.md`, `assets/peticion-monitorio.md` y `assets/burofax-masc-reclamacion.md`. Ningún defecto encontrado exigió reescribir sustancialmente la lógica de enrutamiento (Punto 1) ni el estilo conversacional (tono, invisibilidad), que superaron la prueba sin cambios.
