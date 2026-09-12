---
name: monitorio
description: >
  Genera la peticion inicial de proceso monitorio para reclamar una deuda dineraria liquida,
  determinada, vencida y exigible de cualquier cuantia, conforme a los articulos 812 a 818 de la
  **Ley 1/2000 de Enjuiciamiento Civil (LEC)**, que regula el proceso monitorio como via rapida para cobrar deudas documentadas, en su version consolidada vigente verificada en el BOE.
  Opcionalmente genera tambien el burofax de requerimiento previo (intento de MASC). Adapta el
  documento segun la naturaleza de las partes y el tipo de deuda (rentas de arrendamiento u otra).
  NO usar para deudas no dinerarias, iliquidas o controvertidas, ni para reclamaciones frente a
  Administraciones Publicas.
when_to_use: |
  - El usuario quiere reclamar el cobro de una deuda dineraria impagada.
  - El usuario dispone de documentos que acreditan la deuda (facturas, contrato, reconocimiento, rentas).
  - El usuario pide una peticion de monitorio o un burofax previo de reclamacion de pago.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - alcance: solo peticion inicial / peticion inicial + burofax previo
  - tipo_deuda: rentas de arrendamiento / otra (facturas, prestamo, servicios, comunidad de propietarios)
  - naturaleza_acreedor: persona fisica o persona juridica
  - datos_acreedor: nombre o razon social, NIF o CIF, domicilio
  - datos_deudor: nombre o razon social, NIF o CIF, domicilio o lugar donde pueda ser hallado
  - origen_deuda: descripcion del origen y documentos que la acreditan
  - cuantia: principal en euros e intereses si proceden
  - fecha_vencimiento: fecha en que la deuda vencio y devino exigible
  - partido_judicial: domicilio del deudor a efectos de competencia (Art. 813)
  - masc_intentado: si se ha intentado un medio adecuado de solucion de controversias (si / no)
outputs:
  - peticion_monitorio: peticion inicial de proceso monitorio en markdown, DRAFT
  - burofax_requerimiento: opcional, burofax de requerimiento previo en markdown, DRAFT
references:
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-documentos-acreditativos-deuda.md
  - references/lec-proceso-monitorio-812-818.md
  - references/masc-requisito-procedibilidad-lo1-2025.md
assets:
  - assets/template-burofax-requerimiento-previo-masc.md
  - assets/template-peticion-inicial-monitorio-rentas.md
  - assets/template-peticion-inicial-monitorio.md
---

# Generar Peticion de Proceso Monitorio

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación —cuyo catálogo y su correspondencia con las respuestas del formulario figuran en la Fase 1.2— y el origen de la plantilla (`origen_plantilla`).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas (por ejemplo, anotar un vector como resuelto) son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la naturaleza del caso y fijar los vectores deterministas de estado.

### 1.1 Escucha Activa Previa
Antes de abrir formularios interactivos o hacer preguntas, analiza el mensaje inicial del usuario y la documentación aportada:
- Si el mensaje ya especifica inequívocamente los vectores de la operación, asígnalos de forma inmediata y silenciosa en memoria y pasa a la **Fase 2**.
- Si restan vectores por definir, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado interactivo mediante la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las opciones de triaje:

