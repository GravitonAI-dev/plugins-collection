# Test de ejecucion — skill `derecho-civil-modificacion-medidas`

Ejecucion manual del arbol de decision sobre cuatro escenarios (3 principales + 1 contra-caso). Datos SINTETICOS (no corresponden a personas reales); se usan solo para verificar el enrutamiento, el filtro de viabilidad y el relleno de los assets.

## Verificacion normativa (Punto 2)

- Fuentes: CC (BOE-A-1889-4763, Arts. 90, 91, 93, 100, 101, 142, 146, 148, 152), LEC (BOE-A-2000-323, Arts. 775, 776, 770, 777, 749), LO 1/2025 (BOE-A-2025-76) y LOPJ (BOE-A-1985-12666, Art. 89).
- Verificacion real efectuada el 31/08/2026: el Art. 87 ter LOPJ que se citaba en el encargo esta SUPRIMIDO por la LO 1/2025; la regla de competencia exclusiva y de exclusion de MASC en violencia de genero vive en el Art. 89.6, 89.7 y 89.9 LOPJ (y en el Art. 44 LO 1/2004). Los procesos de familia contenciosos SI estan sujetos al requisito de MASC de la LO 1/2025.
- En este test la lectura online se simula como disponible -> version verificada 31/08/2026.

---

## Test 1 — Reduccion de alimentos por despido involuntario (contenciosa)

**Mensaje inicial:** "Pago 400 euros al mes de pension de alimentos para mi hijo desde el divorcio. Me despidieron hace 4 meses, cobro el paro y no llego. Mi ex mujer no quiere bajarla. Quiero pedir que la reduzcan."

### Recorrido del arbol
```
V1 -> escucha activa: "pension de alimentos... hijo"     V1 = medidas relativas a los hijos
V1a -> escucha activa: "pension de alimentos"             V1a = pension de alimentos
V1b -> escucha activa: "quiero pedir que la reduzcan"     V1b = reducir
V2 -> escucha activa: "mi ex mujer no quiere"             V2 = contenciosa
Comprobacion previa: existe sentencia de divorcio previa (sin pregunta, confirmado por el relato)
FILTRO DE VIABILIDAD (1.B):
  Que cambio -> "me despidieron"
  Desde cuando -> "hace 4 meses"
  Como se acredita -> PREGUNTA -> "carta de despido y certificado del SEPE"
  Evaluacion: despido INVOLUNTARIO, acreditable, con vocacion de permanencia -> ENCAJA (sin advertencia de imputabilidad)
HOJA -> assets/demanda-modificacion-medidas.md (variante CONTENCIOSA)
```

### Momento de las preguntas
- Turno 1: introduccion fija + no hace falta pregunta de clasificacion (V1, V1a, V1b y V2 resueltos por escucha activa); pasa directo al Filtro de Viabilidad.
- Turno 2: "Indique que ha cambiado..." -> ya contestado en el mensaje inicial, no se repite.
- Turno 3: "Indique con que documentacion puede acreditarlo" (unica pregunta realmente pendiente del filtro).
- Turno 4: Confirmacion visible (Punto 3): cita Art. 775 LEC + Art. 90.3, 91, 93 y 146 CC + advertencia de via contenciosa (juicio verbal, MASC exigible, riesgo de reconvencion).
- Turnos 5-6: parte solicitante y otra parte (confirmacion agrupada cada una).
- Turno 7: resolucion de origen — tipo, fecha, juzgado, y transcripcion literal del pronunciamiento de alimentos (el usuario debe copiarla de su sentencia).
- Turno 8: hijos afectados (nombre y fecha de nacimiento del hijo, confirmacion agrupada).
- Turno 9: la alteracion de circunstancias (negociacion) — la skill explica los 5 requisitos, muestra la redaccion propuesta del hecho (despido, fecha) y pide confirmacion; pide despues la relacion de documentos (carta de despido, certificado del SEPE) SIN volver a preguntar que cambio ni desde cuando, ya resuelto en el Filtro de Viabilidad.
- Turno 10: documentacion economica de ambas partes (Art. 770.1ª LEC).
- Turno 11: intento de solucion extrajudicial (MASC) — usuario aun no lo intento: la skill advierte del riesgo de inadmision y recomienda intentarlo antes de presentar.
- Turno 12: redaccion de la medida nueva (negociacion) — importe reducido propuesto, con la advertencia expresa de no retroactividad y de que dejar de pagar por cuenta propia genera deuda ejecutable.
- Turno 13: modificacion provisional (Art. 775.3 LEC) — usuario decide pedirla dada la urgencia economica.
- Turno 14: prueba adicional.
- Turno 15: juzgado, representacion y cierre.

