---
name: reclamacion-clausulas-abusivas
title: Reclamación de cláusulas abusivas
i18n:
  en:
    name: unfair-terms-claim
    title: Unfair terms claim
    description: >
      Generates filings to claim the nullity of unfair terms in consumer contracts and
      restitution of amounts unduly charged, under the **Consolidated General Act for the
      Protection of Consumers and Users (TRLGDCU, Royal Legislative Decree 1/2007)**, which
      defines basic consumer rights and the control of unfair terms, **Law 7/1998 on General
      Contract Terms (LCGC)** and **Directive 93/13/EEC**, in the consolidated version verified
      in the BOE. At the user's choice it produces an OUT-OF-COURT CLAIM to the bank or company,
      or a CLAIM for nullity with restitution of amounts and interest. It covers mortgage
      arrangement costs, floor clauses, IRPH, arrangement fees, default interest, revolving
      cards and other terms not individually negotiated. Do not use for contracts between
      businesses with no consumer, for individually negotiated terms, or for claims outside
      consumer law.
description: >
  Genera escritos para reclamar la nulidad de cláusulas abusivas en contratos con consumidores y la
  restitución de las cantidades indebidamente cobradas, conforme al **Texto Refundido de la Ley General
  para la Defensa de los Consumidores y Usuarios (TRLGDCU, Real Decreto Legislativo 1/2007)**, que define los derechos básicos del consumidor y el control de las cláusulas abusivas, la **Ley
  7/1998 de Condiciones Generales de la Contratación (LCGC)** y la **Directiva 93/13/CEE**, en su versión
  consolidada vigente verificada en el BOE. Produce, a elección del usuario, una RECLAMACIÓN
  EXTRAJUDICIAL a la entidad o empresa, o una DEMANDA de nulidad con restitución de cantidades e
  intereses. Cubre gastos de formalización de hipoteca, cláusula suelo, IRPH, comisión de apertura,
  interés de demora, tarjeta revolving u otras condiciones no negociadas individualmente. NO usar para
  contratos entre empresarios sin consumidor, para cláusulas negociadas individualmente, ni para
  reclamaciones ajenas al derecho de consumo.
when_to_use: |
  - El usuario es un consumidor (o su representante) que quiere impugnar una cláusula predispuesta de un contrato de adhesión.
  - El usuario quiere recuperar cantidades cobradas en virtud de una cláusula que considera abusiva (gastos, comisiones, intereses).
  - El usuario pide una reclamación previa a la entidad/empresa o una demanda de nulidad de cláusula abusiva con restitución.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario
  - alcance: reclamación extrajudicial / demanda de nulidad con restitución
  - tipo_clausula: gastos de formalización de hipoteca / cláusula suelo / IRPH / comisión de apertura / interés de demora / tarjeta revolving / otra
  - naturaleza_reclamante: consumidor persona física (o representante legal)
  - datos_reclamante: nombre, NIF, domicilio a efectos de notificaciones
  - datos_predisponente: entidad o empresa (banco, financiera, prestador de servicios), CIF, domicilio
  - datos_contrato: tipo de contrato, fecha, número, notaría y protocolo si es escritura, y cláusula concreta impugnada
  - cantidades_reclamadas: importes cobrados en virtud de la cláusula y su desglose documental
  - comunidad_autonoma: para fuero y para servicios de consumo autonómicos
outputs:
  - reclamacion_extrajudicial: opcional, escrito de reclamación previa a la entidad o empresa en markdown, DRAFT
  - demanda_nulidad: opcional, demanda de nulidad de cláusula abusiva con restitución de cantidades e intereses en markdown, DRAFT
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

# Reclamación de Cláusulas Abusivas en Contratos con Consumidores

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
Una vez resueltos los vectores, evalúa en este orden:

