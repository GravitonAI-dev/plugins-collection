---
name: juicio-ordinario
description: >
  Prepara de principio a fin un juicio ordinario civil conforme a la Ley de Enjuiciamiento Civil (LEC)
  en su version consolidada vigente verificada en el BOE. Cubre el ciclo completo por fases y genera el
  documento de cada una: intake del caso, comprobacion de admisibilidad (ambito del Art. 249, cuantia,
  competencia, postulacion de abogado y procurador, y requisito de MASC de la LO 1/2025), demanda del
  Art. 399 con sus documentos, guion de la audiencia previa (Arts. 414-430), proposicion de prueba
  (Art. 429 y 281-386) y minuta de conclusiones (Art. 433). NO usar para asuntos atribuidos al juicio
  verbal por la materia o por cuantia igual o inferior a 15.000 euros, para procesos especiales
  (familia, sucesiones contenciosas, division de patrimonios, monitorio, cambiario), ni para redactar
  la contestacion, la reconvencion o los recursos del demandado.
when_to_use: |
  - El usuario quiere demandar en un juicio ordinario civil (cuantia superior a 15.000 euros o materia del Art. 249.1).
  - El usuario necesita determinar si su asunto se tramita por juicio ordinario y preparar la demanda.
  - El usuario esta en un juicio ordinario ya iniciado y necesita el guion de la audiencia previa, la proposicion de prueba o las conclusiones.
  - El usuario pide una demanda de juicio ordinario del Art. 399 LEC con sus documentos.
inputs:
  - origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)
  - fase: intake / admisibilidad / demanda / audiencia-previa / proposicion-prueba / conclusiones (o ciclo completo)
  - materia: descripcion de la pretension y de la accion que se ejercita
  - via_ordinario: por la materia (Art. 249.1) / por la cuantia (Art. 249.2, superior a 15.000 euros)
  - naturaleza_actor: persona fisica o persona juridica
  - datos_actor: nombre o razon social, NIF o CIF, domicilio a efectos de notificaciones
  - naturaleza_demandado: persona fisica o persona juridica
  - datos_demandado: nombre o razon social, NIF o CIF, domicilio donde pueda ser emplazado
  - hechos: relato ordenado de los hechos en que se funda la pretension
  - cuantia: interes economico de la demanda y su justificacion (Arts. 251-253)
  - documentos: documentos fundamentales de la accion y dictamenes periciales disponibles (Arts. 265, 336)
  - partido_judicial: fuero aplicable (domicilio del demandado, lugar del inmueble, domicilio del consumidor, etc.)
  - postulacion: datos del procurador y del abogado (preceptivos, Arts. 23 y 31)
  - masc_intentado: si se ha intentado un medio adecuado de solucion de controversias (si / no)
  - hechos_controvertidos: solo para audiencia previa, prueba y conclusiones; hechos discutidos por el demandado
outputs:
  - checklist_admisibilidad: comprobacion de ambito, cuantia, competencia, postulacion y MASC, en markdown, DRAFT
  - demanda_juicio_ordinario: demanda del Art. 399 LEC en markdown, DRAFT
  - guion_audiencia_previa: guion / escrito de preparacion de la audiencia previa en markdown, DRAFT
  - proposicion_prueba: proposicion de prueba ordenada por medios en markdown, DRAFT
  - escrito_conclusiones: minuta de conclusiones (Art. 433) en markdown, DRAFT
references:
  - references/admisibilidad-competencia-postulacion-masc.md
  - references/estilo-redaccion-escritos.md
  - references/fuentes-plantillas-validadas.md
  - references/lec-ambito-y-cuantia.md
  - references/lec-audiencia-previa.md
  - references/lec-demanda-y-documentos.md
  - references/lec-prueba-y-conclusiones.md
assets:
  - assets/template-checklist-admisibilidad.md
  - assets/template-demanda-juicio-ordinario.md
  - assets/template-escrito-de-conclusiones.md
  - assets/template-guion-audiencia-previa.md
  - assets/template-proposicion-de-prueba.md
---

# Preparar un Juicio Ordinario Civil (ciclo completo)

> DRAFT — para revisión por un abogado colegiado antes de su firma. No constituye asesoramiento jurídico definitivo.

---

