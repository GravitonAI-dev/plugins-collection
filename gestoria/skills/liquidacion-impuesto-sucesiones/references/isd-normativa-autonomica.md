# Normativa Autonómica del ISD — Que varía por CCAA y como verificarlo

> Material de referencia para la skill `liquidacion-impuesto-sucesiones`. Explica por qué el importe del
> Impuesto de Sucesiones depende sobre todo de la comunidad autónoma y como verificar la normativa vigente
> con web_search. Lo lee el agente al preparar la autoliquidación; no forma parte del output al usuario.
> La tabla de ejemplo es orientativa y está marcada [verificar]: NO usarla como dato firme.

---

## Por qué la CCAA es la clave del trámite

El ISD es un tributo estatal CEDIDO a las comunidades autónomas (Ley 22/2009). Cada CCAA puede aprobar:

- Reducciones propias o mejoras de las estatales (parentesco, vivienda habitual, empresa familiar, discapacidad).
- Su propia tarifa y sus coeficientes multiplicadores.
- Bonificaciones de la cuota, que en muchas CCAA dejan la cuota de Grupos I y II cercana a cero.

Consecuencia: una misma herencia puede tributar de forma muy distinta según donde tuviera su residencia habitual el causante. Por eso el Bloque A del procedimiento (CCAA competente) es crítico.

---

## Punto de conexión (que CCAA es competente)

| Regla | Detalle |
|---|---|
| Adquisiciones mortis causa | CCAA donde el causante tuvo su residencia habitual |
| Residencia habitual | CCAA donde permaneció más días en los 5 años anteriores al fallecimiento [verificar] |
| No residentes / bienes en el extranjero | Puede corresponder a la AEAT (Estado) con derecho a aplicar la normativa autonómica; caso a escalar |

---

## Tabla de ejemplo (orientativa, NO usar como dato firme) [verificar]

| CCAA | Régimen típico Grupos I y II [verificar] |
|---|---|
| Madrid | Bonificación de la cuota cercana al 99% para Grupos I y II [verificar] |
| Andalucía | Reducción elevada y bonificación cercana al 99% para descendientes, cónyuge y ascendientes [verificar] |
| Canarias | Bonificación muy alta para Grupos I y II [verificar] |
| Comunidad Valenciana | Bonificación elevada para familiares directos; mejoras para colaterales en calendario [verificar] |
| Cataluña | Tarifa propia reducida y reducciones por heredero, sin bonificación general de la cuota [verificar] |
| Resto de CCAA | Régimen propio variable; verificar caso a caso [verificar] |

Los datos anteriores cambian con frecuencia y pueden estar desactualizados. Sirven solo para orientar la búsqueda, nunca como cuota.

---

## Cómo verificar (OBLIGATORIO en la Fase 2.1)

Una vez conocida la CCAA competente, la skill ejecuta:
```
web_search("Impuesto Sucesiones [comunidad autónoma] reducciones bonificaciones vigentes 2026 grupo parentesco cuota")
```
Y, si procede, una segunda búsqueda por el organismo y el modelo:
```
web_search("[comunidad autónoma] Hacienda autonómica Impuesto Sucesiones modelo 650 sede presentación")
```
Todo lo obtenido se traslada al borrador marcado [verificar].

---

## Regla para la skill

Nunca estimar la cuota sin haber verificado la normativa autonómica de la CCAA competente. Si la verificación falla, aplicar el mínimo estatal (`isd-ley-29-1987.md`) y advertir de forma expresa que la CCAA puede mejorar el régimen y que la estimación queda [verificar].
