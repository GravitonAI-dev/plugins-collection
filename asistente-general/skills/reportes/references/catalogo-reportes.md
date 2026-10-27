# Catalogo de artefactos tipicos

Recetas de partida para los artefactos que mas se piden: tipo de entregable (V1), bloques, graficos que funcionan y datos que pedir. La receta se deduce de la peticion (V6 en `SKILL.md`); se adapta al caso y se aplican todas las reglas de la skill. Si falta un dato para un bloque y el usuario no lo tiene, el bloque se quita. Las propuestas de honorarios, los boletines y cualquier otro documento de texto no tienen receta aqui: se redactan en Markdown con su skill.

---

## Cliente

### Informe de situacion del expediente (`situacion_expediente`)

- **V1:** `informe_visual`; en version corta (solo plazos, hitos y proximos pasos), `cronograma_expediente`. Para enviar al cliente o dejar en su espacio.
- **Pregunta que responde:** donde estamos, que nos pedian o pedimos, que viene ahora y cuando.
- **Bloques:** indicadores (cuantia inicial, cuantia actual, diferencia, proximo vencimiento) → antecedentes en cuatro lineas → comparativa de importes (columnas agrupadas o cascada con `@clave`) → plazos (diagrama de plazos con fases abiertas y fechas aproximadas) y cronologia → quien es quien (diagrama en arbol o radial, si hay varias partes o sociedades) → proximos pasos con responsable → aviso de riesgo si corre un plazo.
- **Datos que pedir:** partes y su relacion, cifras iniciales y actuales con su fecha, hitos con fecha cierta, plazo en curso, responsable.
- **Version larga (dossier de caso, para preparar una reunion o una vista):** anade prueba disponible (tabla con distintivos), riesgos (matriz) y estrategia.

### Viabilidad o comparativa de opciones (`viabilidad`)

- **V1:** `comparativa`; `informe_visual` si hay que explicar mucho contexto, o `presentacion` si se decide en una reunion.
- **Bloques:** la recomendacion en el titular → criterios de decision → vias u opciones en tabla comparativa con distintivos (en diapositivas, `comparativa`) → coste y plazo de cada una (columnas agrupadas o bala) → riesgos (matriz) → recomendacion y hoja de ruta (diagrama de flujo con la decision).
- **Datos que pedir:** objetivo del cliente, opciones y criterios, cuantia, coste y plazo de cada via, plazos de prescripcion o caducidad conocidos.

---

## Despacho

### Informe mensual de actividad y KPIs (`kpis_mensual`)

- **V1:** `cuadro_mando`. Para la reunion de socios o de area.
- **Bloques:** indicadores con variacion frente al mes anterior (`signo`) y minigrafico → facturacion frente a objetivo (linea con umbral o bala) → por area (barras o anillo) → saldo por area (divergentes) → horas frente a objetivo (bala) → asuntos abiertos y cerrados → tabla de detalle con totales en `cifras`.
- **Datos que pedir:** serie mensual de facturacion y cobro, objetivo, horas por area y objetivo, asuntos abiertos al inicio y al final, saldo por area.

### Memoria anual (`memoria_anual`)

- **V1:** `documento_largo`.
- **Bloques:** portada → carta de presentacion → el ano en cifras (indicadores) → evolucion (linea de varios anos) → por area (barras y anillo) → asuntos destacados → equipo → objetivos del ano siguiente.
- **Datos que pedir:** cifras del ano y de los anteriores, asuntos destacados que se pueden citar, equipo, objetivos.

### Facturacion y cobros (`facturacion_cobros`)

- **V1:** `cuadro_mando` o `panel_datos` si el detalle pesa mas que los KPIs.
- **Bloques:** facturado, cobrado y pendiente (indicadores con `operacion`) → evolucion de lo pendiente (linea con umbral en `riesgo`) → antiguedad de la deuda (anillo) → mayores deudores (barras) → circuito de recobro (diagrama) → acciones.
- **Datos que pedir:** facturacion y cobro por periodo, saldo vencido por antiguedad, mayores deudores con fecha de corte.

---

## Analisis

