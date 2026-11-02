# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `desahucio`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica en cada lanzamiento para aplicar la redacción vigente al documento que redacta.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LAU — Ley 29/1994 de Arrendamientos Urbanos (texto consolidado) | BOE-A-1994-26003 | consolidado a la fecha de verificación (última mod. conocida 25/05/2023, Ley 12/2023) | https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003 |
| LO 1/2025 de eficiencia del Servicio Público de Justicia | BOE-A-2025-76 | 02/01/2025 (en vigor 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| RDL 2/2026 (medidas frente a situaciones de vulnerabilidad social) | BOE-A-2026-2547 | 03/02/2026 (suspensión extraordinaria de lanzamientos vigente hasta 31/12/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2026-2547 |

Artículos relevantes de la LEC para esta skill: 250.1.1 y 250.1.2 (supuestos de desahucio), 52.1.7 (competencia), 437 (demanda y acumulación de rentas), 438 y 438.5 (tramitación del juicio verbal y requerimiento), 440.3 y 440.4 (señalamiento del lanzamiento), 447.2 (cosa juzgada de rentas acumuladas), 22.4 (enervación), 403.2, 264.4 y 399.3 (requisito y acreditación del MASC).

Artículos relevantes de la LAU: 27 (resolución por impago) y 35 (resolución en uso distinto de vivienda).

---

## Plantillas de la skill

| Asset | Supuesto |
|---|---|
| `assets/template-demanda-desahucio-falta-pago.md` | Falta de pago de rentas (con bloque condicional para acumular la reclamación de rentas, Art. 437.3 LEC) |
| `assets/template-demanda-desahucio-expiracion-plazo.md` | Expiración del plazo contractual o legal |
| `assets/template-demanda-desahucio-precario.md` | Precario (ocupación gratuita sin título) |

Las plantillas siguen la estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO. En cada lanzamiento, si cambian los trámites procesales (plazos del requerimiento, señalamiento del lanzamiento, requisito de MASC), la skill aplica la redacción vigente al documento que redacta, sin modificar los assets del plugin.

---

## Guías de estilo de redacción judicial (consulta)

| Recurso | Uso |
|---|---|
| Guía de redacción judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminología y corrección del lenguaje jurídico |

Principios aplicados en los assets: estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO; evitar latinajos innecesarios; numerar hechos y fundamentos; una idea por párrafo.

---

## Verificación de normativa autonómica o especial

Para las especialidades de vulnerabilidad, gran tenedor, zonas de mercado residencial tensionado y organismos de conciliación/intermediación previa, verificar con `web_search` la versión vigente y la normativa autonómica antes de redactar.
