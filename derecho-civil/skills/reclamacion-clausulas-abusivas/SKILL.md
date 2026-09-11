---
name: reclamacion-clausulas-abusivas
description: >
  Genera escritos para reclamar la nulidad de clausulas abusivas en contratos con consumidores y la
  restitucion de las cantidades indebidamente cobradas, conforme al **Texto Refundido de la Ley General
  para la Defensa de los Consumidores y Usuarios (TRLGDCU, Real Decreto Legislativo 1/2007)**, que define los derechos basicos del consumidor y el control de las clausulas abusivas, la **Ley
  7/1998 de Condiciones Generales de la Contratacion (LCGC)** y la **Directiva 93/13/CEE**, en su version
  consolidada vigente verificada en el BOE. Produce, a eleccion del usuario, una RECLAMACION
  EXTRAJUDICIAL a la entidad o empresa, o una DEMANDA de nulidad con restitucion de cantidades e
  intereses. Cubre gastos de formalizacion de hipoteca, clausula suelo, IRPH, comision de apertura,
  interes de demora, tarjeta revolving u otras condiciones no negociadas individualmente. NO usar para
  contratos entre empresarios sin consumidor, para clausulas negociadas individualmente, ni para
  reclamaciones ajenas al derecho de consumo.
when_to_use: |
  - El usuario es un consumidor (o su representante) que quiere impugnar una clausula predispuesta de un contrato de adhesion.
  - El usuario quiere recuperar cantidades cobradas en virtud de una clausula que considera abusiva (gastos, comisiones, intereses).
  - El usuario pide una reclamacion previa a la entidad/empresa o una demanda de nulidad de clausula abusiva con restitucion.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - alcance: reclamacion extrajudicial / demanda de nulidad con restitucion
  - tipo_clausula: gastos de formalizacion de hipoteca / clausula suelo / IRPH / comision de apertura / interes de demora / tarjeta revolving / otra
  - naturaleza_reclamante: consumidor persona fisica (o representante legal)
  - datos_reclamante: nombre, NIF, domicilio a efectos de notificaciones
  - datos_predisponente: entidad o empresa (banco, financiera, prestador de servicios), CIF, domicilio
  - datos_contrato: tipo de contrato, fecha, numero, notaria y protocolo si es escritura, y clausula concreta impugnada
  - cantidades_reclamadas: importes cobrados en virtud de la clausula y su desglose documental
  - comunidad_autonoma: para fuero y para servicios de consumo autonomicos
outputs:
  - reclamacion_extrajudicial: opcional, escrito de reclamacion previa a la entidad o empresa en markdown, DRAFT
  - demanda_nulidad: opcional, demanda de nulidad de clausula abusiva con restitucion de cantidades e intereses en markdown, DRAFT
references:
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/jurisprudencia-tjue-ts-clausulas.md
  - references/lcgc-condiciones-generales.md
  - references/trlgdcu-clausulas-abusivas.md
assets:
  - assets/template-demanda-nulidad-clausula-abusiva.md
  - assets/template-reclamacion-extrajudicial-clausula-abusiva.md
---

