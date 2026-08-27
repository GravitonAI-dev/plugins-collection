---
name: desahucio
description: >
  Genera la demanda de juicio verbal de desahucio de finca urbana conforme al articulo 250.1 de la
  Ley de Enjuiciamiento Civil (LEC) en su version consolidada vigente verificada en el BOE, en tres
  supuestos: desahucio por falta de pago de rentas (con opcion de ACUMULAR la reclamacion de las
  rentas y cantidades debidas), desahucio por expiracion del plazo contractual y desahucio por
  precario (ocupacion sin titulo). Aplica la resolucion del arrendamiento por impago del art. 27 LAU
  y las novedades procesales de la LO 1/2025 (requisito de MASC, tramitacion escrita del juicio
  verbal, señalamiento del lanzamiento). NO usar para tutela sumaria de la posesion frente a okupacion
  ilegal (Art. 250.1.4), desahucio de finca rustica, ejecucion hipotecaria, ni para redactar la
  oposicion del demandado.
when_to_use: |
  - El usuario quiere recuperar la posesion de una vivienda o local urbano arrendado o cedido.
  - El arrendatario no paga la renta y el arrendador quiere desahuciarlo (con o sin reclamacion de rentas).
  - El contrato de arrendamiento ha expirado y el arrendatario no desaloja.
  - Un ocupante posee la finca sin titulo ni pago (precario) y el propietario quiere recuperarla.
  - El usuario pide una demanda de desahucio de finca urbana.
inputs:
  - supuesto: falta de pago / expiracion del plazo / precario
  - acumular_rentas: solo en falta de pago, acumular o no la reclamacion de rentas debidas (si / no)
  - tipo_inmueble: vivienda habitual / local de negocio o uso distinto de vivienda
  - naturaleza_arrendador: persona fisica o persona juridica
  - datos_arrendador: nombre o razon social, NIF o CIF, domicilio a efectos de notificaciones
  - naturaleza_arrendatario: persona fisica o persona juridica (u ocupante en precario)
  - datos_arrendatario: nombre o razon social, NIF o CIF, domicilio del inmueble
  - datos_inmueble: direccion completa, referencia catastral, comunidad autonoma y municipio
  - datos_contrato: fecha de firma, renta mensual, duracion pactada (falta de pago y expiracion)
  - rentas_debidas: importe total adeudado y periodos impagados (falta de pago)
  - fecha_expiracion: fecha en que expiro el contrato y sus prorrogas (expiracion del plazo)
  - titulo_precario: descripcion de la cesion gratuita y de su revocacion (precario)
  - requerimiento_previo: si se practico requerimiento fehaciente de pago con 30 dias de antelacion (si / no)
  - masc_intentado: si se ha intentado un medio adecuado de solucion de controversias (si / no)
  - gran_tenedor: si el arrendador es gran tenedor y el demandado puede estar en situacion de vulnerabilidad (si / no / desconocido)
outputs:
  - demanda_desahucio: demanda de juicio verbal de desahucio en markdown, DRAFT, segun el supuesto elegido
references:
  - references/lec-juicio-desahucio.md
  - references/lau-resolucion-por-impago.md
  - references/enervacion-y-vulnerabilidad.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/template-demanda-desahucio-falta-pago.md
  - assets/template-demanda-desahucio-expiracion-plazo.md
  - assets/template-demanda-desahucio-precario.md
---

# Generar Demanda de Juicio de Desahucio

> DRAFT — para revision por un abogado antes de su presentacion. No constituye asesoramiento juridico.

## Guardrails

1. Verificar siempre la LEC y la LAU en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version de la LEC o de la LAU posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada. El juicio de desahucio ha sido reformado por la LO 1/2025 (tramitacion escrita del juicio verbal, requisito de MASC): confirmar siempre la redaccion vigente.
3. El juicio de desahucio de finca urbana se sustancia por juicio verbal (Art. 250.1.1 para falta de pago y expiracion del plazo; Art. 250.1.2 para precario). No usar esta skill para okupacion ilegal por tutela sumaria de la posesion (Art. 250.1.4): en ese caso, advertir y escalar.
4. Competencia exclusiva del tribunal del lugar en que este sita la finca (Art. 52.1.7 LEC). No admitir sumision a otro fuero.
5. La enervacion de la accion (Art. 22.4 LEC) solo cabe en el desahucio por falta de pago, una sola vez, y no procede si el arrendador requirio de pago de forma fehaciente con al menos 30 dias de antelacion y el arrendatario no pago. No cabe enervacion en expiracion del plazo ni en precario. Informar siempre de esta regla.
6. Posicion conservadora sobre el MASC: la LO 1/2025 introdujo el intento previo de un medio adecuado de solucion de controversias como requisito de admisibilidad (Art. 403.2 LEC). Ante la duda sobre su exigencia en desahucio, recomendar e integrar el intento previo y advertir de la cuestion.
7. Vulnerabilidad: si el arrendador es gran tenedor o el inmueble es vivienda habitual del demandado, advertir de las especialidades procesales de vulnerabilidad (traslado a servicios sociales, posibles suspensiones del lanzamiento) y verificar la normativa vigente. Nunca omitir esta advertencia en desahucios de vivienda.
8. Marcar todos los campos a rellenar con `[DATO]` en mayusculas. Nunca inventar datos, rentas, fechas ni referencias catastrales.
9. Nunca redactar clausulas o pretensiones que contradigan normas imperativas de la LAU (Art. 6 LAU) ni afirmar la resolucion del contrato sin base en el Art. 27 LAU. Nunca inventar jurisprudencia.

