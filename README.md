# plugins-collection

Marketplace de plugins para agentes LLM. La estructura es **agnóstica del orquestador**: está pensada para ser consumida por Claude (Code, Cowork, Managed Agents), pero también por LangGraph, AutoGen, Temporal, o cualquier orquestador custom que respete el shape.

> Todo el contenido en español. Tono profesional, sin emojis. Comandos y nombres técnicos en inglés.

---

## 1. ¿Qué es?

`plugins-collection` es un **catálogo versionado de plugins de agente**. Cada plugin es un bundle autocontenido que agrupa:

- un **playbook** (cómo se comporta el agente en ese dominio),
- un set de **skills** (procedimientos paso a paso),
- referencias a **servidores MCP** y **tools** que el agente puede invocar,
- opcionalmente, **scripts**, **agentes programados** y **hooks** (placeholders estructurales por ahora).

Todo el repositorio es **markdown + JSON, sin código de runtime**. La "ejecución" la hace el orquestador que lo carga: él lee los markdown y JSON, los interpreta, y monta el flujo de agente encima.

---

## 2. Estado actual (importante)

Este repo es un **punto de partida**. Contiene la estructura completa y un plugin de ejemplo funcionando a nivel de **definición**, no a nivel de **ejecución runtime**. Antes de usarlo lee esta tabla.

| Capa | Qué existe | Qué **no** existe todavía |
|---|---|---|
| Marketplace | `.claude-plugin/marketplace.json` con registry de plugins | Instalador propio (se usa el de Claude Code) |
| Catálogo de MCP servers | `mcp_servers.json` con 5 servers declarados | Cliente MCP que los conecte y ejecute |
| Catálogo de tools | `agent_tools.json` con 5 tools declarados (input/output schema) | Runtime que los invoque |
| Plugin manifest | `plugin.json` con metadatos y lista de skills | Sistema de versionado / firma de plugins |
| Playbook | `CLAUDE.md` raíz y por plugin | Sistema que cargue perfiles desde `~/.claude/...` |
| Skills | `SKILL.md` con frontmatter y procedimiento | Mecanismo de auto-invocación por contexto |
| References | `references/*.md` como contexto por skill | Indexado / búsqueda semántica sobre ellos |
| Assets | `assets/*.md` como plantillas | Motor de template con variables |
| **Scripts** | Estructura `scripts/` mencionada pero **ningún plugin la usa** | Ejecución de scripts desde SKILL.md |
| **Agents (scheduled)** | Carpeta `agents/` mencionada pero **no creada en el ejemplo** | Watchers / monitors / cron agents |
| **Hooks** | Carpeta `hooks/` mencionada pero **no creada en el ejemplo** | Sistema de pre/post-tool hooks |
| **Subagentes** | No existe en la estructura | Sistema de delegación `callable_agents` |
| **Slash commands** | Convención `/<plugin>:<skill>` documentada | Definiciones formales en `commands/` |
| Validación | Validación manual cruzada (ver §10) | Script `validate.py` automatizado |

**En resumen**: lo que hay es la **maqueta** de un sistema de plugins. El valor ahora mismo es:
1. Tener el shape canónico decidido y documentado.
2. Poder escribir plugins/skills y versionarlos como código.
3. Poder conectar un orquestador real (Claude Code, LangGraph, lo que sea) **encima** de este repo sin renegociar la estructura.

Lo que **no** hay todavía: el runtime, los scripts, los agentes programados, los hooks. La estructura los contempla, pero la implementación es para una fase posterior.

---

## 3. Cómo encaja con tu orquestador

El repo **no incluye** un orquestador. Lo que hace es **definir el contrato** que cualquier orquestador puede interpretar.

