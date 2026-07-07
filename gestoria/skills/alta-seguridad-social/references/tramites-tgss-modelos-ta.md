# Tramites ante la TGSS y Modelos TA

> Material de referencia para la skill `alta-seguridad-social`. Relaciona cada operacion (alta o baja)
> con el modelo TA correspondiente, la via de presentacion y el circuito ante la Tesoreria General de la
> Seguridad Social (TGSS). La skill verifica los modelos y la via en cada lanzamiento y, si detecta un
> cambio, ACTUALIZA este archivo antes de preparar el tramite.

---

## Modelos TA por operacion

| Operacion | Sujeto | Modelo / tramite | Via de presentacion |
|---|---|---|---|
| Afiliacion inicial y asignacion de NUSS | Trabajador | Modelo TA.1 (solicitud de afiliacion, numero de la Seguridad Social y variacion de datos) | Import@ss; tambien la puede solicitar el empresario por el Sistema RED |
| Inscripcion de empresa y apertura del CCC principal | Empleador | Modelo TA.6 (inscripcion de empresa / apertura de cuenta de cotizacion) | Sede electronica de la TGSS / Sistema RED |
| Variacion de datos o baja del CCC | Empleador | Variaciones sobre el modelo TA.6 (TA.7 para cuentas de cotizacion secundarias) [verificar] | Sede electronica de la TGSS / Sistema RED |
| Alta o baja de trabajador por cuenta ajena | Trabajador (Regimen General) | Alta / baja del trabajador (modelo TA.2/S; en la practica se transmite por el Sistema RED) | Sistema RED (empresas y autorizados) |
| Alta o baja de empleada de hogar | Empleada de hogar (Sistema Especial) | Solicitud de alta / baja del Sistema Especial de Empleados de Hogar (modelo TA.2/S-0138) | Import@ss (el empleador de hogar no requiere autorizacion RED) |

Nota: la denominacion exacta del modelo o su codigo puede variar; verificar en el Paso 1 el modelo TA vigente antes de usarlo. Marcar `[verificar]` cualquier codigo no confirmado.

---

## Vias de presentacion

| Via | Quien la usa | Descripcion |
|---|---|---|
| Sistema RED (Remision Electronica de Datos) | Empresas del Regimen General y autorizados (gestorias, graduados sociales) | Transmision electronica obligatoria de afiliacion, cotizacion y partes. Requiere autorizacion RED y certificado. Modulos RED Directo / SILTRA. |
| Import@ss | Trabajadores, empleadores de hogar y particulares sin autorizacion RED | Portal y app de la Seguridad Social para tramites de afiliacion, altas y bajas con certificado digital, DNI-e o Cl@ve. |
| Sede electronica de la TGSS | Empresas para la inscripcion y variaciones del CCC | Registro electronico de la Seguridad Social con certificado o Cl@ve. |

---

## Circuito habitual del alta de un trabajador

1. El trabajador debe tener NUSS. Si no lo tiene, afiliacion inicial (TA.1).
2. El empleador debe estar inscrito y tener CCC. Si no lo tiene, inscripcion de empresa (TA.6).
3. El empleador comunica el alta del trabajador con caracter PREVIO al inicio, indicando CCC, NUSS, grupo de cotizacion, codigo de contrato y tipo de jornada.
4. Durante la relacion, cualquier cambio se comunica como variacion de datos.
5. Al cese, el empleador comunica la baja en plazo.

---

## Datos que exige el alta del trabajador

| Dato | Detalle |
|---|---|
| CCC del empleador | Codigo de Cuenta de Cotizacion donde se da de alta |
| NUSS del trabajador | Numero de la Seguridad Social del trabajador |
| Grupo de cotizacion | Segun la categoria profesional (grupos 1 a 11) |
| Fecha de efectos | Fecha de inicio real de la actividad |
| Codigo de contrato | Modalidad contractual (indefinido, temporal, fijo-discontinuo) |
| Tipo de jornada | Completa o parcial (coeficiente si es parcial) |
| Condicion / colectivo | Peculiaridades de cotizacion o bonificaciones si aplican [verificar] |

---

<!-- EDITAR PARA TU EQUIPO: si trabajais habitualmente con un modulo RED concreto (RED Directo o SILTRA) o con un procedimiento interno de recogida de datos, documentarlo aqui -->
