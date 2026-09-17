---
name: gestoria-impuestos-transmision-inmueble
description: >
  Prepara los dos impuestos que se devengan al transmitir un inmueble en Espana conforme al **Real
  Decreto Legislativo 1/1993**, texto refundido de la Ley del Impuesto sobre Transmisiones
  Patrimoniales y Actos Juridicos Documentados, que grava la adquisicion, y al **Real Decreto
  Legislativo 2/2004**, texto refundido de la Ley Reguladora de las Haciendas Locales, que regula el
  impuesto municipal sobre el incremento de valor de los terrenos de naturaleza urbana.


  Genera tres documentos: la hoja de datos de la autoliquidacion del impuesto de transmisiones
  patrimoniales (modelo 600 autonomico), la hoja de datos de la autoliquidacion o declaracion de la
  plusvalia municipal, y el escrito de solicitud de rectificacion de autoliquidacion y devolucion de
  ingresos indebidos al amparo de la **Ley 58/2003** General Tributaria.


  Aplica el valor de referencia de Catastro como base imponible, compara los dos metodos de calculo de
  la plusvalia (coeficientes objetivos e incremento real) para aplicar el mas favorable, comprueba el
  supuesto de no sujecion cuando no hay incremento de valor, y computa los plazos de presentacion de
  treinta dias habiles en actos entre vivos y de seis meses en las transmisiones por causa de muerte.


  NO usar para transmisiones sujetas a IVA (obra nueva, primera entrega o transmision empresarial), ni
  para el impuesto de sucesiones y donaciones, que corresponde a la skill de liquidacion del impuesto
  de sucesiones, ni para el IRPF de la ganancia patrimonial del vendedor, ni para recursos
  contencioso-administrativos contra liquidaciones.


  Normas aplicadas, en su texto consolidado en el BOE:
  [Ley del ITP y AJD](https://www.boe.es/buscar/act.php?id=BOE-A-1993-25359),
  [Ley Reguladora de las Haciendas Locales](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214) y
  [Ley General Tributaria](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186).
when_to_use: |
  - El usuario ha comprado una vivienda de segunda mano y tiene que liquidar el impuesto de transmisiones.
  - El usuario ha vendido, heredado o recibido en donacion un inmueble y le reclaman la plusvalia municipal.
  - El usuario pregunta cuanto va a pagar por comprar o vender una vivienda y en que plazo.
  - El usuario vendio con perdida o por debajo del precio de compra y quiere saber si debe pagar plusvalia.
  - El usuario pago una plusvalia que considera indebida y quiere solicitar su devolucion.
  - El usuario pregunta que es el valor de referencia de Catastro y como afecta a lo que paga.
inputs:
  - documento: autoliquidacion ITP / plusvalia municipal / solicitud de rectificacion y devolucion (V1)
  - tipo_transmision: onerosa / lucrativa (V2)
  - metodo_calculo_plusvalia: objetivo por coeficientes / incremento real (V3)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - datos_obligado: nombre y apellidos o razon social, NIF/NIE/CIF, domicilio fiscal, telefono y correo
  - datos_transmitente: identidad y NIF de quien transmite
  - datos_adquirente: identidad y NIF de quien adquiere
  - datos_inmueble: direccion completa, referencia catastral, superficie, valor catastral total y del suelo
  - datos_operacion: fecha de la transmision, titulo, notario y numero de protocolo si existe
  - valores: precio o valor declarado y valor de referencia de Catastro
  - fechas_adquisicion_anterior: fecha y valor de la adquisicion anterior del mismo inmueble
  - municipio_y_ordenanza: ayuntamiento competente, tipo de gravamen y coeficientes de la ordenanza
  - comunidad_autonoma: comunidad competente y tipo de gravamen aplicable, con sus bonificaciones
  - motivo_rectificacion: causa por la que se considera indebido el ingreso y su importe
outputs:
  - hoja_datos_itp: hoja de datos para la autoliquidacion del modelo 600 autonomico, DRAFT
  - hoja_datos_plusvalia: hoja de datos de la plusvalia municipal con los dos metodos comparados, DRAFT
  - solicitud_rectificacion: escrito de rectificacion de autoliquidacion y devolucion de ingresos indebidos, DRAFT
  - checklist_plazos_y_documentos: documentos, sede de presentacion y computo de plazos de cada impuesto
references:
  - references/itp-base-imponible-y-valor-referencia.md
  - references/plusvalia-municipal-metodos-y-no-sujecion.md
  - references/estilo-redaccion-escritos-tributarios.md
assets:
  - assets/template-hoja-datos-itp-modelo-600.md
  - assets/template-hoja-datos-plusvalia-municipal.md
  - assets/template-solicitud-rectificacion-devolucion.md
---

# Impuestos de la Transmisión de un Inmueble (ITP y Plusvalía Municipal)

> DRAFT — para revisión por un gestor o asesor colegiado antes de su presentación. No constituye asesoramiento profesional vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar la liquidación de los impuestos que se devengan al transmitir un inmueble.

### Vectores de Estado (Uso Estrictamente Interno):
- **V1 (Documento):** `itp_modelo_600` | `plusvalia_iivtnu` | `rectificacion_devolucion` | `transmision_sujeta_iva`.
- **V2 (Tipo de Transmisión):** `onerosa` | `lucrativa`.
- **V3 (Método de Cálculo de la Plusvalía):** `objetivo_coeficientes` | `incremento_real`.
- **origen_plantilla:** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

Tu primer objetivo es determinar qué impuesto se liquida y en qué concepto.

### 1.1 Apertura Inmediata y Escucha Activa Previa
En el mismo turno en que se activa la skill, sin detenerte a esperar ninguna reacción del usuario, actúa de inmediato:
1. **Anuncio de Apertura (Vía Chat):** Envía primero un mensaje breve y cordial, en el registro formal de un gestor administrativo (de usted), confirmando que vais a preparar la liquidación de los impuestos de la transmisión del inmueble.
2. **Escucha Activa:** Evalúa en ese mismo turno el mensaje inicial del usuario y el historial de la conversación:
   - Si el usuario ya indicó de forma inequívoca qué impuesto necesita liquidar y si la transmisión es a título oneroso o gratuito, registra los vectores en silencio y avanza directamente a la **Fase 2**.
   - Si falta determinar el documento (`V1`) o el tipo de transmisión (`V2`), invoca ya en ese mismo turno, junto con el anuncio de apertura, la herramienta `restricted_human_in_the_loop_request`. No emitas el anuncio como mensaje aislado a la espera de que el usuario reaccione: el anuncio y el formulario de clasificación viajan juntos, en el mismo turno.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "documento",
      "rationale": "Resolver V1 para determinar cual de los dos impuestos se liquida o si se reclama una devolucion.",
      "question": "¿Qué necesita preparar?",
      "options": [
        {"id": "itp_modelo_600", "label": "Impuesto de transmisiones patrimoniales por la compra del inmueble (modelo 600)"},
        {"id": "plusvalia_iivtnu", "label": "Plusvalía municipal por la transmisión del inmueble"},
        {"id": "rectificacion_devolucion", "label": "Reclamar la devolución de un impuesto que ya pagó y considera indebido"},
        {"id": "transmision_sujeta_iva", "label": "Es obra nueva, primera entrega o una transmisión entre empresas sujeta a IVA"}
      ]
    },
    {
      "id": "tipo_transmision",
      "rationale": "Resolver V2: en las transmisiones onerosas el sujeto pasivo de la plusvalia es el transmitente y en las lucrativas el adquirente.",
      "question": "¿Cómo se ha transmitido el inmueble?",
      "options": [
        {"id": "onerosa", "label": "A título oneroso (compraventa, permuta, dación en pago)"},
        {"id": "lucrativa", "label": "A título gratuito (herencia o donación)"}
      ]
    },
    {
      "id": "metodo_calculo_plusvalia",
      "rationale": "Resolver V3: el contribuyente puede optar por el metodo que le resulte mas favorable.",
      "question": "Si es plusvalía municipal, ¿conoce el valor por el que se adquirió antes el inmueble, para poder comparar el incremento real con el cálculo por coeficientes?",
      "options": [
        {"id": "incremento_real", "label": "Sí, dispongo de la escritura de adquisición anterior"},
        {"id": "objetivo_coeficientes", "label": "No, o prefiero el cálculo por coeficientes sobre el valor catastral"},
        {"id": "no_procede", "label": "No procede: el trámite no es la plusvalía municipal (es ITP modelo 600 o rectificación)"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `documento`
- `V2` — `tipo_transmision`
- `V3` — `metodo_calculo_plusvalia`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V1 = transmision_sujeta_iva`:**
  - **DETENER.** Informar de que la primera entrega de vivienda por promotor y las transmisiones empresariales tributan por IVA y por la modalidad de actos jurídicos documentados, con reglas de renuncia a la exención y de inversión del sujeto pasivo que esta skill no cubre. Derivar a asesor fiscal. No crear documento.
- **Si `V1 = itp_modelo_600`:**
  - Hoja de datos del sistema: `assets/template-hoja-datos-itp-modelo-600.md`. Proceder a la **Fase 2**.
- **Si `V1 = plusvalia_iivtnu`:**
  - Hoja de datos del sistema: `assets/template-hoja-datos-plusvalia-municipal.md`. Proceder a la **Fase 2**.
- **Si `V1 = rectificacion_devolucion`:**
  - Escrito del sistema: `assets/template-solicitud-rectificacion-devolucion.md`. Proceder a la **Fase 2**.
- `V2` no elige plantilla: determina quién es el obligado tributario de la plusvalía y el plazo de presentación aplicable.
- `V3` no elige plantilla: determina si se calculan y comparan los dos métodos de la plusvalía o solo el objetivo.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `itp-base-imponible-y-valor-referencia.md`, `plusvalia-municipal-metodos-y-no-sujecion.md` y `estilo-redaccion-escritos-tributarios.md`.
2. Verifica **obligatoriamente** mediante `web_search` el tipo de gravamen vigente del impuesto de transmisiones en la comunidad autónoma competente y sus bonificaciones, así como el tipo y los coeficientes de la ordenanza fiscal del ayuntamiento en el caso de la plusvalía. Ambos son autonómicos y municipales y cambian con frecuencia: nunca los des por conocidos. Si detectas modificaciones, aplica la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Plazos Aplicables:**
   - Para el impuesto de transmisiones: explicar que el sujeto pasivo es el adquirente, que la base imponible es el valor de referencia de Catastro salvo que el precio declarado sea superior, que el tipo lo fija la comunidad autónoma, y que el plazo de presentación es de **treinta días hábiles** desde la fecha del documento.
   - Para la plusvalía municipal: explicar que grava el incremento de valor del suelo urbano, que el obligado es el transmitente en las transmisiones onerosas y el adquirente en las gratuitas, que existen **dos métodos de cálculo** y puede aplicarse el que resulte más favorable, que **no hay sujeción si no hubo incremento de valor**, y que el plazo es de treinta días hábiles en actos entre vivos y de **seis meses** prorrogables a un año en las transmisiones por causa de muerte.
   - Para la solicitud de devolución: explicar el plazo de prescripción de cuatro años y advertir de que las autoliquidaciones que ya adquirieron firmeza antes de la sentencia del Tribunal Constitucional sobre el método de cálculo de la plusvalía no pueden revisarse por ese motivo.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Mencionar por su denominación formal la hoja o escrito (sin mostrar rutas internas ni volcar su contenido) **que ha resuelto el enrutamiento de la Fase 1.3**. **No propongas una plantilla distinta de la enrutada.**
3. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
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

### Hoja de Ruta de Secciones — RAMA IMPUESTO DE TRANSMISIONES:

1. **Obligado tributario y presentador** *(confirmación agrupada)*: identidad del adquirente con su NIF/NIE, domicilio fiscal, teléfono y correo, y datos del presentador o representante si difiere.
2. **Transmitente y título de la operación**: identidad y NIF del transmitente, fecha del documento, notario y número de protocolo, y naturaleza del negocio.
3. **Identificación del inmueble**: dirección completa, referencia catastral, superficie, valor catastral y, en su caso, anejos y cuota de participación.
4. **Base imponible**: comparación entre el precio declarado y el valor de referencia de Catastro, con aplicación del mayor de los dos, y explicación de que el valor de referencia puede impugnarse por el cauce de la rectificación si se considera superior al valor de mercado.
5. **Tipo de gravamen, bonificaciones y cuota**: tipo autonómico verificado, aplicación de tipos reducidos si concurren los requisitos (vivienda habitual, edad, familia numerosa, discapacidad, según la comunidad) y cálculo de la cuota resultante.
6. **Presentación y plazos**: sede de presentación de la comunidad autónoma, forma telemática, documentación a adjuntar y cómputo expreso del plazo de treinta días hábiles con su fecha límite.

### Hoja de Ruta de Secciones — RAMA PLUSVALÍA MUNICIPAL:

1. **Obligado tributario según el tipo de transmisión** *(confirmación agrupada)*: identidad y NIF del obligado, que será el transmitente en la transmisión onerosa y el adquirente en la gratuita, con su domicilio y datos de contacto.
2. **Inmueble y datos catastrales**: referencia catastral, dirección, valor catastral total y **valor catastral del suelo** en la fecha del devengo, que es la base del cálculo objetivo.
3. **Fechas y periodo de generación**: fecha de la adquisición anterior y fecha de la transmisión actual, con determinación de los años completos de tenencia y la advertencia de que los periodos inferiores al año también tributan.
4. **Comprobación de no sujeción**: comparación entre el valor de adquisición y el de transmisión. *Condicional ausencia de incremento:* si no hubo incremento de valor, redactar la declaración de no sujeción con la aportación de ambos títulos como prueba, en lugar de la autoliquidación.
5. **Cálculo por los dos métodos**: *Condicional `V3 = incremento_real`:* cálculo del incremento real imputable al suelo mediante la proporción del valor catastral del suelo sobre el total, y cálculo objetivo mediante el coeficiente del periodo, aplicando el resultado más favorable y dejando constancia de la comparación. *Condicional `V3 = objetivo_coeficientes`:* cálculo objetivo con el coeficiente vigente de la ordenanza.
6. **Bonificaciones, cuota y presentación**: bonificaciones de la ordenanza municipal, en particular la de transmisiones mortis causa de la vivienda habitual a favor de descendientes o cónyuge, cuota resultante, sede del ayuntamiento y cómputo del plazo aplicable.

### Hoja de Ruta de Secciones — RAMA RECTIFICACIÓN Y DEVOLUCIÓN:

1. **Solicitante y acto que se impugna** *(confirmación agrupada)*: identidad y NIF del solicitante, administración a la que se dirige, identificación de la autoliquidación o liquidación (número, fecha, importe ingresado y concepto).
2. **Hechos**: relato cronológico de la transmisión, del ingreso realizado y de la circunstancia que lo convierte en indebido.
3. **Fundamentos jurídicos**: invocación de la rectificación de autoliquidaciones y de la devolución de ingresos indebidos de la Ley General Tributaria, y del motivo material concreto (ausencia de incremento de valor, error en la base imponible, aplicación de método de cálculo más gravoso, bonificación no aplicada o valor de referencia superior al de mercado).
4. **Prescripción y firmeza**: cómputo del plazo de cuatro años y advertencia expresa sobre la imposibilidad de revisar situaciones ya firmes por el motivo de inconstitucionalidad del método objetivo.
5. **Solicitud, intereses y documentación**: petición de rectificación, de devolución del importe y de los intereses de demora desde la fecha del ingreso, cuenta bancaria para la devolución y relación de documentos que se acompañan.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa Obligatoria:** los tipos de gravamen y los coeficientes son autonómicos y municipales. Está prohibido consignar un tipo o un coeficiente sin haberlo verificado en la fuente oficial correspondiente en esta misma sesión.
2. **Cero Invención de Datos:** prohibido inventar referencias catastrales, valores catastrales, valores de referencia, tipos, coeficientes o números de expediente. Todo dato no confirmado permanece como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** aplicar novedades normativas o de ordenanza en el borrador del workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** no liquidar operaciones sujetas a IVA, ni el impuesto de sucesiones y donaciones, ni el IRPF de la ganancia patrimonial, ni interponer recursos contencioso-administrativos, que deben derivarse a asesor fiscal o letrado.
