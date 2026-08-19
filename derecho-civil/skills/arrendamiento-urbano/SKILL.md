---
name: arrendamiento-urbano
description: >
  Genera un contrato de arrendamiento urbano completo (vivienda habitual o local de negocio)
  entre arrendador y arrendatario, aplicando la Ley 29/1994 de Arrendamientos Urbanos (LAU)
  en su version consolidada vigente verificada en el BOE. Adapta las clausulas segun la
  naturaleza de las partes (persona fisica o juridica) y la ubicacion del inmueble.
  NO usar para arrendamientos de finca rustica, viviendas turisticas, contratos de temporada,
  viviendas militares, ni viviendas de porteros o guardas.
when_to_use: |
  - El usuario quiere redactar un contrato de alquiler de vivienda o local.
  - El usuario proporciona datos de arrendador, arrendatario e inmueble.
  - El usuario pide que el contrato cumpla con la LAU.
inputs:
  - tipo_inmueble: vivienda habitual o local de negocio / uso distinto de vivienda
  - naturaleza_arrendador: persona fisica o persona juridica
  - naturaleza_arrendatario: persona fisica o persona juridica
  - datos_arrendador: nombre o razon social, NIF o CIF, domicilio
  - datos_arrendatario: nombre o razon social, NIF o CIF, domicilio
  - datos_inmueble: direccion completa, referencia catastral, descripcion, comunidad autonoma, municipio
  - renta_mensual: importe en euros
  - duracion: anos pactados o "minimo legal"
  - fianza: mensualidades o "segun ley"
  - fecha_inicio: fecha de inicio del contrato
  - clausulas_adicionales: opcionales, a peticion del usuario
outputs:
  - contrato_arrendamiento: contrato completo en markdown, DRAFT, con todas las clausulas LAU
references:
  - references/lau-vivienda-plazos-renta-fianza.md
  - references/lau-derechos-obligaciones-partes.md
  - references/lau-arrendamiento-local-negocio.md
  - references/fuentes-plantillas-validadas.md
assets:
  - assets/contrato-arrendamiento-vivienda.md
  - assets/contrato-arrendamiento-local.md
---

# Generar Contrato de Arrendamiento

> DRAFT — para revision por un abogado colegiado antes de su firma. No constituye asesoramiento juridico.

## Guardrails

1. Verificar siempre la LAU en el BOE antes de redactar. Sin verificacion, no proceder.
2. Si se detecta en el BOE una version de la LAU posterior a la registrada en las references, actualizar los archivos del plugin antes de redactar (ver Paso 2). No usar una version desactualizada.
3. Duracion minima: 5 anos si el arrendador es persona fisica, 7 anos si es persona juridica (Art. 9.1 LAU). No pactar plazos inferiores sin advertir de la prorroga obligatoria.
4. Gastos de gestion y formalizacion del contrato siempre a cargo del arrendador (Art. 20.1 LAU).
5. En zonas de mercado residencial tensionado, aplicar los limites de renta de los Arts. 17.6 y 17.7 LAU si el usuario confirma que el inmueble esta en una zona declarada como tal.
6. Fianza minima: 1 mensualidad en vivienda, 2 mensualidades en local de negocio (Art. 36 LAU). No admitir fianzas inferiores.
7. Marcar todos los campos a rellenar con `{{DATO_FALTANTE}}`. Nunca inventar datos, rentas, fechas ni referencia catastral.
8. Nunca redactar clausulas que contravengan normas imperativas de la LAU. Nunca inventar jurisprudencia.

**DIRECTIVA DE INVISIBILIDAD (Chat Limpio):**
Toda la lógica descrita en este documento (la clasificación de vectores V1-V4, las secuencias numeradas, la verificación normativa y la creación del documento base) es un flujo de ejecución ESTRICTAMENTE INTERNO.
Tienes PROHIBIDO mencionar en el chat:
- Nombres de vectores (ej. "V1", "V2").
- Resúmenes de validación con checks (ej. "Finalidad: ✔").
- En qué fase de la instrucción te encuentras (ej. "Ahora pasaremos al punto 4", "Voy a proceder a crear el documento").
- Preámbulos conversacionales antes de hacer las preguntas de clasificación. Si es tu turno de preguntar, **emite únicamente la pregunta exacta y nada más**.

## 1. CLASIFICACIÓN DINÁMICA (Vectores de Estado)

Tu primer objetivo es resolver 4 vectores de clasificación de manera SILENCIOSA. 
Aplica la Escucha Activa Global para extraer estos datos de cualquier mensaje. 
**IMPORTANTE (Invisibilidad):** Los nombres de estos vectores (`V1`, `V2`, etc.) y el hecho de que estás validándolos son de uso estrictamente interno. **NUNCA los menciones en el chat.** No imprimas listas de validación ni resúmenes con "checks" (✔). Si extraes un dato con éxito, simplemente regístralo en tu memoria en silencio.

