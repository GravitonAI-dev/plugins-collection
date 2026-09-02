---
name: derecho-civil-reclamacion-clausulas-abusivas
description: >
  Genera escritos para reclamar la nulidad de clausulas abusivas en contratos con consumidores y la
  restitucion de las cantidades indebidamente cobradas, conforme al Texto Refundido de la Ley General
  para la Defensa de los Consumidores y Usuarios (TRLGDCU, Real Decreto Legislativo 1/2007), la Ley
  7/1998 de Condiciones Generales de la Contratacion (LCGC) y la Directiva 93/13/CEE, en su version
  consolidada vigente verificada en el BOE. Produce, a eleccion del usuario, una RECLAMACION
  EXTRAJUDICIAL a la entidad o empresa, o una DEMANDA de nulidad con restitucion de cantidades e
  intereses. Cubre gastos de formalizacion de hipoteca, clausula suelo, IRPH, comision de apertura,
  interes de demora, tarjeta revolving u otras condiciones no negociadas individualmente. NO usar para
  contratos entre empresarios sin consumidor, para clausulas negociadas individualmente, ni para
  reclamaciones ajenas al derecho de consumo.
when_to_use: |
  - El usuario es un consumidor (o su representante) que quiere impugnar una clausula predispuesta de un contrato de adhesion.
  - El usuario quiere recuperar cantidades cobradas en virtud de una clausula que considera abusiva (gastos, comisiones, intereses).
  - El usuario pide una reclamacion previa a la entidad/empresa o una demanda de nulidad de clausula abusiva con restitucion.
inputs:
  - alcance: reclamacion extrajudicial / demanda de nulidad con restitucion
  - tipo_clausula: gastos de formalizacion de hipoteca / clausula suelo / IRPH / comision de apertura / interes de demora / tarjeta revolving / otra
  - naturaleza_reclamante: consumidor persona fisica (o representante legal)
  - datos_reclamante: nombre, NIF, domicilio a efectos de notificaciones
  - datos_predisponente: entidad o empresa (banco, financiera, prestador de servicios), CIF, domicilio
  - datos_contrato: tipo de contrato, fecha, numero, notaria y protocolo si es escritura, y clausula concreta impugnada
  - cantidades_reclamadas: importes cobrados en virtud de la clausula y su desglose documental
  - comunidad_autonoma: para fuero y para servicios de consumo autonomicos
outputs:
  - reclamacion_extrajudicial: opcional, escrito de reclamacion previa a la entidad o empresa en markdown, DRAFT
  - demanda_nulidad: opcional, demanda de nulidad de clausula abusiva con restitucion de cantidades e intereses en markdown, DRAFT
references:
  - references/trlgdcu-clausulas-abusivas.md
  - references/lcgc-condiciones-generales.md
  - references/jurisprudencia-tjue-ts-clausulas.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/reclamacion-extrajudicial-clausula-abusiva.md
  - assets/demanda-nulidad-clausula-abusiva.md
---

# Reclamacion de Clausulas Abusivas en Contratos con Consumidores

> DRAFT — para revision por un abogado antes de su presentacion. No constituye asesoramiento juridico.

## Guardrails

1. Verificar siempre el TRLGDCU, la LCGC y la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada.
3. La materia se aplica SOLO a consumidores (Art. 3 TRLGDCU) frente a un predisponente (empresario) y SOLO a clausulas no negociadas individualmente (Art. 82). Si la clausula fue negociada, o ambas partes son empresarios, no procede esta via: advertir y ofrecer escalacion.
4. La jurisprudencia del TJUE (Directiva 93/13/CEE) y del Tribunal Supremo en esta materia es CAMBIANTE y decisiva. Antes de redactar, verificar SIEMPRE con web_search la jurisprudencia reciente del tipo de clausula reclamado (ver Paso 1.3). No citar ninguna sentencia sin haberla verificado en esa consulta.
5. Posicion conservadora: no afirmar que una clausula es nula con caracter automatico o generalizado. La abusividad exige el control de incorporacion y de transparencia caso por caso (Arts. 80, 82, 83 TRLGDCU; Directiva 93/13). Presentar la pretension de nulidad como fundada, no como cosa juzgada.
6. Nunca inventar sentencias, numeros de resolucion, fechas ni doctrina. Marcar con `{{VERIFICAR}}` (doble llave, nunca corchete simple `[verificar]`: colisiona con los identificadores de privacidad `[PERSON_1]`) todo claim factual o jurisprudencial no confirmado en el Paso 1.
7. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{cuantia_reclamada}}` (NUNCA corchete simple `[DATO]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `Edit` posterior necesita un `oldString` unico. Nunca inventar datos, cuantias, fechas ni numeros de contrato.
8. La accion de nulidad de clausula abusiva es imprescriptible; la accion de restitucion tiene su propio regimen de prescripcion segun la jurisprudencia vigente (verificar en el Paso 1). No afirmar plazos de restitucion sin verificar.

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. En esta materia, ademas, verifica la jurisprudencia reciente porque es determinante y cambia con frecuencia. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del TRLGDCU, de la LCGC y de la LEC.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555",
  format: "text"
)
```
Extraer: fecha del texto consolidado vigente del TRLGDCU; redaccion actual de los arts. 80 a 91 (control de incorporacion, concepto de clausula abusiva, nulidad y no integracion, lista de clausulas abusivas).

Consultar tambien la LCGC:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-1998-8789",
  format: "text"
)
```
Extraer: redaccion vigente sobre control de incorporacion (Arts. 5 y 7), nulidad (Arts. 8 y 9), Registro de Condiciones Generales y accion de cesacion (Arts. 11 y 12).

