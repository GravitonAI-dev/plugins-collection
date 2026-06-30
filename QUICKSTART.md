# QUICKSTART — Crear o editar plugins y skills

> Como arrancar el proceso asistido de creacion o edicion de plugins y skills de este repositorio.

---

## 1. Lo unico que necesitas

- Acceso a Claude (Code, Cowork, o cualquier LLM con contexto largo).
- El archivo `plugin-builder.md` de la raiz de este repo (ya existe).

No necesitas instalar nada, no necesitas scripts, no necesitas conocimiento previo del repo. El builder se encarga de leer los catalogos, validar referencias y respetar las convenciones.

---

## 2. Arrancar la sesion

1. Abre Claude.
2. Adjunta o pega el contenido de `plugin-builder.md` como contexto inicial de la conversacion.
3. Escribe un mensaje como:

```
Sigue las instrucciones de plugin-builder.md y arranca una sesion de scaffolding.
```

Claude adoptara el rol del Plugin & Skill Builder y te hara la primera pregunta: que modo quieres usar.

---

## 3. Los cuatro modos

| Modo | Lo que hace | Cuando usarlo |
|---|---|---|
| **A** | Crear un plugin nuevo de cero a registrado en `marketplace.json` | Cuando tienes un dominio vertical nuevo (ej: `privacy-legal`, `healthcare-compliance`). |
| **B** | Crear una skill nueva dentro de un plugin existente | Cuando quieres agregar una capacidad a un plugin que ya existe. |
| **C** | Editar un plugin existente (agregar/quitar archivos, modificar contenido) | Cuando un plugin necesita ajustes despues de creado. |
| **D** | Editar una skill existente | Cuando una skill necesita cambios en su SKILL.md, references o assets. |

Responde con la letra. El builder te guia paso a paso desde ahi.

---

## 4. Como es una sesion tipica

1. **Discovery**. El builder te hace preguntas **una por una** (nombre, dominio, audiencia, dependencias, etc.). Responde cada una antes de pasar a la siguiente.
2. **Plan global**. Antes de escribir nada, el builder te presenta el arbol de archivos a crear/modificar con contenido tentativo. Te pide **OK** antes de continuar.
3. **Ejecucion**. Tras el OK, escribe los archivos **uno por uno**, mostrandote el contenido completo y pidiendo confirmacion antes de cada `write`.
4. **Validacion**. Al final corre un checklist (IDs en catalogos, kebab-case, semver, DRAFT header). Si algo falla, propone el fix concreto y espera confirmacion.
5. **Cierre**. Resumen de archivos creados/modificados, IDs pendientes en catalogos globales (si los hubo), sugerencias de version bump.

El builder **nunca** escribe un archivo sin tu confirmacion previa.

---

## 5. Lo que el builder NO hace

- **Borrar archivos.** Si quieres quitar algo, lo hace `rm -rf` manual fuera de la sesion.
- **Commitear, pushear, abrir PR.** Esas acciones quedan fuera del builder.
- **Definir servidores MCP ni tools nuevos.** Solo puedes elegir de los catalogos globales (`mcp_servers.json` y `agent_tools.json` en la raiz del repo). Si necesitas un id nuevo, queda como pendiente para que el equipo de desarrollo del orquestador lo agregue al catalogo fuera de esta sesion.
- **Implementar `agents/` programados ni `hooks/`.** Esos elementos quedan vacios en esta fase y no se consultan.
- **Dar opinion legal, fiscal, medica o financiera.** Para eso usa el plugin correspondiente (`commercial-legal`, `general-assistant`, etc.).

---

## 6. Despues de la sesion

- Revisa el resumen que entrega el builder.
- Si quedaron **IDs pendientes** en los catalogos globales, abre ticket al equipo de desarrollo del orquestador para que los agregue a `mcp_servers.json` o `agent_tools.json` raiz.
- Si agregaste o modificaste plugins/skills, bumpea la version en `plugin.json` y en `marketplace.json` segun semver:
  - **MAJOR**: cambios incompatibles (schema que rompe, default que cambia).
  - **MINOR**: skills nuevas o capabilities additive.
  - **PATCH**: fixes descriptivos, typos, ajustes menores.
- Cuando exista `scripts/validate.py` (proxima fase), correlo para automatizar las validaciones.

---

## 7. Para profundizar

| Recurso | Que hay |
|---|---|
| `plugin-builder.md` | System prompt completo del builder. Lo lee el LLM al arrancar la sesion. |
| `README.md` | Estructura completa del repo, todas las convenciones, como agregar plugins y skills a mano. |
| `.claude-plugin/marketplace.json` | El registro de plugins disponibles. |
| `commercial-legal/` y `general-assistant/` | Plugins de ejemplo para ver la estructura en uso. |

---

**Mantenido por GravitonAI.**