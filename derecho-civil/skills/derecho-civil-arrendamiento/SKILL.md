---
name: derecho-civil-arrendamiento
description: >
  Genera los documentos del ciclo completo del arrendamiento urbano: contratos nuevos (vivienda
  habitual, local de negocio, vivienda por temporada y habitacion) y comunicaciones sobre contratos
  vigentes (actualizacion anual de la renta, no renovacion a vencimiento y requerimiento de
  devolucion de fianza). Aplica la Ley 29/1994 de Arrendamientos Urbanos (LAU), la Ley 12/2023 por
  el derecho a la vivienda (zonas de mercado residencial tensionado, IRAV) y el Codigo Civil
  (habitacion, arts. 1542 y ss.), en sus versiones consolidadas vigentes verificadas en el BOE.
  Adapta las clausulas segun la naturaleza de las partes (persona fisica o juridica) y la ubicacion
  del inmueble. NO usar para arrendamientos de finca rustica, viviendas turisticas (Art. 5.e LAU),
  viviendas militares, ni viviendas de porteros o guardas.
when_to_use: |
  - El usuario quiere redactar un contrato de alquiler de vivienda, de local, de temporada o de habitacion.
  - El usuario quiere comunicar a la otra parte la actualizacion de la renta, la no renovacion del contrato, o requerir la devolucion de la fianza de un contrato ya extinguido.
  - El usuario proporciona datos de arrendador, arrendatario e inmueble.
  - El usuario pide que el documento cumpla con la LAU o la normativa de vivienda vigente.
inputs:
  - tipo_gestion: contrato nuevo o comunicacion sobre contrato vigente
  - tipo_inmueble: vivienda (completa o habitacion) o local de negocio / uso distinto de vivienda
  - finalidad_uso: permanente o temporal (temporada); turistico queda fuera de alcance
  - zona_tensionada: si / no / no lo se (solo vivienda habitual; verificable por el agente)
  - tipo_comunicacion: actualizacion de renta, no renovacion o devolucion de fianza (solo si comunicacion)
  - remitente_comunicacion: arrendador o arrendatario (solo si comunicacion)
  - naturaleza_arrendador: persona fisica o persona juridica
  - naturaleza_arrendatario: persona fisica o persona juridica
  - datos_arrendador: nombre o razon social, NIF o CIF, domicilio
  - datos_arrendatario: nombre o razon social, NIF o CIF, domicilio
  - datos_inmueble: direccion completa, referencia catastral, descripcion, comunidad autonoma, municipio
  - causa_temporada: causa real y acreditable de la temporalidad (solo temporada)
  - datos_habitacion: identificacion de la habitacion, zonas comunes, normas de convivencia (solo habitacion)
  - renta_mensual: importe en euros
  - duracion: anos pactados o "minimo legal" (contratos); fechas de inicio y fin (temporada y habitacion)
  - fianza: mensualidades o "segun ley"
  - fecha_inicio: fecha de inicio del contrato
  - datos_contrato_vigente: fecha del contrato, vencimiento, renta vigente, fechas de extincion y entrega de llaves (solo comunicaciones)
  - clausulas_adicionales: opcionales, a peticion del usuario
outputs:
  - contrato_arrendamiento: contrato completo en markdown, DRAFT, con las clausulas del regimen legal aplicable
  - comunicacion_arrendaticia: carta breve en markdown, DRAFT, lista para envio por burofax
references:
  - references/lau-vivienda-plazos-renta-fianza.md
  - references/lau-derechos-obligaciones-partes.md
  - references/lau-arrendamiento-local-negocio.md
  - references/temporada-habitacion-comunicaciones.md
  - references/fuentes-plantillas-validadas.md
assets:
  - assets/contrato-arrendamiento-vivienda.md
  - assets/contrato-arrendamiento-local.md
  - assets/contrato-arrendamiento-temporada.md
  - assets/contrato-arrendamiento-habitacion.md
  - assets/comunicacion-actualizacion-renta.md
  - assets/comunicacion-no-renovacion.md
  - assets/requerimiento-devolucion-fianza.md
---

# Generar Documentos de Arrendamiento Urbano

> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico.

## 0. CONFIRMACION DE CARGA Y ARRANQUE (visible, una sola vez)

Al cargarse esta skill, lo PRIMERO que emites en el chat, antes de cualquier otro texto, es esta linea fija:

**Skill cargada satisfactoriamente.**

A continuacion, en el MISMO mensaje y sin esperar ninguna confirmacion del usuario, ARRANCAS la ejecucion del procedimiento: emite la introduccion fija que la skill defina y, seguidamente, la primera pregunta que no haya quedado ya resuelta por Escucha Activa. Si el procedimiento arranca con una verificacion normativa interna, ejecutala en silencio y continua hasta la primera pregunta o hasta la Confirmacion visible, segun corresponda.

PROHIBIDO detenerse tras la linea de carga, preguntar si desea empezar, o emitir la linea a solas en un turno propio: la skill queda cargada y en ejecucion en ese mismo turno.

Esta linea es, junto con la introduccion fija, la UNICA excepcion a la prohibicion de mencionar la mecanica interna. Se emite una sola vez, al cargar, y no se repite en ningun turno posterior.

## Guardrails

