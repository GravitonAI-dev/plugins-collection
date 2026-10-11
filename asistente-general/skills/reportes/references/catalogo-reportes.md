# Catalogo de reportes tipicos

Recetas de partida para los reportes que mas se piden: tipo de entregable (V1), bloques, graficos que funcionan y datos que pedir. La receta se deduce de la peticion (V6 en `SKILL.md`); se adapta al caso y se aplican todas las reglas de la skill. Si falta un dato para un bloque y el usuario no lo tiene, el bloque se quita.

---

## Cliente

### Informe de situacion del expediente (`situacion_expediente`)

- **V1:** `informe_visual`. Para enviar al cliente o dejar en su espacio.
- **Pregunta que responde:** donde estamos, que nos pedian o pedimos, que viene ahora y cuando.
- **Bloques:** indicadores (cuantia inicial, cuantia actual, diferencia, proximo vencimiento) → antecedentes en cuatro lineas → comparativa de importes (columnas agrupadas o cascada con `@clave`) → plazos (diagrama de plazos con fases abiertas y fechas aproximadas) y cronologia → quien es quien (diagrama en arbol o radial, si hay varias partes o sociedades) → proximos pasos con responsable → aviso de riesgo si corre un plazo.
- **Datos que pedir:** partes y su relacion, cifras iniciales y actuales con su fecha, hitos con fecha cierta, plazo en curso, responsable.
- **Version larga (dossier de caso, para preparar una reunion o una vista):** anade prueba disponible (tabla con distintivos), riesgos (matriz) y estrategia.

### Propuesta de honorarios (`propuesta_honorarios`)

- **V1:** `informe_visual` o `presentacion` si se presenta en reunion.
- **Bloques:** que necesita el cliente (en sus palabras) → como lo resolvemos (diagrama por carriles: cliente, despacho, juzgado u organismo) → fases y calendario (plazos con fechas aproximadas) → honorarios por fase (tabla con totales en `cifras`) → que incluye y que no → equipo → condiciones y validez.
- **Datos que pedir:** alcance, fases, importe o criterio de cada fase, provisiones de fondos, equipo, validez de la oferta.
- **Como pitch en reunion (`presentacion`):** portada, que nos han contado, lo que esta en juego (`cifra`), como lo resolvemos (`grafico` con diagrama), por que nosotros, equipo, honorarios (`tabla`), proximos pasos y cierre.

### Viabilidad o comparativa de opciones (`viabilidad`)

- **V1:** `informe_visual`, o `presentacion` si se decide en una reunion.
- **Bloques:** la recomendacion en el titular → criterios de decision → vias u opciones en tabla comparativa con distintivos (en diapositivas, `comparativa`) → coste y plazo de cada una (columnas agrupadas o bala) → riesgos (matriz) → recomendacion y hoja de ruta (diagrama de flujo con la decision).
- **Datos que pedir:** objetivo del cliente, opciones y criterios, cuantia, coste y plazo de cada via, plazos de prescripcion o caducidad conocidos.

---

## Despacho

### Informe mensual de actividad y KPIs (`kpis_mensual`)

- **V1:** `panel_datos`. Para la reunion de socios o de area.
- **Bloques:** indicadores con variacion frente al mes anterior (`signo`) y minigrafico → facturacion frente a objetivo (linea con umbral o bala) → por area (barras o anillo) → saldo por area (divergentes) → horas frente a objetivo (bala) → asuntos abiertos y cerrados → tabla de detalle con totales en `cifras`.
- **Datos que pedir:** serie mensual de facturacion y cobro, objetivo, horas por area y objetivo, asuntos abiertos al inicio y al final, saldo por area.

### Memoria anual (`memoria_anual`)

- **V1:** `documento_largo`.
- **Bloques:** portada → carta de presentacion → el ano en cifras (indicadores) → evolucion (linea de varios anos) → por area (barras y anillo) → asuntos destacados → equipo → objetivos del ano siguiente.
- **Datos que pedir:** cifras del ano y de los anteriores, asuntos destacados que se pueden citar, equipo, objetivos.

### Facturacion y cobros (`facturacion_cobros`)

- **V1:** `panel_datos`.
- **Bloques:** facturado, cobrado y pendiente (indicadores con `operacion`) → evolucion de lo pendiente (linea con umbral en `riesgo`) → antiguedad de la deuda (anillo) → mayores deudores (barras) → circuito de recobro (diagrama) → acciones.
- **Datos que pedir:** facturacion y cobro por periodo, saldo vencido por antiguedad, mayores deudores con fecha de corte.

---

## Analisis

### Due diligence (`due_diligence`)

- **V1:** `documento_largo`.
- **Bloques:** resumen ejecutivo con las incidencias rojas → alcance y documentacion revisada → estructura societaria (diagrama en arbol) → incidencias por area (tabla con distintivos) → contingencias cuantificadas (barras o cascada) → matriz de riesgos → recomendaciones y condiciones para la operacion.
- **Datos que pedir:** perimetro, documentacion recibida y fecha, incidencias detectadas por el equipo con su valoracion. Nunca se presume una incidencia que no consta.

### Riesgos y cumplimiento (`riesgos_cumplimiento`)

- **V1:** `informe_visual`.
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

### Boletin normativo (`boletin_normativo`)

- **V1:** `informe_visual`.
- **Bloques:** lo mas importante del periodo (tres avisos) → novedades por materia (secciones) → plazos de entrada en vigor (diagrama de plazos) → a quien afecta (tabla) → que hacer.
- **Datos que pedir o buscar:** normas del periodo verificadas en el BOE o el diario oficial, con enlace a la version consolidada.

### Caso de exito (`caso_exito`)

- **V1:** `resumen_ejecutivo`, o `informe_visual` si hace falta mas de una pagina.
- **Bloques:** el reto → lo que hicimos (diagrama de flujo o cronologia) → el resultado en una cifra grande → cita del cliente (solo si la autoriza) → equipo.
- **Datos que pedir:** autorizacion del cliente para citarlo o anonimizacion, resultado cuantificado, cita literal.

