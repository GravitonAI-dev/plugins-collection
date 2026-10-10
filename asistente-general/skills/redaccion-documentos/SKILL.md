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
  Redacta, estructura y adapta cualquier tipo de documento: juridico, escrito administrativo,
  escrito de descargo o pliego de alegaciones sancionadoras, contrato atipico, acuerdo privado,
  comunicaciones corporativas, propuestas comerciales, correos electronicos formales, informes,
  memorandos internos, cartas personales y redacciones de uso personal que no dispongan de una
  skill vertical especifica en el catalogo. Aplica la **Ley 39/2015** del Procedimiento Administrativo
  Comun para tramites y escritos ante el sector publico, el **Codigo Civil** / **Codigo de Comercio**
  para pactos privados, y estandares corporativos y buenas practicas comerciales para comunicaciones
  de negocio. Opera mediante clasificacion rapida de vectores, propuesta de estructura base, volcado
  inmediato en workspace (.md) y edicion incremental seccion a seccion con resolucion rigurosa de
  partes y datos. NO usar para materias que dispongan de skill vertical propia en el catalogo
  (arrendamiento urbano, carta de despido, demanda social, monitorio, desahucio, recursos de
  alzada/reposicion reglados, etc.).
when_to_use: |
  - El usuario solicita redactar un escrito de descargo, alegaciones o pliego frente a una notificacion administrativa sancionadora.
  - El usuario necesita elaborar un contrato, convenio o acuerdo privado a medida no tipificado en otra skill.
  - El usuario requiere una solicitud formal, instancia, reclamacion generica o comunicacion legal en su workspace.
  - El usuario necesita redactar comunicaciones corporativas, propuestas comerciales, correos electronicos formales, informes o memorandos internos.
  - El usuario requiere cartas personales, comunicados informales o redacciones de uso personal.
  - El usuario aporta un borrador, minuta o texto propio y solicita adaptarlo o formalizarlo como documento en disco.
inputs:
  - 'categoria_documento: escrito_administrativo_descargo / contrato_acuerdo_privado / solicitud_reclamacion_formal / comunicacion_generica / informe_o_propuesta (V1)'
  - 'ambito_juridico: administrativo_sancionador / civil_patrimonial / mercantil_societario / particular / corporativo_negocios / uso_personal (V2)'
  - 'perfil_solicitante: persona_fisica / persona_juridica (V3)'
  - 'estado_procedimiento: fase_alegaciones_plazo / requerimiento_previo / formalizacion_inicial (V4)'
  - 'origen_plantilla: plantilla estandar del sistema / plantilla propia del usuario (V5)'
  - 'expediente_referencia: numero de expediente, sancion o referencia administrativa si procede'
  - 'partes_intervinientes: nombres, NIF/CIF y domicilios de las partes u organo receptor'
  - 'hechos_y_pretensiones: antecedentes facticos, motivos de oposicion y peticion concreta'
outputs:
  - documento_workspace: documento final en formato markdown (.md) redactado incrementalmente en el workspace del usuario, DRAFT para revision letrada
references:
  - references/metodologia-redaccion-juridica.md
assets:
  - assets/template-escrito-administrativo-descargo.md
  - assets/template-documento-privado-acuerdo.md
  - assets/template-documento-general.md
---

# Redaccion de Documentos Juridicos y Administrativos

> DRAFT — Para revision letrada colegiada antes de su firma o presentacion formal.

---

## FASE 1 — TRIAJE INTERACTIVO Y CLASIFICACION

**Correspondencia con el enrutamiento.** Los vectores de esta skill se nombran con los identificadores siguientes; cada uno se resuelve con la respuesta indicada. No preguntes de nuevo nada que ya esté aquí:
- `V1` — categoria del documento, resuelta en el triaje de la seccion 1.1
- `V2` — ambito juridico material
- `V3` — perfil del solicitante
- `V4` — estado del procedimiento
- `V5` — origen de la plantilla, resuelto en la Fase 2

### Vectores de Estado Internos

El asistente resuelve y mantiene en memoria los siguientes vectores para orientar la redaccion:

| Vector | Descripcion | Valores posibles |
|:---|:---|:---|
| V1 | Categoria del documento | `escrito_administrativo_descargo`, `contrato_acuerdo_privado`, `solicitud_reclamacion_formal`, `comunicacion_generica`, `informe_o_propuesta` |
| V2 | Ambito juridico material | `administrativo_sancionador`, `civil_patrimonial`, `mercantil_societario`, `particular`, `corporativo_negocios`, `uso_personal` |
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