1. Verificar siempre la normativa aplicable en el BOE antes de redactar (LAU; Ley 12/2023 e IRAV si vivienda habitual; Codigo Civil si habitacion). Sin verificacion, no proceder.
2. Si se detecta en el BOE una version de una norma posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Punto 2). No usar una version desactualizada.
3. Duracion minima en vivienda habitual: 5 anos si el arrendador es persona fisica, 7 anos si es persona juridica (Art. 9.1 LAU). No pactar plazos inferiores sin advertir de la prorroga obligatoria. En temporada, habitacion y local NO aplican los plazos minimos ni las prorrogas del Titulo II.
4. Gastos de gestion y formalizacion del contrato de vivienda siempre a cargo del arrendador (Art. 20.1 LAU).
5. En zonas de mercado residencial tensionado, aplicar los limites de renta de los Arts. 17.6 y 17.7 LAU y advertir de la prorroga extraordinaria del Art. 10.3 LAU. La declaracion de zona es un dato publico verificable (boletin oficial autonomico): contrastarla siempre, aunque el cliente crea conocer la respuesta.
6. Actualizacion de renta en vivienda habitual: en contratos celebrados desde el 26/05/2023, el incremento anual no puede superar el IRAV publicado por el INE (Resolucion INE 18/12/2024, BOE-A-2024-26685, vigente desde 01/01/2025). No redactar clausulas de actualizacion por encima de ese limite ni comunicaciones de actualizacion con porcentaje superior al IRAV vigente.
7. Fianza minima legal: 1 mensualidad en vivienda habitual, 2 mensualidades en local y en temporada (uso distinto de vivienda, Art. 36.1 LAU). No admitir fianzas inferiores. En habitacion (Codigo Civil) la fianza es de libre pacto. Garantias adicionales en vivienda de hasta 5/7 anos: maximo 2 mensualidades (Art. 36.5 LAU).
8. Arrendamiento de temporada: exigir una causa de temporalidad real y acreditable. NUNCA redactar un contrato de temporada para encubrir una residencia habitual y permanente (fraude de ley): si se detecta esa intencion, rechazar, explicar la recalificacion como vivienda (Titulo II LAU) y ofrecer el contrato de vivienda.
9. Comunicacion de no renovacion (Art. 10.1 LAU): preaviso minimo de 4 meses si comunica el arrendador y 2 meses si comunica el arrendatario, contados desde el vencimiento hacia atras. Verificar SIEMPRE las fechas antes de redactar; si el preaviso ya no llega, advertir de que la comunicacion seria extemporanea y de que el contrato se prorrogaria.
10. Requerimiento de devolucion de fianza: solo procede transcurrido 1 mes desde la entrega de llaves (Art. 36.4 LAU). Verificar las fechas; antes de ese mes, no redactar el requerimiento sin advertirlo.
11. Marcar todos los campos a rellenar como placeholder pendiente. Use el nombre propio de la plantilla (p. ej. `{{nombre_arrendador}}`, `{{referencia_catastral}}`): NO lo sustituya por un literal genérico como `{{DATO_FALTANTE}}`, que se repetiría idéntico en múltiples campos y rompería la precisión quirúrgica del `Edit` (oldString ambiguo) al rellenar cada uno por separado. Nunca inventar datos, rentas, fechas ni referencia catastral.
12. Nunca redactar clausulas que contravengan normas imperativas de la ley aplicable. Nunca inventar jurisprudencia.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la lógica descrita en este documento (la clasificación de vectores V0-V8, las secuencias numeradas, la verificación normativa y la creación del documento base) es un flujo de ejecución ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2").
- Resúmenes de validación con checks (ej. "Finalidad: ✔").
- En qué fase de la instrucción te encuentras (ej. "Ahora pasaremos al punto 4", "Voy a proceder a crear el documento").
- Preámbulos conversacionales antes de hacer las preguntas de clasificación. Si es tu turno de preguntar, **emite únicamente la pregunta exacta y nada más** — con la única excepción de la línea de carga del Punto 0, de la introducción fija del Punto 1 (ver más abajo), que solo se usa una vez, en el primer turno de toda la conversación.

## 1. CLASIFICACIÓN DINÁMICA (Vectores de Estado)

**Introducción (solo en el primer turno, una única vez):** antes de la primera pregunta de este árbol, y solo la primera vez, añade en el mismo mensaje esta introducción fija, con tono de abogado (usted, formal, sin coloquialismos). No afirmes todavía qué norma aplica (el Punto 1 aún no ha determinado si el caso se rige por el Título II de la LAU, por su Título III, por el Código Civil o queda fuera de alcance, Art. 5.e):

"Vamos a proceder a la elaboración de su documento de arrendamiento. Para ajustarlo correctamente a su caso, es necesario precisar antes algunos datos."

No repitas esta introducción en turnos posteriores: es exclusiva del primer mensaje de la conversación, antes de la primera pregunta de clasificación.

Tu primer objetivo es resolver los vectores de clasificación de manera SILENCIOSA.
Aplica la Escucha Activa Global para extraer estos datos de cualquier mensaje.
**IMPORTANTE (Invisibilidad):** Los nombres de estos vectores (`V0`, `V1`, etc.) y el hecho de que estás validándolos son de uso estrictamente interno. **NUNCA los menciones en el chat.** No imprimas listas de validación ni resúmenes con "checks" (✔). Si extraes un dato con éxito, simplemente regístralo en tu memoria en silencio.

