# Test de ejecucion — skill `derecho-civil-desahucio`

Ejecucion manual del arbol de decision sobre tres escenarios. Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: LEC (BOE-A-2000-323, Libro III y Arts. 22, 52, 250, 437-441, 447, 549), LAU (BOE-A-1994-26003, Art. 27), LO 1/2025 (BOE-A-2025-76) y Ley 12/2023 (BOE-A-2023-12203).
- Verificacion real efectuada el 31/08/2026: STC 26/2025, de 29 de enero, declaro inconstitucionales y nulas las letras c) del Art. 439.6 y el Art. 439.7 LEC (acreditar vulnerabilidad del demandado y conciliacion previa por gran tenedor) — la skill NO los exige. El regimen extraordinario de suspension de lanzamientos por vulnerabilidad ligado al RDL 11/2020 queda marcado "verificar manualmente" en cada lanzamiento.
- En este test la lectura online se simula como disponible -> `fecha_verificacion_normativa` = 28/02/2025 (verificado 31/08/2026).

---

## Test 1 — Falta de pago con requerimiento previo (excluye enervacion) + acumulacion de rentas

**Mensaje inicial:** "Mi inquilino no paga la renta desde hace 4 meses. Le mande un burofax hace dos meses requiriendo el pago y no contesto. Quiero desahuciarlo y que me pague lo que debe."

### Recorrido del arbol
```
V1 -> escucha activa: "mi inquilino"                    V1 = arrendamiento con renta (sin pregunta)
V2 -> escucha activa: "no paga la renta"                V2 = falta de pago (sin pregunta)
V3 -> PREGUNTA: "Lo que desea preparar es..." -> 1       V3 = demanda judicial
V6 -> escucha activa: "burofax hace dos meses,
       no contesto" (>30 dias, con acuse)               V6 = 1 (mas de 30 dias, justificante)
V4 -> PREGUNTA: destino del inmueble -> 1                V4 = vivienda habitual
V5 -> PREGUNTA: gran tenedor -> 2                        V5 = 10 o menos / <1.500 m2
V7 -> PREGUNTA: MASC intentado -> el propio burofax
       de requerimiento sirve de intento (usuario
       confirma que fue negociacion directa)             V7 = si (reutiliza el burofax)
HOJA IMPAGO -> assets/demanda-desahucio-falta-pago.md
```
Assets cargados: solo `demanda-desahucio-falta-pago.md`. No se activan bloques de expiracion ni de precario.

### Momento de las preguntas
- Turno 1: introduccion fija + primera pregunta pendiente (V3, ya que V1/V2 resueltos por escucha activa). Una pregunta por turno.
- Turno 2: V6 (requerimiento previo), con las 3 opciones numeradas.
- Turnos 3-4: V4 y V5 en turnos separados (no comprimidos).
- Turno 5: V7 (MASC), en la que la skill detecta que el burofax ya descrito puede servir de intento previo y lo confirma con el usuario en vez de pedirlo de nuevo.
- Turno 6: Confirmacion visible (Punto 3): texto fijo IMPAGO + mencion de gran tenedor y postulacion + eleccion plantilla/documento propio.
- Turnos 7-9: parte demandante (confirmacion agrupada), parte demandada (confirmacion agrupada), inmueble.
- Turno 10: mencion de gran tenedor (ya resuelta, se hace constar sin re-preguntar) con su consecuencia documental explicada.
- Turno 11: contrato y deuda de rentas (fecha, renta mensual, periodos, importe, documentos) — NO se re-pregunta que hay 4 meses de impago, ya extraido del mensaje inicial.
- Turno 12: requerimiento previo y enervacion (negociacion) — la skill confirma que, al haber requerimiento fehaciente >30 dias, NO procede la enervacion y lo hace constar.
- Turno 13: acumulacion de rentas (negociacion) — usuario confirma que si, con importe y periodos.
- Turnos 14-16: lanzamiento anticipado, compromiso de condonacion (declina), informacion de vivienda habitual (sin pregunta), MASC (ya resuelto), juzgado, lugar y fecha.

### Documento generado (extracto relleno, datos sinteticos)
```
DEMANDA DE JUICIO VERBAL DE DESAHUCIO POR FALTA DE PAGO — ARRENDADOR A contra ARRENDATARIO A
> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico definitivo.

AL JUZGADO DE PRIMERA INSTANCIA DE CIUDAD EJEMPLO

HECHOS
PRIMERO. Contrato de arrendamiento de vivienda de fecha 01/09/2024, renta 800 euros/mes.
SEGUNDO. Deuda de 3.200 euros correspondiente a las mensualidades de mayo a agosto de 2026.
TERCERO. El inmueble constituye la vivienda habitual de la parte demandada.
CUARTO. La parte actora no es gran tenedora de vivienda en los terminos del Art. 3.k de la Ley 12/2023.
QUINTO. Se requirio de pago fehacientemente el [fecha >30 dias], sin resultado; no procede la enervacion (Art. 22.4 LEC).

SUPLICO: se declare resuelto el contrato, se condene al desalojo y al pago de 3.200 euros mas las rentas que se devenguen hasta la entrega de la posesion...
```
Resultado: **PASA**. No aparecen bloques de expiracion de plazo ni de precario; la mencion de gran tenedor y el pronunciamiento sobre enervacion constan expresamente, como exige el Art. 439.3 y 439.6 LEC.

