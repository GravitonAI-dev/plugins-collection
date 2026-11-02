# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-reclamacion-cantidad`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica en cada lanzamiento para aplicar la redacción vigente al documento que redacta.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado, última modificación 28/02/2025 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Público de Justicia | BOE-A-2025-76 | publicada 03/01/2025, en vigor 03/04/2025 (verificado 31/08/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |

Artículos relevantes de la LEC para esta skill:

| Artículos | Materia | Redacción vigente verificada |
|---|---|---|
| 812 a 818 | Proceso monitorio (petición inicial, competencia, requerimiento, oposición) | Art. 818 modificado por LO 1/2025: impugnación de la oposición en 10 días y prueba en 5 días (verbal); demanda de ordinario en 1 mes desde el traslado de la oposición; rentas de arrendamiento siempre por juicio verbal (818.3) |
| 815.4 | Control de oficio de cláusulas abusivas en contratos empresario-consumidor antes del requerimiento | Redacción del RDL 6/2023 (en vigor 20/03/2024). Verificar el texto literal en el BOE antes de citarlo en un escrito |
| 249.2 | Juicio ordinario por cuantía: demandas que excedan de 15.000 euros o de interés económico imposible de calcular | Umbral de 15.000 euros introducido por RDL 6/2023 (en vigor 20/03/2024); NO modificado por LO 1/2025 |
| 250.2 | Juicio verbal por cuantía: demandas que no excedan de 15.000 euros | Misma reforma RDL 6/2023 |
| 250.1.1º | Rentas y cantidades debidas por arrendamiento: juicio verbal cualquiera que sea la cuantía | — |
| 437 y ss. | Demanda del juicio verbal; demanda sucinta y formulario normalizado si la cuantía no excede de 2.000 euros y no intervienen abogado ni procurador | Última reforma relevante: RDL 6/2023 |
| 399 y ss. | Demanda del juicio ordinario | — |
| 264 (y 403.2) | Acreditación documental del intento de MASC como requisito de procedibilidad | Introducido por LO 1/2025 |
| 23 y 31 | Postulación: abogado y procurador no preceptivos en verbales de cuantía <= 2.000 euros ni en la petición inicial de monitorio | — |

---

## Plantillas validadas — Modelos Normalizados del CGPJ

### Proceso monitorio

| Recurso | Detalle |
|---|---|
| Nombre | Modelo Normalizado de Proceso Monitorio Civil |
| Aprobado por | Comisión Permanente del Consejo General del Poder Judicial (Acuerdo de 22/12/2015) |
| Publicación | BOE-A-2016-783 |
| Landing oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/El-proceso-monitorio |
| Verificación | Landing accesible el 31/08/2026; ofrece "Guía sobre el Procedimiento Monitorio" (PDF) y "Proceso Monitorio. Modelo normalizado" (PDF y Word) |

### Juicio verbal

| Recurso | Detalle |
|---|---|
| Nombre | Juicio Verbal. Modelo normalizado de Demanda (para reclamaciones en que no es preceptiva la intervención de abogado y procurador, cuantía <= 2.000 euros) |
| Landing oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/El-juicio-verbal- |
| Verificación | Landing accesible el 31/08/2026; ofrece "Guía sobre el Juicio Verbal" (PDF), "Modelo normalizado de Demanda" (PDF y Word) y "Modelo normalizado de Contestación a la demanda" (PDF y Word), todos actualizados a 01/08/2025 (posteriores a la LO 1/2025) |
| Archivo del modelo | https://www.poderjudicial.es/stfls/CGPJ/ATENCI%C3%93N%20CIUDADANA/FICHERO/20250801%20Juicio%20Verbal.%20Modelo%20normalizado%20de%20Demanda.rtf |

Los assets `assets/peticion-monitorio.md` y `assets/demanda-juicio-verbal.md` se basan en la estructura de estos modelos normalizados. En cada lanzamiento, la skill re-verifica ambas landings; si el CGPJ publica una versión posterior a la registrada, actualiza el asset correspondiente.

No existe modelo normalizado del CGPJ para la demanda de juicio ordinario (es preceptiva la intervención de abogado y procurador); el asset `assets/demanda-juicio-ordinario.md` sigue la estructura del art. 399 LEC y las guías de estilo de redacción judicial. Tampoco existe modelo normalizado específico de oposición al monitorio; el asset `assets/oposicion-monitorio.md` sigue los arts. 815.1 y 818 LEC.

---

## Guías de estilo de redacción judicial (consulta)

| Recurso | Uso |
|---|---|
| Guía de redacción judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminología y corrección del lenguaje jurídico |

Principios aplicados en los assets: estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO; evitar latinajos innecesarios; numerar hechos y fundamentos; una idea por párrafo. Ver `references/estilo-redaccion-escritos.md`.

---

## Notas de verificación (31/08/2026)

- El texto consolidado completo de la LEC en el BOE es demasiado extenso para una lectura íntegra automatizada; la redacción literal de los arts. 249.2, 250, 437, 815.4 y 818 se contrasto además con repositorios jurídicos secundarios (Iberley). **Antes de citar literalmente un artículo en un escrito, verificar la redacción exacta en el BOE.**
- La LO 1/2025 no modifico el umbral de 15.000 euros de los arts. 249.2 y 250.2.
- La aplicación del requisito de MASC al proceso monitorio sigue siendo cuestión discutida (ver `references/masc-requisito-procedibilidad-lo1-2025.md`).
