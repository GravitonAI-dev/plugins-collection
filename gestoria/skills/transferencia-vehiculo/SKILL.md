---
name: transferencia-vehiculo
description: >
  Prepara el tramite administrativo de cambio de titularidad (transferencia) de un vehiculo usado ante
  la DGT y, en su caso, la notificacion de venta por el vendedor, conforme al **Reglamento General de Vehiculos (RD 2822/1998)**, que regula la matriculacion y los cambios de titularidad de los vehiculos, en su texto consolidado verificado en el BOE y a la normativa de tasas de la DGT.
  Opera bajo el flujo de 5 fases canonicas con clasificacion HITL, consulta de assets, creacion zero-vacios
  en workspace y edicion incremental seccion a seccion. Genera el contrato de compraventa, la hoja de datos
  para la solicitud en la DGT, la notificacion de venta y el checklist de documentos, tasas y liquidacion
  del ITP autonomico (modelo 620/621). NO usar para vehiculos nuevos, matriculaciones iniciales, bajas
  definitivas por desguace, duplicados de permiso, ni para transmisiones en compraventa profesional en
  regimen de existencias.
when_to_use: |
  - Un particular compra o vende un vehiculo usado y necesita cambiar la titularidad en la DGT.
  - El usuario quiere el contrato de compraventa del vehiculo y la hoja de datos del tramite.
  - El vendedor quiere notificar la venta a la DGT para dejar de figurar como titular.
  - El usuario pide el checklist de documentos, tasas y organismo para presentar la transferencia.
inputs:
  - tipo_tramite_dgt: cambio_titularidad / notificacion_venta / ambos_tramites (V1)
  - tipo_vehiculo: turismo / motocicleta / ciclomotor / vehiculo_comercial (V2)
  - naturaleza_vendedor: persona_fisica / persona_juridica (V3)
  - naturaleza_comprador: persona_fisica / persona_juridica (V4)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_vehiculo: matricula, numero de bastidor (VIN), marca, modelo, fecha de primera matriculacion
  - datos_vendedor: nombre o razon social, NIF o CIF, domicilio
  - datos_comprador: nombre o razon social, NIF o CIF, domicilio
  - precio: precio de venta pactado en euros y fecha de la transmision
  - comunidad_autonoma: comunidad autonoma del comprador a efectos del ITP
  - estado_itv: si el vehiculo tiene la ITV en vigor (si / no / no aplica)
outputs:
  - contrato_compraventa: contrato de compraventa del vehiculo en markdown, DRAFT
  - solicitud_cambio_titularidad: hoja de datos + checklist + organismo + tasa para la solicitud DGT, DRAFT
  - notificacion_venta: opcional, escrito de notificacion de venta del vendedor a la DGT, DRAFT
references:
  - references/dgt-cambio-titularidad.md
  - references/itp-vehiculos-usados.md
  - references/fuentes-y-tasas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-contrato-compraventa-vehiculo.md
  - assets/template-solicitud-cambio-titularidad-dgt.md
  - assets/template-notificacion-venta-dgt.md
---

# Preparar el Cambio de Titularidad de un Vehículo (DGT)

> DRAFT — para revisión por un gestor administrativo o profesional habilitado antes de su presentación telemática o presencial. No constituye asesoramiento legal vinculante ni sustituye la tramitación oficial ante la DGT ni la Agencia Tributaria autonómica.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar la transmisión de vehículos usados, el contrato de compraventa y los formularios de la Dirección General de Tráfico (DGT).

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y el cumplimiento de la normativa de tráfico y tributaria, el asistente resuelve y mantiene internamente en memoria los siguientes vectores de estado:
- **V1 (Tipo de Trámite DGT):** `cambio_titularidad` | `notificacion_venta` | `ambos_tramites`.
- **V2 (Tipo de Vehículo):** `turismo` | `motocicleta` | `ciclomotor` *(tasa reducida)* | `vehiculo_comercial`.
- **V3 (Naturaleza del Vendedor):** `persona_fisica` | `persona_juridica`.
- **V4 (Naturaleza del Comprador):** `persona_fisica` | `persona_juridica`.
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas (por ejemplo, anotar un vector como resuelto) son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es identificar el alcance del encargo (cambio de titularidad por el comprador, notificación de venta por el vendedor o ambos) y el tipo de vehículo.

### 1.1 Escucha Activa Previa
Antes de invocar formularios, evalúa el mensaje inicial del usuario:
- Si el usuario ya precisó el tipo de vehículo y si actúa como comprador o vendedor requiriendo contrato y solicitud, registra los vectores y avanza a la **Fase 2**.
- Si falta delimitar el alcance del trámite (`V1`) o el tipo de vehículo (`V2`), invoca de inmediato la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las opciones de triaje:

