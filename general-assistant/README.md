# general-assistant

Plugin de proposito general. Atiende consultas que requieren informacion publica, hechos actuales, contexto externo o verificacion. Cubre el caso "no se que plugin usar" — cuando la consulta no encaja claramente en un vertical, este plugin es el fallback.

> Todo output de este plugin es una respuesta directa, **no** un borrador legal, fiscal ni medico. Para temas verticales, usar el plugin correspondiente.

## Que hace

- Responde consultas generales del usuario que requieren informacion publica.
- Decide por turno si necesita invocar `io.gravitonai.tools.web_search` o basta con conocimiento general.
- Sintetiza la respuesta con atribucion (URL visible por fuente usada).
- Marca `[verificar]` cualquier claim factual que no pueda confirmar con una fuente.

## Que NO hace

- **No revisa contratos.** Para NDAs, MSAs, suscripciones SaaS y similares, usar `commercial-legal`.
- **No da opinion legal, fiscal, medica ni financiera.** Esas consultas se derivan al plugin vertical correspondiente o a un profesional humano. Marca como `[verificar]`.
- **No accede a datos internos del usuario** (documentos adjuntos, RAG privado, bases de la empresa). Solo informacion publica de la web.
- **No es un agente de tareas.** No envia emails, no crea tickets, no escribe en calendarios. Para eso estan otros plugins.
- **No escala a humanos.** Este plugin no es un flujo de aprobacion; responde o deriva.

## Skills incluidas

| Skill | Descripcion | Invocacion |
|---|---|---|
| `general-query` | Atender una consulta general, decidiendo si invocar `io.gravitonai.tools.web_search` y sintetizando la respuesta con atribucion. | `/general-assistant:general-query` |

Ver detalle en `skills/general-query/SKILL.md`.

## Dependencias

### Servidores MCP (referenciados en `.mcp.json`)

Ninguno. El plugin opera exclusivamente con la tool `io.gravitonai.tools.web_search`, que se ejecuta in-process.

### Tools (referenciadas en `agent_tools.json`)

| ID | Requerido | Proposito |
|---|---|---|
| `io.gravitonai.tools.web_search` | Si | Recuperar informacion publica actual cuando la consulta parece requerir datos externos. |

Si `web_search` no esta disponible, la skill degrada con gracia: responde solo con conocimiento general y marca `[verificar]` en claims factuales.

## Como instalar

### En Claude Code

```
# Agregar el marketplace (apuntar a la raiz de este repo)
/plugin marketplace add /ruta/a/plugins-collection

# Instalar el plugin
/plugin install general-assistant@plugins-collection

# Reiniciar Claude Code

# Hacer una consulta general
/general-assistant:general-query
```

### En Claude Cowork

1. Abrir el tab Cowork.
2. Click en "Customize" en el sidebar.
3. Click en "Browse plugins" o subir el `.zip` de la carpeta `general-assistant/`.
4. Habilitar la skill `general-query`.

## Como tunear el plugin

1. **Editar el playbook**: `general-assistant/CLAUDE.md` tiene marcadores `<!-- EDITAR PARA TU EQUIPO -->` en la seccion "Defaults" y en la "Matriz de escalacion". Ajustar segun el equipo.
2. **Anadir mas tools**: si el plugin necesita otra tool (p. ej. `io.gravitonai.tools.read_document` para documentos locales), agregarla primero al catalogo global `agent_tools.json` raiz y luego referenciarla en `general-assistant/agent_tools.json`.
3. **Anadir mas skills**: copiar la estructura de `skills/general-query/` a `skills/<nueva-skill>/` y escribir el `SKILL.md` con el procedimiento. Actualizar el array `skills` en `plugin.json`.
4. **Actualizar la version**: bumpear `version` en `general-assistant/.claude-plugin/plugin.json` y en el entry de `.claude-plugin/marketplace.json` (semver).

## Estructura del plugin

```
general-assistant/
  .claude-plugin/
    plugin.json                                   # manifest
  .mcp.json                                       # MCP servers que consume (vacio en esta version)
  agent_tools.json                                # tools que consume
  CLAUDE.md                                       # playbook del plugin
  README.md                                       # este archivo
  skills/
    general-query/
      SKILL.md                                    # procedimiento
      references/
        source-attribution-conventions.md         # como citar fuentes
      assets/
        answer-output-template.md                 # plantilla de output
```

## Mantenimiento

- Propietario: GravitonAI.
- Issues: abrir ticket en el repo.
- Cambios incompatibles: bump MAJOR en `plugin.json` + en entry de `marketplace.json`.
