# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `juicio-ordinario`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica en cada lanzamiento para aplicar la redacción vigente al documento que redacta.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| RDL 6/2023 (que elevo a 15.000 euros el umbral del juicio verbal / ordinario) | BOE-A-2023-25652 | 20/12/2023 (en vigor 20/03/2024) | https://www.boe.es/buscar/act.php?id=BOE-A-2023-25652 |
| LO 1/2025 de eficiencia del Servicio Público de Justicia | BOE-A-2025-76 | 02/01/2025 (en vigor 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |

Artículos relevantes de la LEC para esta skill:
- Ámbito y cuantía: 248, 249.1 (por razón de la materia), 249.2 (por cuantía superior a 15.000 euros), 250 (juicio verbal, por contraste), 251-255 (determinación de la cuantía).
- Admisibilidad y postulación: 23 y 31 (abogado y procurador), 45, 50-52 (competencia objetiva y territorial).
- Procedibilidad (MASC): 264.4, 399.3 y 403.2, introducidos/modificados por la LO 1/2025.
- Demanda y documentos: 399 (contenido de la demanda), 264-266 (documentos procesales y de fondo), 269-270 (preclusion y presentación posterior), 336 (dictámenes periciales con la demanda).
- Audiencia previa: 414-430.
- Prueba: 217 (carga de la prueba), 281-386 (medios de prueba), 429 (proposición y admisión de prueba).
- Conclusiones: 433.

---

## Umbral de cuantía (verificación crítica)

| Cuantía de la pretensión | Juicio |
|---|---|
| Hasta 15.000 euros (y no incluida en el Art. 250.1 por la materia) | Juicio verbal |
| Superior a 15.000 euros, o interés económico incalculable | Juicio ordinario (Art. 249.2) |
| Materias del Art. 249.1 | Juicio ordinario con independencia de la cuantía |

El umbral se elevo de 6.000 a 15.000 euros por el RDL 6/2023, con efecto desde el 20/03/2024. La skill re-verifica este importe en cada lanzamiento; si el BOE registra otro, aplica el vigente al documento que redacta e informa del cambio en el chat, sin modificar esta tabla ni `references/lec-ambito-y-cuantia.md`.

---

## Plantillas de la skill

| Asset | Fase |
|---|---|
| `assets/template-checklist-admisibilidad.md` | Etapa procesal 1 — admisibilidad, competencia, postulación, cuantía y MASC |
| `assets/template-demanda-juicio-ordinario.md` | Etapa procesal 2 — demanda (Art. 399 LEC) |
| `assets/template-guion-audiencia-previa.md` | Etapa procesal 3 — audiencia previa (Arts. 414-430) |
| `assets/template-proposicion-de-prueba.md` | Etapa procesal 4 — proposición de prueba (Art. 429 y 281-386) |
| `assets/template-escrito-de-conclusiones.md` | Etapa procesal 5 — conclusiones (Art. 433) |

Las plantillas siguen la estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO cuando procede. En cada lanzamiento, si cambian los trámites procesales o los umbrales, la skill aplica la redacción vigente al documento que redacta, sin modificar los assets del plugin.

---

## Guías de estilo de redacción judicial (consulta)

| Recurso | Uso |
|---|---|
| Guía de redacción judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminología y corrección del lenguaje jurídico |

Principios aplicados en los assets: estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO; evitar latinajos innecesarios; numerar hechos y fundamentos; una idea por párrafo.

---

## Verificación de normativa autonómica o especial

Para especialidades por razón de la materia (consumidores, propiedad horizontal, competencia desleal, propiedad intelectual e industrial, condiciones generales de la contratación) y para el detalle de la acreditación del MASC, verificar con `web_search` la versión vigente antes de redactar.