### Documento generado (extracto relleno, datos sinteticos)
```
DEMANDA DE MODIFICACION DE MEDIDAS DEFINITIVAS (Art. 775 LEC, via contenciosa) — PROGENITOR A contra PROGENITOR B
> DRAFT — para revision por un abogado colegiado antes de su presentacion o firma. No constituye asesoramiento juridico.

HECHOS
PRIMERO. Sentencia de divorcio de fecha {{fecha}}, Juzgado de Primera Instancia nº {{n}} de {{ciudad}}, autos {{numero}}, que fijo una pension de alimentos de 400 euros mensuales a cargo de PROGENITOR A a favor de HIJO MENOR 1.
SEGUNDO. PROGENITOR A fue despedido el {{fecha}}, hace mas de cuatro meses, percibiendo desde entonces la prestacion por desempleo. Se acompanan carta de despido y certificado del SEPE.
[...]
SUPLICO: se fije la pension de alimentos en {{importe_reducido}} euros mensuales desde la fecha que en Derecho proceda.

ADVERTENCIA: la modificacion no produce efectos hasta resolucion judicial firme; la pension de 400 euros sigue siendo exigible y ejecutable hasta entonces.
```
Resultado: **PASA**. No se activa el bloque de mutuo acuerdo ni el de propuesta de convenio.

---

## Test 2 — Extincion por hijo de 26 anos trabajando e independizado

**Mensaje inicial:** "Mi hijo tiene 26 anos, trabaja a jornada completa desde hace un ano y vive en su propio piso de alquiler. Sigo pagandole 300 euros de alimentos por la sentencia de divorcio. Quiero dejar de pagar."

### Recorrido del arbol
```
V1 -> escucha activa: "mi hijo... alimentos"             V1 = medidas relativas a los hijos
V1a -> escucha activa: "alimentos"                        V1a = pension de alimentos
V1b -> escucha activa: "quiero dejar de pagar"            V1b = extinguir
V2 -> PREGUNTA: "La modificacion se plantea..." -> 2      V2 = contenciosa (no hay acuerdo previo con el otro progenitor)
V3 -> escucha activa: "trabaja... vive en su propio
       piso"                                              V3 = independencia economica del hijo
FILTRO DE VIABILIDAD: cambio = hijo independiente
       economicamente y sin convivencia; acreditable
       (nomina, contrato de alquiler); no imputable al
       solicitante; con vocacion de permanencia -> ENCAJA
HOJA -> assets/solicitud-extincion-pension-alimentos.md
```

### Momento de las preguntas
- Turno 1: introduccion fija + V2 (unico vector no resuelto por escucha activa).
- Turno 2: filtro de viabilidad, pregunta de acreditacion (que, desde cuando y como ya venian en el mensaje; solo se completa lo que falte).
- Turno 3: Confirmacion visible con cita Art. 93.2 y 152 CC.
- Turnos 4-6: parte solicitante, otra parte, alimentista (confirmacion agrupada cada bloque). La edad del hijo (26 anos) la calcula la skill a partir de la fecha de nacimiento, sin preguntarla directamente.
- Turno 7: resolucion de origen (transcripcion literal del pronunciamiento de alimentos).
- Turno 8: causa de extincion (negociacion) — YA resuelta por escucha activa (independencia economica); la skill explica el doble presupuesto del Art. 93.2 (no convivencia + sin ingresos propios) y pide los datos que faltan: ocupacion, empleador, fecha de inicio del empleo e ingresos aproximados, y confirma que el hijo no convive en el domicilio familiar.
- Turno 9: acreditacion de la causa (nomina, contrato de alquiler, empadronamiento).
- Turno 10: requerimiento extrajudicial previo (negociacion) — usuario decide enviarlo antes de demandar; sirve tambien de MASC.
- Turno 11: intento de solucion extrajudicial — se reutiliza el requerimiento anterior sin volver a pedir fechas.
- Turno 12: fecha de efectos solicitada (negociacion) — se explica la falta de retroactividad y se pide la fecha desde la que se interesa.
- Turno 13: subsistencia del resto de medidas (usuario confirma que no hay otros hijos con pension).
- Turno 14: prueba, juzgado, representacion y cierre.

