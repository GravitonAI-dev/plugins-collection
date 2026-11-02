# Fuentes Oficiales, Sedes y Plazos

> Material de referencia para la skill `alta-baja-autonomo`. Registra las fuentes normativas, las sedes de
> presentación y los plazos del alta y la baja censal (AEAT) y del alta y la baja en el RETA (Seguridad
> Social). La skill verifica estas fuentes en cada lanzamiento y, si detecta una versión posterior,
> aplica la redacción vigente al trámite que prepara, sin modificar los archivos del plugin.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla y las cuotas del ejercicio en curso. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al trámite que prepara en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Ley 20/2007, de 11 de julio, del Estatuto del Trabajo Autónomo | BOE-A-2007-13409 | texto consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409 |
| RD-ley 13/2022, nuevo sistema de cotización de autónomos | BOE-A-2022-12482 | en vigor 01/01/2023 | https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482 |

Artículos relevantes de la Ley 20/2007 para esta skill: arts. 30 a 38 bis (cotización y beneficios en la cotización). La tabla de tramos y cuotas de cada ejercicio se fija en la Ley de Presupuestos Generales del Estado (o norma que la prorrogue): verificar el ejercicio en curso en la Fase 2.1. [verificar]

---

## Sedes de presentación

| Trámite | Organismo | Sede | Identificación |
|---|---|---|---|
| Alta censal (modelo 036) | AEAT | Sede Electrónica de la AEAT (sede.agenciatributaria.gob.es) | Certificado digital, DNI-e o Cl@ve |
| Alta en el RETA | TGSS (Seguridad Social) | Import@ss (portal) e Importass app | Certificado digital, DNI-e o Cl@ve |

---

## Plazos y orden de los trámites — ALTA

| Paso | Trámite | Plazo |
|---|---|---|
| 1 | Alta censal (modelo 036) en la AEAT | ANTES del inicio de la actividad |
| 2 | Alta en el RETA en Import@ss | Hasta 60 días naturales antes del inicio; efectos desde la fecha de inicio real |

Nota: aunque el orden habitual es censo y luego RETA, el alta en el RETA puede solicitarse anticipadamente. Ambos deben estar formalizados para la fecha de inicio real de la actividad.

---

## Plazos y orden de los trámites — BAJA

| Paso | Trámite | Plazo |
|---|---|---|
| 1 | Baja en el RETA en Import@ss | 3 días naturales siguientes al cese de la actividad |
| 2 | Baja censal (modelo 036, casilla 150) en la AEAT | 1 mes desde el cese de la actividad |

Notas [verificar]:
- Ambos plazos se cuentan desde la fecha real de cese; la baja en el RETA es la más urgente (3 días naturales, se cuentan fines de semana y festivos).
- La baja censal se comunica en el modelo 036 marcando la causa de baja (casilla 150) y la fecha efectiva del cese (casilla 152). En caso de fallecimiento del obligado, el plazo es de 6 meses.
- Efectos en la cuota del RETA: desde el sistema de cotización por rendimientos reales, las tres primeras bajas de cada año natural surten efecto desde el día del cese (se cotiza solo por los días trabajados); a partir de la cuarta baja del mismo año, se cotiza el mes completo. Si la baja se comunica fuera de plazo, surte efecto la fecha de presentación y se generan cuotas hasta entonces.
- La baja censal implica dejar de ser sujeto pasivo de las obligaciones derivadas de la actividad, pero NO exime de presentar las ultimas declaraciones del periodo ni de saldar deudas pendientes.

---

## Regularización y obligaciones posteriores (aviso)

- La cuota del RETA se regulariza al año siguiente según los rendimientos reales que la AEAT comunique a la TGSS.
- Obligaciones periódicas según régimen: IVA (modelo 303 trimestral, 390 resumen anual), IRPF (pagos fraccionados 130/131), retenciones si procede (modelo 111/115), y declaración anual de la renta.

---

## Verificación de especialidades

Para regímenes especiales de IVA, alta en el ROI/VIES, actividades sujetas a módulos o especialidades autonómicas/locales (tasas, licencias de apertura), verificar con `web_search` la versión vigente antes de preparar el trámite.
