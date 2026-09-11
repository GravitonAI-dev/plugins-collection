---
name: derecho-mercantil-juntas-y-acuerdos-sociales
description: >
  Genera los documentos de la vida societaria ordinaria de una sociedad limitada espanola conforme al
  **Real Decreto Legislativo 1/2010**, texto refundido de la Ley de Sociedades de Capital (LSC), que
  regula la junta general, su convocatoria, las mayorias y el acta, y al **Real Decreto 1784/1996**,
  Reglamento del Registro Mercantil, que fija los requisitos de la certificacion y elevacion a publico
  de los acuerdos.


  Genera tres documentos: el anuncio o comunicacion de convocatoria de junta general con su orden del
  dia, el acta de la junta (universal u ordinaria convocada) con los acuerdos adoptados y sus
  mayorias, y la certificacion de acuerdos sociales expedida por el organo de administracion para su
  elevacion a publico o inscripcion.


  Calcula y comunica los plazos de convocatoria y de aprobacion y deposito de cuentas, aplica las
  mayorias reforzadas de los Arts. 199 y 201 LSC, y advierte del conflicto de interes del Art. 190
  LSC.


  NO usar para la impugnacion de acuerdos sociales ni para acciones de responsabilidad contra
  administradores, para sociedades anonimas cotizadas, ni para modificaciones estructurales como
  fusion o escision.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Ley de Sociedades de Capital](https://www.boe.es/buscar/act.php?id=BOE-A-2010-10544) y
  [Reglamento del Registro Mercantil](https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533).
when_to_use: |
  - El usuario tiene que convocar una junta general y necesita el anuncio o la comunicacion con su orden del dia.
  - El usuario ha celebrado una junta y necesita redactar el acta con los acuerdos adoptados.
  - El usuario necesita una certificacion de acuerdos para el notario, el banco o el Registro Mercantil.
  - El usuario va a aprobar las cuentas anuales y pregunta por plazos y por el deposito registral.
  - El usuario va a cesar o nombrar administrador y pregunta como documentarlo.
  - El usuario pregunta que mayoria hace falta para un acuerdo concreto o si puede celebrar junta universal.
inputs:
  - documento: convocatoria / acta de junta / certificacion de acuerdos (V1)
  - tipo_junta: universal / convocada (V2)
  - naturaleza_acuerdo: aprobacion de cuentas / modificacion de estatutos / cambio de administrador / otros acuerdos (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_sociedad: denominacion, domicilio, CIF y datos registrales
  - datos_socios: identidad de los socios, participaciones y porcentaje de cada uno
  - organo_administracion: composicion actual del organo y identidad de quien convoca o certifica
  - fecha_hora_lugar: fecha, hora y lugar de celebracion de la junta y, en su caso, segunda convocatoria
  - orden_del_dia: puntos del orden del dia en su redaccion definitiva
  - acuerdos_adoptados: texto de cada acuerdo, votos a favor, en contra y abstenciones
  - datos_cuentas: ejercicio, fecha de cierre, resultado y propuesta de aplicacion
  - datos_administrador: identidad, NIF, domicilio y cargo del administrador nombrado o cesado
outputs:
  - convocatoria_junta: anuncio o comunicacion individual de convocatoria con orden del dia, DRAFT
  - acta_junta_general: acta de la junta general con asistentes, acuerdos y mayorias, DRAFT
  - certificacion_acuerdos: certificacion de acuerdos sociales firmada por el organo de administracion, DRAFT
  - calendario_plazos: computo de los plazos de convocatoria, aprobacion y deposito de cuentas
references:
  - references/lsc-junta-general-y-acuerdos.md
  - references/rrm-certificacion-y-deposito-cuentas.md
  - references/estilo-redaccion-societaria.md
assets:
  - assets/template-convocatoria-junta-general.md
  - assets/template-acta-junta-general.md
  - assets/template-certificacion-acuerdos.md
---

# Convocatoria, Acta y Certificación de Acuerdos de la Junta General

> DRAFT — para revisión por un abogado mercantilista o notario antes de su firma, elevación a público o inscripción. No constituye asesoramiento jurídico vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva y rigurosa a través de un procedimiento estructurado en 5 fases secuenciales para documentar la junta general y sus acuerdos.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `convocatoria_junta` | `acta_junta` | `certificacion_acuerdos` | `impugnacion_acuerdos`.
- **V2 (Tipo de Junta):** `universal` | `convocada`.
- **V3 (Naturaleza del Acuerdo):** `aprobacion_cuentas` | `modificacion_estatutos` | `cambio_administrador` | `otros_acuerdos`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar qué documento societario se prepara y en qué acuerdo se sustenta.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un abogado mercantilista (de usted), confirmando que vais a preparar la documentación de la junta general de su sociedad.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué documento necesita, si la junta es universal o convocada y qué se va a acordar, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`), el tipo de junta (`V2`) o la naturaleza del acuerdo (`V3`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar cual de los tres documentos societarios se prepara.",
      "question": "¿Qué documento necesita preparar?",
      "options": [
        {"id": "convocatoria_junta", "label": "Convocatoria de la junta general con su orden del día"},
        {"id": "acta_junta", "label": "Acta de la junta ya celebrada"},
        {"id": "certificacion_acuerdos", "label": "Certificación de acuerdos para notaría, banco o Registro Mercantil"},
        {"id": "impugnacion_acuerdos", "label": "Impugnar un acuerdo social ya adoptado o exigir responsabilidad al administrador"}
      ]
    },
    {
      "id": "tipo_junta",
      "rationale": "Resolver V2: la junta universal no requiere convocatoria previa y su acta tiene formalidades propias.",
      "question": "¿La junta se celebra o se celebró como junta universal, con todo el capital presente y aceptando el orden del día, o mediante convocatoria previa?",
      "options": [
        {"id": "universal", "label": "Junta universal (todo el capital presente y de acuerdo)"},
        {"id": "convocada", "label": "Junta convocada previamente por el órgano de administración"}
      ]
    },
    {
      "id": "naturaleza_acuerdo",
      "rationale": "Resolver V3 para aplicar la mayoria exigible y las advertencias de forma publica e inscripcion.",
      "question": "¿Cuál es el acuerdo principal que se va a adoptar o que se adoptó?",
      "options": [
        {"id": "aprobacion_cuentas", "label": "Aprobación de cuentas anuales y aplicación del resultado"},
        {"id": "modificacion_estatutos", "label": "Modificación de estatutos, aumento o reducción de capital, o cambio de domicilio o de objeto"},
        {"id": "cambio_administrador", "label": "Nombramiento, cese o reelección de administrador"},
        {"id": "otros_acuerdos", "label": "Otros acuerdos de gestión ordinaria"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `tipo_junta`
- `V3` — `naturaleza_acuerdo`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = impugnacion_acuerdos`:**
  - **DETENER.** Informar de que la impugnación de acuerdos sociales y la acción de responsabilidad contra administradores son actuaciones contenciosas con plazos de caducidad breves y legitimación tasada, que exigen dirección letrada y quedan fuera del alcance de esta skill. Derivar a abogado de litigación societaria. No crear documento.
- **Si `V1 = convocatoria_junta`:**
  - Plantilla del sistema: `assets/template-convocatoria-junta-general.md`. Proceder a la **Fase 2**.
- **Si `V1 = acta_junta`:**
  - Plantilla del sistema: `assets/template-acta-junta-general.md`. Proceder a la **Fase 2**.
- **Si `V1 = certificacion_acuerdos`:**
  - Plantilla del sistema: `assets/template-certificacion-acuerdos.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina si se suprime el bloque de convocatoria y se incorpora la fórmula de aceptación unánime del orden del día propia de la junta universal.
- `V3` no elige plantilla: determina la mayoría que debe consignarse, si el acuerdo exige escritura pública e inscripción, y si procede el aviso de depósito de cuentas.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `lsc-junta-general-y-acuerdos.md`, `rrm-certificacion-y-deposito-cuentas.md` y `estilo-redaccion-societaria.md`.
2. Opcionalmente verifica mediante `web_search` los plazos y formularios vigentes de depósito de cuentas en el Registro Mercantil. Aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Plazos Aplicables:**
   - Para la convocatoria: plazo mínimo de quince días de antelación en la sociedad limitada, computados desde la remisión de la comunicación al último de los socios cuando la forma sea comunicación individual, y contenido mínimo obligatorio del anuncio.
   - Para el acta: obligación de recoger asistentes, capital presente, orden del día, resultado de las votaciones con expresión del capital que votó a favor, y aprobación del acta; y necesidad de transcribirla al libro de actas.
   - Para la certificación: quién puede certificar y con qué cargo vigente e inscrito, y su función de título para la elevación a público o para la inscripción.
   - Si el acuerdo es de aprobación de cuentas: junta dentro de los seis primeros meses del ejercicio y depósito en el Registro Mercantil dentro del mes siguiente a la aprobación.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Nombrar por su ruta la plantilla **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

### 2.3 Fijación del origen de la plantilla y manejo de la elección
- **Si `origen_plantilla = plantilla_sistema`:** utiliza el asset enrutado y avanza a la **Fase 3**.
- **Si `origen_plantilla = plantilla_usuario`:** toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, verifica que no omita menciones cuya ausencia impide la inscripción (identidad de quien convoca, orden del día, capital concurrente, mayorías, cargo vigente del certificante), advierte en el chat y propón la redacción válida, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en el workspace del usuario, con el nombre `convocatoria_junta_general.md`, `acta_junta_general.md` o `certificacion_acuerdos.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos de la clasificación y de la escucha activa, incluida la fecha del sistema cuando proceda. Todos los datos pendientes permanecen como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves. PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):** ejecuta `read_file` sobre el archivo creado para confirmar su integridad.
3. **Confirmación en Chat:** informa al usuario de la ruta del archivo generado e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Anuncio de la sección + Pregunta] --> [Vista Previa en texto plano] --> [¿Confirmamos esta sección?] --> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Anuncio y Pregunta en Chat:** anuncia la sección sustantiva con una frase breve en registro jurídico-mercantil (por ejemplo, *"Pasamos ahora a consignar el resultado de las votaciones"*) y, en el mismo mensaje, formula ya la primera pregunta. No pidas permiso para pasar de sección: informa y continúa.
2. **Búsqueda prioritaria de partes e intervinientes y Regla de Cero Redundancia (`search_clients` / `get_client` — REG-CLI-01 y REG-CLI-02):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** conforme a `REG-CLI-01` de `CLAUDE.md`. Si los datos de una persona ya fueron obtenidos mediante `search_clients` o `get_client`, **queda TERMINANTEMENTE PROHIBIDO volver a pedir dicha información** (nombre, DNI/NIE/CIF, domicilio, contacto, etc.), ya sea en el chat o en `slot_filling_request` (`REG-CLI-02`). Si todos los datos requeridos constan en la ficha del cliente, **NO invoques `slot_filling_request`**: redacta directamente la cláusula, muestra la vista previa en texto plano en el chat y pide confirmación. Solo si faltan campos específicos ausentes en la ficha, invocarás `slot_filling_request` exclusivamente para los datos pendientes.
   - **Datos estructurados no de cliente agrupados (`slot_filling_request`, MANDATORIO):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