## Directivas Operacionales y Vectores de Estado Internos

Esta skill guía al usuario de manera consultiva, rigurosa y transparente a través de un procedimiento estructurado en 5 fases secuenciales.

### Vectores de Estado (Uso Estrictamente Interno):

Para garantizar un enrutamiento determinista y el cumplimiento normativo riguroso, el asistente resuelve y mantiene internamente en memoria los vectores de estado de la operación (V1 a V4) y el origen de la plantilla (V5).

> **REGLA DE INVISIBILIDAD EN CHAT (Global CLAUDE.md):**
> Los identificadores técnicos de los vectores (`V1`, `V2`, `V3`, `V4`, `V5`) y los resúmenes de validación con marcas (ej. "V1 resuelto ✔") son **estrictamente de control interno**. Tienes **PROHIBIDO** mencionarlos o imprimirlos en el chat visible al usuario. Comunícate siempre en lenguaje natural cordial y profesional.

---

## FASE 1 — CLASIFICACIÓN INICIAL (Resolución de Vectores V1 a V4 mediante Formulario HITL)

Tu primer objetivo es clasificar con precisión la naturaleza del caso y fijar los vectores deterministas de estado.

### 1.1 Escucha Activa Previa
Antes de abrir formularios interactivos o hacer preguntas, analiza el mensaje inicial del usuario y la documentación aportada:
- Si el mensaje ya especifica inequívocamente los vectores de la operación, asígnalos de forma inmediata y silenciosa en memoria y pasa a la **Fase 2**.
- Si restan vectores por definir, no formules preguntas abiertas en turnos sucesivos: presenta el formulario estructurado interactivo mediante la herramienta `restricted_human_in_the_loop_request`.

### 1.2 Formulario de Clasificación (`restricted_human_in_the_loop_request`)
Presenta al usuario las opciones estructuradas para resolver los vectores pendientes:
```json
{
  "type": "object",
  "properties": {
    "fase_procesal": {
      "type": "string",
      "description": "Fase procesal requerida (V1)",
      "enum": [
        "demanda",
        "checklist_admisibilidad",
        "audiencia_previa",
        "proposicion_prueba",
        "escrito_conclusiones"
      ]
    },
    "via_ordinario": {
      "type": "string",
      "description": "Criterio de atribuci\u00f3n al juicio ordinario (V2)",
      "enum": [
        "materia",
        "cuantia"
      ]
    },
    "masc_previo": {
      "type": "string",
      "description": "Intento de MASC previo a la demanda (V3)",
      "enum": [
        "si_intentado",
        "no_intentado"
      ]
    }
  },
  "required": [
    "fase_procesal",
    "via_ordinario"
  ]
}
```

### 1.3 Enrutamiento de Estado (Routing por Vectores)
Antes de redactar la demanda, completar la comprobacion de admisibilidad (asset `checklist-admisibilidad.md`) validando:

a) **Clase de juicio (Art. 249):** confirmar que procede el ordinario, por la materia (Art. 249.1) o por cuantia superior a 15.000 euros o interes incalculable (Art. 249.2). Si corresponde al verbal, no procede esta skill: advertir y derivar (para reclamaciones de renta o desahucio, derivar a `desahucio`; para deuda dineraria liquida por monitorio, a `monitorio`).

b) **Determinacion de la cuantia (Arts. 251-253):** fijar el interes economico y justificarlo. La cuantia se expresa en la demanda (Art. 253).

c) **Competencia (Arts. 45, 50-52):** identificar el organo (Juzgado de Primera Instancia o, en su caso, de lo Mercantil) y el fuero territorial. Advertir de los fueros imperativos (inmuebles, consumidores) donde no cabe sumision.

d) **Postulacion (Arts. 23 y 31):** confirmar que se cuenta con procurador y abogado. Sin ellos, no puede seguirse el ordinario.

e) **MASC (Art. 403.2, 264.4, 399.3 — LO 1/2025):** confirmar el intento previo o la concurrencia de una excepcion. Por defecto conservador, recomendar acreditar el intento previo para evitar la inadmision.

f) **Documentos (Arts. 264-266, 336) y preclusion (Art. 269):** verificar que se dispone de los documentos fundamentales y de los dictamenes periciales para acompanarlos con la demanda.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y NEGOCIACIÓN DE ASSETS (Vía Chat — Resolución de V5)

