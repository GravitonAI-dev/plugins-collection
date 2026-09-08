# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `reclamacion-consumo`. Registra las fuentes normativas que la
> skill verifica en cada lanzamiento y la base sobre la que se construyen sus assets.

---

## Regla de verificacion permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una version posterior a la registrada, aplica la redaccion vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte de que la verificacion queda pendiente.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios, aprobado por Real Decreto Legislativo 1/2007 | BOE-A-2007-20555 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555 |
| Real Decreto 713/2024, por el que se aprueba el Reglamento que regula el Sistema Arbitral de Consumo | BOE-A-2024-15208 | publicado 24/07/2024; en vigor desde 13/08/2024 | https://www.boe.es/buscar/act.php?id=BOE-A-2024-15208 |
| Ley 7/1998, sobre condiciones generales de la contratacion | BOE-A-1998-8789 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-1998-8789 |
| Ley 7/2017, de resolucion alternativa de litigios en materia de consumo | BOE-A-2017-12659 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2017-12659 |

**Cambio normativo relevante ya verificado:** el **Real Decreto 231/2008**, que regulaba el Sistema Arbitral de Consumo, **esta derogado** por el Real Decreto 713/2024 con efectos desde el **13 de agosto de 2024**. Cualquier referencia al 231/2008 en un documento del usuario o en una plantilla ajena debe corregirse.

---

## Preceptos que la skill localiza y verifica en cada lanzamiento

- El plazo de garantia legal de los bienes y el de los servicios, y desde cuando se cuenta cada uno.
- El plazo de que dispone el consumidor para comunicar la falta de conformidad, si la norma vigente lo fija.
- El orden de prelacion entre reparacion, sustitucion, rebaja del precio y resolucion del contrato.
- El plazo de respuesta de la empresa a la hoja oficial de reclamaciones, que fija la normativa autonomica.
- El plazo de resolucion del procedimiento arbitral y el regimen de la mediacion previa.
- Los efectos del laudo y los supuestos tasados de la accion de anulacion.

---

## Normativa autonomica (verificacion obligatoria por caso)

El modelo de hoja de quejas y reclamaciones, el numero de ejemplares, el organismo competente, la forma de presentacion y el plazo de respuesta de la empresa **son autonomicos**. La skill los verifica con `web_search` para la comunidad autonoma del caso antes de redactar, y **no presume el procedimiento de una comunidad en otra**.

Elementos que hay que fijar por comunidad autonoma:

| Elemento | Como se verifica |
|---|---|
| Norma que aprueba el modelo de hoja | Boletin oficial autonomico |
| Numero de ejemplares y destino de cada uno | Norma autonomica del modelo |
| Organismo competente | Direccion general de consumo autonomica u oficina municipal |
| Registro de presentacion | Sede electronica autonomica o municipal |
| Plazo de respuesta de la empresa | Norma autonomica del modelo |

---

## Base de las plantillas

Los assets no reproducen ningun impreso oficial: vuelcan el **contenido** que el impreso exige, para que pueda transcribirse o adjuntarse.

| Asset | Base |
|---|---|
| `template-reclamacion-previa-empresa.md` | Estructura de reclamacion fehaciente: partes, contratacion, hechos numerados, fundamento, peticion, plazo y documentos |
| `template-hoja-reclamaciones.md` | Campos comunes de los modelos autonomicos de hoja de quejas y reclamaciones |
| `template-solicitud-arbitraje-consumo.md` | Contenido de la solicitud de arbitraje conforme al Reglamento del Sistema Arbitral de Consumo |
| `template-escrito-administracion-consumo.md` | Estructura de escrito administrativo: expone, solicita y documentos |