- **V1 (Finalidad):** Habitual (incluye: permanente, vivir, residencia) / Negocio estable / Temporada (vacacional) / Turístico.
- **V2 (Tipo Inmueble):** Vivienda (incluye: piso, casa, apartamento, chalet) / Local (incluye: nave, comercial).
- **V3 (Naturaleza Arrendador):** Física / Jurídica.
- **V4 (Naturaleza Arrendatario):** Física / Jurídica.

**REGLA ESTRICTA DE PREGUNTAS (Protocolo Predecible):**
Si, tras analizar el contexto, te falta resolver uno o más vectores, **TIENES PROHIBIDO inventar la redacción de la pregunta**. Debes formular **UNA SOLA PREGUNTA por turno**, utilizando EXACTAMENTE el texto que corresponda al vector faltante, en este orden estricto, **sin añadir preámbulos ni resúmenes de lo que ya sabes**:

*   **Para V1 (Finalidad):** "¿El uso previsto del inmueble es permanente en el tiempo, o es de temporada (vacacional, de verano, por trabajo temporal) o se trata de una vivienda turística gestionada como alojamiento?"
*   **Para V2 (Tipo Inmueble):** "¿El inmueble que se va a arrendar es una vivienda (cualquier tipo: piso, casa, chalet, apartamento) o un local de negocio / espacio para uso distinto de vivienda?"
*   **Para V3 (Naturaleza Arrendador):** "¿El arrendador es persona física o persona jurídica (empresa, sociedad)?"
*   **Para V4 (Naturaleza Arrendatario):** "¿Y el arrendatario, es persona física o persona jurídica?"

*(Si el usuario ya proporcionó la respuesta a un vector, OMITE la pregunta exacta correspondiente y evalúa el siguiente).*

### Enrutamiento de Estado (Routing)
Una vez resueltos los 4 vectores (V1 a V4), evalúa:
- Si [V1 = Temporada o Turístico] -> Detén el proceso (fuera de alcance LAU). No crees documento.
- Si [V1 = Habitual] Y [V2 = Vivienda] -> Plantilla a usar: `assets/contrato-arrendamiento-vivienda.md` (Fianza mínima: 1 mensualidad).
- Si [V1 = Habitual] Y [V2 = Local] -> Plantilla a usar: `assets/contrato-arrendamiento-local.md` (Fianza mínima: 2 mensualidades).

---

## 2. VERIFICACIÓN Y AUTO-ACTUALIZACIÓN NORMATIVA BOE (Interno)

Una vez completado el Enrutamiento (Punto 1), no hagas más preguntas al usuario. La skill se actualiza a sí misma en cada lanzamiento: comprueba la fuente oficial y, si detecta una versión posterior, reescribe sus propios archivos antes de redactar. Ejecuta SIEMPRE esta secuencia:

**2.1 — Leer la versión registrada localmente.** Abre `references/fuentes-plantillas-validadas.md` y anota la "Versión registrada" de la LAU.

**2.2 — Consultar la fuente oficial vigente.** Invoca:
```
read_document(
  path: "https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003",
  format: "text"
)
```
Extrae: fecha del texto consolidado vigente de la LAU; redacción actual de los arts. 9 (duración), 17 y 20 (renta y gastos), 27 (resolución) y 36 (fianza).

**2.3 — Comparar.** Contrasta la versión oficial con la registrada localmente y con el texto de las references.

**2.4 — Auto-actualizar los archivos del plugin (OBLIGATORIO si hay cambios).** Si la versión oficial es posterior o el texto de los artículos cambió, usa `Write`/`Edit` para:
- Actualizar el contenido afectado en `references/lau-vivienda-plazos-renta-fianza.md`, `references/lau-derechos-obligaciones-partes.md` y/o `references/lau-arrendamiento-local-negocio.md` con la redacción vigente.
- Actualizar la tabla "Versión registrada" y la fecha en `references/fuentes-plantillas-validadas.md`.
- Informar brevemente al usuario de que se detectó y aplicó una versión más reciente (norma y fecha).

No redactes ningún documento hasta haber completado esta actualización. Nunca uses una versión desactualizada.

**2.5 — Fallback si la fuente no es accesible.** Si `read_document` falla (error HTTP, timeout):
```
web_search("Ley 29/1994 Arrendamientos Urbanos texto consolidado BOE articulos 9 17 20 27 36")
```
Si también falla: usa las references locales como respaldo y notifica al usuario: "No se pudo verificar la versión vigente de la LAU en el BOE. El contrato se genera con la versión de referencia. Verificar manualmente antes de firmar."