## Procedimiento

### Paso 1 — Verificacion normativa

**1.1 — Consultar la version registrada en references.** Consultar el archivo `fuentes-plantillas-validadas.md` directamente desde el bloque `<document kind="references-collection">` de tu system prompt y anotar la "Version registrada" de la LEC, de la LAU, de la LO 1/2025 y de la normativa de vulnerabilidad.

**1.2 — Consultar la fuente oficial vigente en vivo.** Invocar:
```
web_search("BOE-A-2000-323 Ley Enjuiciamiento Civil juicio verbal desahucio articulo 250 437 440 texto consolidado")
```
Extraer: fecha del texto consolidado vigente de la LEC; redaccion actual de los arts. 250.1, 437, 438, 440, 22.4, 447.2 (desahucio y acumulacion) y del art. 403.2 y 264.4 (requisito y acreditacion del MASC).

Consultar tambien la LAU:
```
web_search("BOE-A-1994-26003 Ley 29/1994 Arrendamientos Urbanos articulo 27 resolucion impago texto consolidado")
```
Extraer: fecha del texto consolidado vigente de la LAU y redaccion actual del art. 27 (resolucion por impago).

**1.3 — Comparar.** Contrastar la version oficial con la registrada en `fuentes-plantillas-validadas.md` y con las referencias del prompt (`lec-juicio-desahucio.md`, `lau-resolucion-por-impago.md`, `enervacion-y-vulnerabilidad.md`).

**1.4 — Aplicar cambios normativos.** Si la version oficial es posterior o el texto de los articulos ha cambiado:
- Aplicar en memoria la redaccion vigente para adaptar los tramites y fundamentacion de la demanda.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

**1.5 — Fallback si la busqueda no es accesible.** Si la busqueda web falla: usar las references cargadas en el prompt como respaldo y notificar al usuario:
"No se pudo verificar en vivo la version vigente de la LEC/LAU en el BOE. La demanda se genera con la version de referencia. Verificar manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos:

**Bloque A — Supuesto de desahucio:**
"Que tipo de desahucio necesita? (1) Falta de pago de rentas; (2) Expiracion del plazo del contrato; (3) Precario (ocupacion gratuita sin titulo tras revocar la tolerancia)."

Si responde (1), preguntar ademas: "Desea ACUMULAR en la misma demanda la reclamacion de las rentas y cantidades debidas (recomendado, Art. 437.3 LEC), o solo el desahucio?"

**Bloque B — Tipo de inmueble:**
"El inmueble es (1) vivienda habitual, o (2) local de negocio o uso distinto de vivienda?"

**Bloque C — Datos del arrendador / propietario (demandante):**
- Nombre completo o razon social, NIF/CIF, domicilio a efectos de notificaciones.
- Persona fisica o juridica. Si juridica, datos del representante.
- Si es gran tenedor de vivienda (para las advertencias de vulnerabilidad).

**Bloque D — Datos del arrendatario / ocupante (demandado):**
- Nombre completo o razon social, NIF/CIF si se conoce.
- Domicilio del inmueble objeto del desahucio.

**Bloque E — Datos del inmueble:**
- Direccion completa, referencia catastral, comunidad autonoma y municipio.

**Bloque F — Datos del contrato y de la deuda (segun supuesto):**
- Falta de pago: fecha del contrato, renta mensual, periodos y cuantia total impagada; si se practico requerimiento fehaciente de pago con 30 dias de antelacion (afecta a la enervacion).
- Expiracion del plazo: fecha del contrato, fecha de expiracion del plazo y de sus prorrogas, y si se notifico la no renovacion en plazo.
- Precario: descripcion de como se cedio el uso gratuito, la relacion con el ocupante y como y cuando se revoco la tolerancia (requerimiento de restitucion).

**Bloque G — MASC (procedibilidad):**
"Se ha intentado ya algun medio adecuado de solucion de controversias (negociacion, mediacion, conciliacion, requerimiento) antes de demandar? (si / no)"

Si responde "no", advertir de que la LO 1/2025 exige acreditar el intento previo de MASC como requisito de admisibilidad (Art. 403.2 LEC) y recomendar realizarlo antes de presentar.

### Paso 3 — Validacion de procedibilidad

Antes de redactar, validar:

a) **Supuesto y procedimiento (Art. 250.1):** confirmar que el caso encaja en falta de pago, expiracion del plazo (250.1.1) o precario (250.1.2). Si es okupacion ilegal, no procede esta skill: advertir y escalar.