1. **Escucha activa:** Analizar el mensaje inicial del usuario y la documentacion aportada. Si los vectores V1-V4 se deducen de forma inequivoca, asignarlos en silencio y avanzar a la Fase 2 sin formularios innecesarios (per `REG-TRI-01`).
2. **Formulario residual:** Solo si quedan vectores por definir, presentar un formulario interactivo mediante `restricted_human_in_the_loop_request` para desambiguar el tipo de documento y el ambito juridico.
3. **Invisibilidad de vectores tecnicos:** Los identificadores V1, V2, etc. son de control interno; queda terminantemente prohibido mencionarlos al usuario.

---

## FASE 2 — PLAN DE ACCION, MARCO LEGAL Y ELECCION DE PLANTILLA (REG-AST-01)

### Marco Legal Aplicable

Segun el vector V2 resuelto:

- **Administrativo sancionador (V2 = `administrativo_sancionador`):** Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Comun de las Administraciones Publicas (arts. 53, 76 y 77 — derecho de alegacion y tramitacion de procedimientos sancionadores); Ley 40/2015 de Regimen Juridico del Sector Publico.
- **Civil patrimonial (V2 = `civil_patrimonial`):** Codigo Civil (arts. 1254-1314 — teoria general del contrato); Codigo de Comercio para pactos mercantiles.
- **Mercantil societario (V2 = `mercantil_societario`):** Codigo de Comercio; Ley de Sociedades de Capital (Real Decreto Legislativo 1/2010).
- **Particular (V2 = `particular`):** Autonomia de la voluntad (art. 1255 CC).
- **Corporativo negocios (V2 = `corporativo_negocios`):** Estandares corporativos y buenas practicas comerciales.
- **Uso personal (V2 = `uso_personal`):** Libre redaccion y formato.

### Eleccion de Plantilla (REG-AST-01)

Convoca obligatoriamente el formulario de eleccion de plantilla per REG-AST-01.

---

## FASE 3 — CREACION DEL DOCUMENTO BASE EN DISCO (REG-DOC-01)

### Volcado Inicial (REG-DOC-01)

1. **Crear el archivo en disco** mediante `create_file` con la plantilla completa (o la minuta propia revisada). El nombre del archivo sera descriptivo en `snake_case.md` (ej. `escrito_descargo_administrativo.md`, `acuerdo_privado_servicios.md`, `propuesta_comercial_cliente.md`).
2. **Disclaimer condicional:** El disclaimer `> DRAFT — Para revision letrada colegiada antes de su firma o presentacion formal.` es **estrictamente condicional**: solo debe insertarse si el documento pertenece a un dominio legal o administrativo (V2 es `administrativo_sancionador`, `civil_patrimonial` o `mercantil_societario`). NO debe insertarse si V2 es `corporativo_negocios` o `uso_personal`.
3. **Volcado inmediato de partes conocidas (REG-CLI-04):** Si los datos de las partes ya son conocidos (por escucha activa, `search_clients` o fichas de clientes), sustituir TODOS los marcadores `{{NOMBRE_...}}` en el documento completo: titulo H1, comparecencia y bloque de firmas. Queda terminantemente prohibido dejar marcadores de partes en blanco si la informacion ya es conocida.
4. **Confirmacion en chat:** Indicar la ruta absoluta del documento creado y los datos de partes incorporados. Encadenar de inmediato hacia la primera seccion de la Fase 4.

---

## FASE 4 — EDICION INCREMENTAL SECCION A SECCION

### Hoja de Ruta de Secciones

Aplicar `edit_file` siguiendo el orden de la plantilla base:

1. **Encabezamiento / Remitente:** (Aplica REG-CLI-01 a 04 para partes).
2. **Contexto / Antecedentes:** (Recogida con `slot_filling_request` si aplica).
3. **Cuerpo Principal / Clausulas / Alegaciones:** (Negociacion -> Confirmacion en chat -> `edit_file`).
4. **Cierre / Firmas / Suplico:** (Resolucion final).

### Reglas de Edicion

- **Surgical precision:** Copiar el texto real del documento con exactitud matematica al usar `edit_file` (guiones largos, caracteres ordinales, saltos de linea).
- **Verificacion prioritaria en workspace:** Consultar `# WORKSPACE ACTIVE DOCUMENTS` antes de invocar `read_file`.
- **Cero destruccion:** Si `edit_file` falla, NUNCA sobrescribir con `Write`. Revisar el contenido autentico y reintentar.

---

## FASE 5 — BUCLE DE REALIMENTACION FINAL Y CIERRE (REG-FDB-01 & REG-CLO-01)

Presenta el menu interactivo de revision final per REG-FDB-01. Al finalizar, emite las advertencias preceptivas de cierre per REG-CLO-01.

---
