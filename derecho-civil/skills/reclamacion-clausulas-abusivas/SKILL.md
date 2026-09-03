---
name: reclamacion-clausulas-abusivas
description: >
  Genera escritos para reclamar la nulidad de clausulas abusivas en contratos con consumidores y la
  restitucion de las cantidades indebidamente cobradas, conforme al Texto Refundido de la Ley General
  para la Defensa de los Consumidores y Usuarios (TRLGDCU, Real Decreto Legislativo 1/2007), la Ley
  7/1998 de Condiciones Generales de la Contratacion (LCGC) y la Directiva 93/13/CEE, en su version
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
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
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
    "fase_reclamacion": {
      "type": "string",
      "description": "Fase de la reclamaci\u00f3n de nulidad (V1)",
      "enum": [
        "extrajudicial",
        "demanda_judicial"
      ]
    },
    "tipo_clausula": {
      "type": "string",
      "description": "Cl\u00e1usula contractual impugnada (V2)",
      "enum": [
        "gastos_hipotecarios",
        "clausula_suelo",
        "comision_apertura",
        "tarjeta_revolving"
      ]
    }
  },
  "required": [
    "fase_reclamacion",
    "tipo_clausula"
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
1. **Marco Legal Aplicable:** Real Decreto Legislativo 1/2007 (TRLGDCU, Arts. 80, 82 a 91), Ley 7/1998 sobre Condiciones Generales de la Contratación (LCGC, Arts. 5, 7, 8), Jurisprudencia vinculante del Tribunal de Justicia de la Unión Europea (TJUE) y del Tribunal Supremo (Pleno).
2. **Orientación Legal del Caso:**
La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. En esta materia, ademas, verifica la jurisprudencia reciente porque es determinante y cambia con frecuencia. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del TRLGDCU, de la LCGC y de la LEC.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_file(...) o web_search(...)
```
Extraer: fecha del texto consolidado vigente del TRLGDCU; redaccion actual de los arts. 80 a 91 (control de incorporacion, concepto de clausula abusiva, nulidad y no integracion, lista de clausulas abusivas).

Consultar tambien la LCGC:
```
read_file(...) o web_search(...)
```
Extraer: redaccion vigente sobre control de incorporacion (Arts. 5 y 7), nulidad (Arts. 8 y 9), Registro de Condiciones Generales y accion de cesacion (Arts. 11 y 12).

Y la LEC para la demanda (competencia, procedimiento y control de oficio):
```
read_file(...) o web_search(...)
```

**1.3 — Verificar la JURISPRUDENCIA RECIENTE del tipo de clausula (OBLIGATORIO en esta materia).** La doctrina del TJUE y del Tribunal Supremo cambia con frecuencia y determina el resultado. Antes de redactar, invocar web_search especifica para el tipo de clausula reclamado, por ejemplo:
```
web_search("TJUE Tribunal Supremo clausula <tipo> jurisprudencia reciente <ano actual> nulidad restitucion")
```
Ejemplos de terminos por tipo: "gastos hipotecarios distribucion notaria registro gestoria", "clausula suelo transparencia retroactividad", "IRPH control transparencia", "comision de apertura", "interes de demora abusivo prestamo personal", "tarjeta revolving usura TAE". Anotar solo los criterios verificados; si una sentencia no se puede confirmar, no citarla y marcar `{{VERIFICAR}}`.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior, el texto de los articulos ha cambiado, o la jurisprudencia verificada difiere de la registrada, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/trlgdcu-clausulas-abusivas.md` y/o `references/lcgc-condiciones-generales.md` con la redaccion vigente.
- Actualizar los criterios jurisprudenciales verificados en `references/jurisprudencia-tjue-ts-clausulas.md`, conservando la advertencia de que son cambiantes y deben re-verificarse.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version o doctrina mas reciente (norma/sentencia y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_file` falla (error HTTP, timeout):
```
web_search("texto refundido Ley General Defensa Consumidores Usuarios clausulas abusivas articulos 80 82 83 BOE consolidado")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del TRLGDCU/LCGC en el BOE. El escrito se genera con la version de referencia y con la advertencia de jurisprudencia no verificada. Verificar manualmente antes de presentar."
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-demanda-nulidad-clausula-abusiva.md`).
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

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. En esta materia, ademas, verifica la jurisprudencia reciente porque es determinante y cambia con frecuencia. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del TRLGDCU, de la LCGC y de la LEC.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_file(...) o web_search(...)
```
Extraer: fecha del texto consolidado vigente del TRLGDCU; redaccion actual de los arts. 80 a 91 (control de incorporacion, concepto de clausula abusiva, nulidad y no integracion, lista de clausulas abusivas).

Consultar tambien la LCGC:
```
read_file(...) o web_search(...)
```
Extraer: redaccion vigente sobre control de incorporacion (Arts. 5 y 7), nulidad (Arts. 8 y 9), Registro de Condiciones Generales y accion de cesacion (Arts. 11 y 12).

Y la LEC para la demanda (competencia, procedimiento y control de oficio):
```
read_file(...) o web_search(...)
```

**1.3 — Verificar la JURISPRUDENCIA RECIENTE del tipo de clausula (OBLIGATORIO en esta materia).** La doctrina del TJUE y del Tribunal Supremo cambia con frecuencia y determina el resultado. Antes de redactar, invocar web_search especifica para el tipo de clausula reclamado, por ejemplo:
```
web_search("TJUE Tribunal Supremo clausula <tipo> jurisprudencia reciente <ano actual> nulidad restitucion")
```
Ejemplos de terminos por tipo: "gastos hipotecarios distribucion notaria registro gestoria", "clausula suelo transparencia retroactividad", "IRPH control transparencia", "comision de apertura", "interes de demora abusivo prestamo personal", "tarjeta revolving usura TAE". Anotar solo los criterios verificados; si una sentencia no se puede confirmar, no citarla y marcar `{{VERIFICAR}}`.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior, el texto de los articulos ha cambiado, o la jurisprudencia verificada difiere de la registrada, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/trlgdcu-clausulas-abusivas.md` y/o `references/lcgc-condiciones-generales.md` con la redaccion vigente.
- Actualizar los criterios jurisprudenciales verificados en `references/jurisprudencia-tjue-ts-clausulas.md`, conservando la advertencia de que son cambiantes y deben re-verificarse.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version o doctrina mas reciente (norma/sentencia y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_file` falla (error HTTP, timeout):
```
web_search("texto refundido Ley General Defensa Consumidores Usuarios clausulas abusivas articulos 80 82 83 BOE consolidado")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del TRLGDCU/LCGC en el BOE. El escrito se genera con la version de referencia y con la advertencia de jurisprudencia no verificada. Verificar manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos:

**Bloque A — Alcance del encargo:**
"Desea generar (1) una reclamacion extrajudicial previa a la entidad o empresa, o (2) una demanda judicial de nulidad de la clausula con restitucion de cantidades? (La reclamacion previa suele recomendarse antes de demandar.)"

**Bloque B — Tipo de clausula:**
"Que clausula desea impugnar? (1) gastos de formalizacion de hipoteca, (2) clausula suelo, (3) IRPH, (4) comision de apertura, (5) interes de demora, (6) tarjeta revolving, (7) otra (describala)."

**Bloque C — Condicion de consumidor y del predisponente:**
- Que el reclamante actuo como consumidor (persona fisica ajena a actividad empresarial o profesional, Art. 3 TRLGDCU).
- Datos del reclamante: nombre, NIF, domicilio a efectos de notificaciones.
- Datos del predisponente: entidad o empresa, CIF, domicilio.

**Bloque D — Datos del contrato y de la clausula:**
- Tipo de contrato, fecha, numero. Si es escritura publica: notaria y numero de protocolo.
- Transcripcion o descripcion de la clausula concreta impugnada.
- Si la clausula fue o no negociada individualmente (por defecto, condicion general no negociada).

**Bloque E — Cantidades cobradas y prueba documental:**
- Importes efectivamente cobrados en virtud de la clausula, con su desglose (facturas de gestoria, aranceles de notaria y registro, cuadro de amortizacion, extractos, liquidaciones).
- Documentos que acreditan cada pago.

**Bloque F — Localizacion (fuero y consumo autonomico):**
"En que comunidad autonoma y municipio reside el consumidor? (Para el fuero del Art. 52.3 LEC y para orientar sobre los servicios de consumo autonomicos.)"

### Paso 3 — Validacion de la pretension

Antes de redactar, validar:

a) **Ambito subjetivo:** que el reclamante es consumidor y el predisponente es empresario (Art. 3 TRLGDCU). Si no, no procede esta via: advertir y ofrecer escalacion.

b) **Condicion general no negociada (Art. 82.1 TRLGDCU; Art. 1 LCGC):** que la clausula fue predispuesta e impuesta sin negociacion individual. Si fue negociada, advertir de que el control de contenido no opera igual.

c) **Control de incorporacion y de transparencia (Arts. 5 y 7 LCGC; Art. 80 TRLGDCU):** valorar si la clausula supera los requisitos de claridad, concrecion, sencillez y accesibilidad, y si el consumidor pudo comprender su carga economica y juridica.

d) **Control de contenido (Arts. 82, 85-90 TRLGDCU):** valorar si causa, en contra de la buena fe, un desequilibrio importante en perjuicio del consumidor.

e) **Jurisprudencia verificada (Paso 1.3):** encuadrar la clausula en los criterios TJUE/TS confirmados, con posicion conservadora. No prometer resultado.

f) **Restitucion:** si la clausula es nula, precisar el efecto restitutorio (Art. 83 TRLGDCU y jurisprudencia): devolucion de lo pagado con intereses. No afirmar plazos de prescripcion de la restitucion sin verificar en el Paso 1.

### Paso 4 — Generacion de los documentos

Seleccionar la plantilla segun el alcance:
- Reclamacion previa: `assets/template-reclamacion-extrajudicial-clausula-abusiva.md`
- Demanda: `assets/template-demanda-nulidad-clausula-abusiva.md`

Invocar:
```
create_file(...)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado conservan el placeholder propio del asset en doble llave (nunca corchete simple). Los claims factuales o jurisprudenciales no verificados se marcan `{{VERIFICAR}}`.

Aplicar el estilo de `references/estilo-redaccion-escritos.md`: escrito claro y ordenado, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos ni citas largas, y SUPLICO ajustado a la nulidad y la restitucion pedidas.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1) y, en su caso, la nota de jurisprudencia verificada o `{{VERIFICAR}}`.
- Identifica correctamente al consumidor, al predisponente y la clausula impugnada.
- Expresa con claridad el control de incorporacion/transparencia/contenido y el efecto restitutorio, con las cantidades desglosadas.
- Sigue el estilo de redaccion clara (hechos y fundamentos numerados, una idea por parrafo).

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado antes de su presentacion.
2. Version del TRLGDCU/LCGC verificada: [fecha extraida en Paso 1].
3. La jurisprudencia del TJUE y del Tribunal Supremo en materia de clausulas abusivas es cambiante; los criterios citados se verificaron el {{fecha_verificacion_jurisprudencia}} y deben confirmarse antes de presentar. Los claims marcados {{VERIFICAR}} no han sido confirmados.
4. La abusividad exige un analisis caso por caso (control de incorporacion, transparencia y contenido). No existe nulidad automatica generalizada.
5. La accion de nulidad es imprescriptible; la accion de restitucion tiene su propio regimen de prescripcion, que debe confirmarse con la jurisprudencia vigente.
6. Para la demanda, la competencia territorial corresponde, a eleccion del consumidor, a su propio domicilio (Art. 52.3 LEC). Verificar la preceptividad de abogado y procurador segun la cuantia.
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

1. Verificar siempre el TRLGDCU, la LCGC y la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada.
3. La materia se aplica SOLO a consumidores (Art. 3 TRLGDCU) frente a un predisponente (empresario) y SOLO a clausulas no negociadas individualmente (Art. 82). Si la clausula fue negociada, o ambas partes son empresarios, no procede esta via: advertir y ofrecer escalacion.
4. La jurisprudencia del TJUE (Directiva 93/13/CEE) y del Tribunal Supremo en esta materia es CAMBIANTE y decisiva. Antes de redactar, verificar SIEMPRE con web_search la jurisprudencia reciente del tipo de clausula reclamado (ver Paso 1.3). No citar ninguna sentencia sin haberla verificado en esa consulta.
5. Posicion conservadora: no afirmar que una clausula es nula con caracter automatico o generalizado. La abusividad exige el control de incorporacion y de transparencia caso por caso (Arts. 80, 82, 83 TRLGDCU; Directiva 93/13). Presentar la pretension de nulidad como fundada, no como cosa juzgada.
6. Nunca inventar sentencias, numeros de resolucion, fechas ni doctrina. Marcar con `{{VERIFICAR}}` (doble llave, nunca corchete simple `[verificar]`: colisiona con los identificadores de privacidad `[PERSON_1]`) todo claim factual o jurisprudencial no confirmado en el Paso 1.
7. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{cuantia_reclamada}}` (NUNCA corchete simple `[DATO]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `Edit` posterior necesita un `oldString` unico. Nunca inventar datos, cuantias, fechas ni numeros de contrato.
8. La accion de nulidad de clausula abusiva es imprescriptible; la accion de restitucion tiene su propio regimen de prescripcion segun la jurisprudencia vigente (verificar en el Paso 1). No afirmar plazos de restitucion sin verificar.

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. En esta materia, ademas, verifica la jurisprudencia reciente porque es determinante y cambia con frecuencia. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del TRLGDCU, de la LCGC y de la LEC.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_file(...) o web_search(...)
```
Extraer: fecha del texto consolidado vigente del TRLGDCU; redaccion actual de los arts. 80 a 91 (control de incorporacion, concepto de clausula abusiva, nulidad y no integracion, lista de clausulas abusivas).

Consultar tambien la LCGC:
```
read_file(...) o web_search(...)
```
Extraer: redaccion vigente sobre control de incorporacion (Arts. 5 y 7), nulidad (Arts. 8 y 9), Registro de Condiciones Generales y accion de cesacion (Arts. 11 y 12).

Y la LEC para la demanda (competencia, procedimiento y control de oficio):
```
read_file(...) o web_search(...)
```

**1.3 — Verificar la JURISPRUDENCIA RECIENTE del tipo de clausula (OBLIGATORIO en esta materia).** La doctrina del TJUE y del Tribunal Supremo cambia con frecuencia y determina el resultado. Antes de redactar, invocar web_search especifica para el tipo de clausula reclamado, por ejemplo:
```
web_search("TJUE Tribunal Supremo clausula <tipo> jurisprudencia reciente <ano actual> nulidad restitucion")
```
Ejemplos de terminos por tipo: "gastos hipotecarios distribucion notaria registro gestoria", "clausula suelo transparencia retroactividad", "IRPH control transparencia", "comision de apertura", "interes de demora abusivo prestamo personal", "tarjeta revolving usura TAE". Anotar solo los criterios verificados; si una sentencia no se puede confirmar, no citarla y marcar `{{VERIFICAR}}`.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior, el texto de los articulos ha cambiado, o la jurisprudencia verificada difiere de la registrada, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/trlgdcu-clausulas-abusivas.md` y/o `references/lcgc-condiciones-generales.md` con la redaccion vigente.
- Actualizar los criterios jurisprudenciales verificados en `references/jurisprudencia-tjue-ts-clausulas.md`, conservando la advertencia de que son cambiantes y deben re-verificarse.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version o doctrina mas reciente (norma/sentencia y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_file` falla (error HTTP, timeout):
```
web_search("texto refundido Ley General Defensa Consumidores Usuarios clausulas abusivas articulos 80 82 83 BOE consolidado")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del TRLGDCU/LCGC en el BOE. El escrito se genera con la version de referencia y con la advertencia de jurisprudencia no verificada. Verificar manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos:

**Bloque A — Alcance del encargo:**
"Desea generar (1) una reclamacion extrajudicial previa a la entidad o empresa, o (2) una demanda judicial de nulidad de la clausula con restitucion de cantidades? (La reclamacion previa suele recomendarse antes de demandar.)"

**Bloque B — Tipo de clausula:**
"Que clausula desea impugnar? (1) gastos de formalizacion de hipoteca, (2) clausula suelo, (3) IRPH, (4) comision de apertura, (5) interes de demora, (6) tarjeta revolving, (7) otra (describala)."

**Bloque C — Condicion de consumidor y del predisponente:**
- Que el reclamante actuo como consumidor (persona fisica ajena a actividad empresarial o profesional, Art. 3 TRLGDCU).
- Datos del reclamante: nombre, NIF, domicilio a efectos de notificaciones.
- Datos del predisponente: entidad o empresa, CIF, domicilio.

**Bloque D — Datos del contrato y de la clausula:**
- Tipo de contrato, fecha, numero. Si es escritura publica: notaria y numero de protocolo.
- Transcripcion o descripcion de la clausula concreta impugnada.
- Si la clausula fue o no negociada individualmente (por defecto, condicion general no negociada).

**Bloque E — Cantidades cobradas y prueba documental:**
- Importes efectivamente cobrados en virtud de la clausula, con su desglose (facturas de gestoria, aranceles de notaria y registro, cuadro de amortizacion, extractos, liquidaciones).
- Documentos que acreditan cada pago.

**Bloque F — Localizacion (fuero y consumo autonomico):**
"En que comunidad autonoma y municipio reside el consumidor? (Para el fuero del Art. 52.3 LEC y para orientar sobre los servicios de consumo autonomicos.)"

### Paso 3 — Validacion de la pretension

Antes de redactar, validar:

a) **Ambito subjetivo:** que el reclamante es consumidor y el predisponente es empresario (Art. 3 TRLGDCU). Si no, no procede esta via: advertir y ofrecer escalacion.

