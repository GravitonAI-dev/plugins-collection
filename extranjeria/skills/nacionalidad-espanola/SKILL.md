---
name: nacionalidad-espanola
description: >
  Prepara el expediente de solicitud de nacionalidad española por residencia y sus escritos asociados:
  la hoja de datos de la solicitud, el escrito motivado que acredita el arraigo y la buena conducta
  cívica, el checklist documental completo con su régimen de legalización y traducción, el escrito de
  subsanación cuando el Registro requiere documentación, y el escrito de alegaciones frente a la
  propuesta de resolución desestimatoria. Aplica el Código Civil en materia de adquisición de la
  nacionalidad y su normativa de desarrollo procedimental, en sus versiones consolidadas vigentes
  verificadas en el BOE. Determina el plazo de residencia legal exigible según la nacionalidad de
  origen y la situación personal, comprueba las pruebas obligatorias y sus exenciones, y comunica el
  plazo de resolución, el efecto del silencio y el plazo para jurar tras la concesión. NO usar para la
  nacionalidad por opción, por carta de naturaleza ni por posesión de estado, ni para la recuperación
  de la nacionalidad, que tienen cauces propios.
when_to_use: |
  - El usuario quiere solicitar la nacionalidad española por residencia y necesita preparar el expediente.
  - El usuario pregunta cuántos años de residencia necesita según su nacionalidad de origen o su situación.
  - El usuario quiere saber qué documentos necesita, cuáles hay que apostillar y cuáles traducir.
  - El usuario ha recibido un requerimiento de subsanación del Registro Civil y necesita contestarlo.
  - El usuario ha recibido una propuesta de resolución desestimatoria y quiere alegar.
  - El usuario pregunta por las pruebas CCSE y DELE, por sus exenciones o por el juramento posterior.
  - El usuario pregunta cuánto tarda el expediente y qué ocurre si no le contestan.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - tipo_documento: hoja de datos de la solicitud / escrito motivado de solicitud / checklist documental / escrito de subsanación / alegaciones a propuesta desestimatoria
  - via_plazo: por qué vía se computa el plazo de residencia exigible
  - situacion_pruebas: pruebas superadas, pendientes o exentas
  - estado_expediente: no presentado / presentado y en tramitación / con requerimiento de subsanación / con propuesta desestimatoria
  - datos_solicitante: nombre y apellidos como constan en el pasaporte, NIE, nacionalidad, fecha y lugar de nacimiento, domicilio y estado civil
  - datos_filiacion: nombre y apellidos del padre y de la madre, con su fecha y lugar de nacimiento
  - historial_residencia: fecha de entrada en España, autorizaciones sucesivas y periodos de ausencia del territorio
  - documentacion_disponible: documentos de que ya dispone y su estado de legalización y traducción
outputs:
  - expediente_nacionalidad: documento completo en markdown, DRAFT, con la relación documental numerada y el régimen de legalización de cada documento extranjero
references:
  - references/fuentes-plantillas-validadas.md
  - references/plazos-de-residencia-y-computo.md
  - references/pruebas-ccse-y-dele.md
  - references/documentacion-legalizacion-y-traduccion.md
  - references/tramitacion-plazos-y-recursos.md
assets:
  - assets/template-hoja-datos-solicitud-nacionalidad.md
  - assets/template-escrito-motivado-nacionalidad.md
  - assets/checklist-documentacion-nacionalidad.md
  - assets/template-escrito-subsanacion.md
  - assets/template-alegaciones-propuesta-desestimatoria.md
---

# Preparar el Expediente de Nacionalidad Española por Residencia

> DRAFT — para revisión por un abogado colegiado antes de su presentación. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

- **V1 (Tipo de documento):** `hoja_datos` | `escrito_motivado` | `checklist` | `subsanacion` | `alegaciones`.
- **V2 (Vía de cómputo del plazo):** `general_diez` | `reducido_dos` | `reducido_uno` | `refugiado_cinco` | `no_lo_se`.
- **V3 (Situación de las pruebas):** `superadas` | `pendientes` | `exento`.
- **V4 (Estado del expediente):** `no_presentado` | `en_tramitacion` | `requerimiento_subsanacion` | `propuesta_desestimatoria`.
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos en el chat visible al usuario.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