3. **Vista Previa (Preview):** muestra el texto redactado en texto plano, sin backticks de código.
4. **Confirmación:** pregunta literalmente: `¿Confirmamos esta sección?`.
5. **Persistencia en Disco:** tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.
6. **Validación de sentido, no solo de formato:** comprueba que el capital concurrente no excede del capital social, que la mayoría consignada alcanza la exigible para el acuerdo, que la fecha de la junta es posterior a la de la convocatoria y respeta la antelación mínima, y que la aplicación del resultado cuadra con el resultado del ejercicio. Si algo no encaja, dialoga en el chat, señala el motivo y pide aclaración antes de volcarlo.

### Hoja de Ruta de Secciones — RAMA CONVOCATORIA:

1. **Sociedad y órgano convocante** *(confirmación agrupada)*: denominación, domicilio, CIF y datos registrales; identidad y cargo de quien convoca, con constancia de que su cargo está vigente.
2. **Fecha, hora, lugar y forma de comunicación**: fecha y hora de la reunión, lugar de celebración o régimen de asistencia telemática, y forma de comunicación conforme a los estatutos, con el cómputo expreso de la antelación mínima de quince días.
3. **Orden del día**: redacción de cada punto con claridad y sin ambigüedad, separando los asuntos que exigen mayoría reforzada. Advertir de que no pueden adoptarse acuerdos sobre asuntos no incluidos, salvo las excepciones legales como el cese de administradores.
4. **Derechos de información de los socios**: mención del derecho a obtener los documentos que se someten a aprobación, y en la aprobación de cuentas, del derecho a obtener las cuentas anuales de forma inmediata y gratuita.
5. **Menciones adicionales según el acuerdo**: *Condicional `V3 = modificacion_estatutos`:* expresión del derecho a examinar el texto íntegro de la modificación propuesta y a pedir su entrega o envío gratuito.