b) **Condicion general no negociada (Art. 82.1 TRLGDCU; Art. 1 LCGC):** que la clausula fue predispuesta e impuesta sin negociacion individual. Si fue negociada, advertir de que el control de contenido no opera igual.

c) **Control de incorporacion y de transparencia (Arts. 5 y 7 LCGC; Art. 80 TRLGDCU):** valorar si la clausula supera los requisitos de claridad, concrecion, sencillez y accesibilidad, y si el consumidor pudo comprender su carga economica y juridica.

d) **Control de contenido (Arts. 82, 85-90 TRLGDCU):** valorar si causa, en contra de la buena fe, un desequilibrio importante en perjuicio del consumidor.

e) **Jurisprudencia verificada (Paso 1.3):** encuadrar la clausula en los criterios TJUE/TS confirmados, con posicion conservadora. No prometer resultado.

f) **Restitucion:** si la clausula es nula, precisar el efecto restitutorio (Art. 83 TRLGDCU y jurisprudencia): devolucion de lo pagado con intereses. No afirmar plazos de prescripcion de la restitucion sin verificar en el Paso 1.

### Paso 4 — Generacion de los documentos

Seleccionar la plantilla segun el alcance:
- Reclamacion previa: `assets/template-reclamacion-extrajudicial-clausula-abusiva.md`
- Demanda: `assets/template-demanda-nulidad-clausula-abusiva.md`

