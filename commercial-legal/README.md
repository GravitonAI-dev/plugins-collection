# commercial-legal

Plugin de Claude para revision de acuerdos comerciales: NDAs, NDAs mutuos, suscripciones SaaS, enmiendas menores. Produce borradores con triage automatico VERDE/AMARILLO/ROJO que un abogado revisa antes de cualquier firma.

> **Borrador, no opinion legal.** Todo output de este plugin es para revision por un abogado. No es asesoria legal. Ver `CLAUDE.md` raiz para guardrails uniformes.

## Que hace

- Triage de NDAs entrantes: clasifica cada NDA como VERDE (auto-aprobable), AMARILLO (requiere revision) o ROJO (escalar a abogado).
- Memo estructurado con issues flagged, base legal y recomendacion.
- Escalacion estructurada al abogado responsable cuando el veredicto es ROJO.

## Que NO hace

- No firma NDAs. No envia NDAs a contrapartes. No los sube a DocuSign.
- No revisa MSAs, acuerdos de socios, term sheets ni contratos de M&A. Esos iran en plugins separados.
- No da opinion legal final. Recomienda consulta con abogado en todo caso AMARILLO/ROJO.
- No opera sobre PDFs escaneados sin OCR. Contratos en idiomas distintos al ingles se marcan como AMARILLO y se derivan.
- No conoce jurisprudencia por si solo. Si necesita verificar un precedente, conecte un research tool (CourtListener) — si no, las citaciones se marcan `[verificar]`.

## Skills incluidas

| Skill | Descripcion | Invocacion |
|---|---|---|
| `nda-review` | Triage de NDAs entrantes con output VERDE/AMARILLO/ROJO + memo | `/commercial-legal:nda-review` |

Ver detalle en `skills/nda-review/SKILL.md`.

## Dependencias

### Servidores MCP (referenciados en `.mcp.json`)

| ID | Nombre | Requerido | Proposito |
|---|---|---|---|
| `io.gravitonai.courtlistener` | CourtListener | No | Verificar jurisprudencia cuando hay clausulas atipicas |
| `io.gravitonai.gdrive` | Google Drive | Si | Leer NDAs subidos como documentos de Drive |

Si CourtListener no esta conectado, las citaciones a precedentes se marcan `[verificar]` y el triage sigue funcionando.

### Tools (referenciados en `agent_tools.json`)

| ID | Requerido | Proposito |
|---|---|---|
| `io.gravitonai.tools.read_document` | Si | Leer el NDA desde su ubicacion |
| `io.gravitonai.tools.draft_markdown` | Si | Generar el memo de triage |
| `io.gravitonai.tools.escalate_to_attorney` | Si | Crear ticket de escalacion para casos ROJO |

## Como instalar

### En Claude Code

```
# Agregar el marketplace (apuntar a la raiz de este repo)
/plugin marketplace add /ruta/a/plugins-collection

# Instalar el plugin
/plugin install commercial-legal@plugins-collection

# Reiniciar Claude Code

# Ejecutar el primer triage
/commercial-legal:nda-review
```

### En Claude Cowork

1. Abrir el tab Cowork.
2. Click en "Customize" en el sidebar.
3. Click en "Browse plugins" o subir el `.zip` de la carpeta `commercial-legal/`.
4. Habilitar la skill `nda-review`.

## Como tunear el plugin

1. **Editar el playbook**: `commercial-legal/CLAUDE.md` tiene marcadores `<!-- EDITAR PARA TU EQUIPO -->` en jurisdiccion, defaults y matriz de escalacion. Ajustar segun el equipo.
2. **Cambiar jurisdiccion por defecto**: editar la seccion "Jurisdiccion por defecto" en el `CLAUDE.md` del plugin.
3. **Agregar MCP servers**: si el plugin necesita un servidor nuevo, agregarlo primero a `mcp_servers.json` raiz y luego referenciarlo en `commercial-legal/.mcp.json`.
4. **Agregar tools**: igual, primero al catalogo global `agent_tools.json`, luego al `agent_tools.json` del plugin.
5. **Agregar skills**: copiar la estructura de `skills/nda-review/` a `skills/<nueva-skill>/` y escribir el `SKILL.md` con el procedimiento.
6. **Actualizar la version**: bumpear `version` en `commercial-legal/.claude-plugin/plugin.json` y en el entry de `.claude-plugin/marketplace.json` (semver).

## Estructura del plugin

```
commercial-legal/
  .claude-plugin/
    plugin.json            # manifest
  .mcp.json                # MCP servers que consume
  agent_tools.json         # tools que consume
  CLAUDE.md                # playbook del plugin
  README.md                # este archivo
  skills/
    nda-review/
      SKILL.md             # procedimiento
      references/
        nda-clause-checklist.md
      assets/
        nda-triage-output-template.md
```

## Mantenimiento

- Propietario: GravitonAI.
- Issues: abrir ticket en el repo.
- Cambios incompatibles: bump MAJOR en `plugin.json` + en entry de `marketplace.json`.
