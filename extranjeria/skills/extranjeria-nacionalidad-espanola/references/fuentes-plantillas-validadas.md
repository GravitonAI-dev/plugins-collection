# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `extranjeria-nacionalidad-espanola`.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin.

**Además de la norma, comprueba las instrucciones administrativas.** En esta materia el criterio con el que se resuelve lo fija con frecuencia una instrucción, no el texto legal.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Código Civil — adquisición de la nacionalidad | BOE-A-1889-4763 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| Ley Orgánica 4/2000 sobre derechos y libertades de los extranjeros en España | BOE-A-2000-544 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2000-544 |
| Reglamento de la Ley Orgánica 4/2000, aprobado por Real Decreto 1155/2024 | BOE-A-2024-24099 | publicado 20/11/2024; en vigor desde 20/05/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099 |
| Ley 20/2011 del Registro Civil | BOE-A-2011-12628 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2011-12628 |

**Cambio normativo ya verificado:** el **Real Decreto 557/2011**, anterior Reglamento de Extranjería, **está derogado** por el Real Decreto 1155/2024, en vigor desde el **20 de mayo de 2025**. Ninguna plantilla ni referencia de este plugin puede apoyarse en el reglamento anterior.

---

## Preceptos y datos que la skill localiza y verifica en cada lanzamiento

- Los plazos de residencia legal exigibles por cada vía, y los supuestos que dan derecho a cada plazo reducido.
- Que se entiende por residencia legal, continuada e inmediatamente anterior, y que rompe la continuidad.
- El régimen de las pruebas de integración, su vigencia y sus exenciones por edad, capacidad o nacionalidad.
- El plazo de resolución del expediente y el sentido del silencio.
- El plazo para comparecer a jurar o prometer tras la concesión, y la consecuencia de dejarlo transcurrir.
- La denominación, el código y el importe vigente del modelo de tasa.
- El órgano competente y la sede de presentación vigentes.

---

## Base de las plantillas

Los assets no reproducen ningún formulario oficial: reúnen y ordenan el contenido que este exige.

| Asset | Base |
|---|---|
| `template-hoja-datos-solicitud-nacionalidad.md` | Campos del formulario oficial de solicitud, ordenados por bloques |
| `template-escrito-motivado-nacionalidad.md` | Estructura de escrito administrativo: expone, solicita, otrosíes y relación documental |
| `template-checklist-documentacion-nacionalidad.md` | Relación documental con su estado, su vigencia y su régimen de legalización |
| `template-escrito-subsanacion.md` | Contestación punto por punto al requerimiento, en su mismo orden |
| `template-alegaciones-propuesta-desestimatoria.md` | Alegaciones en trámite de audiencia previo a la resolución |

`template-checklist-documentacion-nacionalidad.md` no es un documento a presentar, sino un instrumento de control del expediente. Lleva el prefijo `template-` porque se rellena con marcadores `{{...}}`, como exige la guía de autoría.
