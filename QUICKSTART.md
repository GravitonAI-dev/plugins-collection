# QUICKSTART — Crear un plugin y una skill desde cero

> Esto es lo mínimo que necesitas para crear tu primer plugin funcional.
> Sin MCP, sin tools externas, sin references, sin assets.
> Solo el plugin, su playbook y una skill básica.

---

## 1. ¿Qué vas a crear?

Un **plugin** es una carpeta que contiene todo lo que el agente necesita para trabajar en un dominio específico (ej: revisión legal, privacidad, ventas).

Dentro del plugin hay **skills** — procedimientos que el agente sabe ejecutar.

```
mi-plugin/                         ← tu plugin
 ├─ .claude-plugin/
 │    └─ plugin.json              ← identidad del plugin
 ├─ CLAUDE.md                      ← playbook (cómo se comporta el agente)
 ├─ README.md                     ← documentación
 └─ skills/
      └─ mi-skill/                ← tu skill
           └─ SKILL.md            ← procedimiento de la skill
```

Eso es todo.

---

## 2. Crear la estructura del plugin

```bash
mkdir -p mi-plugin/.claude-plugin
mkdir -p mi-plugin/skills/mi-skill
```

---

## 3. Crear plugin.json

Archivo: `mi-plugin/.claude-plugin/plugin.json`

```json
{
  "name": "mi-plugin",
  "version": "0.1.0",
  "description": "Descripción breve de qué hace este plugin.",
  "author": { "name": "Tu Nombre" },
  "skills": ["mi-skill"]
}
```

---

## 4. Crear el playbook (CLAUDE.md del plugin)

Archivo: `mi-plugin/CLAUDE.md`

```markdown
# CLAUDE.md — mi-plugin

> Playbook del plugin. Define cómo se comporta el agente en este dominio.
> Las reglas de aquí solo pueden estrechar las del CLAUDE.md raíz, nunca relajarlas.

## Propósito

[Qué hace este plugin y para quién.]

## Tono y estilo

[Profesional, claro. Cómo se expresan los resultados.]

## Defaults

[Qué se asume si el usuario no lo dice. Ej: "si no se especifica el plazo, asumir 2 años."]

## Matriz de escalación

| Veredicto | Acción |
|---|---|
| VERDE | Auto-aprobado. |
| AMARILLO | Revisión por abogado. |
| ROJO | Escalar a abogado inmediatamente. |

## Skills incluidas

- `mi-skill` — [descripción de una línea]

## Limitaciones

[Qué NO hace este plugin.]
```

---

## 5. Crear README.md del plugin

Archivo: `mi-plugin/README.md`

```markdown
# mi-plugin

Descripción de una línea de qué hace.

## Qué hace

[Descripción más detallada.]

## Qué no hace

[Lo que está fuera de su alcance.]

## Skills

- `mi-skill` — [descripción]
```

---

## 6. Crear la skill (SKILL.md)

Esta es la parte más importante. El archivo `SKILL.md` tiene dos partes: el **frontmatter** (metadatos) y el **cuerpo** (procedimiento).

Archivo: `mi-plugin/skills/mi-skill/SKILL.md`

### 6a. Frontmatter (obligatorio)

```yaml
---
name: mi-skill
description: Descripción de una línea de cuándo usar esta skill. Termina con "NO usar para...".
---
```

**Reglas del frontmatter**:
- `name`: el nombre de la skill en kebab-case (guiones, sin espacios).
- `description`: **una sola línea corrida**. Lo que el agente lee para decidir cuándo invocar la skill. Termina siempre con "NO usar para..." para evitar invocaciones incorrectas.

### 6b. Cuerpo del SKILL.md

```markdown
# mi-skill

[Breve descripción de qué hace esta skill.]

> **DRAFT — para revisión por un abogado. No constituye asesoría legal.**

## Guardrails

1. [Tu primer guardrail específico.]
2. [Tu segundo guardrail específico.]

## Procedimiento

1. [Paso 1 — qué hace el agente]
2. [Paso 2 — qué hace el agente]
3. [Paso 3 — qué hace el agente]

## Formato de salida

[Describe qué produce la skill: un memo, un veredicto, una recomendación, etc.]

## Escalación

[Cuándo escalar a un humano o abogado.]
```

---

## 7. Registrar el plugin en marketplace.json

En `.claude-plugin/marketplace.json` raíz, agregar al array `plugins[]`:

```json
{
  "name": "mi-plugin",
  "displayName": "Mi Plugin",
  "source": "./mi-plugin",
  "version": "0.1.0",
  "description": "Descripción breve.",
  "author": { "name": "Tu Nombre" }
}
```

---

## 8. Checklist final

Antes de commitear, verifica:

- [ ] `mi-plugin/.claude-plugin/plugin.json` existe y tiene `version`.
- [ ] `mi-plugin/CLAUDE.md` existe.
- [ ] `mi-plugin/skills/mi-skill/SKILL.md` existe con frontmatter (`name` + `description`).
- [ ] El array `skills` en `plugin.json` incluye `"mi-skill"`.
- [ ] `marketplace.json` tiene la entry de `mi-plugin`.
- [ ] El nombre de la skill está en **kebab-case** (`mi-skill`, no `miSkill` ni `mi_skill`).

---

## 9. Estructura final

Tu plugin queda así:

```
mi-plugin/
 ├─ .claude-plugin/
 │    └─ plugin.json
 ├─ CLAUDE.md
 ├─ README.md
 └─ skills/
      └─ mi-skill/
           └─ SKILL.md
```

Eso es todo lo que necesitas para un plugin funcional con una skill básica.

---

## 10. Próximos pasos

- **commercial-legal/** — Plugin de ejemplo para ver cómo queda un plugin completo.
- **README.md §13** — Procedimiento completo de cómo agregar un plugin (referencia).
- **README.md §14** — Procedimiento completo de cómo agregar una skill (referencia).

---

**Mantenido por GravitonAI.**
