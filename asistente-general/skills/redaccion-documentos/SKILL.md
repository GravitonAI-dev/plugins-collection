---
name: redaccion-documentos
title: Redacción de documentos
i18n:
  en:
    name: document-drafting
    title: Document drafting
    description: >
      Drafts, structures and adapts any type of document that has no specific vertical skill in
      the catalogue: legal documents, administrative filings, statements of defence and
      pleadings against penalties, atypical contracts, private agreements, corporate
      communications, business proposals, formal e-mails, reports, internal memos and personal
      letters. It applies **Law 39/2015** on Common Administrative Procedure for filings before
      the public sector, the **Civil Code** and **Commercial Code** for private agreements, and
      corporate standards and good business practice for business communications. It classifies
      the request, proposes a base structure, creates the file in the workspace and edits it
      section by section with rigorous resolution of parties and data. Do not use for matters
      that have their own vertical skill (urban lease, dismissal letter, labour claim, order for
      payment, eviction, regulated administrative appeals, etc.).
description: >
  Redacta, estructura y adapta cualquier tipo de documento: jurídico, escrito administrativo,
  escrito de descargo o pliego de alegaciones sancionadoras, contrato atípico, acuerdo privado,
  comunicaciones corporativas, propuestas comerciales, correos electrónicos formales, informes,
  memorandos internos, cartas personales y redacciones de uso personal que no dispongan de una
  skill vertical específica en el catálogo. Aplica la **Ley 39/2015** del Procedimiento Administrativo
  Común para trámites y escritos ante el sector público, el **Código Civil** / **Código de Comercio**
  para pactos privados, y estándares corporativos y buenas prácticas comerciales para comunicaciones
  de negocio. Opera mediante clasificación rápida de vectores, propuesta de estructura base, volcado
  inmediato en workspace (.md) y edición incremental sección a sección con resolución rigurosa de
  partes y datos. NO usar para materias que dispongan de skill vertical propia en el catálogo
  (arrendamiento urbano, carta de despido, demanda social, monitorio, desahucio, recursos de
  alzada/reposición reglados, etc.).
when_to_use: |
  - El usuario solicita redactar un escrito de descargo, alegaciones o pliego frente a una notificación administrativa sancionadora.
  - El usuario necesita elaborar un contrato, convenio o acuerdo privado a medida no tipificado en otra skill.
  - El usuario requiere una solicitud formal, instancia, reclamación genérica o comunicación legal en su workspace.
  - El usuario necesita redactar comunicaciones corporativas, propuestas comerciales, correos electrónicos formales, informes o memorandos internos.
  - El usuario requiere cartas personales, comunicados informales o redacciones de uso personal.
  - El usuario aporta un borrador, minuta o texto propio y solicita adaptarlo o formalizarlo como documento en disco.
inputs:
  - 'categoria_documento: escrito_administrativo_descargo / contrato_acuerdo_privado / solicitud_reclamacion_formal / comunicacion_generica / informe_o_propuesta (V1)'
  - 'ambito_juridico: administrativo_sancionador / civil_patrimonial / mercantil_societario / particular / corporativo_negocios / uso_personal (V2)'
  - 'perfil_solicitante: persona_fisica / persona_juridica (V3)'
  - 'estado_procedimiento: fase_alegaciones_plazo / requerimiento_previo / formalizacion_inicial (V4)'
  - 'origen_plantilla: plantilla estándar del sistema / plantilla propia del usuario (V5)'
  - 'expediente_referencia: número de expediente, sanción o referencia administrativa si procede'
  - 'partes_intervinientes: nombres, NIF/CIF y domicilios de las partes u órgano receptor'
  - 'hechos_y_pretensiones: antecedentes fácticos, motivos de oposición y petición concreta'
outputs:
  - documento_workspace: documento final en formato markdown (.md) redactado incrementalmente en el workspace del usuario, DRAFT para revisión letrada
references:
  - references/metodologia-redaccion-juridica.md
assets:
  - assets/template-escrito-administrativo-descargo.md
  - assets/template-documento-privado-acuerdo.md
  - assets/template-documento-general.md
---

# Redacción de Documentos Jurídicos y Administrativos

> DRAFT — Para revisión letrada colegiada antes de su firma o presentación formal.

---

## FASE 1 — TRIAJE INTERACTIVO Y CLASIFICACIÓN

**Correspondencia con el enrutamiento.** Los vectores de esta skill se nombran con los identificadores siguientes; cada uno se resuelve con la respuesta indicada. No preguntes de nuevo nada que ya esté aquí:
- `V1` — categoría del documento, resuelta en el triaje de la sección 1.1
- `V2` — ámbito jurídico material
- `V3` — perfil del solicitante
- `V4` — estado del procedimiento
- `V5` — origen de la plantilla, resuelto en la Fase 2

### Vectores de Estado Internos

El asistente resuelve y mantiene en memoria los siguientes vectores para orientar la redacción:

| Vector | Descripción | Valores posibles |
|:---|:---|:---|
| V1 | Categoría del documento | `escrito_administrativo_descargo`, `contrato_acuerdo_privado`, `solicitud_reclamacion_formal`, `comunicacion_generica`, `informe_o_propuesta` |
| V2 | Ámbito jurídico material | `administrativo_sancionador`, `civil_patrimonial`, `mercantil_societario`, `particular`, `corporativo_negocios`, `uso_personal` |
| V3 | Perfil del solicitante | `persona_fisica`, `persona_juridica` |
| V4 | Estado del procedimiento | `fase_alegaciones_plazo`, `requerimiento_previo`, `formalizacion_inicial` |
| V5 | Origen de la plantilla | `plantilla_sistema`, `plantilla_usuario` |

