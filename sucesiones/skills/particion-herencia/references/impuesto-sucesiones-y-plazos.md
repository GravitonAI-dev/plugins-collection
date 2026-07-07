# Impuesto de Sucesiones y Donaciones, Plusvalia Municipal y Plazos

> Material de referencia para la skill `particion-herencia`. Resume los tributos y plazos que la skill
> debe ADVERTIR al usuario al entregar los documentos de particion. La skill NO liquida impuestos:
> solo informa de plazos y remite a verificar la normativa autonomica con `web_search`.

---

## Impuesto sobre Sucesiones y Donaciones (ISD)

| Aspecto | Detalle |
|---|---|
| Norma estatal | Ley 29/1987, de 18 de diciembre, del Impuesto sobre Sucesiones y Donaciones (BOE-A-1987-28141) |
| Reglamento | Real Decreto 1629/1991, de 8 de noviembre |
| Naturaleza | Tributo directo que grava las adquisiciones mortis causa (herencias y legados) |
| Cesion a las CCAA | Es un tributo CEDIDO a las comunidades autonomas (Ley 22/2009). Cada CCAA regula reducciones, bonificaciones y tarifa; las diferencias entre territorios son muy grandes |
| Sujeto pasivo | Cada heredero o legatario por lo que adquiere |
| Plazo de autoliquidacion | **6 meses** desde el fallecimiento del causante, prorrogable por otros 6 meses si se solicita dentro de los 5 primeros meses |
| Competencia territorial | La CCAA de residencia habitual del causante (regla general de puntos de conexion) |

**Advertencia obligatoria de la skill**: las bonificaciones y reducciones (por parentesco, vivienda habitual, empresa familiar, discapacidad) dependen de la CCAA. La skill debe indicar al usuario que verifique la normativa vigente de su comunidad autonoma con `web_search` antes de liquidar (ejemplo de busqueda: "Impuesto Sucesiones bonificaciones [comunidad autonoma] 2025 vigente").

---

## Plusvalia municipal (IIVTNU)

| Aspecto | Detalle |
|---|---|
| Nombre | Impuesto sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana (IIVTNU) |
| Norma | Texto Refundido de la Ley Reguladora de las Haciendas Locales (RDLeg 2/2004), arts. 104 y ss.; redaccion tras el RDL 26/2021 (adaptacion a la STC 182/2021) |
| Hecho imponible | Incremento de valor de un terreno urbano que se pone de manifiesto con la transmision, tambien la mortis causa |
| Ambito | Solo inmuebles URBANOS; los rusticos no tributan por este impuesto |
| Sujeto pasivo | El heredero que adquiere el inmueble |
| Plazo | **6 meses** desde el fallecimiento (prorrogable hasta 1 ano a solicitud) |
| Competencia | El ayuntamiento donde radica el inmueble |

**Nota**: tras la STC 182/2021 y el RDL 26/2021, no hay sujecion si no existe incremento real de valor; conviene comprobar el metodo de calculo (objetivo o real) mas favorable.

---

## Otros tramites y plazos asociados

| Tramite | Plazo / momento |
|---|---|
| Certificado de defuncion | Registro Civil, tras el fallecimiento |
| Certificado de ultimas voluntades y de seguros | A partir de 15 dias habiles desde la defuncion |
| Copia autorizada del testamento o acta de declaracion de herederos | Antes de la particion |
| Autoliquidacion del ISD | 6 meses desde el fallecimiento (prorrogable) |
| Autoliquidacion de la plusvalia municipal (si hay inmueble urbano) | 6 meses desde el fallecimiento (prorrogable) |
| Escritura de aceptacion y particion e inscripcion en el Registro de la Propiedad | Tras la liquidacion de impuestos |

---

## Regla de verificacion (OBLIGATORIA para la skill)

La skill nunca calcula la cuota del ISD ni de la plusvalia. Al entregar los documentos, incluye SIEMPRE la advertencia de:
1. Que el ISD es autonomico y el plazo general es de 6 meses.
2. Que si hay inmuebles urbanos hay que liquidar tambien la plusvalia municipal, tambien en 6 meses.
3. Que la normativa autonomica del ISD debe verificarse con `web_search` para la comunidad autonoma del causante.

<!-- EDITAR PARA TU EQUIPO: fijar aqui las CCAA en las que opera habitualmente el despacho y enlazar sus portales tributarios autonomicos para agilizar la verificacion. -->
