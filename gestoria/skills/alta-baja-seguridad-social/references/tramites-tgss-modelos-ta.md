# Trámites ante la TGSS y Modelos TA

> Material de referencia para la skill `alta-baja-seguridad-social`. Relaciona cada operación (alta o baja)
> con el modelo TA correspondiente, la vía de presentación y el circuito ante la Tesorería General de la
> Seguridad Social (TGSS). La skill verifica los modelos y la vía en cada lanzamiento y, si detecta un
> cambio, ACTUALIZA este archivo antes de preparar el trámite.

---

## Modelos TA por operación

| Operación | Sujeto | Modelo / trámite | Vía de presentación |
|---|---|---|---|
| Afiliación inicial y asignación de NUSS | Trabajador | Modelo TA.1 (solicitud de afiliación, número de la Seguridad Social y variación de datos) | Import@ss; también la puede solicitar el empresario por el Sistema RED |
| Inscripción de empresa y apertura del CCC principal | Empleador | Modelo TA.6 (inscripción de empresa / apertura de cuenta de cotización) | Sede electrónica de la TGSS / Sistema RED |
| Variación de datos o baja del CCC | Empleador | Variaciones sobre el modelo TA.6 (TA.7 para cuentas de cotización secundarias) [verificar] | Sede electrónica de la TGSS / Sistema RED |
| Alta o baja de trabajador por cuenta ajena | Trabajador (Régimen General) | Alta / baja del trabajador (modelo TA.2/S; en la práctica se transmite por el Sistema RED) | Sistema RED (empresas y autorizados) |
| Alta o baja de empleada de hogar | Empleada de hogar (Sistema Especial) | Solicitud de alta / baja del Sistema Especial de Empleados de Hogar (modelo TA.2/S-0138) | Import@ss (el empleador de hogar no requiere autorización RED) |

Nota: la denominación exacta del modelo o su código puede variar; verificar en la Fase 2.1 el modelo TA vigente antes de usarlo. Marcar `[verificar]` cualquier código no confirmado.

---

## Vías de presentación

| Vía | Quién la usa | Descripción |
|---|---|---|
| Sistema RED (Remisión Electrónica de Datos) | Empresas del Régimen General y autorizados (gestorías, graduados sociales) | Transmisión electrónica obligatoria de afiliación, cotización y partes. Requiere autorización RED y certificado. Módulos RED Directo / SILTRA. |
| Import@ss | Trabajadores, empleadores de hogar y particulares sin autorización RED | Portal y app de la Seguridad Social para trámites de afiliación, altas y bajas con certificado digital, DNI-e o Cl@ve. |
| Sede electrónica de la TGSS | Empresas para la inscripción y variaciones del CCC | Registro electrónico de la Seguridad Social con certificado o Cl@ve. |

---

## Circuito habitual del alta de un trabajador

1. El trabajador debe tener NUSS. Si no lo tiene, afiliación inicial (TA.1).
2. El empleador debe estar inscrito y tener CCC. Si no lo tiene, inscripción de empresa (TA.6).
3. El empleador comunica el alta del trabajador con carácter PREVIO al inicio, indicando CCC, NUSS, grupo de cotización, código de contrato y tipo de jornada.
4. Durante la relación, cualquier cambio se comunica como variación de datos.
5. Al cese, el empleador comunica la baja en plazo.

---

## Datos que exige el alta del trabajador

| Dato | Detalle |
|---|---|
| CCC del empleador | Código de Cuenta de Cotización donde se da de alta |
| NUSS del trabajador | Número de la Seguridad Social del trabajador |
| Grupo de cotización | Según la categoría profesional (grupos 1 a 11) |
| Fecha de efectos | Fecha de inicio real de la actividad |
| Código de contrato | Modalidad contractual (indefinido, temporal, fijo-discontinuo) |
| Tipo de jornada | Completa o parcial (coeficiente si es parcial) |
| Condición / colectivo | Peculiaridades de cotización o bonificaciones si aplican [verificar] |

---

