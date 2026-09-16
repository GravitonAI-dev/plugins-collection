---
name: derecho-civil-sucesion-abintestato-y-voluntades
description: >
  Prepara los dos documentos que el catalogo de sucesiones no cubria conforme al **Codigo Civil**, que
  fija el orden de suceder cuando no hay testamento (Arts. 912 a 958) y los derechos del conyuge
  viudo, y a la **Ley 41/2002** basica reguladora de la autonomia del paciente, que reconoce el
  derecho a dejar instrucciones previas sobre los cuidados y el tratamiento medico.


  Genera dos documentos: el requerimiento al notario para el acta de notoriedad de declaracion de
  herederos abintestato, con la acreditacion del parentesco y de la inexistencia de testamento, y el
  documento de voluntades anticipadas o instrucciones previas, con la designacion de representante y
  su inscripcion registral.


  Determina el orden sucesorio aplicable y quien excluye a quien, calcula la cuota que corresponde a
  cada llamado y el usufructo del conyuge viudo, identifica el notario territorialmente competente y
  la documentacion imprescindible, computa el plazo de veinte dias habiles de tramitacion del acta, y
  advierte de los limites de las voluntades anticipadas y de su prevalencia sobre la decision de los
  familiares.


  NO usar para redactar testamentos ni para la planificacion sucesoria, que corresponde a la skill de
  testamento y planificacion, ni para aceptar o partir la herencia, que corresponde a la skill de
  herencia, ni para sucesiones regidas por derechos civiles forales o con elemento internacional.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Codigo Civil](https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763) y
  [Ley 41/2002 de autonomia del paciente](https://www.boe.es/buscar/act.php?id=BOE-A-2002-22188).
when_to_use: |
  - Ha fallecido un familiar sin testamento y hay que acreditar quienes son los herederos.
  - El usuario pregunta quien hereda si no hay testamento y en que proporcion.
  - El usuario pregunta que le corresponde al conyuge viudo cuando no hay testamento.
  - El usuario quiere dejar instrucciones sobre los tratamientos medicos que acepta o rechaza.
  - El usuario quiere designar a alguien que decida por el si no puede expresarse.
  - El usuario pregunta donde se inscriben las voluntades anticipadas para que los medicos las vean.
inputs:
  - documento: acta de declaracion de herederos / voluntades anticipadas (V1)
  - orden_sucesorio: descendientes / ascendientes o colaterales / conyuge o pareja (V2)
  - testamento: acreditada la inexistencia de testamento / pendiente de comprobar (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_causante: nombre, NIF, ultimo domicilio, fecha y lugar de fallecimiento, estado civil
  - datos_requirente: nombre, NIF, domicilio, telefono y correo, y parentesco con el causante
  - parentesco_llamados: identidad, NIF, domicilio y parentesco de todos los posibles herederos
  - documentacion_estado_civil: certificados de defuncion, nacimiento, matrimonio y libro de familia
  - certificado_ultimas_voluntades: resultado del certificado del Registro de Actos de Ultima Voluntad
  - testigos: identidad y NIF de los testigos que conocen a la familia del causante
  - patrimonio_relevante: bienes principales y su ubicacion, a efectos de competencia notarial
  - datos_otorgante_voluntades: nombre, NIF, domicilio y capacidad del otorgante
  - instrucciones_medicas: tratamientos que acepta y que rechaza, y situaciones previstas
  - representante_designado: identidad, NIF y contacto del representante y de su sustituto
outputs:
  - requerimiento_acta_declaracion_herederos: requerimiento al notario para el acta de notoriedad, DRAFT
  - documento_voluntades_anticipadas: documento de instrucciones previas con representante, DRAFT
  - checklist_documentacion: documentacion, notario competente, plazos e inscripciones registrales
references:
  - references/cc-orden-sucesorio-abintestato.md
  - references/acta-notarial-y-voluntades-anticipadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-requerimiento-acta-declaracion-herederos.md
  - assets/template-documento-voluntades-anticipadas.md
---

# Sucesión sin Testamento y Voluntades Anticipadas

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `acta_declaracion_herederos` | `voluntades_anticipadas` | `testamento`.
- **V2 (Orden Sucesorio):** `descendientes` | `ascendientes_o_colaterales` | `conyuge_o_pareja`.
- **V3 (Testamento):** `inexistencia_acreditada` | `pendiente_comprobar`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar el documento y, en la sucesión sin testamento, quiénes son los llamados.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un abogado de despacho (de usted), confirmando qué documento vais a preparar. Cuando se trate de un fallecimiento reciente, incorpora una fórmula sobria de condolencia, sin extenderte.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca el documento, el parentesco de los llamados y si consta la inexistencia de testamento, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), el orden sucesorio (`V2`) o la situación del testamento (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar cual de los dos documentos se prepara.",
      "question": "¿Qué necesita preparar?",
      "options": [
        {"id": "acta_declaracion_herederos", "label": "Acreditar quiénes son los herederos de un fallecido sin testamento"},
        {"id": "voluntades_anticipadas", "label": "Dejar por escrito mis instrucciones médicas para el futuro"},
        {"id": "testamento", "label": "Hacer testamento o planificar mi sucesión"}
      ]
    },
    {
      "id": "orden_sucesorio",
      "rationale": "Resolver V2 para determinar el orden de suceder y las cuotas que corresponden.",
      "question": "Si es declaración de herederos abintestato, ¿qué familiares sobreviven al fallecido?",
      "options": [
        {"id": "descendientes", "label": "Hijos o nietos"},
        {"id": "ascendientes_o_colaterales", "label": "No hay hijos: padres, hermanos, sobrinos, tíos o primos"},
        {"id": "conyuge_o_pareja", "label": "Solo cónyuge o pareja, sin hijos ni padres"},
        {"id": "no_procede", "label": "No procede: la persona está viva (se solicitan voluntades anticipadas)"}
      ]
    },
    {
      "id": "testamento",
      "rationale": "Resolver V3: sin el certificado del Registro de Actos de Ultima Voluntad el notario no puede autorizar el acta.",
      "question": "Si es declaración de herederos, ¿han obtenido ya el certificado del Registro de Actos de Última Voluntad que acredita que no hay testamento?",
      "options": [
        {"id": "inexistencia_acreditada", "label": "Sí, ya lo tenemos y no hay testamento"},
        {"id": "pendiente_comprobar", "label": "No, todavía no lo hemos solicitado"},
        {"id": "no_procede", "label": "No procede: son voluntades anticipadas (no hay causante fallecido)"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `orden_sucesorio`
- `V3` — `testamento`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = testamento`:**
  - **DETENER.** Informar de que la redacción del testamento y la planificación sucesoria tienen su propio cauce, con el análisis de la legítima, las mejoras, los legados y la fiscalidad de la sucesión. Derivar a la skill de testamento y planificación del plugin de derecho civil. No crear documento.
- **Si `V1 = acta_declaracion_herederos`:**
  - Plantilla del sistema: `assets/template-requerimiento-acta-declaracion-herederos.md`. Proceder a la **Fase 2**.
- **Si `V1 = voluntades_anticipadas`:**
  - Plantilla del sistema: `assets/template-documento-voluntades-anticipadas.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina el orden de suceder que se invoca, quiénes deben ser citados y las cuotas que se consignan.
- `V3` no elige plantilla: determina si el documento incorpora el bloque de gestiones previas pendientes y la advertencia de que el acta no puede autorizarse sin el certificado de últimas voluntades.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `cc-orden-sucesorio-abintestato.md`, `acta-notarial-y-voluntades-anticipadas.md` y `estilo-redaccion-escritos.md`.
2. Comprueba la **vecindad civil** del causante o del otorgante: si es foral, el orden sucesorio y los derechos del cónyuge pueden ser distintos. En voluntades anticipadas, verifica mediante `web_search` la normativa autonómica aplicable, que determina la forma de otorgamiento y el registro competente.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Plazos Aplicables:**
   - Para la declaración de herederos: explicar que, sin testamento, la ley designa a los herederos por un **orden de llamamientos** en el que cada grupo excluye al siguiente, y que ese hecho se acredita mediante **acta de notoriedad** autorizada por notario, no mediante resolución judicial. Explicar el notario territorialmente competente y que el acta requiere **dos testigos** que conozcan a la familia y un plazo de **veinte días hábiles** desde el requerimiento inicial hasta su conclusión.
   - Recordar los plazos fiscales que corren desde el fallecimiento: **seis meses** para el impuesto de sucesiones, prorrogables, y para la plusvalía municipal cuando haya inmuebles.
   - Para voluntades anticipadas: explicar que el documento permite dejar instrucciones sobre los tratamientos que se aceptan o rechazan y designar un representante que decida por el otorgante, que **prevalece sobre la opinión de los familiares**, y que solo es plenamente eficaz si se **inscribe** en el registro autonómico y, a través de él, en el registro nacional que consultan los profesionales sanitarios.
   - Advertir de los límites: no pueden solicitarse actuaciones contrarias al ordenamiento jurídico ni a la buena práctica clínica, ni intervenciones que no se correspondan con el supuesto de hecho previsto.
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

### Hoja de Ruta de Secciones — RAMA ACTA DE DECLARACIÓN DE HEREDEROS:

1. **Requirente y su interés** *(confirmación agrupada)*: identidad, NIF, domicilio y contacto del requirente, y parentesco o interés legítimo que le habilita para promover el acta.
2. **Causante y su fallecimiento**: identidad completa, NIF, último domicilio y residencia habitual, fecha y lugar del fallecimiento, y estado civil al tiempo del fallecimiento con identificación del cónyuge si lo hubiera.
3. **Notario competente**: determinación del notario territorialmente competente por el último domicilio o residencia habitual del causante, por el lugar del fallecimiento o por el lugar donde radique la mayor parte de su patrimonio, con la alternativa de distrito colindante.
4. **Inexistencia de testamento**: resultado del certificado del Registro General de Actos de Última Voluntad y del certificado de contratos de seguros de cobertura de fallecimiento. *Condicional `V3 = pendiente_comprobar`:* relación de gestiones previas pendientes con su forma de obtención y advertencia de que el acta no puede autorizarse sin ellas.
5. **Llamados y acreditación del parentesco** *(confirmación agrupada)*: relación de todos los posibles herederos con su identidad, NIF, domicilio y parentesco, y documentación que acredita cada vínculo (certificados de nacimiento, de matrimonio y libro de familia).
6. **Orden sucesorio y cuotas**: exposición del orden de suceder aplicable conforme a `V2`, con la exclusión de los grados posteriores, la cuota que corresponde a cada llamado y, cuando concurra, el derecho del cónyuge viudo con su naturaleza y su extensión.
7. **Testigos y solicitud**: identidad de los dos testigos que conocen a la familia del causante y que no tienen interés en la sucesión, y petición formal de que se autorice el acta de notoriedad, con la advertencia del plazo de veinte días hábiles.

### Hoja de Ruta de Secciones — RAMA VOLUNTADES ANTICIPADAS:

1. **Otorgante y capacidad** *(confirmación agrupada)*: identidad completa, NIF, domicilio, contacto, y manifestación de que actúa libremente y con capacidad para decidir.
2. **Valores y criterios personales**: declaración de los valores y las prioridades que deben guiar las decisiones sanitarias cuando el otorgante no pueda expresarse, que es la parte que orienta la interpretación del resto.
3. **Situaciones previstas**: descripción de los escenarios clínicos en los que el documento debe aplicarse (enfermedad irreversible, daño cerebral severo, situación terminal, demencia avanzada), con la mayor concreción posible.
4. **Instrucciones sobre tratamientos**: tratamientos y actuaciones que se aceptan y que se rechazan, con mención expresa de las medidas de soporte vital, la nutrición e hidratación artificiales, la reanimación y los cuidados paliativos y la sedación.
5. **Designación de representante**: identidad, NIF y contacto del representante y de su sustituto, con el alcance de sus facultades y la constancia de su aceptación.
6. **Donación de órganos y destino del cuerpo**: voluntad sobre la donación de órganos y tejidos y, en su caso, sobre la donación del cuerpo a la ciencia y sobre el destino del cuerpo.
7. **Formalización, inscripción y revocación**: forma de otorgamiento elegida conforme a la normativa autonómica (ante notario, ante testigos o ante el funcionario del registro), solicitud de inscripción en el registro autonómico y su traslado al registro nacional, entrega de copia a las personas indicadas, y constancia del derecho a modificarlo o revocarlo en cualquier momento.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias, la vecindad civil y la normativa autonómica de voluntades anticipadas antes de citar preceptos, cuotas o formas de otorgamiento.
2. **Cero Invención de Datos:** prohibido inventar identidades de herederos, fechas de fallecimiento, datos de certificados o números de registro. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Prohibido omitir llamados:** está terminantemente prohibido redactar el requerimiento excluyendo a un posible heredero de grado preferente o igual del que el usuario haya dado noticia. Si el usuario pretende omitir a alguien, negarse y advertir de la nulidad y de la responsabilidad que ello comporta.
4. **Prohibido redactar instrucciones ilícitas:** no incorporar al documento de voluntades anticipadas peticiones contrarias al ordenamiento jurídico vigente ni a la buena práctica clínica.
5. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
6. **Límites de Alcance:** no redactar testamentos, no aceptar ni partir herencias, no liquidar el impuesto de sucesiones y no intervenir en sucesiones forales o internacionales, que corresponden a otras skills o a profesional competente.