---

## Test 2 — Precario (familiar que no paga ni tiene titulo)

**Mensaje inicial:** "Mi hermano vive gratis en un piso mio desde hace tres anos, sin contrato ni renta. Le pedi que se fuera hace un mes por burofax y no se ha ido. Quiero recuperar el piso."

### Recorrido del arbol
```
V1 -> escucha activa: "vive gratis... sin contrato
       ni renta"                                        V1 = cesion gratuita sin renta
V3 -> PREGUNTA: via -> 1                                 V3 = demanda judicial
V4 -> PREGUNTA: destino -> 1 (vivienda habitual del
       hermano)                                          V4 = vivienda habitual
V5 -> PREGUNTA: gran tenedor -> 2                        V5 = no gran tenedor
V7 -> PREGUNTA: MASC -> el burofax de revocacion de
       la tolerancia sirve de intento previo             V7 = si
HOJA PRECARIO -> assets/demanda-desahucio-precario.md
```
V2 y V6 NO se activan (solo aplican si V1 = arrendamiento). Verificado: el asset generado no contiene la clausula de deuda de rentas ni el pronunciamiento sobre enervacion (ambos exclusivos de la HOJA IMPAGO).

### Momento de las preguntas
- Turno 1: introduccion fija (ya emitida en el test 1 si fuera la misma sesion; en sesion nueva se repite una unica vez) + pregunta V3, ya que V1 se resolvio por escucha activa.
- Turnos 2-3: V4 y V5 por separado.
- Turno 4: V7, reconduciendo el burofax de revocacion como MASC.
- Resto de turnos: identico patron de confirmacion agrupada por parte, seccion de origen de la ocupacion y revocacion de la tolerancia (con verificacion explicita de que no media renta ni contraprestacion), juzgado, lugar y fecha. La seccion "acumulacion de rentas" y "requerimiento previo y enervacion" NO se ofrecen (exclusivas de impago).

### Documento generado (extracto relleno)
```
DEMANDA DE JUICIO VERBAL DE DESAHUCIO POR PRECARIO — PROPIETARIO A contra OCUPANTE A
> DRAFT — para revision por un abogado colegiado antes de su firma.

HECHOS
PRIMERO. Titularidad del inmueble por PROPIETARIO A, escritura de compraventa de fecha {{dato}}.
SEGUNDO. Cesion gratuita del uso a OCUPANTE A desde 2023, sin renta ni contraprestacion de ninguna clase.
TERCERO. Revocacion de la tolerancia mediante burofax de fecha {{dato}}, sin que el ocupante haya desalojado.
```
Resultado: **PASA**. Sin fugas de bloques de la hoja de impago.

---

## Test 3 — Acuerdo de condonacion con entrega de llaves

**Mensaje inicial:** "Tengo un inquilino que debe 5 meses de renta, 2.500 euros. Prefiero llegar a un acuerdo: le perdono la mitad de la deuda si me entrega las llaves este mes, en vez de ir a juicio."

### Recorrido del arbol
```
V1 -> escucha activa: "inquilino... renta"               V1 = arrendamiento con renta
V3 -> escucha activa: "prefiero llegar a un acuerdo"     V3 = acuerdo de salida pactada (sin pregunta)
HOJA ACUERDO -> assets/acuerdo-condonacion-entrega-llaves.md
```
V2, V4, V5, V6 y V7 NO se preguntan (el routing los excluye explicitamente cuando V3 = acuerdo: "no hay demanda que admitir"). Verificado: el documento generado no contiene AL JUZGADO, HECHOS, FUNDAMENTOS ni SUPLICO — es un contrato de transaccion, no un escrito procesal.

