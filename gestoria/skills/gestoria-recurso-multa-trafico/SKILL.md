---
name: gestoria-recurso-multa-trafico
description: >
  Prepara la defensa frente a una sancion de trafico en Espana conforme al **Real Decreto Legislativo
  6/2015**, texto refundido de la Ley sobre Trafico, Circulacion de Vehiculos a Motor y Seguridad
  Vial, que regula el procedimiento sancionador, la identificacion del conductor y el permiso por
  puntos, y a la **Ley 39/2015** del Procedimiento Administrativo Comun, que fija las reglas de
  notificacion, plazos y recursos.


  Genera tres documentos: el escrito de identificacion del conductor responsable cuando la denuncia se
  dirige al titular del vehiculo, el escrito de alegaciones dentro del procedimiento sancionador, y el
  recurso de reposicion contra la resolucion sancionadora ya dictada.


  Computa los plazos de veinte dias naturales para alegar y de un mes para recurrir, explica el efecto
  del pago con reduccion del cincuenta por ciento (que pone fin al procedimiento, impide alegar y no
  evita la perdida de puntos), revisa los defectos de notificacion y la validez de la notificacion
  electronica en la Direccion Electronica Vial, y comprueba la prescripcion de la infraccion y la
  caducidad del procedimiento.


  NO usar para el recurso contencioso-administrativo ante los tribunales, ni para infracciones penales
  contra la seguridad vial (conduccion sin permiso, alcoholemia penal, temeridad), ni para sanciones
  de otras administraciones distintas de trafico, ni para reclamar danos de un accidente.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Ley sobre Trafico y Seguridad Vial](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722) y
  [Ley 39/2015 del Procedimiento Administrativo Comun](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565).
when_to_use: |
  - Al usuario le ha llegado una multa de trafico y quiere alegar o recurrir.
  - Al usuario, como titular del vehiculo, le requieren que identifique quien conducia.
  - El usuario pregunta si le conviene pagar con el descuento del cincuenta por ciento o alegar.
  - El usuario pregunta si le van a quitar puntos y si el descuento se los devuelve.
  - El usuario cree que la multa esta mal notificada, prescrita o caducada.
  - El usuario ya recibio la resolucion sancionadora y quiere recurrirla en via administrativa.
