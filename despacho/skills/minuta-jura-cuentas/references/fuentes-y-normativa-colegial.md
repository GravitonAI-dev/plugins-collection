# Fuentes Oficiales y Normativa Colegial

> Material de referencia para la skill `minuta-jura-cuentas`.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte al usuario de que la verificación queda pendiente.

---

## Fuentes normativas

| Norma | Identificación | Verificación |
|---|---|---|
| Estatuto General de la Abogacía Española, aprobado por Real Decreto 135/2021 | Real Decreto 135/2021, de 2 de marzo | Verificar identificador BOE y versión consolidada con `web_search` |
| Ley 1/2000, de Enjuiciamiento Civil | BOE-A-2000-323 | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| Ley Orgánica 6/1985 del Poder Judicial — artículo 542.3, secreto profesional | BOE-A-1985-12666 | Verificar el identificador y la redacción vigente del precepto |
| Ley 15/2007 de Defensa de la Competencia — régimen de los criterios orientativos de honorarios | Verificar identificador BOE | Verificar con `web_search` |
| Normativa de protección de consumidores y usuarios | Texto refundido aprobado por Real Decreto Legislativo 1/2007 | Verificar identificador y versión consolidada |
| Ley 2/1974 de Colegios Profesionales | Verificar identificador BOE | Verificar con `web_search` |

**Regla estricta:** esta skill no consigna identificadores BOE ni números de artículo de normativa deontológica que no haya verificado en la sesión. Cuando el dato no esté verificado, se cita la norma por su denominación oficial y se deja constancia de la verificación pendiente.

---

## La capa colegial: por qué no basta con la norma estatal

El ejercicio profesional está regulado en **tres niveles** y la skill debe recorrerlos en este orden:

1. **Norma estatal:** Estatuto General de la Abogacía Española y legislación general.
2. **Normativa deontológica del Consejo General de la Abogacía Española.**
3. **Normativa y acuerdos del colegio de adscripción**, que puede imponer requisitos adicionales sobre contenido de la hoja de encargo, información al cliente, retribución vinculada al resultado, publicidad y comunicación de la renuncia.

**Consecuencia operativa:** ninguna skill de este plugin invoca un deber deontológico concreto sin haber identificado antes el colegio de adscripción del profesional y comprobado su normativa con `web_search`. Un requisito que existe en un colegio puede no existir en otro.

---

## Criterios orientativos de honorarios

Los colegios profesionales pueden elaborar criterios orientativos **a los exclusivos efectos legalmente admitidos**, señaladamente la **tasación de costas** y la **jura de cuentas**. Fuera de esos supuestos no operan como baremo de precios, y su publicación o aplicación como tal está limitada por la normativa de defensa de la competencia.

Consecuencias prácticas:

1. Los criterios orientativos **no sirven como única definición del honorario frente al cliente** en la hoja de encargo. Una cláusula que remita genéricamente a ellos no fija un honorario determinado ni determinable.
2. Sí son la referencia natural en la **jura de cuentas** y en la **tasación de costas**, y por eso conviene conocerlos y conservarlos.
3. Antes de invocarlos, verificar que el colegio de adscripción los tiene publicados y en qué versión.

---

## Magnitudes fiscales que se verifican en cada asunto

| Magnitud | Fuente |
|---|---|
| Tipo de impuesto sobre el valor añadido aplicable a los servicios profesionales | Normativa vigente del impuesto |
| Tipo de retención a cuenta del IRPF sobre rendimientos de actividades profesionales | Normativa vigente del impuesto |
| Tipo reducido de retención aplicable a profesionales en inicio de actividad | Normativa vigente del impuesto |
| Supuestos en que el cliente está obligado a practicar retención | Normativa vigente del impuesto |
| Interés legal del dinero, como referencia del interés de demora pactado | Ley de presupuestos generales del Estado del ejercicio |
| Importe de las tasas judiciales, cuando resulten exigibles | Normativa vigente de tasas |

**Ninguna de estas cifras se escribe de memoria.** Se verifican con `web_search` en cada asunto.

---

## Estilo de redacción

Principios aplicados en los assets: minuta con **relación fechada de actuaciones** en tabla y desglose económico en tres bloques separados —honorarios, suplidos y liquidación—, porque la minuta global sin desglose es el defecto que más impugnaciones provoca y el que hace inviable la jura de cuentas; escritos judiciales con la estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO; manifestación formal del artículo 35 como apartado propio y destacado, por ser requisito legal; descripción de **actuaciones y no de contenidos**, para respetar el secreto profesional en un escrito que se incorpora a las actuaciones; bloque final de advertencias dirigido al profesional que revisa, con el trámite aplicable según el tipo de impugnación.