En esta fase interactúas **directamente a través del chat (en texto plano conversacional, SIN formularios)** para compartir el plan de trabajo, el fundamento normativo y acordar la plantilla base con el usuario.

### 2.1 Verificación Normativa Interna
1. Consulta las referencias jurídicas cargadas en tu contexto (carpeta `references/`).
2. Opcionalmente verifica en vivo mediante `web_search` la legislación consolidada en el BOE si se requieren confirmar índices o modificaciones normativas recientes.

### 2.2 Mensaje de Plan de Acción y Consulta de Assets
Envía un mensaje estructurado y formal que contenga:
1. **Marco Legal Aplicable:** Artículos 249, 399, 403, 414-433 de la Ley de Enjuiciamiento Civil (LEC), reformada por Real Decreto-ley 6/2023 (umbral de 15.000 €) y Ley Orgánica 1/2025 de eficiencia procesal (MASC como requisito de admisibilidad).
2. **Orientación Legal del Caso:**
La skill se actualiza a si misma en cada lanzamiento: comprueba las fuentes oficiales y, si detecta una version posterior, reescribe sus propios archivos (references y assets) antes de redactar. Ejecutar SIEMPRE esta secuencia:

**1.2 — Consultar la fuente oficial vigente en vivo.** Invocar:
```
read_file(...) o web_search(...)
```
Extraer: fecha del texto consolidado vigente de la LEC; redaccion actual de los arts. 248-255 (ambito y cuantia), 23 y 31 (postulacion), 45 y 50-52 (competencia), 399 y 264-266, 269-270, 336 (demanda y documentos), 414-430 (audiencia previa), 217 y 281-386, 429 (prueba) y 433 (conclusiones); el umbral vigente de cuantia entre juicio verbal y ordinario; y el estado de aplicacion de la LO 1/2025 (BOE-A-2025-76) sobre el requisito de MASC (arts. 403.2, 264.4 y 399.3).

Consultar tambien sobre MASC:
```
web_search("BOE-A-2025-76 LO 1/2025 MASC requisito procedibilidad articulo 403 264 399 LEC texto consolidado")
```

**1.3 — Comparar.** Contrastar la version oficial con la registrada en `fuentes-plantillas-validadas.md` y con las referencias del prompt (`lec-ambito-y-cuantia.md`, `admisibilidad-competencia-postulacion-masc.md`, `lec-demanda-y-documentos.md`, `lec-audiencia-previa.md`, `lec-prueba-y-conclusiones.md`). Prestar especial atencion al umbral de cuantia del Art. 249.2 y al requisito de MASC.

**1.4 — Aplicar cambios normativos.** Si la version oficial es posterior o el texto de los articulos ha cambiado:
- Aplicar en memoria la redaccion vigente para adaptar los tramites, fases procesales y fundamentacion de los escritos.
- Informar brevemente al usuario de que se detecto y aplico una version mas reciente (norma y fecha).

No redactar ningun documento hasta haber completado esta actualizacion. Nunca usar una version desactualizada.

**1.5 — Fallback si la fuente no es accesible.** Si `read_file` falla (error HTTP, timeout):
```
web_search("Ley Enjuiciamiento Civil juicio ordinario articulo 249 399 audiencia previa 414 texto consolidado BOE")
```
y
```
web_search("LO 1/2025 MASC requisito procedibilidad articulo 403 264 399 LEC texto consolidado")
```
Si tambien falla: usar las references locales como respaldo y notificar al usuario:
"No se pudo verificar la version vigente de la LEC en el BOE. Los documentos se generan con la version de referencia. Verificar manualmente antes de presentar."
3. **Propuesta de Plantilla Oficial del Sistema:** Detalla que dispones de la plantilla oficial validada (`assets/template-checklist-admisibilidad.md`).
4. **Pregunta Explícita al Usuario (Vía Chat):** Formula exactamente la siguiente consulta en el chat:
   > *"¿Desea que utilicemos la plantilla base propuesta por el sistema o prefiere aportar su propia plantilla/minuta para trabajar sobre ella adjuntándola en el chat?"*

