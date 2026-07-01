# Civil - Arrendamiento Urbano

Plugin de GravitonAI para la generacion de contratos de arrendamiento urbano con cumplimiento de la Ley 29/1994 de Arrendamientos Urbanos (LAU).

---

## Que hace

- Genera contratos de arrendamiento de vivienda habitual entre arrendador y arrendatario.
- Genera contratos de arrendamiento de local de negocio / uso distinto de vivienda.
- Adapta el contrato segun la naturaleza de las partes (persona fisica o juridica).
- Aplica la normativa vigente verificando siempre la ultima version consolidada de la LAU en el BOE antes de redactar.
- Advierte sobre zonas de mercado residencial tensionado y aplica las limitaciones de renta correspondientes (Art. 17.6 y 17.7 LAU, Ley 12/2023).
- Genera clausulas conformes a la LAU e indica cuales son imperativas y cuales dispositivas.

## Que NO hace

- No revisa contratos existentes (para eso, crear una skill `revisar-contrato-arrendamiento`).
- No cubre arrendamientos de finca rustica, viviendas turisticas, viviendas militares ni porteros/guardas.
- No tramita el deposito de fianza ante el organismo autonomico.
- No da opinion juridica concreta; el output siempre es un DRAFT para revision por abogado.
- No reemplaza la firma ante notario ni la inscripcion en el Registro de la Propiedad.

---

## Skills

### `generar-contrato-arrendamiento`

Genera un contrato de arrendamiento urbano completo a partir de los datos recogidos al usuario.

Invocacion: `/civil-arrendamiento-urbano:generar-contrato-arrendamiento`

Inputs requeridos:
- Tipo de inmueble (vivienda / local de negocio)
- Datos del arrendador (nombre/razon social, NIF/CIF, domicilio, naturaleza: persona fisica o juridica)
- Datos del arrendatario (nombre/razon social, NIF/CIF, domicilio, naturaleza: persona fisica o juridica)
- Datos del inmueble (direccion completa, referencia catastral, descripcion, comunidad autonoma, municipio)
- Renta mensual pactada
- Duracion pactada (o "minimo legal")
- Fianza (o "segun ley")
- Fecha de inicio del contrato

Output: contrato completo en markdown, DRAFT, listo para revision por abogado.

---

## Dependencias

### Tools requeridas

| ID | Uso |
|---|---|
| `io.gravitonai.tools.read_document` | Lectura directa de la LAU en el BOE (verificacion normativa) |
| `io.gravitonai.tools.web_search` | Fallback normativo y consulta de normativa autonomica |
| `io.gravitonai.tools.draft_markdown` | Generacion del contrato desde plantilla |

### Tools opcionales

| ID | Uso |
|---|---|
| `io.gravitonai.tools.escalate_to_attorney` | Escalacion a abogado en casos complejos |

### Servidores MCP

Ninguno.

---

## Instalacion

```
/plugin marketplace add ./civil-arrendamiento-urbano
```

---

## Tuning

<!-- EDITAR PARA TU EQUIPO: personalizar segun la practica del despacho -->

- Jurisdiccion por defecto: en `CLAUDE.md`, campo "Jurisdiccion por defecto".
- Clausulas adicionales habituales del despacho: agregar en `skills/generar-contrato-arrendamiento/references/` como nuevo archivo de referencia y referenciar desde `SKILL.md`.
- Plantillas personalizadas: editar `skills/generar-contrato-arrendamiento/assets/contrato-arrendamiento-vivienda.md` y `contrato-arrendamiento-local.md`.