Y la LEC para la demanda (competencia, procedimiento y control de oficio):
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2000-323",
  format: "text"
)
```

**1.3 — Verificar la JURISPRUDENCIA RECIENTE del tipo de clausula (OBLIGATORIO en esta materia).** La doctrina del TJUE y del Tribunal Supremo cambia con frecuencia y determina el resultado. Antes de redactar, invocar web_search especifica para el tipo de clausula reclamado, por ejemplo:
```
web_search("TJUE Tribunal Supremo clausula <tipo> jurisprudencia reciente <ano actual> nulidad restitucion")
```
Ejemplos de terminos por tipo: "gastos hipotecarios distribucion notaria registro gestoria", "clausula suelo transparencia retroactividad", "IRPH control transparencia", "comision de apertura", "interes de demora abusivo prestamo personal", "tarjeta revolving usura TAE". Anotar solo los criterios verificados; si una sentencia no se puede confirmar, no citarla y marcar `{{VERIFICAR}}`.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior, el texto de los articulos ha cambiado, o la jurisprudencia verificada difiere de la registrada, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/trlgdcu-clausulas-abusivas.md` y/o `references/lcgc-condiciones-generales.md` con la redaccion vigente.
- Actualizar los criterios jurisprudenciales verificados en `references/jurisprudencia-tjue-ts-clausulas.md`, conservando la advertencia de que son cambiantes y deben re-verificarse.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version o doctrina mas reciente (norma/sentencia y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_document` falla (error HTTP, timeout):
```
web_search("texto refundido Ley General Defensa Consumidores Usuarios clausulas abusivas articulos 80 82 83 BOE consolidado")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del TRLGDCU/LCGC en el BOE. El escrito se genera con la version de referencia y con la advertencia de jurisprudencia no verificada. Verificar manualmente antes de presentar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos:

**Bloque A — Alcance del encargo:**
"Desea generar (1) una reclamacion extrajudicial previa a la entidad o empresa, o (2) una demanda judicial de nulidad de la clausula con restitucion de cantidades? (La reclamacion previa suele recomendarse antes de demandar.)"

**Bloque B — Tipo de clausula:**
"Que clausula desea impugnar? (1) gastos de formalizacion de hipoteca, (2) clausula suelo, (3) IRPH, (4) comision de apertura, (5) interes de demora, (6) tarjeta revolving, (7) otra (describala)."

**Bloque C — Condicion de consumidor y del predisponente:**
- Que el reclamante actuo como consumidor (persona fisica ajena a actividad empresarial o profesional, Art. 3 TRLGDCU).
- Datos del reclamante: nombre, NIF, domicilio a efectos de notificaciones.
- Datos del predisponente: entidad o empresa, CIF, domicilio.

**Bloque D — Datos del contrato y de la clausula:**
- Tipo de contrato, fecha, numero. Si es escritura publica: notaria y numero de protocolo.
- Transcripcion o descripcion de la clausula concreta impugnada.
- Si la clausula fue o no negociada individualmente (por defecto, condicion general no negociada).

**Bloque E — Cantidades cobradas y prueba documental:**
- Importes efectivamente cobrados en virtud de la clausula, con su desglose (facturas de gestoria, aranceles de notaria y registro, cuadro de amortizacion, extractos, liquidaciones).
- Documentos que acreditan cada pago.

**Bloque F — Localizacion (fuero y consumo autonomico):**
"En que comunidad autonoma y municipio reside el consumidor? (Para el fuero del Art. 52.3 LEC y para orientar sobre los servicios de consumo autonomicos.)"

### Paso 3 — Validacion de la pretension

Antes de redactar, validar:

a) **Ambito subjetivo:** que el reclamante es consumidor y el predisponente es empresario (Art. 3 TRLGDCU). Si no, no procede esta via: advertir y ofrecer escalacion.

b) **Condicion general no negociada (Art. 82.1 TRLGDCU; Art. 1 LCGC):** que la clausula fue predispuesta e impuesta sin negociacion individual. Si fue negociada, advertir de que el control de contenido no opera igual.

