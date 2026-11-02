# Impuesto de Sucesiones y Donaciones, Plusvalía Municipal y Plazos

> Material de referencia para la skill `derecho-civil-herencia`. Resume los tributos y plazos que la skill
> debe ADVERTIR al usuario al entregar los documentos de partición. La skill NO liquida impuestos:
> solo informa de plazos y remite a verificar la normativa autonómica con `web_search`.

---

## Impuesto sobre Sucesiones y Donaciones (ISD)

| Aspecto | Detalle |
|---|---|
| Norma estatal | Ley 29/1987, de 18 de diciembre, del Impuesto sobre Sucesiones y Donaciones (BOE-A-1987-28141, consolidado verificado el 31/08/2026, última actualización publicada el 28/12/2022) |
| Reglamento | Real Decreto 1629/1991, de 8 de noviembre (BOE-A-1991-27678, consolidado verificado el 31/08/2026, última actualización publicada el 05/04/2023) |
| Naturaleza | Tributo directo que grava las adquisiciones mortis causa (herencias y legados) |
| Cesión a las CCAA | Es un tributo CEDIDO a las comunidades autónomas (Ley 22/2009). Cada CCAA regula reducciones, bonificaciones y tarifa; las diferencias entre territorios son muy grandes |
| Sujeto pasivo | Cada heredero o legatario por lo que adquiere |
| Plazo de autoliquidación | **6 meses** desde el fallecimiento del causante (Art. 67.1.a RD 1629/1991), prorrogable por otro plazo igual si se solicita dentro de los 5 primeros meses (Art. 68 RD 1629/1991: silencio positivo al mes de la solicitud; la prórroga devenga intereses de demora) |
| Renuncia a la herencia | Art. 28 Ley 29/1987: en la renuncia pura, simple y gratuita tributan los beneficiarios (con el parentesco del renunciante si es superior); en la renuncia a favor de persona determinada tributa el renunciante y además se liquida la cesión o donación; la renuncia tras prescribir el impuesto se reputa donación. Ver `cc-aceptacion-renuncia-division.md` |
| Competencia territorial | La CCAA de residencia habitual del causante (regla general de puntos de conexión) |

**Advertencia obligatoria de la skill**: las bonificaciones y reducciones (por parentesco, vivienda habitual, empresa familiar, discapacidad) dependen de la CCAA. La skill debe indicar al usuario que verifique la normativa vigente de su comunidad autónoma con `web_search` antes de liquidar (ejemplo de búsqueda: "Impuesto Sucesiones bonificaciones [comunidad autónoma] 2025 vigente").

---

## Plusvalía municipal (IIVTNU)

| Aspecto | Detalle |
|---|---|
| Nombre | Impuesto sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana (IIVTNU) |
| Norma | Texto Refundido de la Ley Reguladora de las Haciendas Locales (RDLeg 2/2004), arts. 104 y ss.; redacción tras el RDL 26/2021 (adaptación a la STC 182/2021) |
| Hecho imponible | Incremento de valor de un terreno urbano que se pone de manifiesto con la transmisión, también la mortis causa |
| Ámbito | Solo inmuebles URBANOS; los rústicos no tributan por este impuesto |
| Sujeto pasivo | El heredero que adquiere el inmueble |
| Plazo | **6 meses** desde el fallecimiento (prorrogable hasta 1 año a solicitud) |
| Competencia | El ayuntamiento donde radica el inmueble |

**Nota**: tras la STC 182/2021 y el RDL 26/2021, no hay sujeción si no existe incremento real de valor; conviene comprobar el método de cálculo (objetivo o real) más favorable.

---

## Otros trámites y plazos asociados

| Trámite | Plazo / momento |
|---|---|
| Certificado de defunción | Registro Civil, tras el fallecimiento |
| Certificado de ultimas voluntades y de seguros | A partir de 15 días hábiles desde la defunción |
| Copia autorizada del testamento o acta de declaración de herederos | Antes de la partición |
| Autoliquidación del ISD | 6 meses desde el fallecimiento (prorrogable) |
| Autoliquidación de la plusvalía municipal (si hay inmueble urbano) | 6 meses desde el fallecimiento (prorrogable) |
| Escritura de aceptación y partición e inscripción en el Registro de la Propiedad | Tras la liquidación de impuestos |

---

## Regla de verificación (OBLIGATORIA para la skill)

La skill nunca calcula la cuota del ISD ni de la plusvalía. Al entregar los documentos, incluye SIEMPRE la advertencia de:
1. Que el ISD es autonómico y el plazo general es de 6 meses.
2. Que si hay inmuebles urbanos hay que liquidar también la plusvalía municipal, también en 6 meses.
3. Que la normativa autonómica del ISD debe verificarse con `web_search` para la comunidad autónoma del causante.