- **V0 (Gestión):** Contrato nuevo / Comunicación sobre un contrato ya en vigor (actualización de renta, no renovación, devolución de fianza).
- **V2 (Tipo Inmueble):** Vivienda (incluye: piso, casa, apartamento, chalet — completa o una habitación) / Local (incluye: nave, comercial). *(Solo si V0 = Contrato.)*
- **V5 (Alcance — solo si V2 = Vivienda):** Vivienda completa / Habitación (una habitación de la vivienda, con uso compartido de zonas comunes — se rige por el Código Civil, arts. 1542 y ss., no por la LAU).
- **V1 (Finalidad — solo si V2 = Vivienda y V5 = Vivienda completa):** Permanente (residencia habitual, Art. 2 LAU) / Temporal (temporada —vacacional, de verano, por trabajo o estudios temporales, uso distinto de vivienda del Art. 3.2 LAU, sin plazos mínimos ni protecciones del Título II— o vivienda turística —uso inmediato comercializado en canales de oferta turística, sujeta a normativa autonómica, excluida de la LAU, Art. 5.e—).
- **V6 (Zona tensionada — solo si V1 = Permanente, o si V0 = Comunicación de no renovación con V8 = Arrendador):** Sí / No / No lo sé. Es un dato público (boletín oficial autonómico): "No lo sé" es respuesta válida y el agente lo verifica por sí mismo en la edición incremental.
- **V3 (Naturaleza Arrendador):** Física / Jurídica (empresa). *(Solo contratos; en habitación determina el bloque de representante del arrendador.)*
- **V4 (Naturaleza Arrendatario):** Física / Jurídica (empresa). *(Solo contratos de vivienda habitual, local y temporada. En habitación el arrendatario es siempre persona física: no preguntar.)*
- **V7 (Tipo de comunicación — solo si V0 = Comunicación):** Actualización de renta / No renovación / Devolución de fianza.
- **V8 (Remitente — solo si V0 = Comunicación y V7 = Actualización o No renovación):** Arrendador / Arrendatario. *(En devolución de fianza el remitente es siempre el arrendatario: no preguntar.)*

**Criterio legal para resolver V1 en caso de ambigüedad:** lo decisivo no es la palabra que use el usuario sino la naturaleza del uso — duración limitada y predeterminada por causa distinta de la residencia (temporada) o comercialización como alojamiento (turístico) excluyen el régimen de vivienda habitual. Si la respuesta no permite distinguir con claridad (p. ej. "es para vivir un tiempo"), repite la pregunta de V1 pidiendo esa aclaración concreta en vez de asumir "permanente".

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si, tras analizar el contexto, te falta resolver uno o más vectores, **TIENES PROHIBIDO inventar la redacción de la pregunta**. Debes formular **UNA SOLA PREGUNTA por turno**, utilizando EXACTAMENTE el texto que corresponda al vector faltante, en este orden estricto, **sin añadir preámbulos ni resúmenes de lo que ya sabes**. Cada pregunta se presenta como texto libre seguido de las alternativas numeradas: el usuario responde con el número o con la palabra, nunca con texto libre sin opciones:

*   **Para V0 (Gestión):**
    "La gestión que desea realizar es:
    1. Redactar un contrato de arrendamiento nuevo
    2. Remitir una comunicación sobre un contrato ya en vigor"
*   **Para V7 (Tipo de comunicación — solo si V0 = Comunicación):**
    "La comunicación que desea remitir es:
    1. Actualización anual de la renta
    2. No renovación del contrato a su vencimiento
    3. Requerimiento de devolución de la fianza"
*   **Para V8 (Remitente — solo si V7 = Actualización o No renovación):**
    "Quien remite la comunicación es:
    1. El arrendador
    2. El arrendatario"
*   **Para V2 (Tipo Inmueble — solo si V0 = Contrato):**
    "El inmueble objeto del arrendamiento es:
    1. Vivienda
    2. Local de negocio"
*   **Para V5 (Alcance — solo si V2 = Vivienda):**
    "El arrendamiento comprende:
    1. La vivienda completa
    2. Una habitación de la vivienda"
*   **Para V1 (Finalidad — solo si V5 = Vivienda completa):**
    "El uso será:
    1. Permanente, sin plazo predeterminado
    2. Temporal (de temporada o alojamiento turístico)"
*   **Para V1-b (solo si V1 = Temporal y no queda claro cuál de las dos):**
    "El uso temporal es:
    1. De temporada (por ejemplo, de verano o por trabajo)
    2. Alojamiento turístico"
*   **Para V6 (Zona tensionada — solo en los casos indicados arriba):**
    "¿Se encuentra el inmueble en una zona declarada de mercado residencial tensionado?
    1. Sí
    2. No
    3. No lo sé"
*   **Para V3 (Naturaleza Arrendador):**
    "El arrendador es:
    1. Persona física
    2. Empresa (persona jurídica)"
*   **Para V4 (Naturaleza Arrendatario):**
    "El arrendatario es:
    1. Persona física
    2. Empresa (persona jurídica)"

*(Si el usuario ya proporcionó la respuesta a un vector, OMITE la pregunta exacta correspondiente y evalúa el siguiente. Si responde con el número, interpreta la opción correspondiente exactamente igual que si hubiera escrito la palabra).*

