---
name: monitorio
description: >
  Genera la peticion inicial de proceso monitorio para reclamar una deuda dineraria liquida,
  determinada, vencida y exigible de cualquier cuantia, conforme a los articulos 812 a 818 de la
  Ley de Enjuiciamiento Civil (LEC) en su version consolidada vigente verificada en el BOE.
  Opcionalmente genera tambien el burofax de requerimiento previo (intento de MASC). Adapta el
  documento segun la naturaleza de las partes y el tipo de deuda (rentas de arrendamiento u otra).
  NO usar para deudas no dinerarias, iliquidas o controvertidas, ni para reclamaciones frente a
  Administraciones Publicas.
when_to_use: |
  - El usuario quiere reclamar el cobro de una deuda dineraria impagada.
  - El usuario dispone de documentos que acreditan la deuda (facturas, contrato, reconocimiento, rentas).
  - El usuario pide una peticion de monitorio o un burofax previo de reclamacion de pago.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
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

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación (V1 a V4) y el origen de la plantilla (V5).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la naturaleza del caso y fijar los vectores deterministas de estado.

### 1.1 Escucha Activa Previa
Antes de abrir formularios interactivos o hacer preguntas, analiza el mensaje inicial del usuario y la documentación aportada:
- Si el mensaje ya especifica inequívocamente los vectores de la operación, asígnalos de forma inmediata y silenciosa en memoria y pasa a la **Fase 2**.
- Si restan vectores por definir, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado interactivo mediante la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Presenta al usuario las opciones estructuradas para resolver los vectores pendientes:
```json
{
  "type": "object",
  "properties": {
    "tipo_deuda": {
      "type": "string",
      "description": "Naturaleza de la deuda dineraria (V1)",
      "enum": [
        "rentas_arrendamiento",
        "deuda_comercial_general",
        "comunidad_propietarios"
      ]
    },
    "alcance_escrito": {
      "type": "string",
      "description": "Documento o alcance solicitado (V2)",
      "enum": [
        "peticion_judicial",
        "burofax_masc"
      ]
    }
  },
  "required": [
    "tipo_deuda",
    "alcance_escrito"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Asigna deterministamente la plantilla del sistema aplicable según la combinación de vectores resultante y valida los presupuestos legales antes de avanzar a la Fase 2.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 812 a 818 de la Ley de Enjuiciamiento Civil (LEC), modificados por RDL 6/2023 y LO 1/2025; Art. 21 de la Ley de Propiedad Horizontal; y Art. 813 LEC (competencia territorial improrrogable del domicilio del deudor).
2. **Orientación Legal del Caso:**
La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" de la LEC y del modelo del CGPJ.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_file(...) o web_search(...)
```
Extraer: fecha del texto consolidado vigente de la LEC; redaccion actual de los arts. 812 a 818 y del art. 264 (acreditacion del intento de MASC); estado de aplicacion de la LO 1/2025 (BOE-A-2025-76).

Consultar tambien el modelo normalizado del CGPJ:
```
read_file(...) o web_search(...)
```

**1.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/lec-proceso-monitorio-812-818.md`, `references/lec-documentos-acreditativos-deuda.md` y/o `references/masc-requisito-procedibilidad-lo1-2025.md` con la redaccion vigente.
- Si el CGPJ publica un modelo posterior, actualizar la estructura de `assets/template-peticion-inicial-monitorio.md` (y la variante de rentas si procede).
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_file` falla (error HTTP, timeout):
```
web_search("Ley Enjuiciamiento Civil proceso monitorio articulos 812 818 texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. La peticion se genera con la version de referencia. Verificar manualmente antes de presentar."
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-burofax-requerimiento-previo-masc.md`).
4. **Pregunta Explícita al Usuario (Vía Chat):** Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
* **Si `[V5 = plantilla_sistema]` (El usuario acepta la plantilla propuesta):**
  Toma el texto íntegro de la plantilla correspondiente directamente desde el catálogo del prompt y procede de inmediato a la **Fase 3**.
* **Si `[V5 = plantilla_usuario]` (El usuario aporta su propia minuta adjuntando un documento o pegando texto):**
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

### Paso 1 — Verificacion normativa

