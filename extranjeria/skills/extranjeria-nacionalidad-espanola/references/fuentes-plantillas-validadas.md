# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `extranjeria-nacionalidad-espanola`.

---

## Regla de verificacion permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una version posterior a la registrada, aplica la redaccion vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin.

**Ademas de la norma, comprueba las instrucciones administrativas.** En esta materia el criterio con el que se resuelve lo fija con frecuencia una instruccion, no el texto legal.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Codigo Civil — adquisicion de la nacionalidad | BOE-A-1889-4763 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| Ley Organica 4/2000 sobre derechos y libertades de los extranjeros en Espana | BOE-A-2000-544 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2000-544 |
| Reglamento de la Ley Organica 4/2000, aprobado por Real Decreto 1155/2024 | BOE-A-2024-24099 | publicado 20/11/2024; en vigor desde 20/05/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099 |
| Ley 20/2011 del Registro Civil | BOE-A-2011-12628 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2011-12628 |

**Cambio normativo ya verificado:** el **Real Decreto 557/2011**, anterior Reglamento de Extranjeria, **esta derogado** por el Real Decreto 1155/2024, en vigor desde el **20 de mayo de 2025**. Ninguna plantilla ni referencia de este plugin puede apoyarse en el reglamento anterior.

---

## Preceptos y datos que la skill localiza y verifica en cada lanzamiento

- Los plazos de residencia legal exigibles por cada via, y los supuestos que dan derecho a cada plazo reducido.
- Que se entiende por residencia legal, continuada e inmediatamente anterior, y que rompe la continuidad.
- El regimen de las pruebas de integracion, su vigencia y sus exenciones por edad, capacidad o nacionalidad.
- El plazo de resolucion del expediente y el sentido del silencio.
- El plazo para comparecer a jurar o prometer tras la concesion, y la consecuencia de dejarlo transcurrir.
- La denominacion, el codigo y el importe vigente del modelo de tasa.
- El organo competente y la sede de presentacion vigentes.

---

## Base de las plantillas

Los assets no reproducen ningun formulario oficial: reunen y ordenan el contenido que este exige.

| Asset | Base |
|---|---|
| `template-hoja-datos-solicitud-nacionalidad.md` | Campos del formulario oficial de solicitud, ordenados por bloques |
| `template-escrito-motivado-nacionalidad.md` | Estructura de escrito administrativo: expone, solicita, otrosies y relacion documental |
| `checklist-documentacion-nacionalidad.md` | Relacion documental con su estado, su vigencia y su regimen de legalizacion |
| `template-escrito-subsanacion.md` | Contestacion punto por punto al requerimiento, en su mismo orden |
| `template-alegaciones-propuesta-desestimatoria.md` | Alegaciones en tramite de audiencia previo a la resolucion |

`checklist-documentacion-nacionalidad.md` no lleva el prefijo `template-` porque no es una plantilla de documento a presentar, sino un instrumento de control del expediente.