### 1.1 Escucha Activa Previa

Antes de invocar el formulario, extrae del mensaje del usuario todo dato que ya conste: su nacionalidad de origen, cuánto tiempo lleva en España, si está casado con española o español, si nació aquí, si tiene hijos españoles, si ha hecho ya los exámenes y en qué punto está el expediente.

**Dos datos gobiernan todo lo demás y conviene captarlos de entrada:** la **nacionalidad de origen**, que determina el plazo de residencia exigible, y la **continuidad de la residencia legal**, que es el requisito que más denegaciones produce.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)

Invoca la herramienta con las opciones de triaje:

```json
{
  "form_data": [
    {
      "id": "tipo_documento",
      "rationale": "Resolver V1: cada momento del expediente tiene su propio documento, su propio destinatario y su propio plazo.",
      "question": "¿Qué documento necesita preparar?",
      "options": [
        {"id": "hoja_datos", "label": "La hoja de datos de la solicitud"},
        {"id": "escrito_motivado", "label": "El escrito motivado que acompaña a la solicitud"},
        {"id": "checklist", "label": "El checklist de la documentación que debe reunir"},
        {"id": "subsanacion", "label": "La contestación a un requerimiento de subsanación"},
        {"id": "alegaciones", "label": "Las alegaciones frente a una propuesta desestimatoria"}
      ]
    },
    {
      "id": "via_plazo",
      "rationale": "Resolver V2: el plazo de residencia legal exigible varía radicalmente según la nacionalidad de origen y la situación personal, y de él depende que la solicitud sea siquiera admisible.",
      "question": "¿Por qué vía le corresponde el plazo de residencia?",
      "options": [
        {"id": "reducido_uno", "label": "Nací en España, o estoy casado con española o español, o soy hijo o nieto de española o español"},
        {"id": "reducido_dos", "label": "Soy de un país iberoamericano, Andorra, Filipinas, Guinea Ecuatorial o Portugal, o soy de origen sefardí"},
        {"id": "refugiado_cinco", "label": "Tengo reconocida la condición de refugiado"},
        {"id": "general_diez", "label": "Ninguno de los casos anteriores"},
        {"id": "no_lo_se", "label": "No lo sé: verifíquelo usted"}
      ]
    },
    {
      "id": "situacion_pruebas",
      "rationale": "Resolver V3: sin las pruebas superadas o acreditada la exención, el expediente no prospera, y conviene saberlo antes de reunir el resto de la documentación.",
      "question": "¿En qué situación están las pruebas de integración?",
      "options": [
        {"id": "superadas", "label": "Ya las he superado"},
        {"id": "pendientes", "label": "Todavía no las he hecho"},
        {"id": "exento", "label": "Estoy exento o exenta"}
      ]
    },
    {
      "id": "estado_expediente",
      "rationale": "Resolver V4: el documento que procede y el plazo aplicable dependen del punto en que se encuentre el expediente.",
      "question": "¿En qué punto está su expediente?",
      "options": [
        {"id": "no_presentado", "label": "Todavía no lo he presentado"},
        {"id": "en_tramitacion", "label": "Presentado y en tramitación"},
        {"id": "requerimiento_subsanacion", "label": "He recibido un requerimiento de subsanación"},
        {"id": "propuesta_desestimatoria", "label": "He recibido una propuesta de resolución desestimatoria"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_documento`
- `V2` — `via_plazo`
- `V3` — `situacion_pruebas`
- `V4` — `estado_expediente`

### 1.3 Control de Requisitos y Enrutamiento (PRIMERA ACCIÓN OBLIGATORIA)

**Comprobación 1 — Plazo de residencia legal exigible.** Es el requisito que decide la admisibilidad.

* **Si `[V2 = no_lo_se]` → resuélvelo tú** antes de continuar: pregunta la nacionalidad de origen, el lugar de nacimiento, el estado civil y la filiación, y determina la vía aplicable sobre `references/plazos-de-residencia-y-computo.md`, **verificando el precepto vigente con `web_search`**. Informa del resultado en el chat con la cita y el enlace consultado.
* **Advertencia obligatoria en todas las vías:** el plazo se cuenta sobre **residencia legal, continuada e inmediatamente anterior** a la solicitud. Explica qué rompe la continuidad y por qué las ausencias del territorio son la causa más frecuente de denegación. Pide el historial de ausencias antes de dar por cumplido el plazo.

