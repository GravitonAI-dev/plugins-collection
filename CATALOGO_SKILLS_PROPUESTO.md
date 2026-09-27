# Catálogo de capacidades — España y Estados Unidos

> Propuesta. **No desarrollada**: fija qué capacidades faltan, **de qué tipo es cada una** y en qué orden construirlas.
>
> Las 21 capacidades seleccionadas no son 21 skills. Son **1 entorno de ejecución, 8 herramientas, 8 conectores y 7 skills**. Confundirlos es el error que hay que evitar antes de escribir una línea.

## 1. El criterio de selección

Una capacidad se gana el sitio cuando, al quitarla, la respuesta empeora de forma medible. Eso ocurre en cuatro situaciones y solo en cuatro: formato binario, cálculo determinista, dato externo verificable y acción en el mundo real. Todo lo demás ya está en los pesos del modelo o se resuelve con una línea en el prompt de sistema (§7).

## 2. Skill, herramienta o conector — la distinción que importa

| Tipo | Qué es | Quién ejecuta | Cuándo es la respuesta correcta |
|---|---|---|---|
| **Herramienta** | Función tipada con argumentos y resultado estructurado | Código, siempre igual | El resultado debe ser exacto y auditable. Nada que decidir |
| **Conector** | Servidor que expone acceso a un sistema externo | Código contra un tercero | El dato o la acción vive fuera del producto |
| **Entorno de ejecución** | Sandbox donde el modelo corre código con librerías | Código que el modelo escribe al momento | La tarea es abierta y no cabe en una función fija |
| **Skill** | Instrucciones, procedimiento y assets que se cargan en contexto | El modelo, guiado | Hay criterio, convenciones o plantillas que el modelo no puede adivinar |

La regla práctica: **si el resultado no depende de ningún criterio, no es una skill.** Calcular un plazo con festivos de Castilla y León no tiene criterio: tiene tabla y aritmética. Eso es una herramienta. En cambio, saber qué campos tiene una nómina española frente a una estadounidense y con qué confianza se han leído sí es criterio, y eso sí es una skill.

Tus ~60 skills legales actuales están bien clasificadas: plantilla + procedimiento + referencias normativas es exactamente la forma de una skill. Lo que sigue, en su mayoría, no lo es.

---

## 3. Capa 1 — Entorno de ejecución *(1, y es el cuello de botella)*

| Capacidad | Qué es | Por qué |
|---|---|---|
| `sandbox de código` | Entorno Python aislado con librerías de ofimática, imagen y datos preinstaladas, y acceso al sistema de ficheros del espacio de trabajo | **Sin esto, el bloque de ficheros no existe.** Las skills `docx` o `xlsx` de cualquier ecosistema no manipulan el fichero: le dicen al modelo qué código escribir. Si no hay dónde ejecutarlo, la skill es papel mojado |

Es la decisión número uno del plan. Todo lo demás depende de si existe o no.

## 4. Capa 2 — Herramientas *(8 funciones, cero criterio)*

| # | Herramienta | Qué devuelve | Qué hay que construir | Mercado | Prio |
|---|---|---|---|---|---|
| 1 | `calcular_plazo` | Fecha límite, días hábiles, cuenta atrás, husos | Calendario de festivos por año y territorio, estatal, autonómico, local, federal y estatal de EEUU | Jurisdicción | **P0** |
| 2 | `ocr` | Texto de una imagen o escaneo, enderezado y limpio | Motor OCR + corrección de perspectiva | Neutra | **P0** |
| 3 | `validar_identificador` | Válido o no: NIF, NIE, CIF, IBAN, EIN, SSN, VAT | Algoritmos de dígito de control | Jurisdicción | P1 |
| 4 | `calcular_impuesto` | Retención, tramos y cuota estimada | Tablas del ejercicio vigente: IRPF y Seguridad Social; federal, estatal y FICA | Jurisdicción | P1 |
| 5 | `calcular_financiacion` | Cuadro de amortización, TAE, APR, interés compuesto | Motor financiero con convenciones de cada mercado | Localización | P1 |
| 6 | `convertir_unidad` | Métrico e imperial, tallas, temperatura, formatos de fecha y número | Tablas de conversión | Localización | P2 |
| 7 | `convertir_formato` | Fichero convertido entre markdown, Word, PDF y HTML | Cadena de conversión con pruebas de fidelidad | Neutra | P2 |
| 8 | `procesar_imagen` | Imagen recortada, rotada, comprimida, sin EXIF | Librería de imagen | Neutra | P1 |

## 5. Capa 3 — Conectores *(8 sistemas externos)*

| # | Conector | A qué conecta | Qué hay que construir | Mercado | Prio |
|---|---|---|---|---|---|
| 9 | `boe` | Versión consolidada vigente, cita literal, enlace permanente | Cliente de la API del BOE y boletines autonómicos + caché + control de vigencia | España | **P0** |
| 10 | `agencias-us` | Formulario vigente, fee, plazo y requisitos en IRS, SSA, USCIS y DMV estatal | Catálogo por agencia y estado con verificación de versión | EEUU | **P0** |
| 11 | `registros-mercantiles` | Existencia y datos reales de una empresa | Registro Mercantil y Secretary of State por estado | Jurisdicción | P1 |
| 12 | `tipos-de-cambio` | Tipo real con fecha de referencia | API de divisas | Neutra | P2 |
| 13 | `precios-de-mercado` | Precio y disponibilidad reales por mercado | Fuentes de precio + normalización de moneda | Localización | P2 |
| 14 | `envio-fehaciente` | Envío real con acuse: burofax y certificado; certified mail | Proveedor por mercado + custodia del acuse | Jurisdicción | P1 |
| 15 | `calendario` | Eventos y avisos reales en el calendario del usuario | Conector de calendario | Neutra | P2 |
| 16 | `firma-electronica` | Firma de un PDF y validación de firmas recibidas | Proveedor de firma + validación de cadena de confianza | Jurisdicción | P2 |

