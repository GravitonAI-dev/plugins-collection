# HOJA DE LIQUIDACIÓN DETALLADA — {{nombre_trabajador: nombre y apellidos}}

> **DRAFT — para revisión por un abogado o graduado social colegiado. Documento de trabajo interno que acompaña al recibo de finiquito. No constituye asesoramiento jurídico definitivo.**  
> Convenio colectivo aplicable: {{denominacion_convenio: denominación y ámbito del convenio colectivo}} (código {{codigo_convenio: código de convenio}})

---

## 1. Datos de partida

| Dato | Valor | Origen |
|---|---|---|
| Persona trabajadora | {{nombre_trabajador: nombre y apellidos}} | — |
| DNI/NIE | {{dni_trabajador: DNI/NIE}} | — |
| Fecha de antigüedad | {{fecha_antiguedad: fecha (DD/MM/AAAA)}} | Contrato de {{fecha_contrato: fecha (DD/MM/AAAA)}} |
| Fecha de extinción | {{fecha_extincion: fecha (DD/MM/AAAA)}} | {{causa_extincion: origen}} |
| Tiempo total de servicio | {{tiempo_servicio: tiempo total de servicio}} | Cálculo |
| Categoría o grupo profesional | {{categoria_profesional: categoría o grupo profesional}} | Convenio |
| Salario base mensual | {{salario_base_mensual: importe en euros}} € | Nómina y tabla de convenio |
| Complementos mensuales | {{complementos_mensuales: complementos mensuales}} € | {{origen_complementos: origen}} |
| Número de pagas extraordinarias | {{numero_pagas: número de pagas extraordinarias}} | Convenio, artículo {{articulo_convenio_pagas: origen}} |
| Periodo de devengo de las pagas | {{periodo_devengo_pagas: periodo de devengo de las pagas}} | Convenio, artículo {{articulo_convenio_pagas: origen}} |
| ¿Pagas prorrateadas en nómina? | {{pagas_prorrateadas: sí / no}} | Nómina |
| Días de vacaciones anuales | {{dias_vacaciones_anuales: número de días}} | Convenio, artículo {{articulo_convenio_vacaciones: origen}} |
| Salario bruto anual con prorrateos | {{salario_bruto_anual: importe en euros}} € | Cálculo |
| Salario diario regulador | {{salario_dia_regulador: importe en euros}} € | {{salario_bruto_anual: importe en euros}} / 365 |

---

## 2. Salario del mes de la extinción

**Fórmula aplicada:** {{formula_salario_mes: detalle del cálculo}}

**Desarrollo:** {{desarrollo_salario_mes: detalle del cálculo}}

**Importe: {{importe_salario_mes: importe en euros}} euros**

---

## 3. Pagas extraordinarias

### 3.1 Paga extraordinaria de {{denominacion_paga_1: denominación de la paga extraordinaria}}

| Elemento | Valor |
|---|---|
| Periodo de devengo | {{periodo_devengo_paga_1: periodo de devengo}} |
| Días devengados | {{dias_devengados_paga_1: número de días}} |
| Importe íntegro de la paga | {{importe_integro_paga_1: importe en euros}} € |
| Fórmula | {{formula_paga_1: detalle del cálculo}} |
| **Importe proporcional** | **{{importe_paga_1: importe en euros}} €** |

### 3.2 Paga extraordinaria de {{denominacion_paga_2: denominación de la paga extraordinaria}}

| Elemento | Valor |
|---|---|
| Periodo de devengo | {{periodo_devengo_paga_2: periodo de devengo}} |
| Días devengados | {{dias_devengados_paga_2: número de días}} |
| Importe íntegro de la paga | {{importe_integro_paga_2: importe en euros}} € |
| Fórmula | {{formula_paga_2: detalle del cálculo}} |
| **Importe proporcional** | **{{importe_paga_2: importe en euros}} €** |

{{parrafo_pagas_prorrateadas_no_procede: bloque condicional que inserta la skill}}

---

## 4. Vacaciones devengadas y no disfrutadas

| Elemento | Valor |
|---|---|
| Días de vacaciones que corresponden al año completo | {{dias_vacaciones_anuales: número de días}} |
| Periodo de devengo | {{periodo_devengo_vacaciones: periodo de devengo}} |
| Días trabajados en el periodo de devengo | {{dias_trabajados_devengo_vacaciones: número de días}} |
| Días devengados | {{dias_devengados_vacaciones: número de días}} |
| Días ya disfrutados | {{dias_disfrutados_vacaciones: número de días}} |
| **Días pendientes** | **{{dias_vacaciones_pendientes: número de días}}** |
| Fórmula | {{formula_vacaciones: detalle del cálculo}} |
| **Importe** | **{{importe_vacaciones: importe en euros}} €** |

