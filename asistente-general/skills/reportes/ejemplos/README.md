# Ejemplos de la skill `reportes`

Artefactos de demostracion generados con la base `../assets/template-base-reportes.md` y las maquetas de `../references/maquetas-reportes.md`. Se abren **con doble clic** en cualquier navegador: no necesitan servidor, ni conexion, ni instalar nada. El boton inferior de cada pagina la imprime o la guarda como PDF; al lado de cada `.html` esta ese PDF ya generado.

> DRAFT — Los datos son ficticios y sirven unicamente para mostrar el formato. Ningun importe, plazo o conclusion de estos archivos es real.

| Archivo | Maqueta | Que demuestra |
| :--- | :--- | :--- |
| `panel_reclamacion_cantidad.html` | `panel_datos` | Panel con indicadores, minigrafico de tendencia, barras comparativas, anillo de reparto, evolucion con area y umbral, cascada de importes, medidor de plazo y tabla con totales |
| `informe_viabilidad_monitorio.html` | `informe_visual` (tema sobrio) | Informe de lectura con indice lateral, indicadores, secciones numeradas, tabla comparativa, diagrama de plazos, cronologia de hitos, avisos y firmas |
| `simulador_intereses_demora.html` | `herramienta_interactiva` | Herramienta que recalcula al instante, con medidor, desglose y lista de verificacion con progreso |
| `presentacion_reclamacion_cliente.html` | `presentacion` + modulo de diagramas | 13 diapositivas para una reunion de cliente: portada, agenda, cifra enlazada a un grafico, cascada, barras, separador, diagrama de flujo, comparativa, cronologia, cita, proximos pasos, equipo y cierre; notas del orador y fuentes automaticas |
| `white_paper_morosidad_pymes.html` | `documento_largo` + modulo de diagramas | White paper de siete paginas: portada, resumen ejecutivo con cifra enlazada, indice con enlaces, capitulos en pagina nueva con linea, barras, diagrama y matriz, notas y fuentes; cabecera y numeracion al imprimir |
| `resumen_reclamacion_una_pagina.html` | `resumen_ejecutivo` | Una sola pagina A4: titular con la recomendacion, tres indicadores (uno calculado), un grafico, conclusiones y la decision que se pide |
| `galeria_graficos.html` | base sin maqueta + todos los modulos | Los 30 tipos (con el mapa de Espana por comunidades y por provincias): los del motor, las cuatro disposiciones de diagrama, los graficos avanzados, el QR, iconos y un vencimiento en dias habiles, cada uno con su tabla de datos, su CSV y su fuente |

El informe conserva a proposito el marcador `{{LETRADO_RESPONSABLE}}`: asi se ve como queda un dato que el usuario decide no aportar.

## Regenerar

```bash
python3 generar_ejemplos.py            # HTML y PDF (necesita Google Chrome para el PDF)
python3 generar_ejemplos.py --sin-pdf  # HTML y comprobacion en Chrome, sin PDF
```

El guion compone cada ejemplo igual que lo hara el modelo: copia la base, inserta la maqueta leida de la referencia y escribe el bloque de datos. Despues abre cada archivo en Chrome sin ventana y **falla** si la consola registra algun error (un grafico mal declarado, una fuente sin declarar) o si queda algun marcador sin resolver. Si se cambia la base o una maqueta, basta con volver a ejecutarlo para que los ejemplos y sus PDF queden al dia.

## Contornos del mapa

`generar_mapa.py` produce los contornos simplificados de los bloques `mapa_ccaa` y `mapa_provincias` a partir de Natural Earth (`ne_10m_admin_1_states_provinces`, dominio publico): agrupa las provincias en comunidades, proyecta, simplifica, coloca Canarias en recuadro y deja Ceuta y Melilla como puntos. Necesita `pyshp` y `shapely` y el shapefile descargado de naturalearthdata.com en la misma carpeta. Solo hace falta si se quieren regenerar.
