---
name: alta-baja-autonomo
description: >
  Prepara el alta y la baja de trabajador autonomo en Espana: (1) el alta o la baja censal en la AEAT
  mediante el modelo 036 (declaracion censal en el censo de empresarios, profesionales y retenedores;
  en el alta con epigrafe IAE y eleccion de regimen de IVA e IRPF; en la baja con la fecha efectiva de
  cese y sus efectos en IVA e IRPF) y (2) el alta o la baja en el RETA de la Seguridad Social (en el alta,
  eleccion de base segun rendimientos netos previstos y tarifa plana; en la baja, comunicacion del cese
  y efectos en la cuota), conforme a la Ley 20/2007 (LETA) y al RD-ley 13/2022 en su version consolidada
  verificada en el BOE. Opera bajo el flujo de 5 fases canonicas con clasificacion HITL, consulta de assets,
  creacion zero-vacios en workspace y edicion incremental seccion a seccion. NO usar para altas ni bajas de
  sociedades mercantiles (SL/SA), autonomos societarios o colaboradores sin revision letrada, ni para el calculo
  definitivo de cuotas ni para la presentacion telematica automatica ante la sede electronica.
when_to_use: |
  - El usuario va a darse de alta como autonomo (trabajador por cuenta propia) por primera vez o de nuevo.
  - El usuario va a cesar su actividad y darse de baja como autonomo (baja censal 036 y baja en el RETA).
  - El usuario necesita preparar el modelo 036 (alta o baja censal en Hacienda) y el alta o la baja en el RETA.
  - El usuario quiere saber que epigrafe IAE, regimen de IVA/IRPF y tramo de cuota le corresponden.
  - El usuario pregunta por la tarifa plana, los plazos de alta o de baja, los efectos del cese en la cuota o la documentacion necesaria.
inputs:
  - tipo_operacion: alta / baja (V1)
  - tipo_actividad: empresarial / profesional / artistica (V2)
  - naturaleza_titular: persona_fisica (V3)
  - regimen_cotizacion: reta_general / reta_tarifa_plana / reta_societario_colaborador (V4)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - datos_interesado: nombre y apellidos, NIF, domicilio fiscal, telefono y correo de contacto
  - actividad: descripcion de la actividad economica (alta que va a ejercer; baja que cesa)
  - epigrafe_iae: epigrafe del IAE si lo conoce (empresarial o profesional)
  - fecha_inicio: fecha prevista de inicio de la actividad (solo para el alta)
  - fecha_cese: fecha de cese de la actividad (solo para la baja)
  - rendimientos_previstos: rendimientos netos mensuales previstos en euros (alta para el tramo de cotizacion)
  - regimen_iva: regimen de IVA aplicable (general / recargo de equivalencia / exento) si lo conoce
  - regimen_irpf: metodo de estimacion de IRPF (directa simplificada / directa normal / objetiva-modulos)
  - tarifa_plana: si cumple los requisitos de la cuota reducida de inicio de actividad (si / no / desconocido)
  - domicilio_actividad: lugar donde ejerce la actividad, si difiere del domicilio fiscal
  - obligaciones_pendientes: declaraciones o cuotas del periodo aun no presentadas (baja para el aviso de cierre fiscal)
outputs:
  - hoja_datos_alta_censal: hoja de datos para el alta en el modelo 036 con epigrafe IAE y regimenes, DRAFT
  - hoja_datos_alta_reta: hoja de datos para el alta en RETA con tramo y cuota estimada, DRAFT
  - hoja_datos_baja_censal: hoja de datos para la baja en el modelo 036 con fecha de cese y efectos en IVA/IRPF, DRAFT
  - hoja_datos_baja_reta: hoja de datos para la baja en el RETA con fecha de cese y efectos en la cuota, DRAFT
  - checklist_documentos: relacion de documentos, sedes y plazos de cada tramite
references:
  - references/censo-036-037-aeat.md
  - references/reta-cotizacion-ingresos-reales.md
  - references/fuentes-y-plazos.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-hoja-datos-alta-censal-036.md
  - assets/template-hoja-datos-alta-reta.md
  - assets/template-hoja-datos-baja-censal-036.md
  - assets/template-hoja-datos-baja-reta.md
---