### Enrutamiento de Estado (Routing)
Una vez resueltos los vectores necesarios, evalúa:
- Si [V0 = Comunicación] y [V7 = Actualización de renta] -> Plantilla a usar: `assets/comunicacion-actualizacion-renta.md`.
- Si [V0 = Comunicación] y [V7 = No renovación] -> Plantilla a usar: `assets/comunicacion-no-renovacion.md`.
- Si [V0 = Comunicación] y [V7 = Devolución de fianza] -> Plantilla a usar: `assets/requerimiento-devolucion-fianza.md` (remitente: arrendatario. Si quien consulta es el arrendador que quiere CONTESTAR a un requerimiento recibido, detén el proceso y deriva a `escalate_to_attorney`).
- Si [V0 = Contrato] y [V2 = Local] -> Plantilla a usar: `assets/contrato-arrendamiento-local.md` (Fianza mínima: 2 mensualidades). La duración del local es de libre pacto (Título III LAU): no aplica V1.
- Si [V0 = Contrato] y [V2 = Vivienda] y [V5 = Habitación] -> Plantilla a usar: `assets/contrato-arrendamiento-habitacion.md` (régimen del Código Civil, arts. 1542 y ss.; fianza de libre pacto). No aplican V1 ni V6.
- Si [V0 = Contrato] y [V5 = Vivienda completa] y [V1 = Permanente] -> Plantilla a usar: `assets/contrato-arrendamiento-vivienda.md` (Fianza mínima: 1 mensualidad). V6 determina los bloques de zona tensionada del asset (Arts. 10.3, 17.6 LAU); si V6 = No lo sé, se resuelve en la sección 1 de la edición incremental.
- Si [V0 = Contrato] y [V5 = Vivienda completa] y [V1 = Temporal] identificado como temporada -> Plantilla a usar: `assets/contrato-arrendamiento-temporada.md` (uso distinto de vivienda, Art. 3.2 LAU; fianza mínima: 2 mensualidades). Exige causa de temporalidad real (Guardrail 8).
- Si [V1 = Temporal] identificado como turístico -> Detén el proceso: vivienda turística excluida expresamente de la LAU (Art. 5.e), sujeta a normativa turística autonómica. No crees documento.

---

## 2. VERIFICACIÓN Y AUTO-ACTUALIZACIÓN NORMATIVA BOE (Interno)

Una vez completado el Enrutamiento (Punto 1), no hagas más preguntas al usuario. La skill se actualiza a sí misma en cada lanzamiento: comprueba la fuente oficial y, si detecta una versión posterior, reescribe sus propios archivos antes de redactar. Ejecuta SIEMPRE esta secuencia:

**2.1 — Leer la versión registrada localmente.** Abre `references/fuentes-plantillas-validadas.md` y anota la "Versión registrada" de cada norma aplicable a la ruta resuelta en el Punto 1.

**2.2 — Consultar la fuente oficial vigente.** Usa la herramienta de lectura de documentos para leer, en formato texto, las URLs que correspondan a la ruta:
- Siempre (salvo habitación): LAU, https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003 — fecha del texto consolidado vigente; redacción actual de los arts. 3.2 (temporada), 9-11 (duración, prórroga y preaviso de no renovación), 17-20 (renta, actualización 18.2 y gastos), 27 (resolución) y 36 (fianza: 36.1, 36.4 y 36.5).
- Si la ruta es vivienda habitual, o comunicación de actualización de renta o de no renovación: Ley 12/2023, https://www.boe.es/buscar/act.php?id=BOE-A-2023-12203 (zonas tensionadas, prórroga extraordinaria) y, para la actualización de renta, el valor vigente del IRAV publicado por el INE (https://www.ine.es/uc/oC7D0Ncd; definición en https://www.boe.es/diario_boe/txt.php?id=BOE-A-2024-26685).
- Si la ruta es habitación: Código Civil, arts. 1542 y ss., https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763.

**2.3 — Comparar.** Contrasta la versión oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la versión oficial es posterior o el texto de los artículos cambió, usa `Write`/`Edit` para:
- Actualizar el contenido afectado en `references/lau-vivienda-plazos-renta-fianza.md`, `references/lau-derechos-obligaciones-partes.md`, `references/lau-arrendamiento-local-negocio.md` y/o `references/temporada-habitacion-comunicaciones.md` con la redacción vigente.
- Actualizar la tabla "Versión registrada" y la fecha en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detectó y aplicó una versión más reciente (norma y fecha).

No redactes ningún documento hasta haber completado esta actualización. Nunca uses una versión desactualizada.

**2.5 — Fallback si la fuente no es accesible.** Si la lectura del BOE falla (error HTTP, timeout), busca en la web la norma afectada (p. ej. "Ley 29/1994 Arrendamientos Urbanos texto consolidado BOE articulos 9 17 20 27 36", "IRAV INE valor vigente"). Si también falla, usa las references locales como respaldo y notifica al usuario: "No se pudo verificar la versión vigente de la normativa en el BOE. El documento se genera con la versión de referencia. Verificar manualmente antes de firmar."

---

## 3. CONFIRMACIÓN (visible al usuario)

A diferencia de los Puntos 1 y 2, esta sección **es visible** para el usuario — no es lógica interna. Tras completar la verificación normativa (Punto 2), en un único mensaje:

**3.1 — Informa la norma aplicable.** Indica qué ley y qué artículos concretos aplican al caso ya clasificado (Punto 1), con la versión vigente verificada (Punto 2). Incluye SIEMPRE el enlace al BOE o a la ley (la misma URL consultada en el Punto 2.2), para que el usuario pueda verificarlo por su cuenta. Registro de tratamiento formal (usted), tono de abogado — preciso, sin coloquialismos. Cita según la ruta:
- Vivienda habitual: Ley 29/1994 (LAU), arts. 2 y 9 (vivienda habitual y duración), 17 a 20 (renta y gastos) y 36 (fianza); si zona tensionada, además Ley 12/2023 y arts. 10.3, 17.6 y 17.7 LAU. Ejemplo: "Al presente caso le resulta de aplicación la Ley 29/1994, de Arrendamientos Urbanos (LAU), en concreto los artículos 2 y 9 (vivienda habitual y duración), 17 a 20 (renta y gastos) y 36 (fianza), en su versión consolidada vigente desde el 25/05/2023 (Ley 12/2023). Puede consultar el texto oficial en el BOE en el siguiente enlace: https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003"
- Local: Ley 29/1994 (LAU), art. 3 y Título III (arts. 29 a 35) y 36 (fianza).
- Temporada: Ley 29/1994 (LAU), art. 3.2 (arrendamiento de temporada, uso distinto de vivienda), Título III y 36 (fianza de 2 mensualidades).
- Habitación: Código Civil, arts. 1542 y siguientes (arrendamiento de cosas), por quedar fuera del ámbito del art. 2.1 de la LAU conforme al criterio mayoritario de las Audiencias Provinciales.
- Comunicaciones: el artículo que da fundamento a la comunicación (18 y 18.2 —actualización, con el valor del IRAV vigente si procede—; 10.1 —no renovación, con el preaviso de 4 o 2 meses según el remitente—; 36.4 —devolución de fianza—).