### Due diligence (`due_diligence`)

- **V1:** `documento_largo`.
- **Bloques:** resumen ejecutivo con las incidencias rojas → alcance y documentacion revisada → estructura societaria (diagrama en arbol) → incidencias por area (tabla con distintivos) → contingencias cuantificadas (barras o cascada) → matriz de riesgos → recomendaciones y condiciones para la operacion.
- **Datos que pedir:** perimetro, documentacion recibida y fecha, incidencias detectadas por el equipo con su valoracion. Nunca se presume una incidencia que no consta.

### Riesgos y cumplimiento (`riesgos_cumplimiento`)

- **V1:** `lista_control` para el grado de cumplimiento, `mapa_riesgos` para las contingencias.
- **Bloques:** mapa de riesgos (matriz) → grado de cumplimiento por obligacion (bala o tabla con distintivos) → plazos regulatorios (diagrama de plazos) → responsables (carriles) → plan de accion.
- **Datos que pedir:** obligaciones aplicables y su estado, riesgos con probabilidad e impacto valorados por el usuario, plazos y responsables.

### Informe de mercado o sector (`mercado_sector`)

- **V1:** `informe_visual` o `documento_largo`.
- **Bloques:** conclusion → tamano y evolucion (linea con anotaciones de cambios normativos) → reparto (tarta o barras) → comparativa territorial (mapa por comunidades o provincias, y barras para el detalle) → tendencias → implicaciones para el cliente.
- **Datos que pedir o buscar:** solo fuentes oficiales o publicas citadas con URL y fecha; si el fetch no puede leer un PDF o una hoja de calculo de la fuente, se dice y no se rellena de memoria.

---

## Comunicacion

### White paper (`white_paper`)

- **V1:** `documento_largo`.
- **Bloques:** portada → resumen ejecutivo (tres conclusiones) → contexto y problema → analisis por capitulos, con un grafico o diagrama que sostenga cada tesis → que deberian hacer las empresas → metodologia y fuentes → sobre el despacho.
- **Datos que pedir:** tema, tesis, publico, datos propios o fuentes que se autorizan; normativa solo verificada en la sesion.

### Caso de exito (`caso_exito`)

- **V1:** `infografia`; `ficha_una_pagina` si es para el cliente y no para divulgar.
- **Bloques:** el reto → lo que hicimos (diagrama de flujo o cronologia) → el resultado en una cifra grande → cita del cliente (solo si la autoriza) → equipo.
- **Datos que pedir:** autorizacion del cliente para citarlo o anonimizacion, resultado cuantificado, cita literal.

---

## Gestion y analisis con maqueta propia

### Captacion y conversion (`captacion_conversion`)

- **V1:** `embudo_conversion`.
- **Bloques:** indicadores (entradas, conversion con `signo`, cerrados, mayor perdida) → embudo por etapas → evolucion por antiguedad (area apilada) → por donde pasa cada asunto (sankey).
- **Datos que pedir:** numero de asuntos en cada etapa del periodo y del anterior, y los flujos entre etapas si se conocen.

### Carga del equipo (`carga_equipo`)

- **V1:** `actividad_equipo`.
- **Bloques:** indicadores (horas, asuntos nuevos, mediana de resolucion, area sobrecargada) → asuntos por area y mes (mapa de calor) → dias de mas carga (calendario) → tiempos por juzgado o area (cajas) → horas frente a objetivo (bala).
- **Datos que pedir:** asuntos nuevos por area y mes, horas por area y su objetivo, dias de resolucion en bruto si se quieren las cajas. Datos agregados por area salvo que el usuario pida por persona.

### Sensibilidad de una reclamacion (`sensibilidad_reclamacion`)

- **V1:** `escenarios`.
- **Bloques:** indicadores (central, minimo, maximo) → tabla de supuestos → resultado por escenario (columnas) → que supuesto pesa mas (tornado) → la oferta y lo que se reclama dentro de la horquilla (rango).
- **Datos que pedir:** los supuestos que se barajan con su valor bajo, central y alto, y el resultado de cada escenario calculado por el usuario o por la herramienta interactiva.