### Correspondencia de Vectores y Plantilla Base

| V1 | Plantilla base asociada |
|:---|:---|
| `escrito_administrativo_descargo` | `assets/template-escrito-administrativo-descargo.md` |
| `solicitud_reclamacion_formal` | `assets/template-escrito-administrativo-descargo.md` (adaptada) |
| `contrato_acuerdo_privado` | `assets/template-documento-privado-acuerdo.md` |
| `comunicacion_generica` | `assets/template-documento-general.md` |
| `informe_o_propuesta` | `assets/template-documento-general.md` |

### Procedimiento de Triaje

1. **Escucha activa:** Analizar el mensaje inicial del usuario y la documentación aportada. Si los vectores V1-V4 se deducen de forma inequívoca, asignarlos en silencio y avanzar a la Fase 2 sin formularios innecesarios (per `REG-TRI-01`).
2. **Formulario residual:** Solo si quedan vectores por definir, presentar un formulario interactivo mediante `restricted_human_in_the_loop_request` para desambiguar el tipo de documento y el ámbito jurídico.
3. **Invisibilidad de vectores técnicos:** Los identificadores V1, V2, etc. son de control interno; queda terminantemente prohibido mencionarlos al usuario.

---

## FASE 2 — PLAN DE ACCIÓN, MARCO LEGAL Y ELECCIÓN DE PLANTILLA (REG-AST-01)

### Marco Legal Aplicable

Según el vector V2 resuelto:

- **Administrativo sancionador (V2 = `administrativo_sancionador`):** Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas (arts. 53, 76 y 77 — derecho de alegación y tramitación de procedimientos sancionadores); Ley 40/2015 de Régimen Jurídico del Sector Público.
- **Civil patrimonial (V2 = `civil_patrimonial`):** Código Civil (arts. 1254-1314 — teoría general del contrato); Código de Comercio para pactos mercantiles.
- **Mercantil societario (V2 = `mercantil_societario`):** Código de Comercio; Ley de Sociedades de Capital (Real Decreto Legislativo 1/2010).
- **Particular (V2 = `particular`):** Autonomía de la voluntad (art. 1255 CC).
- **Corporativo negocios (V2 = `corporativo_negocios`):** Estándares corporativos y buenas prácticas comerciales.
- **Uso personal (V2 = `uso_personal`):** Libre redacción y formato.

### Elección de Plantilla (REG-AST-01)

Convoca obligatoriamente el formulario de elección de plantilla per REG-AST-01.

---

## FASE 3 — CREACIÓN DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

### Volcado Inicial (REG-DOC-01)

1. **Crear el archivo en disco** mediante `create_file` con la plantilla completa (o la minuta propia revisada). El nombre del archivo será descriptivo en `snake_case.md` (ej. `escrito_descargo_administrativo.md`, `acuerdo_privado_servicios.md`, `propuesta_comercial_cliente.md`).
2. **Disclaimer condicional:** El disclaimer `> DRAFT — Para revisión letrada colegiada antes de su firma o presentación formal.` es **estrictamente condicional**: solo debe insertarse si el documento pertenece a un dominio legal o administrativo (V2 es `administrativo_sancionador`, `civil_patrimonial` o `mercantil_societario`). NO debe insertarse si V2 es `corporativo_negocios` o `uso_personal`.
3. **Volcado inmediato de partes conocidas (REG-CLI-04):** Si los datos de las partes ya son conocidos (por escucha activa, `search_clients` o fichas de clientes), sustituir TODOS los marcadores `{{NOMBRE_...}}` en el documento completo: título H1, comparecencia y bloque de firmas. Queda terminantemente prohibido dejar marcadores de partes en blanco si la información ya es conocida.
4. **Confirmación en chat:** Indicar la ruta absoluta del documento creado y los datos de partes incorporados. Encadenar de inmediato hacia la primera sección de la Fase 4.

---

## FASE 4 — EDICIÓN INCREMENTAL SECCIÓN A SECCIÓN

### Hoja de Ruta de Secciones

Aplicar `edit_file` siguiendo el orden de la plantilla base:

1. **Encabezamiento / Remitente:** (Aplica REG-CLI-01 a 04 para partes).
2. **Contexto / Antecedentes:** (Recogida con `slot_filling_request` si aplica).
3. **Cuerpo Principal / Cláusulas / Alegaciones:** (Negociación -> Confirmación en chat -> `edit_file`).
4. **Cierre / Firmas / Suplico:** (Resolución final).

### Reglas de Edición

- **Surgical precisión:** Copiar el texto real del documento con exactitud matemática al usar `edit_file` (guiones largos, caracteres ordinales, saltos de línea).
- **Verificación prioritaria en workspace:** Consultar `# WORKSPACE ACTIVE DOCUMENTS` antes de invocar `read_file`.
- **Cero destrucción:** Si `edit_file` falla, NUNCA sobrescribir con `Write`. Revisar el contenido auténtico y reintentar.

---

## FASE 5 — BUCLE DE REALIMENTACIÓN FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Presenta el menú interactivo de revisión final per REG-FDB-01. Al finalizar, emite las advertencias preceptivas de cierre per REG-CLO-01.

---