**3.2 — Ofrece la plantilla o pide el documento propio.** En el mismo mensaje, informa de que se dispone de una plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores, basada en esa normativa, y pregunta cuál usar como base (alternativas numeradas: es una decisión que cambia el flujo, igual que las preguntas de clasificación del Punto 1):

"¿Qué documento desea utilizar como base?
1. La plantilla de ConfidentialAI, revisada por nuestros abogados y colaboradores
2. Adjuntar su propio documento"

**3.3 — Enrutamiento según la respuesta:**
- Si elige la plantilla de ConfidentialAI -> continuar con el Punto 4 usando el asset correspondiente a la ruta del Punto 1.
- Si elige adjuntar su propio documento -> pedirle que lo adjunte o pegue su contenido, leerlo con `Read`, y usarlo como documento base en el Punto 4 en lugar del asset. Se le siguen aplicando los mismos guardrails legales (mínimos de duración y fianza, gastos a cargo del arrendador, límites de zonas tensionadas e IRAV, causa real de temporada, plazos de preaviso): si el documento adjuntado los incumple, adviértelo antes de continuar con la edición incremental.

---

## 4. CREACIÓN DEL DOCUMENTO BASE (Cero Vacíos)

Inmediatamente después de la Confirmación (Punto 3), estás OBLIGADO a crear el documento en disco.
1. Utiliza `Read` para leer el documento base decidido en el Punto 3 (la plantilla del Punto 1, o el documento que adjuntó el usuario).
2. Reemplaza en memoria las variables de clasificación y CUALQUIER OTRO DATO que ya poseas gracias a la escucha activa inicial (nombres, dirección, etc.).
3. Utiliza `Write` para guardar el archivo completo en disco. Los datos faltantes deben quedar intactos como `{{DATO_FALTANTE}}`.
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. En esa MISMA respuesta, sin turno intermedio y sin preguntar si desea empezar, emite el anuncio fijo de la primera seccion y formula ya su primera pregunta, para que el flujo no se detenga (regla del `CLAUDE.md` raiz, seccion 6.1, punto 5, y coherencia con el Punto 0: la skill esta en ejecucion desde que se carga).

---

## 5. EDICIÓN INCREMENTAL DE CLÁUSULAS

Ahora, recorre secuencialmente la lista de secciones de la ruta resuelta en el Punto 1 (5.A para contratos, 5.B para comunicaciones). Por cada sección de la que falten datos, aplica el Ciclo de Edición Incremental del sistema global (Formular Pregunta -> Mostrar Vista Previa en texto plano -> Pedir Confirmación -> Tras confirmación, usar `Edit` en disco). **A diferencia de las preguntas de clasificación (Punto 1), estas son preguntas de relleno de datos: se piden en prosa natural y el cliente responde con texto libre (nombres, direcciones, importes), no con alternativas numeradas. Solo cuando una pregunta de esta sección tenga un numero pequeño y cerrado de respuestas posibles (ej. zona tensionada: sí/no/no lo sé) se ofrecen esas opciones, sin forzar a numerar los datos que son texto libre. Un dato por turno: si un punto de esta lista agrupa más de un dato (aunque sean de la misma parte o cláusula), pídalos en turnos separados, nunca juntos en el mismo mensaje — cada sub-apartado (a, b, c...) es su propio turno. **Validación de sentido, no solo de formato:** usted es un LLM, no un formulario — no acepte mecánicamente cualquier texto que el cliente escriba como si fuera automáticamente un dato válido. Antes de darlo por bueno, razone si la respuesta tiene sentido en el contexto de lo preguntado (más allá de la coherencia nombre/naturaleza o el formato de un documento de identidad, ya cubiertos en el Punto 2). Si la respuesta es absurda, imposible o claramente no responde a lo preguntado (p. ej., "un cohete" como elemento accesorio de una vivienda), no la escriba en el documento: dialogue con el cliente, señale por qué no encaja y pida que lo aclare, antes de continuar al siguiente dato.**

**Anuncio de sección (visible, sin esperar confirmación aparte):** al terminar una sección (aplicado su `Edit`, o la confirmación agrupada de la sección de partes) y antes de la primera pregunta de la sección siguiente, añada en el mismo mensaje el anuncio fijo de esa sección (tono de abogado, usted, sin coloquialismos), y a continuación la pregunta. No pida permiso para pasar de sección: informe y continúe en el mismo turno. Estos anuncios son de la sección SUSTANTIVA del documento, identificable por el cliente (ubicación, partes, objeto...); sigue estrictamente prohibido nombrar vectores, puntos numerados o fases de la instrucción interna (Directiva de Invisibilidad).