| Orquestador | Cómo consumiría este repo |
|---|---|
| **Claude Code** | `/plugin marketplace add <path>` lee `marketplace.json`, instala plugins, carga `SKILL.md` como slash commands, usa `CLAUDE.md` como system prompt. Los catálogos se cargan como configuración. |
| **Claude Cowork** | Mismo flujo desde la UI. Customiza desde la sidebar. |
| **Claude Managed Agents** | `agent.yaml` por cookbook referencia los mismos `SKILL.md` y `CLAUDE.md`. El orchestrator se deploya a la API. |
| **LangGraph / LangChain** | Un custom loader lee `marketplace.json`, parsea cada `plugin.json`, y monta un grafo donde los nodos son las skills y las aristas siguen el flujo descrito en `SKILL.md`. Los catálogos se inyectan como tool definitions. |
| **AutoGen / CrewAI** | Similar: las skills se modelan como tareas con su `SKILL.md` como prompt, los MCP servers como tools, los playbooks como instrucciones del agente. |
| **Custom / in-house** | Un loader en Python/TS lee la estructura y la mapea a tu modelo interno (workers, channels, etc.). El contrato es solo JSON + markdown. |

La estructura no favorece a ninguno. Si mañana cambias de Claude a LangGraph, **los plugins siguen siendo los mismos archivos**.

---

## 4. Vista general del flujo de agente

Cómo viaja una solicitud del usuario a través del sistema, end to end:

```
   ┌──────────────────┐
   │      Usuario     │
   │  "/commercial-   │
   │  legal:nda-review"│
   └────────┬─────────┘
            │
            ▼
   ┌──────────────────────────────────────────┐
   │              Orquestador                 │  (Claude Code, LangGraph, custom)
   │  1. Lee marketplace.json                 │
   │  2. Resuelve plugin: commercial-legal    │
   │  3. Carga CLAUDE.md (raíz + plugin)      │
   │     → guardrails, idioma, tono           │
   │  4. Lee plugin.json → skills[]           │
   │  5. Resuelve: .mcp.json y agent_tools.   │
   │     json contra catálogos globales       │
   │  6. Carga skills/nda-review/SKILL.md     │
   └────────┬─────────────────────────────────┘
            │
            ▼
   ┌──────────────────────────────────────────┐
   │            Agente (LLM)                  │
   │  7. SKILL.md dicta el procedimiento:     │
   │     - Lee references/nda-clause-         │
   │       checklist.md (contexto)            │
   │     - Aplica triage GREEN/YELLOW/RED     │
   │     - Llena assets/nda-triage-           │
   │       output-template.md                 │
   │  8. Si la skill lo requiere:             │
   │     - Invoca tools (read_document, etc.) │
   │     - Conecta MCP servers (CourtListener)│
   │     - Ejecuta scripts (futuro)           │
   │  9. Aplica guardrails en cada paso       │
   └────────┬─────────────────────────────────┘
            │
            ▼
   ┌──────────────────────────────────────────┐
   │              Output                      │
   │  10. Memo de triage (markdown)           │
   │  11. Si verdict == ROJO:                 │
   │      gate → confirmar → escalate_to_     │
   │      attorney tool                       │
   └──────────────────────────────────────────┘
```

**Lo que el orquestador hace**: interpretar y orquestar.
**Lo que el agente hace**: razonar y aplicar el procedimiento.
**Lo que el repo hace**: definir el contrato que ambos respetan.

---

## 5. Estructura del repositorio

```
plugins-collection/                       ← raíz del marketplace
│
├── .claude-plugin/
│   └── marketplace.json                  ← registry de plugins (entrada al sistema)
│
├── mcp_servers.json                      ← catálogo global de servidores MCP
├── agent_tools.json                      ← catálogo global de tools
│
├── CLAUDE.md                             ← system prompt global
├── README.md                             ← este archivo
├── .gitignore
│
└── <plugin>/                             ← un plugin autocontenido
    │
    ├── .claude-plugin/
    │   └── plugin.json                   ← manifest del plugin
    │
    ├── .mcp.json                         ← qué servers globales usa este plugin
    ├── agent_tools.json                  ← qué tools globales usa este plugin
    │
    ├── CLAUDE.md                         ← playbook del plugin (comportamiento)
    ├── README.md                         ← docs del plugin
    │
    └── skills/
        └── <skill-name>/
            ├── SKILL.md                  ← procedimiento (obligatorio)
            ├── references/               ← contexto que la skill consulta
            │   └── *.md
            ├── assets/                   ← plantillas que la skill produce
            │   └── *.md
            └── scripts/                  ← ejecutables (estructural, no usado aún)
                └── *.sh / *.py
```

