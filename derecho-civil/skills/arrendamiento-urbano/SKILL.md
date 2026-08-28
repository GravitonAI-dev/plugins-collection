---
name: arrendamiento-urbano
description: >
  Genera y adapta contratos de arrendamiento urbano completos (vivienda habitual o local de negocio)
  conforme a la Ley 29/1994 de Arrendamientos Urbanos (LAU) en su versión consolidada vigente verificada
  en el BOE y la Ley 12/2023 por el derecho a la vivienda. Implementa un flujo estructurado con clasificación
  inicial de vectores de estado mediante formulario interactivo, propuesta de plan de acción legal y negociación
  de plantillas vía chat, creación del documento base en workspace y edición incremental cláusula a cláusula.
  NO usar para arrendamientos rústicos, viviendas turísticas reguladas por CCAA, contratos de temporada,
  viviendas militares ni cesiones gratuitas o precario.
when_to_use: |
  - El usuario desea redactar o personalizar un contrato de alquiler de vivienda habitual o local comercial.
  - El usuario necesita un contrato formal conforme a la LAU y normativa de vivienda vigente.
  - El usuario desea utilizar la plantilla oficial del sistema o aportar su propia minuta para su adaptación.
inputs:
  - destino_inmueble: vivienda habitual / local comercial / temporada / turístico (V1)
  - tipo_inmueble: vivienda / local (V2)
  - naturaleza_arrendador: persona física / persona jurídica (V3)
  - naturaleza_arrendatario: persona física / persona jurídica (V4)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - datos_arrendador: nombre o razón social, NIF o CIF, domicilio para notificaciones, representación
  - datos_arrendatario: nombre o razón social, NIF o CIF, domicilio actual, representación
  - datos_inmueble: dirección completa, referencia catastral, superficie útil, anejos (garaje, trastero), inventario
  - duracion: plazo pactado en años, fecha de inicio, prórrogas
  - renta_mensual: importe en euros, medio de pago, cuenta IBAN, límites de zona tensionada
  - actualizacion_renta: índice pactado (IGC / tope IPC según art. 18 LAU)
  - fianza_garantias: fianza legal obligatoria, organismo autonómico de depósito, garantías adicionales
  - gastos_suministros: distribución de IBI y comunidad, suministros individualizados
  - pactos_opcionales: renuncia a tanteo y retracto, notificaciones electrónicas, mediación/arbitraje, mascotas
outputs:
  - contrato_arrendamiento: contrato completo de arrendamiento urbano en markdown, DRAFT, conforme a la LAU
references:
  - references/lau-vivienda-plazos-renta-fianza.md
  - references/lau-derechos-obligaciones-partes.md
  - references/lau-arrendamiento-local-negocio.md
assets:
  - assets/template-contrato-arrendamiento-vivienda.md
  - assets/template-contrato-arrendamiento-local.md
---

# Generar Contrato de Arrendamiento Urbano

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y el cumplimiento riguroso de las normas imperativas de la LAU, el asistente resuelve y mantiene internamente en memoria los siguientes vectores de estado:
- **V1 (Destino / Finalidad):** `vivienda_habitual` (residencia permanente) | `local_comercial` (negocio estable) | `temporada` | `turistico`.
- **V2 (Tipo Inmueble):** `vivienda` (piso, casa, chalet) | `local` (nave, oficina, local comercial). *(Inferido de V1: si V1=`vivienda_habitual` $\rightarrow$ V2=`vivienda`; si V1=`local_comercial` $\rightarrow$ V2=`local`)*.
- **V3 (Naturaleza Arrendador):** `persona_fisica` (particular) | `persona_juridica` (sociedad, entidad).
- **V4 (Naturaleza Arrendatario):** `persona_fisica` (particular) | `persona_juridica` (sociedad, empresa).
- **V5 (Origen Plantilla / Asset):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural ("Dado que el arrendador es una empresa...", "Al tratarse de una vivienda habitual...").

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es resolver los vectores de estado de clasificación **V1, V2, V3 y V4**.

