# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-reclamacion-cantidad`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso de verificacion se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado, ultima modificacion 28/02/2025 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Publico de Justicia | BOE-A-2025-76 | publicada 03/01/2025, en vigor 03/04/2025 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |

Articulos relevantes de la LEC para esta skill:

| Articulos | Materia | Redaccion vigente verificada |
|---|---|---|
| 812 a 818 | Proceso monitorio (peticion inicial, competencia, requerimiento, oposicion) | Art. 818 modificado por LO 1/2025: impugnacion de la oposicion en 10 dias y prueba en 5 dias (verbal); demanda de ordinario en 1 mes desde el traslado de la oposicion; rentas de arrendamiento siempre por juicio verbal (818.3) |
| 815.4 | Control de oficio de clausulas abusivas en contratos empresario-consumidor antes del requerimiento | Redaccion del RDL 6/2023 (en vigor 20/03/2024). Verificar el texto literal en el BOE antes de citarlo en un escrito |
| 249.2 | Juicio ordinario por cuantia: demandas que excedan de 15.000 euros o de interes economico imposible de calcular | Umbral de 15.000 euros introducido por RDL 6/2023 (en vigor 20/03/2024); NO modificado por LO 1/2025 |
| 250.2 | Juicio verbal por cuantia: demandas que no excedan de 15.000 euros | Misma reforma RDL 6/2023 |
| 250.1.1º | Rentas y cantidades debidas por arrendamiento: juicio verbal cualquiera que sea la cuantia | — |
| 437 y ss. | Demanda del juicio verbal; demanda sucinta y formulario normalizado si la cuantia no excede de 2.000 euros y no intervienen abogado ni procurador | Ultima reforma relevante: RDL 6/2023 |
| 399 y ss. | Demanda del juicio ordinario | — |
| 264 (y 403.2) | Acreditacion documental del intento de MASC como requisito de procedibilidad | Introducido por LO 1/2025 |
| 23 y 31 | Postulacion: abogado y procurador no preceptivos en verbales de cuantia <= 2.000 euros ni en la peticion inicial de monitorio | — |

---

## Plantillas validadas — Modelos Normalizados del CGPJ

### Proceso monitorio

| Recurso | Detalle |
|---|---|
| Nombre | Modelo Normalizado de Proceso Monitorio Civil |
| Aprobado por | Comision Permanente del Consejo General del Poder Judicial (Acuerdo de 22/12/2015) |
| Publicacion | BOE-A-2016-783 |
| Landing oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/El-proceso-monitorio |
| Verificacion | Landing accesible el 31/08/2026; ofrece "Guia sobre el Procedimiento Monitorio" (PDF) y "Proceso Monitorio. Modelo normalizado" (PDF y Word) |

### Juicio verbal

| Recurso | Detalle |
|---|---|
| Nombre | Juicio Verbal. Modelo normalizado de Demanda (para reclamaciones en que no es preceptiva la intervencion de abogado y procurador, cuantia <= 2.000 euros) |
| Landing oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/El-juicio-verbal- |
| Verificacion | Landing accesible el 31/08/2026; ofrece "Guia sobre el Juicio Verbal" (PDF), "Modelo normalizado de Demanda" (PDF y Word) y "Modelo normalizado de Contestacion a la demanda" (PDF y Word), todos actualizados a 01/08/2025 (posteriores a la LO 1/2025) |
| Archivo del modelo | https://www.poderjudicial.es/stfls/CGPJ/ATENCI%C3%93N%20CIUDADANA/FICHERO/20250801%20Juicio%20Verbal.%20Modelo%20normalizado%20de%20Demanda.rtf |

Los assets `assets/peticion-monitorio.md` y `assets/demanda-juicio-verbal.md` se basan en la estructura de estos modelos normalizados. En cada lanzamiento, la skill re-verifica ambas landings; si el CGPJ publica una version posterior a la registrada, actualiza el asset correspondiente.

No existe modelo normalizado del CGPJ para la demanda de juicio ordinario (es preceptiva la intervencion de abogado y procurador); el asset `assets/demanda-juicio-ordinario.md` sigue la estructura del art. 399 LEC y las guias de estilo de redaccion judicial. Tampoco existe modelo normalizado especifico de oposicion al monitorio; el asset `assets/oposicion-monitorio.md` sigue los arts. 815.1 y 818 LEC.

---

## Guias de estilo de redaccion judicial (consulta)

| Recurso | Uso |
|---|---|
| Guia de redaccion judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |

Principios aplicados en los assets: estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO; evitar latinajos innecesarios; numerar hechos y fundamentos; una idea por parrafo. Ver `references/estilo-redaccion-escritos.md`.

---

## Notas de verificacion (31/08/2026)

- El texto consolidado completo de la LEC en el BOE es demasiado extenso para una lectura integra automatizada; la redaccion literal de los arts. 249.2, 250, 437, 815.4 y 818 se contrasto ademas con repositorios juridicos secundarios (Iberley). **Antes de citar literalmente un articulo en un escrito, verificar la redaccion exacta en el BOE.**
- La LO 1/2025 no modifico el umbral de 15.000 euros de los arts. 249.2 y 250.2.
- La aplicacion del requisito de MASC al proceso monitorio sigue siendo cuestion discutida (ver `references/masc-requisito-procedibilidad-lo1-2025.md`).
