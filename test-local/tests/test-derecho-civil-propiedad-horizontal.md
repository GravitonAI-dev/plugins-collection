# Test de ejecucion — skill `derecho-civil-propiedad-horizontal`

Ejecucion manual del arbol de decision sobre tres escenarios. Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: LPH (BOE-A-1960-10906, Arts. 7, 9, 17, 18, 21), LEC (BOE-A-2000-323, Arts. 249, 264, 403, 812-818) y LO 1/2025 (BOE-A-2025-76).
- Verificacion real efectuada el 31/08/2026: art. 21 LPH en su redaccion vigente (visto bueno del presidente salvo secretario-administrador profesional que no vaya a intervenir en la reclamacion); art. 18.2 legitimacion tasada y requisito de estar al corriente de pago con la excepcion de acuerdos sobre cuotas de participacion del Art. 9.
- En este test la lectura online se simula como disponible -> `fecha_verificacion_normativa` = 31/08/2026.

---

## Test 1 — Comunidad reclama 2.400 euros de cuotas con acuerdo de junta

**Mensaje inicial:** "Soy el administrador de una comunidad. Un propietario debe 2.400 euros de cuotas de los ultimos 8 meses. La junta ya aprobo la liquidacion de la deuda y me autorizo a reclamarla."

### Recorrido del arbol
```
V1 -> escucha activa: "soy el administrador de una
       comunidad"                                       V1 = comunidad (sin pregunta)
V2 -> escucha activa: "debe... cuotas"                   V2 = impago de cuotas (sin pregunta)
V4 -> escucha activa: "la junta ya aprobo... y me
       autorizo"                                         V4 = si (sin pregunta)
HOJA CUOTAS -> assets/certificacion-deuda-comunidad.md, despues assets/peticion-monitorio-cuotas-lph.md
```
V3, V5 y V6 no aplican (exclusivos de la rama "propietario" o de "actividad"). Se generan DOS documentos en el orden indicado, reutilizando en el segundo los datos ya recogidos en el primero.

### Momento de las preguntas
- Turno 1: introduccion fija; como V1, V2 y V4 ya estan resueltos por escucha activa, la primera respuesta pasa directo a la Confirmacion (Punto 3) con el texto fijo CUOTAS y enlace BOE.
- Turnos 2-3: datos de la comunidad (confirmacion agrupada) y del propietario deudor (confirmacion agrupada), incluida la pregunta sobre si el secretario-administrador va a intervenir profesionalmente en la reclamacion (determina si hace falta el visto bueno del presidente).
- Turno 4: acuerdo de la junta y notificacion de la deuda al deudor (fecha, medio; NO se re-pregunta que la junta ya aprobo la liquidacion, solo se piden los datos concretos que faltan: fecha exacta y medio de notificacion).
- Turno 5: desglose de la deuda (negociacion) — la skill explica que la ley exige desglose y no admite importe global; usuario aporta 8 mensualidades de 300 euros.
- Turno 6: intereses y gastos de la reclamacion (negociacion, uno a uno).
- Turno 7: contra quien se dirige la reclamacion (negociacion) — usuario confirma que el piso no ha cambiado de titularidad.
- Turno 8: juzgado competente (eleccion entre domicilio del deudor y lugar de la finca, Art. 813 LEC).
- Turno 9: postulacion y embargo preventivo (negociacion).
- Turno 10: lugar y fecha; cierre de la certificacion.
- Turnos 11+: creacion de la peticion inicial de monitorio, reutilizando sin re-preguntar los datos de comunidad, deudor, acuerdo y desglose ya confirmados.

### Documento generado (extracto relleno, datos sinteticos)
```
CERTIFICACION DEL ACUERDO DE LIQUIDACION DE LA DEUDA — COMUNIDAD DE PROPIETARIOS EJEMPLO
> DRAFT — para revision por un abogado colegiado antes de su firma.

Deuda de PROPIETARIO A (piso 3ºB, cuota de participacion 5,2%):
Enero 2026: 300 euros. Febrero 2026: 300 euros. [...] Agosto 2026: 300 euros.
TOTAL: 2.400 euros, mas intereses desde cada vencimiento (Art. 21.1 LPH).

Visto bueno del Presidente: SI, se une visto bueno.
```
```
PETICION INICIAL DE PROCESO MONITORIO ESPECIAL (Art. 21 LPH y Art. 812.2.2º LEC)
Deudor: PROPIETARIO A. Cuantia: 2.400 euros.
```
Resultado: **PASA**. La peticion de monitorio no repite ninguna pregunta ya respondida en la certificacion.

