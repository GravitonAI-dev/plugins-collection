# Conceptos de la Liquidación y su Cálculo

> Referencia de cálculo para la skill `finiquito-liquidacion`. Todo importe se muestra con su fórmula
> antes de escribirse en el documento.

---

## 1. Los conceptos que siempre deben revisarse

| Concepto | ¿Procede siempre? | Fuente del dato |
|---|---|---|
| Salario del mes en curso hasta la fecha de extinción | Sí | Nómina y días trabajados |
| Parte proporcional de pagas extraordinarias | Sí, **salvo que estén prorrateadas** | Convenio y nómina |
| Vacaciones devengadas y no disfrutadas | Sí | Convenio y calendario de disfrute |
| Horas extraordinarias pendientes | Si las hay | Registro de jornada |
| Comisiones e incentivos devengados | Si los hay | Contrato y liquidaciones previas |
| Dietas y gastos pendientes de reembolso | Si los hay | Justificantes |
| Indemnización por la extinción | Según la causa | Módulo legal o convencional |
| Anticipos y préstamos | Como deducción | Documento de concesión |
| Preaviso incumplido | Como deducción | Convenio |

## 2. Salario del mes de la extinción

**Criterio del mes de treinta días** (el más habitual en convenios con salario mensual):

`importe = salario mensual bruto / 30 × días trabajados del mes`

**Criterio de días naturales del mes:**

`importe = salario mensual bruto / días naturales del mes × días trabajados`

El criterio aplicable lo determina el convenio o la práctica consolidada de la empresa reflejada en nóminas anteriores. Comprobarlo antes de calcular, y aplicar el mismo criterio a todos los conceptos.

## 3. Pagas extraordinarias

`importe proporcional = importe íntegro de la paga / días del periodo de devengo × días devengados`

El **periodo de devengo** es la variable crítica:

| Modelo de devengo | Ejemplo de cómputo |
|---|---|
| Semestres naturales | Paga de verano: del 1 de enero al 30 de junio. Paga de Navidad: del 1 de julio al 31 de diciembre |
| Año natural | Ambas pagas se devengan del 1 de enero al 31 de diciembre |
| De fecha a fecha | Cada paga se devenga en los doce meses anteriores a su fecha de abono |

Un mismo trabajador con la misma antigüedad y salario puede tener liquidaciones muy distintas según el modelo. **Nunca se presume: se lee en el convenio.**

**Pagas prorrateadas:** si el convenio lo permite y la nómina lo refleja, las pagas se abonan mes a mes y **no procede liquidación adicional**. Comprobarlo en la nómina y hacerlo constar expresamente en el documento para evitar la duplicidad o la reclamación posterior.

## 4. Vacaciones devengadas y no disfrutadas

`días devengados = días de vacaciones anuales / 365 × días trabajados en el periodo de devengo`

`días pendientes = días devengados − días ya disfrutados`

`importe = salario diario × días pendientes`

**Efectos en Seguridad Social:** las vacaciones devengadas y no disfrutadas que se abonan en la liquidación **se cotizan**, prolongando la situación de alta durante los días correspondientes. La fecha de baja en el sistema debe ajustarse en consecuencia. Es un error frecuente cursar la baja en la fecha de cese y liquidar vacaciones sin cotizarlas.

**Vacaciones disfrutadas de más:** si la persona trabajadora ha disfrutado más días de los devengados, cabe la deducción, siempre que se justifique con el calendario y se explique.

## 5. Horas extraordinarias y complementos variables

- Las horas extraordinarias pendientes se abonan con el valor pactado, que no puede ser inferior al de la hora ordinaria, o se compensan por descanso dentro de los cuatro meses siguientes a su realización.
- El **registro de jornada** es la fuente de prueba: sin registro, la posición de la empresa frente a una reclamación de horas extraordinarias es muy débil.
- Comisiones e incentivos: se liquidan los **devengados**, aunque su liquidación ordinaria fuera posterior. El criterio de devengo debe estar en el contrato o en el plan de incentivos.

## 6. Interés por mora (artículo 29.3)

El interés por mora en el pago del salario es el **diez por ciento** de lo adeudado, computado anualmente. Se aplica a las cantidades salariales impagadas, no a las indemnizatorias. Advertirlo cuando la liquidación se retrase.

## 7. Prescripción (artículo 59)

Las acciones derivadas del contrato de trabajo que no tengan señalado plazo especial prescriben **al año** de su terminación. Para el ejercicio de acciones dirigidas a exigir percepciones económicas, el plazo de un año se computa desde el día en que la acción pudiera ejercitarse.

## 8. Tratamiento fiscal y de cotización

| Concepto | Cotiza | Tributa |
|---|---|---|
| Salario, pagas extraordinarias, vacaciones no disfrutadas, horas extraordinarias, comisiones | Sí | Sí, como rendimiento del trabajo |
| Indemnización legal por despido | No, hasta la cuantía obligatoria | Exenta hasta el límite legal, con tope máximo |
| Exceso indemnizatorio pactado sobre el mínimo legal | Sí | Sí, con posible reducción por irregularidad |
| Cantidad pactada en extinción por mutuo acuerdo | Sí | Sí, íntegramente |
| Dietas y gastos con justificación | No, dentro de los límites reglamentarios | Exentos dentro de los límites |

**Verificar siempre con `web_search` los límites vigentes de exención antes de aplicarlos.** No consignar cifras de memoria.

## 9. Errores de cálculo más frecuentes

1. Liquidar pagas extraordinarias que ya estaban prorrateadas en la nómina.
2. Aplicar un periodo de devengo de pagas distinto del que fija el convenio.
3. Olvidar cotizar las vacaciones no disfrutadas y cursar mal la fecha de baja.
4. Calcular la indemnización sobre el salario base en lugar de sobre el salario bruto con prorrateos.
5. Practicar deducciones sin respaldo documental.
6. Usar criterios distintos —mes de treinta días y días naturales— para conceptos del mismo documento.
7. No incluir los complementos de devengo superior al mes en el salario regulador.