## 6. Capa 4 — Skills reales *(7, las únicas que aportan criterio)*

| # | Skill | Qué criterio aporta que no está en una función | Sobre qué se apoya | Prio |
|---|---|---|---|---|
| 17 | `documentos-word` | Recetario: cómo conservar estilos al rellenar una plantilla, cuándo usar control de cambios, cómo no corromper el fichero, qué hacer con tablas anidadas | Sandbox | **P0** |
| 18 | `hojas-de-calculo` | Recetario: cómo detectar cabeceras sucias y filas basura, cuándo fórmula y cuándo valor, qué gráfico corresponde a cada pregunta | Sandbox | **P0** |
| 19 | `documentos-pdf` | Recetario: cuándo extraer texto y cuándo hace falta OCR, cómo recuperar tablas, cómo rellenar un formulario sin romper el original | Sandbox + `ocr` | **P0** |
| 20 | `extraer-datos-de-documento` | **Los esquemas por tipo de documento**: qué campos tiene una nómina española frente a una estadounidense, una factura, un extracto; qué es obligatorio, qué se valida contra qué y con qué confianza se ha leído cada campo | `ocr` + `validar_identificador` | **P0** |
| 21 | `presentaciones` | Contenido estructurado sobre plantilla, con el renderizado siempre determinista y el modelo sin tocar nunca el XML | Sandbox | P1 |
| 22 | `comparar-dos-documentos` | Alineación por significado y no por caracteres, y el juicio sobre qué implica cada cambio | Sandbox | P1 |
| 23 | `tramitar-ante-organismo` | El procedimiento completo: qué formulario, qué documentos adjuntar, en qué orden, y **la parada humana obligatoria antes de firmar o presentar** | `boe`, `agencias-us`, `envio-fehaciente`, `firma-electronica` | P1 |

Fíjate en el patrón: **las skills son delgadas y viven encima.** Aportan recetario, esquemas y procedimiento. La potencia está debajo, en el sandbox, las funciones y los conectores.

---

## 7. Lo que no lleva nada de esto

Escribir correos y mensajes · textos personales · corregir estilo · adaptar tono · resumir · traducir · explicar conceptos · dar clase · lluvia de ideas · naming · guiones · recetas · rutinas de ejercicio · arreglos domésticos · soporte técnico doméstico · planificar viajes o eventos · comparar alternativas · quitar marcas de texto generado.

Son de altísima frecuencia — escribir correos es la petición de escritura más repetida que existe — y por eso hay que ser bueno en ellos. Pero la frecuencia dice en qué hay que ser bueno, **no qué hay que construir**: el modelo ya los resuelve sin ayuda. Donde sí conviene invertir es en el prompt de sistema del asistente general (`consulta-general`): formato consistente, longitud, tono y disciplina de no afirmar sin fuente. Eso cuesta un fichero.

---

## 8. Orden de ejecución

El orden ya no es por prioridad de producto, es por **dependencia técnica**. No se puede escribir la skill antes que aquello sobre lo que se apoya.

**Hito 0 — Sandbox de ejecución.** Sin él, nada del bloque de ficheros es posible. Es la primera pieza y no tiene alternativa.

**Hito 1 — Herramientas base.** `calcular_plazo` y `ocr`. Son las dos de las que cuelga más cosa.

**Hito 2 — Conectores de fuente oficial.** `boe` y `agencias-us`. Estrenan la capa de doble mercado, y conviene resolver ese problema aquí y no a mitad de catálogo.

**Hito 3 — Las cuatro skills P0.** `documentos-word`, `hojas-de-calculo`, `documentos-pdf` y `extraer-datos-de-documento`. Ya tienen debajo todo lo que necesitan.

**Hito 4 — El resto**, por prioridad: validadores e impuestos, `presentaciones`, `comparar-dos-documentos`, `envio-fehaciente` y `tramitar-ante-organismo`, y por último firma, calendario, precios y divisas.

---

## 9. Decisiones previas al desarrollo

1. **¿Hay sandbox o no?** Es la pregunta que más cambia el plan. Si la plataforma ya ejecuta código, el Hito 0 desaparece y se empieza por el Hito 1. Si no, es un proyecto de infraestructura, no de producto, y hay que presupuestarlo como tal.

2. **Skill, herramienta o conector, declarado en cada ficha.** El esquema actual de `SKILL.md` (`name`, `description`, `when_to_use`, `inputs`, `outputs`) no distingue el tipo ni declara dependencias. Con capacidades que se apoyan unas en otras, hace falta un campo de dependencias o acabarás con skills cargadas sin lo que necesitan debajo.

3. **Idioma y jurisdicción son ejes independientes.** Un hispanohablante en Texas quiere respuesta en español con reglas de EEUU. El `CLAUDE.md` detecta idioma y fija español por defecto; hace falta un vector de mercado separado, y en EEUU el estado forma parte de él.

4. **Nueve de las 23 dependen de datos que caducan**: festivos, tablas fiscales, formularios de agencia, tipos de cambio, normativa, precios. Necesitan responsable y calendario de actualización desde el día uno, o se convierten en la parte del producto que miente con más seguridad.

5. **Cálculo fuera del modelo, sin excepción.** El modelo recoge datos, invoca la función y explica el resultado. Nunca calcula. Es la única forma de que el número sea auditable.

6. **Freno humano en todo lo irreversible.** Enviar, presentar y firmar. La parada humana no es una opción de configuración: es parte del diseño.