# Reclamacion de Clausulas Abusivas en Contratos con Consumidores

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
      "rationale": "Resolver V1: la reclamación extrajudicial y la demanda de nulidad con restitución tienen assets y exigencias distintas.",
      "question": "¿Qué documento necesita?",
      "options": [
        {"id": "extrajudicial", "label": "Reclamación extrajudicial a la entidad"},
        {"id": "demanda_nulidad", "label": "Demanda de nulidad de la cláusula con restitución de cantidades"}
      ]
    },
    {
      "id": "tipo_clausula",
      "rationale": "Resolver V2: cada tipo de cláusula tiene su propio encuadre normativo y su propia doctrina, que debe verificarse en la Fase 2.1 antes de redactar.",
      "question": "¿Qué cláusula o práctica se impugna?",
      "options": [
        {"id": "gastos_hipoteca", "label": "Gastos de formalización de hipoteca"},
        {"id": "clausula_suelo", "label": "Cláusula suelo"},
        {"id": "irph", "label": "Índice de referencia IRPH"},
        {"id": "comision_apertura", "label": "Comisión de apertura"},
        {"id": "interes_demora", "label": "Interés de demora"},
        {"id": "revolving", "label": "Tarjeta revolving o crédito al consumo con interés usurario"},
        {"id": "otra", "label": "Otra condición general no negociada individualmente"}
      ]
    },
    {
      "id": "condicion_reclamante",
      "rationale": "Resolver V3: la protección frente a cláusulas abusivas exige la condición de consumidor; sin ella el régimen aplicable es distinto.",
      "question": "¿Contrató el reclamante como consumidor, al margen de una actividad empresarial o profesional?",
      "options": [
        {"id": "consumidor", "label": "Sí, como consumidor"},
        {"id": "empresario_profesional", "label": "No, contrató en el marco de su actividad empresarial o profesional"}
      ]
    }
  ]
}
```

**Correspondencia con el enrutamiento.** La Fase 1.3 nombra los vectores con los identificadores siguientes; cada uno se resuelve con la respuesta indicada de este formulario. No preguntes de nuevo nada que ya esté aquí:
- `V1` — `alcance`
- `V2` — `tipo_clausula`
- `V3` — `condicion_reclamante`

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Una vez resueltos los vectores, evalua en este orden:

- Si **V3 = empresario_profesional o profesional** → **DETENER**. El control de contenido de las clausulas abusivas del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios exige la condicion de consumidor. Fuera de ella solo caben el control de incorporacion y el de transparencia de la Ley 7/1998 sobre condiciones generales de la contratacion, con un resultado muy distinto. Explicarlo, no dar falsas expectativas y escalar a letrado. No crear documento.
- Si **V3 = consumidor** y **V1 = extrajudicial** → **HOJA EXTRAJUDICIAL**: `assets/template-reclamacion-extrajudicial-clausula-abusiva.md`.
- Si **V3 = consumidor** y **V1 = demanda_nulidad** → **HOJA DEMANDA**: `assets/template-demanda-nulidad-clausula-abusiva.md`. Si **no consta reclamacion previa a la entidad ni intento de un medio adecuado de solucion de controversias**, generar **ANTES** `assets/template-reclamacion-extrajudicial-clausula-abusiva.md`: es requisito de procedibilidad de la demanda (Arts. 264.4.º y 403.2 LEC) y su omision determina la inadmision. Advertir al cliente y ofrecer preparar la demanda despues.
- V2 no elige asset: activa dentro de la hoja elegida el bloque de fundamentacion propio del tipo de clausula (gastos de constitucion de la hipoteca, clausula suelo, IRPH, comision de apertura, interes de demora o credito revolving).
- Si **V2 = IRPH o revolving** → antes de fundamentar, **verificar con `web_search` la doctrina vigente** del Tribunal de Justicia de la Union Europea y del Tribunal Supremo: es materia en evolucion y una cita desactualizada compromete la reclamacion. No afirmar el sentido de ninguna resolucion que no se haya verificado en esta sesion.
- Si la clausula fue objeto de un **acuerdo transaccional o novacion posterior** suscrito por el cliente → advertir de que su validez depende del control de transparencia de esa novacion y **escalar**: la viabilidad exige examinar el documento.
- Si la pretension principal **no es la nulidad de una clausula** sino el cobro de una cantidad ya reconocida → **DETENER** y derivar a `reclamacion-cantidad`.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución del origen de la plantilla)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
Ejecuta esta secuencia completa; en esta materia la verificación no es opcional:


La skill verifica las fuentes oficiales en cada lanzamiento y, si detecta una version posterior, aplica la redaccion vigente al documento que redacta en el workspace del usuario, sin modificar sus propios archivos de plugin. En esta materia, ademas, verifica la jurisprudencia reciente porque es determinante y cambia con frecuencia. Ejecutar SIEMPRE esta secuencia:

- **Leer la fecha/version registrada localmente.** Consultar `references/fuentes-plantillas-validadas.md`, que llega cargada en tu contexto, y anotar la version y la fecha registradas de cada norma, para poder contrastarlas despues con la fuente oficial.
- **Consultar la fuente oficial vigente en vivo.** Invocar:
```
web_search(...)
```
Extraer: fecha del texto consolidado vigente del TRLGDCU; redaccion actual de los arts. 80 a 91 (control de incorporacion, concepto de clausula abusiva, nulidad y no integracion, lista de clausulas abusivas).

Consultar tambien la LCGC:
```
web_search(...)
```
Extraer: redaccion vigente sobre control de incorporacion (Arts. 5 y 7), nulidad (Arts. 8 y 9), Registro de Condiciones Generales y accion de cesacion (Arts. 11 y 12).

Y la LEC para la demanda (competencia, procedimiento y control de oficio):
```
web_search(...)
```

- **Verificar la JURISPRUDENCIA RECIENTE del tipo de clausula (OBLIGATORIO en esta materia).** La doctrina del TJUE y del Tribunal Supremo cambia con frecuencia y determina el resultado. Antes de redactar, invocar web_search especifica para el tipo de clausula reclamado, por ejemplo:
```
web_search("TJUE Tribunal Supremo clausula <tipo> jurisprudencia reciente <ano actual> nulidad restitucion")
```
Ejemplos de terminos por tipo: "gastos hipotecarios distribucion notaria registro gestoria", "clausula suelo transparencia retroactividad", "IRPH control transparencia", "comision de apertura", "interes de demora abusivo prestamo personal", "tarjeta revolving usura TAE". Anotar solo los criterios verificados; si una sentencia no se puede confirmar, no citarla y marcar `{{VERIFICAR}}`.

- **Comparar y aplicar cambios.** Contrastar la version oficial y jurisprudencia con la registrada en `fuentes-plantillas-validadas.md` y con las referencias del prompt (`trlgdcu-clausulas-abusivas.md`, `lcgc-condiciones-generales.md`, `jurisprudencia-tjue-ts-clausulas.md`). Si hay modificaciones:
- Aplicar en memoria la redaccion y doctrina vigente para adaptar la fundamentacion del escrito.
- Informar brevemente al usuario de que se detecto y aplico una version o doctrina mas reciente (norma/sentencia y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

- **Fallback si la fuente no es accesible.** Si `web_search` no devuelve la fuente oficial:
```
web_search("texto refundido Ley General Defensa Consumidores Usuarios clausulas abusivas articulos 80 82 83 BOE consolidado")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del TRLGDCU/LCGC en el BOE. El escrito se genera con la version de referencia y con la advertencia de jurisprudencia no verificada. Verificar manualmente antes de presentar."

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Real Decreto Legislativo 1/2007 (TRLGDCU, Arts. 80, 82 a 91), Ley 7/1998 sobre Condiciones Generales de la Contratación (LCGC, Arts. 5, 7, 8), Jurisprudencia vinculante del Tribunal de Justicia de la Unión Europea (TJUE) y del Tribunal Supremo (Pleno).
2. **Orientación Legal del Caso:**
   Informa al usuario, en registro formal, de la norma y los artículos aplicables a la ruta resuelta, con la versión vigente verificada en la Fase 2.1 y el enlace de la fuente consultada.

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** y nombrala por su ruta. Si el enrutamiento asigno varios documentos, nombralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la seccion de assets.
4. **Pregunta Explícita al Usuario (Vía Chat):** Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base predeterminada (de la sección de plantillas) o prefiere aportar su propia minuta para trabajar sobre ella pegando el texto en el chat o abriéndola en el editor?"*

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
2. **Validación de Integridad:**
   - La comprobación de integridad y contenido del archivo creado se realiza consultando prioritariamente la sección `# WORKSPACE ACTIVE DOCUMENTS` del prompt, donde el sistema mantiene siempre la última versión de todos los documentos. Solo se debe invocar `read_file` si es estrictamente necesario y en algún caso extremo (ej. el archivo no aparece en dicha sección o contenido truncado).