**Diálogo y acuerdo en las cláusulas de negociación entre partes:** no todas las cláusulas son datos objetivos (nombre, dirección, NIF): algunas implican una decisión o un pacto entre arrendador y arrendatario con consecuencias legales — duración y prórrogas, renta y su índice de actualización, fianza y garantías adicionales, reparto de gastos, límites de renta en zona tensionada, causa de la temporada, normas de convivencia, pactos opcionales (adquisición preferente, mediación). En esas cláusulas no se limite a registrar el número o la opción que dé el cliente: explique brevemente el régimen legal por defecto o la implicación relevante (p. ej., que los gastos de gestión son siempre del arrendador por el Art. 20.1 LAU, que una duración inferior al mínimo legal se prorroga igualmente, que la actualización no puede superar el IRAV, o que la garantía adicional no puede exceder de 2 mensualidades por el Art. 36.5 LAU), y confirme que el cliente entiende y está de acuerdo antes de escribirlo en el documento. Esto es dialogar y llegar a un acuerdo, no una simple confirmación mecánica de dato. Cada sección de las listas siguientes está marcada como **[negociación]** o **[dato objetivo]**.

### 5.A — Contratos (vivienda habitual, local, temporada, habitación)

Anuncios fijos (vivienda habitual; para las variantes de otras rutas, ver las notas de cada sección):
- Al abrir la sección 1 (tras la confirmación de comenzar, Punto 4.4): "Procedemos a determinar la ubicación del inmueble, a los efectos de verificar su posible sujeción a los límites de renta en zona de mercado residencial tensionado." — En local, temporada y habitación, donde no aplican esos límites, el anuncio es: "Procedemos a determinar la ubicación del inmueble."
- Al pasar a la sección 2: "Concluida la ubicación del inmueble, pasamos a la identificación de las partes contratantes."
- Al pasar a la sección 3: "Identificadas las partes, procede determinar el objeto del contrato."
- Al pasar a la sección 4: "Determinado el objeto, corresponde fijar la duración del arrendamiento."
- Al pasar a la sección 5: "Fijada la duración, procede establecer la renta pactada."
- Al pasar a la sección 6: "Establecida la renta, corresponde determinar su índice de actualización." — Solo vivienda habitual y local; en temporada y habitación esta sección se omite salvo que la duración pactada supere el año.
- Al pasar a la sección 7: "Procedemos a fijar la fianza y, en su caso, las garantías adicionales."
- Al pasar a la sección 8: "Corresponde ahora determinar el reparto de gastos y suministros."
- Al pasar a la sección 9: "Por último, procede recoger los pactos opcionales que las partes deseen incorporar." — En habitación: "Por último, procede fijar las normas de uso y convivencia y los pactos opcionales."

1. **Ubicación y Zona Tensionada [dato objetivo, verificado por el agente]:** Pregunte únicamente la comunidad autónoma y el municipio del inmueble (texto libre). **Solo vivienda habitual:** la declaración de zona de mercado residencial tensionado es un dato público, publicado en el boletín oficial autonómico correspondiente (o en el BOE, si la declaración es estatal): en cuanto tenga el municipio, verifíquelo usted mismo con `web_search` (p. ej. "zona mercado residencial tensionado [municipio] [comunidad autónoma] boletín oficial"), priorizando el boletín oficial correspondiente como fuente frente a resultados no oficiales, e informe del resultado en la vista previa de la cláusula, sin necesidad de que el cliente confirme el dato. Si el resultado verificado contradice lo indicado en la clasificación (V6), prevalece la fuente oficial: infórmelo y ajuste los bloques del contrato. En local, temporada y habitación no hay verificación de zona tensionada.
2. **Partes (un dato por turno dentro de cada parte, pero confirmación agrupada por parte — no confirme dato a dato):** pregunte los datos del arrendador (a-c) y del arrendatario (d-f) uno por turno como se detalla abajo, pero SIN aplicar el Ciclo de Edición Incremental completo (vista previa + confirmación + `Edit`) tras cada sub-apartado individual. Acumule en memoria los datos de cada parte a medida que los obtiene. Solo al completar el último dato de esa parte (apartado c para el arrendador, apartado f para el arrendatario), muestre una única vista previa con el nombre/razón social, documento de identidad y domicilio de esa parte juntos, pida una única confirmación conjunta ("¿Confirmamos estos datos del arrendador/arrendatario?") y, tras confirmar, aplique el `Edit` que los vuelca todos a la vez.
   a. Nombre completo del arrendador si V3 = persona física, o razón social si V3 = persona jurídica (use el valor ya resuelto en el Punto 1: nunca ofrezca ambas opciones a la vez si la naturaleza ya se conoce). **Validación de coherencia:** si el nombre aportado no encaja con V3 (p. ej. suena a razón social de empresa —"S.L.", "S.A.", "Sociedad", nombre comercial— habiéndose pedido nombre de persona física, o al revés), no lo dé por bueno: señale la posible incoherencia y pida confirmación antes de continuar con el documento de identidad.
   b. Documento de identidad del arrendador: DNI o NIE si V3 = persona física (DNI para españoles, NIE para extranjeros residentes — formato 1 letra X/Y/Z + 7 dígitos + 1 letra), NIF/CIF si V3 = persona jurídica (use el valor ya resuelto en el Punto 1, no vuelva a preguntar por la naturaleza). Si el cliente indica que la parte es extranjera, pida NIE sin insistir en el formato de DNI. **Validación de formato:** si la respuesta no tiene forma de ningún documento de identidad válido (DNI, NIE, NIF/CIF según corresponda) — p. ej. es claramente un nombre de persona, o una cadena de caracteres sin ninguna estructura reconocible — no la acepte como documento: trátelo como una corrección del dato del apartado (a) o pida aclaración, y repita la pregunta del documento de identidad.
   c. Domicilio a efectos de notificaciones del arrendador. Al completar este dato, ejecute la confirmación agrupada del bloque arrendador (a-c) descrita arriba antes de pasar al arrendatario. **En habitación**, incluya en este bloque el título de disponibilidad del arrendador sobre la vivienda (propietario, o arrendatario con facultad de subarrendar).
   d. Nombre completo del arrendatario si V4 = persona física, o razón social si V4 = persona jurídica. Aplique la misma validación de coherencia con V4. En habitación, el arrendatario es siempre persona física.
   e. Documento de identidad del arrendatario: mismo criterio del apartado (b) (DNI/NIE si V4 = persona física, NIF/CIF si V4 = persona jurídica), incluida la misma validación de formato.
   f. Domicilio actual del arrendatario (**en temporada**: su domicilio habitual y permanente, que debe ser distinto de la vivienda arrendada — si el cliente indica que no tiene otra residencia, active el Guardrail 8). Al completar este dato, ejecute la confirmación agrupada del bloque arrendatario (d-f) descrita arriba.