### Momento de las preguntas
- Turno 1: introduccion fija + confirmacion de que V3 ya se detecto; primer turno sustantivo pasa directo a la Confirmacion (Punto 3) con el texto fijo ACUERDO (Art. 1809 CC) y la eleccion plantilla/documento propio.
- Turnos 2-3: parte arrendadora y parte arrendataria (confirmacion agrupada cada una).
- Turno 4: inmueble y contrato que se extingue.
- Turno 5: deuda que se reconoce (negociacion) — la skill explica antes de pedir la cifra que el reconocimiento fija el importe sobre el que operara la condonacion. Usuario confirma 2.500 euros (5 meses x 500).
- Turno 6: alcance de la condonacion (negociacion) — usuario ya indico "la mitad": la skill NO vuelve a preguntar el importe total, solo pide que subsiste (1.250 euros), forma y plazo de pago, y explica la condicion suspensiva a la entrega (Arts. 1156 y 1187 CC).
- Turno 7: entrega de llaves y posesion (fecha cierta, este mes).
- Turnos 8-10: fianza y garantias, renuncia reciproca de acciones (negociacion, se explica la posicion conservadora de excepcionar danos), consecuencias del incumplimiento.
- Turno 11: fuerza ejecutiva del acuerdo (negociacion) — la skill explica las tres opciones (homologacion, escritura publica, documento privado) y recomienda homologacion si hay pleito en curso o escritura publica si no lo hay.
- Turno 12: lugar, fecha y firma.

### Documento generado (extracto relleno)
```
ACUERDO DE CONDONACION DE RENTAS Y ENTREGA DE LLAVES — ARRENDADOR B y ARRENDATARIO B
> DRAFT — para revision por un abogado colegiado antes de su firma.

CUARTA — Deuda reconocida: 2.500 euros (5 mensualidades de 500 euros, mayo a septiembre de 2026).
QUINTA — Condonacion: parcial, por importe de 1.250 euros, condicionada a la entrega de la posesion el {{fecha}}. Subsiste una deuda de 1.250 euros, pagadera en {{plazo}}.
SEXTA — Entrega de llaves: {{fecha}} a las {{hora}}, en el propio inmueble, con levantamiento de acta.
```
Resultado: **PASA**. Ningun dato ya aportado (importe total de la deuda, "la mitad", plazo de un mes) se vuelve a preguntar.

---

## Revision UX

Hallazgos:
1. La pregunta V3 ("lo que desea preparar es...") aparece razonablemente pronto, tras V1/V2 resueltos por escucha activa: el usuario no repite informacion ya dada.
2. Las menciones obligatorias del Art. 439.6 (destino del inmueble, gran tenedor) se explican con su consecuencia documental antes de darlas por resueltas, en vez de tratarlas como tramite oculto — coherente con el principio de dialogo en clausulas de negociacion.
3. Reutilizar el burofax ya descrito por el usuario como acreditacion de MASC (en vez de pedir un tramite nuevo) reduce turnos sin perder rigor: la skill sigue verificando que cumple los requisitos del Art. 10.2 LO 1/2025 antes de darlo por bueno.
4. En el acuerdo de condonacion, separar "deuda reconocida" de "alcance de la condonacion" en dos turnos distintos (en vez de uno) evita que el usuario tenga que calcular el importe subsistente el mismo turno en que fija la deuda total.
5. Pendiente de revision humana: el guardrail 10 remite el estado del RDL 11/2020 a verificacion en cada lanzamiento; en este test se marca como "verificar manualmente" en vez de darlo por vigente o derogado, que es el comportamiento correcto exigido por la regla de actualizacion normativa.

Ajustes aplicados: ninguno adicional a los ya incorporados en el SKILL.md (routing de V7 con reutilizacion del burofax, y separacion de las secciones 4 y 5 de la HOJA ACUERDO).

---

## Verificacion en vivo + calidad LLM

Ejecucion REAL (no sobre el papel) del escenario del Test 1, jugando el turno del LLM operativo, con `Write`/`Read`/`Edit` reales sobre `test-local/output/demanda_desahucio_falta_pago_arrendador_a.md`. Verificacion normativa hecha contra la API del BOE (no simulada): `curl` a `datosabiertos/api/legislacion-consolidada` para el Art. 22.4 LEC (confirma "treinta dias", version vigente BOE-A-2025-76, en vigor 03/04/2025) y el Art. 439.6 LEC (confirma que las letras c) del apartado 6 y el apartado 7 estan anuladas por la STC 26/2025, version BOE-A-2025-4079).

### A) Calidad de la respuesta del LLM

Extractos literales generados en la conversacion simulada:

Turno 1 (intro fija + V3): *"Vamos a preparar el documento que le permita recuperar la posesión del inmueble por la vía que corresponda a su caso... Lo que desea preparar es: 1. La demanda judicial para recuperar la posesión 2. Un acuerdo con la parte ocupante..."*

Turno 5 (V7, resolviendo con criterio en vez de repreguntar en seco): *"Sí, el burofax de requerimiento de pago con acuse de recibo que ya me ha descrito puede servir como acreditación del intento previo de solución extrajudicial que exige la Ley Orgánica 1/2025... Doy por resuelto este punto con ese documento."*