3. **Confirmación en Chat y Encadenamiento Inmediato:**
   - Informa al usuario de la ruta absoluta del documento creado.
   - En esa **misma respuesta**, introduce la primera sección/cláusula de la **Fase 4** y formula ya su primera pregunta, sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

### Protocolo Obligatorio de Edición
Para cada cláusula o bloque temático del documento, ejecuta estrictamente el siguiente ciclo interactivo:
```
[Pregunta al Usuario] --> [Vista Previa en texto plano] --> [¿Confirmamos?] --> [edit_file en el editor]
```
1. **Pregunta en Chat:** Solicita los datos específicos de la sección.
2. **Vista Previa:** Muestra el texto exacto redactado en texto plano en el chat.
3. **Confirmación:** Consulta al usuario si está conforme o desea algún ajuste.
4. **Persistencia en Disco:** Una vez confirmado, ejecuta `edit_file` con `old_string` y `new_string` exactos. La verificación del documento se realiza prioritariamente a través de la sección `# WORKSPACE ACTIVE DOCUMENTS`, recurriendo a `read_file` únicamente en casos extremos y estrictamente necesarios.

**Petición de grupos de datos mediante `search_clients` y `slot_filling_request`, y confirmaciones en el chat:**
- **Búsqueda prioritaria de partes e intervinientes (`search_clients` — MÁXIMA PRIORIDAD):** Siempre que la sección requiera identificar personas físicas o jurídicas (partes intervinientes, solicitantes, representados, cónyuges, empresa, administradores, interesados, etc.), **DEBES invocar `search_clients` en primer lugar** antes de solicitar datos al usuario o llamar a formularios, conforme a la regla global `REG-CLI-01` de `CLAUDE.md`. Solo si `search_clients` devuelve 0 resultados o si tras recuperar la ficha faltan campos puntuales, invocarás `slot_filling_request` exclusivamente para los campos pendientes.
- **Grupos de datos estructurados no de cliente (MANDATORIO con `slot_filling_request`):** Para datos del objeto, circunstancias del hecho, bienes, importes, deudas, expedientes o parámetros complementarios, **DEBES invocar `slot_filling_request`** pidiendo todos los campos del grupo a la vez en lote. Queda **ESTRICTAMENTE PROHIBIDO** pedir estos datos de forma fragmentada uno por uno en sucesivos turnos de chat.
- **Campos omitidos o negativa expresa (No insistencia):** Si el usuario pide explícitamente no aportar determinados campos de información, pásalos por alto de inmediato sin insistir en pedirlos ni presionar. Rellena la plantilla con los datos disponibles, conserva los no aportados como marcadores pendientes ({{NOMBRE_CAMPO}} o {{DATO_FALTANTE}}) e indica en la confirmación cuáles faltan antes de continuar con la siguiente sección.
- **Validación de sentido, no solo de formato:** razone si la respuesta tiene sentido en el contexto de lo preguntado. Si es absurda, imposible o incongruente, dialogue en el chat, señale el motivo y pida aclaración antes de volcarla al documento.

