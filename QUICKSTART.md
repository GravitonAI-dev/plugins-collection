# QUICKSTART — Crear o editar plugins y skills

> Como arrancar el proceso asistido de creación o edición de plugins y skills de este repositorio.

---

## 1. Lo único que necesitas

- Acceso a Claude (Code, Cowork, o cualquier LLM con contexto largo).
- El archivo `plugin-builder.md` de la raíz de este repo (ya existe).

No necesitas instalar nada, no necesitas scripts, no necesitas conocimiento previo del repo. El builder se encarga de leer los catálogos, validar referencias y respetar las convenciones.

---

## 2. Arrancar la sesión

1. Abre Claude.
2. Adjunta o pega el contenido de `plugin-builder.md` como contexto inicial de la conversación.
3. Escribe un mensaje como:

```
Sigue las instrucciones de plugin-builder.md y arranca una sesión de scaffolding.
```

Claude adoptará el rol del Plugin & Skill Builder y te hará la primera pregunta: qué modo quieres usar.

---

## 3. Los cuatro modos

| Modo | Lo que hace | Cuándo usarlo |
|---|---|---|
| **A** | Crear un plugin nuevo de cero a registrado en `marketplace.json` | Cuando tienes un dominio vertical nuevo (ej: `privacy-legal`, `healthcare-compliance`). |
| **B** | Crear una skill nueva dentro de un plugin existente | Cuando quieres agregar una capacidad a un plugin que ya existe. |
| **C** | Editar un plugin existente (agregar/quitar archivos, modificar contenido) | Cuando un plugin necesita ajustes después de creado. |
| **D** | Editar una skill existente | Cuando una skill necesita cambios en su SKILL.md, references o assets. |

Responde con la letra. El builder te guía paso a paso desde ahí.

---

## 4. Como es una sesión típica

1. **Discovery**. El builder te hace preguntas **una por una** (nombre, dominio, audiencia, dependencias, etc.). Responde cada una antes de pasar a la siguiente.
2. **Plan global**. Antes de escribir nada, el builder te presenta el árbol de archivos a crear/modificar con contenido tentativo. Te pide **OK** antes de continuar.
3. **Ejecución**. Tras el OK, escribe los archivos **uno por uno**, mostrándote el contenido completo y pidiendo confirmación antes de cada `write`.
4. **Validación**. Al final corre un checklist (IDs en catálogos, kebab-case, semver, DRAFT header). Si algo falla, propone el fix concreto y espera confirmación.
5. **Cierre**. Resumen de archivos creados/modificados, IDs pendientes en catálogos globales (si los hubo), sugerencias de versión bump.

El builder **nunca** escribe un archivo sin tu confirmación previa.

---

## 5. Lo que el builder NO hace

- **Borrar archivos.** Si quieres quitar algo, lo hace `rm -rf` manual fuera de la sesión.
- **Commitear, pushear, abrir PR.** Esas acciones quedan fuera del builder.
- **Definir servidores MCP ni tools nuevos.** Solo puedes elegir de los catálogos globales (`mcp_servers.json` y `agent_tools.json` en la raíz del repo). Si necesitas un id nuevo, queda como pendiente para que el equipo de desarrollo del orquestador lo agregue al catálogo fuera de esta sesión.
- **Implementar `agents/` programados ni `hooks/`.** Esos elementos quedan vacíos en esta fase y no se consultan.
- **Dar opinión legal, fiscal, médica o financiera.** Para eso usa el plugin especializado correspondiente (`derecho-civil`, `gestoria`, etc.).

---

## 6. Después de la sesión

- Revisa el resumen que entrega el builder.
- Si quedaron **IDs pendientes** en los catálogos globales, abre ticket al equipo de desarrollo del orquestador para que los agregue a `mcp_servers.json` o `agent_tools.json` raíz.
- Si agregaste o modificaste plugins/skills, bumpea la versión en `plugin.json` y en `marketplace.json` según semver:
  - **MAJOR**: cambios incompatibles (schema que rompe, default que cambia).
  - **MINOR**: skills nuevas o capabilities additive.
  - **PATCH**: fixes descriptivos, typos, ajustes menores.
- Antes de subir, pasa el control de calidad obligatorio de la sección 10 del `README.md` (control automático, `/simplify`, `/code-review` y marca de revisado): el hook corta el push de lo que no esté marcado.

---

## 7. Para profundizar

| Recurso | Qué hay |
|---|---|
| `plugin-builder.md` | System prompt completo del builder. Lo lee el LLM al arrancar la sesión. |
| `README.md` | Estructura completa del repo, todas las convenciones, como agregar plugins y skills a mano. |
| `.claude-plugin/marketplace.json` | El registro de plugins disponibles. |
| `derecho-civil/`, `gestoria/`, `asistente-general/` y `gestion-plantillas/` | Plugins del repositorio para ver la estructura en uso. |

---

**Mantenido por GravitonAI.**