- Si **V3 = empresario_profesional o profesional** → **DETENER**. El control de contenido de las cláusulas abusivas del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios exige la condición de consumidor. Fuera de ella solo caben el control de incorporación y el de transparencia de la Ley 7/1998 sobre condiciones generales de la contratación, con un resultado muy distinto. Explicarlo, no dar falsas expectativas y escalar a letrado. No crear documento.
- Si **V3 = consumidor** y **V1 = extrajudicial** → **HOJA EXTRAJUDICIAL**: `assets/template-reclamacion-extrajudicial-clausula-abusiva.md`.
- Si **V3 = consumidor** y **V1 = demanda_nulidad** → **HOJA DEMANDA**: `assets/template-demanda-nulidad-clausula-abusiva.md`. Si **no consta reclamación previa a la entidad ni intento de un medio adecuado de solución de controversias**, generar **ANTES** `assets/template-reclamacion-extrajudicial-clausula-abusiva.md`: es requisito de procedibilidad de la demanda (Arts. 264.4.º y 403.2 LEC) y su omisión determina la inadmisión. Advertir al cliente y ofrecer preparar la demanda después.
- V2 no elige asset: activa dentro de la hoja elegida el bloque de fundamentación propio del tipo de cláusula (gastos de constitución de la hipoteca, cláusula suelo, IRPH, comisión de apertura, interés de demora o crédito revolving).
- Si **V2 = IRPH o revolving** → antes de fundamentar, **verificar con `web_search` la doctrina vigente** del Tribunal de Justicia de la Unión Europea y del Tribunal Supremo: es materia en evolución y una cita desactualizada compromete la reclamación. No afirmar el sentido de ninguna resolución que no se haya verificado en esta sesión.
- Si la cláusula fue objeto de un **acuerdo transaccional o novación posterior** suscrito por el cliente → advertir de que su validez depende del control de transparencia de esa novación y **escalar**: la viabilidad exige examinar el documento.
- Si la pretensión principal **no es la nulidad de una cláusula** sino el cobro de una cantidad ya reconocida → **DETENER** y derivar a `reclamacion-cantidad`.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

En esta fase compartes en el chat el plan de trabajo y marco legal, y consultas preceptivamente la plantilla base mediante formulario interactivo de opciones cerradas (`restricted_human_in_the_loop_request`), aplicando rigurosamente el protocolo universal de `REG-AST-01` de `CLAUDE.md`:

### 2.1 Verificación Normativa Interna
Ejecuta esta secuencia completa; en esta materia la verificación no es opcional:


La skill verifica las fuentes oficiales en cada lanzamiento y, si detecta una versión posterior, aplica la redacción vigente al documento que redacta en el workspace del usuario, sin modificar sus propios archivos de plugin. En esta materia, además, verifica la jurisprudencia reciente porque es determinante y cambia con frecuencia. Ejecutar SIEMPRE esta secuencia:

- **Leer la fecha/versión registrada localmente.** Consultar `references/fuentes-plantillas-validadas.md`, que llega cargada en tu contexto, y anotar la versión y la fecha registradas de cada norma, para poder contrastarlas después con la fuente oficial.
- **Consultar la fuente oficial vigente en vivo.** Invocar:
```
web_search(...)
```
Extraer: fecha del texto consolidado vigente del TRLGDCU; redacción actual de los arts. 80 a 91 (control de incorporación, concepto de cláusula abusiva, nulidad y no integración, lista de cláusulas abusivas).

Consultar también la LCGC:
```
web_search(...)
```
Extraer: redacción vigente sobre control de incorporación (Arts. 5 y 7), nulidad (Arts. 8 y 9), Registro de Condiciones Generales y acción de cesación (Arts. 11 y 12).

Y la LEC para la demanda (competencia, procedimiento y control de oficio):
```
web_search(...)
```