---

## Test 2 — Propietario ausente impugna un acuerdo de derrama dentro de plazo

**Mensaje inicial:** "No pude ir a la ultima junta de mi comunidad. Me acabo de enterar de que aprobaron una derrama de 3.000 euros hace 2 meses y me parece un abuso. Quiero impugnarla."

### Recorrido del arbol
```
V1 -> PREGUNTA: "Actua usted en nombre de..." -> 2       V1 = propietario
V3 -> PREGUNTA: "Lo que desea es..." -> 1                V3 = impugnacion
V5.a -> PREGUNTA: posicion en la votacion -> 2 (ausente) V5.a = ausente
V5.b -> PREGUNTA: al corriente de pago -> 1 (si)         V5.b = al corriente
Plazo: acuerdo hace 2 meses, comunicado al ausente
        hace 1 mes -> dentro del plazo de 3 meses         plazo vigente (sin pregunta, calculado)
HOJA IMPUGNACION -> assets/demanda-impugnacion-acuerdos.md
```
V2, V4 y V6 no aplican (exclusivos de la rama "comunidad").

### Momento de las preguntas
- Turno 1: introduccion fija + V1 (no se pudo inferir por escucha activa: el mensaje no dice explicitamente "actuo como propietario", aunque lo insinua; la skill pregunta para no asumir).
- Turno 2: V3.
- Turnos 3-4: V5.a y V5.b, en preguntas separadas (nunca combinadas, conforme a la regla de la guia).
- Turno 5: Confirmacion visible con el texto fijo IMPUGNACION, la caducidad de 3 meses / 1 ano y el aviso de MASC.
- Turnos 6-7: parte demandante y comunidad demandada (confirmacion agrupada cada una).
- Turno 8: la junta y el acuerdo impugnado (fecha, convocatoria, punto del orden del dia, texto literal, resultado de la votacion) — la skill valida que el resultado descrito por el usuario cuadra con "aprobaron la derrama".
- Turno 9: legitimacion y plazo — la skill calcula el plazo (2 meses transcurridos desde el acuerdo, menos de 3) y lo hace constar; NO vuelve a preguntar la posicion en la votacion, ya resuelta en V5.a/V5.b.
- Turno 10: situacion de pago (negociacion) — ya resuelta (al corriente), se hace constar sin volver a preguntar.
- Turno 11: motivos de la impugnacion (negociacion) — usuario alega "me parece un abuso": la skill explica los 3 supuestos del Art. 18.1 y pide que concrete cual aplica (gravemente lesivo / grave perjuicio individual / contrario a estatutos), sin aceptar "me parece un abuso" como motivo valido sin mas concrecion.
- Turnos 12-13: suspension cautelar (negociacion, se explica que no es automatica), peticion adicional del suplico.
- Turno 14: intento de solucion previa (MASC).
- Turno 15: juzgado, lugar y fecha.

### Documento generado (extracto relleno)
```
DEMANDA DE JUICIO ORDINARIO DE IMPUGNACION DE ACUERDOS — PROPIETARIO C contra COMUNIDAD DE PROPIETARIOS EJEMPLO 2
> DRAFT — para revision por un abogado colegiado antes de su firma.

HECHOS
PRIMERO. Junta de {{fecha}}, punto {{n}} del orden del dia: aprobacion de derrama de 3.000 euros.
SEGUNDO. El demandante no asistio; se le comunico el acuerdo el {{fecha}}. El plazo de tres meses del Art. 18.3 LPH no ha vencido.
TERCERO. El demandante esta al corriente de pago de todas las deudas vencidas con la comunidad.

FUNDAMENTOS DE DERECHO
[...] el acuerdo es gravemente lesivo para los intereses de la comunidad en beneficio de uno o varios propietarios / supone un grave perjuicio para el demandante sin obligacion juridica de soportarlo (Art. 18.1 LPH) [segun lo que el usuario concrete].
```
Resultado: **PASA**. No se admite el motivo generico "me parece un abuso" sin encuadrarlo en el Art. 18.1.

