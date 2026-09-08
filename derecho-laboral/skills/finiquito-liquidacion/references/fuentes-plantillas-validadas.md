# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `finiquito-liquidacion`.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte al usuario de que la verificación queda pendiente.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Estatuto de los Trabajadores — texto refundido aprobado por Real Decreto Legislativo 2/2015 | BOE-A-2015-11430 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 |
| Ley General de la Seguridad Social — texto refundido aprobado por Real Decreto Legislativo 8/2015 | BOE-A-2015-11724 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| Ley 36/2011, reguladora de la Jurisdicción Social | BOE-A-2011-15936 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2011-15936 |

Artículos relevantes del Estatuto de los Trabajadores: 3.5 (indisponibilidad de derechos), 26 (concepto de salario), 29 (liquidación, pago e interés por mora), 38 (vacaciones), 49 (extinción del contrato y propuesta de liquidación) y 59 (prescripción).

Norma fiscal cuya versión vigente debe verificarse con `web_search` antes de citarla: Ley 35/2006 del Impuesto sobre la Renta de las Personas Físicas, en cuanto a la exención de las indemnizaciones por despido y su límite máximo.

---

## Magnitudes que se verifican en cada lanzamiento

| Magnitud | Fuente |
|---|---|
| Límite de exención en el IRPF de la indemnización por despido y su tope máximo | Texto vigente de la Ley 35/2006 y doctrina de la Agencia Tributaria |
| Tipos de cotización a cargo de la persona trabajadora | Orden anual de cotización publicada en el BOE |
| Salario mínimo interprofesional | Real decreto anual publicado en el BOE |
| Interés legal del dinero, a efectos del interés por mora | Ley de presupuestos generales del Estado del ejercicio |

---

## Convenio colectivo: datos imprescindibles para liquidar

El convenio es la fuente que decide el resultado del cálculo. Antes de liquidar hay que extraer de él:

1. **Número de pagas extraordinarias** y, sobre todo, **el periodo de devengo de cada una**: por semestres naturales, por año natural, o de fecha a fecha. Es el dato que más veces se calcula mal.
2. **Régimen de vacaciones:** días anuales, periodo de devengo y reglas de disfrute.
3. **Plazo de preaviso** en la baja voluntaria y consecuencias de su incumplimiento.
4. **Complementos de devengo superior al mes** que deban prorratearse en la liquidación.
5. **Mejoras indemnizatorias** sobre los mínimos legales.

| Registro | URL |
|---|---|
| REGCON — Registro y depósito de convenios y acuerdos colectivos | https://expinterweb.mites.gob.es/regcon/ |
| Boletines autonómicos y provinciales | Verificar con `web_search` |

---

## Estilo de redacción

Principios aplicados en los assets: el recibo consigna importes en tabla de devengos y deducciones, con una columna dedicada al detalle del cálculo de cada concepto; la hoja de liquidación desarrolla cada fórmula y deja constancia de las comprobaciones realizadas y de su origen documental; la salvedad de firma y el derecho a la presencia de un representante legal figuran expresamente; el bloque final de advertencias distingue lo que debe saber la empresa de lo que debe saber la persona trabajadora.
