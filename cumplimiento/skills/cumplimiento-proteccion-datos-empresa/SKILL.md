---
name: cumplimiento-proteccion-datos-empresa
description: >
  Prepara la documentacion de proteccion de datos que debe tener una empresa cliente conforme al
  **Reglamento (UE) 2016/679** general de proteccion de datos, que impone el registro de actividades de
  tratamiento, el contrato con el encargado y la notificacion de brechas, y a la **Ley Organica
  3/2018** de proteccion de datos personales y garantia de los derechos digitales, que lo desarrolla en
  Espana y fija los supuestos de delegado de proteccion de datos obligatorio.


  Genera tres documentos: el registro de actividades de tratamiento con su base de licitud y sus
  plazos de conservacion, el contrato de encargado del tratamiento con el contenido minimo exigido, y
  la notificacion de violacion de seguridad a la Agencia Espanola de Proteccion de Datos con su
  comunicacion a los interesados.


  Determina la base de licitud de cada tratamiento, distingue responsable de encargado, computa el
  plazo de setenta y dos horas para notificar una brecha y el de un mes para atender los derechos de
  los interesados, y advierte de cuando la designacion de delegado de proteccion de datos o la
  evaluacion de impacto dejan de ser opcionales.


  NO usar para la defensa ante un expediente sancionador ya abierto por la autoridad de control, ni
  para transferencias internacionales que exijan clausulas contractuales tipo o normas corporativas
  vinculantes, ni para el paquete de proteccion de datos del propio despacho, que corresponde a la
  skill de proteccion de datos del despacho.


  Normas aplicadas, en su texto consolidado:
  [Reglamento General de Proteccion de Datos](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679)
  en el Diario Oficial de la Union Europea, y
  [Ley Organica 3/2018](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673) en el BOE.
when_to_use: |
  - La empresa no tiene registro de actividades de tratamiento y necesita crearlo.
  - La empresa va a contratar un proveedor que accedera a datos personales y necesita el contrato de encargado.
  - La empresa ha sufrido una brecha de seguridad y hay que notificarla.
  - El usuario pregunta que base legal ampara un tratamiento concreto o cuanto tiempo puede conservar los datos.
  - El usuario pregunta si su empresa esta obligada a tener delegado de proteccion de datos.
  - El usuario pregunta que hacer ante una solicitud de acceso, supresion u oposicion de un cliente o empleado.
