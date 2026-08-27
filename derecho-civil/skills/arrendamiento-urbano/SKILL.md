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
assets:
  - assets/contrato-arrendamiento-vivienda.md
  - assets/contrato-arrendamiento-local.md
---

# Generar Contrato de Arrendamiento

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

## 2. VERIFICACIÓN NORMATIVA BOE (Interno)

Una vez completado el Enrutamiento (Punto 1), no hagas más preguntas al usuario. Ejecuta de inmediato:
1. Consulta la información en `lau-vivienda-plazos-renta-fianza.md` y `lau-derechos-obligaciones-partes.md` directamente desde el bloque `<document kind="references-collection">` de tu system prompt (TIENES ESTRICTAMENTE PROHIBIDO usar la herramienta `read_file` para leer references o assets).
2. Consulta en vivo mediante `web_search("Ley 29/1994 arrendamientos urbanos texto consolidado BOE")` la última modificación vigente del BOE.
3. Si hay cambios normativos relevantes, aplícalos a tu memoria. Si falla la búsqueda, usa las referencias cargadas en el prompt como respaldo e informa al usuario.

---

## 3. CREACIÓN DEL DOCUMENTO BASE (Cero Vacíos)

Inmediatamente después de la verificación normativa (Punto 2), estás OBLIGADO a crear el documento en disco.
1. Toma el texto íntegro de la plantilla seleccionada (`contrato-arrendamiento-vivienda.md` o `contrato-arrendamiento-local.md`), ubicada directamente en el bloque `<document kind="assets-collection">` de tu system prompt (NO uses la herramienta `read_file` para leer plantillas).
2. Reemplaza en memoria las variables de clasificación y CUALQUIER OTRO DATO que ya poseas gracias a la escucha activa inicial (nombres, dirección, etc.).
3. Utiliza `Write` (o `create_file`) para guardar el archivo completo en disco del workspace. Los datos faltantes deben quedar intactos como `{{DATO_FALTANTE}}`.
4. (Regla Global): Ejecuta `read_file` exclusivamente sobre el archivo creado en disco para validar y confirma la ruta absoluta en el chat al usuario. Inmediatamente después, en la misma respuesta, formula la primera pregunta de la edición incremental (Punto 4, sección 1: Ubicación y Zona Tensionada) para iniciar el ajuste detallado.

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

### Límites Legales (Guardrails de Dominio)
- **Duración:** Si V3 (Arrendador) = Física -> mínimo 5 años. Si V3 = Jurídica -> mínimo 7 años. (Art. 9.1 LAU).
- **Gastos:** Gastos de gestión/formalización siempre a cargo del arrendador (Art. 20.1 LAU).
- **Zonas Tensionadas:** Aplicar límites de renta Arts. 17.6 y 17.7 LAU si aplica.

---

## BUCLE DE REALIMENTACIÓN FINAL

Tras completar el Punto 4, muestra el siguiente menú y espera instrucciones (aplicando `Edit` según corresponda):
1. Ajustar una cláusula existente.
2. Añadir una cláusula adicional.
3. Eliminar una cláusula opcional.
4. Corregir un dato.
5. Cerrar y dar el contrato por bueno.

*(Al cerrar, emite las advertencias estándar: DRAFT, necesidad de revisión por abogado colegiado, depósito autonómico de fianza y registro de la propiedad).*