# Preparar el Alta o la Baja de Trabajador Autónomo (Censal AEAT + RETA)

> DRAFT — para revisión por un gestor administrativo o asesor colegiado antes de su presentación oficial. No constituye asesoramiento fiscal vinculante ni representación técnica ante la AEAT o la TGSS.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar la documentación de alta o baja en Hacienda (Modelo 036) y la Seguridad Social (RETA).

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y el cumplimiento de las normas tributarias y laborales, el asistente resuelve y mantiene internamente en memoria los siguientes vectores de estado:
- **V1 (Tipo de Operación):** `alta` | `baja`.
- **V2 (Tipo de Actividad):** `empresarial` | `profesional` | `artistica`.
- **V3 (Naturaleza del Titular):** `persona_fisica` (autónomo individual).
- **V4 (Régimen de Cotización / Bonificación):** `reta_general` | `reta_tarifa_plana` | `reta_societario_colaborador` *(fuera de alcance directo / advertencia)*.
- **V5 (Origen Plantilla / Asset):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas técnicas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es determinar el tipo de trámite y el encuadre operativo.

### 1.1 Escucha Activa Previa
Antes de invocar formularios, evalúa el mensaje inicial del usuario:
- Si el usuario ya indicó de forma inequívoca si desea tramitar un alta o una baja, su actividad y si solicita tarifa plana, registra los vectores en silencio y avanza a la **Fase 2**.
- Si falta determinar la operación principal (`V1`) o el encuadre de cotización (`V4`), invoca de inmediato la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de triaje:

