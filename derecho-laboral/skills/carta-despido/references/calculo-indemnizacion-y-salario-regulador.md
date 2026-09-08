# Cálculo de Indemnizaciones y Salario Regulador

> Referencia de cálculo para la skill `carta-despido`. Todo importe se muestra desglosado en el chat
> antes de escribirlo en el documento.

---

## 1. El salario regulador: la base de todo

El módulo de cálculo es el **salario diario regulador**, no el salario base ni el neto en nómina. Se obtiene del salario bruto anual efectivamente devengado, incluidos:

- Salario base.
- Complementos salariales de devengo periódico (antigüedad, puesto, nocturnidad, turnicidad, responsabilidad).
- **Prorrateo de las pagas extraordinarias**, aunque se abonen en sus fechas.
- Complementos de devengo superior al mes, prorrateados (bonus, participación en beneficios), cuando sean salariales y consolidados.
- Retribución en especie valorada (vehículo, vivienda, seguro médico) cuando constituya salario.

Se excluyen: las percepciones extrasalariales (dietas, plus de transporte, quebranto de moneda, indemnizaciones por gastos), las horas extraordinarias no habituales y las mejoras voluntarias no consolidadas.

**Fórmula:** `salario diario regulador = salario bruto anual con prorrateos / 365`

Cuando el salario sea variable o irregular, se toma el promedio del último año efectivamente trabajado. En jornada a tiempo parcial se computa el salario realmente percibido, sin elevarlo a jornada completa. Si en el último año hubo reducción de jornada por guarda legal o cuidado, el salario regulador se calcula sobre el que correspondería **sin** la reducción.

---

## 2. Módulos indemnizatorios

| Supuesto | Módulo | Tope | Precepto |
|---|---|---|---|
| Despido objetivo (artículos 52 y 53) | 20 días de salario por año de servicio | 12 mensualidades | Artículo 53.1.b) |
| Despido improcedente | 33 días de salario por año de servicio | 24 mensualidades | Artículo 56.1 |
| Finalización de contrato temporal | 12 días de salario por año de servicio | Sin tope específico | Artículo 49.1.c) |
| Extinción por voluntad del trabajador con causa (artículo 50) | La del despido improcedente | 24 mensualidades | Artículo 50.2 |
| Extinción por modificación sustancial o movilidad geográfica | 20 días por año | 9 mensualidades (artículo 41) / 12 mensualidades (artículo 40) | Artículos 40.1 y 41.3 |
| Despido disciplinario procedente | No procede indemnización | — | Artículo 55.7 |
| No superación del periodo de prueba | No procede indemnización | — | Artículo 14.2 |
| Contratos formativos y contrato de sustitución, a su término | No procede la indemnización de 12 días | — | Artículo 49.1.c) |

---

## 3. Cómputo de la antigüedad

- Se computa desde la **fecha de antigüedad reconocida**, que puede ser anterior a la del contrato vigente si hubo contratos previos encadenados sin interrupción significativa, subrogación o sucesión de empresa.
- Los periodos inferiores al año se **prorratean por meses**; la fracción de mes se computa como mes completo.
- Los periodos de suspensión del contrato (incapacidad temporal, excedencia forzosa, nacimiento y cuidado) computan como tiempo de servicio. La excedencia voluntaria no computa.
- El tiempo de puesta a disposición por empresa de trabajo temporal en el mismo puesto computa a efectos de antigüedad si media contratación posterior directa.

**Fórmula:** `indemnización = salario diario regulador × módulo de días × (años completos + meses / 12)`

---

## 4. Régimen transitorio de los contratos anteriores al 12 de febrero de 2012

Para la indemnización por despido improcedente de contratos formalizados **antes del 12 de febrero de 2012**, la disposición transitoria undécima del Estatuto de los Trabajadores establece un cálculo en dos tramos:

- Tramo hasta el 11 de febrero de 2012 inclusive: 45 días de salario por año de servicio.
- Tramo desde el 12 de febrero de 2012: 33 días de salario por año de servicio.

El importe resultante tiene topes propios que deben comprobarse en el texto vigente de la disposición transitoria antes de aplicarla. **No aplicar este régimen sin verificar la redacción consolidada vigente en el BOE:** su literalidad es compleja y su aplicación errónea es una fuente habitual de reclamación de diferencias.

---

## 5. Salarios de tramitación

Proceden cuando el despido se declara **nulo**, y cuando se declara **improcedente y el empresario opta por la readmisión** (o cuando la opción corresponde al trabajador y este opta por readmisión). Se calculan desde la fecha del despido hasta la notificación de la sentencia o hasta que el trabajador haya encontrado otro empleo, deduciéndose en ese caso lo percibido.

---

## 6. Advertencias de cálculo obligatorias en el chat

1. El importe calculado es una estimación basada en los datos aportados: el importe definitivo depende del salario regulador realmente acreditado en nómina y del convenio aplicable.
2. El convenio colectivo puede mejorar los módulos legales: comprobarlo siempre antes de cerrar el importe.
3. La indemnización por despido está exenta de tributación en el IRPF hasta el límite legalmente establecido para la cuantía obligatoria; el exceso pactado tributa. Verificar el límite vigente antes de informar de ello.
4. Mostrar siempre la fórmula completa con sus factores, nunca solo el resultado.
