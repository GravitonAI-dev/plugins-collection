---
name: liquidacion-impuesto-sucesiones
description: >
  Prepara la autoliquidacion del Impuesto sobre Sucesiones y Donaciones (modelo 650, adquisiciones
  mortis causa) de un heredero conforme a la **Ley 29/1987 del Impuesto sobre Sucesiones y Donaciones (LISD)**, que regula el hecho imponible, las reducciones y la cuota del impuesto, y a su **Reglamento (RD 1629/1991)**
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
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
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
- **origen_plantilla (origen de la plantilla):** `plantilla_sistema` | `plantilla_usuario`.

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores y los resúmenes de validación con marcas técnicas (por ejemplo, anotar un vector como resuelto) son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial, claro y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores de dominio mediante Formulario HITL)

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

**Correspondencia con el enrutamiento.** Los vectores de esta skill se nombran con los identificadores siguientes; cada uno se resuelve con la respuesta indicada. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `modalidad_transmision`
- `V2` — `grupo_parentesco`
- `V3` — naturaleza del causahabiente: no se pregunta, es siempre persona fisica
- `V4` — `comunidad_autonoma`, clave de las bonificaciones autonomicas

### 1.3 Enrutamiento de Estado (Routing por Vectores)
- Plantillas del sistema propuestas: `assets/template-borrador-autoliquidacion-650.md` y `assets/template-checklist-documentacion-sucesiones.md`.
- Proceder de inmediato a la **Fase 2**.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
1. Consulta las referencias internas: `isd-ley-29-1987.md`, `isd-normativa-autonomica.md`, `plusvalia-municipal.md` y `fuentes-y-plazos.md`.
2. Realiza consulta en vivo mediante `web_search` de la normativa autonómica específica de la CCAA competente para confirmar bonificaciones vigentes (ej. bonificación del 99% en cuota para Grupos I y II en Madrid o Andalucía, reducciones por adquisición de vivienda habitual, etc.). Si detectas modificaciones de baremos, aplica la normativa vigente en el workspace sin alterar los assets locales.

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y pedagógico:
1. **Marco Legal y Régimen de la CCAA Competente:**
   - Citar la Ley 29/1987 estatal y la ley autonómica aplicable.
   - Explicar las reducciones por parentesco del Grupo respectivo y la bonificación sobre cuota aplicable en esa CCAA.
   - Recordar el plazo legal imperativo de **6 meses desde el fallecimiento** para presentar la autoliquidación (con posibilidad de solicitar prórroga por otros 6 meses dentro de los primeros 5 meses).
2. **Propuesta de Plantilla Oficial del Sistema:**
   - Detallar que dispones de las plantillas oficiales adaptadas: borrador del modelo 650 y checklist documental integral.
   - Menciona por su denominación formal (sin mostrar rutas internas ni volcar su contenido) la hoja **que ha resuelto el enrutamiento de la Fase 1.3**; si el enrutamiento asigno varias, nombralas todas y en el orden en que se van a rellenar. **No propongas una hoja distinta de la enrutada.**
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

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. **Carácter Provisional de la Cuota:** Queda prohibido presentar la cuota tributaria como definitiva o garantizada; debe consignarse expresamente la advertencia de comprobación administrativa.
2. **Cero Invención de Datos:** No inventar referencias catastrales, importes de tasación ni datos fiscales. Todo dato pendiente debe permanecer como `{{DATO_FALTANTE}}`.
3. **Inmutabilidad del Plugin en Disco:** Aplicar cualquier variación en bonificaciones autonómicas directamente en el workspace del usuario; nunca modificar los archivos internos del plugin.
4. **Límites de Alcance:** Esta skill no realiza la partición formal del caudal relicto (adjudicación jurídica de lotes), la cual debe realizarse mediante la skill `derecho-civil:herencia` y formalizarse ante Notario público.
