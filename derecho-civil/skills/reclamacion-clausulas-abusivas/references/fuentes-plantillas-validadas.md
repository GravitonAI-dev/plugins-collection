# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `reclamacion-clausulas-abusivas`. Registra las fuentes normativas
> y jurisprudenciales que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin
> en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. En esta materia, ademas, el Paso 1.3 verifica la jurisprudencia reciente del tipo de clausula: si difiere de la registrada, se actualiza `jurisprudencia-tjue-ts-clausulas.md`. Si la fuente no es accesible, se usa la version local, se marca `{{VERIFICAR}}` y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| TRLGDCU — Real Decreto Legislativo 1/2007 (texto refundido, consolidado) | BOE-A-2007-20555 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555 |
| LCGC — Ley 7/1998 sobre condiciones generales de la contratacion (consolidado) | BOE-A-1998-8789 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-1998-8789 |
| LEC — Ley 1/2000 de Enjuiciamiento Civil (consolidado) | BOE-A-2000-323 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |

Articulos relevantes: TRLGDCU arts. 3, 4, 80, 82, 83, 85-90; LCGC arts. 1, 5, 7, 8, 9, 11, 12; LEC art. 52.3 (fuero del consumidor) y control de oficio de clausulas abusivas.

Norma europea de referencia (no en BOE): Directiva 93/13/CEE del Consejo, de 5 de abril de 1993, sobre clausulas abusivas en contratos con consumidores.

---

## Fuentes jurisprudenciales (verificar en cada uso)

| Fuente | Uso | URL |
|---|---|---|
| CURIA — jurisprudencia del TJUE | Verificar sentencias del TJUE sobre la Directiva 93/13/CEE por tipo de clausula | https://curia.europa.eu |
| CENDOJ — buscador de jurisprudencia del CGPJ | Verificar sentencias del Tribunal Supremo (Sala Primera) | https://www.poderjudicial.es/search/indexAN.jsp |

La jurisprudencia de esta materia es cambiante. Se verifica con web_search en el Paso 1.3 y solo se cita lo confirmado. Ver `jurisprudencia-tjue-ts-clausulas.md`.

---

## Guias de estilo de redaccion (consulta)

| Recurso | Uso |
|---|---|
| Guia de redaccion judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |

Principios aplicados en los assets: estructura clara con HECHOS y FUNDAMENTOS DE DERECHO numerados; para la demanda, AL JUZGADO / HECHOS / FUNDAMENTOS / SUPLICO; para la reclamacion previa, exposicion ordenada y peticion concreta. Ver `estilo-redaccion-escritos.md`.

---

## Verificacion de normativa autonomica o especial

Para la via administrativa de consumo (hojas de reclamaciones, arbitraje de consumo) y para especialidades autonomicas, verificar con `web_search` la normativa vigente de la comunidad autonoma del consumidor antes de orientar sobre esa via. Para la tarjeta revolving, verificar ademas el encuadre de usura (Ley de 23 de julio de 1908, de Represion de la Usura).
