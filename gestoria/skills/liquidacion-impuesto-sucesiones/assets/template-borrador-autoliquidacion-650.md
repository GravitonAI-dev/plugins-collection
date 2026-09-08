# BORRADOR DE AUTOLIQUIDACION DEL IMPUESTO DE SUCESIONES (MODELO 650)

> **DRAFT — para revision por un gestor o asesor fiscal antes de su presentacion. No constituye asesoramiento fiscal ni juridico.**
> Version de la Ley 29/1987 verificada en el BOE: {{FECHA_VERIFICACION_ISD}}
> Comunidad autonoma competente: {{COMUNIDAD_AUTONOMA}}
> IMPORTANTE: la cuota es una ESTIMACION , no la cuota definitiva.

---

## 1. Tributo y organismo

| Campo | Valor |
|---|---|
| Tributo | Impuesto sobre Sucesiones y Donaciones (adquisiciones mortis causa) |
| Modelo | 650 (o modelo autonomico equivalente {{MODELO_AUTONOMICO}} ) |
| Organismo competente | Hacienda autonomica de {{COMUNIDAD_AUTONOMA}} |
| Sede de presentacion | {{SEDE_PRESENTACION}} |
| Plazo | 6 meses desde el fallecimiento, prorrogable por otros 6 (solicitud dentro de los 5 primeros meses) |
| Fecha limite estimada | {{FECHA_LIMITE}} |

## 2. Causante

| Campo | Valor |
|---|---|
| Nombre | {{NOMBRE_CAUSANTE}} |
| NIF | {{NIF_CAUSANTE}} |
| Fecha de fallecimiento | {{FECHA_FALLECIMIENTO}} |
| Lugar de fallecimiento | {{LUGAR_FALLECIMIENTO}} |
| Ultimo domicilio | {{ULTIMO_DOMICILIO_CAUSANTE}} |
| CCAA de residencia habitual | {{COMUNIDAD_AUTONOMA}} |

## 3. Sujeto pasivo (heredero)

| Campo | Valor |
|---|---|
| Nombre | {{NOMBRE_HEREDERO}} |
| NIF | {{NIF_HEREDERO}} |
| Domicilio | {{DOMICILIO_HEREDERO}} |
| Parentesco con el causante | {{PARENTESCO}} |
| Grupo (I a IV) | {{GRUPO_PARENTESCO}} |
| Patrimonio preexistente (si la CCAA lo exige) | {{PATRIMONIO_PREEXISTENTE}} |

## 4. Caudal hereditario

**A) Activo (bienes y derechos):**

| N. | Bien / derecho | Referencia / identificacion | Valor (EUR) |
|---|---|---|---|
| {{NUMERO_ORDEN_ACTIVO: número de orden}} | {{DESCRIPCION_BIEN: bien o derecho inventariado}} | {{IDENTIFICACION_BIEN: referencia catastral, matrícula, IBAN o dato que lo identifique}} | {{VALOR_BIEN: importe en euros}} |

(Repetir una fila por cada bien o derecho del caudal relicto.)

Ajuar domestico (Art. 15; 3% del caudal relicto salvo prueba): {{VALOR_AJUAR}} EUR 

Total caudal relicto: {{TOTAL_CAUDAL_RELICTO}} EUR

**B) Cargas, deudas y gastos deducibles (Arts. 12-14):**

| N. | Concepto | Importe (EUR) |
|---|---|---|
| {{NUMERO_ORDEN_DEDUCCION: número de orden}} | {{CONCEPTO_DEDUCIBLE: carga, deuda o gasto deducible}} | {{IMPORTE_DEDUCIBLE: importe en euros}} |

(Repetir una fila por cada carga, deuda o gasto deducible debidamente justificado.)

Total deducible: {{TOTAL_DEDUCIBLE}} EUR

**C) Seguros de vida (beneficiario el heredero):** {{IMPORTE_SEGUROS_VIDA}} EUR

## 5. Calculo estimado (todos los importes )

| Concepto | Importe (EUR) |
|---|---|
| Masa hereditaria neta (caudal relicto - deducible) | {{MASA_NETA}} |
| Porcion individual del heredero | {{PORCION_INDIVIDUAL}} |
| (+) Seguros de vida acumulados | {{IMPORTE_SEGUROS_VIDA}} |
| Base imponible | {{BASE_IMPONIBLE}} |
| (-) Reduccion por parentesco (Grupo {{GRUPO_PARENTESCO}}) | {{REDUCCION_PARENTESCO}} |
| (-) Reduccion por seguros de vida (Art. 20.2.b) | {{REDUCCION_SEGUROS}} |
| (-) Reduccion vivienda habitual (Art. 20.2.c) | {{REDUCCION_VIVIENDA}} |
| (-) Reduccion empresa familiar (Art. 20.2.c) | {{REDUCCION_EMPRESA}} |
| (-) Reduccion por discapacidad | {{REDUCCION_DISCAPACIDAD}} |
| Base liquidable | {{BASE_LIQUIDABLE}} |
| Cuota integra (tarifa aplicada) | {{CUOTA_INTEGRA}} |
| Coeficiente multiplicador (grupo / patrimonio) | {{COEFICIENTE_MULTIPLICADOR}} |
| Cuota tributaria | {{CUOTA_TRIBUTARIA}} |
| (-) Bonificacion autonomica de la cuota | {{BONIFICACION_AUTONOMICA}} |
| **Cuota estimada a ingresar** | **{{CUOTA_A_INGRESAR}} ** |

Regimen autonomico aplicado (fuente verificada): {{FUENTE_NORMATIVA_AUTONOMICA}} 

## 6. Plusvalia municipal (IIVTNU)

---

> **Advertencias:**
> 1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un gestor o asesor fiscal antes de su presentacion.
> 2. La cuota es una ESTIMACION , no la cuota definitiva. Los importes, reducciones y bonificaciones dependen de la CCAA {{COMUNIDAD_AUTONOMA}} y del ejercicio.
> 3. Version de la Ley 29/1987 verificada: {{FECHA_VERIFICACION_ISD}}.
> 4. Plazo: 6 meses desde el fallecimiento, prorrogable por otros 6 (solicitud dentro de los 5 primeros meses).
> 5. Organismo: Hacienda autonomica de {{COMUNIDAD_AUTONOMA}}. Modelo 650 o el autonomico equivalente .
> 6. Si hay inmuebles urbanos, liquidar ademas la plusvalia municipal (IIVTNU) en el ayuntamiento correspondiente.
