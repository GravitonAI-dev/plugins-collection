# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `arrendamiento-urbano`. Registra las fuentes normativas que la
> skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| LAU — Ley 29/1994 de Arrendamientos Urbanos (texto consolidado) | BOE-A-1994-26003 | 25/05/2023 (Ley 12/2023) | https://www.boe.es/buscar/act.php?id=BOE-A-1994-26003 |

Articulos relevantes de la LAU para esta skill: 2-5 (ambito), 8 (cesion y subarriendo), 9 (duracion y prorroga), 17-20 (renta, actualizacion, gastos, zonas tensionadas), 27 (resolucion), 36 (fianza), Titulo III (locales de negocio).

---

## Verificacion de otras normas autonomicas o especiales

Para zonas de mercado residencial tensionado declaradas por comunidades autonomas o especialidades forales, verificar con `web_search` la version vigente antes de redactar.