**1.1 — Consultar la version registrada en references.** Consultar el archivo `fuentes-plantillas-validadas.md` directamente desde el bloque `<document kind="references-collection">` de tu system prompt y anotar la "Version registrada" de la LEC y del modelo del CGPJ.

**1.2 — Consultar la fuente oficial vigente en vivo.** Invocar:
```
read_file(...) o web_search(...)
```
Extraer: fecha del texto consolidado vigente de la LEC; redaccion actual de los arts. 812 a 818 y del art. 264 (acreditacion del intento de MASC); estado de aplicacion de la LO 1/2025 (BOE-A-2025-76).

Consultar tambien el modelo normalizado del CGPJ:
```
read_file(...) o web_search(...)
```

**1.3 — Comparar.** Contrastar la version oficial con la registrada en `fuentes-plantillas-validadas.md` y con las referencias del prompt (`lec-proceso-monitorio-812-818.md`, `lec-documentos-acreditativos-deuda.md`, `masc-requisito-procedibilidad-lo1-2025.md`).

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/lec-proceso-monitorio-812-818.md`, `references/lec-documentos-acreditativos-deuda.md` y/o `references/masc-requisito-procedibilidad-lo1-2025.md` con la redaccion vigente.
- Si el CGPJ publica un modelo posterior, actualizar la estructura de `assets/template-peticion-inicial-monitorio.md` (y la variante de rentas si procede).
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_file` falla (error HTTP, timeout):
```
web_search("Ley Enjuiciamiento Civil proceso monitorio articulos 812 818 texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. La peticion se genera con la version de referencia. Verificar manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos:

**Bloque A — Alcance del encargo:**
"Desea generar (1) solo la peticion inicial del monitorio, o (2) tambien el burofax de requerimiento previo de pago (recomendado para acreditar el intento de negociacion previa)?"

**Bloque B — Tipo de deuda:**
"La deuda procede de (1) rentas de arrendamiento impagadas, o (2) otra causa (facturas, prestamo, servicios, gastos de comunidad)?"

**Bloque C — Datos del acreedor:**
- Nombre completo o razon social, NIF/CIF, domicilio a efectos de notificaciones.
- Persona fisica o juridica. Si juridica, datos del representante.

**Bloque D — Datos del deudor:**
- Nombre completo o razon social, NIF/CIF.
- Domicilio o residencia, o lugar donde pueda ser hallado (para competencia y requerimiento, Art. 813).

**Bloque E — Origen y cuantia de la deuda:**
- Origen de la deuda y documentos que la acreditan (facturas, contrato, reconocimiento, certificacion de rentas).
- Principal adeudado en euros.
- Intereses reclamados (pactados o interes legal desde el vencimiento), si proceden.
- Fecha de vencimiento y de exigibilidad.

**Bloque F — MASC (procedibilidad):**
"Se ha intentado ya algun medio de solucion previa (burofax, mediacion, negociacion)? (si / no)"

Si responde "no" y se ha optado por solo la peticion inicial, advertir de la cuestion del requisito de procedibilidad (LO 1/2025) y recomendar generar tambien el burofax.

### Paso 3 — Validacion de procedibilidad

Antes de redactar, validar:

a) **Naturaleza de la deuda (Art. 812):** que es dineraria, liquida, determinada, vencida y exigible. Si falla cualquiera de estos requisitos, no procede monitorio: advertir y ofrecer juicio declarativo o escalacion.

b) **Documento acreditativo (Art. 812):** que existe al menos un documento de los previstos. Si no existe, no procede.

c) **Competencia (Art. 813):** identificar el Juzgado de Primera Instancia del domicilio del deudor. Si el deudor es ilocalizable, advertir de la limitacion (el requerimiento por edictos no procede en el monitorio; podria derivar en archivo).

d) **MASC (LO 1/2025):** confirmar si se ha intentado o si concurre una excepcion. Por defecto conservador, integrar el burofax de requerimiento previo.

e) **Cuantia y via posterior:** informar de que, si el deudor se opone, el asunto se resolvera por juicio verbal (hasta 15.000 euros) u ordinario (superior), Art. 818.

### Paso 4 — Generacion de los documentos

Seleccionar la plantilla segun el tipo de deuda:
- Rentas de arrendamiento: `assets/template-peticion-inicial-monitorio-rentas.md`
- Otra deuda: `assets/template-peticion-inicial-monitorio.md`

Generar la peticion inicial en el workspace invocando `create_file`:
```
create_file(...)
```

Si el usuario ha pedido tambien el burofax (Bloque A opcion 2), generar ademas con la plantilla `template-burofax-requerimiento-previo-masc.md`:
```
create_file(...)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado conservan el placeholder propio del asset en doble llave (nunca corchete simple).

