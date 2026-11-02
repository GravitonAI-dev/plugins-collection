# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `masc-acuerdos`. Registra las fuentes normativas que la skill
> verifica en cada lanzamiento y las plantillas sobre las que se construyen sus assets.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte expresamente al usuario de que la verificación queda pendiente.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Ley Orgánica 1/2025, de 2 de enero, de medidas en materia de eficiencia del Servicio Público de Justicia | BOE-A-2025-76 | publicada 03/01/2025; requisito de procedibilidad en vigor desde 03/04/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| Ley 1/2000, de 7 de enero, de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| Código Civil (texto consolidado) — transacción, arts. 1809 y siguientes | BOE-A-1889-4763 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| Ley 5/2012, de mediación en asuntos civiles y mercantiles | BOE-A-2012-9112 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2012-9112 |

**Preceptos que la skill debe localizar y verificar en cada lanzamiento, sin citarlos de memoria:**

- El precepto de la Ley Orgánica 1/2025 que enumera los medios que se consideran adecuados.
- El precepto que enumera las materias exceptuadas del requisito de procedibilidad.
- El precepto que regula el efecto de la actividad negociadora sobre la prescripción y sobre la caducidad, y el momento en que el cómputo se reanuda.
- El precepto que fija cuándo se entiende intentada la actividad negociadora sin acuerdo.
- El precepto que fija el plazo máximo de duración de la actividad negociadora.
- El umbral de interés económico a partir del cual la asistencia letrada es preceptiva, y el supuesto en que lo es por razón del medio empleado.
- Los artículos de la Ley 1/2000 reformados por la Ley Orgánica 1/2025 en materia de admisión de la demanda y de documentos que deben acompañarla.
- El precepto que regula el efecto de la conducta de las partes durante el intento sobre la imposición de costas.

---

## Base de las plantillas

Los assets de esta skill no reproducen ningún modelo normalizado oficial: a la fecha de creación de la skill no existe un modelo oficial publicado para los documentos del MASC. Se construyen sobre la estructura documental propia de cada figura:

| Asset | Base |
|---|---|
| `template-requerimiento-negociacion-masc.md` | Estructura del requerimiento fehaciente, con la delimitación del objeto y el plazo de respuesta |
| `template-acta-intento-masc.md` | Estructura de acta acreditativa: partes, medio, objeto, desarrollo fechado y resultado |
| `template-oferta-vinculante.md` | Estructura de oferta contractual con plazo de aceptación y carácter vinculante |
| `template-acuerdo-transaccional-masc.md` | Estructura del contrato de transacción del Código Civil |
| `template-declaracion-responsable-imposibilidad-masc.md` | Estructura de declaración responsable con relación de diligencias practicadas |

Si el Ministerio de Justicia, el Consejo General del Poder Judicial o el Consejo General de la Abogacía publican modelos normalizados para estos documentos, la skill los verifica con `web_search` y aplica su estructura al documento que redacta.

---

## Guías de estilo de redacción

| Recurso | Uso |
|---|---|
| Guía de redacción jurídica clara (Ministerio de Justicia) | Frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminología y corrección del lenguaje jurídico |