---

## 3. CREACIÓN DEL DOCUMENTO BASE (Cero Vacíos)

Inmediatamente después de la verificación normativa (Punto 2), estás OBLIGADO a crear el documento en disco.
1. Utiliza `Read` para leer la plantilla seleccionada en el Punto 1 (`vivienda` o `local`).
2. Reemplaza en memoria las variables de clasificación y CUALQUIER OTRO DATO que ya poseas gracias a la escucha activa inicial (nombres, dirección, etc.).
3. Utiliza `Write` para guardar el archivo completo en disco. Los datos faltantes deben quedar intactos como `{{DATO_FALTANTE}}`.
4. (Regla Global): Ejecuta `Read` para validar y confirma la ruta absoluta en el chat al usuario. Inmediatamente después, en la misma respuesta, formula la primera pregunta de la edición incremental (Punto 4, sección 1: Ubicación y Zona Tensionada) para iniciar el ajuste detallado.

---

## 4. EDICIÓN INCREMENTAL DE CLÁUSULAS

Ahora, recorre secuencialmente la siguiente lista de cláusulas. Por cada cláusula de la que falten datos, aplica el Ciclo de Edición Incremental del sistema global (Formular Pregunta -> Mostrar Vista Previa en texto plano -> Pedir Confirmación -> Tras confirmación, usar `Edit` en disco):

1. **Ubicación y Zona Tensionada:** Comunidad autónoma, municipio. ¿Es zona tensionada? (Si no lo sabe, búscalo).
2. **Partes:** Nombre/Razón social, NIF/CIF, domicilio para notificaciones.
3. **Objeto:** Dirección completa, referencia catastral, m2, anexos (garaje, trastero).
4. **Duración:** Duración en años o "mínimo legal", fecha de inicio.
5. **Renta:** Importe mensual en euros, forma de pago, IBAN.
6. **Actualización:** Índice pactado o "según ley" (IGC).
7. **Fianza y Garantías:** Meses de fianza (verificar mínimo legal), garantías adicionales.
8. **Gastos y Suministros:** Quién paga IBI, comunidad (por defecto arrendador; suministros a cargo del inquilino).
9. **Pactos Opcionales:** Renuncia a adquisición preferente, correos electrónicos para notificaciones, mediación, cláusulas extra.

(Los límites legales de cada cláusula — duración, gastos, zonas tensionadas, fianza — están fijados en la sección Guardrails al inicio de este documento; no se redactan por fuera de esos límites.)

---

## BUCLE DE REALIMENTACIÓN FINAL

Tras completar el Punto 4, muestra el siguiente menú y espera instrucciones (aplicando `Edit` según corresponda):
1. Ajustar una cláusula existente.
2. Añadir una cláusula adicional.
3. Eliminar una cláusula opcional.
4. Corregir un dato.
5. Cerrar y dar el contrato por bueno.

Al cerrar, añade al final:
```
Advertencias:
1. Este documento es un DRAFT generado automaticamente. Debe ser revisado por un abogado colegiado antes de su firma.
2. Version de la LAU verificada: [fecha extraida en el Punto 2].
3. La fianza debe depositarse en el organismo autonomico correspondiente (Art. 36.3 LAU) segun la comunidad autonoma del inmueble.
4. Se recomienda la inscripcion del contrato en el Registro de la Propiedad para su oponibilidad frente a terceros.
```

## Como NO se usa esta skill

- No usar para arrendamientos de finca rústica (excluidos de la LAU, Art. 5.a).
- No usar para viviendas turísticas ni contratos de temporada (excluidos de la LAU, Art. 5.e y 3.2).
- No usar para viviendas militares, de porteros o guardas, ni las demás excluidas por el Art. 5 LAU.
- No usar para redactar la resolución o el desahucio derivado de un incumplimiento: para eso, derivar a la skill `desahucio`.
- No usar si el usuario pide opinión jurídica sobre un litigio ya existente entre las partes: derivar a `escalate_to_attorney`.

## Escalación

| Situación | Acción |
|---|---|
| Litigio o conflicto ya existente entre arrendador y arrendatario | Escalar vía `escalate_to_attorney` |
| Inmueble en zona de mercado residencial tensionado, con dudas sobre los límites de renta aplicables | Verificar con `web_search` la declaración autonómica vigente y advertir |
| Arrendatario o arrendador menor de edad o con discapacidad sin representación clara | Advertir de la necesidad de representación legal y escalar |
| Duda sobre normativa autonómica o foral que module la LAU | Usar `web_search` para verificar; si persiste la duda, advertir y escalar |