### Documento generado (extracto relleno)
```
SOLICITUD DE EXTINCION DE LA PENSION DE ALIMENTOS — PROGENITOR C contra PROGENITOR D
> DRAFT — para revision por un abogado colegiado antes de su presentacion o firma.

HECHOS
[...]
La mayoria de edad por si sola no extingue la pension (Art. 93, parrafo segundo, CC); en este caso concurren ademas los dos presupuestos: el hijo, de 26 anos, no convive en el domicilio familiar desde {{fecha}} y percibe ingresos propios suficientes por su trabajo desde {{fecha}}, acreditado con nomina y contrato de alquiler.
[...]
SUPLICO: se declare extinguida la pension de alimentos desde {{fecha_efectos}}.
```
Resultado: **PASA**.

---

## Test 3 — Cambio de custodia consensuado

**Mensaje inicial:** "Mi ex pareja y yo estamos de acuerdo en pasar de custodia exclusiva mia a custodia compartida. Ya lo hemos hablado y estamos de acuerdo en el reparto de semanas."

### Recorrido del arbol
```
V1 -> escucha activa: "custodia"                          V1 = medidas relativas a los hijos
V1a -> escucha activa: "custodia... compartida"           V1a = guarda, custodia y regimen de estancias
V2 -> escucha activa: "estamos de acuerdo"                V2 = consensuada
FILTRO DE VIABILIDAD: cambio = acuerdo mutuo sobre
       reparto de tiempo, no imputable, con vocacion de
       permanencia -> ENCAJA
HOJA -> assets/demanda-modificacion-medidas.md (variante CONSENSUADA)
```
V1b y V3 no aplican (exclusivos de pension de alimentos/compensatoria).

### Momento de las preguntas
- Turno 1: introduccion fija; todos los vectores de clasificacion resueltos por escucha activa -> pasa directo al Filtro de Viabilidad.
- Turnos 2-3: filtro de viabilidad (que cambio y como se acredita el acuerdo; "desde cuando" ya contestado).
- Turno 4: Confirmacion visible con el texto de la variante CONSENSUADA (Art. 777 LEC, propuesta de nuevo convenio, intervencion del Ministerio Fiscal por haber hijos menores).
- Turnos 5-8: parte solicitante, otra parte, resolucion de origen, hijos afectados.
- Turno 9: la alteracion de circunstancias (negociacion) — se explica igual que en contenciosa pero mas breve, dado que ambas partes coinciden.
- Turno 10: documentacion economica — SE OMITE (exclusiva de la variante contenciosa, regla 1ª del Art. 770).
- Turno 11: intento de solucion extrajudicial — SE OMITE (exclusivo de contenciosa).
- Turno 12: acuerdo alcanzado y propuesta de nuevo convenio (negociacion) — se recoge el consentimiento por escrito de la otra parte y el reparto semanal concreto; la skill advierte de que un acuerdo danoso para los hijos no se aprobaria (Art. 90.2 CC) y verifica que el reparto no lo es.
- Turno 13: redaccion de la medida nueva (custodia compartida, calendario).
- Turno 14: modificacion provisional — SE OMITE (exclusiva de contenciosa).
- Turno 15: prueba — SE OMITE (exclusiva de contenciosa).
- Turno 16: juzgado, representacion y cierre.

### Documento generado (extracto relleno)
```
DEMANDA DE MODIFICACION DE MEDIDAS DEFINITIVAS (Art. 775 LEC, via consensuada) — PROGENITOR E y PROGENITOR F
> DRAFT — para revision por un abogado colegiado antes de su presentacion o firma.

Se acompana como Documento nº {{n}} la propuesta de nuevo convenio regulador, que establece un regimen de custodia compartida por semanas alternas.
```
Resultado: **PASA**. Ningun bloque de la variante contenciosa (MASC, documentacion economica de ambas partes, modificacion provisional, reconvencion) aparece en el documento.

---

## Contra-caso — Solicitante que dejo el trabajo voluntariamente