### Hoja de Ruta de Secciones y Cláusulas Condicionales

1. **Parte reclamante (Consumidor)** *(confirmación agrupada)*: nombre y apellidos, NIF, domicilio a efectos de notificaciones, condición de consumidor particular (art. 3 TRLGDCU).
2. **Entidad predisponente (Empresario / Banco)** *(confirmación agrupada)*: denominación social o entidad bancaria, CIF, domicilio social y servicio de atención al cliente (SAC).
3. **Identificación del contrato y cláusula impugnada**: tipo de operación financiera (préstamo hipotecario, crédito al consumo, tarjeta revolving), fecha de firma, notario y número de protocolo (si escritura pública), y transcripción/ubicación de la cláusula litigiosa (gastos, apertura, IRPH, multidivisa, suelo, interés de demora).
4. **Fundamentación jurídica de la abusividad**: control de transparencia material e incorporación (arts. 5 y 7 LCGC; art. 80 TRLGDCU), falta de negociación individual y desequilibrio contractual conforme a la doctrina consolidada del TJUE (Directiva 93/13/CEE) y Tribunal Supremo.
5. **Cantidades cobradas indebidamente y restitución**: desglose pormenorizado de los importes abonados (facturas de notaría, registro, gestoría, tasación o liquidaciones de intereses/comisiones), con cálculo del interés legal del dinero devengado.
6. **Petición y advertencia de acciones (Suplico)**: concesión de plazo preceptivo de respuesta formal y advertencia expresa de interposición de acciones judiciales con imposición de costas si no hay avenencia.

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

1. Verificar siempre el TRLGDCU, la LCGC y la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Verificar siempre la versión consolidada vigente de la norma en el BOE antes de redactar. Si se detectan cambios normativos, aplicar la redacción vigente en el documento a generar en el workspace sin usar versiones desactualizadas.
3. La materia se aplica SOLO a consumidores (Art. 3 TRLGDCU) frente a un predisponente (empresario) y SOLO a clausulas no negociadas individualmente (Art. 82). Si la clausula fue negociada, o ambas partes son empresarios, no procede esta via: advertir y ofrecer escalacion.
4. La jurisprudencia del TJUE (Directiva 93/13/CEE) y del Tribunal Supremo en esta materia es CAMBIANTE y decisiva. Antes de redactar, verificar SIEMPRE con web_search la jurisprudencia reciente del tipo de clausula reclamado (ver la Fase 2.1). No citar ninguna sentencia sin haberla verificado en esa consulta.
5. Posicion conservadora: no afirmar que una clausula es nula con caracter automatico o generalizado. La abusividad exige el control de incorporacion y de transparencia caso por caso (Arts. 80, 82, 83 TRLGDCU; Directiva 93/13). Presentar la pretension de nulidad como fundada, no como cosa juzgada.
6. Nunca inventar sentencias, numeros de resolucion, fechas ni doctrina. Marcar con `{{VERIFICAR}}` (doble llave, nunca corchete simple `[verificar]`: colisiona con los identificadores de privacidad `[PERSON_1]`) todo claim factual o jurisprudencial no confirmado en la Fase 1.
7. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{CUANTIA_RECLAMADA}}` (NUNCA corchete simple `[DATO]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `edit_file` posterior necesita un `oldString` unico. Nunca inventar datos, cuantias, fechas ni numeros de contrato.
8. La accion de nulidad de clausula abusiva es imprescriptible; la accion de restitucion tiene su propio regimen de prescripcion segun la jurisprudencia vigente (verificar en la Fase 1). No afirmar plazos de restitucion sin verificar.