b) **Titulo y legitimacion:** el demandante debe ser el arrendador/propietario legitimado. En falta de pago y expiracion, debe existir contrato de arrendamiento. En precario, debe acreditarse la titularidad y la ausencia de titulo del ocupante.

c) **Resolucion por impago (Art. 27 LAU):** en falta de pago, confirmar que el impago de la renta o cantidades asimiladas es causa de resolucion.

d) **Enervacion (Art. 22.4 LEC):** informar de si el demandado podra enervar la accion pagando o consignando, y de que no cabe enervacion si se practico requerimiento fehaciente con 30 dias de antelacion sin pago, ni en expiracion del plazo ni en precario.

e) **Competencia (Art. 52.1.7 LEC):** identificar el Juzgado de Primera Instancia del lugar donde este sita la finca.

f) **MASC (Art. 403.2 LEC):** confirmar si se ha intentado o si concurre una excepcion. Por defecto conservador, recomendar acreditar el intento previo.

g) **Vulnerabilidad:** en desahucio de vivienda, advertir del posible traslado a servicios sociales y de las suspensiones extraordinarias del lanzamiento vigentes; verificar la normativa aplicable.

### Paso 4 — Generacion del documento

Tomar la plantilla correspondiente directamente desde el bloque `<document kind="assets-collection">` de tu system prompt:
- Falta de pago: `template-demanda-desahucio-falta-pago.md` (activar el bloque condicional de acumulacion de rentas si el usuario lo pidio).
- Expiracion del plazo: `template-demanda-desahucio-expiracion-plazo.md`
- Precario: `template-demanda-desahucio-precario.md`

Generar el documento en el workspace invocando `create_file`:
```
create_file(
  relative_file_path: "demanda_desahucio.md",
  file_content: "... contenido completo redactado a partir de la plantilla y los datos recogidos en los bloques A-G ..."
)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado quedan como `[DATO — PENDIENTE DE COMPLETAR]`.

Aplicar las directivas de `estilo-redaccion-escritos.md` (disponible directamente en `<document kind="references-collection">` del prompt): escrito breve y directo, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos ni citas largas, y SUPLICO ajustado a lo estrictamente pedido.

Tras guardar el archivo en disco del workspace, invocar `read_file` exclusivamente sobre la ruta del workspace para verificar la integridad del documento escrito.

### Paso 5 — Revision final y advertencias

Verificar que el documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente al demandante, al demandado, el inmueble y el juzgado competente.
- Expresa con claridad el supuesto (impago, expiracion o precario) y, en su caso, las rentas debidas y sus periodos.
- Sigue el estilo de redaccion judicial clara (hechos y fundamentos numerados, una idea por parrafo).

Entregar el documento y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado antes de su presentacion.
2. Version de la LEC y de la LAU verificada: [fecha extraida en Paso 1].
3. Competencia del tribunal del lugar donde este sita la finca (Art. 52.1.7 LEC).
4. La LO 1/2025 exige acreditar el intento previo de un MASC (Art. 403.2 LEC). Conservar el justificante.
5. En el desahucio por falta de pago, el demandado puede enervar la accion pagando o consignando (Art. 22.4 LEC), salvo que se le requiriera de pago fehacientemente con 30 dias de antelacion sin resultado. No cabe enervacion en expiracion del plazo ni en precario.
6. En desahucios de vivienda pueden aplicar suspensiones extraordinarias del lanzamiento por vulnerabilidad y traslado a servicios sociales. Verificar la normativa vigente.
7. En el juicio verbal reformado por la LO 1/2025, la proposicion de prueba y las alegaciones sobre excepciones procesales se realizan por escrito; la vista se limita a la practica de la prueba.
```

## Como NO se usa esta skill

- No usar para la tutela sumaria de la posesion frente a okupacion ilegal (Art. 250.1.4 LEC): tiene tramitacion propia.
- No usar para desahucio de finca rustica ni de arrendamientos excluidos de la LAU (Art. 5 LAU).
- No usar para la ejecucion hipotecaria ni para el desahucio derivado de ejecucion.
- No usar para redactar la oposicion del demandado ni el escrito de enervacion.
- No usar para reclamar solo rentas sin desahucio: para una reclamacion dineraria pura, derivar a la skill `monitorio`.
- No usar si el usuario pide opinion juridica sobre un litigio: derivar a un abogado.

## Escalacion

| Situacion | Accion |
|---|---|
| Okupacion ilegal (sin relacion de arrendamiento ni cesion previa) | Advertir que procede la via del Art. 250.1.4 y escalar |
| Demandado en situacion de vulnerabilidad acreditada o arrendador gran tenedor | Advertir de las especialidades y suspensiones y ofrecer escalacion |
| Litigio previo entre las partes o reconvencion previsible | Advertir y derivar a un abogado |
| Dudas sobre la exigencia del MASC en el caso concreto | Advertir y recomendar confirmar con el juzgado competente |
| Caso con componente penal (coacciones, usurpacion) o litigio activo | Advertir y derivar a un abogado penalista/procesalista |
| Duda sobre normativa autonomica o de vulnerabilidad aplicable | Usar web_search para verificar y advertir al usuario |
