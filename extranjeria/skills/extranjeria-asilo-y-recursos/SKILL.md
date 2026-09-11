---
name: extranjeria-asilo-y-recursos
description: >
  Prepara los dos escritos de extranjeria que el catalogo no cubria conforme a la **Ley 12/2009**,
  reguladora del derecho de asilo y de la proteccion subsidiaria, que fija los requisitos de la
  proteccion internacional y las garantias del solicitante, y a la **Ley Organica 4/2000** de
  Extranjeria, que remite el regimen de impugnacion de las resoluciones a las leyes generales del
  procedimiento administrativo.


  Genera dos documentos: el escrito de alegaciones y relato de persecucion que acompana la solicitud de
  proteccion internacional, y el recurso administrativo contra la denegacion, la inadmision o el
  archivo de un expediente de extranjeria.


  Distingue el asilo de la proteccion subsidiaria y de las razones humanitarias, estructura el relato
  de persecucion en torno a los cinco motivos legales y al agente perseguidor, computa los plazos
  brevisimos del procedimiento en frontera y en centro de internamiento y los del recurso, y determina
  si contra la resolucion cabe alzada o reposicion segun lo que indique su propia notificacion.


  NO usar para el recurso contencioso-administrativo ante los tribunales, ni para solicitar el NIE o
  las autorizaciones de residencia, que corresponden a la skill de extranjeria y residencia, ni para
  la nacionalidad espanola, ni para expedientes de expulsion o devolucion, que exigen direccion
  letrada urgente.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Ley 12/2009 del derecho de asilo](https://www.boe.es/buscar/act.php?id=BOE-A-2009-17242) y
  [Ley Organica 4/2000 de Extranjeria](https://www.boe.es/buscar/act.php?id=BOE-A-2000-544).
when_to_use: |
  - El usuario ha huido de su pais y quiere solicitar asilo o proteccion internacional en Espana.
  - El usuario necesita redactar el relato de persecucion que sustenta su solicitud de asilo.
  - Al usuario le han denegado o inadmitido la solicitud de proteccion internacional.
  - Al usuario le han denegado una autorizacion de residencia y quiere recurrir en via administrativa.
  - El usuario pregunta la diferencia entre asilo, proteccion subsidiaria y razones humanitarias.
  - El usuario pregunta que plazo tiene para recurrir una resolucion de extranjeria.
inputs:
  - documento: alegaciones de proteccion internacional / recurso contra resolucion de extranjeria (V1)
  - lugar_solicitud: en territorio espanol / en frontera o en centro de internamiento (V2)
  - recurso_procedente: recurso de alzada / recurso de reposicion (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_solicitante: nombre y apellidos, nacionalidad, fecha de nacimiento, documento de identidad y domicilio
  - datos_familiares: familiares que acompanan o que permanecen en el pais de origen, con su situacion
  - datos_expediente: numero de expediente, oficina o organo, fechas de presentacion y de resolucion
  - relato_persecucion: hechos de persecucion sufridos o temidos, con fechas, lugares y autores
  - motivo_proteccion: motivo legal en que se funda (raza, religion, nacionalidad, opiniones politicas, pertenencia a grupo social, genero u orientacion sexual)
  - agente_perseguidor: identidad del agente perseguidor y su relacion con el Estado
  - proteccion_estatal: gestiones realizadas ante las autoridades del pais de origen y su resultado
  - prueba_disponible: documentos, informes de pais, certificados medicos, testigos y publicaciones
  - motivos_recurso: motivos de fondo y de forma de la impugnacion
  - situacion_actual: situacion documental, laboral y de arraigo del interesado en Espana
outputs:
  - alegaciones_proteccion_internacional: escrito de alegaciones y relato de persecucion, DRAFT
  - recurso_resolucion_extranjeria: recurso administrativo contra la resolucion desfavorable, DRAFT
  - checklist_plazos_y_garantias: plazos aplicables, garantias del solicitante y organismos de apoyo
references:
  - references/ley-12-2009-proteccion-internacional.md
  - references/recursos-en-extranjeria-y-plazos.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-alegaciones-proteccion-internacional.md
  - assets/template-recurso-resolucion-extranjeria.md
---

# Protección Internacional y Recursos en Extranjería

> DRAFT — para revisión por un abogado especialista en extranjería antes de su presentación. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `alegaciones_proteccion` | `recurso_extranjeria` | `via_contenciosa`.
- **V2 (Lugar de la Solicitud):** `en_territorio` | `en_frontera_o_cie`.
- **V3 (Recurso Procedente):** `alzada` | `reposicion`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar el escrito y, en protección internacional, dónde se formula la solicitud, porque de ello dependen plazos radicalmente distintos.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve, cordial y respetuoso, en el registro formal de un abogado de extranjería (de usted), confirmando el escrito que vais a preparar. Cuando se trate de protección internacional, hazlo con especial cuidado: la persona puede estar relatando hechos traumáticos.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué necesita, dónde se encuentra y qué resolución quiere recurrir, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), el lugar de la solicitud (`V2`) o el recurso procedente (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar si se prepara la solicitud de proteccion o el recurso contra una resolucion.",
      "question": "¿Qué necesita preparar?",
      "options": [
        {"id": "alegaciones_proteccion", "label": "Solicitud de asilo o protección internacional, con su relato"},
        {"id": "recurso_extranjeria", "label": "Recurso contra una resolución de extranjería que le han denegado"},
        {"id": "via_contenciosa", "label": "Ya agoté la vía administrativa y quiero acudir a los tribunales"}
      ]
    },
    {
      "id": "lugar_solicitud",
      "rationale": "Resolver V2: el procedimiento en frontera y en centro de internamiento tiene plazos de dias, no de meses.",
      "question": "¿Dónde se encuentra la persona que solicita protección?",
      "options": [
        {"id": "en_territorio", "label": "Ya en territorio español, con libertad de movimientos"},
        {"id": "en_frontera_o_cie", "label": "En un puesto fronterizo, en un aeropuerto o en un centro de internamiento"}
      ]
    },
    {
      "id": "recurso_procedente",
      "rationale": "Resolver V3: el recurso depende de si el acto agota o no la via administrativa, segun indique su notificacion.",
      "question": "¿Qué recurso indica la notificación de la resolución que quiere impugnar?",
      "options": [
        {"id": "alzada", "label": "Recurso de alzada ante el órgano superior"},
        {"id": "reposicion", "label": "Recurso de reposición, o dice que agota la vía administrativa"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `lugar_solicitud`
- `V3` — `recurso_procedente`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = via_contenciosa`:**
  - **DETENER.** Informar de que el recurso contencioso-administrativo en materia de extranjería exige demanda ante el juzgado competente, con plazo de dos meses desde la notificación del acto que agota la vía administrativa, con representación y defensa preceptivas, y con la posibilidad de solicitar medidas cautelares de suspensión que en esta materia resultan decisivas. Derivar a abogado especialista en extranjería. No crear documento.
- **Si `V1 = alegaciones_proteccion`:**
  - Escrito del sistema: `assets/template-alegaciones-proteccion-internacional.md`. Proceder a la **Fase 2**.
- **Si `V1 = recurso_extranjeria`:**
  - Escrito del sistema: `assets/template-recurso-resolucion-extranjeria.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina los plazos que se comunican y las garantías que se invocan, radicalmente más breves en frontera y en centro de internamiento.
- `V3` no elige plantilla: determina si el recurso se redacta como de alzada ante el órgano superior jerárquico o como de reposición ante el mismo órgano.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `ley-12-2009-proteccion-internacional.md`, `recursos-en-extranjeria-y-plazos.md` y `estilo-redaccion-escritos.md`.
2. Verifica **obligatoriamente** mediante `web_search` la información actualizada del **país de origen** cuando se prepare un relato de persecución (situación de seguridad, colectivos en riesgo, actuación de las autoridades), y las instrucciones vigentes de la Secretaría de Estado de Migraciones y de la Oficina de Asilo y Refugio. La información de país es prueba esencial y cambia con rapidez.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal, Garantías y Plazos:**
   - Explicar la diferencia entre las tres figuras: el **derecho de asilo** para quien tiene temor fundado de ser perseguido por motivos de raza, religión, nacionalidad, opiniones políticas o pertenencia a determinado grupo social, incluidos los motivos de género y orientación sexual; la **protección subsidiaria** para quien, sin reunir esos requisitos, corre riesgo real de sufrir daños graves (pena de muerte, tortura o tratos inhumanos, o amenazas graves derivadas de violencia indiscriminada en conflicto); y las **razones humanitarias** como salida residual.
   - Comunicar las **garantías del solicitante**: derecho a la asistencia jurídica gratuita y a intérprete, a que se comunique su solicitud al Alto Comisionado de las Naciones Unidas para los Refugiados, a la no devolución mientras se tramita, y a la documentación provisional que autoriza la permanencia.
   - *Condicional `V2 = en_frontera_o_cie`:* advertir con claridad de que en frontera y en centro de internamiento los plazos son de **días**, con posibilidad de reexamen también en días, y de que la intervención de abogado es **urgente e imprescindible**; ofrecer el documento como apoyo, no como sustituto.
   - Para el recurso: comunicar el plazo de **un mes** desde la notificación y advertir de que el recurso **no suspende** por sí solo la eficacia de la resolución, por lo que la suspensión debe pedirse expresamente.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta el escrito **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que el relato no contenga contradicciones internas ni afirmaciones que el interesado no haya expresado, y que el recurso identifique correctamente el acto y el órgano, advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `alegaciones_proteccion_internacional.md` o `recurso_resolucion_extranjeria.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa, incluidas la fecha del sistema y las fechas límite. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta sección?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro jurídico (por ejemplo, *"Pasamos ahora a identificar al agente perseguidor"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Trato especialmente cuidadoso en el relato:** al recabar los hechos de persecución, pregunta de forma abierta, sin sugerir respuestas, sin exigir detalles innecesarios de episodios traumáticos y sin cuestionar la credibilidad del relato. Si la persona no recuerda una fecha exacta, hazlo constar como aproximada en lugar de forzar una precisión falsa.
3. **Búsqueda prioritaria de partes e intervinientes y Regla de Cero Redundancia (`search_clients` / `get_client` — REG-CLI-01 y REG-CLI-02):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01` de `CLAUDE.md`. Si los datos de una persona ya fueron obtenidos mediante `search_clients` o `get_client`, **queda TERMINANTEMENTE PROHIBIDO volver a pedir dicha información** (nombre, DNI/NIE/CIF, domicilio, contacto, etc.), ya sea en el chat o en `slot_filling_request` (`REG-CLI-02`). Si todos los datos requeridos constan en la ficha del cliente, **NO invoques `slot_filling_request`**: redacta directamente la cláusula, muestra la vista previa en texto plano en el chat y pide confirmación. Solo si faltan campos específicos ausentes en la ficha, invocarás `slot_filling_request` exclusivamente para los datos pendientes.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
4. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
5. **Confirmación:** pregunta literalmente: `¿Confirmamos esta sección?`.
6. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
7. **Validación de sentido, no solo de formato:** comprueba que la cronología del relato es coherente, que las fechas de salida del país y de entrada en España encajan, que el motivo legal invocado se corresponde con los hechos narrados y que, en el recurso, el plazo no ha vencido. Si detectas una contradicción en el relato, **señálala en el chat con tacto y pide aclaración**: una incoherencia no resuelta es el principal motivo de denegación por falta de credibilidad.

### Hoja de Ruta de Secciones — RAMA ALEGACIONES DE PROTECCIÓN INTERNACIONAL:

1. **Identidad y datos personales** *(confirmación agrupada)*: nombre y apellidos, nacionalidad, fecha y lugar de nacimiento, documentación de que dispone, idioma y necesidad de intérprete, y domicilio o lugar en que se encuentra.
2. **Situación familiar**: familiares que acompañan al solicitante y familiares que permanecen en el país de origen, con su situación y riesgo, a efectos de extensión de la protección y de reagrupación.
3. **Itinerario y llegada a España**: fecha y forma de salida del país de origen, países de tránsito y su duración, fecha y lugar de entrada en España, y motivo por el que no solicitó protección antes, si procede.
4. **Relato de persecución**: exposición cronológica de los hechos sufridos, con fechas (aproximadas cuando no se recuerden con exactitud), lugares, personas intervinientes y consecuencias. Se recoge conversando, sin sugerir contenidos.
5. **Motivo legal de la persecución**: encuadre del relato en el motivo o motivos legales, con la explicación de por qué la persecución se dirige contra el solicitante por esa causa.
6. **Agente perseguidor y protección del Estado**: identificación del agente (autoridades del Estado, partidos, organizaciones o agentes no estatales), gestiones realizadas ante las autoridades del país de origen y su resultado, y razones por las que el Estado no puede o no quiere proporcionar protección.
7. **Temor fundado y riesgo actual**: razones por las que el temor persiste y por las que el retorno supondría un riesgo real y actual, con referencia a la situación del país verificada en la sesión.
8. **Protección subsidiaria y razones humanitarias**: *Condicional insuficiencia del encuadre en asilo:* alegación subsidiaria de riesgo de daños graves y, en su defecto, de razones humanitarias.
9. **Vulnerabilidad y necesidades especiales**: *Condicional concurrencia:* menores, personas con discapacidad, personas mayores, mujeres embarazadas, familias monoparentales con menores, víctimas de trata, de tortura o de violencia sexual o de género, con la solicitud del tratamiento diferenciado que corresponda.
10. **Prueba y solicitud**: relación de la prueba aportada (documentos personales, informes médicos y psicológicos, denuncias, publicaciones, informes de país, testigos), y petición de reconocimiento de la condición de refugiado o, subsidiariamente, de la protección subsidiaria.

### Hoja de Ruta de Secciones — RAMA RECURSO EN EXTRANJERÍA:

1. **Interesado, representación y órgano** *(confirmación agrupada)*: identidad y datos del interesado, representante y título de la representación, y órgano al que se dirige el recurso conforme a `V3`.
2. **Resolución impugnada y cómputo del plazo**: identificación del expediente y de la resolución, fecha de la resolución y de su notificación, y cómputo expreso del plazo de un mes con su fecha límite.
3. **Antecedentes del expediente**: solicitud presentada, documentación aportada, requerimientos recibidos y contestados, y contenido de la resolución con su motivación.
4. **Motivos de forma**: falta o insuficiencia de motivación, requerimiento de documentación no exigible, omisión del trámite de audiencia o de subsanación, valoración de documentación no requerida previamente, e incongruencia entre lo solicitado y lo resuelto.
5. **Motivos de fondo**: acreditación de los requisitos que la resolución considera incumplidos, aportación de la documentación que subsana el defecto apreciado, y razonamiento sobre el arraigo, los medios económicos, la vivienda o el vínculo familiar según el tipo de autorización.
6. **Circunstancias personales y proporcionalidad**: arraigo social, familiar y laboral, tiempo de residencia, situación de menores a cargo, y desproporción de la consecuencia denegatoria respecto de la finalidad de la norma.
7. **Suspensión, petición y documentos**: solicitud expresa y motivada de suspensión de la ejecución cuando proceda, pretensión concreta (concesión de la autorización, retroacción para subsanar, admisión a trámite), y relación de documentos que se acompañan.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
El escrito ha sido generado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (relato, motivo legal, prueba o motivos del recurso).
2. Añadir la alegación subsidiaria de protección subsidiaria o de razones humanitarias.
3. Añadir la solicitud de suspensión de la ejecución de la resolución.
4. Revisar la coherencia global del relato y realizar control de calidad previo a la presentación.
5. Dar el escrito por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT y necesidad de letrado:** el escrito es un borrador preparatorio. En protección internacional y en cualquier expediente con riesgo de expulsión o devolución, la intervención de abogado especialista **no es opcional**: es imprescindible, y existe derecho a asistencia jurídica gratuita.
2. **Procedimiento en frontera y en centro de internamiento:** los plazos son de **días**, con posibilidad de reexamen igualmente en días. Si la persona está en esa situación, lo prioritario es contactar de inmediato con el servicio de orientación jurídica del colegio de abogados o con las organizaciones especializadas.
3. **No devolución:** el solicitante de protección internacional no puede ser devuelto ni expulsado mientras se resuelva su solicitud, y tiene derecho a permanecer en territorio español con la documentación provisional que se le expida.
4. **Coherencia del relato:** la credibilidad es el eje de la decisión. Un relato con contradicciones internas o con datos que no encajan con la información de país se deniega. Vale más un relato breve, coherente y sostenible que uno extenso y contradictorio.
5. **Prueba de la situación del país:** los informes de organismos internacionales y de organizaciones especializadas son prueba central, y deben citarse con su fuente y su fecha. No debe inventarse ninguna referencia.
6. **Plazos del recurso:** un mes desde la notificación. La resolución es ejecutiva: el recurso no suspende su eficacia y la suspensión debe pedirse expresamente y motivarse.
7. **Apoyo institucional:** existen organizaciones especializadas y el Alto Comisionado de las Naciones Unidas para los Refugiados, que puede ser informado de la solicitud y emitir informe. Debe orientarse a la persona hacia esos recursos.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa y de País Previa:** consultar las referencias y verificar la información del país de origen en la sesión antes de redactar el relato. Está prohibido citar informes de país sin haberlos consultado.
2. **Cero Invención de Datos y de Relato:** prohibido inventar, completar o embellecer hechos de persecución, fechas, nombres o episodios que el interesado no haya expresado. El relato es de la persona, no del redactor. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}` o se consigna como aproximado.
3. **Prohibido construir un relato falso:** si el usuario solicita fabricar o adornar hechos para reforzar la solicitud, negarse y advertir de que la falsedad determina la denegación, puede acarrear consecuencias legales y arruina la credibilidad de un caso que podría ser fundado.
4. **Trato de la persona:** no cuestionar la credibilidad del relato en el chat, no exigir detalles innecesarios de hechos traumáticos y no sugerir respuestas. Señalar las contradicciones con tacto y como necesidad técnica.
5. **Urgencia y derivación:** si la persona está en frontera, en un centro de internamiento o con una orden de expulsión o devolución, priorizar la derivación urgente a letrado sobre la redacción del documento.
6. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas o instrucciones administrativas en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
7. **Límites de Alcance:** no preparar recursos contencioso-administrativos, ni solicitudes de residencia o de nacionalidad, ni la defensa en expedientes de expulsión, que corresponden a otras skills o a profesional especializado.
