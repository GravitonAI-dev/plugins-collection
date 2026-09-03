# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `derecho-civil-arrendamiento`. Registra las fuentes normativas que la
> skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 2 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| LAU — Ley 29/1994 de Arrendamientos Urbanos (texto consolidado) | BOE-A-1994-26003 | 25/05/2023 (Ley 12/2023) — verificada 31/08/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003 |
| Ley 12/2023, por el derecho a la vivienda (texto consolidado) | BOE-A-2023-12203 | consolidado a 28/02/2026 — verificada 31/08/2026 | https://www.boe.es/buscar/act.php?id=BOE-A-2023-12203 |
| Resolucion INE 18/12/2024 — define el IRAV (indice de referencia para la actualizacion anual de los arrendamientos de vivienda) | BOE-A-2024-26685 | en vigor desde 01/01/2025 — verificada 31/08/2026 | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2024-26685 |
| Codigo Civil (arrendamiento de cosas, arts. 1542 y ss. — regimen del alquiler de habitacion) | BOE-A-1889-4763 | texto consolidado vigente | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |

Articulos relevantes de la LAU para esta skill: 2-5 (ambito; 3.2 arrendamiento de temporada como uso distinto de vivienda; 5.e exclusion de vivienda turistica), 8 (cesion y subarriendo), 9-11 (duracion, prorroga — preaviso de no renovacion: 4 meses arrendador / 2 meses arrendatario, Art. 10.1 —, desistimiento), 17-20 (renta, actualizacion — notificacion por escrito con el porcentaje aplicado, exigible desde el mes siguiente, Art. 18.2 —, gastos, zonas tensionadas Arts. 17.6 y 17.7), 25 (adquisicion preferente), 27 (resolucion), 36 (fianza: 1 mensualidad vivienda / 2 uso distinto, Art. 36.1; devolucion en 1 mes desde la entrega de llaves con interes legal en caso de demora, Art. 36.4; garantias adicionales con limite de 2 mensualidades en vivienda de hasta 5/7 anos, Art. 36.5), Titulo III (uso distinto de vivienda).

---

## Datos verificados el 31/08/2026

**Indice de actualizacion de renta en vivienda (IRAV).** Desde el 01/01/2025, la actualizacion anual de la renta de los contratos de arrendamiento de vivienda celebrados a partir del 26/05/2023 tiene como limite el IRAV que publica mensualmente el INE (Resolucion de 18/12/2024, BOE-A-2024-26685, dictada por mandato de la Ley 12/2023). El IRAV se define como el minimo entre la variacion anual del IPC, la del IPC subyacente y una tasa media ajustada. Sustituye al IPC como tope del Art. 18 LAU para esos contratos; el IGC solo subsiste como indice supletorio de pacto en contratos anteriores al 26/05/2023 y en usos distintos de vivienda. Valor vigente: consultar el ultimo dato publicado por el INE (https://www.ine.es/uc/oC7D0Ncd) en la fecha de cada actualizacion.

**Zonas de mercado residencial tensionado (Ley 12/2023, Art. 18).** Las declaran las administraciones competentes en materia de vivienda (comunidades autonomas), mediante resolucion publicada en su boletin oficial. Efectos en la LAU (disposicion final primera de la Ley 12/2023): limites de renta de los nuevos contratos (Arts. 17.6 y 17.7 LAU — no superar la ultima renta del contrato anterior en 5 anos, con incremento maximo del 10% en supuestos tasados; si el arrendador es gran tenedor, tope ademas por el indice de referencia de precios) y prorroga extraordinaria de hasta 3 anos a solicitud del arrendatario (Art. 10.3 LAU). Gran tenedor (Art. 3.k Ley 12/2023): titular de mas de 10 inmuebles urbanos de uso residencial o mas de 1.500 m² construidos de ese uso (excluidos garajes y trasteros); en zonas tensionadas puede rebajarse a 5.

**Regimen del alquiler de habitacion.** El arrendamiento de una habitacion (no de la vivienda completa) queda fuera de la LAU: no satisface de modo permanente la necesidad de vivienda del arrendatario exigida por el Art. 2.1 LAU. Se rige por lo pactado y, supletoriamente, por el Codigo Civil, arts. 1542 y siguientes (arrendamiento de cosas). Es el criterio mayoritario y reiterado de las Audiencias Provinciales (entre otras, las de Madrid, Barcelona, Valladolid o Baleares); no citar sentencias concretas sin verificarlas. Consecuencias: sin plazos minimos ni prorrogas del Titulo II LAU, sin fianza legal obligatoria del Art. 36 (la fianza es de libre pacto) y sin limites de renta de zona tensionada.

**Arrendamiento de temporada.** Es arrendamiento para uso distinto de vivienda (Art. 3.2 LAU): se rige por la voluntad de las partes y el Titulo III LAU, sin plazos minimos ni prorrogas del Titulo II. Fianza legal: 2 mensualidades (Art. 36.1, uso distinto). Exige causa de temporalidad real y acreditable (verano, trabajo o estudios temporales, obra en la vivienda habitual); si el uso real es residencia permanente, el contrato se recalifica como vivienda. No confundir con la vivienda turistica (Art. 5.e LAU), excluida de la LAU y sujeta a normativa autonomica, que sigue fuera del alcance de esta skill.

---

## Verificacion de otras normas autonomicas o especiales

Para zonas de mercado residencial tensionado declaradas por comunidades autonomas (consultar el boletin oficial autonomico correspondiente), normativa turistica autonomica o especialidades forales, verificar con `web_search` la version vigente antes de redactar.
