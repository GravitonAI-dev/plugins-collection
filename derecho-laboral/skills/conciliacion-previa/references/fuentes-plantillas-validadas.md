# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `conciliacion-previa`.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte al usuario de que la verificación queda pendiente.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Ley 36/2011, reguladora de la Jurisdicción Social | BOE-A-2011-15936 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2011-15936 |
| Estatuto de los Trabajadores — texto refundido aprobado por Real Decreto Legislativo 2/2015 | BOE-A-2015-11430 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 |

Artículos relevantes de la Ley 36/2011: 63 (evitación del proceso), 64 (**excepciones al intento de conciliación**), 65 (efectos sobre los plazos), 66 (asistencia obligatoria al acto), 67 (impugnación del acuerdo) y 68 (fuerza ejecutiva de lo acordado). Del Estatuto de los Trabajadores: 29.3 (interés por mora) y 59 (prescripción y caducidad).

**El artículo 64 se verifica siempre en su redacción vigente** con `web_search` antes de afirmar que un asunto está o no exceptuado del trámite: su lista ha sido modificada en sucesivas reformas, y el error consume el plazo de caducidad del cliente.

---

## Organismos y sedes de presentación

El nombre exacto del organismo, su sede electrónica y su modelo de papeleta **se verifican con `web_search` en cada asunto** a partir de la comunidad autónoma del centro de trabajo. Ver `organismos-de-conciliacion.md`.

---

## Calendario laboral

Los días hábiles se computan excluyendo sábados, domingos y festivos **nacionales, autonómicos y locales**. El calendario laboral del año en curso se publica en el BOE y en los boletines autonómicos, y los festivos locales en los boletines provinciales. **Verificarlo con `web_search` antes de dar por vivo o vencido un plazo.**

---

## Estilo de redacción

Principios aplicados en los assets: encabezamiento con el organismo destinatario y, en la cabecera del documento, el plazo aplicable y la fecha límite calculada, de modo que el profesional que revisa lo vea antes que nada; datos de las partes en tabla, con domicilio social y de centro de trabajo separados para asegurar la citación; hechos en relato cronológico; pretensión formulada con los efectos legales concretos que se piden; desglose de cantidades en tabla con el detalle del cálculo de cada concepto; bloque final de advertencias con el régimen de plazos, la asistencia obligatoria y la congruencia con la demanda posterior.
