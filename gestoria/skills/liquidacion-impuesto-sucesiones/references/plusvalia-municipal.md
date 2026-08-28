# IIVTNU — Plusvalia Municipal en la Transmision Mortis Causa

> Material de referencia para la skill `liquidacion-impuesto-sucesiones`. Resume cuando aplica la plusvalia
> municipal por heredar inmuebles urbanos y sus plazos, para que la skill AVISE al usuario. La skill NO
> calcula ni presenta la plusvalia: solo informa. Lo lee el agente; no forma parte del output al usuario.

---

## Que es y cuando aplica

| Aspecto | Detalle |
|---|---|
| Nombre | Impuesto sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana (IIVTNU) |
| Norma | Texto Refundido de la Ley Reguladora de las Haciendas Locales (RDLeg 2/2004, BOE-A-2004-4214), Arts. 104 y ss.; redaccion tras el RDL 26/2021 (adaptacion a la STC 182/2021) |
| Hecho imponible | Incremento de valor de un terreno URBANO que se pone de manifiesto con la transmision, tambien la mortis causa |
| Ambito | Solo inmuebles URBANOS; los rusticos no tributan por este impuesto |
| Sujeto pasivo | El heredero que adquiere el inmueble |
| Competencia | El ayuntamiento donde radica el inmueble (no la Hacienda autonomica) |
| Plazo | 6 meses desde el fallecimiento, prorrogable hasta 1 ano a solicitud [verificar en la ordenanza municipal] |

---

## Puntos a advertir

- Es un tributo DISTINTO del Impuesto de Sucesiones: distinto organismo (ayuntamiento), distinto calculo y distinto plazo. Ambos conviven cuando la herencia incluye inmuebles urbanos.
- Tras la STC 182/2021 y el RDL 26/2021, no hay sujecion si no existe incremento real de valor del terreno. Conviene comparar el metodo objetivo y el metodo de calculo real y elegir el mas favorable. [verificar]
- El calculo y las bonificaciones (por ejemplo, por vivienda habitual del causante) dependen de la ORDENANZA de cada ayuntamiento. [verificar]

---

## Regla para la skill

Si la herencia incluye al menos un inmueble urbano, la skill incluye SIEMPRE el aviso de la plusvalia municipal en el borrador y en el checklist: organismo (ayuntamiento del inmueble), plazo (6 meses, prorrogable) y recomendacion de comparar el metodo de calculo. La skill NO calcula la cuota de la plusvalia.