c) **Control de incorporacion y de transparencia (Arts. 5 y 7 LCGC; Art. 80 TRLGDCU):** valorar si la clausula supera los requisitos de claridad, concrecion, sencillez y accesibilidad, y si el consumidor pudo comprender su carga economica y juridica.

d) **Control de contenido (Arts. 82, 85-90 TRLGDCU):** valorar si causa, en contra de la buena fe, un desequilibrio importante en perjuicio del consumidor.

e) **Jurisprudencia verificada (Paso 1.3):** encuadrar la clausula en los criterios TJUE/TS confirmados, con posicion conservadora. No prometer resultado.

f) **Restitucion:** si la clausula es nula, precisar el efecto restitutorio (Art. 83 TRLGDCU y jurisprudencia): devolucion de lo pagado con intereses. No afirmar plazos de prescripcion de la restitucion sin verificar en el Paso 1.

### Paso 4 — Generacion de los documentos

Seleccionar la plantilla segun el alcance:
- Reclamacion previa: `assets/reclamacion-extrajudicial-clausula-abusiva.md`
- Demanda: `assets/demanda-nulidad-clausula-abusiva.md`

Invocar:
```
draft_markdown(
  template_id: "reclamacion-extrajudicial-clausula-abusiva" | "demanda-nulidad-clausula-abusiva",
  variables: {
    todos los datos recogidos en los bloques A-F,
    tipo_clausula, criterios jurisprudenciales verificados en el Paso 1.3,
    fecha_verificacion_normativa
  }
)
```

Rellenar todos los campos con los datos reales. Los campos que el usuario no haya proporcionado conservan el placeholder propio del asset en doble llave (nunca corchete simple). Los claims factuales o jurisprudenciales no verificados se marcan `{{VERIFICAR}}`.

Aplicar el estilo de `references/estilo-redaccion-escritos.md`: escrito claro y ordenado, HECHOS numerados con una idea por apartado, documentos relacionados y numerados, voz activa, sin latinismos ni citas largas, y SUPLICO ajustado a la nulidad y la restitucion pedidas.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1) y, en su caso, la nota de jurisprudencia verificada o `{{VERIFICAR}}`.
- Identifica correctamente al consumidor, al predisponente y la clausula impugnada.
- Expresa con claridad el control de incorporacion/transparencia/contenido y el efecto restitutorio, con las cantidades desglosadas.
- Sigue el estilo de redaccion clara (hechos y fundamentos numerados, una idea por parrafo).

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado antes de su presentacion.
2. Version del TRLGDCU/LCGC verificada: [fecha extraida en Paso 1].
3. La jurisprudencia del TJUE y del Tribunal Supremo en materia de clausulas abusivas es cambiante; los criterios citados se verificaron el {{fecha_verificacion_jurisprudencia}} y deben confirmarse antes de presentar. Los claims marcados {{VERIFICAR}} no han sido confirmados.
4. La abusividad exige un analisis caso por caso (control de incorporacion, transparencia y contenido). No existe nulidad automatica generalizada.
5. La accion de nulidad es imprescriptible; la accion de restitucion tiene su propio regimen de prescripcion, que debe confirmarse con la jurisprudencia vigente.
6. Para la demanda, la competencia territorial corresponde, a eleccion del consumidor, a su propio domicilio (Art. 52.3 LEC). Verificar la preceptividad de abogado y procurador segun la cuantia.
```

## Como NO se usa esta skill

- No usar cuando ambas partes son empresarios o profesionales: la proteccion del TRLGDCU es del consumidor.
- No usar para clausulas negociadas individualmente ni para el objeto principal del contrato cuando sea claro y comprensible (salvo falta de transparencia).
- No usar para revisar o redactar el contrato de prestamo o de servicio en si (eso es otra skill: generacion o revision contractual).
- No usar para reclamaciones de consumo ajenas a clausulas abusivas (garantias de producto, viajes combinados, etc.) sin adaptacion.
- No usar para emitir un dictamen sobre las probabilidades de exito de un litigio concreto: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| El reclamante no es consumidor o la contraparte no es empresario | Advertir que no procede esta via y ofrecer escalacion |
| Clausula negociada individualmente o duda seria sobre su caracter de condicion general | Advertir de la limitacion del control de contenido y ofrecer escalacion |
| Jurisprudencia del tipo de clausula contradictoria o no verificable | Marcar `{{VERIFICAR}}`, adoptar posicion conservadora y recomendar confirmacion por abogado |
| Cuantia elevada, allanamiento improbable u oposicion tecnica previsible de la entidad | Advertir del riesgo procesal y ofrecer escalacion |
| Concurrencia de accion colectiva o de cesacion (Arts. 12 LCGC, 53-56 TRLGDCU) | Escalar via escalate_to_attorney |
| Posible usura (tarjeta revolving) con marco distinto (Ley de 23 de julio de 1908) | Advertir del doble encuadre (abusividad y usura) y escalar para valoracion |