inputs:
  - documento: registro de actividades / contrato de encargado / notificacion de brecha (V1)
  - papel_entidad: responsable del tratamiento / encargado del tratamiento (V2)
  - nivel_riesgo: tratamiento ordinario / categorias especiales o alto riesgo (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_entidad: razon social, CIF, domicilio, actividad y numero de personas trabajadoras
  - datos_contacto_privacidad: responsable interno, delegado de proteccion de datos si existe, y correo de contacto
  - tratamientos: finalidades, categorias de interesados y de datos, y origen de los datos
  - bases_licitud: base juridica de cada tratamiento y, si es consentimiento, forma de obtenerlo
  - destinatarios: cesiones previstas, encargados y transferencias internacionales
  - plazos_conservacion: plazo o criterio de conservacion de cada tratamiento
  - medidas_seguridad: medidas tecnicas y organizativas implantadas
  - datos_encargado: razon social del proveedor, servicio prestado, subencargados y ubicacion de los datos
  - datos_brecha: fecha y hora de deteccion, naturaleza del incidente, datos y personas afectadas, medidas adoptadas
outputs:
  - registro_actividades_tratamiento: registro de actividades de tratamiento por finalidad, DRAFT
  - contrato_encargado_tratamiento: contrato de encargado del tratamiento con contenido minimo, DRAFT
  - notificacion_brecha: notificacion de violacion de seguridad a la autoridad y comunicacion a interesados, DRAFT
  - checklist_cumplimiento: obligaciones exigibles segun plantilla y riesgo, con sus plazos
references:
  - references/rgpd-registro-encargado-y-brechas.md
  - references/bases-licitud-plazos-y-derechos.md
  - references/estilo-redaccion-cumplimiento.md
assets:
  - assets/template-registro-actividades-tratamiento.md
  - assets/template-contrato-encargado-tratamiento.md
  - assets/template-notificacion-brecha-seguridad.md
---

# Documentación de Protección de Datos de la Empresa (Registro, Encargado y Brechas)

> DRAFT — para revisión por un abogado o consultor de cumplimiento antes de su aprobación y publicación. No constituye asesoramiento jurídico vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva y rigurosa a través de un procedimiento estructurado en 5 fases secuenciales para preparar la documentación de protección de datos de la empresa.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `registro_actividades` | `contrato_encargado` | `notificacion_brecha` | `expediente_sancionador`.
- **V2 (Papel de la Entidad):** `responsable` | `encargado`.
- **V3 (Nivel de Riesgo):** `tratamiento_ordinario` | `alto_riesgo`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar qué documento se prepara y en qué posición está la entidad.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un consultor de cumplimiento (de usted), confirmando que vais a preparar la documentación de protección de datos de la empresa.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué documento necesita, si la empresa actúa como responsable o como encargado y si hay datos sensibles, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), el papel de la entidad (`V2`) o el nivel de riesgo (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar cual de los tres documentos de proteccion de datos se prepara.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "registro_actividades", "label": "Registro de actividades de tratamiento de la empresa"},
        {"id": "contrato_encargado", "label": "Contrato con un proveedor que accede a datos personales"},
        {"id": "notificacion_brecha", "label": "Notificación de una brecha o incidente de seguridad"},
        {"id": "expediente_sancionador", "label": "Ya hay un expediente abierto por la Agencia Española de Protección de Datos"}
      ]
    },
    {
      "id": "papel_entidad",
      "rationale": "Resolver V2: responsable y encargado tienen obligaciones distintas y el contrato se redacta desde una posicion u otra.",
      "question": "¿En esta relación su empresa decide para qué se usan los datos, o los trata por cuenta de otra empresa?",
      "options": [
        {"id": "responsable", "label": "Decide las finalidades (responsable del tratamiento)"},
        {"id": "encargado", "label": "Los trata por cuenta de un cliente (encargado del tratamiento)"}
      ]
    },
    {
      "id": "nivel_riesgo",
      "rationale": "Resolver V3 para advertir de la evaluacion de impacto y del delegado de proteccion de datos obligatorio.",
      "question": "¿Se tratan datos de salud, biométricos, ideológicos, de menores, o se elaboran perfiles con efectos relevantes?",
      "options": [
        {"id": "tratamiento_ordinario", "label": "No: datos identificativos, de contacto, laborales o de facturación"},
        {"id": "alto_riesgo", "label": "Sí, alguno de esos casos"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `papel_entidad`
- `V3` — `nivel_riesgo`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = expediente_sancionador`:**
  - **DETENER.** Informar de que la defensa ante un expediente sancionador ya abierto exige alegaciones con plazos propios y estrategia probatoria, y que la documentación que se elabore a partir de ese momento puede ser examinada por la autoridad. Derivar a abogado especialista en protección de datos. No crear documento.
- **Si `V1 = registro_actividades`:**
  - Plantilla del sistema: `assets/template-registro-actividades-tratamiento.md`. Proceder a la **Fase 2**.
- **Si `V1 = contrato_encargado`:**
  - Plantilla del sistema: `assets/template-contrato-encargado-tratamiento.md`. Proceder a la **Fase 2**.
- **Si `V1 = notificacion_brecha`:**
  - Plantilla del sistema: `assets/template-notificacion-brecha-seguridad.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina desde qué posición se redacta el contrato y qué obligaciones se imponen a la otra parte.
- `V3` no elige plantilla: determina si se activan las advertencias de evaluación de impacto, de delegado de protección de datos obligatorio y de comunicación a los interesados.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `rgpd-registro-encargado-y-brechas.md`, `bases-licitud-plazos-y-derechos.md` y `estilo-redaccion-cumplimiento.md`.
2. Opcionalmente verifica mediante `web_search` las guías y el formulario de notificación de brechas vigentes de la Agencia Española de Protección de Datos. Aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal, Obligación y Riesgo:**
   - Para el registro de actividades: explicar que es una obligación documental cuya **ausencia es en sí misma infracción**, con independencia de que exista o no incidente, y que es el primer documento que solicita la autoridad en cualquier actuación.
   - Para el contrato de encargado: explicar que la comunicación de datos a un proveedor **sin contrato** es una infracción autónoma, y que el contrato debe recoger un contenido mínimo tasado.
   - Para la notificación de brecha: comunicar el plazo de **setenta y dos horas** desde el conocimiento del incidente para notificar a la autoridad, y el deber adicional de comunicar a los interesados cuando el riesgo sea alto; explicar que la notificación tardía se sanciona de forma independiente del incidente.
   - Advertir del marco sancionador y de que la documentación sirve como prueba de diligencia.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta la plantilla **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que no omita el contenido mínimo legalmente exigido ni contenga cláusulas que exoneren indebidamente al encargado, advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `registro_actividades_tratamiento.md`, `contrato_encargado_tratamiento.md` o `notificacion_brecha_seguridad.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa, incluida la fecha del sistema y el cómputo del plazo de setenta y dos horas cuando proceda. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta sección?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro técnico-normativo (por ejemplo, *"Pasamos ahora a fijar la base de licitud de cada tratamiento"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Búsqueda prioritaria, Cero Redundancia y Guardado de Nuevos Clientes (`search_clients` / `get_client` / `save_client` — REG-CLI-01, REG-CLI-02 y REG-CLI-03):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01`. Si los datos ya constan en el sistema, **queda TERMINANTEMENTE PROHIBIDO volver a pedirlos** (`REG-CLI-02`) y se omite `slot_filling_request`. Si se especifican datos de una persona nueva (por formulario o chat), **pregunta al usuario mediante formulario (`restricted_human_in_the_loop_request`) si desea guardarla como nuevo cliente** (`REG-CLI-03`). En caso afirmativo, invoca `save_client` con los campos disponibles. Luego de esto (o si es negativo), continúa con el flujo normal de redacción y confirmación de la skill.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta sección?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** comprueba que la base de licitud declarada es compatible con la finalidad, que el plazo de conservación no es indefinido sin justificación, que las categorías de datos declaradas se corresponden con la finalidad y que, en una brecha, la fecha de detección es coherente con el plazo de notificación. Si la base de licitud invocada no sostiene el tratamiento, **dilo antes de volcarlo**.

### Hoja de Ruta de Secciones — RAMA REGISTRO DE ACTIVIDADES:

1. **Identificación del responsable y contacto de privacidad** *(confirmación agrupada)*: razón social, CIF, domicilio, actividad, número de personas trabajadoras, responsable interno y delegado de protección de datos si existe.
2. **Inventario de tratamientos**: relación de finalidades reales de la empresa (clientes y facturación, personal y nóminas, candidaturas, videovigilancia, marketing, proveedores, web y cookies), descartando las que no realiza.
3. **Por cada tratamiento: interesados, datos y origen**: categorías de interesados, categorías de datos y procedencia. *Condicional `V3 = alto_riesgo`:* identificación expresa de las categorías especiales y de la excepción que las habilita.
4. **Base de licitud y finalidad**: base jurídica de cada tratamiento con su justificación, y forma de obtención del consentimiento cuando sea la base.
5. **Destinatarios, encargados y transferencias**: cesiones legalmente previstas, proveedores que acceden a datos y su contrato, y transferencias internacionales con su garantía.
6. **Plazos de conservación y medidas de seguridad**: plazo o criterio por tratamiento, con su fundamento legal o contable, y medidas técnicas y organizativas implantadas.
7. **Aprobación y revisión**: órgano que aprueba, fecha, versión y periodicidad de revisión del registro.

### Hoja de Ruta de Secciones — RAMA CONTRATO DE ENCARGADO:

1. **Partes y posición de cada una** *(confirmación agrupada)*: identificación del responsable y del encargado, con sus datos y representantes, y determinación expresa de quién es cada uno.
2. **Objeto, duración y naturaleza del tratamiento**: servicio prestado, operaciones que se realizan sobre los datos, finalidad, tipo de datos y categorías de interesados.
3. **Instrucciones y obligaciones del encargado**: tratamiento conforme a instrucciones documentadas, deber de confidencialidad extensivo a su personal, prohibición de uso para fines propios y de comunicación a terceros.
4. **Subencargados**: régimen de autorización previa, obligación de imponerles las mismas obligaciones y responsabilidad del encargado por su actuación.
5. **Seguridad, brechas y asistencia**: medidas de seguridad, deber de comunicar cualquier brecha al responsable **sin dilación indebida**, y asistencia en la atención de derechos, en las evaluaciones de impacto y en las consultas a la autoridad.
6. **Ubicación de los datos y transferencias**: ubicación de los servidores y régimen de las transferencias internacionales, con la garantía aplicable.
7. **Destino de los datos al finalizar y auditoría**: devolución o supresión con certificación, plazo, y derecho del responsable a auditar o a recibir evidencias de cumplimiento.

### Hoja de Ruta de Secciones — RAMA NOTIFICACIÓN DE BRECHA:

1. **Entidad notificante y contacto** *(confirmación agrupada)*: identificación del responsable, persona de contacto y delegado de protección de datos si existe.
2. **Cronología del incidente**: fecha y hora de la brecha, de su detección y del conocimiento por el responsable, con el cómputo expreso del plazo de setenta y dos horas y su fecha límite.
3. **Naturaleza del incidente**: descripción de lo ocurrido, causa, si continúa activo, y si ha habido acceso, alteración, pérdida o divulgación de los datos.
4. **Datos y personas afectadas**: categorías y número aproximado de interesados y de registros afectados, con indicación de si hay categorías especiales o datos de menores.
5. **Consecuencias probables y medidas adoptadas**: riesgos para los derechos de los afectados, medidas de contención y de mitigación ya aplicadas, y medidas correctoras previstas.
6. **Comunicación a los interesados**: *Condicional riesgo alto:* redacción de la comunicación a los afectados en lenguaje claro, con la descripción del incidente, las posibles consecuencias, las medidas adoptadas y las recomendaciones concretas, y con el contacto para más información.
7. **Registro interno de la brecha**: constancia de la inscripción del incidente en el registro interno de violaciones de seguridad, obligatorio incluso cuando la brecha no sea notificable.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
La documentación de protección de datos ha sido generada y actualizada en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (tratamientos, bases de licitud o plazos de conservación).
2. Añadir un tratamiento o un proveedor adicional.
3. Preparar el documento complementario (del registro al contrato de encargado, o la comunicación a los interesados).
4. Revisar la coherencia global y realizar control de calidad previo a su aprobación.
5. Dar la documentación por finalizada y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el documento es un borrador preparatorio; debe ser revisado por un profesional antes de su aprobación y publicación.
2. **La ausencia del documento es la infracción:** no tener registro de actividades, o comunicar datos a un proveedor sin contrato de encargado, se sanciona por sí mismo, sin necesidad de que exista ningún incidente.
3. **Plazo de setenta y dos horas:** la notificación de una brecha a la autoridad debe hacerse sin dilación indebida y, a más tardar, en setenta y dos horas desde que el responsable tuvo conocimiento. Si se supera, hay que notificar igualmente y motivar el retraso.
4. **Documento vivo:** el registro debe actualizarse cuando cambien los tratamientos, y el protocolo de brechas exige un registro interno de todos los incidentes, notificables o no.
5. **Derechos de los interesados:** deben atenderse en el plazo de un mes, prorrogable de forma motivada. Conviene tener el procedimiento definido antes de recibir la primera solicitud.
6. **Delegado de protección de datos y evaluación de impacto:** su exigencia depende de la actividad y del tipo de tratamiento, no solo del tamaño de la empresa. Si concurre alguno de los supuestos legales, la designación es obligatoria y debe comunicarse a la autoridad.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar preceptos, plazos o importes de sanción. No afirmar que una obligación no aplica sin haber comprobado la actividad y el tipo de tratamiento.
2. **Cero Invención de Datos:** prohibido inventar finalidades, categorías de datos, proveedores, medidas de seguridad o cifras de afectados. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **No maquillar el cumplimiento:** está prohibido redactar un registro que declare medidas de seguridad o plazos que la empresa no aplica realmente. Documentar lo que no se cumple agrava la responsabilidad.
4. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas o guías de la autoridad en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
5. **Límites de Alcance:** no preparar defensa ante expedientes sancionadores, ni evaluaciones de impacto completas, ni instrumentos de transferencia internacional, que deben derivarse a especialista.
