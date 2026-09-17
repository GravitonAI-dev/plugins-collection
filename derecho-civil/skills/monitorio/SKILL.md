---
name: monitorio
description: >
  Genera la peticion inicial de proceso monitorio para reclamar una deuda dineraria liquida,
  determinada, vencida y exigible de cualquier cuantia, conforme a los articulos 812 a 818 de la
  **Ley 1/2000 de Enjuiciamiento Civil (LEC)**, que regula el proceso monitorio como via rapida para cobrar deudas documentadas, en su version consolidada vigente verificada en el BOE.
  Opcionalmente genera tambien el burofax de requerimiento previo (intento de MASC). Adapta el
  documento segun la naturaleza de las partes y el tipo de deuda (rentas de arrendamiento u otra).
  NO usar para deudas no dinerarias, iliquidas o controvertidas, ni para reclamaciones frente a
  Administraciones Publicas.
when_to_use: |
  - El usuario quiere reclamar el cobro de una deuda dineraria impagada.
  - El usuario dispone de documentos que acreditan la deuda (facturas, contrato, reconocimiento, rentas).
  - El usuario pide una peticion de monitorio o un burofax previo de reclamacion de pago.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - alcance: solo peticion inicial / peticion inicial + burofax previo
  - tipo_deuda: rentas de arrendamiento / otra (facturas, prestamo, servicios, comunidad de propietarios)
  - naturaleza_acreedor: persona fisica o persona juridica
  - datos_acreedor: nombre o razon social, NIF o CIF, domicilio
  - datos_deudor: nombre o razon social, NIF o CIF, domicilio o lugar donde pueda ser hallado
  - origen_deuda: descripcion del origen y documentos que la acreditan
  - cuantia: principal en euros e intereses si proceden
  - fecha_vencimiento: fecha en que la deuda vencio y devino exigible
  - partido_judicial: domicilio del deudor a efectos de competencia (Art. 813)
  - masc_intentado: si se ha intentado un medio adecuado de solucion de controversias (si / no)
outputs:
  - peticion_monitorio: peticion inicial de proceso monitorio en markdown, DRAFT
  - burofax_requerimiento: opcional, burofax de requerimiento previo en markdown, DRAFT
references:
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-documentos-acreditativos-deuda.md
  - references/lec-proceso-monitorio-812-818.md
  - references/masc-requisito-procedibilidad-lo1-2025.md
assets:
  - assets/template-burofax-requerimiento-previo-masc.md
  - assets/template-peticion-inicial-monitorio-rentas.md
  - assets/template-peticion-inicial-monitorio.md
---

