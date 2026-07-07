# Fuentes Oficiales, Organismos y Plazos del Impuesto de Sucesiones

> Material de referencia para la skill `liquidacion-impuesto-sucesiones`. Registra las fuentes normativas,
> los organismos de presentacion y los plazos que la skill verifica y, si detecta una version posterior,
> ACTUALIZA en el plugin en cada lanzamiento (Paso 1). Lo lee el agente; no forma parte del output.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla y la normativa
autonomica de la CCAA competente. **Si se detecta una version posterior a la registrada, la skill
actualiza el archivo correspondiente del plugin (reference o asset) antes de preparar el tramite** y anota
la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local, se marca
[verificar] y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Ley 29/1987 del Impuesto sobre Sucesiones y Donaciones (texto consolidado) | BOE-A-1987-28141 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141 |
| RD 1629/1991, Reglamento del ISD | BOE-A-1991-27678 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-1991-27678 |
| TR Ley Reguladora de las Haciendas Locales (plusvalia municipal, IIVTNU) | BOE-A-2004-4214 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 |
| Ley 22/2009 de financiacion de las CCAA (cesion del ISD y puntos de conexion) | BOE-A-2009-20375 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2009-20375 |

Articulos relevantes de la Ley 29/1987 para esta skill: 1, 3, 5-8 (hecho imponible y sujeto pasivo), 9 (base imponible), 12-15 (cargas, deudas, gastos y ajuar), 20 (reducciones y grupos de parentesco), 21-22 (tarifa y coeficientes).

---

## Modelo y sede de presentacion

| Recurso | Detalle |
|---|---|
| Modelo estatal | Modelo 650 — Autoliquidacion del ISD, adquisiciones mortis causa |
| Aprobacion del modelo | Orden HAP/2488/2014, de 29 de diciembre (modelos 650, 651 y 655) [verificar version vigente] |
| Instrucciones AEAT | https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G702.shtml |
| Sede de presentacion | Hacienda autonomica de la CCAA de residencia habitual del causante. Muchas CCAA usan su propio modelo y su propia sede electronica [verificar por CCAA] |

<!-- EDITAR PARA TU EQUIPO: enlazar aqui las sedes electronicas de las Haciendas autonomicas donde el despacho presenta con mas frecuencia y su modelo autonomico equivalente al 650. -->

---

## Plazos

| Tramite | Plazo |
|---|---|
| Autoliquidacion del ISD (modelo 650) | 6 meses desde el fallecimiento, prorrogable por otros 6 si se solicita dentro de los 5 primeros meses |
| Certificado de ultimas voluntades y de seguros | A partir de 15 dias habiles desde la defuncion |
| Plusvalia municipal (IIVTNU), si hay inmueble urbano | 6 meses desde el fallecimiento, prorrogable hasta 1 ano a solicitud [verificar ordenanza] |

---

## Verificacion de la normativa autonomica (OBLIGATORIA)

Ver `isd-normativa-autonomica.md`. La skill verifica con `web_search` las reducciones y bonificaciones
vigentes de la CCAA competente antes de estimar la cuota. Sin esa verificacion, la estimacion se marca
[verificar] y se advierte al usuario.
