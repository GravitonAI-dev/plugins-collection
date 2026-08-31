# Asistente General

Plugin de GravitonAI para la atención de consultas abiertas, orientación jurídica y administrativa multidisciplinar, análisis de supuestos de hecho, búsquedas web y generación bajo demanda de informes y dictámenes técnicos cuando una consulta no clasifica en una skill vertical especializada.

Sirve como el **fallback universal y asistente de primera línea** para orquestadores como LangGraph, Claude Code o arquitecturas multiagente.

---

## Qué hace

- Resuelve consultas directas, definiciones, cálculos, conceptos y cuestiones de conocimiento general en el chat de forma ágil y sin burocracia.
- Realiza búsquedas de información, datos de mercado y hechos recientes en tiempo real mediante `web_search` con citas estructuradas.
- Inspecciona, resume y analiza documentos existentes en el espacio de trabajo activo mediante `read_file`.
- Analiza problemas legales y administrativos multidisciplinares, identificando la normativa aplicable, la viabilidad de pretensiones y los riesgos.
- Detecta si la consulta encaja en una skill especializada del catálogo (`derecho-civil`, `gestoria`, etc.) y orienta al usuario hacia ella.
- Genera y edita incrementalmente en el workspace informes formales (`informe_consulta_legal.md`, `memo_orientacion.md`) cuando el usuario lo solicita.

## Qué NO hace

- No sustituye el asesoramiento ni la representación legal por un abogado o graduado social colegiado.
- No redacta contratos hiper-especializados ni demandas tipificadas cuando existe una skill vertical propia (ej. `arrendamiento-urbano`, `monitorio`, etc.).
- No fuerza la creación de documentos en disco ni cuestionarios interactivos innecesarios para dudas directas.

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
    └── consulta-general/
        ├── SKILL.md
        ├── assets/
        │   ├── template-informe-consulta-general.md
        │   └── template-memo-orientacion-rapida.md
        └── references/
            ├── metodologia-analisis-juridico.md
            ├── fuentes-normativas-generales.md
            └── matriz-derivacion-especialidades.md
```