**Resumen por capa** (qué hace cada una en el flujo):

| Capa | Carpeta/archivo | Quién lo lee | Rol en el flujo de agente |
|---|---|---|---|
| Marketplace | `.claude-plugin/marketplace.json` | Orquestador | "Qué plugins hay y dónde están" |
| Catálogos globales | `mcp_servers.json`, `agent_tools.json` | Orquestador + validadores | Fuente única de verdad sobre servers y tools |
| System prompt global | `CLAUDE.md` raíz | Agente | Guardrails, idioma, tono, convenciones |
| Plugin manifest | `<plugin>/.claude-plugin/plugin.json` | Orquestador | Identidad, skills listadas, autor |
| Plugin MCP ref | `<plugin>/.mcp.json` | Orquestador | Qué servers necesita este plugin |
| Plugin tools ref | `<plugin>/agent_tools.json` | Orquestador | Qué tools necesita este plugin |
| Plugin playbook | `<plugin>/CLAUDE.md` | Agente | Comportamiento específico del dominio |
| Plugin docs | `<plugin>/README.md` | Humanos | Qué hace, qué no hace, cómo tunear |
| Skill procedure | `<plugin>/skills/<skill>/SKILL.md` | Agente | Procedimiento paso a paso de la skill |
| Skill context | `references/` | Agente | Material que la skill consulta |
| Skill templates | `assets/` | Agente | Plantillas de output de la skill |
| Skill scripts | `scripts/` | Agente (vía bash) | Código ejecutable (futuro) |

---

## 6. Capa global — el "exterior" del repositorio

### 6.1 `.claude-plugin/marketplace.json`

**Rol en el flujo**: punto de entrada. El orquestador lo lee primero para saber qué plugins están disponibles y desde dónde se carga cada uno.

**Estructura**: sigue el formato de marketplace de Claude Code. Cada entry declara `name`, `source` (path al plugin), `version`, `description`, `author`.

**Ejemplo**:
```json
{
  "name": "commercial-legal",
  "source": "./commercial-legal",
  "version": "0.1.0",
  "description": "Revisión de NDAs contra el playbook del equipo."
}
```

### 6.2 `mcp_servers.json`

**Rol en el flujo**: catálogo que el orquestador consulta cuando un plugin declara que necesita un servidor MCP. Le da al orquestador cómo conectarse (URL, transporte, auth).

**Estructura**: sigue `server.json` del MCP Registry de Anthropic. Cada server tiene `id` único, `transport`, `auth`, `tags`, opcionalmente `used_by`.

**Cuándo se usa**: cuando la skill necesita datos externos en vivo (dockets de CourtListener, registros de Ironclad, archivos de Google Drive).

**Estado actual**: existen 5 servers declarados como ejemplo. El cliente MCP que los conecte y ejecute lo trae el orquestador, no este repo.

### 6.3 `agent_tools.json`

**Rol en el flujo**: catálogo de funciones estructuradas que el agente puede invocar. El orquestador convierte cada tool en una function-call que el LLM conoce.

**Estructura**: cada tool tiene `id`, `input_schema` y `output_schema` (JSON Schema). Un campo `side_effects: true|false` indica si el tool modifica estado externo — clave para que la skill pida confirmación antes de invocar.

**Cuándo se usa**: cuando el agente necesita ejecutar algo más complejo que razonar (leer un documento, generar un archivo, crear un ticket de escalación).