---

## Test 3 — Actividad molesta (bar con ruido)

**Mensaje inicial:** "En los bajos de nuestra comunidad hay un bar que hace mucho ruido por las noches. Varios vecinos se han quejado. Queremos que la comunidad actue."

### Recorrido del arbol
```
V1 -> escucha activa: "nuestra comunidad... queremos
       que la comunidad actue"                           V1 = comunidad (sin pregunta)
V2 -> PREGUNTA: asunto de la comunidad -> 2               V2 = actividad molesta
V6 -> PREGUNTA: requerimiento previo -> 1 (no)            V6 = no requerido aun
HOJA CESACION -> assets/requerimiento-cesacion-actividad.md
```
V3, V4 y V5 no aplican.

### Momento de las preguntas
- Turno 1: introduccion fija + V2 (V1 ya resuelto).
- Turno 2: V6.
- Turno 3: Confirmacion visible con texto fijo CESACION y advertencia de que este requerimiento es presupuesto previo a la accion de cesacion, no la demanda en si.
- Turnos 4-5: datos de la comunidad y del presidente (confirmacion agrupada), datos del infractor (confirmacion agrupada) — usuario indica que el bar es arrendatario de un local, no propietario: la skill advierte de que conviene remitir copia al propietario.
- Turno 6: descripcion de la actividad — el usuario responde inicialmente "hacen mucho ruido, son un desastre"; la skill NO acepta esa respuesta como hecho verificable, explica por que y pide horarios, fechas y frecuencia concretos antes de escribir.
- Turno 7: acreditacion (denuncias, actas de policia local).
- Turno 8: fundamento de la prohibicion (negociacion) — usuario y skill acuerdan la via de "actividad que contraviene las disposiciones sobre actividades molestas" (Art. 7.2 LPH).
- Turno 9: plazo de cesacion y medidas solicitadas (negociacion).
- Turno 10: ofrecimiento de solucion negociada.
- Turno 11: informacion de las consecuencias (sin pregunta) + juzgado no aplica aqui (es un requerimiento, no una demanda) + lugar y fecha.

### Documento generado (extracto relleno)
```
REQUERIMIENTO DE CESACION DE ACTIVIDAD MOLESTA — COMUNIDAD DE PROPIETARIOS EJEMPLO 3 a BAR EJEMPLO SL
> DRAFT — para revision por un abogado colegiado antes de su firma.

Hechos: ruido nocturno constatado los dias {{fechas}} entre las 23:00 y las 02:00 horas, con {{n}} quejas vecinales documentadas.
Fundamento: Art. 7.2 de la Ley 49/1960, sobre propiedad horizontal (actividad que contraviene las disposiciones generales sobre actividades molestas).
Plazo de cesacion: 15 dias desde la recepcion de este requerimiento.
```
Resultado: **PASA**. La skill rechazo la primera respuesta vaga del usuario y pidio hechos verificables antes de redactar, conforme a la regla de "validacion de sentido, no solo de formato".

---

## Revision UX

Hallazgos:
1. En el Test 1, saltar directamente a la Confirmacion cuando los 3 vectores ya estan resueltos por escucha activa evita un turno de pregunta redundante y acelera el flujo para el caso mas frecuente (comunidad con acuerdo ya adoptado).
2. Separar V5.a y V5.b en dos turnos (posicion en la votacion / situacion de pago) evita una mega-pregunta y permite aplicar el guardrail de legitimacion tasada inmediatamente despues de V5.a, antes de gastar turnos en datos que resultarian inutiles si el usuario no estuviera legitimado.
3. El rechazo explicito de "me parece un abuso" y de "son un desastre" como motivos/hechos sin concretar demuestra que la skill no es un formulario pasivo: dialoga y exige hechos verificables antes de escribir, conforme a la regla de validacion de sentido de la guia.
4. Advertir de que el requerimiento de cesacion no es la demanda, y que esta exige autorizacion de la junta, evita expectativas erroneas del cliente sobre lo que el documento generado consigue por si solo.
5. Pendiente de revision humana: la distincion entre acuerdo nulo de pleno derecho y meramente anulable (con impacto en el computo del plazo) queda marcada en la tabla de escalacion como "no cerrada", en vez de que la skill zanje la cuestion por su cuenta.

