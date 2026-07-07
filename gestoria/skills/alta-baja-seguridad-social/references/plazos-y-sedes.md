# Plazos, Sedes y Regla de Auto-actualizacion

> Material de referencia para la skill `alta-baja-seguridad-social`. Registra las fuentes normativas, los plazos
> de las altas y bajas, las sedes de presentacion y la regla de auto-actualizacion. La skill verifica estas
> fuentes en cada lanzamiento y, si detecta una version posterior, ACTUALIZA el archivo correspondiente del
> plugin antes de preparar el tramite.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla, los modelos TA y los plazos vigentes. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de preparar el tramite** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| RD-legislativo 8/2015, texto refundido de la LGSS | BOE-A-2015-11724 | texto consolidado a la fecha de verificacion (en vigor 02/01/2016) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| RD 84/1996, Reglamento general de inscripcion, afiliacion, altas, bajas y variaciones | BOE-A-1996-4396 [verificar] | texto consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-1996-4396 |

Modelos TA de referencia: TA.1 (afiliacion / NUSS), TA.6 (inscripcion de empresa / CCC), TA.2/S (alta y baja de trabajador; empleada de hogar TA.2/S-0138). Verificar el modelo vigente en el Paso 1. [verificar]

---

## Plazos de las altas y bajas

| Operacion | Plazo | Efectos |
|---|---|---|
| Alta de trabajador (Regimen General) | PREVIA al inicio; puede solicitarse hasta 60 dias naturales antes | Surte efecto desde la fecha de inicio real de la actividad |
| Baja de trabajador (Regimen General) | Dentro de los 3 dias naturales siguientes al cese | Desde la fecha de cese comunicada |
| Variacion de datos | Dentro de los 3 dias naturales siguientes al cambio | Desde la fecha del cambio |
| Alta de empleada de hogar | Hasta 60 dias antes del inicio y hasta el mismo dia; si ya empezo, hasta 30 dias despues (fuera de plazo) | Desde la fecha de inicio |
| Baja de empleada de hogar | Dentro de los 6 dias naturales siguientes al cese (Import@ss admite tramitarla en 3 dias) | Desde la fecha de cese |
| Inscripcion de empresa (CCC) | PREVIA al inicio de la actividad con trabajadores | Habilita el alta de trabajadores en ese CCC |

El alta o la baja fuera de plazo puede conllevar recargos, responsabilidad en prestaciones y sanciones. Advertir al usuario.

---

## Sedes y via de presentacion

| Tramite | Organismo | Via | Identificacion |
|---|---|---|---|
| Afiliacion (TA.1) | TGSS | Import@ss (o Sistema RED por el empresario) | Certificado digital, DNI-e o Cl@ve |
| Inscripcion de empresa / CCC (TA.6) | TGSS | Sede electronica de la TGSS / Sistema RED | Certificado digital |
| Alta / baja de trabajador | TGSS | Sistema RED (empresas y autorizados) | Autorizacion RED y certificado |
| Alta / baja de empleada de hogar | TGSS | Import@ss | Certificado digital, DNI-e o Cl@ve |

Portales: Import@ss (portal.seg-social.gob.es) y app Importass; sede electronica de la Seguridad Social; Sistema RED (RED Directo / SILTRA).

---

## Obligaciones posteriores (aviso)

- Cotizacion mensual por el Sistema RED (empresas) mediante liquidacion (modelos de cotizacion y ficheros de bases).
- Comunicacion de variaciones de jornada, contrato o retribucion durante la relacion laboral.
- Conservacion de los justificantes de alta, baja y de las liquidaciones.

---

<!-- EDITAR PARA TU EQUIPO: al detectar un cambio de plazo o de modelo TA, actualizar esta tabla y la fila "Version registrada" con la fecha de verificacion -->
