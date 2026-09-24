# Ejemplos de la skill `artefacto-visual`

Artefactos de demostracion generados con las plantillas de `../assets`. Se abren **con doble clic** en cualquier navegador: no necesitan servidor, ni conexion, ni instalar nada. El boton inferior de cada pagina la imprime o la guarda como PDF; al lado de cada `.html` esta ese PDF ya generado.

> DRAFT — Los datos son ficticios y sirven unicamente para mostrar el formato. Ningun importe, plazo o conclusion de estos archivos es real.

| Archivo | Plantilla de origen | Que demuestra |
| :--- | :--- | :--- |
| `panel_reclamacion_cantidad.html` | `template-panel-datos.md` | Panel con indicadores, minigrafico de tendencia, barras comparativas, anillo de reparto, evolucion con area y umbral, cascada de importes, medidor de plazo y tabla con totales |
| `informe_viabilidad_monitorio.html` | `template-informe-visual.md` | Informe de lectura con indice lateral, indicadores, secciones numeradas, tabla comparativa, cronologia de hitos, avisos y firmas |
| `simulador_intereses_demora.html` | `template-herramienta-interactiva.md` | Herramienta que recalcula al instante, con medidor, desglose y lista de verificacion con progreso |
| `galeria_graficos.html` | compuesta a partir del sistema de diseno | Las once formas graficas de la biblioteca, cada una con la formula exacta de sus coordenadas |

El informe conserva a proposito el marcador `{{LETRADO_RESPONSABLE}}`: asi se ve como queda un dato que el usuario decide no aportar.

## Regenerar

```bash
python3 generar_ejemplos.py            # HTML y PDF (necesita Google Chrome para el PDF)
python3 generar_ejemplos.py --sin-pdf  # solo HTML
```

El guion lee las plantillas de `../assets`, calcula toda la geometria de los graficos con las formulas de `../references/biblioteca-componentes-visuales.md` y avisa si algun marcador queda sin resolver. Si se cambia una plantilla, basta con volver a ejecutarlo para que los ejemplos y sus PDF queden al dia.