Ajustes aplicados: ninguno adicional a los ya reflejados en el SKILL.md (rechazo de motivos/hechos vagos en las secciones 6 de HOJA IMPUGNACION y 3 de HOJA CESACION, y el salto directo a Confirmacion cuando todos los vectores resuelven por escucha activa).

---

## Verificacion en vivo + calidad LLM

Ejecucion real (no simulada sobre el papel) del Test 1: verificacion normativa real (WebFetch al BOE, confirmo Art. 21 LPH vigente y proceso monitorio especial; WebSearch del interes legal del dinero 2026 = 3,25 %), y generacion turno a turno de ambos documentos con `Write`/`Read`/`Edit` reales en `test-local/output/certificacion-ph-qa-prueba.md` y `test-local/output/monitorio-ph-qa-prueba.md`.

**Extracto — turno 1 (LLM operativo):**
> "A su caso corresponde el proceso monitorio especial de comunidades de propietarios, regulado en el articulo 21 de la Ley 49/1960... Prepararemos primero la certificacion del acuerdo de liquidacion de la deuda... Fuente consultada: https://www.boe.es/buscar/act.php?id=BOE-A-1960-10906"

**Extracto — transicion entre documentos (sin repetir preguntas):**
> "La certificacion queda cerrada con estos datos. Continuamos con la peticion inicial del proceso monitorio, reutilizando los datos ya recogidos de la comunidad, del deudor, del acuerdo de la junta, del desglose y de los intereses y gastos, sin volver a preguntarlos. Determinamos el juzgado competente..."

**Extracto del documento final (certificacion), desglose real, no agregado:**
> "| Cuota ordinaria | Enero 2026 | 01/01/2026 | 300,00 | ... | **TOTAL** | | | **2.400,00** |"
> "CUARTO — Intereses. ...al tipo de interes legal del dinero vigente del 3,25 %, que a la fecha de esta certificacion ascienden a 29,38 euros."

### Veredicto A (calidad de la respuesta del LLM): PASA

Registro formal ("usted", "indique", "pasamos") en las 15 respuestas del turno; cero menciones de V1-V6 o de fases internas; cero datos inventados (el 3,25 % de interes legal y la fecha de verificacion del BOE se obtuvieron por herramienta, no por memoria); las clausulas de negociacion (desglose, intereses, gastos) se explicaron antes de pedir la decision. La transicion entre certificacion y peticion fue fluida y no repitio ninguna pregunta ya respondida — pero para conseguirlo tuve que decidir por mi cuenta, sin apoyo claro del SKILL.md, que las secciones 7 (juzgado) y 8 (postulacion/embargo) debian preguntarse al construir la peticion y no la certificacion, porque esa asignacion no estaba explicitada.

### Veredicto B (calidad del asset): PASA, con dos defectos corregidos

1. **Corregido en `certificacion-deuda-comunidad.md`:** el bloque condicional de intereses exigia "que la junta acordase intereses" para poder incluir el interes del Art. 21.1 LPH, cuando ese interes es legal y automatico desde cada vencimiento, sin acuerdo de junta; solo una medida disuasoria con tipo distinto necesita acuerdo. Separe ambos supuestos en dos comentarios distintos.
2. **Corregido en `certificacion-deuda-comunidad.md`:** el campo "Referencia catastral" no correspondia a ningun dato preguntado en el Punto 5 del SKILL.md — quedaria sistematicamente como `{{referencia_catastral}}` sin resolver. Eliminado del asset.
3. **Corregido en `SKILL.md`:** anadi una frase que asigna explicitamente las secciones 7-8 a la peticion inicial (no tienen campo en la certificacion) y aclara que la fecha de la seccion 9 se responde dos veces con sentido distinto por documento.

Los placeholders restantes son inequivocos, los bloques condicionales (tablon, procurador, embargo, codemandado) no generan frases forzadas, y ambos documentos finales leen como escritos juridicos reales, con HECHOS numerados, FUNDAMENTOS DE DERECHO ordenados y SUPLICO ajustado.

