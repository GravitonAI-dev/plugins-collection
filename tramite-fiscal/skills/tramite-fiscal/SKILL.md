---
name: tramite-fiscal
description: Revision automatica de clausulas fiscales en terminos y condiciones de proveedores SaaS pequenos con triage VERDE/AMARILLO/ROJO. NO usar para MSAs, contratos complejos, ni temas fiscales que requieran analisis multinivel.
---

> DRAFT — para revision por un abogado. No constituye asesoria legal.

## Guardrails

1. Solo revisar el texto que el usuario proporcione. No inventar ni completar clausulas.
2. Si el documento esta incompleto, indicarlo antes de emitir veredicto.
3. Marcar el output como DRAFT.
4. No proporcionar opinion legal vinculante.
5. Si se detectan clausulas ambiguas o de alto riesgo, escalar via `io.gravitonai.tools.escalate_to_attorney` o recomendar revision profesional.

## Procedimiento

1. Recibir el texto del contrato o terms & conditions del usuario.
2. Identificar clausulas relacionadas con aspectos fiscales:
   - IVA / VAT
   - Withholding tax
   - Tax residency del proveedor
   - Indemnidad fiscal (tax indemnity)
   - Responsabilidad sobre retenciones
   - Clausulas de conservacion de registros fiscales
3. Por cada clausula identificada, aplicar el checklist de riesgos:
   - VERDE: Clausula clara, estandar, sin ambiguedades fiscales.
   - AMARILLO: Clausula con potencial riesgo o ambiguedad que requiere revision profesional.
   - ROJO: Clausula con riesgo fiscal significativo o falta de proteccion requerida.
4. Verificar presencia de:
   - VAT ID o tax ID del proveedor si es relevante.
   - Declaracion de tax residency si el contrato cruza fronteras.
   - Clausula de indemnidad fiscal.
5. Generar memo de triage con:
   - Veredicto general (VERDE/AMARILLO/ROJO).
   - Lista de issues detectados.
   - Recomendacion de accion.
   - Escalacion si aplica.

## Formato de salida

```markdown
> DRAFT — para revision por un abogado. No constituye asesoria legal.

## Memo de Triage Fiscal — [Nombre del Proveedor]

| Campo | Detalle |
|---|---|
| Plugin / version | tramite-fiscal v0.1.0 |
| Skill | tramite-fiscal |
| Fecha | [fecha_actual] |

## Veredicto

**[VERDE / AMARILLO / ROJO]**

## Clausulas Detectadas

### 1. [Nombre de la clausula]
- **Tipo**: IVA / Withholding / Tax Residency / etc.
- **Texto relevante**: "[extracto de la clausula]"
- **Evaluacion**: [VERDE / AMARILLO / ROJO]
- **Issue**: [descripcion del issue si aplica]

## Recomendacion

[Resumen de la accion recomendada]

## Escalacion

[Si aplica: "Escalar a abogado interno" o "Ninguna"]
```

## Como NO se usa

- No usar para revision de MSAs o contratos complejos con múltiples jurisdicciones.
- No usar para calculos o consejos fiscales concretos.
- No usar para revision de clausulas que no sean expresamente fiscales (comerciales, laborales, etc.).
- No usar si el documento es un NDA o acuerdo de otra naturaleza.