# BORRADOR DE AUTOLIQUIDACION DEL IMPUESTO DE SUCESIONES (MODELO 650)

> **DRAFT — para revision por un gestor o asesor fiscal antes de su presentacion. No constituye asesoramiento fiscal ni juridico.**
> Version de la Ley 29/1987 verificada en el BOE: {{fecha_verificacion_isd}}
> Comunidad autonoma competente: {{comunidad_autonoma}}
> IMPORTANTE: la cuota es una ESTIMACION [verificar], no la cuota definitiva.

---

## 1. Tributo y organismo

| Campo | Valor |
|---|---|
| Tributo | Impuesto sobre Sucesiones y Donaciones (adquisiciones mortis causa) |
| Modelo | 650 (o modelo autonomico equivalente {{modelo_autonomico}} [verificar]) |
| Organismo competente | Hacienda autonomica de {{comunidad_autonoma}} |
| Sede de presentacion | {{sede_presentacion}} [verificar] |
| Plazo | 6 meses desde el fallecimiento, prorrogable por otros 6 (solicitud dentro de los 5 primeros meses) |
| Fecha limite estimada | {{fecha_limite}} |

## 2. Causante

| Campo | Valor |
|---|---|
| Nombre | {{nombre_causante}} |
| NIF | {{nif_causante}} |
| Fecha de fallecimiento | {{fecha_fallecimiento}} |
| Lugar de fallecimiento | {{lugar_fallecimiento}} |
| Ultimo domicilio | {{ultimo_domicilio_causante}} |
| CCAA de residencia habitual | {{comunidad_autonoma}} |

## 3. Sujeto pasivo (heredero)

| Campo | Valor |
|---|---|
| Nombre | {{nombre_heredero}} |
| NIF | {{nif_heredero}} |
| Domicilio | {{domicilio_heredero}} |
| Parentesco con el causante | {{parentesco}} |
| Grupo (I a IV) | {{grupo_parentesco}} |
| Patrimonio preexistente (si la CCAA lo exige) | {{patrimonio_preexistente}} [verificar] |

## 4. Caudal hereditario

**A) Activo (bienes y derechos):**

| N. | Bien / derecho | Referencia / identificacion | Valor (EUR) |
|---|---|---|---|
{{inventario_activo: una fila por bien. Ej.: 1 | Vivienda | Ref. catastral [REF] | [VALOR] }}

Ajuar domestico (Art. 15; 3% del caudal relicto salvo prueba): {{valor_ajuar}} EUR [verificar]

Total caudal relicto: {{total_caudal_relicto}} EUR

**B) Cargas, deudas y gastos deducibles (Arts. 12-14):**

| N. | Concepto | Importe (EUR) |
|---|---|---|
{{deducciones: una fila por concepto. Ej.: 1 | Gastos de ultima enfermedad, entierro y funeral | [VALOR] }}

Total deducible: {{total_deducible}} EUR

**C) Seguros de vida (beneficiario el heredero):** {{importe_seguros_vida}} EUR

## 5. Calculo estimado (todos los importes [verificar])

| Concepto | Importe (EUR) |
|---|---|
| Masa hereditaria neta (caudal relicto - deducible) | {{masa_neta}} [verificar] |
| Porcion individual del heredero | {{porcion_individual}} [verificar] |
| (+) Seguros de vida acumulados | {{importe_seguros_vida}} [verificar] |
| Base imponible | {{base_imponible}} [verificar] |
| (-) Reduccion por parentesco (Grupo {{grupo_parentesco}}) | {{reduccion_parentesco}} [verificar] |
| (-) Reduccion por seguros de vida (Art. 20.2.b) | {{reduccion_seguros}} [verificar] |
| (-) Reduccion vivienda habitual (Art. 20.2.c) | {{reduccion_vivienda}} [verificar] |
| (-) Reduccion empresa familiar (Art. 20.2.c) | {{reduccion_empresa}} [verificar] |
| (-) Reduccion por discapacidad | {{reduccion_discapacidad}} [verificar] |
| Base liquidable | {{base_liquidable}} [verificar] |
| Cuota integra (tarifa aplicada) | {{cuota_integra}} [verificar] |
| Coeficiente multiplicador (grupo / patrimonio) | {{coeficiente_multiplicador}} [verificar] |
| Cuota tributaria | {{cuota_tributaria}} [verificar] |
| (-) Bonificacion autonomica de la cuota | {{bonificacion_autonomica}} [verificar] |
| **Cuota estimada a ingresar** | **{{cuota_a_ingresar}} [verificar]** |

Regimen autonomico aplicado (fuente verificada): {{fuente_normativa_autonomica}} [verificar]

## 6. Plusvalia municipal (IIVTNU)

---

> **Advertencias:**
> 1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un gestor o asesor fiscal antes de su presentacion.
> 2. La cuota es una ESTIMACION [verificar], no la cuota definitiva. Los importes, reducciones y bonificaciones dependen de la CCAA {{comunidad_autonoma}} y del ejercicio.
> 3. Version de la Ley 29/1987 verificada: {{fecha_verificacion_isd}}.
> 4. Plazo: 6 meses desde el fallecimiento, prorrogable por otros 6 (solicitud dentro de los 5 primeros meses).
> 5. Organismo: Hacienda autonomica de {{comunidad_autonoma}}. Modelo 650 o el autonomico equivalente [verificar].
> 6. Si hay inmuebles urbanos, liquidar ademas la plusvalia municipal (IIVTNU) en el ayuntamiento correspondiente.
