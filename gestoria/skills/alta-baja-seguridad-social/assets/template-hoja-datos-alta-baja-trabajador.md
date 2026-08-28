# HOJA DE DATOS — {{tipo_operacion: ALTA / BAJA}} DE TRABAJADOR EN LA SEGURIDAD SOCIAL — {{nombre_trabajador}}

> **DRAFT — para revision por un gestor o asesor laboral antes de su presentacion. No constituye asesoramiento laboral.**
> Modelo y plazos verificados en la TGSS: {{fecha_verificacion}}

---

## ORGANISMO Y TRAMITE

| Campo | Valor |
|---|---|
| Organismo | Tesoreria General de la Seguridad Social (TGSS) |
| Operacion | {{tipo_operacion: alta / baja}} |
| Regimen | {{sujeto: Regimen General / Sistema Especial de Empleados de Hogar}} |
| Modelo / tramite | {{modelo: alta-baja Regimen General (TA.2/S, via RED) / empleada de hogar (TA.2/S-0138)}} |
| Via | {{via_presentacion: Sistema RED / Import@ss}} |
| Identificacion | {{medio_identificacion: autorizacion RED / certificado digital / DNI-e / Cl@ve}} |

---

## DATOS DEL EMPLEADOR

| Campo | Valor |
|---|---|
| Razon social o nombre | {{nombre_empleador}} |
| CIF / NIF | {{cif_empleador}} |
| Codigo de Cuenta de Cotizacion (CCC) | {{ccc}} |

---

## DATOS DEL TRABAJADOR

| Campo | Valor |
|---|---|
| Nombre y apellidos | {{nombre_trabajador}} |
| NIF / NIE | {{nif_trabajador}} |
| Numero de la Seguridad Social (NUSS) | {{nuss}} |
| Grupo de cotizacion | {{grupo_cotizacion}} |

---

## DATOS DE LA OPERACION

<!-- Si tipo_operacion es alta: -->
| Campo | Valor |
|---|---|
| Fecha de inicio (efectos del alta) | {{fecha_efectos}} |
| Codigo de contrato | {{codigo_contrato}} |
| Modalidad de contrato | {{modalidad_contrato: indefinido / temporal / fijo-discontinuo}} |
| Tipo de jornada | {{tipo_jornada: completa / parcial}} |
| Coeficiente de parcialidad (si parcial) | {{coeficiente_parcialidad}} |
<!-- Si sujeto es empleada de hogar: Retribucion mensual pactada {{retribucion}} y numero de horas semanales {{horas_semanales}} (determinan la base y la cotizacion del Sistema Especial). -->

<!-- Si tipo_operacion es baja: -->
| Campo | Valor |
|---|---|
| Fecha de cese (efectos de la baja) | {{fecha_efectos}} |
| Causa de la baja | {{causa_baja: fin de contrato / despido / baja voluntaria / otra}} |

---

## PLAZO APLICABLE

<!-- Si tipo_operacion es alta: El alta debe presentarse con caracter PREVIO al inicio (hasta 60 dias naturales antes) y surte efecto desde la fecha de inicio real. -->
<!-- Si tipo_operacion es baja y sujeto es Regimen General: La baja se comunica en los 3 dias naturales siguientes al cese. -->
<!-- Si tipo_operacion es baja y sujeto es empleada de hogar: La baja se comunica en los 6 dias naturales siguientes al cese (Import@ss admite tramitarla en 3). -->

---

## CHECKLIST DE DOCUMENTOS Y PRESENTACION

- [ ] CCC del empleador en vigor (si no lo tiene, inscripcion de empresa previa con el modelo TA.6).
- [ ] NUSS del trabajador (si no lo tiene, afiliacion previa con el modelo TA.1).
- [ ] Documento de identidad del trabajador en vigor.
- [ ] Acceso a la via de presentacion (autorizacion del Sistema RED o certificado / Cl@ve para Import@ss).
<!-- Si tipo_operacion es alta: -->
- [ ] Contrato de trabajo o datos de la relacion laboral (modalidad, jornada, grupo de cotizacion).
- [ ] Alta transmitida ANTES del inicio de la actividad.
<!-- Si tipo_operacion es baja: -->
- [ ] Fecha y causa de cese confirmadas.
- [ ] Baja comunicada dentro del plazo aplicable.

---

> **Advertencias:**
> 1. Esta hoja de datos es un DRAFT. Debe revisarse por un gestor o asesor laboral antes de tramitar la operacion.
> 2. Modelo y plazos verificados: {{fecha_verificacion}}.
> 3. El alta debe ser PREVIA al inicio de la actividad; la baja se comunica en plazo (3 dias naturales en el Regimen General; 6 en empleadas de hogar, admitiendo Import@ss 3).
> 4. El alta o la baja fuera de plazo puede conllevar recargos, responsabilidad en prestaciones y sanciones.
> 5. Las empresas del Regimen General transmiten por el Sistema RED; el empleador de hogar por Import@ss.