**Mensaje inicial:** "Deje mi trabajo hace 3 meses porque no me gustaba el ambiente. Ahora no tengo ingresos y quiero pedir que me bajen la pension que pago a mi hijo."

### Recorrido del arbol
```
V1/V1a/V1b/V2 resueltos por escucha activa (hijos,
   alimentos, reducir, sin indicar acuerdo -> contenciosa
   por defecto, se confirmara en la pregunta V2)
FILTRO DE VIABILIDAD:
  Que cambio -> "deje mi trabajo"
  Desde cuando -> "hace 3 meses"
  Como se acredita -> "la baja voluntaria"
  Evaluacion: cambio VOLUNTARIO e imputable al
    solicitante -> DETENER Y ADVERTIR (Guardrail 6)
```

### Comportamiento esperado
La skill NO continua hacia la Confirmacion ni crea ningun documento. En el mismo turno en que evalua el filtro, emite un unico mensaje con registro formal explicando que la modificacion exige que el cambio no sea imputable a quien lo alega, que una baja voluntaria expone la demanda a la desestimacion con imposicion de costas, y pregunta si desea continuar pese a ello. Solo si el usuario confirma expresamente, la skill continua y dej a constancia del riesgo en las advertencias finales del documento.

**Resultado: PASA.** El filtro de viabilidad detiene el flujo antes de crear cualquier documento, tal como exige el Guardrail 6, sin necesidad de que el usuario llegue a ver un escrito que probablemente seria desestimado.

---

## Revision UX

Hallazgos:
1. Situar el Filtro de Viabilidad (1.B) ANTES de la verificacion normativa y de la creacion del documento evita que un cliente con un cambio claramente imputable (contra-caso) llegue a ver un borrador de demanda: se le advierte en el primer o segundo turno, no al final del proceso.
2. Cuando los 4 vectores de clasificacion se resuelven por escucha activa (Test 1 y Test 3), pasar directamente al Filtro de Viabilidad sin preguntas de clasificacion en frio acorta notablemente el flujo para el caso mas comun (el usuario ya cuenta su situacion completa en el primer mensaje).
3. Calcular la edad del hijo a partir de la fecha de nacimiento (Test 2) en lugar de preguntarla directamente evita un dato redundante y permite validar coherencia si el usuario mencionara una edad distinta.
4. Separar netamente las secciones exclusivas de cada variante (MASC y documentacion economica solo en contenciosa; propuesta de convenio solo en consensuada) evita que aparezcan preguntas irrelevantes para el usuario segun su caso.
5. La advertencia de no retroactividad y del riesgo de generar una deuda ejecutable si se deja de pagar por cuenta propia aparece en todos los flujos de reduccion/extincion antes de cerrar la seccion de la medida nueva, no solo al final del documento: reduce el riesgo de que el cliente actue mal mientras el procedimiento esta en tramite.

Ajustes aplicados: ninguno adicional a los ya reflejados en el SKILL.md (orden Filtro de Viabilidad antes de Verificacion Normativa, y omision explicita por variante de las secciones 5-A.6/10/11 segun consensuada/contenciosa).

---

## Verificacion en vivo + calidad LLM

A diferencia de las secciones anteriores (recorrido del arbol sobre el papel), esta verificacion se **ejecuto de verdad**: me puse en el papel del LLM operativo gobernado por este SKILL.md sobre el mismo escenario del Test 1 ("Pago 400 euros al mes de pension de alimentos... Me despidieron hace 4 meses, cobro el paro... Mi ex mujer no quiere bajarla"), simulando las respuestas de PROGENITOR A / PROGENITOR B / HIJO MENOR 1, y apliquando `Write`, `Read` y varios `Edit` reales sobre `/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/modmedidas-qa-prueba.md`. Simplificacion declarada: no se realizo una consulta HTTP real al BOE (Punto 2); se reutilizo la fecha de verificacion ya registrada en `references/fuentes-plantillas-validadas.md` (31/08/2026, un dia antes de la fecha de la sesion), lo cual no afecta a lo que se evalua aqui (calidad del dialogo y del asset).

### Extractos literales del dialogo

