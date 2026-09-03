---
name: liquidacion-impuesto-sucesiones
description: >
  Prepara la autoliquidacion del Impuesto sobre Sucesiones y Donaciones (modelo 650, adquisiciones
  mortis causa) de un heredero conforme a la Ley 29/1987 (LISD) y a su Reglamento (RD 1629/1991)
  en su version consolidada vigente verificada en el BOE, combinada con la normativa autonomica vigente
  de la comunidad autonoma competente verificada en vivo. Opera bajo el flujo de 5 fases canonicas con
  clasificacion HITL, consulta de assets, creacion zero-vacios en workspace y edicion incremental seccion
  a seccion. Genera el borrador de autoliquidacion del modelo 650 con inventario, reducciones autonómicas
  y cuota estimada debidamente senalada con advertencia de verificacion, checklist documental, organismo
  competente y aviso imperativo de plusvalia municipal (IIVTNU). NO usar para la particion juridica de la
  herencia (usar la skill herencia de derecho-civil), para donaciones inter vivos ni para fijar la cuota
  tributaria con caracter definitivo vinculante.
when_to_use: |
  - El usuario ya sabe que heredero es y que recibe, y necesita preparar la autoliquidacion del Impuesto de Sucesiones (modelo 650).
  - El usuario dispone del inventario y los valores de la herencia (propios o del cuaderno particional) y quiere saber base, estimacion de cuota, plazo y organismo.
  - El usuario pide el checklist de documentos y tasas para presentar el Impuesto de Sucesiones y saber donde se presenta.
inputs:
  - modalidad_transmision: adquisicion_mortis_causa_modelo_650 (V1)
  - grupo_parentesco: grupo_i / grupo_ii / grupo_iii / grupo_iv (V2)
  - naturaleza_causahabiente: persona_fisica (V3)
  - comunidad_autonoma: CCAA de residencia habitual del causante (clave de bonificaciones) (V4)
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - datos_causante: nombre, NIF, fecha y lugar de fallecimiento, ultimo domicilio, CCAA de residencia habitual
  - datos_heredero: nombre, NIF, domicilio, parentesco con el causante y grupo (I a IV)
  - caudal_hereditario: inventario de bienes y sus valores (del cuaderno particional si existe)
  - cargas_deudas: cargas, deudas deducibles y gastos (ultima enfermedad, entierro y funeral)
  - seguros_vida: importe de seguros de vida cuyo beneficiario sea el heredero, si los hay
  - ajuar_domestico: valor declarado del ajuar, o aplicar el 3% del caudal relicto (Art. 15) salvo prueba
  - vivienda_habitual: si el heredero adquiere la vivienda habitual del causante (reduccion Art. 20.2.c)
  - empresa_familiar: si se adquiere empresa individual, negocio o participaciones (reduccion Art. 20.2.c)
  - discapacidad: grado de discapacidad del heredero, si procede reduccion
outputs:
  - borrador_autoliquidacion_650: hoja de datos y borrador del modelo 650 con base, reducciones y cuota estimada en markdown, DRAFT
  - checklist_documentacion: checklist de documentos, tasas, organismo y plazo para la presentacion en markdown, DRAFT
references:
  - references/isd-ley-29-1987.md
  - references/isd-normativa-autonomica.md
  - references/plusvalia-municipal.md
  - references/fuentes-y-plazos.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-borrador-autoliquidacion-650.md
  - assets/template-checklist-documentacion-sucesiones.md
---

# Preparar la Autoliquidación del Impuesto de Sucesiones (Modelo 650)

> DRAFT — para revisión por un gestor administrativo o asesor fiscal colegiado antes de su presentación telemática o presencial. No constituye liquidación tributaria definitiva ni dictamen pericial vinculante.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales para preparar la autoliquidación del Impuesto sobre Sucesiones (Modelo 650) del caudal hereditario atribuido a un heredero o legatario.

### Vectores de Estado (Uso Estrictamente Interno):
Para garantizar un enrutamiento determinista y el correcto cálculo tributario cedido a las Comunidades Autónomas, el asistente resuelve y mantiene internamente en memoria los siguientes vectores de estado:
- **V1 (Modalidad Tributaria):** `adquisicion_mortis_causa_modelo_650`.
- **V2 (Grupo de Parentesco):** `grupo_i` (descendientes menores de 21) | `grupo_ii` (descendientes de 21 o más, cónyuges, ascendientes) | `grupo_iii` (colaterales de 2º y 3º grado, afines) | `grupo_iv` (colaterales de 4º grado o más, extraños).
- **V3 (Naturaleza del Causahabiente):** `persona_fisica` (heredero o legatario individual).
- **V4 (Comunidad Autónoma Competente):** CCAA donde el causante tuvo su residencia habitual durante el mayor número de días de los últimos 5 años anteriores al fallecimiento.
- **V5 (Origen Plantilla / Asset):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas técnicas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es fijar la Comunidad Autónoma competente y el grado de parentesco del heredero, que determinan las reducciones y bonificaciones aplicables.