**Comprobación 2 — Pruebas de integración.**

* **Si `[V3 = pendientes]` → advertencia previa:** sin las pruebas superadas la solicitud no prospera. Explica cuáles son, quién las convoca y que sus certificados tienen su propia vigencia. Ofrece preparar el checklist documental mientras tanto, y **no** presentar la solicitud sin ellas.
* **Si `[V3 = exento]` → verifica la exención**, que depende de la nacionalidad, de la edad o de la capacidad, y **exige acreditarla documentalmente**. No des por buena una exención afirmada sin documento.

**Comprobación 3 — Cómputo y comunicación de plazos.** Comunica en el chat, antes de redactar: el plazo de resolución del expediente, el efecto del silencio transcurrido ese plazo, y —si ya hay concesión— el plazo para jurar o prometer, cuyo transcurso sin comparecer tiene consecuencias. **Verifica cada plazo en el texto vigente: no los cites de memoria.**

**Comprobación 4 — Enrutamiento:**
* **Si `[V1 = hoja_datos]` → Plantilla: `assets/template-hoja-datos-solicitud-nacionalidad.md`.**
* **Si `[V1 = escrito_motivado]` → Plantilla: `assets/template-escrito-motivado-nacionalidad.md`.**
* **Si `[V1 = checklist]` → Asset: `assets/checklist-documentacion-nacionalidad.md`,** ajustado a la vía de `V2`.
* **Si `[V1 = subsanacion]` → Plantilla: `assets/template-escrito-subsanacion.md`.** Pide el requerimiento recibido y su fecha de notificación **antes** de redactar: el plazo corre desde ella y es breve.
* **Si `[V1 = alegaciones]` → Plantilla: `assets/template-alegaciones-propuesta-desestimatoria.md`.** Pide la propuesta recibida y su fecha de notificación antes de redactar.
* **Si `[V1 = subsanacion]` y `[V4 = no_presentado o en_tramitacion]` → DETENER esa pretensión concreta:** no hay requerimiento que contestar. Reconduce al documento que corresponda al estado real del expediente.
* **Si `[V1 = alegaciones]` y `[V4 = no_presentado, en_tramitacion o requerimiento_subsanacion]` → DETENER esa pretensión concreta:** no hay propuesta desestimatoria que alegar. Reconduce.
* **Si `[V4 = requerimiento_subsanacion o propuesta_desestimatoria]` → alerta de plazo destacada** al inicio de la respuesta, antes que ninguna otra cosa, con la fecha límite calculada.
* **Si lo que se pretende es la nacionalidad por opción, por carta de naturaleza, por posesión de estado o la recuperación de la nacionalidad → DETENER**: cauces propios, fuera del alcance de esta skill. Explicar la diferencia y derivar.
* **Si la persona está en situación irregular → DETENER esa pretensión:** la nacionalidad por residencia exige residencia legal. Explicarlo y derivar a `extranjeria-residencia`, que prepara la autorización de residencia, indicando que la nacionalidad es un paso posterior.
* **Si consta un expediente de expulsión o una denegación de entrada → DETENER** y derivar a letrado con urgencia, advirtiendo del plazo.

### 1.4 Validación de presupuestos (interno, antes de la Fase 3)

- **Coincidencia exacta de nombres.** El nombre y los apellidos deben coincidir con el pasaporte y con la certificación de nacimiento. Cualquier discrepancia, incluidos los acentos y el orden de los apellidos, genera requerimiento. Comprobarlo y advertirlo.
- **Vigencia de los documentos.** Las certificaciones registrales extranjeras y los certificados de antecedentes penales tienen vigencia limitada. Comprobar que no caducarán antes de la presentación.
- **Legalización y traducción.** Todo documento público extranjero exige apostilla o legalización y traducción jurada, salvo exención por convenio. Es la causa más frecuente de subsanación.
- **Continuidad de la residencia.** Recabar el historial completo de autorizaciones y de ausencias antes de afirmar que el plazo se cumple.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

