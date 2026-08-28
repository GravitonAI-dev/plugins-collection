# ITP — Vehiculos Usados (Modelo 620)

> Material de referencia para la skill `transferencia-vehiculo`. Basado en el Texto Refundido de la
> Ley del Impuesto sobre Transmisiones Patrimoniales y Actos Juridicos Documentados (RD Legislativo 1/1993),
> en su modalidad de Transmisiones Patrimoniales Onerosas (TPO), y en la Orden anual de precios medios de
> venta que publica el Ministerio de Hacienda. La skill verifica en cada lanzamiento la Orden vigente y los
> tipos autonomicos antes de estimar el impuesto. El importe nunca es definitivo hasta la autoliquidacion.

---

## Cuando aplica el ITP

La compraventa de un vehiculo usado entre particulares esta sujeta a la modalidad de Transmisiones Patrimoniales Onerosas (TPO) del ITP. Lo paga el comprador (adquirente) y su liquidacion es requisito previo para la transferencia en la DGT.

No aplica el ITP (o aplica IVA en su lugar) cuando el vendedor es empresario o profesional que transmite en el ejercicio de su actividad (factura con IVA). En ese caso, la factura sustituye al modelo 620.

---

## Base imponible: el valor de mercado (valor venal)

La base imponible es el **mayor** valor entre:
1. El precio pactado entre comprador y vendedor.
2. El valor de mercado del vehiculo (valor venal) segun las tablas oficiales.

El valor de mercado se obtiene de la Orden anual del Ministerio de Hacienda de precios medios de venta, aplicando a la marca, modelo y potencia el coeficiente de depreciacion segun los anos de antiguedad (desde el 100% para vehiculos de hasta un ano hasta el 10% para vehiculos de mas de doce anos).

| Antiguedad del vehiculo | Coeficiente aproximado sobre el precio medio |
|---|---|
| Hasta 1 ano | 100% |
| Entre 1 y 2 anos | 84% |
| Entre 5 y 6 anos | 43% |
| Mas de 12 anos | 10% |

---

## Tipo de gravamen (varia por comunidad autonoma)

El ITP esta cedido a las comunidades autonomas, que fijan el tipo aplicable a la transmision de vehiculos. A titulo orientativo, el tipo se mueve habitualmente entre el 4% y el 8% segun la comunidad autonoma.

| Referencia | Tipo orientativo |
|---|---|
| Tipo general estatal supletorio para bienes muebles | 4% |
| Rango habitual entre comunidades autonomas | 4% - 8% |

Cuota estimada = base imponible (mayor valor) x tipo autonomico. La skill ofrece una estimacion; el importe definitivo se fija en la autoliquidacion.

---

## Modelo, plazo y organismo

| Elemento | Detalle |
|---|---|
| Modelo | 620 (autoliquidacion de transmision de vehiculos usados); algunas CCAA usan el 621 o tramitacion telematica propia |
| Quien paga | El comprador (adquirente) |
| Plazo | Habitualmente 30 dias habiles desde la fecha de la transmision (verificar el plazo exacto de la comunidad autonoma) |
| Organismo | Hacienda de la comunidad autonoma del domicilio del comprador |
| Efecto | La autoliquidacion presentada y pagada (o la exencion) es requisito para el cambio de titularidad en la DGT |

---

## Exenciones y supuestos frecuentes

- Transmision por empresario o profesional en su actividad: tributa por IVA, no por ITP (factura con IVA).
- Algunas comunidades autonomas contemplan exenciones o cuotas reducidas para vehiculos de mas de determinada antiguedad o de baja cilindrada.
- La transmision entre familiares no esta, por si sola, exenta de ITP salvo prevision autonomica expresa.

---

## Regla practica para la skill

1. Estimar la base imponible (mayor entre precio y valor de mercado).
2. Advertir del tipo aproximado de la comunidad autonoma indicada por el usuario.
3. Marcar el importe como estimacion y recomendar verificar en la Hacienda autonomica antes de presentar.
4. Recordar que sin la autoliquidacion del ITP (o su exencion) la DGT no completa la transferencia.
