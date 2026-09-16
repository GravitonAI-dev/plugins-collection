---
name: derecho-civil-capitulaciones-matrimoniales
description: >
  Redacta la minuta de capitulaciones matrimoniales conforme al **Codigo Civil**, que permite a los
  conyuges estipular, modificar o sustituir el regimen economico de su matrimonio y exige para ello
  escritura publica (Arts. 1315 a 1335), y a la **Ley 1/2000 de Enjuiciamiento Civil** en lo relativo
  al inventario y la liquidacion del regimen que se sustituye.


  Genera dos documentos: la minuta de capitulaciones para el notario, con la eleccion del regimen de
  separacion de bienes o de participacion y los pactos que la acompanan, y el inventario y propuesta
  de liquidacion del regimen anterior cuando se sustituye una sociedad de gananciales ya existente.


  Trata la eleccion entre separacion de bienes, participacion y gananciales con sus consecuencias
  practicas, los pactos sobre atribucion de la vivienda y sobre cargas del matrimonio, la validez y
  los limites de los pactos en prevision de una futura ruptura, la publicidad frente a terceros
  mediante la inscripcion en el Registro Civil y, cuando proceda, en el Registro de la Propiedad y en
  el Registro Mercantil, y la proteccion de los acreedores anteriores.


  NO usar para el convenio regulador de un divorcio o separacion, que corresponde a la skill de
  divorcio, ni para liquidar de forma contenciosa la sociedad de gananciales, que corresponde a la
  skill de liquidacion de gananciales, ni para pactos sucesorios propios de los derechos civiles
  forales.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Codigo Civil](https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763) y
  [Ley 1/2000 de Enjuiciamiento Civil](https://www.boe.es/buscar/act.php?id=BOE-A-2000-323).
when_to_use: |
  - Una pareja va a casarse y quiere pactar separacion de bienes antes de la boda.
  - Un matrimonio en gananciales quiere cambiar a separacion de bienes.
  - Uno de los conyuges va a iniciar una actividad empresarial y quiere proteger el patrimonio familiar.
  - El usuario pregunta las diferencias practicas entre gananciales, separacion de bienes y participacion.
  - El usuario quiere pactar de antemano que ocurrira con la vivienda o con las cargas si la relacion termina.
  - El usuario pregunta desde cuando afecta a terceros el cambio de regimen economico.
inputs:
  - documento: minuta de capitulaciones / inventario y liquidacion del regimen anterior (V1)
  - momento: antes del matrimonio / durante el matrimonio (V2)
  - regimen_elegido: separacion de bienes / participacion / gananciales con pactos (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_conyuges: nombre, NIF/NIE, domicilio, estado civil, nacionalidad y vecindad civil de cada uno
  - datos_matrimonio: fecha y lugar del matrimonio, y datos de su inscripcion en el Registro Civil
  - regimen_vigente: regimen economico actual y titulo del que resulta
  - inventario_bienes: bienes y derechos de cada conyuge y comunes, con su titulo y valor
  - deudas: deudas de cada conyuge y comunes, con acreedor e importe pendiente
  - vivienda_familiar: identificacion de la vivienda, titularidad y pacto que se desea sobre ella
  - pactos_cargas: forma de contribuir a las cargas del matrimonio y a los gastos comunes
  - pactos_prevision_ruptura: pactos que se desean para el caso de futura ruptura
  - hijos: existencia de hijos comunes o de relaciones anteriores y su situacion
outputs:
  - minuta_capitulaciones: minuta de escritura de capitulaciones matrimoniales para el notario, DRAFT
  - inventario_liquidacion_regimen: inventario y propuesta de liquidacion del regimen que se sustituye, DRAFT
  - checklist_inscripciones: inscripciones y comunicaciones necesarias para la eficacia frente a terceros
references:
  - references/cc-regimenes-economicos-y-capitulaciones.md
  - references/pactos-en-prevision-de-ruptura-y-publicidad.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-minuta-capitulaciones-matrimoniales.md
  - assets/template-inventario-liquidacion-regimen.md
---

# Capitulaciones Matrimoniales (Elección y Cambio de Régimen Económico)

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar unas capitulaciones matrimoniales.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `minuta_capitulaciones` | `inventario_liquidacion` | `convenio_divorcio`.
- **V2 (Momento):** `antes_del_matrimonio` | `durante_el_matrimonio`.
- **V3 (Régimen Elegido):** `separacion_de_bienes` | `participacion` | `gananciales_con_pactos`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar el documento, el momento y el régimen que se quiere pactar.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un abogado de despacho (de usted), confirmando que vais a preparar las capitulaciones matrimoniales.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca si están ya casados y qué régimen quieren pactar, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), el momento (`V2`) o el régimen elegido (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar si se prepara la minuta de capitulaciones o el inventario del regimen que se sustituye.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "minuta_capitulaciones", "label": "Minuta de capitulaciones matrimoniales para el notario"},
        {"id": "inventario_liquidacion", "label": "Inventario y liquidación del régimen de gananciales que se sustituye"},
        {"id": "convenio_divorcio", "label": "Nos vamos a separar o divorciar y necesitamos el convenio regulador"}
      ]
    },
    {
      "id": "momento",
      "rationale": "Resolver V2: las capitulaciones anteriores al matrimonio caducan si este no se celebra en el plazo legal, y las posteriores exigen liquidar el regimen anterior.",
      "question": "¿Están ya casados o van a casarse?",
      "options": [
        {"id": "antes_del_matrimonio", "label": "Vamos a casarnos (capitulaciones prenupciales)"},
        {"id": "durante_el_matrimonio", "label": "Ya estamos casados y queremos cambiar de régimen"}
      ]
    },
    {
      "id": "regimen_elegido",
      "rationale": "Resolver V3 para redactar el articulado del regimen que se pacta.",
      "question": "¿Qué régimen económico desean pactar?",
      "options": [
        {"id": "separacion_de_bienes", "label": "Separación de bienes: cada uno conserva y administra lo suyo"},
        {"id": "participacion", "label": "Participación: separación durante el matrimonio y reparto de las ganancias al final"},
        {"id": "gananciales_con_pactos", "label": "Gananciales, pero con pactos concretos que lo modulen"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `momento`
- `V3` — `regimen_elegido`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = convenio_divorcio`:**
  - **DETENER.** Informar de que el convenio regulador de la separación o el divorcio tiene un contenido propio y necesario (medidas sobre los hijos, uso de la vivienda familiar, cargas, pensiones y liquidación del régimen) y una tramitación específica con intervención judicial o notarial y, cuando hay hijos menores, informe del Ministerio Fiscal. Derivar a la skill de divorcio del plugin de derecho civil. No crear documento.
- **Si `V1 = minuta_capitulaciones`:**
  - Plantilla del sistema: `assets/template-minuta-capitulaciones-matrimoniales.md`. Proceder a la **Fase 2**.
- **Si `V1 = inventario_liquidacion`:**
  - Plantilla del sistema: `assets/template-inventario-liquidacion-regimen.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina si se incorpora la advertencia de caducidad de las capitulaciones prenupciales por no celebrarse el matrimonio en el plazo legal, o si es necesaria la liquidación del régimen anterior.
- `V3` no elige plantilla: determina el articulado del régimen que se pacta y las advertencias propias de cada uno.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `cc-regimenes-economicos-y-capitulaciones.md`, `pactos-en-prevision-de-ruptura-y-publicidad.md` y `estilo-redaccion-escritos.md`.
2. Comprueba la **vecindad civil** de cada cónyuge: si alguno tiene vecindad civil foral, el régimen económico legal supletorio y el propio régimen de las capitulaciones pueden ser distintos del común, y procede advertirlo y derivar.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Consecuencias Prácticas:**
   - Explicar que las capitulaciones exigen **escritura pública** y que, para ser eficaces frente a terceros, deben hacerse constar en la **inscripción del matrimonio en el Registro Civil**.
   - Explicar en términos prácticos la diferencia entre los regímenes: en **gananciales**, lo ganado durante el matrimonio es común y responde de las deudas contraídas en el ejercicio de la potestad doméstica; en **separación de bienes**, cada cónyuge conserva la titularidad, administración y disposición de sus bienes, y responde de sus propias deudas, subsistiendo el deber de contribuir a las cargas del matrimonio; en **participación**, funciona como separación durante el matrimonio y al final cada cónyuge participa en las ganancias del otro.
   - *Condicional `V2 = durante_el_matrimonio`:* advertir de que el cambio de régimen **no perjudica los derechos ya adquiridos por terceros**, y que exige **liquidar** el régimen anterior mediante inventario y adjudicaciones.
   - Advertir de que los pactos en previsión de una futura ruptura son admisibles, pero tienen límites: no pueden ser contrarios a la ley, a la igualdad de los cónyuges ni al interés de los hijos, y son revisables si resultan gravemente perjudiciales para uno de ellos.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta la plantilla **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
Aplica el protocolo determinista de `REG-AST-01` (`CLAUDE.md`): si el usuario acepta la plantilla predeterminada propuesta (`plantilla_sistema`), carga el asset enrutado y avanza a la **Fase 3**; si aporta su propia minuta (`plantilla_usuario`), realiza el control de legalidad advirtiendo de cláusulas nulas o contrarias a normas imperativas, adopta la minuta revisada como base y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` y la sección 6.1 de `CLAUDE.md`:
1. **Escritura del Documento (`create_file`):** Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`, aplicando el principio Zero-Omission y el volcado inmediato total de partes (`REG-CLI-04`) en título H1, comparecencia y firmas.
2. **Validación de Integridad:** Comprobación prioritaria mediante `# WORKSPACE ACTIVE DOCUMENTS`.
3. **Confirmación en Chat y Encadenamiento Inmediato:** Informa en el chat de la ruta absoluta del documento creado y los datos de partes incorporados, e introduce en esa misma respuesta la primera sección de la Fase 4 sin detener el flujo.
---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial las secciones del documento respetando rigurosamente las directivas operativas globales de `CLAUDE.md`:
- **Partes e Intervinientes (REG-CLI-01 a 04):** Búsqueda prioritaria con `search_clients`, desambiguación con opción obligatoria `ninguna`, consentimiento de guardado con `save_client` (REG-CLI-03) y volcado directo e inmediato al editor (`edit_file` / `create_file`) sin confirmación en chat (REG-CLI-04).
- **Datos Estructurados Objetivos:** Solicitud en bloque mediante `slot_filling_request`.
- **Equivalencia Chat / Formulario (REG-DAT-01):** Ingestión directa de información aportada por chat sin re-emitir formularios innecesarios; reenvío oportuno si el usuario canceló sin responder.
- **Cláusulas Sustantivas / Negociables:** Negociación en chat -> Vista previa en texto plano -> Pregunta literal de confirmación (`¿Confirmamos esta cláusula?` / `¿Confirmamos esta sección?`) -> Persistencia con `edit_file`.

### Hoja de Ruta de Secciones — RAMA MINUTA DE CAPITULACIONES:

1. **Comparecencia y datos personales** *(confirmación agrupada)*: identidad completa de ambos cónyuges o futuros cónyuges, NIF/NIE, domicilio, nacionalidad, **vecindad civil** y estado civil.
2. **Situación matrimonial y régimen vigente**: *Condicional `V2 = antes_del_matrimonio`:* manifestación del proyecto de contraer matrimonio. *Condicional `V2 = durante_el_matrimonio`:* fecha y lugar del matrimonio, datos de su inscripción en el Registro Civil, régimen vigente y título del que resulta.
3. **Estipulación del régimen elegido**: articulado del régimen conforme a `V3`, con la determinación expresa de la fecha de efectos entre los cónyuges.
4. **Liquidación del régimen anterior**: *Condicional `V2 = durante_el_matrimonio`:* remisión al inventario y a las adjudicaciones, con la constancia de que el patrimonio común queda liquidado y de que cada cónyuge recibe lo que le corresponde.
5. **Contribución a las cargas del matrimonio**: forma y proporción en que cada cónyuge contribuirá al levantamiento de las cargas, y tratamiento del trabajo doméstico como contribución.
6. **Vivienda familiar**: identificación, titularidad, régimen de uso y pacto que se establece, con la advertencia de que la disposición de la vivienda habitual requiere el consentimiento de ambos.
7. **Pactos en previsión de una futura ruptura**: *Condicional pacto expreso:* previsiones sobre la vivienda, sobre compensaciones y sobre gastos, con las advertencias de límites y revisabilidad.
8. **Publicidad, inscripciones y cláusulas finales**: constancia en la inscripción del matrimonio en el Registro Civil, inscripción en el Registro de la Propiedad respecto de los inmuebles y en el Registro Mercantil si alguno es empresario, salvaguarda de los derechos de terceros, y apoderamientos para la tramitación.

### Hoja de Ruta de Secciones — RAMA INVENTARIO Y LIQUIDACIÓN:

1. **Cónyuges, matrimonio y régimen que se liquida** *(confirmación agrupada)*: identidades, datos del matrimonio y régimen vigente con su título.
2. **Activo del patrimonio común**: relación de bienes y derechos comunes con su descripción, título de adquisición, datos registrales y valor atribuido.
3. **Pasivo del patrimonio común**: deudas comunes con acreedor, concepto, importe pendiente y garantía.
4. **Créditos y reintegros entre cónyuges y con el patrimonio común**: cantidades que cada cónyuge deba reintegrar o percibir por bienes privativos invertidos en el común o al contrario.
5. **Determinación del haber y adjudicaciones**: cálculo del remanente, formación de los lotes y adjudicación a cada cónyuge, con el tratamiento de los excesos de adjudicación y su compensación.
6. **Deudas, cargas y advertencias finales**: asunción de deudas por cada cónyuge, advertencia de que el pacto interno no es oponible a los acreedores sin su consentimiento, y solicitud de las inscripciones registrales que procedan.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias y la vecindad civil antes de citar preceptos o afirmar el régimen legal supletorio aplicable.
2. **Cero Invención de Datos:** prohibido inventar datos de inscripción del matrimonio, datos registrales de bienes, valores o importes de deudas. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Neutralidad entre cónyuges:** al explicar las alternativas, exponer con neutralidad la consecuencia para cada uno. Si la skill asiste a uno solo de ellos, advertir de la conveniencia de asesoramiento independiente para el otro y del riesgo de conflicto de interés.
4. **Prohibido pactar sobre hijos futuros:** no redactar cláusulas que predeterminen la guarda, la custodia o el régimen de visitas de hijos, materia indisponible sujeta al interés del menor.
5. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
6. **Límites de Alcance:** no redactar convenios reguladores de divorcio, no liquidar gananciales de forma contenciosa, ni preparar pactos sucesorios forales, que corresponden a otras skills o a profesional competente.