Aplicar las directivas de `estilo-redaccion-escritos.md` (disponible directamente en `<document kind="references-collection">` del prompt): escrito breve y directo, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos ni citas largas, y SUPLICO ajustado a lo estrictamente pedido.

Tras guardar el archivo en disco del workspace, invocar `read_file` exclusivamente sobre la ruta del workspace para verificar la integridad del documento escrito.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente al acreedor, al deudor y el juzgado competente.
- Expresa con claridad el origen y la cuantia de la deuda, y relaciona los documentos que se acompanan.
- Sigue el estilo de redaccion judicial clara (hechos y fundamentos numerados, una idea por parrafo).

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado antes de su presentacion.
2. Version de la LEC verificada: [fecha extraida en Paso 1].
3. Deben acompanarse a la peticion los documentos que acreditan la deuda (Art. 812 LEC).
4. Competencia exclusiva del Juzgado de Primera Instancia del domicilio del deudor (Art. 813 LEC).
5. Tras la admision, el deudor sera requerido para pagar u oponerse en 20 dias. Si se opone, el asunto pasa a juicio verbal u ordinario segun la cuantia (Art. 818 LEC).
6. El requisito de intento de MASC (LO 1/2025) puede ser exigido por el juzgado. Se recomienda conservar el justificante del burofax de requerimiento previo.
```

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

1. Verificar siempre la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version de la LEC posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada.
3. Solo procede el monitorio si la deuda es dineraria, liquida, determinada, vencida y exigible (Art. 812). Si no lo es, no redactar la peticion: advertir y ofrecer alternativa (juicio declarativo) o escalacion.
4. Debe existir al menos un documento que acredite la deuda (Art. 812). Sin documento acreditativo, no procede.
5. Competencia exclusiva del Juzgado de Primera Instancia del domicilio o residencia del deudor (Art. 813). No admitir sumision a otro fuero.
6. Posicion conservadora sobre el MASC: ante la duda sobre si es exigible en el monitorio (LO 1/2025), recomendar e integrar el intento previo (burofax) y advertir de la cuestion.
7. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{cuantia_reclamada}}` (NUNCA corchete simple `[DATO]`: colisiona con los identificadores de privacidad `[PERSON_1]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `Edit` posterior necesita un `oldString` unico. Nunca inventar datos, cuantias ni fechas.
8. Nunca afirmar que la deuda es exigible o incontrovertida sin base documental. Nunca inventar jurisprudencia.

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" de la LEC y del modelo del CGPJ.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_file(...) o web_search(...)
```
Extraer: fecha del texto consolidado vigente de la LEC; redaccion actual de los arts. 812 a 818 y del art. 264 (acreditacion del intento de MASC); estado de aplicacion de la LO 1/2025 (BOE-A-2025-76).

Consultar tambien el modelo normalizado del CGPJ:
```
read_file(...) o web_search(...)
```

**1.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/lec-proceso-monitorio-812-818.md`, `references/lec-documentos-acreditativos-deuda.md` y/o `references/masc-requisito-procedibilidad-lo1-2025.md` con la redaccion vigente.
- Si el CGPJ publica un modelo posterior, actualizar la estructura de `assets/template-peticion-inicial-monitorio.md` (y la variante de rentas si procede).
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_file` falla (error HTTP, timeout):
```
web_search("Ley Enjuiciamiento Civil proceso monitorio articulos 812 818 texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. La peticion se genera con la version de referencia. Verificar manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos:

**Bloque A — Alcance del encargo:**
"Desea generar (1) solo la peticion inicial del monitorio, o (2) tambien el burofax de requerimiento previo de pago (recomendado para acreditar el intento de negociacion previa)?"

**Bloque B — Tipo de deuda:**
"La deuda procede de (1) rentas de arrendamiento impagadas, o (2) otra causa (facturas, prestamo, servicios, gastos de comunidad)?"

**Bloque C — Datos del acreedor:**
- Nombre completo o razon social, NIF/CIF, domicilio a efectos de notificaciones.
- Persona fisica o juridica. Si juridica, datos del representante.

**Bloque D — Datos del deudor:**
- Nombre completo o razon social, NIF/CIF.
- Domicilio o residencia, o lugar donde pueda ser hallado (para competencia y requerimiento, Art. 813).

**Bloque E — Origen y cuantia de la deuda:**
- Origen de la deuda y documentos que la acreditan (facturas, contrato, reconocimiento, certificacion de rentas).
- Principal adeudado en euros.
- Intereses reclamados (pactados o interes legal desde el vencimiento), si proceden.
- Fecha de vencimiento y de exigibilidad.

**Bloque F — MASC (procedibilidad):**
"Se ha intentado ya algun medio de solucion previa (burofax, mediacion, negociacion)? (si / no)"

Si responde "no" y se ha optado por solo la peticion inicial, advertir de la cuestion del requisito de procedibilidad (LO 1/2025) y recomendar generar tambien el burofax.

### Paso 3 — Validacion de procedibilidad

Antes de redactar, validar:

a) **Naturaleza de la deuda (Art. 812):** que es dineraria, liquida, determinada, vencida y exigible. Si falla cualquiera de estos requisitos, no procede monitorio: advertir y ofrecer juicio declarativo o escalacion.

b) **Documento acreditativo (Art. 812):** que existe al menos un documento de los previstos. Si no existe, no procede.

c) **Competencia (Art. 813):** identificar el Juzgado de Primera Instancia del domicilio del deudor. Si el deudor es ilocalizable, advertir de la limitacion (el requerimiento por edictos no procede en el monitorio; podria derivar en archivo).

d) **MASC (LO 1/2025):** confirmar si se ha intentado o si concurre una excepcion. Por defecto conservador, integrar el burofax de requerimiento previo.

e) **Cuantia y via posterior:** informar de que, si el deudor se opone, el asunto se resolvera por juicio verbal (hasta 15.000 euros) u ordinario (superior), Art. 818.

### Paso 4 — Generacion de los documentos

Seleccionar la plantilla segun el tipo de deuda:
- Rentas de arrendamiento: `assets/template-peticion-inicial-monitorio-rentas.md`
- Otra deuda: `assets/template-peticion-inicial-monitorio.md`

Invocar:
```
create_file(...)
```

Si el usuario ha pedido tambien el burofax (Bloque A opcion 2), generar ademas:
```
create_file(...)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado conservan el placeholder propio del asset en doble llave (nunca corchete simple).

Aplicar el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo (una peticion de monitorio es un asunto sencillo, no mas de unos folios), HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos ni citas largas, y SUPLICO ajustado a lo estrictamente pedido.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente al acreedor, al deudor y el juzgado competente.
- Expresa con claridad el origen y la cuantia de la deuda, y relaciona los documentos que se acompanan.
- Sigue el estilo de redaccion judicial clara (hechos y fundamentos numerados, una idea por parrafo).

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado antes de su presentacion.
2. Version de la LEC verificada: [fecha extraida en Paso 1].
3. Deben acompanarse a la peticion los documentos que acreditan la deuda (Art. 812 LEC).
4. Competencia exclusiva del Juzgado de Primera Instancia del domicilio del deudor (Art. 813 LEC).
5. Tras la admision, el deudor sera requerido para pagar u oponerse en 20 dias. Si se opone, el asunto pasa a juicio verbal u ordinario segun la cuantia (Art. 818 LEC).
6. El requisito de intento de MASC (LO 1/2025) puede ser exigido por el juzgado. Se recomienda conservar el justificante del burofax de requerimiento previo.
```

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar para deudas no dinerarias (entrega de cosa, obligaciones de hacer).
- No usar para deudas iliquidas, controvertidas o de existencia dudosa: procede el juicio declarativo.
- No usar para reclamar a una Administracion Publica.
- No usar para redactar la oposicion del deudor ni la posterior demanda de juicio declarativo.
- No usar si el usuario pide opinion juridica sobre un litigio: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.