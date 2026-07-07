# Fuentes oficiales, sedes y plazos — Extranjeria

> Material de referencia para la skill `extranjeria-residencia`. Registra las fuentes normativas (con su
> identificador BOE), las sedes de presentacion, la cita previa y los plazos, y la regla de
> auto-actualizacion. La skill verifica estas fuentes en el Paso 1 y, si detecta una version posterior,
> actualiza los archivos del plugin antes de preparar el tramite.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de este archivo. **Si se detecta una version posterior a la registrada (norma, formulario o tasa), la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de preparar el tramite** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE) — version registrada

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| Ley Organica 4/2000 (LOEX) | BOE-A-2000-544 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2000-544 |
| RD 1155/2024 — Reglamento de Extranjeria | BOE-A-2024-24099 | publicado 20/11/2024, en vigor 20/05/2025 (deroga RD 557/2011) | https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099 |
| Orden ministerial de tasas de extranjeria | Orden PJC/617/2025 `[verificar]` | importes de tasa vigentes | verificar en el BOE la orden en vigor |

---

## Formularios y tasas — fuentes oficiales

| Recurso | URL |
|---|---|
| Formularios EX (modelos generales) — Secretaria de Estado de Migraciones | https://www.inclusion.gob.es/web/migraciones/modelos-generales |
| Modelo 790 codigo 012 (Policia Nacional) | https://sede.policia.gob.es |
| Modelo 790 codigo 052 (Administraciones Publicas) | https://sede.administracionespublicas.gob.es |

---

## Organismos y sedes de presentacion

| Tramite | Organismo | Presentacion |
|---|---|---|
| NIE (en Espana) | Oficina de Extranjeria o comisaria de Policia Nacional de la provincia | Presencial con cita previa; algunos casos por sede electronica |
| NIE (desde el extranjero) | Consulado espanol del pais de residencia | Consular |
| Autorizacion de residencia (en Espana) | Oficina de Extranjeria de la provincia del domicilio | Presencial con cita previa o telematica (sede electronica / plataforma Mercurio) |
| Autorizacion de residencia (desde el extranjero) | Consulado (visado) + Oficina de Extranjeria | El visado se solicita en el consulado (fuera de esta skill) |
| Recogida de la TIE (huellas) | Comisaria de Policia Nacional | Presencial con cita previa, tras la concesion |

La cita previa es habitualmente obligatoria y suele gestionarse por la sede electronica de Administraciones Publicas.

---

## Plazos orientativos

| Concepto | Plazo orientativo | Nota |
|---|---|---|
| Resolucion de la autorizacion de residencia | segun el tramite `[verificar]` | La resolucion es discrecional; el silencio puede ser negativo |
| Recogida de la TIE tras la concesion | 1 mes desde la notificacion `[verificar]` | Pedir cita para huellas |
| Vigencia inicial de la residencia temporal | 1 ano habitual `[verificar]` | Renovable segun el tipo |

`[verificar]` Los plazos y el sentido del silencio administrativo se confirman en el Reglamento vigente y en la resolucion del tramite. La skill no garantiza la concesion: la resolucion es discrecional de la Administracion.

<!-- EDITAR PARA TU EQUIPO: fijar los plazos y sentido del silencio segun el tramite y la practica de vuestra Oficina de Extranjeria -->
