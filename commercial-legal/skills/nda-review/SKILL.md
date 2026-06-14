---
name: nda-review
description: Triage automatico de NDAs entrantes con veredicto VERDE/AMARILLO/ROJO y memo estructurado para revision por abogado. Usar cuando el usuario pega el texto de un NDA, indica una ruta o URL a uno, o pregunta si puede firmarlo o si es aceptable. NO usar para MSAs, NDAs embebidos en otros acuerdos, contratos de trabajo ni NDAs en idiomas distintos al ingles.
---

# nda-review

Triage de NDAs entrantes. Produce un veredicto VERDE / AMARILLO / ROJO y un memo estructurado para que un abogado tome la decision final. No firma, no envia, no sube a DocuSign.

> **DRAFT — para revision por un abogado. No constituye asesoria legal.**

## Guardrails

Aplican los guardrails globales del `CLAUDE.md` raiz y los del `CLAUDE.md` del plugin. Especificos de esta skill:

1. **Header obligatorio**: todo memo de salida empieza con `> DRAFT — para revision por un abogado. No constituye asesoria legal.`
2. **Citaciones**: si no hay research tool conectado, marcar `[verificar]` en toda afirmacion sobre jurisprudencia o precedentes.
3. **Asunciones explicitas**: si algo no esta en el texto del NDA, marcar como asuncion y pedir confirmacion. Ej: "Asumimos NDA mutuo porque el texto no especifica direccion; verificar con la contraparte."
4. **Sin opinion legal final**: nunca responder "si, firme" o "no, rechace". El veredicto es triage, no decision.
5. **Idioma**: si el NDA no esta en ingles, marcar AMARILLO con la nota "requiere traduccion y revision por abogado bilingue" y abortar el resto del triage.

## Procedimiento

### Paso 1 — Recibir input

Aceptar el NDA en cualquiera de estas formas:
- Texto pegado directamente en la conversacion.
- Path local a un archivo `.txt`, `.md`, `.docx` (usar `io.gravitonai.tools.read_document`).
- URL a un Google Doc / archivo en Drive (usar `io.gravitonai.tools.read_document` con el conector `io.gravitonai.gdrive`).

Si el input esta vacio o es ambiguo, pedir aclaracion antes de continuar. No inventar contenido.

### Paso 2 — Validacion inicial

Antes de triage, descartar que el documento sea efectivamente un NDA:

- Titulo o primera seccion menciona "Non-Disclosure", "Confidentiality Agreement", "NDA", "MNDA".
- El documento trata sobre intercambio de informacion confidencial entre dos o mas partes.
- No es un MSA, contrato de servicios, acuerdo de socios, ni term sheet (esos son trabajo de otra skill/abogado).

Si no es NDA, abortar con el mensaje: "Este documento no parece ser un NDA. Escalar a abogado para clasificacion manual." Marcar veredicto como ROJO y emitir memo corto explicando por que se aborto.

### Paso 3 — Aplicar el checklist de clausulas

Leer `references/nda-clause-checklist.md` y aplicar cada item al NDA. Para cada clausula:
- Marcar el veredicto de la clausula (VERDE / AMARILLO / ROJO) segun el checklist.
- Citar el nombre exacto de la clausula y, si esta numerada, la seccion (ej: "Seccion 4 — Confidential Information").
- Si la clausula no existe en el documento, marcar como AUSENTE (no como fallo; algunos NDAs omiten clausulas rutinarias).

### Paso 4 — Determinar veredicto agregado

Reglas (estan en `CLAUDE.md` del plugin bajo "Defaults"):

- **VERDE**: todas las clausulas criticas son VERDE, no hay ninguna AMARILLO o ROJO.
- **AMARILLO**: al menos una clausula es AMARILLO y ninguna es ROJO.
- **ROJO**: al menos una clausula es ROJO, **o** falla la validacion inicial (Paso 2), **o** el NDA no esta en ingles.

### Paso 5 — Componer el memo

Usar la plantilla en `assets/nda-triage-output-template.md`. Llenar cada seccion:
- Header: `> DRAFT — para revision por un abogado. No constituye asesoria legal.`
- Metadata: contraparte (si se proporciono), fecha del triage, version del plugin, idioma, tipo de NDA (mutuo/unilateral).
- Veredicto: el veredicto agregado.
- Issues flagged: lista de clausulas que no son VERDE, con su veredicto individual y la citacion exacta.
- Recomendacion: accion sugerida segun la matriz de escalacion del `CLAUDE.md` del plugin.
- Escalacion: si el veredicto es ROJO, indicar que se creara un ticket via `io.gravitonai.tools.escalate_to_attorney`.

### Paso 6 — Escalar si corresponde

Si el veredicto es ROJO:
- Pedir confirmacion explicita al usuario antes de invocar `io.gravitonai.tools.escalate_to_attorney` (gate obligatorio).
- Si confirma, invocar el tool con: `subject` corto, `context` resumen del memo, `urgency` "high" por defecto.
- Si no confirma, devolver el memo al usuario y dejar que el lo envie manualmente.

Si el veredicto es VERDE o AMARILLO: devolver el memo. No escalar.

## Formato de salida

Ver `assets/nda-triage-output-template.md`. Estructura obligatoria:

1. Header `DRAFT`
2. Metadata
3. Veredicto (con la palabra en mayusculas y color de semaforo en texto)
4. Issues flagged (lista)
5. Recomendacion
6. Bloque de escalacion (solo si ROJO)

## Escalacion

- **Interna (al abogado del equipo)**: veredicto ROJO → `io.gravitonai.tools.escalate_to_attorney` con `urgency: "high"`. Confirmar con usuario antes de invocar.
- **Externa (a contraparte)**: nunca. Este plugin no envia NDAs. Es trabajo del abogado o de un sistema de contract lifecycle management externo.

## Como NO se usa esta skill

- No la invoques para MSAs ni acuerdos maestros. Esos son trabajo de otra skill o de revision manual.
- No la invoques para NDAs en idiomas distintos al ingles sin antes marcar AMARILLO y abortar.
- No la invoques si el "NDA" es en realidad una clausula de confidencialidad embebida en otro contrato. Extraer primero y consultar a abogado sobre el contrato completo.
