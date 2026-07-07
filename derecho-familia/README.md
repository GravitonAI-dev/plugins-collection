# Derecho de Familia

Plugin de GravitonAI para la generacion de documentos de derecho de familia espanol, verificando siempre la version consolidada vigente en el BOE: separacion y divorcio de mutuo acuerdo, medidas sobre los hijos, regimen economico matrimonial y parejas de hecho.

---

## Que hace

- Genera el convenio regulador de separacion o divorcio de mutuo acuerdo (art. 90 CC).
- Genera la demanda conjunta de mutuo acuerdo (art. 777 LEC) para la via judicial.
- Determina la via aplicable (judicial con Ministerio Fiscal si hay hijos menores o con discapacidad dependientes; notarial o ante Letrado de la Administracion de Justicia si no los hay).
- Verifica la normativa vigente en el BOE antes de redactar y actualiza sus references si detecta una version posterior.

## Que NO hace

- No cubre divorcio o separacion contencioso, modificacion de medidas ya acordadas ni nulidad matrimonial.
- No tramita casos con indicios de violencia (se escalan).
- No da opinion juridica concreta; el output siempre es un DRAFT para revision por abogado.
- No sustituye la ratificacion de las partes, la aprobacion judicial ni la escritura notarial.

---

## Skills

### `convenio-regulador`

Genera el convenio regulador de separacion o divorcio de mutuo acuerdo (art. 90 CC) y, para la via judicial, la demanda conjunta (art. 777 LEC).

Invocacion: `/derecho-familia:convenio-regulador`

Inputs requeridos: alcance (solo convenio / convenio + demanda); separacion o divorcio; existencia de hijos menores o dependientes y sus datos; datos de ambos conyuges; regimen economico; guarda y custodia y visitas; uso de la vivienda; pension de alimentos; liquidacion del regimen; pension compensatoria si procede.

Output: convenio regulador en markdown, DRAFT (y, opcionalmente, demanda de mutuo acuerdo).

Que NO hace: no cubre divorcio contencioso, modificacion de medidas ni nulidad matrimonial.

---

## Dependencias

### Tools requeridas

| ID | Uso |
|---|---|
| `io.gravitonai.tools.read_document` | Lectura del CC, LEC y Ley 15/2015 en el BOE (verificacion normativa) |
| `io.gravitonai.tools.web_search` | Fallback normativo y consulta de especialidades autonomicas y jurisprudencia |
| `io.gravitonai.tools.draft_markdown` | Generacion del documento desde plantilla |

### Tools opcionales

| ID | Uso |
|---|---|
| `io.gravitonai.tools.escalate_to_attorney` | Escalacion a abogado en casos contenciosos o sensibles |

### Servidores MCP

Ninguno.

---

## Instalacion

```
/plugin marketplace add ./derecho-familia
```
