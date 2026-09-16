---
name: arrendamiento-urbano
description: >
  Genera los documentos del ciclo completo del arrendamiento urbano: contratos nuevos (vivienda
  habitual, local de negocio, vivienda por temporada y habitacion) y comunicaciones sobre contratos
  vigentes (actualizacion anual de la renta, no renovacion a vencimiento y requerimiento de
  devolucion de fianza). Aplica la **Ley 29/1994 de Arrendamientos Urbanos (LAU)**, que rige los alquileres de vivienda y de uso distinto (duracion, prorrogas, renta y fianza), la **Ley 12/2023 por
  el derecho a la vivienda** (zonas de mercado residencial tensionado, IRAV) y el **Codigo Civil**
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
      "rationale": "Resolver V2: determina el título de la LAU aplicable, la fianza mínima legal y los plazos imperativos.",
      "question": "Si es un contrato nuevo, ¿qué se arrienda?",
      "options": [
        {"id": "vivienda_completa", "label": "Una vivienda completa"},
        {"id": "habitacion", "label": "Una habitación dentro de una vivienda (régimen del Código Civil)"},
        {"id": "local_uso_distinto", "label": "Un local de negocio o inmueble para uso distinto de vivienda"},
        {"id": "no_procede", "label": "No es un contrato nuevo"}
      ]
    },
    {
      "id": "finalidad_uso",
      "rationale": "Resolver V1: distingue la vivienda habitual, sujeta a los plazos mínimos y a los límites de zona tensionada, del arrendamiento de temporada, y excluye el uso turístico.",
      "question": "Si es una vivienda completa, ¿a qué uso se destina?",
      "options": [
        {"id": "permanente", "label": "Residencia habitual y permanente del arrendatario"},
        {"id": "temporada", "label": "Temporada, con causa real y acreditable (trabajo, estudios, obras, verano)"},
        {"id": "turistico", "label": "Alquiler turístico o de corta estancia con fines vacacionales"},
        {"id": "no_procede", "label": "No es una vivienda completa"}
      ]
    },
    {
      "id": "tipo_comunicacion",
      "rationale": "Resolver V7: cada comunicación tiene su propio asset, su plazo de preaviso y su validación de fechas.",
      "question": "Si es una comunicación sobre un contrato vigente, ¿de qué tipo?",
      "options": [
        {"id": "actualizacion_renta", "label": "Actualización anual de la renta"},
        {"id": "no_renovacion", "label": "No renovación del contrato a su vencimiento"},
        {"id": "devolucion_fianza", "label": "Requerimiento de devolución de la fianza"},
        {"id": "no_procede", "label": "No es una comunicación sobre un contrato vigente"}
      ]
    },
    {
      "id": "remitente_comunicacion",
      "rationale": "Resolver V8: el plazo de preaviso del artículo 10.1 LAU es distinto según quién comunique, y la devolución de fianza solo la reclama el arrendatario.",
      "question": "Si es una comunicación, ¿quién la remite?",
      "options": [
        {"id": "arrendador", "label": "El arrendador (propietario)"},
        {"id": "arrendatario", "label": "El arrendatario (inquilino)"},
        {"id": "no_procede", "label": "No es una comunicación"}
      ]
    },
    {
      "id": "zona_tensionada",
      "rationale": "Resolver V6: los límites de renta y la prórroga extraordinaria de zona de mercado residencial tensionado dependen de este valor. Si el usuario no lo sabe, el agente lo verifica él mismo con `web_search` en el boletín oficial autonómico.",
      "question": "Si es un contrato nuevo de vivienda, ¿está el inmueble en zona de mercado residencial tensionado?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"},
        {"id": "no_lo_se", "label": "No lo sé: verifíquelo usted"},
        {"id": "no_procede", "label": "No procede: no es un contrato nuevo de vivienda"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V0` — respuesta a `tipo_gestion`
- `V1` — respuesta a `finalidad_uso`
- `V2` — respuesta a `tipo_inmueble` (`vivienda_completa`, `habitacion` o `local_uso_distinto`)
- `V3` — naturaleza del arrendador (persona física o jurídica): no se pregunta en el formulario de clasificación; se resuelve al recoger sus datos en la Fase 4
- `V4` — naturaleza del arrendatario (persona física o jurídica): no se pregunta en el formulario de clasificación; se resuelve al recoger sus datos en la Fase 4
- `V6` — respuesta a `zona_tensionada`, verificada después por el agente con `web_search`
- `V7` — respuesta a `tipo_comunicacion`
- `V8` — respuesta a `remitente_comunicacion`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores necesarios, evalúa:
- Si [V0 = comunicacion_contrato_vigente] y [V7 = actualizacion_renta] -> Plantilla a usar: `assets/template-comunicacion-actualizacion-renta.md`.
- Si [V0 = comunicacion_contrato_vigente] y [V7 = no_renovacion] -> Plantilla a usar: `assets/template-comunicacion-no-renovacion.md`.
- Si [V0 = comunicacion_contrato_vigente] y [V7 = devolucion_fianza] -> Plantilla a usar: `assets/template-requerimiento-devolucion-fianza.md` (remitente: arrendatario. Si quien consulta es el arrendador que quiere CONTESTAR a un requerimiento recibido, detén el proceso y deriva a derivación formal).
- Si [V0 = contrato_nuevo] y [V2 = local_uso_distinto] -> Plantilla a usar: `assets/template-contrato-arrendamiento-local.md` (Fianza mínima: 2 mensualidades). La duración del local es de libre pacto (Título III LAU): no aplica V1.
- Si [V0 = contrato_nuevo] y [V2 = habitacion] -> Plantilla a usar: `assets/template-contrato-arrendamiento-habitacion.md` (régimen del Código Civil, arts. 1542 y ss.; fianza de libre pacto). No aplican V1 ni V6.
- Si [V0 = contrato_nuevo] y [V2 = vivienda_completa] y [V1 = permanente] -> Plantilla a usar: `assets/template-contrato-arrendamiento-vivienda.md` (Fianza mínima: 1 mensualidad). V6 determina los bloques de zona tensionada del asset (Arts. 10.3, 17.6 LAU); si V6 = No lo sé, se resuelve en la sección 1 de la edición incremental.
- Si [V0 = contrato_nuevo] y [V2 = vivienda_completa] y [V1 = temporada] -> Plantilla a usar: `assets/template-contrato-arrendamiento-temporada.md` (uso distinto de vivienda, Art. 3.2 LAU; fianza mínima: 2 mensualidades). Exige causa de temporalidad real (Guardrail 8).
- Si [V1 = turistico] -> Detén el proceso: vivienda turística excluida expresamente de la LAU (Art. 5.e), sujeta a normativa turística autonómica. No crees documento.

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

### 5.A — Contratos (vivienda habitual, local, temporada, habitación)

Anuncios fijos (vivienda habitual; para las variantes de otras rutas, ver las notas de cada sección):
- Al abrir la sección 1 (tras la creación del documento en Fase 3):
  - Si los datos de las partes ya fueron identificados y volcados al documento en la creación: "Habiendo identificado a las partes e incorporado sus datos al contrato, procedemos a determinar la ubicación del inmueble, a los efectos de verificar su posible sujeción a los límites de renta en zona de mercado residencial tensionado."
  - Si falta identificar o desambiguar partes: "Procedemos a la identificación de las partes contratantes."
- Al pasar a la sección 2: "Concluida la identificación de las partes, procedemos a determinar la ubicación del inmueble, a los efectos de verificar su posible sujeción a los límites de renta en zona de mercado residencial tensionado." — En local, temporada y habitación, donde no aplican esos límites, el anuncio es: "Concluida la identificación de las partes, procedemos a determinar la ubicación del inmueble."
- Al pasar a la sección 3: "Determinada la ubicación del inmueble, procede determinar el objeto del contrato."
- Al pasar a la sección 4: "Determinado el objeto, corresponde fijar la duración del arrendamiento."
- Al pasar a la sección 5: "Fijada la duración, procede establecer la renta pactada."
- Al pasar a la sección 6: "Establecida la renta, corresponde determinar su índice de actualización." — Solo vivienda habitual y local; en temporada y habitación esta sección se omite salvo que la duración pactada supere el año.
- Al pasar a la sección 7: "Procedemos a fijar la fianza y, en su caso, las garantías adicionales."
- Al pasar a la sección 8: "Corresponde ahora determinar el reparto de gastos y suministros."
- Al pasar a la sección 9: "Por último, procede recoger los pactos opcionales que las partes deseen incorporar." — En habitación: "Por último, procede fijar las normas de uso y convivencia y los pactos opcionales."

1. **Partes contratantes [dato objetivo e identificación — búsqueda prioritaria con `search_clients`, volcado inmediato a disco per REG-CLI-04]:**
   - Ejecute prioritariamente `search_clients` para localizar al arrendador y al arrendatario (llamadas paralelas si se conocen ambos nombres, o una llamada por cada parte a identificar).
   - Si se obtiene exactamente una coincidencia, use los datos de la ficha directamente (nombre completo, DNI/NIE/CIF, domicilio fiscal, email, teléfono) y no pida al usuario datos que ya constan en el sistema.
   - Si hay varias coincidencias (o desambiguación de partes), desambigüe mediante `restricted_human_in_the_loop_request` con opciones que muestren `display_name`, `fiscal_id` y `city`, incluyendo **OBLIGATORIAMENTE al final la opción de negación** con `id: "ninguna"` y `label: "Ninguna de las personas identificadas (otra persona)"`. Si el usuario elige esta opción para una parte, trátela como persona no registrada.
   - Si la persona no existe en el sistema, recabe sus datos indispensables mediante `slot_filling_request` y aplique de inmediato `REG-CLI-03` para ofrecer guardarla en el sistema.
   - **Volcado inmediato sin confirmación en chat (REG-CLI-04):** Si los datos de las partes ya constaban al inicio, DEBEN quedar volcados en el documento desde el `create_file` de la Fase 3. Si se recopilan o completan en este paso, aplique de inmediato `edit_file`. **Al volcar o editar los datos de las partes, sustituya sus nombres en TODAS sus apariciones a lo largo del documento entero: en el título/encabezado H1 (`# ... — {{NOMBRE_ARRENDADOR}} / {{NOMBRE_ARRENDATARIO}}`), en la comparecencia (REUNIDOS) y en el bloque final de FIRMAS (`Nombre: {{NOMBRE_...}}`). Está TERMINANTEMENTE PROHIBIDO actualizar únicamente la comparecencia y dejar marcadores pendientes en el título o en las firmas.** (Para marcadores de nombre recurrentes como `{{NOMBRE_ARRENDADOR}}`, use `replace_all: true` en `edit_file` o aplique ediciones que cubran título, comparecencia y firmas). Comunique al usuario en el chat los datos incorporados y los campos pendientes (ej. `{{IBAN}}`), y continúe de inmediato hacia la siguiente sección sin solicitar confirmación en el chat ("¿Confirmamos estos datos?").
   - Validaciones: aplique la validación de coherencia nombre/V3/V4 y formato de documento (DNI/NIE/CIF). Si hay incongruencias, pida aclaración en el chat antes de volcar.
2. **Ubicación y Zona Tensionada [dato objetivo, verificado por el agente]:** Si el cliente ya indicó el municipio o la ubicación del inmueble en el chat (o aportó la descripción general del piso), extraiga dicho dato directamente sin pedirlo de nuevo. Solo si no consta en absoluto, solicite la comunidad autónoma y el municipio. **Solo vivienda habitual:** la declaración de zona de mercado residencial tensionado es un dato público, publicado en el boletín oficial autonómico correspondiente (o en el BOE, si la declaración es estatal): en cuanto tenga el municipio, verifíquelo usted mismo con `web_search` (p. ej. "zona mercado residencial tensionado [municipio] [comunidad autónoma] boletín oficial"), priorizando el boletín oficial correspondiente como fuente frente a resultados no oficiales, e informe del resultado en la vista previa de la cláusula, sin necesidad de que el cliente confirme el dato. Si el resultado verificado contradice lo indicado en la clasificación (V6), prevalece la fuente oficial: infórmelo y ajuste los bloques del contrato. En local, temporada y habitación no hay verificación de zona tensionada.
3. **Objeto [dato objetivo; en temporada incluye una decisión de negociación]:** Dirección completa, referencia catastral, m2, anexos (garaje, trastero). Si el cliente ya aportó estos datos en su mensaje de chat (ej. describiendo la distribución, superficie, dirección, anejos o inventario), asúmalos directamente y redacte la vista previa de la cláusula en el chat sin convocar `slot_filling_request`. Si el cliente no aportó estos datos, solicítelos en bloque mediante `slot_filling_request`. La referencia catastral se pide siempre directamente al cliente, sin intentar buscarla usted mismo: la Sede Electrónica del Catastro es un buscador interactivo, no una URL consultable con `web_search`/`WebFetch`. Si el cliente no la tiene a mano, queda como `{{DATO_FALTANTE}}` (Guardrail 11): no la invente ni la intente localizar. **En temporada** pregunte además la causa concreta de la temporada (trabajo temporal, estudios, verano, obras en la vivienda habitual...) **[negociación]**: explique que la causa debe ser real y acreditable y que sin ella el contrato se recalificaría como vivienda habitual, y valídela (Guardrail 8). **En habitación** el objeto es la identificación de la habitación dentro de la vivienda (número o descripción, superficie, equipamiento) y las zonas comunes de uso compartido; no se pide referencia catastral.
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
2. **Remitente y destinatario (Búsqueda prioritaria con `search_clients`; `slot_filling_request` solo para faltantes):** busque prioritariamente a las partes con `search_clients` (emitiendo llamadas concurrentes si se conocen los nombres). Si hay 1 coincidencia, use los datos de la ficha directamente (nombre, NIF/CIF, domicilio fiscal); si hay varias, desambigüe mediante `restricted_human_in_the_loop_request` (incluyendo obligatoriamente al final la opción de negación `{"id": "ninguna", "label": "Ninguna de las personas identificadas (otra persona)"}`); solo si no existen o faltan datos indispensables, solicite en bloque los datos pendientes mediante `slot_filling_request`. La condición de cada uno (arrendador/arrendatario) ya está resuelta (V8): no la vuelva a preguntar. Al disponer de los datos, vuelque inmediatamente los datos al documento mediante `edit_file` per `REG-CLI-04`, sustituyendo exhaustivamente los nombres en todas sus apariciones (título/encabezado H1, remitente, destinatario y firma final), informe en el chat de los datos asentados y continúe de inmediato hacia el contenido específico sin pedir confirmación previa en el chat ("¿Confirmamos...?").
3. **Contenido específico [negociación — explique el régimen legal antes de fijar cada valor]:**
   - *Actualización de renta:* cláusula del contrato que pacta la actualización (sin pacto expreso no procede la comunicación: adviértalo y detenga la redacción si no existe), renta vigente, índice aplicable y porcentaje. Verifique usted mismo con `web_search` el valor del IRAV vigente publicado por el INE en la fecha de la actualización e infórmelo; si el porcentaje que pretende el cliente supera el IRAV (contratos de vivienda desde el 26/05/2023), explique el límite del Guardrail 6 y no lo redacte por encima. Calcule y muestre la renta resultante y el mes de efectos (el siguiente a la notificación, Art. 18.2 LAU).
   - *No renovación:* fecha de vencimiento del plazo o de la prórroga en curso. **Validación de plazos obligatoria:** compruebe que entre la fecha de envío prevista y el vencimiento median al menos 4 meses (remitente arrendador) o 2 meses (remitente arrendatario), Art. 10.1 LAU; si no llegan, advierta de que la comunicación sería extemporánea y de que el contrato se prorrogaría (Guardrail 9). Si el remitente es el arrendador y V6 = Sí, mantenga el bloque de advertencia de la prórroga extraordinaria del Art. 10.3 LAU; si V6 = No lo sé, verifíquelo con `web_search` como en 5.A.1.
   - *Devolución de fianza:* fecha de extinción del contrato, fecha de entrega de llaves, importe de la fianza, IBAN de devolución y plazo de atención del requerimiento. **Validación de plazos obligatoria:** compruebe que ha transcurrido más de 1 mes desde la entrega de llaves (Art. 36.4 LAU); si no, adviértalo y no redacte el requerimiento sin dejar constancia de la advertencia (Guardrail 10).
4. **Emisión y envío [dato objetivo]:** lugar y fecha de emisión. En la vista previa final, recuerde la recomendación de envío por burofax con certificación de texto y acuse de recibo al domicilio de notificaciones del contrato.

(Los límites legales de cada sección — duración, gastos, zonas tensionadas, IRAV, fianza, preavisos — están fijados en la sección Guardrails al inicio de este documento; no se redacta por fuera de esos límites.)

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
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