```json
{
  "form_data": [
    {
      "id": "tipo_operacion",
      "rationale": "Resolver V1 para determinar si se preparan los trámites de inicio o cese de actividad.",
      "question": "¿Qué trámite desea preparar?",
      "options": [
        {"id": "alta", "label": "Alta de autónomo (inicio de actividad censal y RETA)"},
        {"id": "baja", "label": "Baja de autónomo (cese de actividad censal y RETA)"}
      ]
    },
    {
      "id": "tipo_actividad",
      "rationale": "Resolver V2 para delimitar la naturaleza del epígrafe IAE y retenciones de IRPF.",
      "question": "¿Qué naturaleza tiene la actividad económica?",
      "options": [
        {"id": "profesional", "label": "Actividad profesional (servicios personales, sujeta a retención)"},
        {"id": "empresarial", "label": "Actividad empresarial (comercio, hostelería, industria, sin retención directa)"}
      ]
    },
    {
      "id": "regimen_cotizacion",
      "rationale": "Resolver V4 para determinar el régimen de cuotas en RETA.",
      "question": "¿Opta a la tarifa plana (cuota reducida inicial) o cotiza por tramos de rendimientos reales?",
      "options": [
        {"id": "reta_tarifa_plana", "label": "Tarifa plana (primer alta o más de 2 años sin alta en RETA)"},
        {"id": "reta_general", "label": "Régimen general de cotización por tramos según rendimientos previstos"},
        {"id": "reta_societario_colaborador", "label": "Autónomo societario o familiar colaborador"}
      ]
    }
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- **Si `V4 = reta_societario_colaborador`:**
  - Informar de que los autónomos societarios (administradores de SL/SA) y colaboradores tienen reglas de cotización, bases mínimas y trámites censales específicos que requieren revisión personalizada de escrituras y estatutos. Ofrecer derivar a gestor colegiado o continuar con las advertencias preceptivas.
- **Si `V1 = alta`:**
  - Hojas de datos propuestas del sistema: `assets/template-hoja-datos-alta-censal-036.md` y `assets/template-hoja-datos-alta-reta.md`. Proceder a la **Fase 2**.
- **Si `V1 = baja`:**
  - Hojas de datos propuestas del sistema: `assets/template-hoja-datos-baja-censal-036.md` y `assets/template-hoja-datos-baja-reta.md`. Proceder a la **Fase 2**.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `censo-036-037-aeat.md`, `reta-cotizacion-ingresos-reales.md` y `fuentes-y-plazos.md`.
2. Opcionalmente verifica mediante `web_search` las tablas de bases y tramos del RETA del ejercicio en curso o novedades en los modelos censales 036/037 de la AEAT. Si detectas modificaciones normativas, aplica directamente la redacción vigente sobre los documentos del workspace del usuario sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Plazos Aplicables:**
   - Para ALTA: Explicar que el alta censal (modelo 036) debe presentarse en la AEAT **antes** del inicio material de la actividad, y el alta en el RETA puede solicitarse en Import@ss hasta 60 días antes del inicio.
   - Para BAJA: Explicar que la baja en el RETA debe comunicarse en Import@ss en los **3 días naturales** siguientes al cese, y la baja censal en la AEAT en el plazo de **1 mes**.
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Detallar que dispones de las hojas de datos estructuradas oficiales para volcar la información requerida por la Sede Electrónica de la AEAT y el portal Import@ss de la Seguridad Social.
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
- **Si `V5 = plantilla_sistema`:** Utiliza los assets oficiales correspondientes y avanza a la **Fase 3**.
- **Si `V5 = plantilla_usuario`:** Toma la plantilla adjunta en `<attached_documents>` o el texto pegado en `<user_message>`, valida que cumpla las normas tributarias y laborales imperativas, y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura de los Documentos (`create_file`):**
   - Vuelca íntegramente las plantillas acordadas en el workspace del usuario:
     - En ALTA: `hoja_datos_alta_censal_036.md` y `hoja_datos_alta_reta.md`.
     - En BAJA: `hoja_datos_baja_censal_036.md` y `hoja_datos_baja_reta.md`.
   - Aplica el principio **Zero-Omission**:
     - Sustituye los datos ya conocidos de la clasificación (tipo de trámite, epígrafe general, tarifa plana).
     - Todos los datos pendientes deben permanecer como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves.
     - PROHIBIDO dejar archivos en blanco o con notas resumidas.
2. **Validación de Disco (`read_file`):**
   - Ejecuta `read_file` sobre los archivos creados para confirmar su integridad física en disco.
3. **Confirmación en Chat:**
   - Informa al usuario de la ruta de los archivos generados e introduce de inmediato la primera sección de la **Fase 4** sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques de datos. Para cada bloque, ejecuta estrictamente el ciclo interactivo:
```
[Pregunta al Usuario] ──> [Vista Previa en texto plano] ──> [¿Confirmamos esta sección?] ──> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Pregunta en Chat:** Solicita los datos específicos del bloque orientando sobre las opciones tributarias o de cotización.
2. **Vista Previa (Preview):** Muestra el texto redactado en texto plano (sin backticks de código).
3. **Confirmación:** Pregunta literalmente: `¿Confirmamos esta sección?`.
4. **Persistencia en Disco:** Tras la confirmación, aplica `edit_file` con coincidencia exacta y verifica inmediatamente con `read_file`.

### Hoja de Ruta de Secciones — RAMA ALTA:

1. **Identificación del Titular** *(confirmación agrupada)*:
   - Nombre completo, NIF/NIE, domicilio fiscal completo, teléfono y correo electrónico para notificaciones telemáticas.
2. **Actividad Económica y Epígrafe IAE**:
   - Descripción detallada de la actividad y código IAE (empresarial o profesional).
   - *Condicional actividades múltiples:* Si realiza más de una actividad, incluir epígrafes secundarios y desglosar el régimen de cada una.
   - Domicilio afecto a la actividad (si difiere del domicilio fiscal o si trabaja desde el domicilio habitual con porcentaje afecto).
3. **Régimen Tributario (IVA e IRPF)**:
   - IVA: Régimen general, recargo de equivalencia (comercio minorista persona física), régimen simplificado o exención médica/educativa.
   - IRPF: Estimación directa simplificada (la general hasta 600.000 € de cifra de negocios), estimación directa normal o módulos.
   - Pagos fraccionados: Modelos trimestrales aplicables (Modelo 303 de IVA, Modelo 130 de IRPF o exención si retiene más del 70% de sus ingresos en actividad profesional).
4. **Cotización en el RETA (Seguridad Social)**:
   - Fecha exacta de inicio de la actividad económica.
   - *Condicional Tarifa Plana:* Si aplica, consignar la cuota reducida de inicio durante los primeros 12 meses y requisitos de prórroga al segundo año.
   - *Condicional Régimen General por Rendimientos:* Previsión de rendimientos netos mensuales, encuadre en el tramo de la tabla de cotización vigente, base elegida y cuota mensual estimada. Advertencia expresa de regularización anual por la TGSS.
