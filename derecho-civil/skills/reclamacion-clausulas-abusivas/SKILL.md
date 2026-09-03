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

**1.2 — Consultar la fuente oficial vigente en vivo.** Invocar:
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

**1.4 — Comparar y aplicar cambios.** Contrastar la version oficial y jurisprudencia con la registrada en `fuentes-plantillas-validadas.md` y con las referencias del prompt (`trlgdcu-clausulas-abusivas.md`, `lcgc-condiciones-generales.md`, `jurisprudencia-tjue-ts-clausulas.md`). Si hay modificaciones:
- Aplicar en memoria la redaccion y doctrina vigente para adaptar la fundamentacion del escrito.
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
4. La jurisprudencia del TJUE (Directiva 93/13/CEE) y del Tribunal Supremo en esta materia es CAMBIANTE y decisiva. Antes de redactar, verificar SIEMPRE con web_search la jurisprudencia reciente del tipo de clausula reclamado (ver Paso 1.3). No citar ninguna sentencia sin haberla verificado en esa consulta.
5. Posicion conservadora: no afirmar que una clausula es nula con caracter automatico o generalizado. La abusividad exige el control de incorporacion y de transparencia caso por caso (Arts. 80, 82, 83 TRLGDCU; Directiva 93/13). Presentar la pretension de nulidad como fundada, no como cosa juzgada.
6. Nunca inventar sentencias, numeros de resolucion, fechas ni doctrina. Marcar con `{{VERIFICAR}}` (doble llave, nunca corchete simple `[verificar]`: colisiona con los identificadores de privacidad `[PERSON_1]`) todo claim factual o jurisprudencial no confirmado en el Paso 1.
7. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{cuantia_reclamada}}` (NUNCA corchete simple `[DATO]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `Edit` posterior necesita un `oldString` unico. Nunca inventar datos, cuantias, fechas ni numeros de contrato.
8. La accion de nulidad de clausula abusiva es imprescriptible; la accion de restitucion tiene su propio regimen de prescripcion segun la jurisprudencia vigente (verificar en el Paso 1). No afirmar plazos de restitucion sin verificar.
