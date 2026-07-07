---
name: convenio-regulador
description: >
  Genera el convenio regulador de separacion o divorcio de MUTUO ACUERDO conforme al articulo 90 del
  Codigo Civil (guarda y custodia y regimen de visitas, uso de la vivienda familiar, pension de
  alimentos de los hijos, liquidacion del regimen economico y pension compensatoria si procede) y, para
  la via judicial, la demanda conjunta del articulo 777 de la LEC. Determina la via (judicial con
  Ministerio Fiscal si hay hijos menores o con discapacidad dependientes; notarial o ante Letrado de la
  Administracion de Justicia si no los hay, arts. 82 y 87 CC y Ley 15/2015). Verifica la version vigente
  de las normas en el BOE antes de redactar. NO usar para separacion o divorcio contencioso, ni para la
  modificacion de medidas ya acordadas, ni para nulidad matrimonial.
when_to_use: |
  - Ambos conyuges estan de acuerdo en separarse o divorciarse y quieren pactar los efectos.
  - El usuario pide un convenio regulador o una demanda de divorcio o separacion de mutuo acuerdo.
  - Han transcurrido al menos tres meses desde la celebracion del matrimonio.
inputs:
  - alcance: solo convenio regulador / convenio regulador + demanda de mutuo acuerdo (via judicial)
  - tipo_ruptura: separacion / divorcio
  - hijos: existencia de hijos menores no emancipados o con discapacidad dependientes (si / no)
  - datos_hijos: nombre, fecha de nacimiento y situacion de cada hijo, si los hay
  - datos_conyuge_1: nombre, DNI, domicilio
  - datos_conyuge_2: nombre, DNI, domicilio
  - datos_matrimonio: fecha y lugar de celebracion, regimen economico (gananciales / separacion de bienes)
  - guarda_custodia: modalidad propuesta (exclusiva de un progenitor / compartida) y regimen de visitas
  - vivienda_familiar: titularidad y atribucion del uso propuesta
  - pension_alimentos: importe, periodicidad y gastos extraordinarios de los hijos
  - liquidacion_regimen: bienes y deudas comunes a repartir, si procede
  - pension_compensatoria: si existe desequilibrio economico y en que cuantia y plazo
  - partido_judicial: domicilio del ultimo domicilio comun o de uno de los conyuges (competencia)
outputs:
  - convenio_regulador: convenio regulador de separacion o divorcio en markdown, DRAFT
  - demanda_mutuo_acuerdo: opcional, demanda conjunta del Art. 777 LEC en markdown, DRAFT
references:
  - references/cc-convenio-regulador-art90.md
  - references/cc-divorcio-separacion-art81-87.md
  - references/lec-proceso-mutuo-acuerdo-art777.md
  - references/fuentes-plantillas-validadas.md
  - references/estilo-redaccion-escritos.md
assets:
  - assets/convenio-regulador.md
  - assets/demanda-divorcio-mutuo-acuerdo.md
---

# Generar Convenio Regulador y Demanda de Mutuo Acuerdo

> DRAFT — para revision por un abogado antes de su presentacion o firma. No constituye asesoramiento juridico.

## Guardrails

1. Verificar siempre el Codigo Civil y la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 1). No usar una version desactualizada.
3. Solo procede el mutuo acuerdo si ambos conyuges estan conformes y ha transcurrido el plazo minimo de tres meses desde el matrimonio (Art. 81 CC). Si no hay acuerdo o falta el plazo, no redactar: advertir y ofrecer alternativa (procedimiento contencioso) o escalacion.
4. Si existen hijos menores no emancipados o con la capacidad modificada judicialmente que dependan de sus progenitores, la via es JUDICIAL con intervencion del Ministerio Fiscal (Art. 777 LEC). No proponer la via notarial en ese caso.
5. Si no hay hijos menores ni dependientes, informar de que cabe la via notarial o ante el Letrado de la Administracion de Justicia (arts. 82 y 87 CC, Ley 15/2015), mas agil, sin perjuicio de la judicial. En la via notarial es preceptiva la asistencia de letrado.
6. El interes superior del menor prevalece sobre cualquier pacto. No redactar clausulas daninas para los hijos ni gravemente perjudiciales para un conyuge: no serian aprobadas (Art. 90.2 CC).
7. El convenio debe cubrir todos los extremos aplicables del Art. 90.1 CC. Los no aplicables se omiten con mencion breve de que no proceden; no dejar clausulas vacias.
8. Marcar todos los campos a rellenar con `[DATO]` en mayusculas. Nunca inventar datos, importes, fechas ni la existencia o identidad de hijos.
9. Nunca afirmar que el convenio esta aprobado: solo lo aprueba el juez por sentencia (via judicial) o se formaliza ante notario/LAJ (via extrajudicial). Nunca inventar jurisprudencia.