- **Verificar la JURISPRUDENCIA RECIENTE del tipo de cláusula (OBLIGATORIO en esta materia).** La doctrina del TJUE y del Tribunal Supremo cambia con frecuencia y determina el resultado. Antes de redactar, invocar web_search específica para el tipo de cláusula reclamado, por ejemplo:
```
web_search("TJUE Tribunal Supremo cláusula <tipo> jurisprudencia reciente <año actual> nulidad restitución")
```
Ejemplos de términos por tipo: "gastos hipotecarios distribución notaría registro gestoría", "cláusula suelo transparencia retroactividad", "IRPH control transparencia", "comisión de apertura", "interés de demora abusivo préstamo personal", "tarjeta revolving usura TAE". Anotar solo los criterios verificados; si una sentencia no se puede confirmar, no citarla y marcar `{{VERIFICAR}}`.

- **Comparar y aplicar cambios.** Contrastar la versión oficial y jurisprudencia con la registrada en `fuentes-plantillas-validadas.md` y con las referencias del prompt (`trlgdcu-clausulas-abusivas.md`, `lcgc-condiciones-generales.md`, `jurisprudencia-tjue-ts-clausulas.md`). Si hay modificaciones:
- Aplicar en memoria la redacción y doctrina vigente para adaptar la fundamentación del escrito.
- Informar brevemente al usuario de que se detectó y aplico una versión o doctrina más reciente (norma/sentencia y fecha).

No redactar ningún documento hasta haber completado esta actualización. Nunca usar una versión desactualizada.

- **Fallback si la fuente no es accesible.** Si `web_search` no devuelve la fuente oficial:
```
web_search("texto refundido Ley General Defensa Consumidores Usuarios cláusulas abusivas artículos 80 82 83 BOE consolidado")
```
Si también falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la versión vigente del TRLGDCU/LCGC en el BOE. El escrito se genera con la versión de referencia y con la advertencia de jurisprudencia no verificada. Verificar manualmente antes de presentar."

### 2.2 Mensaje de Plan de Acción y Elección de Plantilla
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Real Decreto Legislativo 1/2007 (TRLGDCU, Arts. 80, 82 a 91), Ley 7/1998 sobre Condiciones Generales de la Contratación (LCGC, Arts. 5, 7, 8), Jurisprudencia vinculante del Tribunal de Justicia de la Unión Europea (TJUE) y del Tribunal Supremo (Pleno).
2. **Orientación Legal del Caso:**
   Informa al usuario, en registro formal, de la norma y los artículos aplicables a la ruta resuelta, con la versión vigente verificada en la Fase 2.1 y el enlace de la fuente consultada.

3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada **que ha resuelto el enrutamiento de la Fase 1.3** (menciónala por su denominación formal, sin mostrar rutas internas ni volcar su contenido). Si el enrutamiento asigno varios documentos, nómbralos todos y en el orden en que se van a redactar. **No propongas una plantilla distinta de la enrutada** ni la primera del inventario de la sección de assets.
4. **Elección de Plantilla Base:** Aplica el protocolo universal de `REG-AST-01` (`CLAUDE.md`), convocando en ese mismo turno el formulario interactivo `restricted_human_in_the_loop_request` para que el usuario elija entre la plantilla del sistema o aportar su propia minuta.

### 2.3 Manejo Determinista de la Elección
Aplica rigurosamente el protocolo de `REG-AST-01` (`CLAUDE.md`): si se selecciona `plantilla_sistema`, carga la plantilla oficial y avanza a la **Fase 3**; si se selecciona `plantilla_usuario`, requiere la minuta (si no consta ya en el chat), ejecuta el control de legalidad y avanza a la **Fase 3**.
---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

Aplica rigurosamente la directiva `REG-DOC-01` (ciclo de creación del documento base):
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

