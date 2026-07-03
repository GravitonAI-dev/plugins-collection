# historical-drafting

Plugin de Claude para la produccion de borradores de resumenes y analisis estructurados sobre eventos historicos, con trazabilidad de fuentes y separacion explicita entre hecho documentado e interpretacion. Pensado para investigadores en general que necesitan un punto de partida verificable.

> **Borrador, no verdad historiografica definitiva.** Todo output de este plugin es para revision humana. No sustituye revision por pares ni validacion academica. Ver `CLAUDE.md` raiz para guardrails uniformes.

## Que hace

- Genera borradores de resumenes estructurados sobre eventos historicos concretos a partir de la consulta del usuario.
- Produce borradores de analisis que distinguen explicitamente entre **hechos documentados** e **interpretacion**.
- Cita fuentes en cada afirmacion factual. Marcador `[verificar]` cuando no hay fuente trazable.
- Aplica una matriz de veredicto VERDE/AMARILLO/ROJO a cada bloque de hechos para guiar la revision humana.
- Permite al investigador remontar cada afirmacion del output a su fuente sin volver a preguntar al agente.

## Que NO hace

- No emite verdades historiograficas definitivas. Todo output es borrador para revision humana.
- No sustituye revision por pares ni publicacion academica.
- No inventa fechas, cifras, nombres ni citas. Si un dato es incierto, lo marca `[verificar]` o lo excluye.
- No accede a archives fisicos. Las fuentes asumidas son localizables digitalmente.
- No aplica categorias o instituciones modernas a eventos historicos si no existian en su epoca (sin anacronismos).
- No cubre todas las geografias ni epocas. Esta primera implementacion incluye solo historia de Venezuela. Otras regiones requeriran skills adicionales.

## Skills incluidas

| Skill | Descripcion | Invocacion |
|---|---|---|
| `venezuela-history` | Investigacion especializada en historia de Venezuela: borradores de resumenes y analisis verificables | `/historical-drafting:venezuela-history` |

Ver detalle en `skills/venezuela-history/SKILL.md`.

## Dependencias

### Servidores MCP (referenciados en `.mcp.json`)

Ninguno. El plugin opera sin conexiones externas a sistemas del orquestador.

### Tools (referenciados en `agent_tools.json`)

| ID | Requerido | Proposito |
|---|---|---|
| `io.gravitonai.tools.web_search` | No | Buscar fuentes y verificacion de hechos en la web abierta |
| `io.gravitonai.tools.read_document` | No | Leer documentos de fuentes (URL o path local) |
| `io.gravitonai.tools.draft_markdown` | No | Generar el borrador en markdown a partir de la plantilla |

Las tres tools son **opcionales**. Si no estan disponibles, la skill degrada con marcadores `[verificar]` y produce un borrador mas conservador.

## Como instalar

### En Claude Code

```
# Agregar el marketplace (apuntar a la raiz de este repo)
/plugin marketplace add /ruta/a/plugins-collection

# Instalar el plugin
/plugin install historical-drafting@plugins-collection

# Reiniciar Claude Code

# Ejecutar la primera investigacion
/historical-drafting:venezuela-history
```

### En Claude Cowork

1. Abrir el tab Cowork.
2. Click en "Customize" en el sidebar.
3. Click en "Browse plugins" o subir el `.zip` de la carpeta `historical-drafting/`.
4. Habilitar la skill `venezuela-history`.

## Como tunear el plugin

1. **Editar el playbook**: `historical-drafting/CLAUDE.md` tiene marcadores `<!-- EDITAR PARA TU EQUIPO -->` en jurisdiccion, defaults y matriz de escalacion. Ajustar segun el equipo.
2. **Cambiar la jurisdiccion/periodo por defecto**: editar la seccion "Jurisdiccion por defecto" en el `CLAUDE.md` del plugin.
3. **Ajustar el estandar de citacion**: editar la seccion "Defaults" en el `CLAUDE.md`.
4. **Agregar MCP servers**: si el plugin necesita un servidor nuevo, agregarlo primero a `mcp_servers.json` raiz y luego referenciarlo en `historical-drafting/.mcp.json`.
5. **Agregar tools**: igual, primero al catalogo global `agent_tools.json`, luego al `agent_tools.json` del plugin.
6. **Agregar skills**: copiar la estructura de `skills/venezuela-history/` a `skills/<nueva-skill>/` y escribir el `SKILL.md` con el procedimiento.
7. **Actualizar la version**: bumpear `version` en `historical-drafting/.claude-plugin/plugin.json` y en el entry de `.claude-plugin/marketplace.json` (semver).

## Estructura del plugin

```
historical-drafting/
  .claude-plugin/
    plugin.json            # manifest
  .mcp.json                # MCP servers que consume (vacio en esta version)
  agent_tools.json         # tools que consume
  CLAUDE.md                # playbook del plugin
  README.md                # este archivo
  skills/
    venezuela-history/
      SKILL.md             # procedimiento
      references/          # (opcional) material de contexto
      assets/              # (opcional) plantillas de output
```

## Mantenimiento

- Propietario: GravitonAI.
- Issues: abrir ticket en el repo.
- Cambios incompatibles: bump MAJOR en `plugin.json` + en entry de `marketplace.json`.