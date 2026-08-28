# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `desahucio`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LAU — Ley 29/1994 de Arrendamientos Urbanos (texto consolidado) | BOE-A-1994-26003 | consolidado a la fecha de verificacion (ultima mod. conocida 25/05/2023, Ley 12/2023) | https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003 |
| LO 1/2025 de eficiencia del Servicio Publico de Justicia | BOE-A-2025-76 | 02/01/2025 (en vigor 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |
| RDL 2/2026 (medidas frente a situaciones de vulnerabilidad social) | BOE-A-2026-2547 | 03/02/2026 (suspension extraordinaria de lanzamientos vigente hasta 31/12/2026) | https://www.boe.es/buscar/act.php?id=BOE-A-2026-2547 |

Articulos relevantes de la LEC para esta skill: 250.1.1 y 250.1.2 (supuestos de desahucio), 52.1.7 (competencia), 437 (demanda y acumulacion de rentas), 438 y 438.5 (tramitacion del juicio verbal y requerimiento), 440.3 y 440.4 (señalamiento del lanzamiento), 447.2 (cosa juzgada de rentas acumuladas), 22.4 (enervacion), 403.2, 264.4 y 399.3 (requisito y acreditacion del MASC).

Articulos relevantes de la LAU: 27 (resolucion por impago) y 35 (resolucion en uso distinto de vivienda).

---

## Plantillas de la skill

| Asset | Supuesto |
|---|---|
| `assets/template-demanda-desahucio-falta-pago.md` | Falta de pago de rentas (con bloque condicional para acumular la reclamacion de rentas, Art. 437.3 LEC) |
| `assets/template-demanda-desahucio-expiracion-plazo.md` | Expiracion del plazo contractual o legal |
| `assets/template-demanda-desahucio-precario.md` | Precario (ocupacion gratuita sin titulo) |

Las plantillas siguen la estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO. En cada lanzamiento, si cambian los tramites procesales (plazos del requerimiento, señalamiento del lanzamiento, requisito de MASC), la skill actualiza los assets.

---

## Guias de estilo de redaccion judicial (consulta)

| Recurso | Uso |
|---|---|
| Guia de redaccion judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |

Principios aplicados en los assets: estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO; evitar latinajos innecesarios; numerar hechos y fundamentos; una idea por parrafo.

---

## Verificacion de normativa autonomica o especial

Para las especialidades de vulnerabilidad, gran tenedor, zonas de mercado residencial tensionado y organismos de conciliacion/intermediacion previa, verificar con `web_search` la version vigente y la normativa autonomica antes de redactar.