**Estado actual**: existen 5 tools declaradas como ejemplo. El runtime que las invoque lo trae el orquestador.

### 6.4 `CLAUDE.md` (raíz)

**Rol en el flujo**: system prompt global. Lo lee el agente antes que cualquier `CLAUDE.md` de plugin. Define idioma (español), tono (profesional, sin emojis), guardrails (DRAFT header, atribución, defaults conservadores, gates, privacidad), convenciones (IDs con prefijo `io.gravitonai.`, semver, referencia por id).

**Regla clave**: las reglas de un plugin solo pueden **estrechar** las reglas globales, nunca ampliarlas.

### 6.5 `README.md`

**Rol en el flujo**: este archivo. Documentación principal para humanos. No es leído por el agente.

### 6.6 `.gitignore`

Excluye artefactos del sistema operativo, IDEs, entornos virtuales, **y borradores privados** (`*.local.md`, `drafts/`, `private/`, `.env`). Regla dura: nada de secretos, datos de clientes, ni archivos subidos por el usuario llega al repo.

---

## 7. Capa de plugin — `<plugin>/`

Un plugin es una unidad de **dominio vertical** (legal comercial, privacidad, propiedad intelectual, etc.). Se compone de: identidad, playbook, dependencias, documentación y skills.

### 7.1 `.claude-plugin/plugin.json`

**Rol en el flujo**: manifest que el orquestador lee para saber qué hay dentro del plugin. Identifica el plugin, su versión, autor, y enumera las skills que contiene.

**Estructura mínima**:
```json
{
  "name": "commercial-legal",
  "version": "0.1.0",
  "description": "...",
  "author": { "name": "GravitonAI" },
  "skills": ["nda-review"],
  "agents": [],
  "hooks": []
}
```

Los arrays `agents` y `hooks` están **vacíos** en este punto (no implementados). Quedan reservados para la fase 2.

### 7.2 `.mcp.json`

**Rol en el flujo**: el orquestador lo lee para saber qué servers del catálogo global necesita este plugin. **Es una referencia por id, no una redefinición del schema.**

**Estructura**:
```json
{
  "servers": [
    { "id": "io.gravitonai.gdrive", "required": true },
    { "id": "io.gravitonai.courtlistener", "required": false }
  ]
}
```

- `required: true` → el plugin no funciona sin este server.
- `required: false` → opcional; la skill degrada con gracia si no está configurado.

### 7.3 `agent_tools.json`

**Rol en el flujo**: análogo a `.mcp.json` pero para tools. El orquestador sabe qué tools tiene que tener disponibles antes de ejecutar cualquier skill de este plugin.

### 7.4 `CLAUDE.md` del plugin

**Rol en el flujo**: playbook del plugin. Lo lee el agente al activarse cualquier skill del plugin. Define el comportamiento específico del dominio: jurisdicción por defecto, tono, defaults de triage, matriz de escalación, guardrails adicionales.

**Diferencia con el `CLAUDE.md` raíz**: el raíz es universal, este es del dominio. Las reglas del plugin no pueden contradecir las del raíz, solo añadir specificity.

**Secciones típicas**:
- Propósito y audiencia.
- Jurisdicción por defecto (con marcadores `EDITAR PARA TU EQUIPO`).
- Tono y estilo de output.
- Defaults: qué se asume si el usuario no lo dice.
- Matriz de escalación: qué casos van a abogado, cuáles se resuelven solos.
- Guardrails adicionales a los globales.
- Lista de skills.
- Limitaciones explícitas.

### 7.5 `README.md` del plugin

**Rol en el flujo**: documentación del plugin para humanos. Estructura sugerida: qué hace, qué no hace, dependencias, cómo instalar, cómo tunear, lista de skills.

---

## 8. Capa de skill — `<plugin>/skills/<skill>/`

Una skill es una **unidad de trabajo concreto**: un procedimiento que el agente sabe ejecutar. Se invoca como `/<plugin>:<skill>` (convención slash command) o se activa automáticamente cuando el contexto lo amerita.