5. **Datos Bancarios y Formalización**:
   - Código IBAN para la domiciliación bancaria de las cuotas del RETA.

### Hoja de Ruta de Secciones — RAMA BAJA:

1. **Identificación del Titular** *(confirmación agrupada)*:
   - Nombre completo, NIF/NIE y domicilio fiscal registrado.
2. **Alcance del Cese y Actividades**:
   - Delimitación de si se trata de un cese total de actividad (baja censal y RETA) o un cese parcial de un epígrafe manteniendo otros activos (solo modificación censal 036, sin baja RETA).
3. **Fecha Efectiva de Cese y Plazos**:
   - Fecha exacta del cese de actividad.
   - Validación del cómputo de plazos: 3 días naturales para el RETA (aviso de efectos en cuota: las 3 primeras bajas del año cotizan por días reales; a partir de la 4ª mes completo) y 1 mes para la AEAT.
4. **Régimen Fiscal de Cierre y Obligaciones Pendientes**:
   - Inventario de últimas declaraciones tributarias obligatorias a presentar tras el cese (Modelo 303 y 390 de IVA, Modelo 130/131 y Renta de IRPF, Modelos 111/190 de retenciones).
   - Constancia de que la baja no extingue deudas tributarias pendientes ni la obligación de conservar libros y facturas durante 4 años.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones de las hojas de datos, presenta al usuario el menú interactivo:
```markdown
Las hojas de datos y checklists para la gestión del trámite han sido generadas y actualizadas en disco.

Seleccione una opción si desea realizar ajustes adicionales:
1. Ajustar o modificar una sección (epígrafe IAE, tramo de cotización, fechas o datos identificativos).
2. Añadir información sobre una actividad complementaria o local afecto.
3. Modificar el régimen tributario seleccionado (IVA / IRPF).
4. Revisar la coherencia global y realizar control de calidad previo a la presentación.
5. Dar las hojas de datos por finalizadas y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
Al dar por concluido el trámite, emite siempre las siguientes advertencias:
1. **Carácter DRAFT:** Los documentos generados son hojas de datos preparatorias para facilitar la cumplimentación telemática; deben ser validadas por un gestor administrativo o asesor fiscal antes de confirmar los trámites oficiales.
2. **Plazos Imperativos de Presentación:**
   - ALTA: Presentar el Modelo 036 en la AEAT **antes** de iniciar operaciones facturables. El alta en RETA debe formalizarse en Import@ss antes o el mismo día del inicio.
   - BAJA: Comunicar la baja en RETA en Import@ss dentro de los **3 días naturales** posteriores al cese. Presentar la baja censal en la AEAT dentro del **mes siguiente**.
3. **Carácter Estimado de las Cuotas:** Las bases y cuotas del RETA calculadas son provisionales y orientativas; la Seguridad Social practicará una regularización anual obligatoria en el ejercicio siguiente contrastando los rendimientos reales declarados a la Agencia Tributaria.
4. **Sedes Oficiales de Tramitación:**
   - Trámite censal: Sede Electrónica de la Agencia Tributaria (aeat.es), mediante certificado digital, DNIe o Cl@ve.
   - Trámite RETA: Portal Import@ss de la Tesorería General de la Seguridad Social (seg-social.es).

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Verificación Normativa Previa:** Consultar siempre las fuentes de referencia antes de emitir tramos de cotización o plazos. Nunca usar tablas derogadas.
2. **Cero Invención de Datos:** Queda estrictamente prohibido inventar epígrafes del IAE, NIFs o cuotas. Todo dato no confirmado debe permanecer como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** Si se detectan novedades en las órdenes de cotización o formularios de la AEAT, aplicar las modificaciones directamente en el borrador del workspace del usuario; nunca intentar modificar los archivos internos del plugin.
4. **Límites de Alcance:** No tramitar constituciones de sociedades mercantiles (SL/SA), modificaciones censales de personas jurídicas ni solicitudes de la prestación por cese de actividad (paro del autónomo), las cuales deben derivarse a profesionales colegiados.