```json
{
  "form_data": [
    {
      "id": "alcance",
      "rationale": "Resolver V1: determina si además de la petición inicial se genera el burofax de requerimiento previo, útil para acreditar el intento de solución previa.",
      "question": "¿Qué alcance tiene el encargo?",
      "options": [
        {"id": "solo_peticion", "label": "Solo la petición inicial del proceso monitorio"},
        {"id": "peticion_y_burofax", "label": "La petición inicial y, antes, el burofax de requerimiento previo de pago"}
      ]
    },
    {
      "id": "tipo_deuda",
      "rationale": "Resolver V2: las rentas de arrendamiento tienen variante propia de petición inicial y régimen específico de acreditación.",
      "question": "¿De dónde procede la deuda?",
      "options": [
        {"id": "rentas_arrendamiento", "label": "Rentas de arrendamiento impagadas"},
        {"id": "otra_causa", "label": "Otra causa: facturas, préstamo, servicios o gastos de comunidad"}
      ]
    },
    {
      "id": "naturaleza_acreedor",
      "rationale": "Resolver V3: fija la estructura de comparecencia y la acreditación de la representación en la petición inicial.",
      "question": "¿Quién es el acreedor?",
      "options": [
        {"id": "persona_fisica", "label": "Persona física"},
        {"id": "persona_juridica", "label": "Persona jurídica"}
      ]
    },
    {
      "id": "masc_intentado",
      "rationale": "Resolver V4: el intento de un medio adecuado de solución de controversias condiciona la procedibilidad conforme a la Ley Orgánica 1/2025.",
      "question": "¿Se ha intentado ya algún medio de solución previa: burofax, mediación o negociación?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `alcance`
- `V2` — `tipo_deuda`
- `V3` — `naturaleza_acreedor`
- `V4` — `masc_intentado`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores, evalua en este orden:

- Si **V2 = rentas_arrendamiento** → **HOJA RENTAS**: `assets/template-peticion-inicial-monitorio-rentas.md` (Art. 812.2.2.º LEC, que admite acumular las rentas y cantidades debidas del arrendamiento).
- Si **V2 = otra causa** → **HOJA GENERAL**: `assets/template-peticion-inicial-monitorio.md`.
- Si **V1 = peticion_y_burofax**, o **V4 = no** → generar ademas, y **ANTES** de la peticion inicial, `assets/template-burofax-requerimiento-previo-masc.md`. El requerimiento fehaciente previo no es presupuesto de admision del monitorio, pero por defecto conservador se recomienda dejarlo acreditado: constituye en mora, fija la fecha de devengo de los intereses y evita la discusion sobre la procedibilidad. Explicaselo al cliente en esos terminos, sin presentarlo como obligatorio.
- Si **V1 = solo_peticion** y **V4 = si** → no se genera el burofax; se hace constar en la peticion el intento ya practicado.
- V3 no elige asset: determina la variante del encabezamiento de comparecencia y la acreditacion de la representacion (persona fisica, o persona juridica con su representante y el titulo del que resulta la representacion).
- Si la deuda **no es dineraria, liquida, determinada, vencida y exigible** (Art. 812.1 LEC) → **DETENER**: el monitorio no es el cauce. Derivar a `reclamacion-cantidad` para que elija la via declarativa procedente. No crear documento.
- Si lo que se pretende es **oponerse** a un monitorio ya notificado al cliente → **DETENER**: derivar a `reclamacion-cantidad`, que cubre el escrito de oposicion. No crear documento.
- Si la deuda es de **cuotas de comunidad de propietarios** → **DETENER** y derivar a `propiedad-horizontal`, que exige la certificacion previa del acuerdo de la junta (articulos 21.1 a 21.3 de la Ley de Propiedad Horizontal) y tiene su propia peticion inicial.
- **Requisito de procedibilidad (Ley Organica 1/2025).** Si el intento previo de un medio adecuado de solucion de controversias no esta acreditado y esta skill no genera por si misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociacion, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaracion responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a tramite.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
Ejecuta esta secuencia completa; en esta materia la verificación no es opcional:


La skill verifica las fuentes oficiales en cada lanzamiento y, si detecta una version posterior, aplica la redaccion vigente al documento que redacta en el workspace del usuario, sin modificar sus propios archivos de plugin. Ejecutar SIEMPRE esta secuencia:

- **Leer la fecha/version registrada localmente.** Consultar `references/fuentes-plantillas-validadas.md`, que llega cargada en tu contexto, y anotar la "Version registrada" de la LEC y del modelo del CGPJ.

- **Consultar la fuente oficial vigente.** Invocar:
```
web_search(...)
```
Extraer: fecha del texto consolidado vigente de la LEC; redaccion actual de los arts. 812 a 818 y del art. 264 (acreditacion del intento de MASC); estado de aplicacion de la LO 1/2025 (BOE-A-2025-76).

Consultar tambien el modelo normalizado del CGPJ:
```
web_search(...)
```

- **Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

- **Aplicación de la redacción vigente.** Si la versión oficial es posterior o el texto de los artículos ha cambiado, aplica la redacción vigente directamente sobre el documento a redactar en el workspace del usuario, sin usar versiones desactualizadas.

- **Fallback si la fuente no es accesible.** Si `web_search` no devuelve la fuente oficial:
```
web_search("Ley Enjuiciamiento Civil proceso monitorio articulos 812 818 texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. La peticion se genera con la version de referencia. Verificar manualmente antes de presentar."

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 812 a 818 de la Ley de Enjuiciamiento Civil (LEC), modificados por RDL 6/2023 y LO 1/2025; Art. 21 de la Ley de Propiedad Horizontal; y Art. 813 LEC (competencia territorial improrrogable del domicilio del deudor).
2. **Orientación Legal del Caso:**
   Informa al usuario, en registro formal, de la norma y los artículos aplicables a la ruta resuelta, con la versión vigente verificada en la Fase 2.1 y el enlace de la fuente consultada.

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** y nombrala por su ruta. Si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la seccion de assets.
4. **Pregunta Explícita al Usuario (Vía Chat):** Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
* **Si `[origen_plantilla = plantilla_sistema]` (El usuario acepta la plantilla propuesta):**
  Toma el texto íntegro de la plantilla correspondiente directamente desde el catálogo del prompt y procede de inmediato a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]` (El usuario aporta su propia minuta adjuntando un documento o pegando texto):**
  1. Accede al contenido del adjunto desde `<attached_documents>` o el mensaje del usuario.
  2. **Guardrail de Verificación Legal:** Analiza el texto aportado. Si contiene cláusulas nulas, contrarias a normas imperativas o de imposible cumplimiento, adviértelo expresamente en el chat y propón la redacción legalmente válida.
  3. Adopta la minuta revisada como base y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos e inserta `{{DATO_FALTANTE}}` para aquellos que deban resolverse durante la redacción.
   - PROHIBIDO dejar archivos en blanco, crear resúmenes o esquemas provisionales.
2. **Validación de Integridad:**
   - La comprobación de integridad y contenido del archivo creado se realiza consultando prioritariamente la sección `# WORKSPACE ACTIVE DOCUMENTS` del prompt, donde el sistema mantiene siempre la última versión de todos los documentos. Solo se debe invocar `read_file` si es estrictamente necesario y en algún caso extremo (ej. el archivo no aparece en dicha sección o contenido truncado).