### 8.1 `SKILL.md` (obligatorio)

**Rol en el flujo**: el corazón de la skill. Es el archivo que el agente lee para saber qué pasos seguir. Define:
- **Frontmatter** (YAML al inicio): descripción, condiciones de uso (`when_to_use`), inputs, outputs, referencias a `references/` y `assets/`.
- **Guardrails** específicos de la skill.
- **Procedimiento**: pasos numerados que el agente ejecuta.
- **Formato de salida**: descripción del output esperado o referencia a un `assets/`.
- **Escalación**: cuándo y cómo pedir confirmación humana o derivar a un abogado.

**Estructura recomendada**:
```markdown
---
description: ...
when_to_use: |
  - condición 1
  - condición 2
inputs:
  - nombre: descripción
outputs:
  - nombre: descripción
references:
  - references/<archivo>.md
assets:
  - assets/<archivo>.md
---

# <nombre de la skill>

## Guardrails
[...]

## Procedimiento
1. Paso 1
2. Paso 2
[...]

## Formato de salida
[referencia a assets/]

## Escalación
[...]
```

### 8.2 `references/`

**Rol en el flujo**: contexto documental que la skill **consulta** durante el procedimiento. No se copia al output. Ejemplos: checklists de cláusulas, matrices de jurisdicción, glosarios, índices de jurisprudencia.

**Cuándo agregar más archivos**: cuando el `SKILL.md` empiece a ser largo y la mayor parte del contenido sea referencial más que procedural.

**Convención**: kebab-case, una concern por archivo. Si la lista crece, agrupar por subcarpeta (`references/us/`, `references/eu/`).

### 8.3 `assets/`

**Rol en el flujo**: plantillas que la skill **produce** como output. Se referencian desde `SKILL.md` por path relativo. La skill las llena con los datos del caso.

**Convención**: cada plantilla lleva marcadores `<!-- {{variable}} -->` o `{{variable}}` que `SKILL.md` indica cómo llenar.

### 8.4 `scripts/` (estructural, no usado aún)

**Rol previsto en el flujo**: código ejecutable que la skill invoca vía `bash`. Útil cuando hay que extraer texto de PDFs, validar estructura de un documento, transformar formatos, etc.

**Estado actual**: el directorio **no está creado** en el ejemplo (`nda-review`). Está mencionado en el `README.md` raíz y reservado en la estructura para plugins que lo necesiten. Cuando un plugin lo agregue, los scripts deben:
- Tener un nombre descriptivo (`extract-text.sh`, `validate-clauses.py`).
- Documentar input/output en su header.
- Referenciarse desde `SKILL.md` por path relativo (`./scripts/<nombre>`).

---

## 9. Elementos estructurales (preparados para escalar)

Estos elementos **no existen en el ejemplo actual** pero la estructura los contempla. Se documentan aquí para que cuando se implementen, haya un lugar claro para cada uno.

### 9.1 `agents/` — agentes programados o event-driven

**Qué sería**: workflows que corren en background, disparados por schedule (cron) o por eventos (webhook, nueva entrada en un feed, etc.). Ejemplos: renewal watcher, docket watcher, regulatory feed monitor, diligence grid.

**Forma esperada** (cuando se implemente): un directorio por plugin, con archivos markdown que tengan frontmatter con schedule y descripción, similar a SKILL.md pero sin inputs del usuario.

**Estado**: no creado. No hay cron / scheduler definido en el repo.

### 9.2 `hooks/` — pre y post-tool hooks

**Qué sería**: código que se ejecuta antes o después de una tool call. Útil para logging, validación adicional, redacción de PII, o gates de seguridad.

**Forma esperada** (cuando se implemente): archivos por hook (`pre-tool.sh`, `post-tool.py`) con metadata sobre cuándo se disparan.

**Estado**: no creado. El concepto está en la estructura pero sin implementación.

