# Reglas de Parametrización, Abstracción y Verificación de Plantillas (Assets)

> Material de referencia para la skill `registrar-plantillas`. Define las pautas metodológicas para procesar, crear asistidamente, verificar compatibilidad y persistir plantillas de documentos (assets) tanto para skills del sistema como globales de usuario.

---

## 0. Vías para Especificar Plantillas

Las únicas vías admitidas para proporcionar o generar el contenido de una plantilla son:

### 0.1 Texto en el Chat (Pegar Directamente)
- El usuario proporciona el texto de la minuta o modelo directamente en la conversación (`<user_message>`).
- Se extrae el texto del mensaje, se analiza su estructura y se parametriza a variables `{{VARIABLE}}`.

### 0.2 Abrir Archivo en el Editor (Archivos del Workspace)
- El usuario indica un archivo ya existente en el espacio de trabajo activo de la conversación (visible o abierto en el editor).
- El contenido auténtico del archivo se consulta prioritariamente en la sección `# WORKSPACE ACTIVE DOCUMENTS` (donde siempre se encuentra la última versión sincronizada). Solo se recurre a la herramienta `read_file` si es estrictamente necesario en algún caso extremo (ej. archivo no visible en dicha sección o contenido truncado):
  ```json
  {
    "relative_file_path": "ruta/al/archivo.md"
  }
  ```
- Si la plantilla es **Global (sin skill)** y el documento en el workspace se denomina como el `asset_name` canónico de una plantilla existente (ej. `template-modelo-de-demanda.md`), este canal constituye la vía de actualización directa mediante `update_user_template`.

### 0.3 Creación Asistida (Desde Cero)
- Cuando el usuario no dispone de un documento previo y desea construir una plantilla nueva desde cero con ayuda del asistente.
- El asistente conduce un diálogo estructurado y consultivo para diseñar la plantilla:
  1. **Finalidad y ámbito:** Identificar el tipo de documento (contrato, escrito judicial, comunicación formal, solicitud administrativa) y su propósito.
  2. **Intervinientes:** Definir las partes o sujetos y sus datos identificativos necesarios.
  3. **Cuerpo y cláusulas principales:** Estructurar las estipulaciones esenciales (objeto, plazos, condiciones económicas, obligaciones de las partes, penalizaciones, fuero y jurisdicción).
  4. **Identificación de variables dinámicas:** Asignar marcadores `{{NOMBRE_VARIABLE}}` a todos los datos variables que cambiarán entre usos.
  5. **Borrador en el editor (`create_file`):** Generar el archivo en el workspace para que el usuario pueda visualizar el documento en tiempo real en el editor.
  6. **Edición colaborativa incremental (`edit_file`):** Refinar y expandir cláusulas directamente en el documento del workspace.
  7. **Persistencia final:** Una vez validado y confirmado (preguntando al usuario: *"¿Quieres que guarde en la sección de plantillas?"*), guardar mediante `save_user_template` o `set_skill_template`.

> [!NOTE]
> **Sin adjuntos de archivos:** La skill NO procesa documentos adjuntos ni archivos subidos fuera del workspace. Toda entrada preexistente debe proceder exclusivamente de texto pegado en el chat o de un archivo abierto en el editor (workspace).

---

## 1. Parametrización y Abstracción de Datos Concretos a Variables

