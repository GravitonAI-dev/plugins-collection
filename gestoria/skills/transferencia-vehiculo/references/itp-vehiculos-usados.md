# ITP — Vehículos Usados (Modelo 620)

> Material de referencia para la skill `transferencia-vehiculo`. Basado en el Texto Refundido de la
> Ley del Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados (RD Legislativo 1/1993),
> en su modalidad de Transmisiones Patrimoniales Onerosas (TPO), y en la Orden anual de precios medios de
> venta que publica el Ministerio de Hacienda. La skill verifica en cada lanzamiento la Orden vigente y los
> tipos autonómicos antes de estimar el impuesto. El importe nunca es definitivo hasta la autoliquidación.

---

## Cuándo aplica el ITP

La compraventa de un vehículo usado entre particulares está sujeta a la modalidad de Transmisiones Patrimoniales Onerosas (TPO) del ITP. Lo paga el comprador (adquirente) y su liquidación es requisito previo para la transferencia en la DGT.

No aplica el ITP (o aplica IVA en su lugar) cuando el vendedor es empresario o profesional que transmite en el ejercicio de su actividad (factura con IVA). En ese caso, la factura sustituye al modelo 620.

---

## Base imponible: el valor de mercado (valor venal)

La base imponible es el **mayor** valor entre:
1. El precio pactado entre comprador y vendedor.
2. El valor de mercado del vehículo (valor venal) según las tablas oficiales.

El valor de mercado se obtiene de la Orden anual del Ministerio de Hacienda de precios medios de venta, aplicando a la marca, modelo y potencia el coeficiente de depreciación según los años de antigüedad (desde el 100% para vehículos de hasta un año hasta el 10% para vehículos de más de doce años).

| Antigüedad del vehículo | Coeficiente aproximado sobre el precio medio |
|---|---|
| Hasta 1 año | 100% |
| Entre 1 y 2 años | 84% |
| Entre 5 y 6 años | 43% |
| Más de 12 años | 10% |

---

## Tipo de gravamen (varía por comunidad autónoma)

El ITP está cedido a las comunidades autónomas, que fijan el tipo aplicable a la transmisión de vehículos. A título orientativo, el tipo se mueve habitualmente entre el 4% y el 8% según la comunidad autónoma.

| Referencia | Tipo orientativo |
|---|---|
| Tipo general estatal supletorio para bienes muebles | 4% |
| Rango habitual entre comunidades autónomas | 4% - 8% |

Cuota estimada = base imponible (mayor valor) x tipo autonómico. La skill ofrece una estimación; el importe definitivo se fija en la autoliquidación.

---

## Modelo, plazo y organismo

| Elemento | Detalle |
|---|---|
| Modelo | 620 (autoliquidación de transmisión de vehículos usados); algunas CCAA usan el 621 o tramitación telemática propia |
| Quién paga | El comprador (adquirente) |
| Plazo | Habitualmente 30 días hábiles desde la fecha de la transmisión (verificar el plazo exacto de la comunidad autónoma) |
| Organismo | Hacienda de la comunidad autónoma del domicilio del comprador |
| Efecto | La autoliquidación presentada y pagada (o la exención) es requisito para el cambio de titularidad en la DGT |

---

## Exenciones y supuestos frecuentes

- Transmisión por empresario o profesional en su actividad: tributa por IVA, no por ITP (factura con IVA).
- Algunas comunidades autónomas contemplan exenciones o cuotas reducidas para vehículos de más de determinada antigüedad o de baja cilindrada.
- La transmisión entre familiares no está, por si sola, exenta de ITP salvo previsión autonómica expresa.

---

## Regla práctica para la skill

1. Estimar la base imponible (mayor entre precio y valor de mercado).
2. Advertir del tipo aproximado de la comunidad autónoma indicada por el usuario.
3. Marcar el importe como estimación y recomendar verificar en la Hacienda autonómica antes de presentar.
4. Recordar que sin la autoliquidación del ITP (o su exención) la DGT no completa la transferencia.