### 9.3 Comandos (`/<plugin>:<skill>`)

**Qué sería**: definiciones formales de slash commands. La convención `/<plugin>:<skill>` ya está documentada y se infiere del nombre del directorio de la skill. Una definición formal en `commands/<nombre>.json` permitiría metadata adicional (descripción, argumentos, permisos).

**Estado**: implícito (por convención de nombres), no formal. No hay archivos `commands/` en el repo.

### 9.4 Subagentes (delegación)

**Qué sería**: la skill puede delegar parte de su trabajo a un subagente especializado (típicamente un LLM en su propio contexto). Ejemplo: una skill de due diligence puede delegar extracción de issues a un subagente por documento.

**Estado**: no contemplado en la estructura actual. Cuando se implemente, probablemente requiera metadata en `SKILL.md` (qué subagentes usar, qué contexto pasan, qué reciben) y un mecanismo de orquestación que el repo actual no define.

### 9.5 Watchers y monitors

**Qué sería**: variantes de agentes programados especializados en observar feeds externos. Se solapan con `agents/` (9.1) pero tienen semántica distinta (son "ojos" sobre una fuente, no "manos" que ejecutan trabajo).

**Estado**: no contemplado estructuralmente. Probablemente vivan en `agents/` cuando se implemente, distinguidos por frontmatter (`type: watcher`).

### 9.6 Validación automatizada

**Qué sería**: un script `scripts/validate.py` que verifique:
- Cada entry de `marketplace.json` tiene un `source` que existe.
- Cada `plugin.json` tiene una `version` semver válida.
- Cada skill listada en `plugin.json` tiene un `SKILL.md` en disco.
- Cada id en `<plugin>/.mcp.json` existe en `mcp_servers.json`.
- Cada id en `<plugin>/agent_tools.json` existe en `agent_tools.json`.

**Estado**: **no implementado todavía**. La validación hoy es manual (ver §10). La lógica es sencilla y es candidata natural para ser el primer script que se agregue cuando se decida meter `scripts/` al repo.

---

## 10. Validación manual (lo que se hace hoy)

Mientras no exista `validate.py`, la validación cruzada se hace con un script ad-hoc. Resultado de la última corrida sobre este repo:

```
=== ERRORS ===   (none)
=== WARNINGS === (none)
=== OK (8) ===
  + [commercial-legal] source dir exists: ./commercial-legal
  + [commercial-legal] manifest name matches
  + [commercial-legal] skill 'nda-review' -> SKILL.md exists
  + [commercial-legal] MCP ref 'io.gravitonai.courtlistener' -> found
  + [commercial-legal] MCP ref 'io.gravitonai.gdrive' -> found
  + [commercial-legal] tool ref 'io.gravitonai.tools.read_document' -> found
  + [commercial-legal] tool ref 'io.gravitonai.tools.draft_markdown' -> found
  + [commercial-legal] tool ref 'io.gravitonai.tools.escalate_to_attorney' -> found
```

Cuando agregues un plugin o skill, el flujo mínimo de validación es:
1. `python3 -c "import json; json.load(open('marketplace.json'))"` y análogos.
2. Confirmar visualmente que todo id referenciado en un plugin existe en su catálogo global.
3. Si algo no cuadra, **no commitear** hasta arreglar.

---

## 11. Catálogos globales — una sola fuente de verdad

Regla de oro: **definir una vez, referenciar por id**.

| Cosa | Dónde se define | Dónde se referencia |
|---|---|---|
| Servidor MCP | `mcp_servers.json` (raíz) | `<plugin>/.mcp.json` |
| Tool | `agent_tools.json` (raíz) | `<plugin>/agent_tools.json` |

**Por qué**: si dos plugins necesitan el mismo servidor MCP (ej: CourtListener), solo se define una vez. Cambiar la URL o el método de auth es un solo cambio. Si un plugin necesita un server que no existe, primero se agrega al catálogo y luego se referencia.