**Efecto sobre la Seguridad Social:** las vacaciones devengadas y no disfrutadas se abonan y se cotizan, prolongando la situación de alta durante {{dias_vacaciones_pendientes: número de días}} días. Fecha de baja resultante a efectos de Seguridad Social: {{fecha_baja_seguridad_social: fecha (DD/MM/AAAA)}}.

---

## 5. Otros conceptos devengados

| Concepto | Detalle y fórmula | Importe |
|---|---|---|
| Horas extraordinarias pendientes | {{detalle_horas_extra: detalle del cálculo}} | {{importe_horas_extra: importe en euros}} € |
| Comisiones e incentivos devengados | {{detalle_comisiones: detalle del cálculo}} | {{importe_comisiones: importe en euros}} € |
| Dietas y gastos pendientes de reembolso | {{detalle_dietas: detalle del cálculo}} | {{importe_dietas: importe en euros}} € |
| {{otro_concepto_devengado: concepto devengado}} | {{detalle_otro_concepto: detalle del cálculo}} | {{importe_otro_concepto: importe en euros}} € |

---

## 6. Indemnización por la extinción

{{bloque_indemnizacion_detallada: bloque condicional que inserta la skill}}

---

## 7. Deducciones

| Concepto | Justificación documental | Importe |
|---|---|---|
| Cotización a la Seguridad Social a cargo de la persona trabajadora | {{justificacion_cotizacion: texto breve}} | {{importe_cotizacion_trabajador: importe en euros}} € |
| Retención a cuenta del IRPF ({{tipo_retencion: porcentaje}} %) | {{justificacion_retencion: texto breve}} | {{importe_retencion_irpf: importe en euros}} € |
| Anticipos concedidos | {{justificacion_anticipos: texto breve}} | {{importe_anticipos: importe en euros}} € |
| Días de preaviso incumplido | {{justificacion_preaviso: texto breve}} | {{importe_preaviso: importe en euros}} € |
| {{otra_deduccion: concepto de la deducción}} | {{justificacion_otra_deduccion: texto breve}} | {{importe_otra_deduccion: importe en euros}} € |

---

## 8. Resumen

| Concepto | Importe |
|---|---|
| Total devengos salariales | {{total_devengos_salariales: importe en euros}} € |
| Indemnización | {{importe_indemnizacion: importe en euros}} € |
| **Total bruto** | **{{total_bruto: importe en euros}} €** |
| Total deducciones | {{total_deducciones: importe en euros}} € |
| **Líquido a percibir** | **{{liquido_percibir: importe en euros}} €** |

**Tratamiento fiscal:** la indemnización por despido está exenta de tributación en el Impuesto sobre la Renta de las Personas Físicas hasta el límite de la cuantía obligatoria legalmente establecida, con el tope máximo vigente. El exceso pactado tributa como rendimiento del trabajo con reducción, en su caso, por irregularidad. Verificar los límites vigentes antes de aplicar la retención.

---

## 9. Comprobaciones realizadas

- Convenio colectivo identificado y verificado: {{denominacion_convenio: denominación y ámbito del convenio colectivo}}.
- Periodo de devengo de pagas extraordinarias comprobado en el convenio: {{periodo_devengo_pagas: periodo de devengo de las pagas según convenio}}.
- Comprobación de si las pagas se abonan prorrateadas: {{pagas_prorrateadas: sí / no}}.
- Comprobación de nóminas de los {{meses_nominas_revisadas: número de meses de nóminas revisadas}} meses anteriores para determinar el salario regulador.
- Comprobación de vacaciones disfrutadas en el calendario laboral.
- Respaldo documental de cada deducción practicada.

---

> **Advertencias:**  
> 1. Este documento es un DRAFT y de uso interno. Debe ser revisado por un abogado o graduado social colegiado.  
> 2. Los importes son estimados a partir de los datos aportados: el importe definitivo depende de las bases realmente cotizadas y del salario acreditado en nómina.  
> 3. El periodo de devengo de las pagas extraordinarias es materia del convenio colectivo y cambia el resultado por completo. No se presume.  
> 4. Esta hoja acompaña al recibo de finiquito y lo sostiene: en una reclamación posterior es el documento que acredita cómo se calculó cada concepto.