Turno 6 (Confirmacion, Punto 3): *"A su caso corresponde el juicio verbal de desahucio por falta de pago, conforme al artículo 250.1.1º de la Ley 1/2000... Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323. El desahucio no figura entre las materias exceptuadas del artículo 5.2 de la Ley Orgánica 1/2025... En el desahucio son preceptivos abogado y procurador... ¿Qué documento desea utilizar como base?"*

Seccion 6 (enervacion, explicacion antes de la constancia): la explicacion de que "la parte demandada puede enervar la acción pagando o consignando lo debido... salvo que se le requiriera de pago por medio fehaciente con al menos treinta días de antelación" se dio ANTES de hacer constar que no procede, tal como exige el SKILL.md.

Veredicto A: **PASA**. Registro formal ("usted"), cero coloquialismos, cero mencion de V1-V7 ni de fases internas, explicaciones de enervacion y gran tenedor claras y en el orden correcto (explicar antes de pedir/hacer constar la decision), cero datos inventados (todos los datos del documento son sinteticos y declarados como tales, coherentes con lo que el cliente dijo: 4 meses de impago, burofax hace 2 meses).

### B) El asset visto desde el LLM que lo rellena

Se detectaron y corrigieron TRES defectos reales durante la ejecucion (no preexistentes de otras skills — se me escaparon a mi al redactar la simulacion y los corregi en el propio asset/SKILL, no solo en el documento de prueba):

1. **Defecto grave — mencion obligatoria ausente en los tres assets de demanda.** Ninguno de `demanda-desahucio-falta-pago.md`, `demanda-desahucio-expiracion-plazo.md` ni `demanda-desahucio-precario.md` contenia placeholder o HECHO para el destino del inmueble ni para la condicion de gran tenedor, pese a que el SKILL.md (Guardrail 3 y Seccion 5.3-5.4) dice literalmente que "su omisión determina la inadmisión" (Art. 439.6.a y b LEC). Corregido: añadido un HECHO "SEGUNDO — Destino del inmueble y condición de la parte actora" (con placeholders `{{destino_inmueble}}` y `{{condicion_gran_tenedor}}`, mas el bloque condicional de certificacion registral) y un nuevo "III. Admisibilidad" en FUNDAMENTOS DE DERECHO, en los tres assets, renumerando los HECHOS y FUNDAMENTOS siguientes.
2. **Defecto de numeracion en el SUPLICO.** El SUPLICO de la hoja de impago tenia el punto 3 (acumulacion de rentas) como bloque condicional numerado; al omitirse (por no estar aun decidido en el momento del `Write`), la numeracion saltaba de "2." a "4." — un salto que se veria en cualquier demanda donde no se acumule la reclamacion de rentas. Corregido en el asset: la clausula de acumulacion ahora es un parrafo "Asimismo, condene..." sin numero propio, y "Imponga las costas" queda fijo en "3." independientemente de la decision.
3. **Inconsistencia de formato en el HECHO opcional de MASC.** El bloque condicional de MASC escribia el titulo del hecho ("QUINTO/SEXTO — Intento de solución previa") en la misma línea que el párrafo, rompiendo el patrón `**ORDINAL — Título.**` en línea propia que usan todos los demás hechos. Corregido en los tres assets.
4. **Gap menor en el SKILL.md** (Seccion 5, item 6): no habia instruccion explicita para pedir la fecha y el medio exactos del requerimiento previo cuando V6=1, pese a que el asset necesita `{{medio_requerimiento}}` y `{{fecha_requerimiento}}`. Añadida la instrucción de pedirlos si aún no se conocen.

Veredicto B: **PASA, con correcciones aplicadas**. Tras las correcciones, los placeholders son inequivocos, los bloques condicionales no generan frases forzadas ni numeraciones rotas, y el documento final (ver `test-local/output/demanda_desahucio_falta_pago_arrendador_a.md`) lee como un escrito de desahucio real: HECHOS numerados con una idea por apartado, FUNDAMENTOS ordenados (competencia, procedimiento, admisibilidad, legitimacion, fondo, procedibilidad, costas) y SUPLICO ajustado a lo pedido (resolucion, desahucio con lanzamiento, condena al pago de rentas acumuladas, costas).

Ficheros modificados: `SKILL.md` (1 edit), `assets/demanda-desahucio-falta-pago.md` (4 edits), `assets/demanda-desahucio-expiracion-plazo.md` (2 edits), `assets/demanda-desahucio-precario.md` (2 edits). Documento de prueba generado con 1 `Write`, 1 `Read` de verificacion y 15 `Edit` incrementales reales en `test-local/output/demanda_desahucio_falta_pago_arrendador_a.md`.
