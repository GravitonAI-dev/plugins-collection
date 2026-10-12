# Asistente General

Plugin de GravitonAI para la atención de consultas abiertas, orientación jurídica y administrativa multidisciplinar, análisis de supuestos de hecho, búsquedas web y generación bajo demanda de informes y dictámenes técnicos cuando una consulta no clasifica en una skill vertical especializada.

Sirve como el **fallback universal y asistente de primera línea** para orquestadores como LangGraph, Claude Code o arquitecturas multiagente.

---

## Qué hace

- Resuelve consultas directas, definiciones, cálculos, conceptos y cuestiones de conocimiento general en el chat de forma ágil y sin burocracia.
- Realiza búsquedas de información, datos de mercado y hechos recientes en tiempo real mediante `web_search` con citas estructuradas.
- Inspecciona, resume y analiza documentos existentes en el espacio de trabajo activo (prioritariamente mediante `# WORKSPACE ACTIVE DOCUMENTS`, o `read_file` como recurso extremo).
- Analiza problemas legales y administrativos multidisciplinares, identificando la normativa aplicable, la viabilidad de pretensiones y los riesgos.
- Detecta si la consulta encaja en una skill especializada del catálogo (`derecho-civil`, `gestoria`, etc.) y orienta al usuario hacia ella.
- Genera y edita incrementalmente en el workspace informes formales (`informe_consulta_legal.md`, `memo_orientacion.md`) cuando el usuario lo solicita.
- Produce artefactos autocontenidos en un único archivo `.html` que el usuario abre en su navegador con doble clic y puede imprimir o guardar como PDF: informes visuales, paneles de datos con gráficos y herramientas interactivas de cálculo.

## Qué NO hace

- No sustituye el asesoramiento ni la representación legal por un abogado o graduado social colegiado.
- No redacta contratos hiper-especializados ni demandas tipificadas cuando existe una skill vertical propia (ej. `arrendamiento-urbano`, `monitorio`, etc.).
- No fuerza la creación de documentos en disco ni cuestionarios interactivos innecesarios para dudas directas.
- No construye aplicaciones web con servidor, base de datos o conexión a servicios externos: los artefactos son un único archivo estático sin dependencias.

---

## Skills

### `consulta-general`

Asistente universal y versátil para el procesamiento de consultas no catalogadas. Opera en tres modalidades adaptativas según la intención del usuario:
1. **Modo Directo (Chat):** Respuestas instantáneas para dudas informativas, datos de mercado o lectura de archivos de workspace.
2. **Modo Consultivo y Orientación:** Diagnóstico del caso, encuadre legal, análisis de riesgos, hoja de ruta y sugerencia de derivación a skills especializadas.
3. **Modo Documental (Workspace bajo demanda):** Creación y edición incremental sección a sección de un dictamen o memorándum formal en disco.

- **Invocación:** `/asistente-general:consulta-general`
- **Inputs principales:** Materia/rama de la consulta (V1), tipo de requerimiento (V2), perfil del consultante (V3), situación de urgencia/plazos (V4), origen de la plantilla/formato (V5), hechos y dudas planteadas.
- **Outputs:** Respuesta argumentada en chat o informe formal en markdown (`DRAFT`) en workspace (`assets/template-informe-consulta-general.md` o `assets/template-memo-orientacion-rapida.md`).

### `reportes`

Generación de artefactos autocontenidos en HTML, del estilo de los que el usuario ya conoce de otros asistentes, pero pensados para un despacho: sobrios, imprimibles y sin una sola dependencia externa (ni librerías, ni CDN, ni conexión). Seis formatos, y un catálogo con las recetas de los artefactos que más se piden (situación del expediente, KPIs mensuales, due diligence, white paper, pitch, propuesta de honorarios...):
1. **Informe visual:** dossier de lectura con índice lateral, indicadores, secciones numeradas, tabla comparativa, cronología de hitos y firmas.
2. **Panel de datos:** rejilla de tarjetas con indicadores, minigráfico de tendencia, barras comparativas, anillo de reparto, evolución con área y umbral, cascada de importes, medidor de plazo y tabla con totales.
3. **Herramienta interactiva:** calculadora o simulador que recalcula al instante, con medidor, desglose auditable y lista de verificación con progreso.
4. **Presentación:** diapositivas 16:9 declaradas como datos (portada, agenda, cifra, gráfico con conclusión, comparativa, cronología, tabla, cita, equipo, próximos pasos), con navegación, pantalla completa y notas del orador; se imprimen una por página.
5. **Documento largo:** white paper, memoria anual o due diligence, con portada a página completa, resumen ejecutivo, índice con enlaces, capítulos que empiezan en página nueva y, al imprimir, cabecera y número de página.
6. **Resumen ejecutivo:** una sola página A4 con la conclusión, tres indicadores, un gráfico y la decisión que se pide.