### Hoja de Ruta de Secciones — RAMA ACTA DE JUNTA:

1. **Encabezamiento y datos de la reunión** *(confirmación agrupada)*: denominación, domicilio, fecha, hora y lugar de celebración, y constitución de la mesa con presidente y secretario.
2. **Válida constitución**: *Condicional `V2 = universal`:* constancia de que está presente o representado todo el capital y de que los concurrentes aceptaron por unanimidad la celebración y el orden del día, con firma de la lista de asistentes. *Condicional `V2 = convocada`:* referencia a la convocatoria, su fecha y forma, y capital concurrente presente y representado con su porcentaje.
3. **Lista de asistentes y capital concurrente**: relación de socios asistentes, participaciones de cada uno y porcentaje sobre el capital.
4. **Deliberación y acuerdos por punto del orden del día**: para cada punto, texto literal del acuerdo sometido a votación y resultado con votos a favor, en contra y abstenciones, expresados en participaciones y en porcentaje. Consignar la mayoría exigible aplicada. *Condicional conflicto de interés:* constancia de la abstención del socio afectado y del capital deducido para el cómputo.
5. **Acuerdos según naturaleza**: *Condicional `V3 = aprobacion_cuentas`:* aprobación de las cuentas del ejercicio con sus cifras y acuerdo de aplicación del resultado. *Condicional `V3 = cambio_administrador`:* cese con efectos, nombramiento, identidad completa del nombrado, duración y aceptación del cargo. *Condicional `V3 = modificacion_estatutos`:* texto literal del artículo o artículos en su nueva redacción.
6. **Aprobación del acta, cierre y firmas**: forma de aprobación del acta, hora de cierre, y firma del presidente y del secretario, con la constancia de la transcripción al libro de actas.

