---
name: arrendamiento-urbano
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
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
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
  - references/fuentes-plantillas-validadas.md
  - references/lau-arrendamiento-local-negocio.md
  - references/lau-derechos-obligaciones-partes.md
  - references/lau-vivienda-plazos-renta-fianza.md
  - references/temporada-habitacion-comunicaciones.md
assets:
  - assets/template-comunicacion-actualizacion-renta.md
  - assets/template-comunicacion-no-renovacion.md
  - assets/template-contrato-arrendamiento-habitacion.md
  - assets/template-contrato-arrendamiento-local.md
  - assets/template-contrato-arrendamiento-temporada.md
  - assets/template-contrato-arrendamiento-vivienda.md
  - assets/template-requerimiento-devolucion-fianza.md
---

# Generar Documentos de Arrendamiento Urbano

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación —cuyo catálogo y su correspondencia con las respuestas del formulario figuran en la Fase 1.2— y el origen de la plantilla (`origen_plantilla`).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

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
      "id": "tipo_gestion",
      "rationale": "Resolver V0: separa la redacción de un contrato nuevo de la comunicación sobre un contrato ya vigente, que usan assets y régimen distintos.",
      "question": "¿Qué necesita preparar?",
      "options": [
        {"id": "contrato_nuevo", "label": "Un contrato de arrendamiento nuevo"},
        {"id": "comunicacion_contrato_vigente", "label": "Una comunicación sobre un contrato ya firmado (renta, no renovación o fianza)"}
      ]
    },
    {
      "id": "tipo_inmueble",
      "rationale": "Resolver V2 y V5: determina el título de la LAU aplicable, la fianza mínima legal y los plazos imperativos.",
      "question": "Si es un contrato nuevo, ¿qué se arrienda?",
      "options": [
        {"id": "vivienda_completa", "label": "Una vivienda completa"},
        {"id": "habitacion", "label": "Una habitación dentro de una vivienda (régimen del Código Civil)"},
        {"id": "local_uso_distinto", "label": "Un local de negocio o inmueble para uso distinto de vivienda"}
      ]
    },
    {
      "id": "finalidad_uso",
      "rationale": "Resolver V1: distingue la vivienda habitual, sujeta a los plazos mínimos y a los límites de zona tensionada, del arrendamiento de temporada, y excluye el uso turístico.",
      "question": "Si es una vivienda completa, ¿a qué uso se destina?",
      "options": [
        {"id": "permanente", "label": "Residencia habitual y permanente del arrendatario"},
        {"id": "temporada", "label": "Temporada, con causa real y acreditable (trabajo, estudios, obras, verano)"},
        {"id": "turistico", "label": "Alquiler turístico o de corta estancia con fines vacacionales"}
      ]
    },
    {
      "id": "tipo_comunicacion",
      "rationale": "Resolver V7: cada comunicación tiene su propio asset, su plazo de preaviso y su validación de fechas.",
      "question": "Si es una comunicación sobre un contrato vigente, ¿de qué tipo?",
      "options": [
        {"id": "actualizacion_renta", "label": "Actualización anual de la renta"},
        {"id": "no_renovacion", "label": "No renovación del contrato a su vencimiento"},
        {"id": "devolucion_fianza", "label": "Requerimiento de devolución de la fianza"}
      ]
    },
    {
      "id": "remitente_comunicacion",
      "rationale": "Resolver V8: el plazo de preaviso del artículo 10.1 LAU es distinto según quién comunique, y la devolución de fianza solo la reclama el arrendatario.",
      "question": "Si es una comunicación, ¿quién la remite?",
      "options": [
        {"id": "arrendador", "label": "El arrendador (propietario)"},
        {"id": "arrendatario", "label": "El arrendatario (inquilino)"}
      ]
    },
    {
      "id": "zona_tensionada",
      "rationale": "Resolver V6: los límites de renta y la prórroga extraordinaria de zona de mercado residencial tensionado dependen de este valor. Si el usuario no lo sabe, el agente lo verifica él mismo con `web_search` en el boletín oficial autonómico.",
      "question": "¿Está el inmueble en zona de mercado residencial tensionado?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"},
        {"id": "no_lo_se", "label": "No lo sé: verifíquelo usted"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V0` — respuesta a `tipo_gestion`
- `V1` — respuesta a `finalidad_uso`
- `V2` — respuesta a `tipo_inmueble` (vivienda si es `vivienda_completa` o `habitacion`; local si es `local_uso_distinto`)
- `V5` — respuesta a `tipo_inmueble` (`vivienda_completa` frente a `habitacion`)
- `V3` — naturaleza del arrendador (persona física o jurídica): no se pregunta en el formulario de clasificación; se resuelve al recoger sus datos en la Fase 4
- `V4` — naturaleza del arrendatario (persona física o jurídica): no se pregunta en el formulario de clasificación; se resuelve al recoger sus datos en la Fase 4
- `V6` — respuesta a `zona_tensionada`, verificada después por el agente con `web_search`
- `V7` — respuesta a `tipo_comunicacion`
- `V8` — respuesta a `remitente_comunicacion`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores necesarios, evalúa:
- Si [V0 = Comunicación] y [V7 = Actualización de renta] -> Plantilla a usar: `assets/template-comunicacion-actualizacion-renta.md`.
- Si [V0 = Comunicación] y [V7 = No renovación] -> Plantilla a usar: `assets/template-comunicacion-no-renovacion.md`.
- Si [V0 = Comunicación] y [V7 = Devolución de fianza] -> Plantilla a usar: `assets/template-requerimiento-devolucion-fianza.md` (remitente: arrendatario. Si quien consulta es el arrendador que quiere CONTESTAR a un requerimiento recibido, detén el proceso y deriva a derivación formal).
- Si [V0 = Contrato] y [V2 = Local] -> Plantilla a usar: `assets/template-contrato-arrendamiento-local.md` (Fianza mínima: 2 mensualidades). La duración del local es de libre pacto (Título III LAU): no aplica V1.
- Si [V0 = Contrato] y [V2 = Vivienda] y [V5 = Habitación] -> Plantilla a usar: `assets/template-contrato-arrendamiento-habitacion.md` (régimen del Código Civil, arts. 1542 y ss.; fianza de libre pacto). No aplican V1 ni V6.
- Si [V0 = Contrato] y [V5 = Vivienda completa] y [V1 = Permanente] -> Plantilla a usar: `assets/template-contrato-arrendamiento-vivienda.md` (Fianza mínima: 1 mensualidad). V6 determina los bloques de zona tensionada del asset (Arts. 10.3, 17.6 LAU); si V6 = No lo sé, se resuelve en la sección 1 de la edición incremental.
- Si [V0 = Contrato] y [V5 = Vivienda completa] y [V1 = Temporal] identificado como temporada -> Plantilla a usar: `assets/template-contrato-arrendamiento-temporada.md` (uso distinto de vivienda, Art. 3.2 LAU; fianza mínima: 2 mensualidades). Exige causa de temporalidad real (Guardrail 8).
- Si [V1 = Temporal] identificado como turístico -> Detén el proceso: vivienda turística excluida expresamente de la LAU (Art. 5.e), sujeta a normativa turística autonómica. No crees documento.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Normativa civil y procesal aplicable consolidada y verificada en el BOE.
2. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** y nombrala por su ruta. Si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la seccion de assets.
3. **Pregunta Explícita al Usuario (Vía Chat):** Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

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
2. **Validación de Integridad (`read_file`):**
   - Ejecuta inmediatamente `read_file` sobre el archivo recién creado para comprobar que el volcado es íntegro y que el archivo existe en disco.
3. **Confirmación en Chat y Encadenamiento Inmediato:**
   - Informa al usuario de la ruta absoluta del documento creado.
   - En esa **misma respuesta**, introduce la primera sección/cláusula de la **Fase 4** y formula ya su primera pregunta, sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

### Protocolo Obligatorio de Edición
Para cada cláusula o bloque temático del documento, ejecuta estrictamente el siguiente ciclo interactivo:
```
[Pregunta al Usuario] ──> [Vista Previa en texto plano] ──> [¿Confirmamos?] ──> [edit_file + read_file]
```
1. **Pregunta en Chat:** Solicita los datos específicos de la sección.
2. **Vista Previa:** Muestra el texto exacto redactado en texto plano en el chat.
3. **Confirmación:** Consulta al usuario si está conforme o desea algún ajuste.
4. **Persistencia en Disco:** Una vez confirmado, ejecuta `edit_file` con `old_string` y `new_string` exactos, y verifica con `read_file`.

### Hoja de Ruta de Secciones y Cláusulas Condicionales

Ahora, recorre secuencialmente la lista de secciones de la ruta resuelta en la Fase 1 (5.A para contratos, 5.B para comunicaciones). Por cada sección de la que falten datos, aplica el Ciclo de Edición Incremental del sistema global (Petición de datos -> Mostrar Vista Previa en texto plano -> Pedir Confirmación -> Tras confirmación, usar `edit_file` en disco).

**Petición de grupos de datos mediante `slot_filling_request` y confirmaciones en el chat:**
- **Datos estructurados agrupados mediante `slot_filling_request`:** Para cualquier grupo de datos objetivos o identificativos (p. ej. datos de las partes: nombre/razón social, DNI/NIE/CIF, domicilio; datos del inmueble o de cuenta bancaria), **NO pregunte dato por dato en el chat**. Invoque la tool `slot_filling_request` agrupando todos los campos del bloque de una sola vez.
- **Validación de sentido, no solo de formato:** Razone si la respuesta tiene sentido en el contexto de lo preguntado. Si la respuesta es absurda, imposible o claramente incongruente, dialogue en el chat, señale el motivo y pida aclaración antes de volcarla al documento.

**Anuncio de sección (visible, sin esperar confirmación aparte):** al terminar una sección (aplicado su `edit_file`, o la confirmación de la sección de partes) y antes de la primera solicitud o pregunta de la sección siguiente, añada en el mismo mensaje el anuncio fijo de esa sección (tono de abogado, usted, sin coloquialismos), y a continuación proceda con la herramienta o pregunta. No pida permiso para pasar de sección: informe y continúe. Estos anuncios son de la sección SUSTANTIVA del documento, identificable por el cliente (ubicación, partes, objeto...); sigue estrictamente prohibido nombrar vectores, puntos numerados o fases de la instrucción interna (Directiva de Invisibilidad).

**Diálogo y acuerdo en las cláusulas de negociación entre partes:** no todas las cláusulas son datos objetivos (nombre, dirección, NIF): algunas implican una decisión o un pacto entre arrendador y arrendatario con consecuencias legales — duración y prórrogas, renta y su índice de actualización, fianza y garantías adicionales, reparto de gastos, límites de renta en zona tensionada, causa de la temporada, normas de convivencia, pactos opcionales (adquisición preferente, mediación). En esas cláusulas no se limite a registrar el número o la opción que dé el cliente: explique brevemente el régimen legal por defecto o la implicación relevante (p. ej., que los gastos de gestión son siempre del arrendador por el Art. 20.1 LAU, que una duración inferior al mínimo legal se prorroga igualmente, que la actualización no puede superar el IRAV, o que la garantía adicional no puede exceder de 2 mensualidades por el Art. 36.5 LAU), y confirme que el cliente entiende y está de acuerdo antes de escribirlo en el documento. Esto es dialogar y llegar a un acuerdo, no una simple confirmación mecánica de dato. Cada sección de las listas siguientes está marcada como **[negociación]** o **[dato objetivo]**.

### 5.A — Contratos (vivienda habitual, local, temporada, habitación)

Anuncios fijos (vivienda habitual; para las variantes de otras rutas, ver las notas de cada sección):
- Al abrir la sección 1 (tras la confirmación de creación del documento, Fase 3): "Procedemos a determinar la ubicación del inmueble, a los efectos de verificar su posible sujeción a los límites de renta en zona de mercado residencial tensionado." — En local, temporada y habitación, donde no aplican esos límites, el anuncio es: "Procedemos a determinar la ubicación del inmueble."
- Al pasar a la sección 2: "Concluida la ubicación del inmueble, pasamos a la identificación de las partes contratantes."
- Al pasar a la sección 3: "Identificadas las partes, procede determinar el objeto del contrato."
- Al pasar a la sección 4: "Determinado el objeto, corresponde fijar la duración del arrendamiento."
- Al pasar a la sección 5: "Fijada la duración, procede establecer la renta pactada."
- Al pasar a la sección 6: "Establecida la renta, corresponde determinar su índice de actualización." — Solo vivienda habitual y local; en temporada y habitación esta sección se omite salvo que la duración pactada supere el año.
- Al pasar a la sección 7: "Procedemos a fijar la fianza y, en su caso, las garantías adicionales."
- Al pasar a la sección 8: "Corresponde ahora determinar el reparto de gastos y suministros."
- Al pasar a la sección 9: "Por último, procede recoger los pactos opcionales que las partes deseen incorporar." — En habitación: "Por último, procede fijar las normas de uso y convivencia y los pactos opcionales."

1. **Ubicación y Zona Tensionada [dato objetivo, verificado por el agente]:** Pregunte únicamente la comunidad autónoma y el municipio del inmueble (texto libre). **Solo vivienda habitual:** la declaración de zona de mercado residencial tensionado es un dato público, publicado en el boletín oficial autonómico correspondiente (o en el BOE, si la declaración es estatal): en cuanto tenga el municipio, verifíquelo usted mismo con `web_search` (p. ej. "zona mercado residencial tensionado [municipio] [comunidad autónoma] boletín oficial"), priorizando el boletín oficial correspondiente como fuente frente a resultados no oficiales, e informe del resultado en la vista previa de la cláusula, sin necesidad de que el cliente confirme el dato. Si el resultado verificado contradice lo indicado en la clasificación (V6), prevalece la fuente oficial: infórmelo y ajuste los bloques del contrato. En local, temporada y habitación no hay verificación de zona tensionada.
2. **Partes (`slot_filling_request` agrupado por parte con confirmación en el chat):** No pida los datos identificativos uno a uno en el chat. Solicite los datos de cada parte en bloque mediante `slot_filling_request`:
   - Arrendador: solicite en bloque nombre completo/razón social (según V3), documento de identidad (DNI/NIE si física, NIF/CIF si jurídica) y domicilio a efectos de notificaciones (en habitación, incluya título de disponibilidad). Al recibir el resultado de la tool, muestre en el chat la vista previa conjunta, pida confirmación ("¿Confirmamos estos datos del arrendador?") y, tras confirmar, aplique el `edit_file`.
   - Arrendatario: solicite en bloque mediante `slot_filling_request` nombre completo/razón social (según V4), documento de identidad y domicilio actual (en temporada: domicilio habitual permanente distinto de la finca). Al recibir el resultado de la tool, muestre en el chat la vista previa conjunta, pida confirmación ("¿Confirmamos estos datos del arrendatario?") y aplique el `edit_file`.
   - Validaciones: aplique la validación de coherencia nombre/V3/V4 y formato de documento (DNI/NIE/CIF). Si hay incongruencias, pida aclaración en el chat antes de volcar.
3. **Objeto [dato objetivo; en temporada incluye una decisión de negociación]:** Dirección completa, referencia catastral, m2, anexos (garaje, trastero). La referencia catastral se pide siempre directamente al cliente, sin intentar buscarla usted mismo: la Sede Electrónica del Catastro es un buscador interactivo, no una URL consultable con `web_search`/`WebFetch`. Si el cliente no la tiene a mano, queda como `{{DATO_FALTANTE}}` (Guardrail 11): no la invente ni la intente localizar. **En temporada** pregunte además la causa concreta de la temporada (trabajo temporal, estudios, verano, obras en la vivienda habitual...) **[negociación]**: explique que la causa debe ser real y acreditable y que sin ella el contrato se recalificaría como vivienda habitual, y valídela (Guardrail 8). **En habitación** el objeto es la identificación de la habitación dentro de la vivienda (número o descripción, superficie, equipamiento) y las zonas comunes de uso compartido; no se pide referencia catastral.
4. **Duración [negociación]:** En vivienda habitual: duración en años o "mínimo legal", fecha de inicio (recuerde los mínimos de 5/7 años del Art. 9.1 LAU y la prórroga del Art. 10). Aproveche este dato para fijar también el lugar y la fecha de firma del encabezamiento del contrato (`{{MUNICIPIO}}` y `{{FECHA_CONTRATO}}`): salvo que el cliente indique otra cosa, coinciden con el municipio del inmueble y con la fecha en que se cierra esta sección. En local: duración pactada y, en su caso, prórroga expresa (sin denuncia el contrato se extingue al vencimiento). En temporada: fechas de inicio y fin ligadas a la causa, sin prórroga legal. En habitación: fechas de inicio y fin y, en su caso, preaviso de terminación anticipada.
5. **Renta [negociación]:** Importe mensual en euros (en temporada: importe y periodicidad — mensual o por la temporada completa), forma de pago, IBAN. En vivienda habitual en zona tensionada, aplique los límites de los Arts. 17.6 y 17.7 LAU (Guardrail 5) y explíquelos antes de fijar el importe.
6. **Actualización [negociación]:** Solo vivienda habitual y local (en temporada y habitación, únicamente si la duración supera el año y las partes lo desean). En vivienda habitual: índice pactado o "según ley" — explique que en contratos celebrados desde el 26/05/2023 el incremento anual no puede superar el IRAV publicado por el INE (Guardrail 6). En local: índice de libre pacto (IPC, IGC u otro).
7. **Fianza y Garantías [negociación]:** Meses de fianza (verifique el mínimo legal de su ruta: 1 mensualidad vivienda habitual, 2 local y temporada, libre pacto en habitación), garantías adicionales — en vivienda de hasta 5/7 años, con el límite de 2 mensualidades del Art. 36.5 LAU, que debe explicar antes de pactar.
8. **Gastos y Suministros [negociación]:** Quién paga IBI, comunidad (por defecto arrendador; suministros a cargo del inquilino; en habitación: si los suministros van incluidos en la renta, a tanto fijo o por reparto). Recuerde el Art. 20.1 LAU (gastos de gestión y formalización siempre del arrendador) en vivienda habitual.
9. **Pactos Opcionales [negociación]:** Renuncia a adquisición preferente (vivienda y local), correos electrónicos para notificaciones, mediación, cláusulas extra. En habitación: normas de uso y convivencia y normas adicionales de la vivienda.

### 5.B — Comunicaciones (actualización de renta, no renovación, devolución de fianza)

Anuncios fijos:
- Al abrir la sección 1 (tras la confirmación de creación del documento, Fase 3): "Procedemos a identificar el contrato de arrendamiento sobre el que versa la comunicación."
- Al pasar a la sección 2: "Identificado el contrato, pasamos a los datos de remitente y destinatario de la comunicación."
- Al pasar a la sección 3: en actualización de renta, "Corresponde ahora determinar la actualización de renta a comunicar."; en no renovación, "Corresponde ahora fijar el vencimiento del contrato y verificar el plazo de preaviso."; en devolución de fianza, "Corresponde ahora concretar la fianza reclamada y los plazos aplicables."
- Al pasar a la sección 4: "Por último, procede fijar el lugar y la fecha de emisión y las indicaciones de envío."

1. **Contrato de referencia [dato objetivo]:** solicite en bloque mediante `slot_filling_request` los datos: fecha de celebración del contrato, tipo (vivienda o uso distinto) e inmueble (dirección y municipio). Al recibir los datos, muestre vista previa en el chat y pida confirmación antes del `edit_file`.
2. **Remitente y destinatario (`slot_filling_request` con confirmación en el chat):** solicite los datos de remitente y destinatario en bloque mediante `slot_filling_request` (remitente: nombre o razón social, NIF/CIF y domicilio; destinatario: nombre y domicilio de notificaciones fijado en el contrato). La condición de cada uno (arrendador/arrendatario) ya está resuelta (V8): no la vuelva a preguntar. Al recibir los datos de la tool, muestre vista previa conjunta en el chat, pida confirmación explícita y aplique el `edit_file`.
3. **Contenido específico [negociación — explique el régimen legal antes de fijar cada valor]:**
   - *Actualización de renta:* cláusula del contrato que pacta la actualización (sin pacto expreso no procede la comunicación: adviértalo y detenga la redacción si no existe), renta vigente, índice aplicable y porcentaje. Verifique usted mismo con `web_search` el valor del IRAV vigente publicado por el INE en la fecha de la actualización e infórmelo; si el porcentaje que pretende el cliente supera el IRAV (contratos de vivienda desde el 26/05/2023), explique el límite del Guardrail 6 y no lo redacte por encima. Calcule y muestre la renta resultante y el mes de efectos (el siguiente a la notificación, Art. 18.2 LAU).
   - *No renovación:* fecha de vencimiento del plazo o de la prórroga en curso. **Validación de plazos obligatoria:** compruebe que entre la fecha de envío prevista y el vencimiento median al menos 4 meses (remitente arrendador) o 2 meses (remitente arrendatario), Art. 10.1 LAU; si no llegan, advierta de que la comunicación sería extemporánea y de que el contrato se prorrogaría (Guardrail 9). Si el remitente es el arrendador y V6 = Sí, mantenga el bloque de advertencia de la prórroga extraordinaria del Art. 10.3 LAU; si V6 = No lo sé, verifíquelo con `web_search` como en 5.A.1.
   - *Devolución de fianza:* fecha de extinción del contrato, fecha de entrega de llaves, importe de la fianza, IBAN de devolución y plazo de atención del requerimiento. **Validación de plazos obligatoria:** compruebe que ha transcurrido más de 1 mes desde la entrega de llaves (Art. 36.4 LAU); si no, adviértalo y no redacte el requerimiento sin dejar constancia de la advertencia (Guardrail 10).
4. **Emisión y envío [dato objetivo]:** lugar y fecha de emisión. En la vista previa final, recuerde la recomendación de envío por burofax con certificación de texto y acuse de recibo al domicilio de notificaciones del contrato.

(Los límites legales de cada sección — duración, gastos, zonas tensionadas, IRAV, fianza, preavisos — están fijados en la sección Guardrails al inicio de este documento; no se redacta por fuera de esos límites.)

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

1. Verificar siempre la normativa aplicable en el BOE antes de redactar (LAU; Ley 12/2023 e IRAV si vivienda habitual; Codigo Civil si habitacion). Sin verificacion, no proceder.
2. Verificar siempre la versión consolidada vigente de la norma en el BOE antes de redactar. Si se detectan cambios normativos, aplicar la redacción vigente en el documento a generar en el workspace sin usar versiones desactualizadas.
3. Duracion minima en vivienda habitual: 5 anos si el arrendador es persona fisica, 7 anos si es persona juridica (Art. 9.1 LAU). No pactar plazos inferiores sin advertir de la prorroga obligatoria. En temporada, habitacion y local NO aplican los plazos minimos ni las prorrogas del Titulo II.
4. Gastos de gestion y formalizacion del contrato de vivienda siempre a cargo del arrendador (Art. 20.1 LAU).
5. En zonas de mercado residencial tensionado, aplicar los limites de renta de los Arts. 17.6 y 17.7 LAU y advertir de la prorroga extraordinaria del Art. 10.3 LAU. La declaracion de zona es un dato publico verificable (boletin oficial autonomico): contrastarla siempre, aunque el cliente crea conocer la respuesta.
6. Actualizacion de renta en vivienda habitual: en contratos celebrados desde el 26/05/2023, el incremento anual no puede superar el IRAV publicado por el INE (Resolucion INE 18/12/2024, BOE-A-2024-26685, vigente desde 01/01/2025). No redactar clausulas de actualizacion por encima de ese limite ni comunicaciones de actualizacion con porcentaje superior al IRAV vigente.
7. Fianza minima legal: 1 mensualidad en vivienda habitual, 2 mensualidades en local y en temporada (uso distinto de vivienda, Art. 36.1 LAU). No admitir fianzas inferiores. En habitacion (Codigo Civil) la fianza es de libre pacto. Garantias adicionales en vivienda de hasta 5/7 anos: maximo 2 mensualidades (Art. 36.5 LAU).
8. Arrendamiento de temporada: exigir una causa de temporalidad real y acreditable. NUNCA redactar un contrato de temporada para encubrir una residencia habitual y permanente (fraude de ley): si se detecta esa intencion, rechazar, explicar la recalificacion como vivienda (Titulo II LAU) y ofrecer el contrato de vivienda.
9. Comunicacion de no renovacion (Art. 10.1 LAU): preaviso minimo de 4 meses si comunica el arrendador y 2 meses si comunica el arrendatario, contados desde el vencimiento hacia atras. Verificar SIEMPRE las fechas antes de redactar; si el preaviso ya no llega, advertir de que la comunicacion seria extemporanea y de que el contrato se prorrogaria.
10. Requerimiento de devolucion de fianza: solo procede transcurrido 1 mes desde la entrega de llaves (Art. 36.4 LAU). Verificar las fechas; antes de ese mes, no redactar el requerimiento sin advertirlo.
11. Marcar todos los campos a rellenar como placeholder pendiente. Use el nombre propio de la plantilla (p. ej. `{{NOMBRE_ARRENDADOR}}`, `{{REFERENCIA_CATASTRAL}}`): NO lo sustituya por un literal genérico como `{{DATO_FALTANTE}}`, que se repetiría idéntico en múltiples campos y rompería la precisión quirúrgica del `edit_file` (oldString ambiguo) al rellenar cada uno por separado. Nunca inventar datos, rentas, fechas ni referencia catastral.
12. Nunca redactar clausulas que contravengan normas imperativas de la ley aplicable. Nunca inventar jurisprudencia.
