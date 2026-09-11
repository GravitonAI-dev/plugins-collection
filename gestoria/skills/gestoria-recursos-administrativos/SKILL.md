---
name: gestoria-recursos-administrativos
description: >
  Prepara los escritos frente a cualquier Administracion espanola conforme a la **Ley 39/2015** del
  Procedimiento Administrativo Comun, que regula los recursos de alzada y de reposicion, el silencio
  administrativo y el computo de plazos, a la **Ley 40/2015** de Regimen Juridico del Sector Publico,
  que fija los requisitos de la responsabilidad patrimonial, y a la **Ley 19/2013** de transparencia,
  que reconoce el derecho de acceso a la informacion publica.


  Genera tres documentos: el recurso administrativo (de alzada cuando el acto no agota la via
  administrativa y de reposicion cuando si la agota), la reclamacion de responsabilidad patrimonial
  por los danos causados por el funcionamiento de los servicios publicos, y la solicitud de acceso a
  la informacion publica con su reclamacion posterior.


  Determina que recurso procede segun si el acto agota o no la via administrativa, computa los plazos
  de un mes y de tres meses y el del silencio con sus efectos, acredita los cuatro requisitos de la
  responsabilidad patrimonial y el plazo de un ano desde el dano, y advierte de la ejecutividad del
  acto y de la necesidad de pedir expresamente la suspension.


  NO usar para el recurso contencioso-administrativo ante los tribunales, ni para sanciones de trafico,
  que tienen su propia skill, ni para procedimientos tributarios, cuya via es la reclamacion
  economico-administrativa, ni para materia de extranjeria, que corresponde a su propio plugin.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Ley 39/2015 del Procedimiento Administrativo Comun](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565),
  [Ley 40/2015 de Regimen Juridico del Sector Publico](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566) y
  [Ley 19/2013 de transparencia](https://www.boe.es/buscar/act.php?id=BOE-A-2013-12887).
when_to_use: |
  - Al usuario le han denegado una licencia, una subvencion o una ayuda y quiere recurrir.
  - Al usuario le han notificado una resolucion administrativa desfavorable y no sabe que recurso cabe.
  - La Administracion no contesta y el usuario pregunta que efecto tiene el silencio.
  - El usuario ha sufrido un dano por el funcionamiento de un servicio publico y quiere ser indemnizado.
  - El usuario quiere pedir informacion o documentacion a una Administracion y no se la facilitan.
  - El usuario pregunta si tiene que pagar o cumplir mientras se resuelve su recurso.
inputs:
  - documento: recurso administrativo / responsabilidad patrimonial / acceso a la informacion (V1)
  - agota_via: el acto no agota la via administrativa / el acto agota la via administrativa (V2)
  - via_previa: primera solicitud / ya hubo resolucion o silencio (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_interesado: nombre o razon social, NIF/NIE/CIF, domicilio de notificaciones, telefono y correo
  - representante: identidad del representante y titulo de la representacion, si actua por medio de otro
  - organo_administracion: administracion, organo que dicto el acto y organo competente para resolver
  - datos_acto: identificacion del acto o resolucion, numero de expediente, fecha y fecha de notificacion
  - contenido_acto: contenido de la resolucion y motivacion que expresa
  - motivos_impugnacion: motivos de fondo y de forma en que se basa la impugnacion
  - datos_dano: descripcion del dano, fecha en que se produjo, lugar y servicio publico implicado
  - valoracion_dano: importe reclamado con su desglose y forma de calculo
  - informacion_solicitada: informacion o documentacion concreta que se solicita y formato preferido
  - prueba: documentos, fotografias, informes y testigos que se aportan
outputs:
  - recurso_administrativo: recurso de alzada o de reposicion con solicitud de suspension, DRAFT
  - reclamacion_responsabilidad_patrimonial: reclamacion de responsabilidad patrimonial con valoracion del dano, DRAFT
  - solicitud_acceso_informacion: solicitud de acceso a la informacion publica y su reclamacion, DRAFT
  - checklist_plazos: computo de plazos, efectos del silencio y via posterior que queda abierta
references:
  - references/lpacap-recursos-silencio-y-plazos.md
  - references/responsabilidad-patrimonial-y-transparencia.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-recurso-administrativo.md
  - assets/template-reclamacion-responsabilidad-patrimonial.md
  - assets/template-solicitud-acceso-informacion.md
---

# Recursos Administrativos, Responsabilidad Patrimonial y Acceso a la Información

> DRAFT — para revisión por un gestor o asesor colegiado antes de su presentación. No constituye asesoramiento profesional vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar su escrito frente a la Administración.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `recurso_administrativo` | `responsabilidad_patrimonial` | `acceso_informacion` | `via_contenciosa`.
- **V2 (Agotamiento de la Vía):** `no_agota_via` | `agota_via`.
- **V3 (Fase):** `primera_solicitud` | `ya_hubo_resolucion_o_silencio`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar el escrito y si el acto agota la vía administrativa, porque de ello depende el recurso procedente.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un gestor administrativo (de usted), confirmando el escrito que vais a preparar y advirtiendo en una línea de que los plazos frente a la Administración son perentorios.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué necesita, qué órgano dictó el acto y si la resolución indicaba el recurso procedente, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), el agotamiento de la vía (`V2`) o la fase (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar cual de los tres escritos frente a la Administracion se prepara.",
      "question": "¿Qué necesita preparar?",
      "options": [
        {"id": "recurso_administrativo", "label": "Recurrir una resolución administrativa que le perjudica"},
        {"id": "responsabilidad_patrimonial", "label": "Reclamar una indemnización por un daño causado por la Administración"},
        {"id": "acceso_informacion", "label": "Pedir información o documentación a una Administración"},
        {"id": "via_contenciosa", "label": "Ya agoté la vía administrativa y quiero acudir a los tribunales"}
      ]
    },
    {
      "id": "agota_via",
      "rationale": "Resolver V2: determina si procede recurso de alzada o de reposicion, que tienen plazos y organos distintos.",
      "question": "¿Indica la notificación que contra la resolución cabe recurso de alzada, o que agota la vía administrativa?",
      "options": [
        {"id": "no_agota_via", "label": "Cabe recurso de alzada, o lo dictó un órgano con superior jerárquico"},
        {"id": "agota_via", "label": "Agota la vía administrativa, o no lo sé con certeza"}
      ]
    },
    {
      "id": "via_previa",
      "rationale": "Resolver V3: la reclamacion de transparencia y el recurso exigen una resolucion o un silencio previos.",
      "question": "¿Es su primera petición a la Administración, o ya recibió respuesta o no le contestaron?",
      "options": [
        {"id": "primera_solicitud", "label": "Es la primera petición"},
        {"id": "ya_hubo_resolucion_o_silencio", "label": "Ya hubo resolución desfavorable o no me contestaron"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `agota_via`
- `V3` — `via_previa`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = via_contenciosa`:**
  - **DETENER.** Informar de que el recurso contencioso-administrativo exige demanda ante el juzgado o tribunal competente, con plazo de dos meses desde la notificación del acto que agota la vía administrativa (o seis meses en los supuestos de silencio), y con representación y defensa en los términos de la ley procesal. Derivar a abogado especialista en derecho administrativo. No crear documento.
- **Si `V1 = recurso_administrativo`:**
  - Escrito del sistema: `assets/template-recurso-administrativo.md`. Proceder a la **Fase 2**.
- **Si `V1 = responsabilidad_patrimonial`:**
  - Escrito del sistema: `assets/template-reclamacion-responsabilidad-patrimonial.md`. Proceder a la **Fase 2**.
- **Si `V1 = acceso_informacion`:**
  - Escrito del sistema: `assets/template-solicitud-acceso-informacion.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina si el recurso se redacta como de alzada ante el órgano superior jerárquico o como de reposición ante el mismo órgano, con sus plazos respectivos.
- `V3` no elige plantilla: determina si el escrito se formula como solicitud inicial o si incorpora la reclamación posterior por la desestimación o el silencio.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `lpacap-recursos-silencio-y-plazos.md`, `responsabilidad-patrimonial-y-transparencia.md` y `estilo-redaccion-escritos.md`.
2. **Cómputo del plazo como primera tarea:** solicita la fecha de notificación y calcula el vencimiento. Verifica además mediante `web_search`, cuando proceda, si la materia tiene un procedimiento **sectorial específico** con plazos propios (subvenciones, contratación pública, función pública, sanidad, educación) y si existe un órgano especializado de resolución, porque prevalecen sobre el régimen general.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal, Plazos y Riesgos:**
   - Para el recurso: explicar la regla que determina el recurso procedente. Si el acto **no agota** la vía administrativa, cabe **recurso de alzada** ante el órgano superior jerárquico, en el plazo de **un mes** si el acto es expreso, o de **tres meses** desde que se produzcan los efectos del silencio. Si el acto **agota** la vía, cabe **recurso de reposición** con carácter **potestativo**, en el plazo de un mes, o acudir directamente a la vía contencioso-administrativa.
   - Advertir de que el acto administrativo es **ejecutivo** y que interponer el recurso **no suspende** su eficacia: la suspensión debe pedirse expresamente y motivarse.
   - Explicar el **silencio**: transcurrido el plazo de resolución, el silencio es con carácter general estimatorio en los procedimientos iniciados a solicitud del interesado, con importantes excepciones legales, y desestimatorio en los procedimientos de responsabilidad patrimonial y en los recursos, con la salvedad del recurso interpuesto contra la desestimación por silencio.
   - Para la responsabilidad patrimonial: explicar los cuatro requisitos (daño efectivo, evaluable económicamente e individualizado; relación de causalidad con el funcionamiento del servicio público; ausencia de deber jurídico de soportar el daño; y que no concurra fuerza mayor) y el plazo de **un año** desde el hecho o desde la curación o determinación del alcance de las secuelas.
   - Para el acceso a la información: explicar el plazo de resolución de **un mes** y la posibilidad de **reclamación** ante el órgano de transparencia competente antes de la vía judicial.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta el escrito **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que identifique correctamente el acto y el órgano competente, que no confunda alzada con reposición y que no omita la solicitud de suspensión cuando sea necesaria, advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `recurso_administrativo.md`, `reclamacion_responsabilidad_patrimonial.md` o `solicitud_acceso_informacion.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa, incluidas la fecha del sistema y las fechas límite calculadas. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta sección?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro administrativo (por ejemplo, *"Pasamos ahora a los motivos de impugnación"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Búsqueda prioritaria de partes e intervinientes y Regla de Cero Redundancia (`search_clients` / `get_client` — REG-CLI-01 y REG-CLI-02):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01` de `CLAUDE.md`. Si los datos de una persona ya fueron obtenidos mediante `search_clients` o `get_client`, **queda TERMINANTEMENTE PROHIBIDO volver a pedir dicha información** (nombre, DNI/NIE/CIF, domicilio, contacto, etc.), ya sea en el chat o en `slot_filling_request` (`REG-CLI-02`). Si todos los datos requeridos constan en la ficha del cliente, **NO invoques `slot_filling_request`**: redacta directamente la cláusula, muestra la vista previa en texto plano en el chat y pide confirmación. Solo si faltan campos específicos ausentes en la ficha, invocarás `slot_filling_request` exclusivamente para los datos pendientes.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta sección?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** comprueba que la fecha de notificación es anterior a la del escrito y que el plazo no ha vencido, que el recurso elegido se corresponde con el agotamiento o no de la vía, que el órgano al que se dirige es el competente y que la valoración del daño suma lo que se reclama. Si el plazo ha vencido o el recurso elegido no es el procedente, **dilo con claridad antes de seguir redactando**.

### Hoja de Ruta de Secciones — RAMA RECURSO ADMINISTRATIVO:

1. **Interesado, representación y órgano** *(confirmación agrupada)*: identidad y NIF del interesado, domicilio y medio de notificación preferente, representante y título de la representación, y órgano al que se dirige el recurso conforme a `V2`.
2. **Acto que se recurre y cómputo del plazo**: identificación del acto, número de expediente, fecha de la resolución y de su notificación, con el cómputo expreso del plazo y su fecha límite; o determinación de los efectos del silencio si no hubo resolución expresa.
3. **Antecedentes**: cronología del procedimiento, solicitudes presentadas, trámites practicados y contenido de la resolución impugnada.
4. **Motivos de forma**: defectos del procedimiento (falta de motivación, omisión del trámite de audiencia, incompetencia del órgano, defectos de notificación, caducidad del procedimiento), con la indefensión que producen.
5. **Motivos de fondo**: error en los hechos, indebida aplicación o interpretación de la norma, desviación de poder, vulneración de la confianza legítima, desproporción de la medida y, en su caso, vulneración de derechos fundamentales.
6. **Solicitud de suspensión de la ejecución**: petición expresa y motivada de suspensión, con la exposición de los perjuicios de imposible o difícil reparación o de la causa de nulidad de pleno derecho en que se funde, y ofrecimiento de garantía si procede.
7. **Petición, prueba y documentos**: pretensión concreta (anulación total o parcial, retroacción del procedimiento, reconocimiento del derecho solicitado), proposición de prueba y relación de documentos que se acompañan.

### Hoja de Ruta de Secciones — RAMA RESPONSABILIDAD PATRIMONIAL:

1. **Reclamante y administración responsable** *(confirmación agrupada)*: identidad y NIF, domicilio y contacto, y administración y servicio público al que se imputa el daño.
2. **Hechos y cómputo del plazo**: relato del hecho dañoso con fecha, hora y lugar precisos, y cómputo del plazo de un año desde el hecho o desde la curación o la determinación del alcance de las secuelas, con la fecha límite.
3. **Daño: efectividad, evaluación e individualización**: descripción del daño y de su alcance, acreditación de que es efectivo, económicamente evaluable e individualizado en el reclamante.
4. **Relación de causalidad y funcionamiento del servicio**: explicación del nexo causal entre el funcionamiento normal o anormal del servicio público y el daño, con la prueba que lo acredita, y análisis de la eventual concurrencia de culpa del perjudicado o de terceros.
5. **Ausencia de deber jurídico de soportar el daño y de fuerza mayor**: razonamiento de que el perjudicado no tenía obligación de soportarlo y de que no concurre fuerza mayor.
6. **Valoración del daño**: desglose por conceptos (daños materiales, gastos acreditados, lucro cesante, daño personal con referencia al sistema de valoración que se aplique y daño moral), con su justificación documental y el total reclamado.
7. **Petición, prueba y documentos**: solicitud de indemnización con su importe e intereses, proposición de prueba (documental, pericial y testifical), y relación de documentos.

### Hoja de Ruta de Secciones — RAMA ACCESO A LA INFORMACIÓN:

1. **Solicitante y órgano** *(confirmación agrupada)*: identidad, NIF, domicilio y medio de notificación, y administración u organismo al que se dirige la solicitud.
2. **Información que se solicita**: descripción precisa de la información o documentación, periodo temporal, y formato o soporte preferido, haciendo constar que no es necesario motivar la solicitud.
3. **Fundamento del derecho**: invocación del derecho de acceso a la información pública, con la advertencia de que los límites y las causas de inadmisión son de interpretación restrictiva y deben ser motivados.
4. **Anticipación de límites y protección de datos**: cuando la información pueda contener datos personales, solicitud de acceso a la información **anonimizada o parcial**, para evitar una denegación total innecesaria.
5. **Plazo y silencio**: mención del plazo de resolución de un mes, prorrogable en los supuestos legales, y del efecto del silencio.
6. **Reclamación posterior**: *Condicional `V3 = ya_hubo_resolucion_o_silencio`:* reclamación ante el órgano de transparencia competente, con la identificación de la solicitud inicial, de la respuesta o del silencio, y con la crítica motivada del límite aplicado.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
El escrito ha sido generado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (motivos, valoración del daño o información solicitada).
2. Añadir un motivo de impugnación adicional.
3. Añadir o reforzar la solicitud de suspensión de la ejecución del acto.
4. Revisar la coherencia global y realizar control de calidad previo a la presentación.
5. Dar el escrito por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el escrito es un borrador preparatorio; debe ser revisado por un gestor administrativo o letrado antes de su presentación.
2. **Plazos perentorios:** un mes para el recurso de alzada y para el de reposición frente a actos expresos; tres meses para la alzada frente al silencio; un año para la reclamación de responsabilidad patrimonial; dos meses para el recurso contencioso-administrativo. Vencidos, el acto queda consentido y firme.
3. **El acto se ejecuta aunque se recurra:** la interposición del recurso no suspende su eficacia. Si conviene evitar la ejecución, hay que **pedir la suspensión expresamente y motivarla**, y valorar el ofrecimiento de garantía.
4. **Recurso de reposición potestativo:** cuando el acto agota la vía administrativa, el recurso de reposición es opcional. Interponerlo consume tiempo, pero también reabre el plazo del contencioso desde su resolución o desde su desestimación presunta. Es una decisión de estrategia que debe explicarse al cliente.
5. **Silencio:** conviene no confiar en el silencio estimatorio sin verificar la excepción aplicable a la materia concreta. En los recursos y en la responsabilidad patrimonial el silencio es desestimatorio.
6. **Procedimientos sectoriales:** subvenciones, contratación pública, función pública, tributos y extranjería tienen cauces y plazos propios que prevalecen sobre el régimen general. Debe comprobarse antes de presentar.
7. **Presentación:** por registro electrónico de la administración competente, por registro general o por cualquiera de los medios legalmente admitidos, conservando siempre el justificante con su fecha y hora.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar plazos, preceptos u órganos, y comprobar si la materia tiene procedimiento sectorial propio.
2. **Cómputo del plazo como paso bloqueante:** antes de redactar, calcular el plazo desde la notificación. Si ha vencido, comunicarlo con claridad y explicar las vías que quedan (revisión de oficio, nulidad de pleno derecho) sin presentar un recurso manifiestamente extemporáneo como si fuera viable.
3. **Cero Invención de Datos:** prohibido inventar números de expediente, fechas de notificación, órganos, importes o referencias de subvención. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
4. **Órgano competente:** no dirigir el recurso al órgano equivocado. Si no consta con certeza, hacerlo constar como dato pendiente y advertir de la necesidad de comprobarlo.
5. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
6. **Límites de Alcance:** no preparar recursos contencioso-administrativos, ni reclamaciones económico-administrativas en materia tributaria, ni recursos de tráfico o de extranjería, que corresponden a otras skills o a profesional competente.
