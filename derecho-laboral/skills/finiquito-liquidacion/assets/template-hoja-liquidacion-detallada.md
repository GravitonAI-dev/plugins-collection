# HOJA DE LIQUIDACIÓN DETALLADA — {{NOMBRE_TRABAJADOR: nombre y apellidos}}

> **DRAFT — para revisión por un abogado o graduado social colegiado. Documento de trabajo interno que acompaña al recibo de finiquito. No constituye asesoramiento jurídico definitivo.**  
> Convenio colectivo aplicable: {{DENOMINACION_CONVENIO: denominación y ámbito del convenio colectivo}} (código {{CODIGO_CONVENIO: código de convenio}})

---

## 1. Datos de partida

| Dato | Valor | Origen |
|---|---|---|
| Persona trabajadora | {{NOMBRE_TRABAJADOR: nombre y apellidos}} | — |
| DNI/NIE | {{DNI_TRABAJADOR: DNI/NIE}} | — |
| Fecha de antigüedad | {{FECHA_ANTIGUEDAD: fecha (DD/MM/AAAA)}} | Contrato de {{FECHA_CONTRATO: fecha (DD/MM/AAAA)}} |
| Fecha de extinción | {{FECHA_EXTINCION: fecha (DD/MM/AAAA)}} | {{CAUSA_EXTINCION: origen}} |
| Tiempo total de servicio | {{TIEMPO_SERVICIO: tiempo total de servicio}} | Cálculo |
| Categoría o grupo profesional | {{CATEGORIA_PROFESIONAL: categoría o grupo profesional}} | Convenio |
| Salario base mensual | {{SALARIO_BASE_MENSUAL: importe en euros}} € | Nómina y tabla de convenio |
| Complementos mensuales | {{COMPLEMENTOS_MENSUALES: importe en euros}} € | {{ORIGEN_COMPLEMENTOS: origen}} |
| Número de pagas extraordinarias | {{NUMERO_PAGAS: número de pagas extraordinarias}} | Convenio, artículo {{ARTICULO_CONVENIO_PAGAS: origen}} |
| Periodo de devengo de las pagas | {{PERIODO_DEVENGO_PAGAS: periodo de devengo de las pagas}} | Convenio, artículo {{ARTICULO_CONVENIO_PAGAS: origen}} |
| ¿Pagas prorrateadas en nómina? | {{PAGAS_PRORRATEADAS: sí / no}} | Nómina |
| Días de vacaciones anuales | {{DIAS_VACACIONES_ANUALES: número de días}} | Convenio, artículo {{ARTICULO_CONVENIO_VACACIONES: origen}} |
| Salario bruto anual con prorrateos | {{SALARIO_BRUTO_ANUAL: importe en euros}} € | Cálculo |
| Salario diario regulador | {{SALARIO_DIA_REGULADOR: importe en euros}} € | {{SALARIO_BRUTO_ANUAL: importe en euros}} / 365 |

---

## 2. Salario del mes de la extinción

**Fórmula aplicada:** {{FORMULA_SALARIO_MES: detalle del cálculo}}

**Desarrollo:** {{DESARROLLO_SALARIO_MES: detalle del cálculo}}

**Importe: {{IMPORTE_SALARIO_MES: importe en euros}} euros**

---

## 3. Pagas extraordinarias

### 3.1 Paga extraordinaria de {{DENOMINACION_PAGA_1: denominación de la paga extraordinaria}}

| Elemento | Valor |
|---|---|
| Periodo de devengo | {{PERIODO_DEVENGO_PAGA_1: periodo de devengo}} |
| Días devengados | {{DIAS_DEVENGADOS_PAGA_1: número de días}} |
| Importe íntegro de la paga | {{IMPORTE_INTEGRO_PAGA_1: importe en euros}} € |
| Fórmula | {{FORMULA_PAGA_1: detalle del cálculo}} |
| **Importe proporcional** | **{{IMPORTE_PAGA_1: importe en euros}} €** |

### 3.2 Paga extraordinaria de {{DENOMINACION_PAGA_2: denominación de la paga extraordinaria}}

| Elemento | Valor |
|---|---|
| Periodo de devengo | {{PERIODO_DEVENGO_PAGA_2: periodo de devengo}} |
| Días devengados | {{DIAS_DEVENGADOS_PAGA_2: número de días}} |
| Importe íntegro de la paga | {{IMPORTE_INTEGRO_PAGA_2: importe en euros}} € |
| Fórmula | {{FORMULA_PAGA_2: detalle del cálculo}} |
| **Importe proporcional** | **{{IMPORTE_PAGA_2: importe en euros}} €** |

{{PARRAFO_PAGAS_PRORRATEADAS_NO_PROCEDE: bloque condicional que inserta la skill}}

---

## 4. Vacaciones devengadas y no disfrutadas

| Elemento | Valor |
|---|---|
| Días de vacaciones que corresponden al año completo | {{DIAS_VACACIONES_ANUALES: número de días}} |
| Periodo de devengo | {{PERIODO_DEVENGO_VACACIONES: periodo de devengo}} |
| Días trabajados en el periodo de devengo | {{DIAS_TRABAJADOS_DEVENGO_VACACIONES: número de días}} |
| Días devengados | {{DIAS_DEVENGADOS_VACACIONES: número de días}} |
| Días ya disfrutados | {{DIAS_DISFRUTADOS_VACACIONES: número de días}} |
| **Días pendientes** | **{{DIAS_VACACIONES_PENDIENTES: número de días}}** |
| Fórmula | {{FORMULA_VACACIONES: detalle del cálculo}} |
| **Importe** | **{{IMPORTE_VACACIONES: importe en euros}} €** |