1. **Parte reclamante (Consumidor)** *(confirmación agrupada)*: nombre y apellidos, NIF, domicilio a efectos de notificaciones, condición de consumidor particular (art. 3 TRLGDCU).
2. **Entidad predisponente (Empresario / Banco)** *(confirmación agrupada)*: denominación social o entidad bancaria, CIF, domicilio social y servicio de atención al cliente (SAC).
3. **Identificación del contrato y cláusula impugnada**: tipo de operación financiera (préstamo hipotecario, crédito al consumo, tarjeta revolving), fecha de firma, notario y número de protocolo (si escritura pública), y transcripción/ubicación de la cláusula litigiosa (gastos, apertura, IRPH, multidivisa, suelo, interés de demora).
4. **Fundamentación jurídica de la abusividad**: control de transparencia material e incorporación (arts. 5 y 7 LCGC; art. 80 TRLGDCU), falta de negociación individual y desequilibrio contractual conforme a la doctrina consolidada del TJUE (Directiva 93/13/CEE) y Tribunal Supremo.
5. **Cantidades cobradas indebidamente y restitución**: desglose pormenorizado de los importes abonados (facturas de notaría, registro, gestoría, tasación o liquidaciones de intereses/comisiones), con cálculo del interés legal del dinero devengado.
6. **Petición y advertencia de acciones (Suplico)**: concesión de plazo preceptivo de respuesta formal y advertencia expresa de interposición de acciones judiciales con imposición de costas si no hay avenencia.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Aplica rigurosamente las directivas `REG-FDB-01` y `REG-CLO-01` de `CLAUDE.md`:
1. **Menú de Revisión Final (REG-FDB-01):** Presenta el menú interactivo de 5 opciones de realimentación y revisión.
2. **Advertencias Preceptivas de Cierre (REG-CLO-01):** Al dar por finalizado el documento (opción 5), emite las advertencias obligatorias de cierre (carácter DRAFT, plazos de liquidación tributaria en 30 días hábiles cuando proceda, y elevación a instrumento público ante Notario para eficacia registral o ejecutiva).
---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre el TRLGDCU, la LCGC y la LEC en el BOE antes de redactar. Sin verificación, no proceder.
2. Verificar siempre la versión consolidada vigente de la norma en el BOE antes de redactar. Si se detectan cambios normativos, aplicar la redacción vigente en el documento a generar en el workspace sin usar versiones desactualizadas.
3. La materia se aplica SOLO a consumidores (Art. 3 TRLGDCU) frente a un predisponente (empresario) y SOLO a cláusulas no negociadas individualmente (Art. 82). Si la cláusula fue negociada, o ambas partes son empresarios, no procede esta vía: advertir y ofrecer escalación.
4. La jurisprudencia del TJUE (Directiva 93/13/CEE) y del Tribunal Supremo en esta materia es CAMBIANTE y decisiva. Antes de redactar, verificar SIEMPRE con web_search la jurisprudencia reciente del tipo de cláusula reclamado (ver la Fase 2.1). No citar ninguna sentencia sin haberla verificado en esa consulta.
5. Posición conservadora: no afirmar que una cláusula es nula con carácter automático o generalizado. La abusividad exige el control de incorporación y de transparencia caso por caso (Arts. 80, 82, 83 TRLGDCU; Directiva 93/13). Presentar la pretensión de nulidad como fundada, no como cosa juzgada.
6. Nunca inventar sentencias, números de resolución, fechas ni doctrina. Marcar con `{{VERIFICAR}}` (doble llave, nunca corchete simple `[verificar]`: colisiona con los identificadores de privacidad `[PERSON_1]`) todo claim factual o jurisprudencial no confirmado en la Fase 1.
7. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{CUANTIA_RECLAMADA}}` (NUNCA corchete simple `[DATO]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `edit_file` posterior necesita un `oldString` único. Nunca inventar datos, cuantías, fechas ni números de contrato.
8. La acción de nulidad de cláusula abusiva es imprescriptible; la acción de restitución tiene su propio régimen de prescripción según la jurisprudencia vigente (verificar en la Fase 1). No afirmar plazos de restitución sin verificar.