Turno 1 (V1/V1a/V1b/V2 ya resueltos por escucha activa del mensaje inicial; "que ha cambiado" tambien resuelto — solo faltan fecha exacta y prueba):
> "Vamos a proceder a la preparación del escrito para modificar las medidas que ya rigen en su caso. Para ajustarlo correctamente, es necesario precisar antes algunos datos.
>
> Indique desde qué fecha exacta se produjo el despido que menciona."

Turno 2 (unica pregunta restante del Filtro de Viabilidad; evaluacion silenciosa: despido no imputable -> sin advertencia, se sigue sin decirlo):
> "Indique con qué documentación puede acreditarlo."

Turno 3 (Confirmacion, Punto 3, visible):
> "A su caso le resulta de aplicación la Ley 1/2000, de Enjuiciamiento Civil, artículo 775, que atribuye la modificación al Juzgado que acordó las medidas definitivas y exige que las circunstancias hayan variado sustancialmente, en relación con el artículo 90.3 y el artículo 91, párrafo último, del Código Civil, en su redacción vigente verificada el 31 de agosto de 2026. Al no prestar su consentimiento la otra parte, el procedimiento será el del artículo 770 de la Ley de Enjuiciamiento Civil, por los trámites del juicio verbal, y deberá acreditarse el intento previo de un medio adecuado de solución de controversias (Ley Orgánica 1/2025, de 2 de enero, artículo 5), sin el cual la demanda podría ser inadmitida (Ley 1/2000, artículo 264, apartado 4.º). Debe usted saber, además, que la otra parte podrá formular reconvención con su contestación y solicitar medidas distintas o contrarias a las que se piden (...). Puede consultar los textos oficiales en: https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 y https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763
>
> ¿Qué documento desea utilizar como base?
> 1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
> 2. Adjuntar su propio documento"

Turno de la seccion de negociacion "alteracion de circunstancias" (explica antes de pedir la decision, sin invocar sentencias):
> "Pasamos al núcleo del escrito: la alteración de circunstancias que justifica la modificación. Para que una alteración permita modificar las medidas debe ser sustancial, sobrevenida a la resolución de origen, acreditable documentalmente, ajena a la voluntad de quien la alega y con vocación de permanencia. El despido que usted describe reúne estos requisitos, al no constar que fuera voluntario. Le propongo la siguiente redacción del hecho: [...] ¿Confirmamos esta redacción?"

Turno de MASC (rama distinta de la del Test 1 en papel: aqui el cliente SI habia iniciado un contacto informal, y la skill lo redirige a un medio acreditable en lugar de darlo por valido sin mas):
> "Un intercambio de mensajería instantánea puede en principio servir de negociación directa entre las partes, pero conviene dejar constancia más solvente del intento y de su fecha, dado que sin ese respaldo documental la demanda podría ser inadmitida. Le recomiendo remitir un burofax con el mismo objeto de esta demanda antes de presentarla. ¿Desea hacerlo?"

Turno de la medida nueva (NEGOCIACION), con la explicacion de no retroactividad exigida por el Guardrail 8 antes de pedir la decision:
> "Corresponde ahora redactar exactamente la medida que se solicita en sustitución de la vigente. La medida debe pedirse redactada de forma completa y autónoma [...]. Debo advertirle, además, de que la modificación no rige hacia atrás de la interposición de la demanda: lo devengado conforme a la resolución vigente sigue siendo exigible y ejecutable, y dejar de pagar por cuenta propia mientras se tramita el procedimiento genera una deuda ejecutable que puede tener consecuencias penales. ¿Qué importe y condiciones desea solicitar?"

### Veredicto A — calidad de la respuesta del LLM

**PASA.** Tono formal de "usted" sostenido en todo el dialogo, sin coloquialismos ("adelante", "vale" solo aparecen en boca del cliente simulado, nunca del agente). Cero menciones de vectores/fases (nunca se dice "V1", "V4", "Punto 3"). El filtro de viabilidad se aplico de forma silenciosa y correcta: como el despido no es imputable, NO aparece ninguna advertencia de riesgo en el chat — comportamiento correcto (la advertencia solo debe salir en el caso contrario, ya cubierto en el contra-caso del Test 3). La explicacion de la no retroactividad aparece ANTES de pedir la redaccion de la medida nueva, tal como exige el Guardrail 8, y no se afirma un criterio pacifico sobre si la modificacion rige desde la demanda o desde la sentencia. Ningun dato se invento: los datos economicos, el burofax y sus fechas fueron aportados por el cliente simulado, nunca supuestos por el agente. Unico matiz: al no intentar el cliente un MASC formal desde el principio, el agente reconduce con criterio (sugiere burofax) en vez de aceptar sin mas un wasap como prueba solida — buena aplicacion practica del Art. 5 LO 1/2025, no exigida literalmente por el SKILL.md pero coherente con el.