## Procedimiento

### Paso 1 — Verificacion y AUTO-ACTUALIZACION normativa (OBLIGATORIO, antes de cualquier otra accion)

La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. Ejecutar SIEMPRE esta secuencia:

**1.1 — Leer la fecha/version registrada localmente.** Abrir `references/fuentes-plantillas-validadas.md` y anotar la "Version registrada" del Codigo Civil, de la LEC y de la Ley 15/2015.

**1.2 — Consultar la fuente oficial vigente.** Invocar:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763",
  format: "text"
)
```
Extraer: fecha del texto consolidado vigente del Codigo Civil; redaccion actual de los arts. 81, 82, 86, 87 (via judicial vs notarial y plazo de tres meses), 90 (contenido del convenio), 92 a 97 (guarda y custodia, alimentos, visitas, efectos economicos, vivienda, pension compensatoria).

Consultar tambien la LEC:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-2000-323",
  format: "text"
)
```
Extraer: redaccion vigente del art. 777 (separacion o divorcio de mutuo acuerdo: documentos, ratificacion, Ministerio Fiscal, sentencia).

**1.3 — Comparar.** Contrastar la version oficial con la registrada localmente y con el texto de las references.

**1.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la version oficial es posterior o el texto de los articulos ha cambiado, usar las herramientas de escritura (Write/Edit) para:
- Actualizar el contenido afectado en `references/cc-convenio-regulador-art90.md`, `references/cc-divorcio-separacion-art81-87.md` y/o `references/lec-proceso-mutuo-acuerdo-art777.md` con la redaccion vigente.
- Si cambia la estructura legal del convenio o de la demanda, actualizar `assets/convenio-regulador.md` y/o `assets/demanda-divorcio-mutuo-acuerdo.md`.
- Actualizar la tabla "Version registrada" y las fechas en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_document` falla (error HTTP, timeout):
```
web_search("Codigo Civil articulo 90 convenio regulador LEC articulo 777 mutuo acuerdo texto consolidado BOE")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente del Codigo Civil / LEC en el BOE. Los documentos se generan con la version de referencia. Verificar manualmente antes de presentar o firmar."

### Paso 2 — Preguntas al usuario (una pregunta por bloque si no las ha proporcionado)

El agente no redacta nada hasta recoger estos datos:

**Bloque A — Alcance y tipo de ruptura:**
"Desea (1) separacion o (2) divorcio? Y necesita (a) solo el convenio regulador, o (b) tambien la demanda de mutuo acuerdo para presentar en el juzgado?"

**Bloque B — Hijos (determina la via):**
"Tienen hijos en comun menores de edad no emancipados, o hijos con discapacidad que dependan de ustedes? (si / no). Si los hay, indique nombre, fecha de nacimiento y situacion de cada uno."

Segun la respuesta:
- Si hay hijos menores o dependientes: informar de que la via es judicial con intervencion del Ministerio Fiscal (Art. 777 LEC) y que la demanda es necesaria.
- Si no los hay: informar de que cabe la via notarial o ante el Letrado de la Administracion de Justicia (mas agil), sin perjuicio de optar por la judicial. Preguntar por que via desean.

**Bloque C — Datos de los conyuges:**
- De cada conyuge: nombre completo, DNI, domicilio actual.
- Fecha y lugar de celebracion del matrimonio.
- Regimen economico: sociedad de gananciales o separacion de bienes.

**Bloque D — Hijos: custodia, visitas y alimentos (solo si hay hijos):**
- Modalidad de guarda y custodia: exclusiva de un progenitor o compartida. Ejercicio de la patria potestad (normalmente conjunta).
- Regimen de visitas, estancias y comunicacion del progenitor no custodio (o reparto en la compartida).
- Pension de alimentos: importe mensual por hijo, dia de pago, cuenta, actualizacion (IPC) y reparto de gastos extraordinarios.

**Bloque E — Vivienda familiar:**
- Titularidad de la vivienda (propia de uno, comun, alquilada).
- A quien se atribuye el uso y por que plazo o condicion.

**Bloque F — Liquidacion del regimen economico:**
- Si desean liquidar en el mismo convenio los bienes y deudas comunes, y su reparto.
- Si lo dejan para un momento posterior.

**Bloque G — Pension compensatoria:**
"Existe un desequilibrio economico entre ustedes derivado de la ruptura (por ejemplo, por dedicacion a la familia o diferencia de ingresos)? Si es asi, indique importe, si es temporal o indefinida, y forma de pago. Si no, se hara constar la renuncia mutua."

### Paso 3 — Validacion previa

Antes de redactar, validar:

a) **Acuerdo y plazo (Art. 81 CC):** que ambos conyuges consienten y que han transcurrido tres meses desde el matrimonio (salvo excepcion por riesgo). Si falta el acuerdo, no procede el mutuo acuerdo.

