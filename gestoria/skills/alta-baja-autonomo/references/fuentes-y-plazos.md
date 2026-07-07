# Fuentes Oficiales, Sedes y Plazos

> Material de referencia para la skill `alta-baja-autonomo`. Registra las fuentes normativas, las sedes de
> presentacion y los plazos del alta y la baja censal (AEAT) y del alta y la baja en el RETA (Seguridad
> Social). La skill verifica estas fuentes en cada lanzamiento y, si detecta una version posterior,
> ACTUALIZA el archivo correspondiente del plugin antes de preparar el tramite.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla y las cuotas del ejercicio en curso. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de preparar el tramite** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Ley 20/2007, de 11 de julio, del Estatuto del Trabajo Autonomo | BOE-A-2007-13409 | texto consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409 |
| RD-ley 13/2022, nuevo sistema de cotizacion de autonomos | BOE-A-2022-12482 | en vigor 01/01/2023 | https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482 |

Articulos relevantes de la Ley 20/2007 para esta skill: arts. 30 a 38 bis (cotizacion y beneficios en la cotizacion). La tabla de tramos y cuotas de cada ejercicio se fija en la Ley de Presupuestos Generales del Estado (o norma que la prorrogue): verificar el ejercicio en curso en el Paso 1. [verificar]

---

## Sedes de presentacion

| Tramite | Organismo | Sede | Identificacion |
|---|---|---|---|
| Alta censal (modelo 036) | AEAT | Sede Electronica de la AEAT (sede.agenciatributaria.gob.es) | Certificado digital, DNI-e o Cl@ve |
| Alta en el RETA | TGSS (Seguridad Social) | Import@ss (portal) e Importass app | Certificado digital, DNI-e o Cl@ve |

---

## Plazos y orden de los tramites — ALTA

| Paso | Tramite | Plazo |
|---|---|---|
| 1 | Alta censal (modelo 036) en la AEAT | ANTES del inicio de la actividad |
| 2 | Alta en el RETA en Import@ss | Hasta 60 dias naturales antes del inicio; efectos desde la fecha de inicio real |

Nota: aunque el orden habitual es censo y luego RETA, el alta en el RETA puede solicitarse anticipadamente. Ambos deben estar formalizados para la fecha de inicio real de la actividad.

---

## Plazos y orden de los tramites — BAJA

| Paso | Tramite | Plazo |
|---|---|---|
| 1 | Baja en el RETA en Import@ss | 3 dias naturales siguientes al cese de la actividad |
| 2 | Baja censal (modelo 036, casilla 150) en la AEAT | 1 mes desde el cese de la actividad |

Notas [verificar]:
- Ambos plazos se cuentan desde la fecha real de cese; la baja en el RETA es la mas urgente (3 dias naturales, se cuentan fines de semana y festivos).
- La baja censal se comunica en el modelo 036 marcando la causa de baja (casilla 150) y la fecha efectiva del cese (casilla 152). En caso de fallecimiento del obligado, el plazo es de 6 meses.
- Efectos en la cuota del RETA: desde el sistema de cotizacion por rendimientos reales, las tres primeras bajas de cada ano natural surten efecto desde el dia del cese (se cotiza solo por los dias trabajados); a partir de la cuarta baja del mismo ano, se cotiza el mes completo. Si la baja se comunica fuera de plazo, surte efecto la fecha de presentacion y se generan cuotas hasta entonces.
- La baja censal implica dejar de ser sujeto pasivo de las obligaciones derivadas de la actividad, pero NO exime de presentar las ultimas declaraciones del periodo ni de saldar deudas pendientes.

---

## Regularizacion y obligaciones posteriores (aviso)

- La cuota del RETA se regulariza al ano siguiente segun los rendimientos reales que la AEAT comunique a la TGSS.
- Obligaciones periodicas segun regimen: IVA (modelo 303 trimestral, 390 resumen anual), IRPF (pagos fraccionados 130/131), retenciones si procede (modelo 111/115), y declaracion anual de la renta.

---

## Verificacion de especialidades

Para regimenes especiales de IVA, alta en el ROI/VIES, actividades sujetas a modulos o especialidades autonomicas/locales (tasas, licencias de apertura), verificar con `web_search` la version vigente antes de preparar el tramite.
