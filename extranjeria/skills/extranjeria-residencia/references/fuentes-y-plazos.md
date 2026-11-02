# Fuentes oficiales, sedes y plazos — Extranjería

> Material de referencia para la skill `extranjeria-residencia`. Registra las fuentes normativas (con su
> identificador BOE), las sedes de presentación, la cita previa y los plazos, y la regla de
> verificación. La skill verifica estas fuentes en la Fase 2.1 y, si detecta una versión posterior,
> aplica la redacción vigente al trámite que prepara, sin modificar los archivos del plugin.

---

## Regla de verificación permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en la Fase 2.1 se comprueban las fuentes de este archivo. **Si se detecta una versión posterior a la registrada (norma, formulario o tasa), la skill aplica la redacción vigente al trámite que prepara en el workspace del usuario** e informa del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la versión local y se informa al usuario.

---

## Fuentes normativas (BOE) — versión registrada

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Ley Orgánica 4/2000 (LOEX) | BOE-A-2000-544 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2000-544 |
| RD 1155/2024 — Reglamento de Extranjería | BOE-A-2024-24099 | publicado 20/11/2024, en vigor 20/05/2025 (deroga RD 557/2011) | https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099 |
| Orden ministerial de tasas de extranjería | Orden PJC/617/2025 `[verificar]` | importes de tasa vigentes | verificar en el BOE la orden en vigor |

---

## Formularios y tasas — fuentes oficiales

| Recurso | URL |
|---|---|
| Formularios EX (modelos generales) — Secretaria de Estado de Migraciones | https://www.inclusion.gob.es/web/migraciones/modelos-generales |
| Modelo 790 código 012 (Policía Nacional) | https://sede.policia.gob.es |
| Modelo 790 código 052 (Administraciones Públicas) | https://sede.administracionespublicas.gob.es |

---

## Organismos y sedes de presentación

| Trámite | Organismo | Presentación |
|---|---|---|
| NIE (en España) | Oficina de Extranjería o comisaria de Policía Nacional de la provincia | Presencial con cita previa; algunos casos por sede electrónica |
| NIE (desde el extranjero) | Consulado español del país de residencia | Consular |
| Autorización de residencia (en España) | Oficina de Extranjería de la provincia del domicilio | Presencial con cita previa o telemática (sede electrónica / plataforma Mercurio) |
| Autorización de residencia (desde el extranjero) | Consulado (visado) + Oficina de Extranjería | El visado se solicita en el consulado (fuera de esta skill) |
| Recogida de la TIE (huellas) | Comisaria de Policía Nacional | Presencial con cita previa, tras la concesión |

La cita previa es habitualmente obligatoria y suele gestionarse por la sede electrónica de Administraciones Públicas.

---

## Plazos orientativos

| Concepto | Plazo orientativo | Nota |
|---|---|---|
| Resolución de la autorización de residencia | según el trámite `[verificar]` | La resolución es discrecional; el silencio puede ser negativo |
| Recogida de la TIE tras la concesión | 1 mes desde la notificación `[verificar]` | Pedir cita para huellas |
| Vigencia inicial de la residencia temporal | 1 año habitual `[verificar]` | Renovable según el tipo |

`[verificar]` Los plazos y el sentido del silencio administrativo se confirman en el Reglamento vigente y en la resolución del trámite. La skill no garantiza la concesión: la resolución es discrecional de la Administración.