### Veredicto B — calidad del asset visto desde el LLM que lo rellena

**PASA CON DEFECTOS REALES ENCONTRADOS Y CORREGIDOS.** Al rellenar el asset se detectaron dos bugs de numeracion hardcodeada en `assets/demanda-modificacion-medidas.md` (ninguno de los dos evidente sobre el papel, solo al ejecutar de verdad un caso y pensar en el caso contrario):

1. **HECHOS "CUARTO"/"QUINTO" fijos como texto literal**, pese a ser bloques condicionales (economico y MASC). En una modificacion de custodia/visitas por via contenciosa (no patrimonial), el bloque CUARTO no se activa pero el QUINTO (MASC) si, produciendo un salto TERCERO -> QUINTO que incumple la propia regla del SKILL.md ("el documento escrito no puede contener saltos ni duplicados en la numeracion", Punto 4.2). Corregido: ambos pasan a `{{numero_hecho_economico}}` / `{{numero_hecho_masc}}`, igual que ya hacia la seccion de FUNDAMENTOS DE DERECHO con `{{numero_fundamento_fondo}}` etc. Tambien se actualizo la referencia cruzada del Fundamento IV ("segun resulta del hecho {{numero_hecho_masc}}").
2. **Mismo bug en la numeracion de "Documento nº 3/4/5"**: asumen siempre que existe un "Documento nº 2" (certificaciones de nacimiento de los hijos). Si no hay hijos afectados (p. ej., modificacion exclusiva de pension compensatoria), el Documento nº 2 no existe y el nº 3 queda mal numerado. Corregido con `{{numero_documento_cambio}}`, `{{numero_documento_economico}}` y `{{numero_documento_masc}}`.

En el caso concreto probado (hijo + patrimonial + contenciosa) ninguno de los dos bugs se manifestaba — se detectaron razonando sobre el combinatoria de bloques, no por fallo visible en este documento. Aparte de ello, la plantilla funciono bien: los placeholders son inequivocos, la transcripcion literal del pronunciamiento vigente y la redaccion de la medida nueva salen naturales y completas (importe en numero y letra, dia de pago, cuenta, sistema de actualizacion, clausula de revision), y el bloque MASC se pudo insertar limpiamente en el punto correcto una vez conocido el dato, sin dejar comentarios HTML ni placeholders huerfanos.

### Autocorreccion durante la propia ejecucion

Al hacer el `Write` inicial, cometi yo mismo el error que el encargo pedia vigilar: inserte un encabezado "QUINTO" con un placeholder inventado (`{{contenido_hecho_masc}}`, que no existe en el asset) antes de conocer si habia MASC o no, incumpliendo la regla de "cero comentarios HTML / omitir hasta conocer el dato" del propio SKILL.md (Punto 4.2). Tambien deje un placeholder inventado `{{otrosi_segundo_provisional}}` para el bloque de modificacion provisional, aun sin resolver. Ambos se detectaron y corrigieron con `Edit` antes de continuar (eliminando el bloque hasta que llego el dato real), dejando el documento consistente con la regla de placeholders con nombre propio (Guardrail 11).

### Documento final generado

`/Users/yruiz/Documents/Mio/pluggin-builder/test-local/output/modmedidas-qa-prueba.md` — demanda contenciosa completa: partes identificadas, resolucion de origen (sentencia de divorcio de mutuo acuerdo, Juzgado de Primera Instancia nº 8 de Madrid, 456/2021) con transcripcion literal de la medida vigente (400 €/mes), hijo identificado, alteracion sustancial (despido no imputable, acreditado), documentacion economica, MASC via burofax, medida nueva (150 €/mes con clausula de revision), OTROSI de prueba y de modificacion provisional, y advertencias finales. Quedan con su placeholder propio `{{nombre_procurador}}` y `{{nombre_letrado}}`, aun no designados por el cliente.
