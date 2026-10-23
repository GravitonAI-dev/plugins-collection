# Ejemplos de la skill `reportes`

Artefactos de demostracion generados con la base `../assets/template-base-reportes.md` y las maquetas de `../references/maquetas-reportes.md`. Se abren **con doble clic** en cualquier navegador: no necesitan servidor, ni conexion, ni instalar nada. El boton inferior de cada pagina la imprime o la guarda como PDF; al lado de cada `.html` esta ese PDF ya generado.

> DRAFT — Los datos son ficticios y sirven unicamente para mostrar el formato. Ningun importe, plazo o conclusion de estos archivos es real.

| Archivo | Maqueta | Que demuestra |
| :--- | :--- | :--- |
| `panel_reclamacion_cantidad.html` | `panel_datos` | Panel con indicadores, minigrafico de tendencia, barras comparativas, anillo de reparto, evolucion con area y umbral, cascada de importes, medidor de plazo y tabla con totales |
| `informe_viabilidad_monitorio.html` | `informe_visual` (tema sobrio) | Informe de lectura con indice lateral, indicadores, secciones numeradas, tabla comparativa, diagrama de plazos, cronologia de hitos, avisos y firmas |
| `simulador_intereses_demora.html` | `herramienta_interactiva` | Herramienta que recalcula al instante, con medidor, desglose y lista de verificacion con progreso |
| `presentacion_reclamacion_cliente.html` | `presentacion` + modulo de diagramas | 13 diapositivas para una reunion de cliente: portada, agenda, cifra enlazada a un grafico, cascada, barras, separador, diagrama de flujo, comparativa, cronologia, cita, proximos pasos, equipo y cierre; notas del orador y fuentes automaticas |
| `white_paper_morosidad_pymes.html` | `documento_largo` (tema editorial + modulo marca) + modulo de diagramas | White paper de siete paginas: portada, resumen ejecutivo con cifra enlazada, indice con enlaces, capitulos en pagina nueva con linea, barras, diagrama y matriz, notas y fuentes; cabecera y numeracion al imprimir |
| `resumen_reclamacion_una_pagina.html` | `resumen_ejecutivo` (tema corporativo) | Una sola pagina A4: titular con la recomendacion, tres indicadores (uno calculado), un grafico, conclusiones y la decision que se pide |
| `cuadro_mando_comite.html` | `cuadro_mando` (tema dorado) | Ocho KPIs con variacion, objetivos en anillos, horas en bala, estado por area y tabla compacta |
| `ficha_deudor_una_pagina.html` | `ficha_una_pagina` (tema minimal) | Datos clave del deudor, tres indicadores (uno calculado), barras y semaforos; una pagina A4 |
| `infografia_morosidad.html` | `infografia` (tema menta) | Tres cifras enormes, pictograma, anillos y linea de tiempo en vertical |
| `comparativa_vias.html` | `comparativa` (tema corporativo) | Tres vias frente a frente con veredicto, radar y halteras de coste |
| `cronograma_expediente_0417.html` | `cronograma_expediente` (tema esmeralda nocturno) | Linea de tiempo, plazos con la marca de hoy, avance por fase y proximos pasos |
| `lista_control_rgpd.html` | `lista_control` (tema tecnico) | Cumplimiento calculado, avance por bloque, semaforos y tabla de evidencias |
| `mapa_riesgos_operacion.html` | `mapa_riesgos` (tema ambar) | Matriz, medidas en semaforos, tornado de impacto y rango de exposicion |
| `escenarios_indemnizacion.html` | `escenarios` (tema oliva y oro) | Supuestos, resultado por escenario, tornado de sensibilidad y horquilla |
| `embudo_captacion.html` | `embudo_conversion` (tema lima) | Embudo, area apilada y sankey, con la conversion calculada |
| `actividad_equipo_t3.html` | `actividad_equipo` (tema pizarra) | Mapa de calor, calendario, cajas y bala de horas |
| `informe_territorial_asuntos.html` | `informe_territorial` (tema lavanda) | Mapa por comunidades con tasas, ranking y pareto |
| `poster_morosidad.html` | `poster` (tema nocturno) | Tres cifras y un grafico grande; imprime en A3 apaisado |
| `galeria_maquetas.html` | indice | Las 18 maquetas con su miniatura (carpeta `miniaturas/`), filtro por familia y enlaces al HTML y al PDF |
| `galeria_catalogo.html` | indice | Catalogo visual de la skill: los 21 estilos y los 44 graficos con su caso de uso. Con `?solo=temas` o `?solo=grupo-N` deja un solo bloque; asi se generan las imagenes de `catalogo/`, que la descripcion de la skill enlaza desde GitHub (rama `main`) porque la ficha de la app solo pinta imagenes por URL |
| `galeria_graficos.html` | base sin maqueta + todos los modulos | Los 43 tipos (con el mapa de Espana por comunidades y por provincias): los del motor, las cuatro disposiciones de diagrama, los graficos avanzados, analiticos y de seguimiento, el QR, iconos y un vencimiento en dias habiles, cada uno con su tabla de datos, su CSV y su fuente |
| `galeria_temas.html` | `panel_datos` con los 21 temas y un selector | El mismo panel con cada tema de `../references/temas-visuales.md`, en claro y en oscuro, cambiando con los botones (o con `?tema=prensa&esquema=oscuro` en la URL). Solo esta galeria lleva todos los temas a la vez; un artefacto real copia uno. `galeria_temas.png` es la hoja de contacto de los 42 estados |

El informe conserva a proposito el marcador `{{LETRADO_RESPONSABLE}}`: asi se ve como queda un dato que el usuario decide no aportar.

## Regenerar

```bash
python3 generar_ejemplos.py            # HTML y PDF (necesita Google Chrome para el PDF)
python3 generar_ejemplos.py --sin-pdf  # HTML y comprobacion en Chrome, sin PDF
```

El guion compone cada ejemplo igual que lo hara el modelo: copia la base, inserta la maqueta leida de la referencia y escribe el bloque de datos. Despues abre cada archivo en Chrome sin ventana y **falla** si la consola registra algun error (un grafico mal declarado, una fuente sin declarar) o si queda algun marcador sin resolver. Si se cambia la base o una maqueta, basta con volver a ejecutarlo para que los ejemplos y sus PDF queden al dia.

## Contornos del mapa

`generar_mapa.py` produce los contornos simplificados de los bloques `mapa_ccaa` y `mapa_provincias` a partir de Natural Earth (`ne_10m_admin_1_states_provinces`, dominio publico): agrupa las provincias en comunidades, proyecta, simplifica, coloca Canarias en recuadro y deja Ceuta y Melilla como puntos. Necesita `pyshp` y `shapely` y el shapefile descargado de naturalearthdata.com en la misma carpeta. Solo hace falta si se quieren regenerar.
