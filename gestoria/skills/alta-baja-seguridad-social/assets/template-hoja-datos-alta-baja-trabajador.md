# HOJA DE DATOS — {{TIPO_OPERACION: ALTA / BAJA}} DE TRABAJADOR EN LA SEGURIDAD SOCIAL — {{NOMBRE_TRABAJADOR}}

> **DRAFT — para revision por un gestor o asesor laboral antes de su presentacion. No constituye asesoramiento laboral.**
> Modelo y plazos verificados en la TGSS: {{FECHA_VERIFICACION}}

---

## ORGANISMO Y TRAMITE

| Campo | Valor |
|---|---|
| Organismo | Tesoreria General de la Seguridad Social (TGSS) |
| Operacion | {{TIPO_OPERACION: alta / baja}} |
| Regimen | {{SUJETO: Regimen General / Sistema Especial de Empleados de Hogar}} |
| Modelo / tramite | {{MODELO: alta-baja Regimen General (TA.2/S, via RED) / empleada de hogar (TA.2/S-0138)}} |
| Via | {{VIA_PRESENTACION: Sistema RED / Import@ss}} |
| Identificacion | {{MEDIO_IDENTIFICACION: autorizacion RED / certificado digital / DNI-e / Cl@ve}} |

---

## DATOS DEL EMPLEADOR

| Campo | Valor |
|---|---|
| Razon social o nombre | {{NOMBRE_EMPLEADOR}} |
| CIF / NIF | {{CIF_EMPLEADOR}} |
| Codigo de Cuenta de Cotizacion (CCC) | {{CCC}} |

---

## DATOS DEL TRABAJADOR

| Campo | Valor |
|---|---|
| Nombre y apellidos | {{NOMBRE_TRABAJADOR}} |
| NIF / NIE | {{NIF_TRABAJADOR}} |
| Numero de la Seguridad Social (NUSS) | {{NUSS}} |
| Grupo de cotizacion | {{GRUPO_COTIZACION}} |

---

## DATOS DE LA OPERACION

| Campo | Valor |
|---|---|
| Fecha de inicio (efectos del alta) | {{FECHA_EFECTOS}} |
| Codigo de contrato | {{CODIGO_CONTRATO}} |
| Modalidad de contrato | {{MODALIDAD_CONTRATO: indefinido / temporal / fijo-discontinuo}} |
| Tipo de jornada | {{TIPO_JORNADA: completa / parcial}} |
| Coeficiente de parcialidad (si parcial) | {{COEFICIENTE_PARCIALIDAD}} |

| Campo | Valor |
|---|---|
| Fecha de cese (efectos de la baja) | {{FECHA_EFECTOS}} |
| Causa de la baja | {{CAUSA_BAJA: fin de contrato / despido / baja voluntaria / otra}} |

---

## PLAZO APLICABLE

---

## CHECKLIST DE DOCUMENTOS Y PRESENTACION

- [ ] CCC del empleador en vigor (si no lo tiene, inscripcion de empresa previa con el modelo TA.6).
- [ ] NUSS del trabajador (si no lo tiene, afiliacion previa con el modelo TA.1).
- [ ] Documento de identidad del trabajador en vigor.
- [ ] Acceso a la via de presentacion (autorizacion del Sistema RED o certificado / Cl@ve para Import@ss).

- [ ] Contrato de trabajo o datos de la relacion laboral (modalidad, jornada, grupo de cotizacion).
- [ ] Alta transmitida ANTES del inicio de la actividad.

- [ ] Fecha y causa de cese confirmadas.
- [ ] Baja comunicada dentro del plazo aplicable.

---

> **Advertencias:**
> 1. Esta hoja de datos es un DRAFT. Debe revisarse por un gestor o asesor laboral antes de tramitar la operacion.
> 2. Modelo y plazos verificados: {{FECHA_VERIFICACION}}.
> 3. El alta debe ser PREVIA al inicio de la actividad; la baja se comunica en plazo (3 dias naturales en el Regimen General; 6 en empleadas de hogar, admitiendo Import@ss 3).
> 4. El alta o la baja fuera de plazo puede conllevar recargos, responsabilidad en prestaciones y sanciones.
> 5. Las empresas del Regimen General transmiten por el Sistema RED; el empleador de hogar por Import@ss.
