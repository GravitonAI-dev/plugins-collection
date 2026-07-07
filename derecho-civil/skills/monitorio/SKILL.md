---
name: monitorio
description: >
  Genera la peticion inicial de proceso monitorio para reclamar una deuda dineraria liquida,
  determinada, vencida y exigible de cualquier cuantia, conforme a los articulos 812 a 818 de la
  Ley de Enjuiciamiento Civil (LEC) en su version consolidada vigente verificada en el BOE.
  Opcionalmente genera tambien el burofax de requerimiento previo (intento de MASC). Adapta el
  documento segun la naturaleza de las partes y el tipo de deuda (rentas de arrendamiento u otra).
  NO usar para deudas no dinerarias, iliquidas o controvertidas, ni para reclamaciones frente a
  Administraciones Publicas.
when_to_use: |
  - El usuario quiere reclamar el cobro de una deuda dineraria impagada.
  - El usuario dispone de documentos que acreditan la deuda (facturas, contrato, reconocimiento, rentas).
  - El usuario pide una peticion de monitorio o un burofax previo de reclamacion de pago.
inputs:
  - alcance: solo peticion inicial / peticion inicial + burofax previo
  - tipo_deuda: rentas de arrendamiento / otra (facturas, prestamo, servicios, comunidad de propietarios)
  - naturaleza_acreedor: persona fisica o persona juridica
  - datos_acreedor: nombre o razon social, NIF o CIF, domicilio
  - datos_deudor: nombre o razon social, NIF o CIF, domicilio o lugar donde pueda ser hallado
  - origen_deuda: descripcion del origen y documentos que la acreditan
  - cuantia: principal en euros e intereses si proceden
  - fecha_vencimiento: fecha en que la deuda vencio y devino exigible
  - partido_judicial: domicilio del deudor a efectos de competencia (Art. 813)
  - masc_intentado: si se ha intentado un medio adecuado de solucion de controversias (si / no)
outputs:
  - peticion_monitorio: peticion inicial de proceso monitorio en markdown, DRAFT
  - burofax_requerimiento: opcional, burofax de requerimiento previo en markdown, DRAFT
references:
  - references/lec-proceso-monitorio-812-818.md
  - references/lec-documentos-acreditativos-deuda.md
  - references/masc-requisito-procedibilidad-lo1-2025.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/peticion-inicial-monitorio.md
  - assets/peticion-inicial-monitorio-rentas.md
  - assets/burofax-requerimiento-previo-masc.md
---

# Generar Peticion de Proceso Monitorio

> DRAFT — para revision por un abogado antes de su presentacion. No constituye asesoramiento juridico.

## Guardrails

1. Verificar siempre la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version de la LEC posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada.
3. Solo procede el monitorio si la deuda es dineraria, liquida, determinada, vencida y exigible (Art. 812). Si no lo es, no redactar la peticion: advertir y ofrecer alternativa (juicio declarativo) o escalacion.
4. Debe existir al menos un documento que acredite la deuda (Art. 812). Sin documento acreditativo, no procede.
5. Competencia exclusiva del Juzgado de Primera Instancia del domicilio o residencia del deudor (Art. 813). No admitir sumision a otro fuero.
6. Posicion conservadora sobre el MASC: ante la duda sobre si es exigible en el monitorio (LO 1/2025), recomendar e integrar el intento previo (burofax) y advertir de la cuestion.
7. Marcar todos los campos a rellenar con `[DATO]` en mayusculas. Nunca inventar datos, cuantias ni fechas.
8. Nunca afirmar que la deuda es exigible o incontrovertida sin base documental. Nunca inventar jurisprudencia.

## Procedimiento

### Paso 1 — Verificacion y actualizacion normativa (OBLIGATORIO, antes de cualquier otra accion)

