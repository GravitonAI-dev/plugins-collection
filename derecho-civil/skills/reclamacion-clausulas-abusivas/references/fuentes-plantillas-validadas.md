# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `reclamacion-clausulas-abusivas`. Registra las fuentes normativas
> y jurisprudenciales que la skill verifica y, si detecta una versión posterior, aplica la redacción vigente al documento que redacta
> en cada lanzamiento.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. En esta materia, además, la Fase 1.3 verifica la jurisprudencia reciente del tipo de cláusula: si difiere de la registrada, se aplica la doctrina vigente al documento que redacta, sin modificar el archivo de referencia del plugin. Si la fuente no es accesible, se usa la versión local, se marca `{{VERIFICAR}}` y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| TRLGDCU — Real Decreto Legislativo 1/2007 (texto refundido, consolidado) | BOE-A-2007-20555 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555 |
| LCGC — Ley 7/1998 sobre condiciones generales de la contratación (consolidado) | BOE-A-1998-8789 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-1998-8789 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (consolidado) | BOE-A-2000-323 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |

Artículos relevantes: TRLGDCU arts. 3, 4, 80, 82, 83, 85-90; LCGC arts. 1, 5, 7, 8, 9, 11, 12; LEC art. 52.3 (fuero del consumidor) y control de oficio de cláusulas abusivas.

Norma europea de referencia (no en BOE): Directiva 93/13/CEE del Consejo, de 5 de abril de 1993, sobre cláusulas abusivas en contratos con consumidores.

---

## Fuentes jurisprudenciales (verificar en cada uso)

| Fuente | Uso | URL |
|---|---|---|
| CURIA — jurisprudencia del TJUE | Verificar sentencias del TJUE sobre la Directiva 93/13/CEE por tipo de cláusula | https://curia.europa.eu |
| CENDOJ — buscador de jurisprudencia del CGPJ | Verificar sentencias del Tribunal Supremo (Sala Primera) | https://www.poderjudicial.es/search/indexAN.jsp |

La jurisprudencia de esta materia es cambiante. Se verifica con web_search en la Fase 2.1 y solo se cita lo confirmado. Ver `jurisprudencia-tjue-ts-clausulas.md`.

---

## Guías de estilo de redacción (consulta)

| Recurso | Uso |
|---|---|
| Guía de redacción judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminología y corrección del lenguaje jurídico |

Principios aplicados en los assets: estructura clara con HECHOS y FUNDAMENTOS DE DERECHO numerados; para la demanda, AL JUZGADO / HECHOS / FUNDAMENTOS / SUPLICO; para la reclamación previa, exposición ordenada y petición concreta. Ver `estilo-redaccion-escritos.md`.

---

## Verificación de normativa autonómica o especial

Para la vía administrativa de consumo (hojas de reclamaciones, arbitraje de consumo) y para especialidades autonómicas, verificar con `web_search` la normativa vigente de la comunidad autónoma del consumidor antes de orientar sobre esa vía. Para la tarjeta revolving, verificar además el encuadre de usura (Ley de 23 de julio de 1908, de Represión de la Usura).
