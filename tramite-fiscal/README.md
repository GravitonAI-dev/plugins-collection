# tramite-fiscal

Plugin de revision de clausulas fiscales en contratos SaaS para el equipo de procurement.

## Que hace

- Revision de terminos y condiciones de proveedores SaaS pequenos.
- Identificacion de clausulas fiscales (IVA, withholding tax, tax residency, etc.).
- Checklist de riesgos con triage VERDE/AMARILLO/ROJO.
- Generacion de memo de triage en formato DRAFT para revision profesional.

## Que NO hace

- No替代 a un abogado en temas fiscales complejos o multinacionales.
- No genera textos legales ni propone clausulas alternativas.
- No realiza calculos fiscales ni advise sobre regimenes especificos.
- No revisa contratos de otras verticales (comercial, laboral, etc.).

## Skills

### tramite-fiscal

Revision de clausulas fiscales en contratos SaaS con checklist de riesgos.

**Inputs:**
- Texto del contrato o terms & conditions pegado por el usuario.

**Outputs:**
- Memo de triage con veredicto VERDE/AMARILLO/ROJO, issues detectados y recomendacion.

## Dependencias

### MCP servers
Ninguno.

### Tools
Ninguna.

## Instalacion

Este plugin se instala via el marketplace de plugins de GravitonAI. No requiere configuracion adicional.

## Tuning

- Jurisdiccion: agnostica por defecto. Ajustar en `CLAUDE.md` segun el equipo.
- Para cambiar el comportamiento del triage, editar el procedimiento en `skills/tramite-fiscal/SKILL.md`.