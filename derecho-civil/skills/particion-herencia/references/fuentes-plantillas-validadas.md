# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `particion-herencia`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Codigo Civil (texto consolidado) | BOE-A-1889-4763 | consolidado a 03/01/2025 (ultima modificacion 01/03/2023) | https://www.boe.es/buscar/act.php?id=BOE-A-1889-4763 |
| Ley 29/1987 del Impuesto sobre Sucesiones y Donaciones | BOE-A-1987-28141 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-1987-28141 |
| TR Ley Reguladora de las Haciendas Locales (plusvalia municipal, IIVTNU) | BOE-A-2004-4214 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2004-4214 |

Articulos relevantes del Codigo Civil para esta skill: 657 y ss. (apertura de la sucesion), 806 a 808 (legitima), 834 y ss. (derechos del conyuge viudo), 912 y ss. y 930 y ss. (sucesion intestada), 988 a 1034 (aceptacion y repudiacion, beneficio de inventario) y 1035 a 1087 (colacion y particion).

---

## Plantillas del plugin

| Asset | Base |
|---|---|
| `assets/template-cuaderno-particional.md` | Estructura estandar de escritura de aceptacion y particion de herencia: comparecencia, exposicion (titulo sucesorio), inventario y avaluo, liquidacion del haber, formacion de lotes y adjudicaciones (Arts. 1058, 1061-1062, 1068 CC) |
| `assets/template-aceptacion-herencia.md` | Documento de aceptacion pura y simple o a beneficio de inventario, con opcion de renuncia (Arts. 988, 998, 1003, 1008-1034 CC) |

Los assets no reproducen un modelo notarial oficial unico (no existe un formulario normalizado estatal para la particion, a diferencia del monitorio del CGPJ): se construyen sobre la estructura que exige el Codigo Civil y la practica notarial. En cada lanzamiento la skill re-verifica los articulos del CC; si su redaccion cambia, actualiza el asset afectado.

---

## Guias de estilo de redaccion (consulta)

| Recurso | Uso |
|---|---|
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |
| Practica notarial de particion de herencias (Consejo General del Notariado) | Estructura del documento particional: comparecencia, exposicion, inventario, avaluo, adjudicaciones, otorgamiento |

Principios aplicados en los assets: estructura COMPARECENCIA / EXPONEN / INVENTARIO Y AVALUO / LIQUIDACION / ADJUDICACIONES / OTORGAMIENTO; clausulas numeradas; cifras en numero y letra; una idea por apartado; sin latinismos innecesarios.

---

## Verificacion de derecho foral o autonomico

Para herencias sujetas a derecho civil foral o especial (Cataluna, Aragon, Navarra, Pais Vasco, Baleares, Galicia), las reglas de legitima, ordenes de sucesion y particion pueden diferir del Codigo Civil comun. Verificar con `web_search` la normativa foral vigente antes de redactar y advertir al usuario.