3. **Objeto [dato objetivo; en temporada incluye una decisión de negociación]:** Dirección completa, referencia catastral, m2, anexos (garaje, trastero). La referencia catastral se pide siempre directamente al cliente, sin intentar buscarla usted mismo: la Sede Electrónica del Catastro es un buscador interactivo, no una URL consultable con `web_search`/`WebFetch`. Si el cliente no la tiene a mano, queda como `{{DATO_FALTANTE}}` (Guardrail 11): no la invente ni la intente localizar. **En temporada** pregunte además la causa concreta de la temporada (trabajo temporal, estudios, verano, obras en la vivienda habitual...) **[negociación]**: explique que la causa debe ser real y acreditable y que sin ella el contrato se recalificaría como vivienda habitual, y valídela (Guardrail 8). **En habitación** el objeto es la identificación de la habitación dentro de la vivienda (número o descripción, superficie, equipamiento) y las zonas comunes de uso compartido; no se pide referencia catastral.
4. **Duración [negociación]:** En vivienda habitual: duración en años o "mínimo legal", fecha de inicio (recuerde los mínimos de 5/7 años del Art. 9.1 LAU y la prórroga del Art. 10). Aproveche este dato para fijar también el lugar y la fecha de firma del encabezamiento del contrato (`{{municipio}}` y `{{fecha_contrato}}`): salvo que el cliente indique otra cosa, coinciden con el municipio del inmueble y con la fecha en que se cierra esta sección. En local: duración pactada y, en su caso, prórroga expresa (sin denuncia el contrato se extingue al vencimiento). En temporada: fechas de inicio y fin ligadas a la causa, sin prórroga legal. En habitación: fechas de inicio y fin y, en su caso, preaviso de terminación anticipada.
5. **Renta [negociación]:** Importe mensual en euros (en temporada: importe y periodicidad — mensual o por la temporada completa), forma de pago, IBAN. En vivienda habitual en zona tensionada, aplique los límites de los Arts. 17.6 y 17.7 LAU (Guardrail 5) y explíquelos antes de fijar el importe.
6. **Actualización [negociación]:** Solo vivienda habitual y local (en temporada y habitación, únicamente si la duración supera el año y las partes lo desean). En vivienda habitual: índice pactado o "según ley" — explique que en contratos celebrados desde el 26/05/2023 el incremento anual no puede superar el IRAV publicado por el INE (Guardrail 6). En local: índice de libre pacto (IPC, IGC u otro).
7. **Fianza y Garantías [negociación]:** Meses de fianza (verifique el mínimo legal de su ruta: 1 mensualidad vivienda habitual, 2 local y temporada, libre pacto en habitación), garantías adicionales — en vivienda de hasta 5/7 años, con el límite de 2 mensualidades del Art. 36.5 LAU, que debe explicar antes de pactar.
8. **Gastos y Suministros [negociación]:** Quién paga IBI, comunidad (por defecto arrendador; suministros a cargo del inquilino; en habitación: si los suministros van incluidos en la renta, a tanto fijo o por reparto). Recuerde el Art. 20.1 LAU (gastos de gestión y formalización siempre del arrendador) en vivienda habitual.
9. **Pactos Opcionales [negociación]:** Renuncia a adquisición preferente (vivienda y local), correos electrónicos para notificaciones, mediación, cláusulas extra. En habitación: normas de uso y convivencia y normas adicionales de la vivienda.

### 5.B — Comunicaciones (actualización de renta, no renovación, devolución de fianza)

Anuncios fijos:
- Al abrir la sección 1 (tras la confirmación de comenzar, Punto 4.4): "Procedemos a identificar el contrato de arrendamiento sobre el que versa la comunicación."
- Al pasar a la sección 2: "Identificado el contrato, pasamos a los datos de remitente y destinatario de la comunicación."
- Al pasar a la sección 3: en actualización de renta, "Corresponde ahora determinar la actualización de renta a comunicar."; en no renovación, "Corresponde ahora fijar el vencimiento del contrato y verificar el plazo de preaviso."; en devolución de fianza, "Corresponde ahora concretar la fianza reclamada y los plazos aplicables."
- Al pasar a la sección 4: "Por último, procede fijar el lugar y la fecha de emisión y las indicaciones de envío."

