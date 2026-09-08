# Fuentes Oficiales y Normativa de Protección de Datos

> Material de referencia para la skill `proteccion-datos-despacho`.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte al usuario de que la verificación queda pendiente.

---

## Fuentes normativas

| Norma | Identificación | Preceptos relevantes |
|---|---|---|
| Reglamento (UE) 2016/679, general de protección de datos | Verificar la versión vigente en el Diario Oficial de la Unión Europea y su corrección de errores | Principios; licitud del tratamiento; categorías especiales; deber de información; derechos de los interesados; responsabilidad del responsable; encargado de tratamiento; registro de actividades; seguridad; notificación de brechas; evaluación de impacto; delegado de protección de datos; transferencias internacionales |
| Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales | Verificar identificador BOE y versión consolidada | Deber de confidencialidad; tratamiento de datos relativos a condenas e infracciones penales por abogados y procuradores; bloqueo de datos; supuestos de designación obligatoria de delegado de protección de datos; videovigilancia; derechos digitales |
| Ley Orgánica 6/1985 del Poder Judicial | Verificar el precepto vigente | Secreto profesional del abogado |
| Estatuto General de la Abogacía Española, aprobado por Real Decreto 135/2021 | Verificar identificador BOE | Deber de secreto profesional y custodia de la información |
| Ley 10/2010, de prevención del blanqueo de capitales | Verificar identificador BOE | Base jurídica y plazo de conservación de la actividad de diligencia debida |

**Regla estricta:** esta skill no consigna números de artículo ni identificadores que no haya verificado en la sesión, y **no escribe de memoria** ningún plazo, contenido mínimo ni supuesto de obligación.

---

## Datos que se verifican en cada asunto

| Dato | Por qué |
|---|---|
| Contenido mínimo del **registro de actividades** | Determina si el documento cumple la obligación |
| Alcance de la **excepción por tamaño** al registro de actividades | En un despacho casi nunca opera, pero debe razonarse |
| Contenido mínimo del **contrato de encargado** | Su omisión parcial es un defecto detectable |
| Contenido del **deber de información** | En sus dos capas, básica y adicional |
| Régimen del deber de información respecto de **datos no obtenidos del interesado**, y sus excepciones | Decisivo para los terceros del asunto |
| **Plazo de notificación de brechas** a la autoridad de control | Se cuenta en horas |
| Umbral de **riesgo alto** para la comunicación a los interesados | Decisión distinta de la anterior |
| Supuestos de **designación obligatoria de delegado** de protección de datos | Puede concurrir según la actividad |
| Supuestos de **evaluación de impacto** | Señaladamente por categorías especiales a gran escala |
| Bases jurídicas aplicables a **categorías especiales** y a **datos penales** | Incluida la previsión específica sobre abogados y procuradores |
| Régimen y garantías de las **transferencias internacionales** | Cambia con las decisiones de la Comisión y de los tribunales |
| Régimen del **bloqueo** de datos | Afecta a los plazos de conservación |
| **Limitaciones** al ejercicio de los derechos por secreto profesional | Determina cómo se responde a la contraparte |

---

## Autoridad de control y recursos

| Recurso | Uso | Verificación |
|---|---|---|
| Autoridad de control competente | Notificación de brechas, consultas, reclamaciones y régimen sancionador | Verificar denominación, sede electrónica y procedimiento de notificación vigentes |
| Guías y herramientas de la autoridad de control | Plantillas, evaluación de riesgo de brechas, criterios sobre bases jurídicas | Verificar existencia y vigencia |
| Comité Europeo de Protección de Datos | Directrices interpretativas | Verificar la vigente sobre la cuestión concreta |
| Colegio de adscripción | Criterios propios sobre la interacción con el secreto profesional | Verificar |

**Ninguna denominación de autoridad, sede electrónica o formulario se escribe de memoria.**

---

## Lo que esta skill no hace

1. **No diseña el sistema de cumplimiento completo** del despacho.
2. **No realiza la evaluación de impacto** cuando resulta exigible: es un trabajo específico con metodología propia.
3. **No decide sobre la notificación de una brecha**: documenta el análisis y deriva la decisión al delegado de protección de datos o a especialista.
4. **No emite dictámenes de cumplimiento** ni certifica la adecuación del sistema.
5. **No sustituye al delegado de protección de datos** cuando su designación es obligatoria.

---

## Estilo de redacción

Principios aplicados en los assets: en el registro de actividades, **una tabla por actividad** con los mismos campos, para que las omisiones sean visibles de un vistazo, y la diligencia debida en prevención del blanqueo como actividad **diferenciada** con su limitación de finalidad expresa; en el contrato de encargado, cláusulas numeradas que siguen el orden del contenido mínimo exigido, con plazos de notificación de brechas del encargado hacia el responsable sensiblemente inferiores al del responsable frente a la autoridad; en la cláusula informativa, estructura de dos capas con tabla básica y desarrollo adicional, y un apartado propio para los límites derivados del secreto profesional; en el registro de brechas, la **hora límite de notificación en la cabecera**, antes que cualquier otro contenido, y separación de las dos decisiones con sus umbrales distintos; bloque final de advertencias dirigido al profesional que revisa.
