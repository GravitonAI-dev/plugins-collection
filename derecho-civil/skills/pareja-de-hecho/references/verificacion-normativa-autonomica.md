# Protocolo de Verificación de la Normativa Autonómica

> Material de referencia para la skill `derecho-civil-pareja-de-hecho`. Define CÓMO se verifica la ley autonómica y su
> registro en cada lanzamiento, que se extrae de esa verificación y que se hace cuando falla.
> Esta reference describe un procedimiento; **no almacena requisitos de ninguna comunidad autónoma**, y no debe
> almacenarlos nunca: se guardarían obsoletos y acabarían citándose de memoria, que es justo lo que la skill prohíbe.

---

## 1. Por qué esta verificación es bloqueante

No existe ley estatal de parejas de hecho ni registro estatal. Diecisiete comunidades autónomas regulan la institución con requisitos distintos: tiempo mínimo de convivencia previa, exigencia o no de empadronamiento conjunto, vecindad civil o simple residencia administrativa, y — lo más relevante — **inscripción constitutiva o meramente declarativa**. Además, varias de esas leyes han sido parcialmente anuladas por el Tribunal Constitucional, de modo que su texto original ya no refleja lo que está en vigor.

En consecuencia, **cualquier afirmación sobre requisitos, registro o efectos autonómicos que no proceda de una verificación hecha en este mismo lanzamiento es una invención**, aunque suene plausible. No se admite el conocimiento previo del modelo como fuente.

---

## 2. Secuencia de verificación (en cada lanzamiento, tras conocer la comunidad autónoma)

**2.1 — Localizar la ley autonómica vigente.**

```
web_search("ley parejas de hecho [comunidad autónoma] texto consolidado requisitos inscripción registro")
web_search("[comunidad autónoma] ley uniones de hecho parejas estables inconstitucional Tribunal Constitucional artículos anulados")
```

Preferir, por este orden: el texto consolidado en el BOE de la ley autonómica (muchas se publican también allí, con notas de vigencia que recogen las anulaciones del Tribunal Constitucional), el boletín oficial de la comunidad autónoma, y la sede electrónica del propio registro. Descartar blogs y webs de despacho como fuente de un requisito concreto: sirven para orientar la búsqueda, no para afirmar.

Si la ley figura en el BOE, contrastarla además por la API de legislación consolidada:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{identificador}/texto/bloque/{bloque}
```
con cabecera `Accept: application/xml`. Recordar el aviso de formato: unas normas usan `artNNN` y otras `aNNN`; un 404 no significa que la norma no exista.

**2.2 — Localizar el registro y su trámite.**

```
web_search("registro parejas de hecho [comunidad autónoma] sede electrónica documentación tasa solicitud inscripción")
```

Fuente válida: la sede electrónica o el portal oficial de la comunidad autónoma. Si el domicilio concreto tiene además registro municipal, comprobar cuál corresponde y si sus efectos son distintos.

**2.3 — Extraer estos datos y solo estos.**

| Dato | Uso en el documento |
|---|---|
| Denominación exacta y completa de la ley, con fecha | `{{DENOMINACION_LEY_AUTONOMICA}}` |
| Enlace al texto oficial consultado | `{{ENLACE_LEY_AUTONOMICA}}` |
| Preceptos anulados o modificados que afecten al caso | Se advierte al cliente; no se cita un artículo anulado |
| Denominación oficial del registro y enlace a su sede | `{{DENOMINACION_REGISTRO}}`, `{{ENLACE_REGISTRO}}` |
| Carácter de la inscripción: constitutiva o declarativa | Determina cómo se explica al cliente que efecto tiene inscribirse |
| Requisitos de constitución: edad, ausencia de vínculo, tiempo mínimo de convivencia previa, empadronamiento conjunto, residencia o vecindad | Tabla de requisitos del checklist |
| Documentación exigida, forma de solicitud, tasa y plazos | Apartados de documentación y trámite del checklist |
| Efectos que la propia ley atribuye a la inscripción, y en particular si reconoce derechos sucesorios | Apartado de efectos; determina el tono de la advertencia sucesoria |
| Fecha en que se ha hecho la verificación | `{{FECHA_VERIFICACION_NORMATIVA_AUTONOMICA}}` |

**2.4 — Registrar y informar.** La fecha de verificación, la denominación de la ley y el enlace se vuelcan al documento generado y se comunican al cliente en la Confirmación visible. No se actualiza esta reference con los requisitos obtenidos (ver la advertencia del encabezamiento); si lo que cambia es una fuente **estatal**, entonces si se actualiza `fuentes-plantillas-validadas.md`.

---

## 3. Que hacer cuando la verificación falla

Fallo es tanto el error técnico (sin resultados, timeout, fuente caída) como el resultado dudoso: fuentes que se contradicen, o solo fuentes no oficiales.

1. **No afirmar nada.** Ningún requisito, ningún plazo, ninguna denominación de registro.
2. **Decírselo al cliente, con estas palabras o equivalentes:** "No he podido verificar en fuente oficial la normativa de parejas de hecho de {{COMUNIDAD_AUTONOMA}} ni los requisitos de su registro. No voy a afirmarle unos requisitos que no he comprobado. Continuo con el documento dejando ese punto expresamente pendiente, y deberá confirmarlo en la sede del registro antes de presentar la solicitud."
3. **Dejar constancia en el documento.** Los placeholders de la ley, del registro y de los requisitos permanecen sin resolver, y el bloque de advertencia de verificación pendiente se activa.
4. **Seguir adelante con lo que si es derecho común.** El pacto de convivencia y el pacto de ruptura se apoyan en el Código Civil y pueden redactarse igualmente; lo único que queda pendiente es la parte autonómica.
5. **En la rama de inscripción, advertir con más fuerza:** ese checklist es precisamente la parte autonómica. Sin verificación, se entrega el esqueleto del trámite con los requisitos marcados como pendientes, y se dice con claridad que no sustituye a la comprobación en la sede del registro.

---

## 4. Casos que la verificación no resuelve y exigen escalación

- **Convivientes que residen en comunidades autónomas distintas**, o que se van a trasladar: puede cambiar el registro competente y la ley aplicable.
- **Distinta vecindad civil entre los convivientes**, o vecindad civil foral distinta de la comunidad de residencia.
- **Elemento internacional**: alguno de los convivientes no reside en España, o la pareja se constituyo en el extranjero.
- **Pareja ya inscrita en otra comunidad** que se plantea una nueva inscripción: comprobar la incompatibilidad y el deber de comunicación entre registros.

En los cuatro casos: advertir, no resolver de oficio y ofrecer escalación.