**Convención de IDs**:
- Servidores: `io.gravitonai.<categoría>.<nombre>` → `io.gravitonai.courtlistener`.
- Tools: `io.gravitonai.tools.<nombre>` → `io.gravitonai.tools.read_document`.

---

## 12. Convenciones

- **Idioma**: todo el contenido en español. Comandos y nombres técnicos en inglés.
- **Tono**: profesional, claro, sin jerga innecesaria. Cero emojis salvo que el usuario los pida.
- **Nombres**: kebab-case para archivos y skills (`nda-review`, `nda-clause-checklist.md`).
- **Sin secretos en el repo**: nunca. `.env`, `*.local.md`, `drafts/`, `private/`.
- **Marcadores de edición**: `<!-- EDITAR PARA TU EQUIPO: ... -->` en secciones que cada equipo debe personalizar.
- **DRAFT por defecto**: cualquier output que toque temas legales / regulatorios / fiscales / privacidad lleva el header `> DRAFT — para revisión por un abogado. No constituye asesoría legal.`

---

## 13. Cómo agregar un plugin nuevo

1. **Crear la carpeta**: `mkdir mi-plugin/`.
2. **Crear el manifest** en `mi-plugin/.claude-plugin/plugin.json` con `name`, `version`, `description`, `author`, y `skills: []` (vacío por ahora; se llena en el paso 7).
3. **Registrar el plugin** en `.claude-plugin/marketplace.json` agregando una entry a `plugins[]` con `name`, `source: "./mi-plugin"`, `version`, `description`.
4. **Identificar dependencias**:
   - ¿Necesita servers MCP nuevos? → agregarlos primero a `mcp_servers.json` raíz.
   - ¿Necesita tools nuevos? → agregarlos primero a `agent_tools.json` raíz.
5. **Crear `mi-plugin/.mcp.json`** listando los IDs de servers que consume.
6. **Crear `mi-plugin/agent_tools.json`** listando los IDs de tools que consume.
7. **Escribir el playbook** en `mi-plugin/CLAUDE.md` con tono, defaults, escalación y guardrails del dominio.
8. **Escribir la documentación** en `mi-plugin/README.md`.
9. **Agregar al menos una skill** en `mi-plugin/skills/<nombre>/SKILL.md`.
10. **Actualizar** el array `skills` en el `plugin.json` con el nombre de la nueva skill.
11. **Validar**: confirmar que todos los IDs referenciados en `.mcp.json` y `agent_tools.json` existen en los catálogos globales.

---

## 14. Cómo agregar una skill nueva

1. **Crear la carpeta**: `mkdir -p mi-plugin/skills/<skill-name>/`.
2. **Escribir `SKILL.md`** con frontmatter (`description`, `when_to_use`, `inputs`, `outputs`, `references`, `assets`) y el procedimiento completo: guardrails, pasos, formato de salida, escalación.
3. **Agregar contexto** en `skills/<skill>/references/` si la skill necesita material referencial (checklists, matrices, glosarios).
4. **Agregar plantillas** en `skills/<skill>/assets/` si la skill produce documentos estructurados.
5. **(Opcional, futuro)** Si la skill necesita ejecutar código, crear `skills/<skill>/scripts/` con los scripts. Por ahora este directorio no se usa en el ejemplo.
6. **Actualizar** el array `skills` en `mi-plugin/.claude-plugin/plugin.json`.
7. **Documentar** la skill en `mi-plugin/README.md` con: nombre, descripción de una línea, ejemplo de invocación, qué no hace.
8. **Validar** que el nombre de la skill es kebab-case y único dentro del plugin.

---

## 15. Versionado

**Semver** (`MAJOR.MINOR.PATCH`) en:
- Cada entry de `marketplace.json` (`version`).
- Cada `plugin.json` (`version`).
- Cada server del catálogo global (`version`).
- Cada tool del catálogo global (`version`).