### Hoja de Ruta de Secciones — RAMA CERTIFICACIÓN DE ACUERDOS:

1. **Certificante y acreditación de su cargo** *(confirmación agrupada)*: identidad, NIF, cargo, fecha de su nombramiento y datos de su inscripción en el Registro Mercantil.
2. **Identificación de la junta certificada**: carácter universal o convocada, fecha, lugar y capital concurrente.
3. **Transcripción de los acuerdos**: texto literal de los acuerdos que se certifican, con su mayoría, evitando resúmenes o paráfrasis.
4. **Finalidad y advertencias**: destino de la certificación (elevación a público, inscripción, entidad bancaria o Administración) y, cuando el acuerdo lo exija, advertencia de que la eficacia frente a terceros requiere escritura pública e inscripción registral.
5. **Fecha, lugar y firma**: firma del certificante y, cuando los estatutos o el Reglamento del Registro Mercantil lo exijan, visto bueno del presidente o del administrador con cargo vigente.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones, presenta al usuario el menú interactivo:
```markdown
El documento societario ha sido generado y actualizado en el editor.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (orden del día, asistentes, acuerdos o mayorías).
2. Añadir un punto adicional al orden del día o un acuerdo adicional.
3. Preparar el documento complementario (del acta a la certificación, o de la convocatoria al acta).
4. Revisar la coherencia global y realizar control de calidad previo a la firma o a la notaría.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
1. **Carácter DRAFT:** el documento es un borrador preparatorio; debe ser revisado por un abogado mercantilista y, cuando proceda, por el notario autorizante.
2. **Libro de actas:** el acta debe transcribirse al libro de actas de la sociedad, que se legaliza en el Registro Mercantil. Sin esa transcripción, la prueba del acuerdo se debilita.
3. **Acuerdos que exigen forma pública e inscripción:** la modificación de estatutos, el aumento y la reducción de capital y el cambio de órgano de administración requieren escritura pública e inscripción en el Registro Mercantil para desplegar plenos efectos frente a terceros.
4. **Cuentas anuales:** la junta ordinaria debe celebrarse dentro de los seis primeros meses del ejercicio siguiente al que se aprueba, y las cuentas deben depositarse en el Registro Mercantil dentro del mes siguiente a su aprobación. El incumplimiento del depósito puede dar lugar a cierre registral y a sanción.
5. **Plazos de impugnación:** los acuerdos sociales son impugnables en plazos breves de caducidad. Si algún socio anuncia su oposición, conviene asesoramiento inmediato.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** consultar las referencias antes de citar preceptos, mayorías o plazos. No consignar mayorías inventadas ni aplicar a la limitada las reglas de quórum propias de la anónima, que no existen en la limitada.
2. **Cero Invención de Datos:** prohibido inventar denominaciones, CIF, datos registrales, porcentajes de capital, resultados contables o fechas de nombramiento. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** no preparar impugnaciones de acuerdos, acciones de responsabilidad, juntas de sociedades cotizadas ni modificaciones estructurales, que deben derivarse a profesional colegiado.
