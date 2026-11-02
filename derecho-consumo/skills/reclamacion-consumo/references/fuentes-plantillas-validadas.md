# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `reclamacion-consumo`. Registra las fuentes normativas que la
> skill verifica en cada lanzamiento y la base sobre la que se construyen sus assets.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte de que la verificación queda pendiente.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios, aprobado por Real Decreto Legislativo 1/2007 | BOE-A-2007-20555 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555 |
| Real Decreto 713/2024, por el que se aprueba el Reglamento que regula el Sistema Arbitral de Consumo | BOE-A-2024-15208 | publicado 24/07/2024; en vigor desde 13/08/2024 | https://www.boe.es/buscar/act.php?id=BOE-A-2024-15208 |
| Ley 7/1998, sobre condiciones generales de la contratación | BOE-A-1998-8789 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-1998-8789 |
| Ley 7/2017, de resolución alternativa de litigios en materia de consumo | BOE-A-2017-12659 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2017-12659 |

**Cambio normativo relevante ya verificado:** el **Real Decreto 231/2008**, que regulaba el Sistema Arbitral de Consumo, **está derogado** por el Real Decreto 713/2024 con efectos desde el **13 de agosto de 2024**. Cualquier referencia al 231/2008 en un documento del usuario o en una plantilla ajena debe corregirse.

---

## Preceptos que la skill localiza y verifica en cada lanzamiento

- El plazo de garantía legal de los bienes y el de los servicios, y desde cuando se cuenta cada uno.
- El plazo de que dispone el consumidor para comunicar la falta de conformidad, si la norma vigente lo fija.
- El orden de prelación entre reparación, sustitución, rebaja del precio y resolución del contrato.
- El plazo de respuesta de la empresa a la hoja oficial de reclamaciones, que fija la normativa autonómica.
- El plazo de resolución del procedimiento arbitral y el régimen de la mediación previa.
- Los efectos del laudo y los supuestos tasados de la acción de anulación.

---

## Normativa autonómica (verificación obligatoria por caso)

El modelo de hoja de quejas y reclamaciones, el número de ejemplares, el organismo competente, la forma de presentación y el plazo de respuesta de la empresa **son autonómicos**. La skill los verifica con `web_search` para la comunidad autónoma del caso antes de redactar, y **no presume el procedimiento de una comunidad en otra**.

Elementos que hay que fijar por comunidad autónoma:

| Elemento | Cómo se verifica |
|---|---|
| Norma que aprueba el modelo de hoja | Boletín oficial autonómico |
| Número de ejemplares y destino de cada uno | Norma autonómica del modelo |
| Organismo competente | Dirección general de consumo autonómica u oficina municipal |
| Registro de presentación | Sede electrónica autonómica o municipal |
| Plazo de respuesta de la empresa | Norma autonómica del modelo |

---

## Base de las plantillas

Los assets no reproducen ningún impreso oficial: vuelcan el **contenido** que el impreso exige, para que pueda transcribirse o adjuntarse.

| Asset | Base |
|---|---|
| `template-reclamacion-previa-empresa.md` | Estructura de reclamación fehaciente: partes, contratación, hechos numerados, fundamento, petición, plazo y documentos |
| `template-hoja-reclamaciones.md` | Campos comunes de los modelos autonómicos de hoja de quejas y reclamaciones |
| `template-solicitud-arbitraje-consumo.md` | Contenido de la solicitud de arbitraje conforme al Reglamento del Sistema Arbitral de Consumo |
| `template-escrito-administracion-consumo.md` | Estructura de escrito administrativo: expone, solicita y documentos |