Al transformar un documento de muestra en una plantilla reutilizable o al crearla desde cero:
- **Nombres y Apellidos / Razones Sociales:** Sustituir por `{{NOMBRE_ARRENDADOR}}`, `{{NOMBRE_DEMANDANTE}}`, `{{RAZON_SOCIAL_EMPRESA}}`, `{{NOMBRE_REPRESENTANTE}}`.
- **Identificadores Fiscales (DNI/NIE/CIF):** Sustituir por `{{NIF_ARRENDADOR}}`, `{{DNI_DEMANDANTE}}`, `{{CIF_ENTIDAD}}`, `{{NIE_SOLICITANTE}}`.
- **Domicilios y Direcciones:** Sustituir por `{{DOMICILIO_NOTIFICACIONES}}`, `{{DIRECCION_INMUEBLE}}`, `{{MUNICIPIO}}`, `{{PROVINCIA}}`.
- **Fechas Concretas:** Sustituir por `{{FECHA_CONTRATO}}`, `{{FECHA_INICIO}}`, `{{FECHA_VENCIMIENTO}}`, `{{FECHA_NOTIFICACION}}`.
- **Importes y Cuentas Bancarias:** Sustituir por `{{RENTA_MENSUAL}}`, `{{CUANTIA_RECLAMADA}}`, `{{IBAN_PAGO}}`, `{{NUMERO_CUENTA}}`.
- **Referencias Notariales o Registrales:** Sustituir por `{{NOMBRE_NOTARIO}}`, `{{PLAZA_NOTARIO}}`, `{{NUMERO_PROTOCOLO}}`, `{{DATOS_REGISTRALES}}`.

### 1.1 Pautas para la Aplicación de Cambios en el Workspace (`edit_file`)
- **Coincidencia Literal (No Regex):** El parámetro `old_string` de `edit_file` busca coincidencia exacta de texto literal. **NUNCA utilices caracteres de escape como `\.`, `\(`, `\)` o `\[`**, ya que provocarán que la búsqueda falle.
- **Edición por Bloques o Secciones Coherentes:** Para evitar agotar el límite de iteraciones de herramientas del orquestador, **no realices micro-sustituciones palabra por palabra**. Agrupa los reemplazos por bloques multilínea completos (ej. todo el encabezado de fecha y remitente, todo el bloque de destinatario, párrafos completos o el pie de firmas).
- **Completitud en el Turno:** Aplica de forma continua y autónoma todas las parametrizaciones en el mismo turno hasta culminar la totalidad del documento, sin detenerte a pedir confirmaciones intermedias.

---

## 2. Convención de Sintaxis de Variables

1. **Formato:** Dobles llaves con el nombre en MAYÚSCULAS y guiones bajos entre palabras, conforme a la Fase 3 de `PLUGIN_AUTHORING_GUIDE.md`:
   - Correcto: `{{NOMBRE_ARRENDADOR}}`, `{{CUANTIA_TOTAL}}`, `{{FECHA_EFECTOS}}`
   - Incorrecto: `<NOMBRE>`, `[Nombre Arrendador]`, `{{NombreArrendador}}` (mayúsculas intercaladas), `{{NOMBREARRENDADOR}}` (sin guion bajo), `{{nombre_arrendador}}` (en minúsculas), `{NOMBRE_ARRENDADOR}` (llave simple)
2. **Variables con Aclaración Opcional:** Si un campo requiere especificar formato o posibles opciones, se puede incluir `:` tras el identificador:
   - Ejemplo: `{{PLAZO_DURACION_ANOS: número de años pactados}}`, `{{TIPO_GARANTIA: aval bancario o fianza en metálico}}`.
3. **Consistencia de Identificadores:** Si un dato se repite en varias secciones (ej. en el encabezado y en el pie de firma), usar EXACTAMENTE el mismo nombre de marcador (`{{NOMBRE_ARRENDADOR}}`).

---

## 3. Regla de Assets Limpios (Sin Condicionales en Comentarios HTML)

- **PROHIBIDO** incluir comentarios HTML condicionales (ej. `<!-- Si persona jurídica: ... -->`, `<!-- Opción A ... -->`) o pseudocódigo dentro del contenido de la plantilla.
- La plantilla debe ser puramente estructural en Markdown limpio.
- Las variaciones o bifurcaciones de redacción son gestionadas por el asistente o por la skill especializada en el momento de la redacción.

---

## 4. Preservación Estructural y de Formato Markdown

- **Títulos y Encabezamientos:** Mantener una jerarquía limpia (`#` para título principal, `##` para secciones/cláusulas, `###` para subsecciones).
- **Tablas:** Convertir datos tabulares a formato estándar Markdown (`| Campo | Valor |`).
- **Cláusulas Numeradas:** Preservar la numeración ordinal o cardinal del documento original (ej. `PRIMERA. — OBJETO`, `SEGUNDA. — RENTA`).
- **Pie de Firmas:** Estructurar los bloques de firma al final del documento:
  ```markdown
  En {{MUNICIPIO_FIRMA}}, a {{FECHA_FIRMA}}.

  Por la parte ARRENDADORA:               Por la parte ARRENDATARIA:
  {{NOMBRE_ARRENDADOR}}                   {{NOMBRE_ARRENDATARIO}}
  ```

