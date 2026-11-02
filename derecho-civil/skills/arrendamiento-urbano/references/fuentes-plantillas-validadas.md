# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-arrendamiento`. Registra las fuentes normativas que la
> skill verifica y, si detecta una versión posterior, aplica la redacción vigente al documento que redacta en cada lanzamiento.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al documento que redacta en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| LAU — Ley 29/1994 de Arrendamientos Urbanos (texto consolidado) | BOE-A-1994-26003 | 25/05/2023 (Ley 12/2023) — verificada 31/08/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003 |
| Ley 12/2023, por el derecho a la vivienda (texto consolidado) | BOE-A-2023-12203 | consolidado a 28/02/2026 — verificada 31/08/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2023-12203 |
| Resolución INE 18/12/2024 — define el IRAV (índice de referencia para la actualización anual de los arrendamientos de vivienda) | BOE-A-2024-26685 | en vigor desde 01/01/2025 — verificada 31/08/2026 | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2024-26685 |
| Código Civil (arrendamiento de cosas, arts. 1542 y ss. — régimen del alquiler de habitación) | BOE-A-1889-4763 | texto consolidado vigente | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |

Artículos relevantes de la LAU para esta skill: 2-5 (ámbito; 3.2 arrendamiento de temporada como uso distinto de vivienda; 5.e exclusión de vivienda turística), 8 (cesión y subarriendo), 9-11 (duración, prórroga — preaviso de no renovación: 4 meses arrendador / 2 meses arrendatario, Art. 10.1 —, desistimiento), 17-20 (renta, actualización — notificación por escrito con el porcentaje aplicado, exigible desde el mes siguiente, Art. 18.2 —, gastos, zonas tensionadas Arts. 17.6 y 17.7), 25 (adquisición preferente), 27 (resolución), 36 (fianza: 1 mensualidad vivienda / 2 uso distinto, Art. 36.1; devolución en 1 mes desde la entrega de llaves con interés legal en caso de demora, Art. 36.4; garantías adicionales con límite de 2 mensualidades en vivienda de hasta 5/7 años, Art. 36.5), Título III (uso distinto de vivienda).

---

## Datos verificados el 31/08/2026

**Índice de actualización de renta en vivienda (IRAV).** Desde el 01/01/2025, la actualización anual de la renta de los contratos de arrendamiento de vivienda celebrados a partir del 26/05/2023 tiene como límite el IRAV que publica mensualmente el INE (Resolución de 18/12/2024, BOE-A-2024-26685, dictada por mandato de la Ley 12/2023). El IRAV se define como el mínimo entre la variación anual del IPC, la del IPC subyacente y una tasa media ajustada. Sustituye al IPC como tope del Art. 18 LAU para esos contratos; el IGC solo subsiste como índice supletorio de pacto en contratos anteriores al 26/05/2023 y en usos distintos de vivienda. Valor vigente: consultar el último dato publicado por el INE (https://www.ine.es/uc/oC7D0Ncd) en la fecha de cada actualización.

**Zonas de mercado residencial tensionado (Ley 12/2023, Art. 18).** Las declaran las administraciones competentes en materia de vivienda (comunidades autónomas), mediante resolución publicada en su boletín oficial. Efectos en la LAU (disposición final primera de la Ley 12/2023): límites de renta de los nuevos contratos (Arts. 17.6 y 17.7 LAU — no superar la última renta del contrato anterior en 5 años, con incremento máximo del 10% en supuestos tasados; si el arrendador es gran tenedor, tope además por el índice de referencia de precios) y prórroga extraordinaria de hasta 3 años a solicitud del arrendatario (Art. 10.3 LAU). Gran tenedor (Art. 3.k Ley 12/2023): titular de más de 10 inmuebles urbanos de uso residencial o más de 1.500 m² construidos de ese uso (excluidos garajes y trasteros); en zonas tensionadas puede rebajarse a 5.

**Régimen del alquiler de habitación.** El arrendamiento de una habitación (no de la vivienda completa) queda fuera de la LAU: no satisface de modo permanente la necesidad de vivienda del arrendatario exigida por el Art. 2.1 LAU. Se rige por lo pactado y, supletoriamente, por el Código Civil, arts. 1542 y siguientes (arrendamiento de cosas). Es el criterio mayoritario y reiterado de las Audiencias Provinciales (entre otras, las de Madrid, Barcelona, Valladolid o Baleares); no citar sentencias concretas sin verificarlas. Consecuencias: sin plazos mínimos ni prórrogas del Título II LAU, sin fianza legal obligatoria del Art. 36 (la fianza es de libre pacto) y sin límites de renta de zona tensionada.

**Arrendamiento de temporada.** Es arrendamiento para uso distinto de vivienda (Art. 3.2 LAU): se rige por la voluntad de las partes y el Título III LAU, sin plazos mínimos ni prórrogas del Título II. Fianza legal: 2 mensualidades (Art. 36.1, uso distinto). Exige causa de temporalidad real y acreditable (verano, trabajo o estudios temporales, obra en la vivienda habitual); si el uso real es residencia permanente, el contrato se recalifica como vivienda. No confundir con la vivienda turística (Art. 5.e LAU), excluida de la LAU y sujeta a normativa autonómica, que sigue fuera del alcance de esta skill.

---

## Verificación de otras normas autonómicas o especiales

Para zonas de mercado residencial tensionado declaradas por comunidades autónomas (consultar el boletín oficial autonómico correspondiente), normativa turística autonómica o especialidades forales, verificar con `web_search` la versión vigente antes de redactar.