**Reglas de bump**:
- **MAJOR**: cambios incompatibles con plugins/skills existentes (campo eliminado, schema que rompe consumidores, default que cambia de significado).
- **MINOR**: nuevo server/tool agregable, nueva skill, nueva capability que no rompe nada.
- **PATCH**: fix de descripción, typo, tag, link roto.

Cuando un catálogo global cambia de manera incompatible, **todos** los plugins que referencian los items afectados deben bumpear su MAJOR en el siguiente ciclo.

---

## 16. Guardrails uniformes

Aplican a **todos** los plugins y skills. Viven en `CLAUDE.md` raíz y se resumen aquí:

1. **Borrador, no consejo.** Output jurídico / regulatorio / fiscal / privacidad lleva header `DRAFT — para revisión por un abogado`.
2. **Atribución.** Toda cita a jurisprudencia, regulación o doctrina lleva fuente enlazada. Sin research tool conectado → `[verificar]`.
3. **Defaults conservadores.** En llamadas subjetivas, elegir la posición más conservadora. Marcar asunción de jurisdicción.
4. **Gates.** Nada de `file`, `send`, `commit`, `delete`, `escalate` sin confirmación explícita.
5. **Privacidad.** Nombres reales, datos de clientes y secretos **nunca** en ejemplos, fixtures o commits. Placeholders: `Acme Corp.`, `Juan Pérez`, `confidencial-ejemplo`.

---

## 17. Plugins incluidos

### `commercial-legal` (v0.1.0)

Plugin de ejemplo. Cubre flujos legales transaccionales comerciales: revisión de NDAs, MSAs, SaaS, escalación a abogado. Triage automático VERDE/AMARILLO/ROJO contra el playbook del equipo.

**Skills incluidas**:
- `nda-review`: triage de NDAs entrantes con output VERDE/AMARILLO/ROJO + memo para abogado.

**MCP servers referenciados**: `io.gravitonai.courtlistener` (opcional), `io.gravitonai.gdrive` (requerido).
**Tools referenciadas**: `io.gravitonai.tools.read_document`, `io.gravitonai.tools.draft_markdown`, `io.gravitonai.tools.escalate_to_attorney`.

Ver `commercial-legal/README.md` para detalle completo.

---

## 18. Estado y roadmap

**Estado actual**:
- 1 plugin (`commercial-legal`), 1 skill (`nda-review`).
- Catálogos globales poblados con 5 servers y 5 tools de ejemplo (no exhaustivos).
- Validación manual cruzada (ver §10). Sin `validate.py` automatizado todavía.
- Sin CI workflows, sin `LICENSE`, sin `CONTRIBUTING.md`, sin `QUICKSTART.md` — no son necesarios en esta fase.
- Sin `scripts/`, `agents/`, `hooks/`, comandos formales, ni subagentes — la estructura los reserva, no los implementa.

**Próximos pasos naturales** (no comprometidos):
1. **Validación automatizada**: agregar `scripts/validate.py` con la lógica de §10.
2. **CI mínimo**: un workflow en `.github/workflows/` que corra el validador en cada PR.
3. **Más skills en `commercial-legal`**: `msa-review`, `saas-subscription-review`, `amendment-tracer` (cada una con su SKILL.md + references + assets).
4. **Más plugins verticales**: `privacy-legal`, `ip-legal`, `litigation-legal`, copiando el shape de `commercial-legal/`.
5. **Catálogos más completos**: llenar `mcp_servers.json` y `agent_tools.json` con todos los servers y tools que el equipo usa en producción.
6. **Agents programados**: decidir dónde y cómo viven los watchers / monitors. Probablemente en `<plugin>/agents/` con frontmatter de schedule.
7. **Hooks**: decidir qué eventos necesitan hooks (pre-tool para redacción de PII, post-tool para logging).
8. **Subagentes**: definir el mecanismo de delegación entre skills.

**Mantenido por GravitonAI.** Para preguntas, abrir issue en el repo.
