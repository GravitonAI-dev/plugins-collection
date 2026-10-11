# Catalogo de reportes tipicos

Recetas de los reportes que mas se piden. Cada receta fija el tipo de entregable (V1), la estructura de bloques, los graficos que funcionan y los datos que hay que pedir. Es un punto de partida: se adapta al caso, pero evita empezar de cero y olvidar lo que el lector espera encontrar.

Uso en el flujo: si la peticion encaja con una receta (por las palabras del usuario o por la escucha activa), se fija `receta_reporte` en silencio y la receta resuelve V1. Si el usuario solo dice «un informe» o «un reporte» y no encaja con ninguna, se ofrece la lista en el formulario de la Fase 1 con la opcion «Otro reporte», que sigue el flujo normal.

Todas las recetas comparten las reglas de la skill: titular que afirma, cifras derivadas declaradas en `cifras`, fuentes con fecha, aviso DRAFT y ningun dato inventado. Lo que falte para un bloque se pide en bloque con un formulario de datos; si el usuario no lo tiene, el bloque se quita en lugar de rellenarlo con supuestos.

---

## Cliente

### Informe de situacion del expediente (`situacion_expediente`)

- **V1:** `informe_visual`. Para enviar al cliente o dejar en su espacio.
- **Pregunta que responde:** donde estamos, que nos pedian o pedimos, que viene ahora y cuando.
- **Bloques:** indicadores (cuantia inicial, cuantia actual, diferencia, proximo vencimiento) → antecedentes en cuatro lineas → comparativa de importes (columnas agrupadas o cascada con `@clave`) → plazos (diagrama de plazos con fases abiertas y fechas aproximadas) y cronologia → quien es quien (diagrama en arbol o radial, si hay varias partes o sociedades) → proximos pasos con responsable → aviso de riesgo si corre un plazo.
- **Datos que pedir:** partes y su relacion, cifras iniciales y actuales con su fecha, hitos con fecha cierta, plazo en curso, responsable.

### Dossier de caso (`dossier_caso`)

- **V1:** `informe_visual`, mas largo. Para preparar una reunion o una vista.
- **Bloques:** resumen de una pagina → hechos (cronologia) → partes (diagrama radial) → pretensiones y cuantias (cascada) → prueba disponible (tabla con distintivos) → riesgos (matriz) → estrategia y siguientes pasos.
- **Datos que pedir:** hechos con fecha, documentos de prueba y su estado, cuantias, riesgos identificados por el letrado.

### Propuesta de honorarios (`propuesta_honorarios`)

- **V1:** `informe_visual` o `presentacion` si se presenta en reunion.
- **Bloques:** que necesita el cliente (en sus palabras) → como lo resolvemos (diagrama por carriles: cliente, despacho, juzgado u organismo) → fases y calendario (plazos con fechas aproximadas) → honorarios por fase (tabla con totales en `cifras`) → que incluye y que no → equipo → condiciones y validez.
- **Datos que pedir:** alcance, fases, importe o criterio de cada fase, provisiones de fondos, equipo, validez de la oferta.

### Informe de viabilidad (`viabilidad`)

- **V1:** `informe_visual`.
- **Bloques:** conclusion en el titular → vias posibles (tabla comparativa o diapositiva `comparativa`) → coste y plazo de cada via (bala o columnas) → riesgos (matriz) → recomendacion y hoja de ruta (diagrama de flujo con la decision).
- **Datos que pedir:** objetivo del cliente, cuantia, documentos, plazos de prescripcion o caducidad conocidos.

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

### Comparativa de opciones (`comparativa_opciones`)

- **V1:** `informe_visual` o `presentacion`.
- **Bloques:** la recomendacion en el titular → criterios de decision → tabla comparativa con distintivos → coste y plazo (columnas agrupadas o bala) → riesgos de cada opcion → recomendacion y condiciones.
- **Datos que pedir:** opciones, criterios y su peso, datos de cada opcion.

### Informe de mercado o sector (`mercado_sector`)

- **V1:** `informe_visual` o `documento_largo`.
- **Bloques:** conclusion → tamano y evolucion (linea con anotaciones de cambios normativos) → reparto (tarta o barras) → comparativa territorial (barras) → tendencias → implicaciones para el cliente.
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

- **V1:** `informe_visual` de una o dos paginas, o `resumen_ejecutivo`.
- **Bloques:** el reto → lo que hicimos (diagrama de flujo o cronologia) → el resultado en una cifra grande → cita del cliente (solo si la autoriza) → equipo.
- **Datos que pedir:** autorizacion del cliente para citarlo o anonimizacion, resultado cuantificado, cita literal.

### Pitch para cliente (`pitch_cliente`)

- **V1:** `presentacion`.
- **Diapositivas:** portada → que nos han contado (sus palabras) → lo que esta en juego (`cifra`) → como lo resolvemos (`grafico` con diagrama) → por que nosotros → equipo → propuesta y honorarios (`tabla`) → proximos pasos → cierre.
- **Datos que pedir:** necesidad del cliente, cifras del caso, equipo, honorarios y validez.

### Resumen ejecutivo de una pagina (`resumen_una_pagina`)

- **V1:** `resumen_ejecutivo`. Para el consejo, un socio o un cliente con poco tiempo.
- **Bloques:** titular con la conclusion → tres indicadores → un grafico que la sostiene → tres conclusiones y la decision que se pide.
- **Datos que pedir:** la decision que se busca y las tres cifras que la justifican.
