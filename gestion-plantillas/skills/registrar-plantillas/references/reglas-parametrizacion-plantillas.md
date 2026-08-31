# Reglas de Parametrización y Abstracción de Plantillas (Assets)

> Material de referencia para la skill `registrar-plantillas`. Define las pautas metodológicas para convertir documentos o minutas de ejemplo en plantillas estandarizadas limpias con marcadores `{{variable}}`.

---

## 0. Ingesta de Documentos desde `<attached_documents>`

Los documentos de ejemplo aportados por el usuario (PDFs, DOCX, TXT, MD) son analizados por el backend y se inyectan automáticamente en el prompt dentro de la sección:

```xml
# ATTACHED DOCUMENTS
<attached_documents>
    <attached_document name="archivo_ejemplo.pdf">
        "Texto completo del archivo..."
    </attached_document>
</attached_documents>
```

- La skill debe extraer el texto directamente de `<attached_document name="...">`.
- Si el usuario aporta el documento mediante texto en el chat, se extrae de `# USER MESSAGE` / `<user_message>`.

---

## 1. Principio de Cero Datos Personales (PII)

Al transformar un documento real (contrato firmado, demanda judicial, solicitud administrativa, hoja censal) en una plantilla reutilizable:
- **Nombres y Apellidos:** Sustituir por `{{nombre_arrendador}}`, `{{nombre_demandante}}`, `{{nombre_interesado}}`, `{{nombre_representante}}`, etc.
- **Identificadores Fiscales / DNI:** Sustituir por `{{nif_arrendador}}`, `{{dni_demandante}}`, `{{cif_entidad}}`, `{{nie_solicitante}}`.
- **Domicilios y Direcciones:** Sustituir por `{{domicilio_notificaciones}}`, `{{direccion_inmueble}}`, `{{municipio}}`, `{{provincia}}`.
- **Fechas Concretas:** Sustituir por `{{fecha_contrato}}`, `{{fecha_inicio}}`, `{{fecha_vencimiento}}`, `{{fecha_notificacion}}`.
- **Importes y Números de Cuenta:** Sustituir por `{{renta_mensual}}`, `{{cuantia_reclamada}}`, `{{iban_pago}}`, `{{numero_cuenta}}`.
- **Referencias Notariales o Registrales:** Sustituir por `{{nombre_notario}}`, `{{plaza_notario}}`, `{{numero_protocolo}}`, `{{datos_registrales}}`.

---

## 2. Convención de Sintaxis de Variables

1. **Formato:** Dobles llaves con nombre en minúsculas y guiones bajos (`snake_case`):
   - Correcto: `{{nombre_arrendador}}`, `{{cuantia_total}}`, `{{fecha_efectos}}`
   - Incorrecto: `<NOMBRE>`, `[Nombre Arrendador]`, `{{NombreArrendador}}`
2. **Variables con Descripción Opcional:** Si un campo requiere una aclaración de formato o valor esperado, se puede incluir `:` tras el identificador:
   - Ejemplo: `{{plazo_duracion_anos: número de años pactados}}`, `{{tipo_garantia: aval bancario o depósito}}`.
3. **Coherencia de Identificadores:** Si la misma variable aparece múltiples veces a lo largo del documento (ej. el nombre del arrendador en el encabezamiento y en el pie de firma), usar EXACTAMENTE el mismo nombre de marcador (`{{nombre_arrendador}}`).

---

## 3. Regla de Assets Limpios (Sin Condicionales en Comentarios HTML)

Siguiendo el estándar de arquitectura de GravitonAI:
- **PROHIBIDO** incluir comentarios HTML condicionales (ej. `<!-- Si persona jurídica: ... -->`, `<!-- Opción A ... -->`).
- La plantilla resultante debe contener la estructura íntegra de cláusulas o estipulaciones en Markdown limpio.
- Las variaciones o bifurcaciones de redacción son manejadas por el procedimiento de la skill destino mediante edición incremental (`edit_file`).

---

## 4. Preservación Estructural y de Formato Markdown

- **Títulos y Encabezamientos:** Mantener la jerarquía de títulos Markdown (`#`, `##`, `###`).
- **Tablas:** Si el documento original incluye tablas de datos o liquidaciones, convertirlas a tablas Markdown estándar (`| Campo | Valor |`).
- **Cláusulas Numeradas:** Preservar la numeración ordinal o cardinal del documento original (ej. `PRIMERA. — OBJETO`, `SEGUNDA. — RENTA`, `1. Hechos`, `2. Fundamentos`).
- **Pie de Firmas:** Estructurar los bloques de firma al final del documento con marcadores de comparecencia:
  ```markdown
  En {{municipio_firma}}, a {{fecha_firma}}.

  Por la parte ARRENDADORA:               Por la parte ARRENDATARIA:
  {{nombre_arrendador}}                   {{nombre_arrendatario}}
  ```