b) **Via correcta (Arts. 82, 87 CC y Art. 777 LEC):** con hijos menores o dependientes, via judicial; sin ellos, notarial/LAJ o judicial. Confirmar la elegida.

c) **Contenido minimo del convenio (Art. 90.1 CC):** que se cubren todos los extremos aplicables. Los no aplicables, mencionar que no proceden.

d) **Interes del menor y equilibrio (Art. 90.2 CC):** que ninguna clausula es danina para los hijos ni gravemente perjudicial para un conyuge.

e) **Competencia (via judicial):** identificar el Juzgado de Primera Instancia del ultimo domicilio comun o del domicilio de cualquiera de los conyuges.

### Paso 4 — Generacion de los documentos

Generar siempre el convenio regulador:
```
draft_markdown(
  template_id: "convenio-regulador",
  variables: {
    todos los datos recogidos en los bloques A-G
  }
)
```

Si el usuario ha pedido tambien la demanda (via judicial, o eleccion en Bloque A), generar ademas:
```
draft_markdown(
  template_id: "demanda-divorcio-mutuo-acuerdo",
  variables: { datos de los conyuges, matrimonio, hijos, partido judicial, relacion de documentos }
)
```

Activar o desactivar los bloques condicionales del asset segun el caso: con hijos menores / sin hijos; gananciales / separacion de bienes; con pension compensatoria / con renuncia. Rellenar todos los campos con los datos reales. Los que el usuario no haya proporcionado quedan como `[DATO — PENDIENTE DE COMPLETAR]`.

Aplicar el estilo de `references/estilo-redaccion-escritos.md`: clausulas numeradas por materia del Art. 90, importes en numero y letra con sistema de actualizacion expreso, demanda breve remitida al convenio, voz activa y sin latinismos.

### Paso 5 — Revision final y advertencias

Verificar que cada documento generado:
- Tiene el header DRAFT.
- Incluye la fecha de verificacion normativa (del Paso 1).
- Identifica correctamente a ambos conyuges y, si procede, a los hijos y el juzgado competente.
- Cubre todos los extremos aplicables del Art. 90 y coincide con la via elegida.
- Sigue el estilo de redaccion clara (clausulas o hechos numerados, una idea por parrafo).

Entregar los documentos y anadir al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado antes de su presentacion o firma.
2. Version del Codigo Civil y de la LEC verificada: [fecha extraida en Paso 1].
3. El plazo minimo para separarse o divorciarse es de tres meses desde la celebracion del matrimonio (Art. 81 CC), salvo excepcion por riesgo.
4. Con hijos menores o con discapacidad dependientes, la via es judicial y el Ministerio Fiscal informa sobre las medidas que les afectan (Art. 777 LEC).
5. El convenio no produce plenos efectos hasta su aprobacion por sentencia (via judicial) o su formalizacion ante notario o Letrado de la Administracion de Justicia (via extrajudicial).
6. El juez, notario o Letrado no aprobaran clausulas daninas para los hijos ni gravemente perjudiciales para un conyuge (Art. 90.2 CC).
7. Deben acompanarse el convenio, la certificacion de matrimonio y las certificaciones de nacimiento de los hijos (Art. 777.2 LEC).
```

## Como NO se usa esta skill

- No usar para separacion o divorcio contencioso (sin acuerdo entre los conyuges).
- No usar para la nulidad matrimonial.
- No usar para modificar medidas ya acordadas o fijadas en sentencia anterior: procede una demanda de modificacion de medidas.
- No usar para ejecutar un convenio incumplido ni para reclamar pensiones impagadas.
- No usar para parejas de hecho no casadas (regimen y procedimiento distintos).
- No usar si el usuario pide opinion juridica sobre un conflicto familiar con hijos: derivar a `escalate_to_attorney`.

## Escalacion

| Situacion | Accion |
|---|---|
| No hay acuerdo entre los conyuges sobre alguno de los extremos | Advertir que no procede el mutuo acuerdo y ofrecer escalacion (procedimiento contencioso) |
| Indicios de violencia, coaccion o desequilibrio grave de poder entre los conyuges | Detener la redaccion y escalar via escalate_to_attorney |
| Hijos con discapacidad o situacion de especial vulnerabilidad | Advertir de la intervencion reforzada del Ministerio Fiscal y ofrecer escalacion |
| Regimen economico complejo (empresas, inmuebles en varios paises, deudas relevantes) | Advertir de la conveniencia de asesoramiento y ofrecer escalacion |
| Matrimonio sujeto a derecho civil foral (Cataluna, Aragon, Navarra, Pais Vasco, Baleares, Galicia) | Verificar la norma autonomica con web_search y advertir |
| Duda sobre la via aplicable o sobre el interes del menor | Elegir la posicion conservadora (via judicial) y ofrecer escalacion |