### 1.1 Escucha Activa Previa
Antes de invocar el formulario, evalúa el mensaje inicial y el historial de la conversación:
- Si el usuario **ya proporcionó de forma inequívoca** los datos para resolver `V1`, `V3` y `V4` (ej: *"Quiero redactar un contrato de alquiler de vivienda habitual de particular a particular"* $\rightarrow$ V1=`vivienda_habitual`, V2=`vivienda`, V3=`persona_fisica`, V4=`persona_fisica`), registra los vectores en silencio y avanza directamente a la **Fase 2**.
- Si falta resolver alguno de los vectores de clasificación o existe ambigüedad, invoca de inmediato la herramienta `restricted_human_in_the_loop_request` para formular el árbol de decisión interactivo.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas necesarias para completar la resolución de los vectores pendientes:

```json
{
  "form_data": [
    {
      "id": "destino_inmueble",
      "rationale": "Resolver V1 (Destino) y V2 (Tipo Inmueble) para determinar el régimen legal aplicable (LAU Título II Vivienda vs Título III Uso distinto).",
      "question": "¿Cuál es el destino o uso previsto del inmueble a arrendar?",
      "options": [
        {"id": "vivienda_habitual", "label": "Vivienda habitual y permanente (residencia permanente del inquilino)"},
        {"id": "local_comercial", "label": "Local de negocio / Comercial / Uso distinto de vivienda"},
        {"id": "temporada", "label": "Arrendamiento de temporada (vacacional, estudios, estancia temporal)"},
        {"id": "turistico", "label": "Vivienda turística (alojamiento turístico regulado por CCAA)"}
      ]
    },
    {
      "id": "naturaleza_arrendador",
      "rationale": "Resolver V3 (Naturaleza Arrendador) para fijar el plazo legal mínimo obligatorio (5 años si es física, 7 si es jurídica) e imputación de gastos según Art. 9 y 20 LAU.",
      "question": "¿Cuál es la condición jurídica de la parte ARRENDADORA (propietario)?",
      "options": [
        {"id": "persona_fisica", "label": "Persona física (particular)"},
        {"id": "persona_juridica", "label": "Persona jurídica (empresa, sociedad, entidad)"}
      ]
    },
    {
      "id": "naturaleza_arrendatario",
      "rationale": "Resolver V4 (Naturaleza Arrendatario) para fijar la estructura de partes y facultades de representación.",
      "question": "¿Cuál es la condición jurídica de la parte ARRENDATARIA (inquilino)?",
      "options": [
        {"id": "persona_fisica", "label": "Persona física (particular)"},
        {"id": "persona_juridica", "label": "Persona jurídica (empresa, sociedad)"}
      ]
    }
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)

Una vez fijados `V1`, `V2`, `V3` y `V4`, evalúa la rama de ejecución:
* **Si `[V1 = temporada]` O `[V1 = turistico]` $\rightarrow$ Detener proceso (Fuera de Alcance LAU):**
  - Informa en el chat de que los arrendamientos de temporada o turísticos se rigen por normativas sectoriales autonómicas o Código Civil especial, quedando excluidos de las garantías del arrendamiento de vivienda habitual de la LAU.
  - Ofrece derivar el caso a un abogado especialista. No crees documento.
* **Si `[V1 = vivienda_habitual]` (y `[V2 = vivienda]`):**
  - Régimen: Título II de la Ley 29/1994 (LAU) y Ley 12/2023 por el derecho a la vivienda.
  - Plantilla del sistema propuesta: `assets/template-contrato-arrendamiento-vivienda.md`.
  - Fianza legal obligatoria: 1 mensualidad de renta (Art. 36.1 LAU).
  - Duración mínima legal imperativa:
    - Si `[V3 = persona_fisica]` $\rightarrow$ Mínimo 5 años (Art. 9.1 LAU).
    - Si `[V3 = persona_juridica]` $\rightarrow$ Mínimo 7 años (Art. 9.1 LAU).
  - Proceder a la **Fase 2**.
* **Si `[V1 = local_comercial]` (y `[V2 = local]`):**
  - Régimen: Título III de la Ley 29/1994 (LAU) y primacía de los pactos de las partes.
  - Plantilla del sistema propuesta: `assets/template-contrato-arrendamiento-local.md`.
  - Fianza legal obligatoria: 2 mensualidades de renta (Art. 36.1 LAU).
  - Proceder a la **Fase 2**.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias en tu system prompt: `lau-vivienda-plazos-renta-fianza.md`, `lau-derechos-obligaciones-partes.md` y `lau-arrendamiento-local-negocio.md`.
2. Opcionalmente verifica en vivo con `web_search("Ley 29/1994 arrendamientos urbanos texto consolidado BOE")` si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y cordial que contenga:
1. **Marco Legal Aplicable:**
   - Cita la **Ley 29/1994 de Arrendamientos Urbanos (LAU)** y la **Ley 12/2023 por el derecho a la vivienda**.
   - Explica con claridad el impacto legal de la clasificación obtenida (`V1-V4`):
     - Duración mínima obligatoria (5 años si `V3=persona_fisica` / 7 años si `V3=persona_juridica`).
     - Fianza legal preceptiva (1 mensualidad si `V1=vivienda_habitual` / 2 mensualidades si `V1=local_comercial`).
     - Prohibición legal de imputar gastos de gestión inmobiliaria y formalización al arrendatario (Art. 20.1 LAU).
     - Límites de renta y prórrogas extraordinarias si la finca radica en zona tensionada.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Detalla que dispones de la plantilla oficial adaptada (`assets/template-contrato-arrendamiento-vivienda.md` o `assets/template-contrato-arrendamiento-local.md`), con una estructura jurídica completa y equilibrada.
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
* **Si `[V5 = plantilla_sistema]` (El usuario acepta la plantilla propuesta):**
  Toma el texto íntegro de la plantilla correspondiente directamente desde el bloque `<document kind="assets-collection">` de tu system prompt y procede de inmediato a la **Fase 3**.
* **Si `[V5 = plantilla_usuario]` (El usuario aporta su propia minuta adjuntando un documento o pegando texto):**
  1. **Acceso al Contenido del Adjunto:**
     - Si el usuario adjunta un archivo (PDF, DOCX, TXT, MD, etc.), su contenido está disponible en el bloque `# ATTACHED DOCUMENTS` / `<attached_documents>` del contexto.
     - Si el usuario pegó el texto directamente en el chat, tómalo del bloque `# USER MESSAGE` / `<user_message>`.
  2. **Guardrail de Verificación (Art. 6 LAU):**
     - Analiza el contenido de la plantilla aportada. Si contiene estipulaciones que contravengan normas imperativas del Título II de la LAU en perjuicio del arrendatario (ej. renuncia a la duración mínima legal de 5/7 años, fianza legal obligatoria superior a 1 mes, o atribución indebida de gastos de gestión inmobiliaria al inquilino):
       - Advierte expresamente al usuario en el chat sobre la nulidad de pleno derecho de dichas cláusulas.
       - Propón la redacción legalmente válida y ajustada a la LAU.
  3. **Adopción de la Plantilla:**
     - Adopta el texto íntegro de la plantilla del usuario como base y avanza a la **Fase 3** (donde se creará el archivo en el workspace mediante `create_file`).

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada (`V5`: ya sea el asset del catálogo desde `<document kind="assets-collection">` o la plantilla adjunta por el usuario desde `<attached_documents>` / `<user_message>`) en el archivo del workspace (ej: `contrato_arrendamiento.md` o `contrato_arrendamiento_vivienda.md`).
   - Aplica el principio **Zero-Omission**:
     - Sustituye todos los datos ya resueltos a través de los vectores `V1-V4` y la escucha activa inicial.
     - Todos los datos o campos pendientes deben permanecer explícitamente como marcadores `{{DATO_FALTANTE}}` en mayúsculas entre dobles llaves.
     - PROHIBIDO dejar archivos en blanco, sólo con títulos o crear resúmenes.