3. **Confirmación en Chat y Encadenamiento Inmediato:**
   - Informa al usuario de la ruta absoluta del documento creado.
   - En esa **misma respuesta**, introduce la primera sección/cláusula de la **Fase 4** y formula ya su primera pregunta, sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

### Protocolo Obligatorio de Edición
Para cada cláusula o bloque temático del documento, ejecuta estrictamente el siguiente ciclo interactivo:
```
[Pregunta al Usuario] --> [Vista Previa en texto plano] --> [¿Confirmamos?] --> [edit_file en el editor]
```
1. **Pregunta en Chat:** Solicita los datos específicos de la sección.
2. **Vista Previa:** Muestra el texto exacto redactado en texto plano en el chat.
3. **Confirmación:** Consulta al usuario si está conforme o desea algún ajuste.
4. **Persistencia en Disco:** Una vez confirmado, ejecuta `edit_file` con `old_string` y `new_string` exactos. La verificación del documento se realiza prioritariamente a través de la sección `# WORKSPACE ACTIVE DOCUMENTS`, recurriendo a `read_file` únicamente en casos extremos y estrictamente necesarios.

**Petición de grupos de datos mediante `search_clients` y `slot_filling_request`, y confirmaciones en el chat:**
- **Búsqueda prioritaria, Cero Redundancia y Guardado de Nuevos Clientes (`search_clients` / `get_client` / `save_client` — REG-CLI-01, REG-CLI-02 y REG-CLI-03):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01`. Si los datos ya constan en el sistema, **queda TERMINANTEMENTE PROHIBIDO volver a pedirlos** (`REG-CLI-02`) y se omite `slot_filling_request`. Si se especifican datos de una persona nueva (por formulario o chat), **DEBES invocar INMEDIATAMENTE `restricted_human_in_the_loop_request`** para preguntar al usuario si desea guardarla como nuevo cliente (`REG-CLI-03`), quedando **TERMINANTEMENTE PROHIBIDO emitir la vista previa de la cláusula o decir 'le preguntaré después' antes de resolver el guardado**. En caso afirmativo, invoca `save_client` con los campos disponibles. Solo tras resolver el guardado (o si el usuario lo rechaza), continúa con el flujo normal de vista previa y confirmación de la cláusula.
- **Grupos de datos estructurados no de cliente (MANDATORIO con `slot_filling_request`):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
- **Campos omitidos o negativa expresa (No insistencia):** Si el usuario pide explícitamente no aportar determinados campos de información, pásalos por alto de inmediato sin insistir en pedirlos ni presionar. Rellena la plantilla con los datos disponibles, conserva los no aportados como marcadores pendientes ({{NOMBRE_CAMPO}} o {{DATO_FALTANTE}}) e indica en la confirmación cuáles faltan antes de continuar con la siguiente sección.
- **Validación de sentido, no solo de formato:** razone si la respuesta tiene sentido en el contexto de lo preguntado. Si es absurda, imposible o incongruente, dialogue en el chat, señale el motivo y pida aclaración antes de volcarla al documento.

### Hoja de Ruta de Secciones y Cláusulas Condicionales

1. **Parte acreedora** *(confirmación agrupada)*: nombre completo o razón social, NIF/CIF, domicilio a efectos de notificaciones. Si es persona jurídica: datos del representante legal.
2. **Parte deudora** *(confirmación agrupada)*: nombre completo o razón social, NIF/CIF, domicilio o lugar donde pueda ser hallado para el requerimiento judicial (art. 813 LEC).
3. **Origen de la deuda y documentos acreditativos**: origen de la deuda (rentas, facturas, contrato, préstamo), desglose de los documentos que la acreditan conforme al art. 812 LEC, fechas de vencimiento y exigibilidad.
4. **Cuantía reclamada e intereses**: principal adeudado en euros e intereses solicitados (pactados o legal del dinero devengados desde el vencimiento).
5. **Juzgado competente**: determinación formal del Juzgado de Primera Instancia del domicilio del deudor (art. 813 LEC).
6. **Requerimiento previo MASC** *(solo si V4 = no, burofax)*: plazo otorgado para el pago (10 días hábiles recomendados), cuenta IBAN de ingreso y medios de contacto para la solución negociada.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones del documento, presenta al usuario un menú interactivo:
```
1. Modificar o ajustar una cláusula o sección existente.
2. Añadir una estipulación o pacto adicional a medida.
3. Eliminar contenido opcional o corregir datos de partes/fincas.
4. Revisar la coherencia global y realizar control de calidad final.
5. Dar el documento por finalizado y cerrar la sesión.
```
### Advertencias Legales Preceptivas de Cierre:
Al dar por finalizado el documento, emite siempre las siguientes advertencias:
- **Carácter DRAFT:** El documento generado es un borrador profesional que debe ser revisado por un abogado colegiado antes de su firma o presentación procesal.
- **Obligaciones Fiscales y Plazos:** Recuerda los plazos de liquidación de tributos (ITP/AJD o Plusvalía municipal en 30 días hábiles) cuando proceda.
- **Elevación a Instrumento Público:** Recuerda que para la inscripción en el Registro de la Propiedad o Mercantil, o para su ejecución forzosa directa, es necesario el otorgamiento ante Notario público.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version de la LEC posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario. No usar una version desactualizada.
3. Solo procede el monitorio si la deuda es dineraria, liquida, determinada, vencida y exigible (Art. 812). Si no lo es, no redactar la peticion: advertir y ofrecer alternativa (juicio declarativo) o escalacion.
4. Debe existir al menos un documento que acredite la deuda (Art. 812). Sin documento acreditativo, no procede.
5. Competencia exclusiva del Juzgado de Primera Instancia del domicilio o residencia del deudor (Art. 813). No admitir sumision a otro fuero.
6. Posicion conservadora sobre el MASC: ante la duda sobre si es exigible en el monitorio (LO 1/2025), recomendar e integrar el intento previo (burofax) y advertir de la cuestion.
7. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{CUANTIA_RECLAMADA}}` (NUNCA corchete simple `[DATO]`: colisiona con los identificadores de privacidad `[PERSON_1]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `edit_file` posterior necesita un `oldString` unico. Nunca inventar datos, cuantias ni fechas.
8. Nunca afirmar que la deuda es exigible o incontrovertida sin base documental. Nunca inventar jurisprudencia.