inputs:
  - documento: identificacion del conductor / alegaciones / recurso de reposicion (V1)
  - fase_procedimiento: con reduccion vigente / procedimiento ordinario (V2)
  - tipo_infraccion: leve o grave sin puntos / grave con puntos / muy grave (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_interesado: nombre y apellidos, NIF/NIE, domicilio de notificaciones, telefono y correo
  - datos_expediente: numero de expediente, organismo sancionador y fecha de la denuncia
  - datos_vehiculo: matricula, marca y modelo, y condicion del interesado (titular, arrendatario o conductor)
  - datos_notificacion: fecha y forma de notificacion, y si esta dado de alta en la Direccion Electronica Vial
  - hechos_denunciados: precepto infringido, hecho denunciado, lugar, fecha y hora
  - importe_y_puntos: importe de la sancion, importe con reduccion y puntos a detraer
  - motivos_defensa: motivos de fondo y de forma en que se basa la defensa
  - prueba: documentos, fotografias, testigos o informes que se aportan
  - datos_conductor: identidad, NIF, domicilio y numero de permiso del conductor responsable
outputs:
  - escrito_identificacion_conductor: escrito de identificacion del conductor responsable, DRAFT
  - escrito_alegaciones: escrito de alegaciones en el procedimiento sancionador, DRAFT
  - recurso_reposicion: recurso de reposicion contra la resolucion sancionadora, DRAFT
  - checklist_plazos: computo de plazos de alegaciones, recurso, prescripcion y caducidad
references:
  - references/procedimiento-sancionador-trafico.md
  - references/notificaciones-prescripcion-y-puntos.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-identificacion-conductor.md
  - assets/template-escrito-alegaciones-multa.md
  - assets/template-recurso-reposicion-multa.md
---

# Defensa frente a una Sanción de Tráfico (Identificación, Alegaciones y Reposición)

> DRAFT — para revisión por un gestor o asesor colegiado antes de su presentación. No constituye asesoramiento profesional vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar su defensa frente a una sanción de tráfico.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `identificacion_conductor` | `alegaciones` | `recurso_reposicion` | `via_contenciosa`.
- **V2 (Fase del Procedimiento):** `con_reduccion_vigente` | `procedimiento_ordinario`.
- **V3 (Tipo de Infracción):** `leve_o_grave_sin_puntos` | `grave_con_puntos` | `muy_grave`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar en qué momento del procedimiento está el expediente y qué escrito procede.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un gestor administrativo (de usted), confirmando que vais a preparar la defensa frente a la sanción de tráfico y advirtiendo en una línea de que los plazos de este procedimiento son cortos y perentorios.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué escrito necesita, en qué fase está el expediente y si la infracción lleva pérdida de puntos, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), la fase (`V2`) o el tipo de infracción (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar que escrito procede segun el momento procedimental.",
      "question": "¿Qué le pide la Administración o qué necesita presentar?",
      "options": [
        {"id": "identificacion_conductor", "label": "Me requieren que identifique quién conducía el vehículo"},
        {"id": "alegaciones", "label": "Quiero alegar contra la denuncia, antes de que haya resolución"},
        {"id": "recurso_reposicion", "label": "Ya hay resolución sancionadora y quiero recurrirla"},
        {"id": "via_contenciosa", "label": "Ya agoté la vía administrativa y quiero ir a los tribunales"}
      ]
    },
    {
      "id": "fase_procedimiento",
      "rationale": "Resolver V2: el plazo de reduccion del 50% coexiste con el de alegaciones y son incompatibles.",
      "question": "¿Está todavía dentro del plazo de pago con reducción del cincuenta por ciento?",
      "options": [
        {"id": "con_reduccion_vigente", "label": "Sí, aún puedo pagar con el descuento"},
        {"id": "procedimiento_ordinario", "label": "No, ese plazo ya pasó o ya presenté alegaciones"}
      ]
    },
    {
      "id": "tipo_infraccion",
      "rationale": "Resolver V3 para advertir de la perdida de puntos y del plazo de prescripcion aplicable.",
      "question": "¿Qué tipo de infracción le imputan?",
      "options": [
        {"id": "leve_o_grave_sin_puntos", "label": "Leve o grave sin pérdida de puntos"},
        {"id": "grave_con_puntos", "label": "Grave con pérdida de puntos"},
        {"id": "muy_grave", "label": "Muy grave"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `fase_procedimiento`
- `V3` — `tipo_infraccion`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = via_contenciosa`:**
  - **DETENER.** Informar de que el recurso contencioso-administrativo exige demanda ante el juzgado competente, con plazo de dos meses desde la notificación del acto que agota la vía administrativa, y que su interposición requiere dirección letrada y representación en los términos de la ley procesal. Derivar a abogado. No crear documento.
- **Si `V1 = identificacion_conductor`:**
  - Escrito del sistema: `assets/template-identificacion-conductor.md`. Proceder a la **Fase 2**.
- **Si `V1 = alegaciones`:**
  - Escrito del sistema: `assets/template-escrito-alegaciones-multa.md`. Proceder a la **Fase 2**.
- **Si `V1 = recurso_reposicion`:**
  - Escrito del sistema: `assets/template-recurso-reposicion-multa.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina si hay que advertir de la incompatibilidad entre el pago con reducción y las alegaciones, y de la fecha límite de cada opción.
- `V3` no elige plantilla: determina la advertencia sobre pérdida de puntos y el plazo de prescripción de la infracción que se comunica.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `procedimiento-sancionador-trafico.md`, `notificaciones-prescripcion-y-puntos.md` y `estilo-redaccion-escritos.md`.
2. Opcionalmente verifica mediante `web_search` el organismo sancionador competente (Dirección General de Tráfico, servicio autonómico o ayuntamiento) y su sede electrónica, así como el cuadro de infracciones y puntos vigente. Aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal, Plazos y la Decisión Económica:**
   - Explicar con claridad la **disyuntiva inicial**: pagar con reducción del cincuenta por ciento en el plazo de veinte días naturales, lo que supone la terminación del procedimiento, la renuncia a formular alegaciones y la pérdida de la posibilidad de recurrir en vía administrativa; o bien alegar en ese mismo plazo, conservando la defensa pero perdiendo el descuento.
   - Advertir de que el pago con reducción **no evita la detracción de puntos** cuando la infracción los lleva aparejados.
   - Comunicar los plazos aplicables: veinte días naturales para alegaciones desde la notificación de la denuncia, un mes para el recurso de reposición desde la notificación de la resolución, y quince días naturales para identificar al conductor.
   - Explicar los plazos de prescripción de la infracción (tres meses para las leves, seis meses para las graves y muy graves) y la caducidad del procedimiento al año desde su inicio.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta el escrito **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que identifique correctamente el expediente y el órgano y que no formule pretensiones improcedentes en esa fase, advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `identificacion_conductor.md`, `escrito_alegaciones.md` o `recurso_reposicion.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa, incluida la fecha del sistema y el cómputo de las fechas límite. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta sección?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro administrativo (por ejemplo, *"Pasamos ahora a los motivos de fondo de su defensa"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Búsqueda prioritaria de partes e intervinientes (MANDATORIO con `search_clients` — MÁXIMA PRIORIDAD):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** antes de solicitar datos al usuario o llamar a formularios, conforme a la regla global `REG-CLI-01` de `CLAUDE.md`. Solo si `search_clients` devuelve 0 resultados o si tras recuperar la ficha faltan campos puntuales, invocarás `slot_filling_request` exclusivamente para los campos pendientes.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta sección?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** comprueba que la fecha de notificación es anterior a la de presentación, que el plazo no está vencido, que la matrícula tiene formato válido y que el motivo alegado es coherente con el hecho denunciado. Si el plazo ya ha vencido, **dilo con claridad antes de seguir redactando** y explica qué opciones quedan.

### Hoja de Ruta de Secciones — RAMA IDENTIFICACIÓN DEL CONDUCTOR:

1. **Interesado y expediente** *(confirmación agrupada)*: identidad y NIF del titular del vehículo, domicilio de notificaciones, número de expediente, organismo requirente y fecha de recepción del requerimiento.
2. **Vehículo y hecho denunciado**: matrícula, marca y modelo, y fecha, hora y lugar del hecho denunciado.
3. **Identificación del conductor** *(confirmación agrupada)*: nombre y apellidos, NIF/NIE, domicilio completo y número de permiso de conducir de la persona que conducía, con la advertencia de que los datos deben ser exactos y verificables.
4. **Supuestos especiales**: *Condicional imposibilidad de identificar:* exposición motivada y acreditada de la imposibilidad (vehículo sustraído con denuncia, vehículo cedido a empresa de alquiler con contrato, vehículo vendido con notificación de venta), con la documentación que lo acredite.
5. **Advertencia de consecuencias y cierre**: constancia de que la no identificación sin causa justificada constituye infracción muy grave con multa agravada, y solicitud de que se tenga por cumplido el deber de identificación.

### Hoja de Ruta de Secciones — RAMA ALEGACIONES:

1. **Interesado y expediente** *(confirmación agrupada)*: identidad y NIF, domicilio de notificaciones, correo y teléfono, número de expediente, organismo y fecha de notificación de la denuncia.
2. **Hecho denunciado y precepto**: transcripción del hecho denunciado, precepto que se dice infringido, importe y puntos, y fecha, hora y lugar.
3. **Motivos de forma**: examen de los defectos del expediente, en particular la falta de datos esenciales en la denuncia, la ausencia de identificación del agente denunciante, los defectos de notificación, la falta de acreditación de la verificación del cinemómetro y su margen de error, y la ausencia de señalización.
4. **Motivos de fondo**: relato de lo realmente ocurrido, con la prueba que lo acredita, y desvirtuación de la presunción de veracidad de la denuncia del agente.
5. **Prescripción y caducidad**: cómputo expreso desde la fecha de la infracción y desde la fecha de inicio del procedimiento, con invocación de la prescripción o de la caducidad si concurren.
6. **Proposición de prueba y solicitud**: relación de documentos que se aportan, proposición de prueba (fotografías, informes, testigos, solicitud de expediente completo) y petición de archivo del expediente o, subsidiariamente, de reducción de la sanción.

### Hoja de Ruta de Secciones — RAMA RECURSO DE REPOSICIÓN:

1. **Interesado, órgano y resolución impugnada** *(confirmación agrupada)*: identidad y NIF, domicilio, órgano que dictó la resolución, número de expediente, fecha de la resolución y fecha de su notificación.
2. **Cumplimiento del plazo**: cómputo expreso del plazo de un mes desde la notificación, con la fecha límite y la constancia de que el recurso se presenta en plazo.
3. **Antecedentes del expediente**: cronología de la denuncia, de las alegaciones presentadas y de la resolución, con indicación de si las alegaciones fueron respondidas.
4. **Motivos del recurso**: falta de motivación de la resolución, ausencia de respuesta a las alegaciones formuladas, defectos de notificación, insuficiencia de la prueba de cargo, prescripción de la infracción o caducidad del procedimiento.
5. **Suspensión y solicitud**: petición de suspensión de la ejecución si se solicita, y súplica de anulación de la resolución con archivo del expediente y de devolución de lo indebidamente ingresado si ya se pagó.
6. **Advertencias de cierre**: constancia de que el recurso de reposición es potestativo, que su resolución agota la vía administrativa, y que contra ella cabe recurso contencioso-administrativo en el plazo de dos meses.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
El escrito ha sido generado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (motivos, prueba o cómputo de plazos).
2. Añadir un motivo adicional de defensa.
3. Preparar el escrito siguiente del procedimiento.
4. Revisar la coherencia global y realizar control de calidad previo a la presentación.
5. Dar el escrito por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el escrito es un borrador preparatorio; debe ser revisado por un gestor administrativo o letrado antes de su presentación.
2. **Plazos perentorios:** veinte días naturales para alegaciones y para el pago con reducción, quince días naturales para identificar al conductor, un mes para el recurso de reposición y dos meses para el recurso contencioso-administrativo. Vencidos, la sanción deviene firme y ejecutable, con apremio del veinte por ciento.
3. **La disyuntiva del descuento:** pagar con reducción del cincuenta por ciento implica renunciar a alegar y a recurrir en vía administrativa, y **no** evita la pérdida de puntos. Alegar conserva la defensa pero pierde el descuento. La decisión es del cliente y debe quedar informada.
4. **Deber de identificación:** no identificar al conductor sin causa justificada constituye infracción muy grave, sancionada con multa del doble o del triple de la original según la gravedad de la infracción originaria. Es habitualmente peor que la multa inicial.
5. **Notificación electrónica:** quienes están dados de alta en la Dirección Electrónica Vial reciben las notificaciones por ese medio, y el plazo corre desde su puesta a disposición aunque no se abra. Conviene revisarla periódicamente.
6. **Presentación:** por registro electrónico del organismo sancionador, en registro presencial o por cualquiera de los medios admitidos por la ley del procedimiento administrativo. Conservar siempre el justificante con su fecha.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar plazos, cuantías o puntos. No inventar el cuadro de infracciones ni el número de puntos de una conducta concreta: si no está confirmado, dejarlo como dato pendiente.
2. **Cero Invención de Datos:** prohibido inventar números de expediente, matrículas, identidades de conductores, números de permiso o datos del agente denunciante. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Prohibición de identificación falsa:** está terminantemente prohibido ayudar a identificar como conductor a una persona que no lo era. Es una conducta que puede constituir infracción muy grave y, en su caso, delito. Si el usuario lo plantea, negarse y advertirlo con claridad.
4. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
5. **Límites de Alcance:** no preparar recursos contencioso-administrativos, ni la defensa de delitos contra la seguridad vial, ni reclamaciones de daños derivadas de accidente, que deben derivarse a letrado.