**Efecto sobre la Seguridad Social:** las vacaciones devengadas y no disfrutadas se abonan y se cotizan, prolongando la situación de alta durante {{DIAS_VACACIONES_PENDIENTES: número de días}} días. Fecha de baja resultante a efectos de Seguridad Social: {{FECHA_BAJA_SEGURIDAD_SOCIAL: fecha (DD/MM/AAAA)}}.

---

## 5. Otros conceptos devengados

| Concepto | Detalle y fórmula | Importe |
|---|---|---|
| Horas extraordinarias pendientes | {{DETALLE_HORAS_EXTRA: detalle del cálculo}} | {{IMPORTE_HORAS_EXTRA: importe en euros}} € |
| Comisiones e incentivos devengados | {{DETALLE_COMISIONES: detalle del cálculo}} | {{IMPORTE_COMISIONES: importe en euros}} € |
| Dietas y gastos pendientes de reembolso | {{DETALLE_DIETAS: detalle del cálculo}} | {{IMPORTE_DIETAS: importe en euros}} € |
| {{OTRO_CONCEPTO_DEVENGADO: concepto devengado}} | {{DETALLE_OTRO_CONCEPTO: detalle del cálculo}} | {{IMPORTE_OTRO_CONCEPTO: importe en euros}} € |

---

## 6. Indemnización por la extinción

{{BLOQUE_INDEMNIZACION_DETALLADA: bloque condicional que inserta la skill}}

---

## 7. Deducciones

| Concepto | Justificación documental | Importe |
|---|---|---|
| Cotización a la Seguridad Social a cargo de la persona trabajadora | {{JUSTIFICACION_COTIZACION: texto breve}} | {{IMPORTE_COTIZACION_TRABAJADOR: importe en euros}} € |
| Retención a cuenta del IRPF ({{TIPO_RETENCION: porcentaje}} %) | {{JUSTIFICACION_RETENCION: texto breve}} | {{IMPORTE_RETENCION_IRPF: importe en euros}} € |
| Anticipos concedidos | {{JUSTIFICACION_ANTICIPOS: texto breve}} | {{IMPORTE_ANTICIPOS: importe en euros}} € |
| Días de preaviso incumplido | {{JUSTIFICACION_PREAVISO: texto breve}} | {{IMPORTE_PREAVISO: importe en euros}} € |
| {{OTRA_DEDUCCION: concepto de la deducción}} | {{JUSTIFICACION_OTRA_DEDUCCION: texto breve}} | {{IMPORTE_OTRA_DEDUCCION: importe en euros}} € |

---

## 8. Resumen

| Concepto | Importe |
|---|---|
| Total devengos salariales | {{TOTAL_DEVENGOS_SALARIALES: importe en euros — calculado, suma de los devengos salariales}} € |
| Indemnización | {{IMPORTE_INDEMNIZACION: importe en euros}} € |
| **Total bruto** | **{{TOTAL_BRUTO: importe en euros — calculado, devengos más indemnización}} €** |
| Total deducciones | {{TOTAL_DEDUCCIONES: importe en euros — calculado, suma de las deducciones}} € |
| **Líquido a percibir** | **{{LIQUIDO_PERCIBIR: importe en euros — calculado, devengos menos deducciones}} €** |

**Tratamiento fiscal:** la indemnización por despido está exenta de tributación en el Impuesto sobre la Renta de las Personas Físicas hasta el límite de la cuantía obligatoria legalmente establecida, con el tope máximo vigente. El exceso pactado tributa como rendimiento del trabajo con reducción, en su caso, por irregularidad. Verificar los límites vigentes antes de aplicar la retención.

---

## 9. Comprobaciones realizadas

- Convenio colectivo identificado y verificado: {{DENOMINACION_CONVENIO: denominación y ámbito del convenio colectivo}}.
- Periodo de devengo de pagas extraordinarias comprobado en el convenio: {{PERIODO_DEVENGO_PAGAS: periodo de devengo de las pagas según convenio}}.
- Comprobación de si las pagas se abonan prorrateadas: {{PAGAS_PRORRATEADAS: sí / no}}.
- Comprobación de nóminas de los {{MESES_NOMINAS_REVISADAS: número de meses de nóminas revisadas}} meses anteriores para determinar el salario regulador.
- Comprobación de vacaciones disfrutadas en el calendario laboral.
- Respaldo documental de cada deducción practicada.

---

> **Advertencias:**  
> 1. Este documento es un DRAFT y de uso interno. Debe ser revisado por un abogado o graduado social colegiado.  
> 2. Los importes son estimados a partir de los datos aportados: el importe definitivo depende de las bases realmente cotizadas y del salario acreditado en nómina.  
> 3. El periodo de devengo de las pagas extraordinarias es materia del convenio colectivo y cambia el resultado por completo. No se presume.  
> 4. Esta hoja acompaña al recibo de finiquito y lo sostiene: en una reclamación posterior es el documento que acredita cómo se calculó cada concepto.
