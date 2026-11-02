# Catálogo de artefactos típicos

Recetas de partida para los artefactos que más se piden: tipo de entregable (V1), bloques, gráficos que funcionan y datos que pedir. La receta se deduce de la petición (V6 en `SKILL.md`); se adapta al caso y se aplican todas las reglas de la skill. Si falta un dato para un bloque y el usuario no lo tiene, el bloque se quita. Las propuestas de honorarios, los boletines y cualquier otro documento de texto no tienen receta aquí: se redactan en Markdown con su skill.

---

## Cliente

### Informe de situación del expediente (`situacion_expediente`)

- **V1:** `informe_visual`; en versión corta (solo plazos, hitos y próximos pasos), `cronograma_expediente`. Para enviar al cliente o dejar en su espacio.
- **Pregunta que responde:** dónde estamos, que nos pedían o pedimos, que viene ahora y cuando.
- **Bloques:** indicadores (cuantía inicial, cuantía actual, diferencia, próximo vencimiento) → antecedentes en cuatro líneas → comparativa de importes (columnas agrupadas o cascada con `@clave`) → plazos (diagrama de plazos con fases abiertas y fechas aproximadas) y cronología → quién es quién (diagrama en árbol o radial, si hay varias partes o sociedades) → próximos pasos con responsable → aviso de riesgo si corre un plazo.
- **Datos que pedir:** partes y su relación, cifras iniciales y actuales con su fecha, hitos con fecha cierta, plazo en curso, responsable.
- **Versión larga (dossier de caso, para preparar una reunión o una vista):** añade prueba disponible (tabla con distintivos), riesgos (matriz) y estrategia.

### Viabilidad o comparativa de opciones (`viabilidad`)

- **V1:** `comparativa`; `informe_visual` si hay que explicar mucho contexto, o `presentacion` si se decide en una reunión.
- **Bloques:** la recomendación en el titular → criterios de decisión → vías u opciones en tabla comparativa con distintivos (en diapositivas, `comparativa`) → coste y plazo de cada una (columnas agrupadas o bala) → riesgos (matriz) → recomendación y hoja de ruta (diagrama de flujo con la decisión).
- **Datos que pedir:** objetivo del cliente, opciones y criterios, cuantía, coste y plazo de cada vía, plazos de prescripción o caducidad conocidos.

---

## Despacho

### Informe mensual de actividad y KPIs (`kpis_mensual`)

- **V1:** `cuadro_mando`. Para la reunión de socios o de área.
- **Bloques:** indicadores con variación frente al mes anterior (`signo`) y minigráfico → facturación frente a objetivo (línea con umbral o bala) → por área (barras o anillo) → saldo por área (divergentes) → horas frente a objetivo (bala) → asuntos abiertos y cerrados → tabla de detalle con totales en `cifras`.
- **Datos que pedir:** serie mensual de facturación y cobro, objetivo, horas por área y objetivo, asuntos abiertos al inicio y al final, saldo por área.

### Memoria anual (`memoria_anual`)

- **V1:** `documento_largo`.
- **Bloques:** portada → carta de presentación → el año en cifras (indicadores) → evolución (línea de varios años) → por área (barras y anillo) → asuntos destacados → equipo → objetivos del año siguiente.
- **Datos que pedir:** cifras del año y de los anteriores, asuntos destacados que se pueden citar, equipo, objetivos.

### Facturación y cobros (`facturacion_cobros`)

- **V1:** `cuadro_mando` o `panel_datos` si el detalle pesa más que los KPIs.
- **Bloques:** facturado, cobrado y pendiente (indicadores con `operacion`) → evolución de lo pendiente (línea con umbral en `riesgo`) → antigüedad de la deuda (anillo) → mayores deudores (barras) → circuito de recobro (diagrama) → acciones.
- **Datos que pedir:** facturación y cobro por periodo, saldo vencido por antigüedad, mayores deudores con fecha de corte.

---

## Análisis

### Due diligence (`due_diligence`)

