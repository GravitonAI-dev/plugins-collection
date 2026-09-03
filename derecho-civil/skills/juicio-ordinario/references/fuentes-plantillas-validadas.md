# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `juicio-ordinario`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| RDL 6/2023 (que elevo a 15.000 euros el umbral del juicio verbal / ordinario) | BOE-A-2023-25652 | 20/12/2023 (en vigor 20/03/2024) | https://www.boe.es/buscar/act.php?id=BOE-A-2023-25652 |
| LO 1/2025 de eficiencia del Servicio Publico de Justicia | BOE-A-2025-76 | 02/01/2025 (en vigor 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |

<!-- EDITAR PARA TU EQUIPO: el umbral de cuantia entre juicio verbal y ordinario (15.000 euros desde el 20/03/2024) puede variar; confirmar en el BOE el importe vigente en la fecha del caso -->

Articulos relevantes de la LEC para esta skill:
- Ambito y cuantia: 248, 249.1 (por razon de la materia), 249.2 (por cuantia superior a 15.000 euros), 250 (juicio verbal, por contraste), 251-255 (determinacion de la cuantia).
- Admisibilidad y postulacion: 23 y 31 (abogado y procurador), 45, 50-52 (competencia objetiva y territorial).
- Procedibilidad (MASC): 264.4, 399.3 y 403.2, introducidos/modificados por la LO 1/2025.
- Demanda y documentos: 399 (contenido de la demanda), 264-266 (documentos procesales y de fondo), 269-270 (preclusion y presentacion posterior), 336 (dictamenes periciales con la demanda).
- Audiencia previa: 414-430.
- Prueba: 217 (carga de la prueba), 281-386 (medios de prueba), 429 (proposicion y admision de prueba).
- Conclusiones: 433.

---

## Umbral de cuantia (verificacion critica)

| Cuantia de la pretension | Juicio |
|---|---|
| Hasta 15.000 euros (y no incluida en el Art. 250.1 por la materia) | Juicio verbal |
| Superior a 15.000 euros, o interes economico incalculable | Juicio ordinario (Art. 249.2) |
| Materias del Art. 249.1 | Juicio ordinario con independencia de la cuantia |

El umbral se elevo de 6.000 a 15.000 euros por el RDL 6/2023, con efecto desde el 20/03/2024. La skill re-verifica este importe en cada lanzamiento; si el BOE registra otro, actualiza esta tabla y `references/lec-ambito-y-cuantia.md`.

---

## Plantillas de la skill

| Asset | Fase |
|---|---|
| `assets/checklist-admisibilidad.md` | Fase 2 — admisibilidad, competencia, postulacion, cuantia y MASC |
| `assets/demanda-juicio-ordinario.md` | Fase 3 — demanda (Art. 399 LEC) |
| `assets/guion-audiencia-previa.md` | Fase 4 — audiencia previa (Arts. 414-430) |
| `assets/proposicion-de-prueba.md` | Fase 5 — proposicion de prueba (Art. 429 y 281-386) |
| `assets/escrito-de-conclusiones.md` | Fase 6 — conclusiones (Art. 433) |

Las plantillas siguen la estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO cuando procede. En cada lanzamiento, si cambian los tramites procesales o los umbrales, la skill actualiza los assets.

---

## Guias de estilo de redaccion judicial (consulta)

| Recurso | Uso |
|---|---|
| Guia de redaccion judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |

Principios aplicados en los assets: estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO; evitar latinajos innecesarios; numerar hechos y fundamentos; una idea por parrafo.

---

## Verificacion de normativa autonomica o especial

Para especialidades por razon de la materia (consumidores, propiedad horizontal, competencia desleal, propiedad intelectual e industrial, condiciones generales de la contratacion) y para el detalle de la acreditacion del MASC, verificar con `web_search` la version vigente antes de redactar.
