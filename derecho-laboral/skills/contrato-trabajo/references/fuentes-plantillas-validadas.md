# Fuentes Oficiales y Plantillas Validadas

> Material de referencia para la skill `contrato-trabajo`.

---

## Regla de verificación permanente (OBLIGATORIA)

En cada lanzamiento, la skill comprueba las fuentes de esta tabla. **Si detecta una versión posterior a la registrada, aplica la redacción vigente al documento que redacta en el workspace del usuario**, informando del cambio en el chat. La skill nunca modifica sus propios archivos de plugin. Si la fuente no es accesible, se usa la referencia local y se advierte al usuario de que la verificación queda pendiente.

---

## Fuentes normativas (BOE)

| Norma | Identificador BOE | Versión registrada | URL |
|---|---|---|---|
| Estatuto de los Trabajadores — texto refundido aprobado por Real Decreto Legislativo 2/2015 | BOE-A-2015-11430 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 |
| Ley General de la Seguridad Social — texto refundido aprobado por Real Decreto Legislativo 8/2015 | BOE-A-2015-11724 | consolidado a la fecha de verificación | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |

Artículos relevantes del Estatuto de los Trabajadores: 6 (edad mínima), 8 (forma del contrato y copia básica), 11 (contratos formativos), 12 (contrato a tiempo parcial), 14 (periodo de prueba), 15 (duración del contrato), 16 (contrato fijo-discontinuo), 21 (pactos de plena dedicación, no concurrencia y permanencia), 34 (jornada y registro), 38 (vacaciones) y 39 (movilidad funcional).

Normas complementarias cuya identificación y versión vigente debe verificarse con `web_search` antes de citarlas: Real Decreto-ley 32/2021 de reforma laboral, Ley 10/2021 de trabajo a distancia, Ley 31/1995 de prevención de riesgos laborales, Reglamento (UE) 2016/679 de protección de datos y Ley Orgánica 3/2018.

---

## Magnitudes que cambian y nunca se escriben de memoria

Estas cifras se verifican **en cada lanzamiento** con `web_search` y jamás se consignan desde el conocimiento previo del modelo:

| Magnitud | Fuente de verificación |
|---|---|
| Salario mínimo interprofesional del ejercicio en curso | Real decreto anual publicado en el BOE |
| Tablas salariales del convenio para el año en curso | Texto del convenio y sus revisiones salariales publicadas |
| Bases máximas y mínimas de cotización | Orden anual de cotización publicada en el BOE |
| Duraciones máximas y porcentajes de los contratos formativos | Texto vigente del artículo 11 del Estatuto de los Trabajadores |
| Porcentaje y periodo de referencia del trabajo a distancia regular | Texto vigente de la Ley 10/2021 |

---

## Convenio colectivo

Datos que deben extraerse del convenio antes de redactar:

1. **Clasificación profesional:** grupos, niveles y funciones asignadas.
2. **Tablas salariales vigentes** para el grupo y nivel, y complementos obligatorios.
3. **Jornada anual y semanal**, distribución irregular y descansos.
4. **Periodo de prueba** máximo por grupo profesional.
5. **Duración máxima ampliada** del contrato por circunstancias de la producción, si el convenio sectorial la amplía.
6. **Reglas de llamamiento** en el contrato fijo-discontinuo y, en su caso, bolsa sectorial de empleo.
7. **Retribución de los contratos formativos**.
8. **Compensación de gastos** en trabajo a distancia.

| Registro | URL |
|---|---|
| REGCON — Registro y depósito de convenios y acuerdos colectivos | https://expinterweb.mites.gob.es/regcon/ |
| Boletines autonómicos y provinciales | Verificar con `web_search` |

---

## Modelos oficiales

El Servicio Público de Empleo Estatal publica los modelos oficiales de contrato y sus anexos, así como la aplicación Contrat@ para la comunicación del contenido de los contratos. Los assets de esta skill siguen la estructura de contrato negocial completo —reunidos, expositivos y cláusulas—, más apta para la revisión profesional que el formulario administrativo, y no sustituyen a la comunicación en Contrat@, que es un trámite separado.

| Recurso | URL |
|---|---|
| SEPE — Modelos de contrato de trabajo | https://www.sepe.es/ |
| Contrat@ — Comunicación de la contratación laboral | https://www.sepe.es/ |

---

## Estilo de redacción

Principios aplicados en los assets: estructura clásica de contrato con REUNIDOS, EXPONEN y CLÁUSULAS numeradas en ordinales; causa de temporalidad expresada en el expositivo y reiterada en la cláusula de duración, de modo que no pueda desgajarse; cláusulas de confidencialidad, protección de datos y prevención de riesgos en todas las modalidades; bloque final de advertencias dirigido al profesional que revisa, con las obligaciones de formalización y sus plazos.