### 2.1 Verificación Normativa Interna
1. Consulta las referencias cargadas en tu contexto.
2. Verifica con `web_search` la versión consolidada vigente en el BOE de los preceptos del Código Civil sobre adquisición de la nacionalidad y de su normativa de desarrollo procedimental.
3. **Comprueba si existen instrucciones posteriores** de la Dirección General competente o de la Secretaría de Estado de Migraciones: en esta materia la instrucción fija el criterio con el que se resuelve.
4. Verifica el importe vigente de la tasa, la denominación y el código del modelo, y las pruebas exigidas con su régimen de exenciones. **No los cites de memoria.**
5. **Si detectas una versión posterior a la registrada, aplica la redacción vigente al documento que redactas en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje formal que contenga:
1. **Vía y plazo de residencia** que le corresponde, con el precepto verificado.
2. **Requisitos que faltan**, si los hay, y en qué orden conviene resolverlos.
3. **Plazo de resolución y efecto del silencio**, y el plazo para jurar tras la concesión.
4. **Documentos extranjeros** que necesitarán apostilla y traducción jurada, dicho de antemano.
5. **Propuesta de plantilla oficial del sistema que ha resuelto el enrutamiento de la Fase 1.3.** Nombrala por su ruta; si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada.**
6. **Pregunta explícita al usuario:**
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación del origen de la plantilla
* **Si `[origen_plantilla = plantilla_sistema]`:** toma el asset íntegro y procede a la **Fase 3**.
* **Si `[origen_plantilla = plantilla_usuario]`:** accede al adjunto y verifica que identifique correctamente al solicitante conforme al pasaporte, exprese la vía y el plazo alegados y relacione los documentos. Si falta alguno de esos elementos, adviértelo y propón la redacción que lo subsana.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura (`create_file`):** vuelca íntegramente la plantilla acordada en el workspace con nombre en `snake_case.md`, aplicando **Zero-Omission**: sustituye los datos ya conocidos y deja los pendientes como marcadores en mayúsculas entre dobles llaves. PROHIBIDO dejar archivos en blanco, con títulos solos o con resúmenes.
2. **Validación (`read_file`):** comprueba el volcado íntegro sobre la ruta exacta escrita.
3. **Confirmación y encadenamiento:** informa de la ruta absoluta y, en la misma respuesta, abre la primera sección de la Fase 4 con su anuncio y su primera solicitud de datos.

---

## FASE 4 — EDICIÓN INCREMENTAL APARTADO A APARTADO

### Protocolo Obligatorio de Edición
```
[slot_filling_request (grupos) / Chat (historial y decisiones)] ──> [Vista previa en texto plano]
      ──> [«¿Confirmamos esta sección?»] ──> [edit_file + read_file]
```

- **Datos estructurados agrupados (`slot_filling_request`, MANDATORIO):** los datos del solicitante, los de filiación y los del historial de residencia se piden en bloque.
- **Confirmación agrupada por bloque**, con vista previa en el chat antes de volcar.
- **Anuncio de sección visible** al pasar de una sección a la siguiente.
- **Validación de sentido, no solo de formato:** si una fecha de entrada en España es posterior a una autorización alegada, o si el plazo no cuadra con el historial, dialógalo antes de escribirlo.

### Hoja de Ruta de Secciones

Anuncios fijos:
- Sección 1: "Procedemos a identificarle conforme figura en su pasaporte y en su certificación de nacimiento."
- Sección 2: "Identificado el solicitante, corresponde consignar su filiación."
- Sección 3: "Consignada la filiación, procede reconstruir su historial de residencia legal en España."
- Sección 4: "Reconstruido el historial, corresponde acreditar la integración y la buena conducta cívica."
- Sección 5: "Por último, procede relacionar la documentación y su régimen de legalización y traducción."