Verificar la version vigente de la LEC (arts. 812-818 y 264) y del modelo normalizado del CGPJ. Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2000-323",
  format: "text"
)
```

Extraer:
- Fecha del texto consolidado vigente de la LEC.
- Redaccion actual de los arts. 812 a 818 y del art. 264 (acreditacion del intento de MASC).
- Estado de aplicacion de la LO 1/2025 (BOE-A-2025-76).

**Actualizacion del plugin (OBLIGATORIA):** si la version consolidada en el BOE es posterior a la registrada en `references/fuentes-plantillas-validadas.md`, o si el texto de los articulos ha cambiado respecto a lo recogido en las references, actualizar los archivos afectados del plugin (references y, si aplica, el asset del CGPJ) con la version vigente y anotar la nueva fecha verificada antes de continuar.

Verificar tambien el modelo normalizado del CGPJ:
```
read_document(
  path: "https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/El-proceso-monitorio",
  format: "text"
)
```
Si el CGPJ publica una version posterior del modelo, actualizar `assets/peticion-inicial-monitorio.md`.

Si read_document falla (error HTTP, timeout):
```
web_search("Ley Enjuiciamiento Civil proceso monitorio articulos 812 818 texto consolidado BOE")
```

Si ambos fallan: usar las references como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. La peticion se genera con la version de referencia. Verificar manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos:

**Bloque A — Alcance del encargo:**
"Desea generar (1) solo la peticion inicial del monitorio, o (2) tambien el burofax de requerimiento previo de pago (recomendado para acreditar el intento de negociacion previa)?"

**Bloque B — Tipo de deuda:**
"La deuda procede de (1) rentas de arrendamiento impagadas, o (2) otra causa (facturas, prestamo, servicios, gastos de comunidad)?"

**Bloque C — Datos del acreedor:**
- Nombre completo o razon social, NIF/CIF, domicilio a efectos de notificaciones.
- Persona fisica o juridica. Si juridica, datos del representante.

**Bloque D — Datos del deudor:**
- Nombre completo o razon social, NIF/CIF.
- Domicilio o residencia, o lugar donde pueda ser hallado (para competencia y requerimiento, Art. 813).

**Bloque E — Origen y cuantia de la deuda:**
- Origen de la deuda y documentos que la acreditan (facturas, contrato, reconocimiento, certificacion de rentas).
- Principal adeudado en euros.
- Intereses reclamados (pactados o interes legal desde el vencimiento), si proceden.
- Fecha de vencimiento y de exigibilidad.

**Bloque F — MASC (procedibilidad):**
"Se ha intentado ya algun medio de solucion previa (burofax, mediacion, negociacion)? (si / no)"

Si responde "no" y se ha optado por solo la peticion inicial, advertir de la cuestion del requisito de procedibilidad (LO 1/2025) y recomendar generar tambien el burofax.

### Paso 3 — Validacion de procedibilidad

Antes de redactar, validar:

a) **Naturaleza de la deuda (Art. 812):** que es dineraria, liquida, determinada, vencida y exigible. Si falla cualquiera de estos requisitos, no procede monitorio: advertir y ofrecer juicio declarativo o escalacion.

b) **Documento acreditativo (Art. 812):** que existe al menos un documento de los previstos. Si no existe, no procede.

c) **Competencia (Art. 813):** identificar el Juzgado de Primera Instancia del domicilio del deudor. Si el deudor es ilocalizable, advertir de la limitacion (el requerimiento por edictos no procede en el monitorio; podria derivar en archivo).

d) **MASC (LO 1/2025):** confirmar si se ha intentado o si concurre una excepcion. Por defecto conservador, integrar el burofax de requerimiento previo.

e) **Cuantia y via posterior:** informar de que, si el deudor se opone, el asunto se resolvera por juicio verbal (hasta 15.000 euros) u ordinario (superior), Art. 818.

### Paso 4 — Generacion de los documentos

Seleccionar la plantilla segun el tipo de deuda:
- Rentas de arrendamiento: `assets/peticion-inicial-monitorio-rentas.md`
- Otra deuda: `assets/peticion-inicial-monitorio.md`

Invocar:
```
draft_markdown(
  template_id: "peticion-inicial-monitorio" | "peticion-inicial-monitorio-rentas",
  variables: {
    todos los datos recogidos en los bloques A-F
  }
)
```

Si el usuario ha pedido tambien el burofax (Bloque A opcion 2), generar ademas:
```
draft_markdown(
  template_id: "burofax-requerimiento-previo-masc",
  variables: { datos del acreedor, deudor, origen y cuantia de la deuda }
)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan como `[DATO — PENDIENTE DE COMPLETAR]`.

Aplicar el estilo de `references/estilo-redaccion-escritos.md`: escrito breve y directo (una peticion de monitorio es un asunto sencillo, no mas de unos folios), HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos ni citas largas, y SUPLICO ajustado a lo estrictamente pedido.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente al acreedor, al deudor y el juzgado competente.
- Expresa con claridad el origen y la cuantia de la deuda, y relaciona los documentos que se acompanan.
- Sigue el estilo de redaccion judicial clara (hechos y fundamentos numerados, una idea por parrafo).

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado antes de su presentacion.
2. Version de la LEC verificada: [fecha extraida en Paso 1].
3. Deben acompanarse a la peticion los documentos que acreditan la deuda (Art. 812 LEC).
4. Competencia exclusiva del Juzgado de Primera Instancia del domicilio del deudor (Art. 813 LEC).
5. Tras la admision, el deudor sera requerido para pagar u oponerse en 20 dias. Si se opone, el asunto pasa a juicio verbal u ordinario segun la cuantia (Art. 818 LEC).
6. El requisito de intento de MASC (LO 1/2025) puede ser exigido por el juzgado. Se recomienda conservar el justificante del burofax de requerimiento previo.
```

## Como NO se usa esta skill

- No usar para deudas no dinerarias (entrega de cosa, obligaciones de hacer).
- No usar para deudas iliquidas, controvertidas o de existencia dudosa: procede el juicio declarativo.
- No usar para reclamar a una Administracion Publica.
- No usar para redactar la oposicion del deudor ni la posterior demanda de juicio declarativo.
- No usar si el usuario pide opinion juridica sobre un litigio: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| Deuda iliquida, controvertida o no dineraria | Advertir que no procede monitorio y ofrecer escalacion |
| Deudor ilocalizable (sin domicilio ni lugar donde ser hallado) | Advertir de la limitacion del Art. 813 y ofrecer escalacion |
| Deuda superior a 15.000 euros con oposicion previsible | Advertir del paso a juicio ordinario y ofrecer escalacion |
| Duda sobre la exigibilidad del MASC en el caso concreto | Advertir y recomendar confirmar con el juzgado competente |
| Existencia de litigio conexo o reconvencion previsible | Escalar via escalate_to_attorney |