---

## 5. Protocolo de Verificación de Compatibilidad con Skills (OBLIGATORIO)

Antes de guardar una plantilla asignada a una skill del sistema (`set_skill_template`), el asistente debe someter la plantilla a una **auditoría de compatibilidad integral**:

### Lista de Chequeo de Compatibilidad:
1. **Correspondencia del Asset (`asset_name`):**
   - El `asset_name` debe coincidir exactamente con uno de los assets declarados formalmente en la skill objetivo (ej. `template-contrato-arrendamiento-vivienda.md`).
2. **Coherencia Temática y Normativa:**
   - La plantilla debe corresponder a la naturaleza del trámite regulado por la skill (ej. un contrato de arrendamiento de vivienda no puede asignarse a un asset de arrendamiento de local ni a una demanda de desahucio).
3. **Cobertura de Variables Esenciales de la Skill:**
   - La plantilla debe incluir los marcadores `{{VARIABLE}}` requeridos para los inputs que la skill recopila y cumplimenta en sus fases de trabajo (consultar los `inputs:` del `SKILL.md` de la skill destino: datos de partes, objeto, importes, plazos, etc.).
4. **Ausencia de Directivas Prohibidas:**
   - Verificar que no existan comentarios HTML de control de flujo (`<!-- Si ... -->`) ni pseudocódigo procedural.

### Directiva de Rechazo por Incompatibilidad:
> **SI LA PLANTILLA NO ES COMPLETAMENTE COMPATIBLE CON LA SKILL:**
> - **NO GUARDAR.** Queda expresamente prohibido invocar `set_skill_template`.
> - Informar al usuario de forma inmediata y constructiva:
>   - Señalar con exactitud qué elementos faltan o resultan incompatibles (ej. "La plantilla carece de la cláusula de duración o de la variable `{{RENTA_MENSUAL}}`, requeridas por la skill `arrendamiento-urbano`").
>   - Proponer la adición o corrección de los bloques afectados.
>   - Solicitar confirmación para aplicar los ajustes antes de proceder al guardado en la sección de plantillas.

---

## 6. Directivas para Plantillas Globales de Usuario (Sin Skill)

Cuando el usuario registra o actualiza una plantilla general no asociada a una skill:

1. **Generación del Asset Name:**
   - El nombre legible proporcionado por el usuario se normaliza a slug en minúsculas con prefijo `template-` y extensión `.md`.
   - Ejemplo: `"Plantilla de Invitación a Evento"` -> `template-plantilla-de-invitacion-a-evento.md`.
2. **Actualización de Plantilla Existente (`update_user_template`):**
   - Se utiliza cuando la plantilla ya existe en el sistema/workspace (ej. identificada por su `asset_name`).
   - Requiere: `asset_name` y `template_content`.
   - **Modalidades de Asistencia Consultiva:** Si el usuario requiere apoyo para trabajar la plantilla antes de actualizarla, se presentan tres opciones mediante formulario interactivo (`restricted_human_in_the_loop_request`):
     * *Convertir datos a placeholders genéricos:* Identificación de datos concretos de ejemplo y sustitución por variables `{{VARIABLE}}`.
     * *Mejorar el contenido:* Optimización de redacción, claridad técnica/jurídica y estructuración en Markdown limpio.
     * *Actualizar contenido:* Integración directa de cláusulas o cambios aportados por el usuario.
3. **Creación de Nueva Plantilla (`save_user_template`):**
   - Se utiliza para crear una plantilla que aún no existe (típicamente creación asistida desde cero).
   - Requiere obligatoriamente:
     * `name`: Nombre o título de la plantilla.
     * `template_content`: Contenido completo en Markdown.
     * `description`: Explicación detallada del propósito o casos de uso de la plantilla.