### 1.1 Escucha Activa Previa
Antes de invocar formularios, evalúa el mensaje inicial del usuario:
- Si el usuario ya precisó la CCAA de residencia del fallecido y su grado de parentesco exacto, registra los vectores y avanza a la **Fase 2**.
- Si falta delimitar la CCAA competente (`V4`) o el grupo de parentesco (`V2`), invoca de inmediato la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Invoca la herramienta con las preguntas de conexión territorial y parentesco:

```json
{
  "form_data": [
    {
      "id": "comunidad_autonoma",
      "rationale": "Resolver V4 para fijar la normativa fiscal autonómica y el organismo tributario gestor.",
      "question": "¿En qué Comunidad Autónoma residió habitualmente el causante durante los últimos 5 años?",
      "options": [
        {"id": "madrid", "label": "Comunidad de Madrid"},
        {"id": "andalucia", "label": "Andalucía"},
        {"id": "cataluna", "label": "Cataluña"},
        {"id": "comunidad_valenciana", "label": "Comunidad Valenciana"},
        {"id": "galicia", "label": "Galicia"},
        {"id": "otra_ccaa", "label": "Otra Comunidad Autónoma de régimen común"}
      ]
    },
    {
      "id": "grupo_parentesco",
      "rationale": "Resolver V2 para aplicar las reducciones de la base y bonificaciones de cuota.",
      "question": "¿Qué relación de parentesco tenía el heredero con el fallecido?",
      "options": [
        {"id": "grupo_i", "label": "Hijo/a o descendiente menor de 21 años (Grupo I)"},
        {"id": "grupo_ii", "label": "Hijo/a de 21 años o más, cónyuge, padre o madre (Grupo II)"},
        {"id": "grupo_iii", "label": "Hermano/a, sobrino/a, tío/a, suegro/a o cuñado/a (Grupo III)"},
        {"id": "grupo_iv", "label": "Primo/a, parientes más lejanos o persona sin vínculo de sangre (Grupo IV)"}
      ]
    }
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- Plantillas del sistema propuestas: `assets/template-borrador-autoliquidacion-650.md` y `assets/template-checklist-documentacion-sucesiones.md`.
- Proceder de inmediato a la **Fase 2**.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

Interacción directa en texto plano conversacional en el chat (sin formularios).

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `isd-ley-29-1987.md`, `isd-normativa-autonomica.md`, `plusvalia-municipal.md` y `fuentes-y-plazos.md`.
2. Realiza consulta en vivo mediante `web_search` de la normativa autonómica específica de la CCAA competente para confirmar bonificaciones vigentes (ej. bonificación del 99% en cuota para Grupos I y II en Madrid o Andalucía, reducciones por adquisición de vivienda habitual, etc.). Si detectas modificaciones de baremos, aplica la normativa vigente en el workspace sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Régimen de la CCAA Competente:**
   - Citar la Ley 29/1987 estatal y la ley autonómica aplicable.
   - Explicar las reducciones por parentesco del Grupo respectivo y la bonificación sobre cuota aplicable en esa CCAA.
   - Recordar el plazo legal imperativo de **6 meses desde el fallecimiento** para presentar la autoliquidación (con posibilidad de solicitar prórroga por otros 6 meses dentro de los primeros 5 meses).
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Detallar que dispones de las plantillas oficiales adaptadas: borrador del modelo 650 y checklist documental integral.
3. **Pregunta Explícita al Usuario (Vía Chat):**
   Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
- **Si `V5 = plantilla_sistema`:** Toma los assets oficiales seleccionados y avanza a la **Fase 3**.
- **Si `V5 = plantilla_usuario`:** Adopta la minuta del usuario desde `<attached_documents>` o `<user_message>`, valida la observancia de la normativa fiscal imperativa y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura de los Documentos (`create_file`):**
   - Vuelca íntegramente las plantillas acordadas en el workspace del usuario:
     - `borrador_autoliquidacion_modelo_650.md`.
     - `checklist_documentacion_sucesiones.md`.
   - Aplica el principio **Zero-Omission**:
     - Sustituye los datos ya conocidos de la clasificación (CCAA, grupo de parentesco, coeficientes).
     - Todos los datos económicos o identificativos pendientes deben permanecer como marcadores `{{DATO_FALTANTE}}` en mayúsculas y dobles llaves.
     - PROHIBIDO dejar archivos en blanco o con resúmenes informales.
2. **Validación de Disco (`read_file`):**
   - Comprueba la integridad del archivo recién creado en el workspace.
3. **Confirmación en Chat:**
   - Comunica las rutas de los archivos generados en disco e introduce de inmediato la primera sección de la **Fase 4**.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

Recorre de forma secuencial los bloques de la autoliquidación aplicando el ciclo interactivo:
```
[Pregunta al Usuario] ──> [Vista Previa en texto plano] ──> [¿Confirmamos esta sección?] ──> [edit_file + read_file]
```

### Protocolo Obligatorio por Sección:
1. **Pregunta en Chat:** Solicita los datos específicos del bloque orientando sobre la valoración fiscal (valor de referencia catastral, saldos bancarios a fecha de fallecimiento).
2. **Vista Previa (Preview):** Muestra el bloque redactado en texto plano.
3. **Confirmación:** Pregunta literalmente: `¿Confirmamos esta sección?`.
4. **Persistencia en Disco:** Tras el consentimiento, aplica `edit_file` y valida inmediatamente con `read_file`.

### Hoja de Ruta de Secciones:

1. **Datos del Causante y Punto de Conexión Territorial** *(confirmación agrupada)*:
   - Nombre completo, NIF, fecha y lugar de defunción, y domicilio habitual en los 5 años previos.
2. **Datos del Heredero o Sujeto Pasivo** *(confirmación agrupada)*:
   - Nombre completo, NIF, domicilio a efectos de notificaciones y patrimonio preexistente (si excede de 400.000 € a efectos de coeficientes multiplicadores).
3. **Inventario del Caudal Relicto y Bienes Adjudicados**:
   - Inmuebles: Identificación, referencia catastral y valor fiscal (mayor entre valor de referencia catastral del Catastro y valor declarado).
   - Dinero en cuentas corrientes, depósitos y fondos de inversión a fecha de defunción.
   - Vehículos a motor (según tablas del Ministerio de Hacienda).
   - Seguros de vida con designación expresa de beneficiario.
   - Presunción legal del Ajuar Doméstico (3% del caudal relicto, art. 15 LISD, descontando inmuebles no residenciales).
4. **Pasivo Deducible y Gastos de Sepelio**:
   - Deudas del causante debidamente justificadas documentalmente.
   - Gastos de última enfermedad, entierro y funeral sufragados por el heredero.
5. **Cálculo de la Liquidación Estimada**:
   - Determinación de la Base Imponible y Base Liquidable.
   - Aplicación de reducciones autonómicas por parentesco, discapacidad o adquisición de vivienda habitual del causante.
   - Cuota íntegra según tarifa aplicable y aplicación de bonificaciones autonómicas de cuota (marcada siempre con indicación de estimación sujeta a confirmación).
6. **Aviso Obligatorio de Plusvalía Municipal (IIVTNU)**:
   - Alerta expresa sobre la obligación independiente de liquidar el Impuesto sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana ante el Ayuntamiento en el plazo de 6 meses si se heredan inmuebles urbanos.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones del borrador, presenta al usuario el menú interactivo:
```markdown
El borrador de autoliquidación del Modelo 650 y el checklist documental han sido generados y actualizados en disco.