```json
{
  "form_data": [
    {
      "id": "tipo_tramite_dgt",
      "rationale": "Resolver V1 para determinar qué documentos de la DGT y contractuales deben generarse.",
      "question": "¿Qué trámite desea preparar ante la DGT?",
      "options": [
        {"id": "ambos_tramites", "label": "Trámite completo: contrato de compraventa y solicitud de cambio de titularidad"},
        {"id": "cambio_titularidad", "label": "Solo solicitud de cambio de titularidad (el comprador transfiere a su nombre)"},
        {"id": "notificacion_venta", "label": "Notificación de venta en DGT (el vendedor notifica la entrega del vehículo)"}
      ]
    },
    {
      "id": "tipo_vehiculo",
      "rationale": "Resolver V2 para aplicar la tasa oficial correcta de la DGT.",
      "question": "¿Qué tipo de vehículo se transmite?",
      "options": [
        {"id": "turismo", "label": "Turismo, furgoneta o vehículo comercial (Tasa ordinaria 4.1)"},
        {"id": "motocicleta", "label": "Motocicleta (Tasa ordinaria 4.1)"},
        {"id": "ciclomotor", "label": "Ciclomotor (Tasa reducida 4.4)"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `tipo_tramite_dgt`
- `V2` — `tipo_vehiculo`
- `V3` — naturaleza del vendedor: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo
- `V4` — naturaleza del comprador: no se pregunta en el formulario de clasificación; se resuelve durante el propio flujo

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- Plantillas del sistema propuestas:
  - Si `V1 = ambos_tramites`: `assets/template-contrato-compraventa-vehiculo.md`, `assets/template-solicitud-cambio-titularidad-dgt.md` y `assets/template-notificacion-venta-dgt.md`.
  - Si `V1 = cambio_titularidad`: `assets/template-contrato-compraventa-vehiculo.md` y `assets/template-solicitud-cambio-titularidad-dgt.md`.
  - Si `V1 = notificacion_venta`: `assets/template-notificacion-venta-dgt.md`.
- Proceder a la **Fase 2**.
- `V2` no elige hoja: determina la tasa oficial de la DGT aplicable.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `dgt-cambio-titularidad.md`, `itp-vehiculos-usados.md`, `fuentes-y-tasas.md` y `estilo-redaccion-escritos.md`.
2. Opcionalmente verifica mediante `web_search` las tasas vigentes de la DGT (Tasa 4.1 para vehículos en general o Tasa 4.4 para ciclomotores, y Tasa 4.1 para notificación de venta). Si detectas variaciones, aplica directamente las tasas vigentes sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Normativo y Requisitos Previos (DGT y Fiscales):**
   - Citar el Reglamento General de Vehículos (RD 2822/1998, arts. 32 y 33).
   - Requisitos habilitantes imperativos: El vehículo debe estar al corriente del Impuesto sobre Vehículos de Tracción Mecánica (IVTM del año anterior pagado en el municipio), no tener reservas de dominio (financieras), precintos judiciales ni embargos inscritos en el Registro de Bienes Muebles, y contar con ITV en vigor para expedir el permiso definitivo.
   - Liquidación obligatoria del Impuesto sobre Transmisiones Patrimoniales (ITP - Modelo 620 o 621 telemático) ante la Comunidad Autónoma del comprador antes de la DGT.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Presentar los modelos oficiales seleccionados.
   - Nombra por su ruta la hoja **que ha resuelto el enrutamiento de la Fase 1.3**; si el enrutamiento asigno varias, nombralas todas y en el orden en que se van a rellenar. **No propongas una hoja distinta de la enrutada.**
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
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

### Hoja de Ruta de Secciones:

1. **Identificación de Vendedor y Comprador** *(confirmación agrupada)*:
   - Nombre completo o razón social, NIF/CIF, domicilio completo a efectos de notificaciones y condición de persona física o jurídica (con facultades de representación).
2. **Datos Identificativos del Vehículo** *(confirmación agrupada)*:
   - Matrícula, número de bastidor (VIN de 17 caracteres), marca, modelo exacto, kilometraje real declarado y fecha de primera matriculación.
3. **Condiciones Económicas y Pago del Precio**:
   - Precio pactado de compraventa en euros.
   - Medio de pago (transferencia bancaria, cheque o efectivo dentro del límite legal).
   - Advertencia sobre tablas mínimas de valoración de Hacienda para la autoliquidación del ITP.
4. **Estado Técnico, Cargas y Garantías**:
   - Estado de la ITV (favorable en vigor o no apto).
   - Manifestación expresa del vendedor de estar al corriente del pago del IVTM y de que el vehículo se encuentra libre de cargas, embargos o reservas de dominio.
   - Régimen de vicios ocultos (garantía de 6 meses entre particulares conforme al Código Civil).
5. **Entrega del Vehículo, Documentación y Plazos**:
   - Fecha, hora y lugar exactos de la entrega del vehículo, llaves y permiso de circulación original.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **ITV e IVTM Preceptivos:** Advertir expresamente de que si el vehículo no tiene la ITV en vigor, la DGT tramitará el cambio pero retendrá el permiso de circulación definitivo emitiendo únicamente una notificación de transferencia provisional.
2. **Cero Invención de Datos:** No inventar matrículas, números de bastidor ni NIFs. Todo dato pendiente debe permanecer como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** Aplicar cualquier variación en tasas o modelos DGT directamente en el workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** No tramitar vehículos adquiridos en subastas judiciales, vehículos diplomáticos, ni matriculaciones ordinarias o de importación, que deben remitirse a gestorías administrativas especializadas.
