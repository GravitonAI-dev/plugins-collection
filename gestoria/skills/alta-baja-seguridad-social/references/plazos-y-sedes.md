# Plazos, Sedes y Regla de Verificación

> Material de referencia para la skill `alta-baja-seguridad-social`. Registra las fuentes normativas, los plazos
> de las altas y bajas, las sedes de presentación y la regla de verificación. La skill verifica estas
> fuentes en cada lanzamiento y, si detecta una versión posterior, aplica la redacción vigente al trámite
> que prepara, sin modificar los archivos del plugin.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de esta tabla, los modelos TA y los plazos vigentes. **Si se detecta una versión posterior a la registrada, la skill aplica la redacción vigente al trámite que prepara en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| RD-legislativo 8/2015, texto refundido de la LGSS | BOE-A-2015-11724 | texto consolidado a la fecha de verificación (en vigor 02/01/2016) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| RD 84/1996, Reglamento general de inscripción, afiliación, altas, bajas y variaciones | BOE-A-1996-4396 [verificar] | texto consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-1996-4396 |

Modelos TA de referencia: TA.1 (afiliación / NUSS), TA.6 (inscripción de empresa / CCC), TA.2/S (alta y baja de trabajador; empleada de hogar TA.2/S-0138). Verificar el modelo vigente en la Fase 2.1. [verificar]

---

## Plazos de las altas y bajas

| Operación | Plazo | Efectos |
|---|---|---|
| Alta de trabajador (Régimen General) | PREVIA al inicio; puede solicitarse hasta 60 días naturales antes | Surte efecto desde la fecha de inicio real de la actividad |
| Baja de trabajador (Régimen General) | Dentro de los 3 días naturales siguientes al cese | Desde la fecha de cese comunicada |
| Variación de datos | Dentro de los 3 días naturales siguientes al cambio | Desde la fecha del cambio |
| Alta de empleada de hogar | Hasta 60 días antes del inicio y hasta el mismo día; si ya empezó, hasta 30 días después (fuera de plazo) | Desde la fecha de inicio |
| Baja de empleada de hogar | Dentro de los 6 días naturales siguientes al cese (Import@ss admite tramitarla en 3 días) | Desde la fecha de cese |
| Inscripción de empresa (CCC) | PREVIA al inicio de la actividad con trabajadores | Habilita el alta de trabajadores en ese CCC |

El alta o la baja fuera de plazo puede conllevar recargos, responsabilidad en prestaciones y sanciones. Advertir al usuario.

---

## Sedes y vía de presentación

| Trámite | Organismo | Vía | Identificación |
|---|---|---|---|
| Afiliación (TA.1) | TGSS | Import@ss (o Sistema RED por el empresario) | Certificado digital, DNI-e o Cl@ve |
| Inscripción de empresa / CCC (TA.6) | TGSS | Sede electrónica de la TGSS / Sistema RED | Certificado digital |
| Alta / baja de trabajador | TGSS | Sistema RED (empresas y autorizados) | Autorización RED y certificado |
| Alta / baja de empleada de hogar | TGSS | Import@ss | Certificado digital, DNI-e o Cl@ve |

Portales: Import@ss (portal.seg-social.gob.es) y app Importass; sede electrónica de la Seguridad Social; Sistema RED (RED Directo / SILTRA).

---

## Obligaciones posteriores (aviso)

- Cotización mensual por el Sistema RED (empresas) mediante liquidación (modelos de cotización y ficheros de bases).
- Comunicación de variaciones de jornada, contrato o retribución durante la relación laboral.
- Conservación de los justificantes de alta, baja y de las liquidaciones.

---

