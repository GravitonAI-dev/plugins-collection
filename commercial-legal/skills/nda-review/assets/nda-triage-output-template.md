# [TRIAGE DE NDA] — <Nombre corto del NDA>

> **DRAFT — para revision por un abogado. No constituye asesoria legal.**

## Metadata

| Campo | Valor |
|---|---|
| Contraparte | <!-- {{counterparty}} --> |
| Fecha del triage | <!-- {{fecha_actual}} (YYYY-MM-DD) --> |
| Plugin / version | commercial-legal v0.1.0 |
| Skill | `nda-review` |
| Idioma del documento | <!-- {{idioma}} (ingles por default) --> |
| Tipo de NDA | <!-- {{mutuo / unilateral / por confirmar}} --> |
| Numero de paginas | <!-- {{n_paginas}} --> |

## Veredicto

# <!-- {{VERDE | AMARILLO | ROJO}} -->

<!-- Ejemplo de descripcion de una linea:
"NDA aceptable con el playbook del equipo. Auto-aprobable por paralegal."
"Necesita revision por abogado antes de firma. Hay 2 clausulas flaggeadas."
"Escalar inmediatamente. Hay clausulas fuera del playbook que requieren decision de abogado senior."
-->

## Issues flagged

<!-- Lista de clausulas que NO son VERDE. Si todo es VERDE, poner "Ninguno." -->

### 1. <!-- Nombre de la clausula --> — <!-- VERDE | AMARILLO | ROJO -->

- **Seccion**: <!-- Ej: "Seccion 4 — Confidential Information" -->
- **Hallazgo**: <!-- Que dice el NDA, con cita textual breve si es posible -->
- **Por que es flag**: <!-- Referencia al checklist (references/nda-clause-checklist.md) y la razon -->
- **Citacion**: <!-- {{fuente o [verificar]}} si no hay research tool conectado -->

### 2. <!-- ... -->

## Asunciones explicitas

<!-- Lista de cosas que se asumieron porque el NDA no las decia. Cada asuncion debe marcarse con [verificar] para que el abogado confirme. -->

- <!-- Ej: "Asumimos NDA mutuo porque el texto no especifica direccion. [verificar] con contraparte." -->
- <!-- Ej: "Asumimos jurisdiccion Delaware por el domicilio de la contraparte. [verificar] con el equipo." -->

## Recomendacion

<!-- Segun la matriz de escalacion del CLAUDE.md del plugin. -->

- <!-- Si VERDE: "Anadir al registro de contratos. No requiere escalacion. Proceder con firma electronica una vez aprobado por paralegal." -->
- <!-- Si AMARILLO: "Anadir al queue de revision del abogado responsable. No firmar hasta que el abogado complete la revision." -->
- <!-- Si ROJO: "Escalar al abogado responsable inmediatamente. Bloquear firma." -->

## Escalacion

<!-- Esta seccion SOLO aparece si el veredicto es ROJO. -->

- **Ticket creado**: <!-- {{ticket_id}} -->
- **Asignado a**: <!-- {{assigned_to}} (resuelto por el tool escalate_to_attorney) -->
- **Urgencia**: high
- **Confirmacion del usuario**: <!-- Si / No / Pendiente -->

<!-- Si el usuario todavia no confirmo la escalacion, dejar pendiente y no invocar el tool. -->

## Notas adicionales

<!-- Cualquier contexto adicional relevante: jurisprudencia aplicable (si se encontro), precedentes del equipo con la misma contraparte, comentarios del usuario. -->

- <!-- Ej: "NDA similar firmado con esta contraparte el 2024-03-15. Ver contrato archivado en {{path}}." -->
