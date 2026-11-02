# Gestoría

Plugin de GravitonAI para la preparación de trámites administrativos de gestoría en España, verificando siempre la normativa y las tasas vigentes en el BOE y en la sede de cada organismo. Genera la solicitud o escrito, la hoja de datos para el formulario oficial y el checklist de documentos, tasas y organismo de presentación.

Salida en DRAFT markdown para revisión profesional en el editor. La presentación telemática automática se abordara más adelante (conectores por API y presentación asistida por navegador con firma humana).

---

## Qué hace

- Prepara el cambio de titularidad de vehículo ante la DGT y la notificación de venta.
- Prepara el alta y la baja de autónomo (censo AEAT 036 y RETA de la Seguridad Social).
- Prepara altas y bajas en la Seguridad Social (afiliación/NUSS, empresa y CCC, trabajadores del Régimen General, empleadas de hogar).
- Prepara la autoliquidación del Impuesto de Sucesiones (modelo 650) y avisa de la plusvalía municipal.
- Verifica la normativa, los modelos y las tasas vigentes en el BOE y sedes oficiales, aplicando la redacción vigente directamente al borrador del workspace.

## Qué NO hace

- No presta asesoramiento jurídico ni redacta demandas (para eso, los plugins de derecho).
- No presenta todavía los trámites de forma automática; genera el DRAFT e indica el organismo y la vía.
- No calcula con carácter definitivo cuotas ni impuestos: los importes se entregan como estimación y deben verificarse.
- No sustituye la revisión por un gestor colegiado o profesional competente.

---

## Skills

### `transferencia-vehiculo`

Prepara el cambio de titularidad de un vehículo usado ante la DGT y, en su caso, la notificación de venta (RD 2822/1998). Genera el contrato de compraventa, la hoja de datos de la solicitud, la notificación de venta y el checklist de documentos, tasa y organismo, con aviso del ITP autonómico.

Invocación: `/gestoria:transferencia-vehiculo`

Inputs: rol (comprador / vendedor / ambos); datos del vehículo (matrícula, bastidor, marca, modelo, fecha 1a matriculación); datos de vendedor y comprador; precio y fecha; comunidad autónoma (ITP); estado de la ITV.

Output: contrato de compraventa, solicitud de cambio de titularidad (hoja de datos + checklist + tasa) y notificación de venta, en markdown, DRAFT.

### `alta-baja-autonomo`

Prepara el alta y la baja de autónomo: alta y baja censal en la AEAT (modelo 036) y alta y baja en el RETA de la Seguridad Social por rendimientos reales (Ley 20/2007, RD-ley 13/2022).

Invocación: `/gestoria:alta-baja-autonomo`

Inputs: tipo de operación (alta / baja); datos del interesado; actividad y epígrafe IAE; fecha de inicio o de cese; rendimientos netos previstos (para el tramo); régimen de IVA e IRPF; tarifa plana; domicilio de la actividad.

Output: hojas de datos del alta o baja censal (036) y del alta o baja en RETA (con cuota estimada en el alta) y checklist de documentos, sedes y plazos, en markdown, DRAFT.

### `alta-baja-seguridad-social`

Prepara altas y bajas en la Seguridad Social por el lado del empleador y del Régimen General (LGSS, RD 84/1996): afiliación inicial / NUSS (TA.1), inscripción de empresa y CCC (TA.6), alta y baja de trabajadores por cuenta ajena (Sistema RED / Import@ss) y empleadas de hogar.

Invocación: `/gestoria:alta-baja-seguridad-social`

Inputs: tipo de operación (alta / baja); sujeto (afiliación inicial / empresa / trabajador / empleada de hogar); datos del empleador (CIF, CCC); datos del trabajador (nombre, NIF, NUSS, grupo de cotización); fecha de efectos; tipo de contrato.

Output: hoja de datos del modelo TA correspondiente, checklist de documentos, organismo (TGSS) y vía (Import@ss / Sistema RED) y plazos, en markdown, DRAFT.

### `liquidacion-impuesto-sucesiones`

Prepara la autoliquidación del Impuesto de Sucesiones (modelo 650, mortis causa) de un heredero (Ley 29/1987 y normativa autonómica). Complementa a `herencia` de derecho-civil (el cuaderno jurídico); esta hace la liquidación fiscal.

Invocación: `/gestoria:liquidacion-impuesto-sucesiones`

Inputs: comunidad autónoma; datos del causante y del heredero (grupo I-IV); caudal hereditario (inventario y valores); cargas y deudas; seguros de vida; ajuar; vivienda habitual; empresa familiar; discapacidad.

Output: borrador del modelo 650 (base y cuota estimada, marcada para verificar) y checklist de documentación, organismo y plazo (6 meses), en markdown, DRAFT. Avisa de la plusvalía municipal.

### `extranjeria-residencia` — trasladada

Esta skill ha pasado al plugin **`extranjeria`**, junto con la nueva `extranjeria-nacionalidad-espanola`.

Invocación: `/extranjeria:extranjeria-residencia`

Motivo del traslado: el marco cambio por completo el 20 de mayo de 2025 con la entrada en vigor del
Reglamento aprobado por el Real Decreto 1155/2024, que derogó el Real Decreto 557/2011, y la materia
acumula ya skills suficientes para constituir un vertical propio.

---

## Dependencias

### Tools requeridas

| ID | Uso |
|---|---|
| `io.gravitonai.tools.read_file` | Lectura de documentos en el workspace (fallback extremo de `# WORKSPACE ACTIVE DOCUMENTS`) |
| `io.gravitonai.tools.create_file` | Creación de solicitudes, hojas de datos y checklists en el workspace |
| `io.gravitonai.tools.edit_file` | Edición incremental de hojas de datos, solicitudes y borradores en el workspace |
| `io.gravitonai.tools.web_search` | Verificación normativa en el BOE, tasas y modelos oficiales |
| `io.gravitonai.tools.human_in_the_loop_request` | Formulario interactivo con opciones (single/multi-select) y texto libre |
| `io.gravitonai.tools.restricted_human_in_the_loop_request` | Formulario con opciones cerradas para confirmaciones y enrutamiento |
| `io.gravitonai.tools.slot_filling_request` | Formulario de captura de datos en lotes (*batch slot-filling*) con campos de texto libre |
| `io.gravitonai.tools.search_clients` | Búsqueda prioritaria de clientes y partes en el sistema por nombre o datos identificativos |
| `io.gravitonai.tools.get_client` | Recuperación de la ficha completa de un cliente existente |

### Servidores MCP

Ninguno por ahora. La presentación telemática (conectores por API y presentación asistida por navegador) se abordara más adelante.

---

## Instalación

```
/plugin marketplace add ./gestoria
```
