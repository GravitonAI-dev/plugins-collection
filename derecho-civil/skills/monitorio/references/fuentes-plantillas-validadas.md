# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `monitorio`. Registra las fuentes normativas y las plantillas
> validadas que la skill verifica y, si detecta una version posterior, ACTUALIZA en el plugin en cada lanzamiento.

---

## Regla de actualizacion permanente (OBLIGATORIA)

Cada vez que se lanza la skill, en el Paso 1 se comprueban las fuentes de esta tabla. **Si se detecta una version posterior a la registrada, la skill actualiza el archivo correspondiente del plugin (reference o asset) antes de redactar** y anota la nueva fecha/version verificada. Si la fuente no es accesible, se usa la version local y se informa al usuario.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Version registrada | URL |
|---|---|---|---|
| LEC — Ley 1/2000 de Enjuiciamiento Civil (texto consolidado) | BOE-A-2000-323 | consolidado a la fecha de verificacion | https://www.boe.es/buscar/act.php?id=BOE-A-2000-323 |
| LO 1/2025 de eficiencia del Servicio Publico de Justicia | BOE-A-2025-76 | 02/01/2025 (en vigor 03/04/2025) | https://www.boe.es/buscar/act.php?id=BOE-A-2025-76 |

Articulos relevantes de la LEC para esta skill: 812 a 818 (proceso monitorio) y 264 (acreditacion del intento de MASC).

---

## Plantilla validada — Modelo Normalizado del CGPJ

| Recurso | Detalle |
|---|---|
| Nombre | Modelo Normalizado de Proceso Monitorio Civil |
| Aprobado por | Comision Permanente del Consejo General del Poder Judicial (Acuerdo de 22/12/2015) |
| Publicacion | BOE-A-2016-783 |
| Landing oficial | https://www.poderjudicial.es/cgpj/es/Servicios/Atencion-Ciudadana/Modelos-normalizados/El-proceso-monitorio |
| PDF oficial | https://www.poderjudicial.es/stfls/CGPJ/ATENCION%20CIUDADANA/FICHERO/20160204%20Modelo%20Normalizado%20de%20Proceso%20Monitorio%20Civil.pdf |
| Acuerdo en BOE | https://www.boe.es/buscar/doc.php?id=BOE-A-2016-783 |

El asset `assets/template-peticion-inicial-monitorio.md` se basa en la estructura de este modelo normalizado. En cada lanzamiento, la skill re-verifica el modelo del CGPJ; si el CGPJ publica una version posterior, actualiza el asset.

---

## Guias de estilo de redaccion judicial (consulta)

| Recurso | Uso |
|---|---|
| Guia de redaccion judicial clara (Ministerio de Justicia) | Estilo claro: frases cortas, una idea por frase, voz activa |
| Libro de estilo de la Justicia (RAE / CGPJ) | Terminologia y correccion del lenguaje juridico |

Principios aplicados en los assets: estructura AL JUZGADO / HECHOS / FUNDAMENTOS DE DERECHO / SUPLICO; evitar latinajos innecesarios; numerar hechos y fundamentos; una idea por parrafo.

---

## Verificacion de otras normas autonomicas o especiales

Para deudas de comunidad de propietarios (Ley 49/1960 de Propiedad Horizontal) o especialidades autonomicas, verificar con `web_search` la version vigente antes de redactar.