Incluye además módulos opcionales, que solo viajan en los artefactos que los usan: **diagramas con conectores** (flujos y procesos, organigramas y estructuras societarias, mapa de relaciones entre partes y quién hace qué), **gráficos avanzados** (dispersión y burbujas, histograma, radar, embudo, treemap, pendiente, halteras, pirámide, calendario de calor y pictograma), **mapa de España** por comunidades autónomas o por provincias, **iconos** propios y **código QR** generado dentro del documento. El motor aplica la **identidad del despacho** (colores, logo y pie) desde los datos y calcula **plazos en días hábiles** con los festivos que se le indiquen.

Los gráficos no se dibujan a mano: se declaran como datos y los dibuja un motor propio incluido en la plantilla base (barras, columnas simples, agrupadas y apiladas, línea con área, umbral y anotaciones, minigráfico, medidor, cascada, matriz de riesgo, diagrama de plazos, anillo y tarta). El motor calcula escalas, totales y porcentajes, añade a cada gráfico su tabla de datos con descarga en CSV y su fuente, y compone el pie de fuentes; las cifras del texto pueden salir del mismo bloque de datos, así que texto y gráfico no se contradicen. Se acompaña de criterios de qué forma responde a cada pregunta y reglas de honestidad gráfica (eje desde cero, sin recortes, sin datos inventados).

- **Invocación:** `/asistente-general:reportes`
- **Inputs principales:** Tipo de artefacto (V1), destino de uso —pantalla o impresión— (V2), origen de los datos (V3), identidad visual (V4), origen de la plantilla (V5), datos y parámetros a representar.
- **Outputs:** Archivo `snake_case.html` en el espacio de trabajo, con tema claro y oscuro, diseño adaptable, estilos de impresión en A4 y aviso `DRAFT` visible.
- **Ejemplos abribles:** `skills/reportes/ejemplos/` contiene siete artefactos completos con su PDF ya generado, incluida una galería con todos los tipos de gráfico del motor.

---

## Estructura del Plugin

```
asistente-general/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json
├── agent_tools.json
├── CLAUDE.md
├── README.md
└── skills/
    ├── consulta-general/
    │   ├── SKILL.md
    │   ├── assets/
    │   │   ├── template-informe-consulta-general.md
    │   │   └── template-memo-orientacion-rapida.md
    │   └── references/
    │       ├── metodologia-analisis-juridico.md
    │       ├── fuentes-normativas-generales.md
    │       └── matriz-derivacion-especialidades.md
    └── reportes/
        ├── SKILL.md
        ├── assets/
        │   └── template-base-reportes.md      ← estilos, temas, impresión y motor de gráficos
        ├── references/
        │   ├── catalogo-reportes.md           ← recetas de los artefactos típicos
        │   ├── maquetas-reportes.md           ← esqueleto de cada tipo de artefacto
        │   ├── modulos-motor.md               ← módulos opcionales (diagramas, gráficos avanzados, iconos, QR)
        │   ├── anatomia-artefacto.md
        │   ├── biblioteca-componentes-visuales.md
        │   └── criterios-visualizacion-datos.md
        └── ejemplos/
            ├── generar_ejemplos.py
            ├── panel_reclamacion_cantidad.html / .pdf
            ├── informe_viabilidad_monitorio.html / .pdf
            ├── simulador_intereses_demora.html / .pdf
            ├── presentacion_reclamacion_cliente.html / .pdf
            ├── white_paper_morosidad_pymes.html / .pdf
            ├── resumen_reclamacion_una_pagina.html / .pdf
            └── galeria_graficos.html / .pdf
```