2. **Validación de Disco (`read_file`):**
   - Ejecuta `read_file` sobre el archivo recién creado para validar que el contenido en disco es exacto y completo.
3. **Confirmación en Chat:**
   - Emite un mensaje indicando la ruta absoluta del archivo creado (ej: *"He creado el documento base en `/ruta/workspace/contrato_arrendamiento.md`"*).
   - En la misma respuesta, sin detener la marcha, introduce la primera sección de la Fase 4 para iniciar la edición incremental.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA

Recorre de forma secuencial los siguientes bloques del contrato. Por cada sección que contenga placeholders `{{...}}` o requiera pacto entre las partes, ejecuta el **Ciclo de Edición Incremental**:

```
[Pregunta / Discusión en Chat] ──> [Vista Previa en texto plano] ──> [¿Confirmamos esta cláusula?] ──> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Pregunta y Diálogo:** Plantea las preguntas necesarias para completar la sección, asesorando sobre las opciones legales disponibles.
2. **Vista Previa (Preview):** Muestra en el chat el texto exacto redactado de la cláusula en texto plano (sin backticks de código).
3. **Petición de Confirmación:** Pregunta literalmente: `¿Confirmamos esta cláusula?`
4. **Edición en Disco:** Tras el "sí" o confirmación del usuario, aplica `edit_file` sustituyendo con exactitud milimétrica el texto antiguo por el nuevo.
5. **Verificación:** Ejecuta `read_file` sobre el archivo para comprobar la modificación antes de continuar con la siguiente sección.

---

### Hoja de Ruta de Cláusulas a Tratar:

#### 1. Encabezamiento y Partes Comparecientes
- Nombres completos o razones sociales, NIF/CIF, domicilios para notificaciones y naturaleza jurídica.
- **Condicional Persona Jurídica:**
  - *Si el arrendador es persona jurídica (`V3 = persona_juridica`):* Insertar en su comparecencia: `Representado por: {{nombre_representante}}, con NIF {{nif_representante}}, en calidad de {{cargo_representante}} según escritura de poder.`
  - *Si el arrendatario es persona jurídica (`V4 = persona_juridica`):* Insertar en su comparecencia: `Representado por: {{nombre_representante_arrendatario}}, con NIF {{nif_representante_arrendatario}}, en calidad de {{cargo_representante_arrendatario}} según escritura de poder.`

#### 2. Objeto del Arrendamiento e Inmueble
- Dirección completa (calle, número, piso/puerta, código postal, municipio, provincia), referencia catastral (20 caracteres) y superficie útil en m².
- **Condicional Elementos Accesorios:**
  - *Si incluye anejos (garaje, trastero, mobiliario):* Insertar en la Cláusula Primera: `Se incluyen en el arrendamiento los siguientes elementos accesorios: {{elementos_accesorios}} (plaza de garaje nº X, trastero nº X, mobiliario según inventario anexo).`
  - *Si se arrienda amueblado:* Incluir al final el **Anexo I (Inventario de Mobiliario y Enseres)** con la tabla detallada de bienes y estado de conservación.

#### 3. Destino y Uso
- **Condicional Destino:**
  - *Si `[V1 = vivienda_habitual]`:* Exclusividad residencial permanente, prohibición expresa de cesión turística o subarriendo inconsentido (Art. 8 LAU). Si conviven terceros, añadir: `y de las siguientes personas: {{personas_convivientes}}.`
  - *Si `[V1 = local_comercial]`:* Actividad económica o comercial concreta permitida (`{{actividad_arrendatario}}`), licencias administrativas y régimen de obras (restitución al estado inicial vs conservación de mejoras sin indemnización).

#### 4. Duración, Entrada en Vigor y Prórrogas
- Fecha de inicio, entrega de llaves y duración pactada inicial.
- **Garantía de prórroga obligatoria (Art. 9.1 LAU):**
  - *Si la duración pactada es inferior al mínimo legal (5 años si `V3=persona_fisica`, 7 años si `V3=persona_juridica`):* Redactar e insertar: `De conformidad con el artículo 9.1 de la LAU, al ser la duración pactada inferior a {{plazo_minimo}} años, el contrato se prorrogará obligatoriamente por plazos anuales hasta alcanzar dicho plazo mínimo, salvo que el ARRENDATARIO manifieste su voluntad de no renovarlo con al menos 30 días de antelación a cada vencimiento.`
- **Condicional Zona Tensionada:**
  - *Si el inmueble radica en zona de mercado residencial tensionado:* Insertar la estipulación: `CLÁUSULA ESPECIAL — ZONA DE MERCADO RESIDENCIAL TENSIONADO. El inmueble se ubica en {{municipio_inmueble}}, declarado zona de mercado residencial tensionado conforme a la Ley 12/2023. La prórroga extraordinaria de hasta 3 años prevista en el artículo 10.3 de la LAU será de aplicación a solicitud del ARRENDATARIO.`

#### 5. Renta y Régimen de Pago
- Cuantía mensual de la renta en euros (cifra y letras), plazo de abono (primeros 7 días) y cuenta IBAN.
- **Condicional Zona Tensionada:**
  - *Si radica en zona tensionada:* Añadir la manifestación: `La renta pactada cumple con los límites establecidos en el artículo 17.6 de la LAU, no superando la última renta del contrato anterior en la misma vivienda en los últimos 5 años ({{ultima_renta_anterior}} euros/mes), con la actualización aplicable.`

#### 6. Actualización Anual de la Renta
- Periodicidad anual conforme al índice pactado (IGC o nuevo índice de referencia oficial, con el límite máximo imperativo de variación del IPC, Art. 18 LAU).

#### 7. Fianza Legal y Garantías Complementarias
- **Fianza obligatoria en metálico (Art. 36.1 LAU):** 1 mensualidad si `V1=vivienda_habitual` / 2 mensualidades si `V1=local_comercial`, e indicación del organismo autonómico de depósito (IVIMA, INCASÒL, AVRA, etc.).
- **Condicional Garantías Adicionales:**
  - *Si se pactan garantías adicionales a la fianza:* Redactar e insertar: `GARANTÍA ADICIONAL: las partes acuerdan además {{tipo_garantia_adicional}} (aval bancario / seguro de impago / depósito adicional) por importe de {{importe_garantia_adicional}} euros (máximo legal de 2 mensualidades de renta en vivienda habitual, Art. 36.5 LAU).`

#### 8. Gastos Generales, Tributos y Suministros
- Gastos de formalización y gestión inmobiliaria: **SIEMPRE a cargo del arrendador** si `V1=vivienda_habitual` (Art. 20.1 LAU).
- **Condicional Distribución de Gastos Generales (Comunidad e IBI):**
  - *Opción A (Gastos generales a cargo del arrendatario):* Insertar pacto expreso por escrito: `Las partes acuerdan que los gastos generales del inmueble (cuota de comunidad de propietarios e IBI) sean a cargo del ARRENDATARIO. A la fecha de firma, dichos gastos ascienden a un total de {{importe_gastos_generales_anuales}} euros anuales.`
  - *Opción B (Gastos generales a cargo del arrendador - por defecto):* `Los gastos generales del inmueble (cuota de comunidad, IBI y seguro) son a cargo del ARRENDADOR.`
- Suministros individualizados (agua, luz, gas): a cargo del arrendatario con obligación de cambio de titularidad en plazo de `{{plazo_cambio_titularidad_suministros}}` días.

#### 9. Conservación, Reparaciones y Obras
- Reparaciones de habitabilidad a cargo del arrendador sin elevación de renta (Art. 21.1 LAU). Pequeñas reparaciones ordinarias a cargo del inquilino (Art. 21.4 LAU). Prohibición de obras no consentidas (Art. 23 LAU).

#### 10. Cesión, Subarriendo y Derecho de Adquisición Preferente
- Prohibición total de cesión y subarriendo inconsentido (Art. 8 LAU).
- **Condicional Tanteo y Retracto (Art. 25 LAU):**
  - *Opción A (Sin renuncia):* Mantener derecho de tanteo y retracto legal según Art. 25 LAU.
  - *Opción B (Renuncia expresa pactada):* Redactar e insertar: `El ARRENDATARIO renuncia expresamente al derecho de adquisición preferente establecido en el artículo 25 de la LAU. En caso de venta, el ARRENDADOR comunicará al ARRENDATARIO su intención de vender con al menos 30 días de antelación.`

#### 11. Notificaciones y Fuero Judicial
- Domicilios y direcciones de correo electrónico para notificaciones fehacientes (Art. 4.6 LAU).
- Sumisión obligatoria e imperativa a los Juzgados del lugar de la finca (Art. 38 LAU y Art. 52.1.7º LEC).
- **Condicional Mediación/Arbitraje:**
  - *Si se pacta mediación o arbitraje previo:* Insertar: `Las partes podrán someter sus controversias a mediación o arbitraje conforme al artículo 4.5 de la LAU antes de acudir a la vía judicial.`

#### 12. Pactos Especiales y Cláusulas a Medida
- Insertar cláusulas adicionales pactadas (admisión o prohibición de mascotas, prohibición de fumar, póliza de seguro de hogar, etc.).

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las cláusulas, muestra en el chat el siguiente menú interactivo de opciones finales:

```markdown
El borrador completo del contrato de arrendamiento ha sido redactado y actualizado en disco.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una cláusula existente.
2. Añadir una cláusula adicional a medida.
3. Eliminar una cláusula opcional.
4. Corregir datos de las partes o del inmueble.
5. Dar el contrato por finalizado y cerrar la sesión.
```

### Advertencias Obligatorias al Cerrar:
Cuando el usuario seleccione finalizar el contrato, emite las advertencias legales preceptivas:
1. **Carácter de Borrador (DRAFT):** El documento generado es una propuesta sujeta a revisión por un abogado colegiado antes de su firma.
2. **Depósito Autonómico Obligatorio de Fianza:** Recordar que el arrendador tiene la obligación legal de depositar el importe de la fianza ante el organismo público autonómico competente dentro del plazo legalmente establecido (su omisión acarrea sanciones económicas y recargos).
3. **Registro de la Propiedad:** Recordar la conveniencia de elevar el contrato a escritura pública e inscribirlo en el Registro de la Propiedad para su plena oponibilidad frente a terceros adquirientes (Art. 37 LAU).

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Nulidad de Cláusulas Perjudiciales (Art. 6 LAU):** Si `[V1 = vivienda_habitual]`, son nulas de pleno derecho y se tendrán por no puestas las estipulaciones que modifiquen en perjuicio del arrendatario las normas imperativas del Título II de la LAU. Si el usuario solicita una cláusula ilegal (ej. contrato de vivienda por 1 año sin prórrogas, fianza legal de 3 meses, o que el inquilino pague la comisión de la inmobiliaria), **rechaza la redacción, cita el artículo correspondiente de la LAU y formula la alternativa legal válida**.
2. **Duración Mínima Imperativa (Art. 9.1 LAU):**
   - Si `[V1 = vivienda_habitual]` Y `[V3 = persona_fisica]` $\rightarrow$ Mínimo 5 años.
   - Si `[V1 = vivienda_habitual]` Y `[V3 = persona_juridica]` $\rightarrow$ Mínimo 7 años.
3. **Gastos Inmobiliarios (Art. 20.1 LAU):** Si `[V1 = vivienda_habitual]`, los gastos de gestión inmobiliaria y los de formalización del contrato serán siempre a cargo del arrendador.
4. **Garantías Adicionales (Art. 36.5 LAU):** Si `[V1 = vivienda_habitual]`, en contratos de hasta 5 o 7 años el valor de las garantías adicionales a la fianza no podrá superar dos mensualidades de renta.
5. **Fuero Imperativo (Art. 38 LAU y Art. 52.1.7º LEC):** Las controversias se sustancian obligatoriamente ante los juzgados de la demarcación donde radique la finca. Queda prohibida la sumisión a fueros distintos.
6. **Cero Invención de Datos y Leyes:** Todos los datos reales no aportados deben quedar como `{{DATO_FALTANTE}}`. Nunca inventes números de DNI, referencias catastrales, importes o artículos normativos.


