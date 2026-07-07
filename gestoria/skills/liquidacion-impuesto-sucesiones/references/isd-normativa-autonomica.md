# Normativa Autonomica del ISD — Que varia por CCAA y como verificarlo

> Material de referencia para la skill `liquidacion-impuesto-sucesiones`. Explica por que el importe del
> Impuesto de Sucesiones depende sobre todo de la comunidad autonoma y como verificar la normativa vigente
> con web_search. Lo lee el agente al preparar la autoliquidacion; no forma parte del output al usuario.
> La tabla de ejemplo es orientativa y esta marcada [verificar]: NO usarla como dato firme.

---

## Por que la CCAA es la clave del tramite

El ISD es un tributo estatal CEDIDO a las comunidades autonomas (Ley 22/2009). Cada CCAA puede aprobar:

- Reducciones propias o mejoras de las estatales (parentesco, vivienda habitual, empresa familiar, discapacidad).
- Su propia tarifa y sus coeficientes multiplicadores.
- Bonificaciones de la cuota, que en muchas CCAA dejan la cuota de Grupos I y II cercana a cero.

Consecuencia: una misma herencia puede tributar de forma muy distinta segun donde tuviera su residencia habitual el causante. Por eso el Bloque A del procedimiento (CCAA competente) es critico.

---

## Punto de conexion (que CCAA es competente)

| Regla | Detalle |
|---|---|
| Adquisiciones mortis causa | CCAA donde el causante tuvo su residencia habitual |
| Residencia habitual | CCAA donde permanecio mas dias en los 5 anos anteriores al fallecimiento [verificar] |
| No residentes / bienes en el extranjero | Puede corresponder a la AEAT (Estado) con derecho a aplicar la normativa autonomica; caso a escalar |

---

## Tabla de ejemplo (orientativa, NO usar como dato firme) [verificar]

| CCAA | Regimen tipico Grupos I y II [verificar] |
|---|---|
| Madrid | Bonificacion de la cuota cercana al 99% para Grupos I y II [verificar] |
| Andalucia | Reduccion elevada y bonificacion cercana al 99% para descendientes, conyuge y ascendientes [verificar] |
| Canarias | Bonificacion muy alta para Grupos I y II [verificar] |
| Comunidad Valenciana | Bonificacion elevada para familiares directos; mejoras para colaterales en calendario [verificar] |
| Cataluna | Tarifa propia reducida y reducciones por heredero, sin bonificacion general de la cuota [verificar] |
| Resto de CCAA | Regimen propio variable; verificar caso a caso [verificar] |

Los datos anteriores cambian con frecuencia y pueden estar desactualizados. Sirven solo para orientar la busqueda, nunca como cuota.

<!-- EDITAR PARA TU EQUIPO: sustituir esta tabla por las CCAA reales del equipo, con enlaces a sus portales tributarios autonomicos y la fecha de ultima verificacion. -->

---

## Como verificar (OBLIGATORIO en el Paso 1.3)

Una vez conocida la CCAA competente, la skill ejecuta:
```
web_search("Impuesto Sucesiones [comunidad autonoma] reducciones bonificaciones vigentes 2026 grupo parentesco cuota")
```
Y, si procede, una segunda busqueda por el organismo y el modelo:
```
web_search("[comunidad autonoma] Hacienda autonomica Impuesto Sucesiones modelo 650 sede presentacion")
```
Todo lo obtenido se traslada al borrador marcado [verificar].

---

## Regla para la skill

Nunca estimar la cuota sin haber verificado la normativa autonomica de la CCAA competente. Si la verificacion falla, aplicar el minimo estatal (`isd-ley-29-1987.md`) y advertir de forma expresa que la CCAA puede mejorar el regimen y que la estimacion queda [verificar].
