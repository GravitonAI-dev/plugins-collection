# Protocolo de Verificacion de la Normativa Autonomica

> Material de referencia para la skill `derecho-civil-pareja-de-hecho`. Define COMO se verifica la ley autonomica y su
> registro en cada lanzamiento, que se extrae de esa verificacion y que se hace cuando falla.
> Esta reference describe un procedimiento; **no almacena requisitos de ninguna comunidad autonoma**, y no debe
> almacenarlos nunca: se guardarian obsoletos y acabarian citandose de memoria, que es justo lo que la skill prohibe.

---

## 1. Por que esta verificacion es bloqueante

No existe ley estatal de parejas de hecho ni registro estatal. Diecisiete comunidades autonomas regulan la institucion con requisitos distintos: tiempo minimo de convivencia previa, exigencia o no de empadronamiento conjunto, vecindad civil o simple residencia administrativa, y — lo mas relevante — **inscripcion constitutiva o meramente declarativa**. Ademas, varias de esas leyes han sido parcialmente anuladas por el Tribunal Constitucional, de modo que su texto original ya no refleja lo que esta en vigor.

En consecuencia, **cualquier afirmacion sobre requisitos, registro o efectos autonomicos que no proceda de una verificacion hecha en este mismo lanzamiento es una invencion**, aunque suene plausible. No se admite el conocimiento previo del modelo como fuente.

---

## 2. Secuencia de verificacion (en cada lanzamiento, tras conocer la comunidad autonoma)

**2.1 — Localizar la ley autonomica vigente.**

```
web_search("ley parejas de hecho [comunidad autonoma] texto consolidado requisitos inscripcion registro")
web_search("[comunidad autonoma] ley uniones de hecho parejas estables inconstitucional Tribunal Constitucional articulos anulados")
```

Preferir, por este orden: el texto consolidado en el BOE de la ley autonomica (muchas se publican tambien alli, con notas de vigencia que recogen las anulaciones del Tribunal Constitucional), el boletin oficial de la comunidad autonoma, y la sede electronica del propio registro. Descartar blogs y webs de despacho como fuente de un requisito concreto: sirven para orientar la busqueda, no para afirmar.

Si la ley figura en el BOE, contrastarla ademas por la API de legislacion consolidada:

```
https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{identificador}/texto/bloque/{bloque}
```
con cabecera `Accept: application/xml`. Recordar el aviso de formato: unas normas usan `artNNN` y otras `aNNN`; un 404 no significa que la norma no exista.

**2.2 — Localizar el registro y su tramite.**

```
web_search("registro parejas de hecho [comunidad autonoma] sede electronica documentacion tasa solicitud inscripcion")
```

Fuente valida: la sede electronica o el portal oficial de la comunidad autonoma. Si el domicilio concreto tiene ademas registro municipal, comprobar cual corresponde y si sus efectos son distintos.

**2.3 — Extraer estos datos y solo estos.**

| Dato | Uso en el documento |
|---|---|
| Denominacion exacta y completa de la ley, con fecha | `{{denominacion_ley_autonomica}}` |
| Enlace al texto oficial consultado | `{{enlace_ley_autonomica}}` |
| Preceptos anulados o modificados que afecten al caso | Se advierte al cliente; no se cita un articulo anulado |
| Denominacion oficial del registro y enlace a su sede | `{{denominacion_registro}}`, `{{enlace_registro}}` |
| Caracter de la inscripcion: constitutiva o declarativa | Determina como se explica al cliente que efecto tiene inscribirse |
| Requisitos de constitucion: edad, ausencia de vinculo, tiempo minimo de convivencia previa, empadronamiento conjunto, residencia o vecindad | Tabla de requisitos del checklist |
| Documentacion exigida, forma de solicitud, tasa y plazos | Apartados de documentacion y tramite del checklist |
| Efectos que la propia ley atribuye a la inscripcion, y en particular si reconoce derechos sucesorios | Apartado de efectos; determina el tono de la advertencia sucesoria |
| Fecha en que se ha hecho la verificacion | `{{fecha_verificacion_normativa_autonomica}}` |

**2.4 — Registrar y informar.** La fecha de verificacion, la denominacion de la ley y el enlace se vuelcan al documento generado y se comunican al cliente en la Confirmacion visible. No se actualiza esta reference con los requisitos obtenidos (ver la advertencia del encabezamiento); si lo que cambia es una fuente **estatal**, entonces si se actualiza `fuentes-plantillas-validadas.md`.

---

## 3. Que hacer cuando la verificacion falla

Fallo es tanto el error tecnico (sin resultados, timeout, fuente caida) como el resultado dudoso: fuentes que se contradicen, o solo fuentes no oficiales.

1. **No afirmar nada.** Ningun requisito, ningun plazo, ninguna denominacion de registro.
2. **Decirselo al cliente, con estas palabras o equivalentes:** "No he podido verificar en fuente oficial la normativa de parejas de hecho de {{comunidad_autonoma}} ni los requisitos de su registro. No voy a afirmarle unos requisitos que no he comprobado. Continuo con el documento dejando ese punto expresamente pendiente, y debera confirmarlo en la sede del registro antes de presentar la solicitud."
3. **Dejar constancia en el documento.** Los placeholders de la ley, del registro y de los requisitos permanecen sin resolver, y el bloque de advertencia de verificacion pendiente se activa.
4. **Seguir adelante con lo que si es derecho comun.** El pacto de convivencia y el pacto de ruptura se apoyan en el Codigo Civil y pueden redactarse igualmente; lo unico que queda pendiente es la parte autonomica.
5. **En la rama de inscripcion, advertir con mas fuerza:** ese checklist es precisamente la parte autonomica. Sin verificacion, se entrega el esqueleto del tramite con los requisitos marcados como pendientes, y se dice con claridad que no sustituye a la comprobacion en la sede del registro.

---

## 4. Casos que la verificacion no resuelve y exigen escalacion

- **Convivientes que residen en comunidades autonomas distintas**, o que se van a trasladar: puede cambiar el registro competente y la ley aplicable.
- **Distinta vecindad civil entre los convivientes**, o vecindad civil foral distinta de la comunidad de residencia.
- **Elemento internacional**: alguno de los convivientes no reside en Espana, o la pareja se constituyo en el extranjero.
- **Pareja ya inscrita en otra comunidad** que se plantea una nueva inscripcion: comprobar la incompatibilidad y el deber de comunicacion entre registros.

En los cuatro casos: advertir, no resolver de oficio y ofrecer escalacion.