- **V1:** `documento_largo`.
- **Bloques:** resumen ejecutivo con las incidencias rojas → alcance y documentación revisada → estructura societaria (diagrama en árbol) → incidencias por área (tabla con distintivos) → contingencias cuantificadas (barras o cascada) → matriz de riesgos → recomendaciones y condiciones para la operación.
- **Datos que pedir:** perímetro, documentación recibida y fecha, incidencias detectadas por el equipo con su valoración. Nunca se presume una incidencia que no consta.

### Riesgos y cumplimiento (`riesgos_cumplimiento`)

- **V1:** `lista_control` para el grado de cumplimiento, `mapa_riesgos` para las contingencias.
- **Bloques:** mapa de riesgos (matriz) → grado de cumplimiento por obligación (bala o tabla con distintivos) → plazos regulatorios (diagrama de plazos) → responsables (carriles) → plan de acción.
- **Datos que pedir:** obligaciones aplicables y su estado, riesgos con probabilidad e impacto valorados por el usuario, plazos y responsables.

### Informe de mercado o sector (`mercado_sector`)

- **V1:** `informe_visual` o `documento_largo`.
- **Bloques:** conclusión → tamaño y evolución (línea con anotaciones de cambios normativos) → reparto (tarta o barras) → comparativa territorial (mapa por comunidades o provincias, y barras para el detalle) → tendencias → implicaciones para el cliente.
- **Datos que pedir o buscar:** solo fuentes oficiales o públicas citadas con URL y fecha; si el fetch no puede leer un PDF o una hoja de cálculo de la fuente, se dice y no se rellena de memoria.

---

## Comunicación

### White paper (`white_paper`)

- **V1:** `documento_largo`.
- **Bloques:** portada → resumen ejecutivo (tres conclusiones) → contexto y problema → análisis por capítulos, con un gráfico o diagrama que sostenga cada tesis → que deberían hacer las empresas → metodología y fuentes → sobre el despacho.
- **Datos que pedir:** tema, tesis, público, datos propios o fuentes que se autorizan; normativa solo verificada en la sesión.

### Caso de éxito (`caso_exito`)

- **V1:** `infografia`; `ficha_una_pagina` si es para el cliente y no para divulgar.
- **Bloques:** el reto → lo que hicimos (diagrama de flujo o cronología) → el resultado en una cifra grande → cita del cliente (solo si la autoriza) → equipo.
- **Datos que pedir:** autorización del cliente para citarlo o anonimización, resultado cuantificado, cita literal.

---

## Gestión y análisis con maqueta propia

### Captación y conversión (`captacion_conversion`)

- **V1:** `embudo_conversion`.
- **Bloques:** indicadores (entradas, conversión con `signo`, cerrados, mayor pérdida) → embudo por etapas → evolución por antigüedad (área apilada) → por dónde pasa cada asunto (sankey).
- **Datos que pedir:** número de asuntos en cada etapa del periodo y del anterior, y los flujos entre etapas si se conocen.

### Carga del equipo (`carga_equipo`)

- **V1:** `actividad_equipo`.
- **Bloques:** indicadores (horas, asuntos nuevos, mediana de resolución, área sobrecargada) → asuntos por área y mes (mapa de calor) → días de más carga (calendario) → tiempos por juzgado o área (cajas) → horas frente a objetivo (bala).
- **Datos que pedir:** asuntos nuevos por área y mes, horas por área y su objetivo, días de resolución en bruto si se quieren las cajas. Datos agregados por área salvo que el usuario pida por persona.

### Sensibilidad de una reclamación (`sensibilidad_reclamacion`)

- **V1:** `escenarios`.
- **Bloques:** indicadores (central, mínimo, máximo) → tabla de supuestos → resultado por escenario (columnas) → que supuesto pesa más (tornado) → la oferta y lo que se reclama dentro de la horquilla (rango).
- **Datos que pedir:** los supuestos que se barajan con su valor bajo, central y alto, y el resultado de cada escenario calculado por el usuario o por la herramienta interactiva.