1. **Contrato de referencia [dato objetivo]:** fecha de celebración del contrato, tipo (vivienda o uso distinto) e inmueble (dirección y municipio). Un dato por turno.
2. **Remitente y destinatario (confirmación agrupada por parte, igual que la sección 2 de 5.A):** del remitente: nombre o razón social, NIF/CIF y domicilio (a-c, con las mismas validaciones de coherencia y formato de 5.A.2); del destinatario: nombre y domicilio de notificaciones fijado en el contrato (d-e). La condición de cada uno (arrendador/arrendatario) ya está resuelta (V8): no la vuelva a preguntar.
3. **Contenido específico [negociación — explique el régimen legal antes de fijar cada valor]:**
   - *Actualización de renta:* cláusula del contrato que pacta la actualización (sin pacto expreso no procede la comunicación: adviértalo y detenga la redacción si no existe), renta vigente, índice aplicable y porcentaje. Verifique usted mismo con `web_search` el valor del IRAV vigente publicado por el INE en la fecha de la actualización e infórmelo; si el porcentaje que pretende el cliente supera el IRAV (contratos de vivienda desde el 26/05/2023), explique el límite del Guardrail 6 y no lo redacte por encima. Calcule y muestre la renta resultante y el mes de efectos (el siguiente a la notificación, Art. 18.2 LAU).
   - *No renovación:* fecha de vencimiento del plazo o de la prórroga en curso. **Validación de plazos obligatoria:** compruebe que entre la fecha de envío prevista y el vencimiento median al menos 4 meses (remitente arrendador) o 2 meses (remitente arrendatario), Art. 10.1 LAU; si no llegan, advierta de que la comunicación sería extemporánea y de que el contrato se prorrogaría (Guardrail 9). Si el remitente es el arrendador y V6 = Sí, mantenga el bloque de advertencia de la prórroga extraordinaria del Art. 10.3 LAU; si V6 = No lo sé, verifíquelo con `web_search` como en 5.A.1.
   - *Devolución de fianza:* fecha de extinción del contrato, fecha de entrega de llaves, importe de la fianza, IBAN de devolución y plazo de atención del requerimiento. **Validación de plazos obligatoria:** compruebe que ha transcurrido más de 1 mes desde la entrega de llaves (Art. 36.4 LAU); si no, adviértalo y no redacte el requerimiento sin dejar constancia de la advertencia (Guardrail 10).
4. **Emisión y envío [dato objetivo]:** lugar y fecha de emisión. En la vista previa final, recuerde la recomendación de envío por burofax con certificación de texto y acuse de recibo al domicilio de notificaciones del contrato.

(Los límites legales de cada sección — duración, gastos, zonas tensionadas, IRAV, fianza, preavisos — están fijados en la sección Guardrails al inicio de este documento; no se redacta por fuera de esos límites.)

---

## BUCLE DE REALIMENTACIÓN FINAL

Tras completar el Punto 5, muestra el siguiente menú y espera instrucciones (aplicando `Edit` según corresponda):
1. Ajustar una cláusula o apartado existente.
2. Añadir contenido adicional.
3. Eliminar contenido opcional.
4. Corregir un dato.
5. Cerrar y dar el documento por bueno.

Al cerrar, añade al final estas advertencias (las que apliquen a la ruta):

1. Este documento es un DRAFT generado automáticamente. Debe ser revisado por un abogado colegiado antes de su firma o envío.
2. Versión de la normativa verificada: fecha extraída en el Punto 2.
3. Contratos con fianza legal (vivienda habitual, local, temporada): la fianza debe depositarse en el organismo autonómico correspondiente (Art. 36.3 LAU) según la comunidad autónoma del inmueble.
4. Contratos: se recomienda la inscripción en el Registro de la Propiedad para su oponibilidad frente a terceros.
5. Comunicaciones: se recomienda el envío por burofax con certificación de texto y acuse de recibo, y conservar el justificante.

## Como NO se usa esta skill

- No usar para arrendamientos de finca rústica (excluidos de la LAU, Art. 5.a).
- No usar para viviendas turísticas (excluidas de la LAU, Art. 5.e, sujetas a normativa autonómica).
- No usar para viviendas militares, de porteros o guardas, ni las demás excluidas por el Art. 5 LAU.
- No usar el contrato de temporada para encubrir una residencia habitual (Guardrail 8): en ese caso, contrato de vivienda.
- No usar para redactar la resolución del contrato por incumplimiento ni el desahucio: para eso, derivar a la skill `derecho-civil-desahucio`. La comunicación de no renovación (Art. 10.1 LAU) es solo para el vencimiento del plazo o de sus prórrogas.
- No usar para reclamar judicialmente rentas o la fianza no devuelta: derivar a la skill `derecho-civil-monitorio` (el requerimiento de devolución de fianza de esta skill es el paso extrajudicial previo).
- No usar si el usuario pide opinión jurídica sobre un litigio ya existente entre las partes: derivar a `escalate_to_attorney`.

## Escalación

| Situación | Acción |
|---|---|
| Litigio o conflicto ya existente entre arrendador y arrendatario | Escalar vía `escalate_to_attorney` |
| Inmueble en zona de mercado residencial tensionado, con dudas sobre los límites de renta aplicables | Verificar con `web_search` la declaración autonómica vigente y advertir |
| El cliente pretende un contrato de temporada sin causa real de temporalidad | Rechazar, explicar la recalificación como vivienda (Titulo II LAU) y ofrecer el contrato de vivienda |
| Comunicación de no renovación con preaviso ya incumplible (extemporánea) | Advertir de la prórroga del Art. 10.1 LAU y de sus consecuencias antes de redactar |
| El arrendador quiere contestar a un requerimiento de fianza recibido | Escalar vía `escalate_to_attorney` |
| Arrendatario o arrendador menor de edad o con discapacidad sin representación clara | Advertir de la necesidad de representación legal y escalar |
| Duda sobre normativa autonómica o foral que module la LAU | Usar `web_search` para verificar; si persiste la duda, advertir y escalar |