# Generar Peticion de Proceso Monitorio

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
      "id": "alcance",
      "rationale": "Resolver V1: determina si además de la petición inicial se genera el burofax de requerimiento previo, útil para acreditar el intento de solución previa.",
      "question": "¿Qué alcance tiene el encargo?",
      "options": [
        {"id": "solo_peticion", "label": "Solo la petición inicial del proceso monitorio"},
        {"id": "peticion_y_burofax", "label": "La petición inicial y, antes, el burofax de requerimiento previo de pago"}
      ]
    },
    {
      "id": "tipo_deuda",
      "rationale": "Resolver V2: las rentas de arrendamiento tienen variante propia de petición inicial y régimen específico de acreditación.",
      "question": "¿De dónde procede la deuda?",
      "options": [
        {"id": "rentas_arrendamiento", "label": "Rentas de arrendamiento impagadas"},
        {"id": "otra_causa", "label": "Otra causa: facturas, préstamo, servicios o gastos de comunidad"}
      ]
    },
    {
      "id": "naturaleza_acreedor",
      "rationale": "Resolver V3: fija la estructura de comparecencia y la acreditación de la representación en la petición inicial.",
      "question": "¿Quién es el acreedor?",
      "options": [
        {"id": "persona_fisica", "label": "Persona física"},
        {"id": "persona_juridica", "label": "Persona jurídica"}
      ]
    },
    {
      "id": "masc_intentado",
      "rationale": "Resolver V4: el intento de un medio adecuado de solución de controversias condiciona la procedibilidad conforme a la Ley Orgánica 1/2025.",
      "question": "¿Se ha intentado ya algún medio de solución previa: burofax, mediación o negociación?",
      "options": [
        {"id": "si", "label": "Sí"},
        {"id": "no", "label": "No"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `alcance`
- `V2` — `tipo_deuda`
- `V3` — `naturaleza_acreedor`
- `V4` — `masc_intentado`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores, evalua en este orden:

- Si **V2 = rentas_arrendamiento** → **HOJA RENTAS**: `assets/template-peticion-inicial-monitorio-rentas.md` (Art. 812.2.2.º LEC, que admite acumular las rentas y cantidades debidas del arrendamiento).
- Si **V2 = otra causa** → **HOJA GENERAL**: `assets/template-peticion-inicial-monitorio.md`.
- Si **V1 = peticion_y_burofax**, o **V4 = no** → generar ademas, y **ANTES** de la peticion inicial, `assets/template-burofax-requerimiento-previo-masc.md`. El requerimiento fehaciente previo no es presupuesto de admision del monitorio, pero por defecto conservador se recomienda dejarlo acreditado: constituye en mora, fija la fecha de devengo de los intereses y evita la discusion sobre la procedibilidad. Explicaselo al cliente en esos terminos, sin presentarlo como obligatorio.
- Si **V1 = solo_peticion** y **V4 = si** → no se genera el burofax; se hace constar en la peticion el intento ya practicado.
- V3 no elige asset: determina la variante del encabezamiento de comparecencia y la acreditacion de la representacion (persona fisica, o persona juridica con su representante y el titulo del que resulta la representacion).
- Si la deuda **no es dineraria, liquida, determinada, vencida y exigible** (Art. 812.1 LEC) → **DETENER**: el monitorio no es el cauce. Derivar a `reclamacion-cantidad` para que elija la via declarativa procedente. No crear documento.
- Si lo que se pretende es **oponerse** a un monitorio ya notificado al cliente → **DETENER**: derivar a `reclamacion-cantidad`, que cubre el escrito de oposicion. No crear documento.
- Si la deuda es de **cuotas de comunidad de propietarios** → **DETENER** y derivar a `propiedad-horizontal`, que exige la certificacion previa del acuerdo de la junta (articulos 21.1 a 21.3 de la Ley de Propiedad Horizontal) y tiene su propia peticion inicial.
- **Requisito de procedibilidad (Ley Organica 1/2025).** Si el intento previo de un medio adecuado de solucion de controversias no esta acreditado y esta skill no genera por si misma el documento que lo acredita, **deriva a `masc-acuerdos`**, que produce el requerimiento de negociacion, el acta del intento, la oferta vinculante, el acuerdo transaccional y la declaracion responsable de imposibilidad. Ofrece encadenar con ella antes de continuar, y advierte de que sin ese documento la demanda no se admite a tramite.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
Ejecuta esta secuencia completa; en esta materia la verificación no es opcional:


La skill verifica las fuentes oficiales en cada lanzamiento y, si detecta una version posterior, aplica la redaccion vigente al documento que redacta en el workspace del usuario, sin modificar sus propios archivos de plugin. Ejecutar SIEMPRE esta secuencia:

- **Leer la fecha/version registrada localmente.** Consultar `references/fuentes-plantillas-validadas.md`, que llega cargada en tu contexto, y anotar la "Version registrada" de la LEC y del modelo del CGPJ.

- **Consultar la fuente oficial vigente.** Invocar:
```
web_search(...)
```
Extraer: fecha del texto consolidado vigente de la LEC; redaccion actual de los arts. 812 a 818 y del art. 264 (acreditacion del intento de MASC); estado de aplicacion de la LO 1/2025 (BOE-A-2025-76).

Consultar tambien el modelo normalizado del CGPJ:
```
web_search(...)
```

- **Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

- **Aplicación de la redacción vigente.** Si la versión oficial es posterior o el texto de los artículos ha cambiado, aplica la redacción vigente directamente sobre el documento a redactar en el workspace del usuario, sin usar versiones desactualizadas.

- **Fallback si la fuente no es accesible.** Si `web_search` no devuelve la fuente oficial:
```
web_search("Ley Enjuiciamiento Civil proceso monitorio articulos 812 818 texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. La peticion se genera con la version de referencia. Verificar manualmente antes de presentar."

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 812 a 818 de la Ley de Enjuiciamiento Civil (LEC), modificados por RDL 6/2023 y LO 1/2025; Art. 21 de la Ley de Propiedad Horizontal; y Art. 813 LEC (competencia territorial improrrogable del domicilio del deudor).
2. **Orientación Legal del Caso:**
   Informa al usuario, en registro formal, de la norma y los artículos aplicables a la ruta resuelta, con la versión vigente verificada en la Fase 2.1 y el enlace de la fuente consultada.

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** (menciónala por su denominación formal, sin mostrar rutas internas ni volcar su contenido). Si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la seccion de assets.
4. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

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

### Hoja de Ruta de Secciones y Cláusulas Condicionales

1. **Parte acreedora** *(confirmación agrupada)*: nombre completo o razón social, NIF/CIF, domicilio a efectos de notificaciones. Si es persona jurídica: datos del representante legal.
2. **Parte deudora** *(confirmación agrupada)*: nombre completo o razón social, NIF/CIF, domicilio o lugar donde pueda ser hallado para el requerimiento judicial (art. 813 LEC).
3. **Origen de la deuda y documentos acreditativos**: origen de la deuda (rentas, facturas, contrato, préstamo), desglose de los documentos que la acreditan conforme al art. 812 LEC, fechas de vencimiento y exigibilidad.
4. **Cuantía reclamada e intereses**: principal adeudado en euros e intereses solicitados (pactados o legal del dinero devengados desde el vencimiento).
5. **Juzgado competente**: determinación formal del Juzgado de Primera Instancia del domicilio del deudor (art. 813 LEC).
6. **Requerimiento previo MASC** *(solo si V4 = no, burofax)*: plazo otorgado para el pago (10 días hábiles recomendados), cuenta IBAN de ingreso y medios de contacto para la solución negociada.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version de la LEC posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario. No usar una version desactualizada.
3. Solo procede el monitorio si la deuda es dineraria, liquida, determinada, vencida y exigible (Art. 812). Si no lo es, no redactar la peticion: advertir y ofrecer alternativa (juicio declarativo) o escalacion.
4. Debe existir al menos un documento que acredite la deuda (Art. 812). Sin documento acreditativo, no procede.
5. Competencia exclusiva del Juzgado de Primera Instancia del domicilio o residencia del deudor (Art. 813). No admitir sumision a otro fuero.
6. Posicion conservadora sobre el MASC: ante la duda sobre si es exigible en el monitorio (LO 1/2025), recomendar e integrar el intento previo (burofax) y advertir de la cuestion.
7. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{CUANTIA_RECLAMADA}}` (NUNCA corchete simple `[DATO]`: colisiona con los identificadores de privacidad `[PERSON_1]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `edit_file` posterior necesita un `oldString` unico. Nunca inventar datos, cuantias ni fechas.
8. Nunca afirmar que la deuda es exigible o incontrovertida sin base documental. Nunca inventar jurisprudencia.