Seleccione una opción si desea realizar ajustes adicionales:
1. Modificar valores de bienes inmuebles, cuentas o deudas deducibles.
2. Revisar la aplicación de reducciones autonómicas (vivienda habitual o empresa familiar).
3. Modificar datos del causante o del heredero.
4. Realizar control de calidad global del cálculo fiscal estimado.
5. Dar el borrador por finalizado y cerrar la sesión.
```

### Advertencias Preceptivas al Finalizar:
Al cerrar el procedimiento, emite siempre las siguientes advertencias:
1. **Carácter Estimado y DRAFT:** La liquidación generada es una estimación técnica orientativa sujeta a revisión profesional por un gestor administrativo o asesor fiscal colegiado antes de su ingreso o presentación telemática.
2. **Plazo Fatal de 6 Meses:** El plazo para presentar la autoliquidación y abonar el tributo es de **6 meses desde el fallecimiento**. La solicitud de prórroga por 6 meses adicionales debe presentarse de forma obligatoria dentro de los primeros 5 meses del plazo.
3. **Comprobación de Valores:** Los valores declarados (especialmente en inmuebles) están sujetos a comprobación de valores por la Administración Tributaria autonómica conforme al valor de referencia del Catastro.
4. **Plusvalía Municipal (IIVTNU):** Recuerda que si la masa hereditaria incluye inmuebles urbanos, debe presentarse de forma obligatoria la autoliquidación o declaración del impuesto de plusvalía municipal ante el Ayuntamiento correspondiente en el mismo plazo de 6 meses.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Carácter Provisional de la Cuota:** Queda prohibido presentar la cuota tributaria como definitiva o garantizada; debe consignarse expresamente la advertencia de comprobación administrativa.
2. **Cero Invención de Datos:** No inventar referencias catastrales, importes de tasación ni datos fiscales. Todo dato pendiente debe permanecer como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** Aplicar cualquier variación en bonificaciones autonómicas directamente en el workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** Esta skill no realiza la partición formal del caudal relicto (adjudicación jurídica de lotes), la cual debe realizarse mediante la skill `derecho-civil:herencia` y formalizarse ante Notario público.