### 2.3 Fijación de V5 (Origen Plantilla) y Manejo de la Elección
* **Si `[V5 = plantilla_sistema]` (El usuario acepta la plantilla propuesta):**
  Toma el texto íntegro de la plantilla correspondiente directamente desde el catálogo del prompt y procede de inmediato a la **Fase 3**.
* **Si `[V5 = plantilla_usuario]` (El usuario aporta su propia minuta adjuntando un documento o pegando texto):**
  1. Accede al contenido del adjunto desde `<attached_documents>` o el mensaje del usuario.
  2. **Guardrail de Verificación Legal:** Analiza el texto aportado. Si contiene cláusulas nulas, contrarias a normas imperativas o de imposible cumplimiento, adviértelo expresamente en el chat y propón la redacción legalmente válida.
  3. Adopta la minuta revisada como base y avanza a la **Fase 3**.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (Zero Vacíos)

1. **Escritura del Documento (`create_file`):**
   - Vuelca íntegramente la plantilla acordada en un archivo en el workspace con nombre en `snake_case.md`.
   - Aplica el principio **Zero-Omission**: sustituye los datos ya conocidos e inserta `{{DATO_FALTANTE}}` para aquellos que deban resolverse durante la redacción.
   - PROHIBIDO dejar archivos en blanco, crear resúmenes o esquemas provisionales.
2. **Validación de Integridad (`read_file`):**
   - Ejecuta inmediatamente `read_file` sobre el archivo recién creado para comprobar que el volcado es íntegro y que el archivo existe en disco.
3. **Confirmación en Chat y Encadenamiento Inmediato:**
   - Informa al usuario de la ruta absoluta del documento creado.
   - En esa **misma respuesta**, introduce la primera sección/cláusula de la **Fase 4** y formula ya su primera pregunta, sin detener el flujo.

---

## FASE 4 — EDICIÓN INCREMENTAL CLÁUSULA A CLÁUSULA / SECCIÓN A SECCIÓN

### Protocolo Obligatorio de Edición
Para cada cláusula o bloque temático del documento, ejecuta estrictamente el siguiente ciclo interactivo:
```
[Pregunta al Usuario] ──> [Vista Previa en texto plano] ──> [¿Confirmamos?] ──> [edit_file + read_file]
```
1. **Pregunta en Chat:** Solicita los datos específicos de la sección.
2. **Vista Previa:** Muestra el texto exacto redactado en texto plano en el chat.
3. **Confirmación:** Consulta al usuario si está conforme o desea algún ajuste.
4. **Persistencia en Disco:** Una vez confirmado, ejecuta `edit_file` con `old_string` y `new_string` exactos, y verifica con `read_file`.

### Hoja de Ruta de Secciones y Cláusulas Condicionales

1. **Encabezamiento y Postulación** *(confirmación agrupada)*: Juzgado de Primera Instancia competente (arts. 45 y 50-52 LEC), datos completos del demandante, datos del procurador y letrado directores (arts. 23 y 31 LEC), datos del demandado y domicilio a efectos de emplazamiento.
2. **Hechos de la Demanda**: relato cronológico, estructurado y numerado de los hechos que fundamentan la pretensión, con invocación expresa de los documentos acompañados (art. 265 LEC) y acreditación del intento de MASC previo (art. 403.2 LEC / LO 1/2025).
3. **Fundamentos de Derecho Procesales**: competencia del juzgado, capacidad y legitimación de las partes (arts. 6 y 10 LEC), representación procesal y defensa técnica (arts. 23 y 31 LEC), procedimiento aplicable por razón de la materia o cuantía (art. 249 LEC).
4. **Fundamentos de Derecho Materiales o de Fondo**: normativa sustantiva aplicable al negocio jurídico litigioso (Código Civil, leyes especiales), jurisprudencia consolidada aplicable, intereses legales o convencionales y costas procesales (art. 394 LEC).
5. **Fijación de la Cuantía**: determinación económica justificada del litigio conforme a las reglas de los arts. 251 a 253 LEC.
6. **Suplico de la Demanda**: pronunciamientos judiciales pedidos con estricta claridad y separación (declaración, condena de dar/hacer/no hacer, restitución de cantidades, intereses y costas).
7. **Fases Posteriores del Ciclo (Documentos complementarios bajo demanda)**:
   - Audiencia Previa (`template-guion-audiencia-previa.md`): acuerdo, cuestiones procesales (arts. 416-425 LEC), fijación de hechos controvertidos y prueba (art. 429 LEC).
   - Proposición de Prueba (`template-proposicion-de-prueba.md`): relación ordenada de medios de prueba (art. 299 LEC) con pertinencia y utilidad.
   - Conclusiones (`template-escrito-de-conclusiones.md`): valoración oral/escrita de la prueba practicada conforme a la carga probatoria (art. 217 LEC).

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE

Una vez completadas todas las secciones del documento, presenta al usuario un menú interactivo:
```
1. Modificar o ajustar una cláusula o sección existente.
2. Añadir una estipulación o pacto adicional a medida.
3. Eliminar contenido opcional o corregir datos de partes/fincas.
4. Revisar la coherencia global y realizar control de calidad final.
5. Dar el documento por finalizado y cerrar la sesión.
```
### Advertencias Legales Preceptivas de Cierre:
Al dar por finalizado el documento, emite siempre las siguientes advertencias:
- **Carácter DRAFT:** El documento generado es un borrador profesional que debe ser revisado por un abogado colegiado antes de su firma o presentación procesal.
- **Obligaciones Fiscales y Plazos:** Recuerda los plazos de liquidación de tributos (ITP/AJD o Plusvalía municipal en 30 días hábiles) cuando proceda.
- **Elevación a Instrumento Público:** Recuerda que para la inscripción en el Registro de la Propiedad o Mercantil, o para su ejecución forzosa directa, es necesario el otorgamiento ante Notario público.

---

## Límites Legales y Guardrails de Dominio (Gobernados por Vectores)

1. Verificar siempre la LEC en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version de la LEC posterior a la registrada en las references, aplicar la redacción vigente directamente sobre el documento a redactar en el workspace del usuario. No usar una version desactualizada. El umbral de cuantia (15.000 euros desde el 20/03/2024, RDL 6/2023) y el requisito de MASC (LO 1/2025) han cambiado recientemente: confirmar siempre la redaccion vigente.
3. Determinar correctamente la clase de juicio: procede el ordinario por la materia (Art. 249.1) o por cuantia superior a 15.000 euros o de interes incalculable (Art. 249.2). Si el asunto corresponde al juicio verbal (materia del Art. 250.1 o cuantia igual o inferior a 15.000 euros), no usar esta skill: advertir y derivar.
4. Postulacion preceptiva: en el juicio ordinario son obligatorios abogado y procurador (Arts. 23 y 31). Nunca redactar la demanda como si pudiera presentarse sin ellos.
5. Competencia: identificar el fuero aplicable (Arts. 45, 50-52). No admitir sumision en fueros imperativos (inmuebles, consumidores). Marcar la jurisdiccion asumida.
6. Posicion conservadora sobre el MASC: la LO 1/2025 exige acreditar el intento previo de un medio adecuado de solucion de controversias como requisito de procedibilidad (Art. 403.2 LEC). Ante la duda, recomendar e integrar el intento previo y advertir de la cuestion (riesgo de inadmision, Art. 403.2).
7. Documentos y preclusion: advertir SIEMPRE de que los documentos fundamentales de la accion y los dictamenes periciales deben acompanarse con la demanda (Arts. 265, 336) y de la preclusion del Art. 269. No admitir aportacion tardia salvo los supuestos del Art. 270.
8. Carga de la prueba (Art. 217): al preparar la prueba y las conclusiones, atribuir a cada parte la carga que le corresponde. Nunca afirmar que un hecho esta probado sin base en las pruebas practicadas.
9. Los campos a rellenar usan el placeholder propio del asset en doble llave, p. ej. `{{cuantia_reclamada}}` (NUNCA corchete simple `[DATO]`: colisiona con los identificadores de privacidad `[PERSON_1]`). Si hace falta marcar un hueco suelto sin placeholder propio, usa `{{DATO_FALTANTE}}` una sola vez por documento: nunca lo repitas para dos datos distintos, porque el `Edit` posterior necesita un `oldString` unico. Nunca inventar datos, cuantias, fechas ni referencias catastrales. Nunca inventar jurisprudencia.