Invocar:
```
create_file(...)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado conservan el placeholder propio del asset en doble llave (nunca corchete simple). Los claims factuales o jurisprudenciales no verificados se marcan `{{VERIFICAR}}`.

Aplicar el estilo de `references/estilo-redaccion-escritos.md`: escrito claro y ordenado, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos ni citas largas, y SUPLICO ajustado a la nulidad y la restitucion pedidas.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1) y, en su caso, la nota de jurisprudencia verificada o `{{VERIFICAR}}`.
- Identifica correctamente al consumidor, al predisponente y la clausula impugnada.
- Expresa con claridad el control de incorporacion/transparencia/contenido y el efecto restitutorio, con las cantidades desglosadas.
- Sigue el estilo de redaccion clara (hechos y fundamentos numerados, una idea por parrafo).

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado antes de su presentacion.
2. Version del TRLGDCU/LCGC verificada: [fecha extraida en Paso 1].
3. La jurisprudencia del TJUE y del Tribunal Supremo en materia de clausulas abusivas es cambiante; los criterios citados se verificaron el {{fecha_verificacion_jurisprudencia}} y deben confirmarse antes de presentar. Los claims marcados {{VERIFICAR}} no han sido confirmados.
4. La abusividad exige un analisis caso por caso (control de incorporacion, transparencia y contenido). No existe nulidad automatica generalizada.
5. La accion de nulidad es imprescriptible; la accion de restitucion tiene su propio regimen de prescripcion, que debe confirmarse con la jurisprudencia vigente.
6. Para la demanda, la competencia territorial corresponde, a eleccion del consumidor, a su propio domicilio (Art. 52.3 LEC). Verificar la preceptividad de abogado y procurador segun la cuantia.
```

### Supuestos Fuera de Alcance (Cómo NO usar esta skill)

- No usar cuando ambas partes son empresarios o profesionales: la proteccion del TRLGDCU es del consumidor.
- No usar para clausulas negociadas individualmente ni para el objeto principal del contrato cuando sea claro y comprensible (salvo falta de transparencia).
- No usar para revisar o redactar el contrato de prestamo o de servicio en si (eso es otra skill: generacion o revision contractual).
- No usar para reclamaciones de consumo ajenas a clausulas abusivas (garantias de producto, viajes combinados, etc.) sin adaptacion.
- No usar para emitir un dictamen sobre las probabilidades de exito de un litigio concreto: derivar a derivación formal.

### Escalación a Letrado
En supuestos de litigiosidad compleja, fraude legal, derechos forales no soportados o riesgo procesal grave, abstente de redactar y deriva al usuario a un letrado en ejercicio.