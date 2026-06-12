# CLAUDE.md — plugins-collection (root)

> System prompt global. Lo lee Claude al trabajar con este repositorio. Contiene convenciones, guardrails y políticas que aplican a **todos** los plugins.

## Propósito del repositorio

`plugins-collection` es un **marketplace de plugins de Claude** mantenido por GravitonAI. Cada plugin es un bundle autocontenido de skills, agentes, conectores MCP y un playbook (`CLAUDE.md` del plugin) que se instala donde el usuario lo necesite (Claude Code, Cowork, Managed Agents).

## Idioma y tono

- **Todo el contenido en español**: `SKILL.md`, `CLAUDE.md`, `README.md`, plantillas, checklists.
- Tono: profesional, claro, sin jerga innecesaria. Cero emojis salvo que el usuario los solicite.
- Direcciones técnicas y comandos en inglés (sintaxis, nombres de tools, paths).

## Guardrails uniformes (no negociables)

1. **Borrador, no consejo legal.** Todo output de un plugin que toque temas jurídicos, regulatorios, de cumplimiento, fiscales o de privacidad debe encabezarse con `> DRAFT — para revisión por un abogado. No constituye asesoría legal.` El abogado revisa, verifica y asume responsabilidad profesional.
2. **Atribución de fuentes.** Toda cita a jurisprudencia, regulación o doctrina debe llevar fuente enlazada. Si no hay research tool conectado, marcar explícitamente `[verificar]`.
3. **Defaults conservadores.** En llamadas subjetivas (privilegio, razonabilidad, riesgo), elegir la posición más conservadora. Marcar la asunción de jurisdicción cuando aplique.
4. **Gates antes de acciones irreversibles.** Nada de `file`, `send`, `commit`, `delete`, `escalate` sin confirmación explícita del usuario o del abogado responsable.
5. **Privacidad.** No incluir nombres reales, datos de clientes ni secretos en ejemplos, fixtures o commits. Usar placeholders tipo `Acme Corp.`, `Juan Pérez`, `confidencial-ejemplo`.

## Cómo están organizados los plugins

```
plugins-collection/         ← este repo (marketplace root)
├── .claude-plugin/
│   └── marketplace.json     ← registro de TODOS los plugins disponibles
├── mcp_servers.json         ← catálogo GLOBAL de servidores MCP (referenciados por id)
├── agent_tools.json         ← catálogo GLOBAL de tools (referenciados por id)
├── CLAUDE.md                ← este archivo (system prompt global)
├── README.md                ← documentación de la estructura y convenciones
└── <plugin-name>/           ← un plugin autocontenido
    ├── .claude-plugin/
    │   └── plugin.json      ← manifest del plugin
    ├── .mcp.json            ← subset de servidores MCP que este plugin usa
    ├── agent_tools.json     ← subset de tools que este plugin usa
    ├── CLAUDE.md            ← playbook / estilo / guardrails del plugin
    ├── README.md            ← documentación del plugin
    └── skills/
        └── <skill-name>/
            ├── SKILL.md     ← procedimiento (lo lee Claude al ejecutar la skill)
            ├── scripts/     ← (opcional) ejecutables
            ├── references/  ← (opcional) contexto documental que la skill necesita
            └── assets/      ← (opcional) plantillas, recursos
```

## Catálogos globales (mcp_servers.json / agent_tools.json)

Los catálogos son la **única fuente de verdad** sobre qué servidores MCP y qué tools existen en el ecosistema. Reglas:

1. **Definir una vez, referenciar por id.** Los plugins NO duplican schemas. Si un plugin necesita un servidor, lo lista en su `.mcp.json` con su `id` global. Si necesita un tool, lo lista en su `agent_tools.json` con su `id` global.
2. **Toda nueva adición va al catálogo global primero.** Agregar un servidor/tool al catálogo raíz antes de que cualquier plugin lo referencie.
3. **Convención de IDs**: prefijo `io.gravitonai.<categoria>.<nombre>`.
   - Servidores: `io.gravitonai.courtlistener`, `io.gravitonai.ironclad`
   - Tools: `io.gravitonai.tools.read_document`, `io.gravitonai.tools.draft_markdown`
4. **Esquema de servidores** sigue `server.json` de Anthropic MCP Registry (campos `id`, `name`, `displayName`, `description`, `version`, `transport`, `auth`, `tags`).
5. **Esquema de tools** sigue el formato de declaración de tools de MCP (`input_schema` y `output_schema` como JSON Schema).

## Convenciones de versionado

- **Semver** en `plugin.json`, en cada `marketplace.json` entry y en cada servidor/tool del catálogo.
- Cambios incompatibles con plugins existentes → bump MAJOR del catálogo.
- Nuevos servidores/tools agregables → bump MINOR.
- Fixes de descripción o tags → bump PATCH.

## Cómo agregar un plugin nuevo (resumen)

1. Crear carpeta `<plugin>/` siguiendo la estructura arriba.
2. Crear `marketplace.json` entry con `name`, `source: "./<plugin>"`, `version`, `description`.
3. Si el plugin necesita servidores/tools nuevos: agregarlos primero al catálogo global.
4. Listar en el `<plugin>/.mcp.json` y `<plugin>/agent_tools.json` los IDs que va a usar.
5. Documentar el playbook en `<plugin>/CLAUDE.md` con guardrails y defaults.
6. Validar que todos los IDs referenciados existen en el catálogo global.

## Cómo agregar una skill nueva (resumen)

1. Crear `<plugin>/skills/<skill>/SKILL.md` con frontmatter (descripción + condiciones de uso), inputs, procedimiento paso a paso, formato de salida, guardrails.
2. Agregar checklist o contexto a `references/` si aplica.
3. Agregar plantillas de salida a `assets/` si aplica.
4. Opcional: scripts ejecutables en `scripts/` (referenciados por path relativo desde `SKILL.md`).
5. Documentar en el `<plugin>/README.md` qué hace la skill y qué no hace.

## Referencia para agentes

Si eres un agente de Claude Code trabajando en este repositorio:

- **Antes de modificar**: lee el `plugin.json` del plugin afectado y su `CLAUDE.md`.
- **Al agregar archivos**: respeta la estructura canónica (no inventes carpetas nuevas sin documentarlas aquí primero).
- **Al referenciar servidores/tools**: usa el `id` del catálogo global, no dupliques schemas.
- **Al escribir contenido**: español, sin emojis, con guardrails y marcadores `EDITAR PARA TU EQUIPO` para secciones personalizables.
- **Nunca commitees secretos**, credenciales, datos de clientes o borradores locales.