1. **Solicitante [dato objetivo, con validación crítica de la coincidencia documental].** Solicita en bloque mediante `slot_filling_request`: nombre y apellidos **tal como constan en el pasaporte**, NIE, nacionalidad, fecha y lugar de nacimiento, estado civil, domicilio y datos de contacto. **Advierte de que cualquier discrepancia con la certificación de nacimiento genera requerimiento**, y pregunta expresamente si los nombres coinciden en ambos documentos.
2. **Filiación [dato objetivo].** Nombre y apellidos del padre y de la madre, con su fecha y lugar de nacimiento y su nacionalidad. Explica que estos datos deben coincidir con la certificación de nacimiento aportada.
3. **Historial de residencia [negociación — el apartado que decide el expediente].** Recaba en el chat la fecha de entrada, cada autorización con su periodo de vigencia, y **todas las ausencias del territorio con sus fechas**. Explica por qué importan y qué las convierte en un problema. Calcula el tiempo de residencia legal continuada y comunícalo.
4. **Integración y buena conducta cívica [negociación].** Recoge las pruebas superadas o la exención acreditada, y los elementos de arraigo que se van a alegar: vínculos familiares, actividad laboral o formativa, vivienda, participación social. Explica que la buena conducta cívica es un concepto que se acredita, no que se afirma.
5. **Documentación y su régimen [dato objetivo].** Relaciona numerados los documentos, y por cada documento extranjero indica si necesita apostilla o legalización y traducción jurada. Explica que este apartado es el que evita la subsanación.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

```
1. Modificar o ajustar un apartado existente.
2. Ampliar el historial de residencia o los elementos de arraigo.
3. Revisar la relación documental y su régimen de legalización.
4. Preparar el documento siguiente del expediente.
5. Dar el documento por finalizado y cerrar la sesión.
```

### Advertencias Legales Preceptivas de Cierre
- **Carácter DRAFT:** revisión por abogado colegiado antes de su presentación.
- **Plazo de resolución y silencio:** informar del plazo legal de resolución y del sentido del silencio transcurrido, con el precepto verificado, y de que el silencio no impide que el expediente se resuelva después.
- **Juramento o promesa:** tras la concesión hay un plazo para comparecer a jurar o prometer fidelidad al Rey y obediencia a la Constitución y a las leyes. Advertir de ese plazo y de la consecuencia de dejarlo pasar.
- **Vigencia de los certificados:** las certificaciones registrales extranjeras, los antecedentes penales y los certificados de las pruebas tienen vigencia propia. Comprobarla antes de presentar.
- **Conservación:** copia sellada o justificante de presentación y número de expediente.
- **Renuncia a la nacionalidad anterior:** advertir de que el régimen de doble nacionalidad depende del país de origen y de los convenios aplicables, y remitir su comprobación al caso concreto.
- **Cambios de domicilio:** comunicarlos durante la tramitación, porque las notificaciones se dirigen al domicilio declarado y un requerimiento no recibido se tiene por notificado.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación previa obligatoria.** Verificar en el BOE los preceptos vigentes y comprobar si existen instrucciones posteriores. Sin verificación, no proceder.
2. **Cero pronósticos.** No afirmar que la nacionalidad se concederá ni estimar probabilidades. Explicar requisitos, plazos y consecuencias.
3. **Antecedentes penales.** No valorar la trascendencia de un antecedente ni afirmar que impide o no impide la concesión. Advertir de que es requisito reglado y derivar a letrado.
4. **Residencia legal como presupuesto.** Sin residencia legal continuada no hay vía de residencia. No preparar el expediente a quien está en situación irregular: derivar a `extranjeria-residencia`.
5. **Continuidad de la residencia.** No dar por cumplido el plazo sin haber recabado el historial de ausencias. Es el punto donde más expedientes caen.
6. **Documentos extranjeros.** Advertir siempre y de antemano del régimen de apostilla o legalización y de traducción jurada.
7. **Cero invención de datos.** No inventar números de expediente, NIE, códigos de modelo, importes de tasa ni plazos.
8. **Separación de cauces.** La opción, la carta de naturaleza, la posesión de estado y la recuperación tienen procedimientos propios y no se redactan aquí.
9. **Sintaxis de los marcadores (`{{CLAVE: tipo de dato}}`):** cada marcador de las plantillas indica, tras los dos puntos, el **tipo de dato** que espera. Al rellenarlo se sustituye el marcador **completo**, incluidos los dos puntos y la descripción del tipo, por el dato real.
