# Fuentes Oficiales, Organismos y Plazos del Impuesto de Sucesiones

> Material de referencia para la skill `liquidacion-impuesto-sucesiones`. Registra las fuentes normativas,
> los organismos de presentación y los plazos que la skill verifica y, si detecta una versión posterior,
> aplica la redacción vigente al trámite que prepara (Fase 1). Lo lee el agente; no forma parte del output.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla y la normativa
autonómica de la CCAA competente. **Si se detecta una versión posterior a la registrada, la skill
aplica la redacción vigente al trámite que prepara en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Antes se anotaba
la nueva fecha/versión verificada. Si la fuente no es accesible, se usa la versión local, se marca
[verificar] y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Ley 29/1987 del Impuesto sobre Sucesiones y Donaciones (texto consolidado) | BOE-A-1987-28141 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141 |
| RD 1629/1991, Reglamento del ISD | BOE-A-1991-27678 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-1991-27678 |
| TR Ley Reguladora de las Haciendas Locales (plusvalía municipal, IIVTNU) | BOE-A-2004-4214 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 |
| Ley 22/2009 de financiación de las CCAA (cesión del ISD y puntos de conexión) | BOE-A-2009-20375 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2009-20375 |

Artículos relevantes de la Ley 29/1987 para esta skill: 1, 3, 5-8 (hecho imponible y sujeto pasivo), 9 (base imponible), 12-15 (cargas, deudas, gastos y ajuar), 20 (reducciones y grupos de parentesco), 21-22 (tarifa y coeficientes).

---

## Modelo y sede de presentación

| Recurso | Detalle |
|---|---|
| Modelo estatal | Modelo 650 — Autoliquidación del ISD, adquisiciones mortis causa |
| Aprobación del modelo | Orden HAP/2488/2014, de 29 de diciembre (modelos 650, 651 y 655) [verificar versión vigente] |
| Instrucciones AEAT | https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G702.shtml |
| Sede de presentación | Hacienda autonómica de la CCAA de residencia habitual del causante. Muchas CCAA usan su propio modelo y su propia sede electrónica [verificar por CCAA] |

---

## Plazos

| Trámite | Plazo |
|---|---|
| Autoliquidación del ISD (modelo 650) | 6 meses desde el fallecimiento, prorrogable por otros 6 si se solicita dentro de los 5 primeros meses |
| Certificado de ultimas voluntades y de seguros | A partir de 15 días hábiles desde la defunción |
| Plusvalía municipal (IIVTNU), si hay inmueble urbano | 6 meses desde el fallecimiento, prorrogable hasta 1 año a solicitud [verificar ordenanza] |

---

## Verificación de la normativa autonómica (OBLIGATORIA)

Ver `isd-normativa-autonomica.md`. La skill verifica con `web_search` las reducciones y bonificaciones
vigentes de la CCAA competente antes de estimar la cuota. Sin esa verificación, la estimación se marca
[verificar] y se advierte al usuario.
