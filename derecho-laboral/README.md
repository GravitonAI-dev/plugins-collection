# Derecho Laboral

Plugin de GravitonAI para la generación de documentos del ciclo completo de la relación laboral española, verificando siempre la versión consolidada vigente en el BOE y el convenio colectivo aplicable antes de redactar. **8 skills** que cubren la contratación, la modificación de condiciones, el régimen disciplinario, la extinción, el cierre económico, la vía previa, la demanda ante el Juzgado de lo Social y la impugnación de resoluciones de Seguridad Social.

---

## Qué hace

- Genera el contrato de trabajo en las modalidades vigentes tras el Real Decreto-ley 32/2021 (indefinido, fijo-discontinuo, temporal por circunstancias de la producción, temporal por sustitución y formativo), a jornada completa o parcial, con el acuerdo de trabajo a distancia de la Ley 10/2021 cuando procede, y validando la causa de temporalidad y el encadenamiento del artículo 15.5.
- Comunica la modificación sustancial de condiciones (artículo 41), el traslado o desplazamiento con cambio de residencia (artículo 40) y la movilidad funcional (artículo 39), con la causa expresada, el preaviso correcto y la información al trabajador de su derecho de rescisión indemnizada; y redacta también el escrito de respuesta del trabajador.
- Ejerce la potestad disciplinaria: amonestación, sanción con suspensión de empleo y sueldo, pliego de cargos y resolución del expediente contradictorio, tomando la tipificación y graduación de faltas del convenio y controlando la prescripción del artículo 60.2.
- Redacta la comunicación extintiva en sus cuatro modalidades individuales: despido disciplinario, despido objetivo con puesta a disposición de la indemnización, no superación del periodo de prueba y finalización de contrato temporal.
- Cierra la relación en el plano económico: recibo de finiquito, hoja de liquidación detallada con la fórmula de cada concepto, acuerdo de extinción por mutuo acuerdo y carta de baja voluntaria.
- Prepara la vía previa: burofax de reclamación de cantidades y papeleta de conciliación por despido, cantidad o sanción, con **control de procedibilidad** —comprueba si el asunto está exceptuado del trámite— y cómputo del plazo de caducidad y de su suspensión.
- Redacta la demanda ante el Juzgado de lo Social en cinco modalidades procesales: despido, cantidad, sanción, modificación sustancial y movilidad del artículo 138, y tutela de derechos fundamentales.
- Impugna resoluciones de Seguridad Social: reclamación administrativa previa, disconformidad con el alta médica, solicitud de revisión del grado de incapacidad y demanda una vez agotada la vía previa.
- **Calcula y comunica siempre el plazo restante** antes de redactar: 20 días hábiles de caducidad en despido, sanción y modificación; 1 año de prescripción en cantidades; 30 días en la reclamación previa de Seguridad Social. En derecho del trabajo el derecho se pierde por el calendario antes que por el fondo.
- **Localiza el convenio colectivo aplicable** en REGCON o en el boletín correspondiente y toma de él la clasificación profesional, las tablas salariales, la jornada, los preavisos y el cuadro de faltas y sanciones. Ninguna sanción, despido disciplinario, salario o jornada se redacta sin él.
- Verifica en cada lanzamiento las magnitudes que cambian solas: salario mínimo interprofesional, tablas de convenio, bases de cotización, límites de exención fiscal de la indemnización. Nunca quedan escritas fijas en la plantilla.

## Qué NO hace

- No cubre procedimientos colectivos: despido colectivo (artículo 51), suspensión y reducción de jornada (artículo 47), inaplicación de convenio (artículo 82.3), conflicto colectivo, impugnación de convenios ni materia electoral.
- No cubre relaciones laborales especiales: alta dirección, empleados de hogar, artistas, deportistas profesionales, representantes de comercio ni centros especiales de empleo.
- No tramita altas, bajas, afiliación ni cotización ante la Tesorería General de la Seguridad Social: eso corresponde al plugin `gestoria`.
- No cubre los actos de encuadramiento, cotización y recaudación, que siguen la vía administrativa común y el orden contencioso-administrativo.
- No presenta escritos ante ningún organismo ni juzgado, ni firma por el profesional.
- No practica cálculos actuariales de prestaciones ni valoraciones médicas: no inventa ni interpreta datos clínicos.
- No cita jurisprudencia que no haya verificado en la propia sesión en una fuente oficial.
- No da opinión jurídica concreta: el output es siempre un DRAFT para revisión por abogado o graduado social colegiado.

---

## Skills

### `contrato-trabajo`

Genera el contrato de trabajo en las modalidades vigentes tras la reforma de 2021, a jornada completa o parcial, con el anexo de trabajo a distancia cuando procede. Valida la causa de temporalidad, comprueba el encadenamiento y verifica que el salario no sea inferior al convenio ni al salario mínimo interprofesional.

Invocación: `/derecho-laboral:contrato-trabajo`

Output: contrato indefinido, fijo-discontinuo, temporal por circunstancias de la producción, temporal por sustitución o formativo, y acuerdo de trabajo a distancia, en markdown, DRAFT.

Qué NO hace: no cubre relaciones laborales especiales, contrato de relevo ni contratos mercantiles de prestación de servicios.

### `modificacion-condiciones`

Comunica la alteración unilateral de condiciones de trabajo y redacta la respuesta del trabajador. Determina el origen de la condición vigente —si procede de convenio estatutario, detiene el proceso porque el cauce es el artículo 82.3—, exige la causa con datos concretos, calcula el preaviso y calcula la indemnización de rescisión.

Invocación: `/derecho-laboral:modificacion-condiciones`

Output: comunicación de modificación sustancial (artículo 41), de traslado o desplazamiento (artículo 40), de movilidad funcional (artículo 39), o escrito del trabajador optando por la extinción, en markdown, DRAFT.

Qué NO hace: no cubre las medidas colectivas que superan los umbrales del artículo 41.2 y exigen periodo de consultas.

### `sancion-disciplinaria`

Ejerce la potestad disciplinaria distinta del despido, con la tipificación y el cuadro de sanciones del convenio, el control de la prescripción de faltas y el expediente contradictorio cuando es preceptivo.

Invocación: `/derecho-laboral:sancion-disciplinaria`

Output: carta de amonestación, carta de sanción con suspensión de empleo y sueldo, pliego de cargos o resolución de expediente contradictorio, en markdown, DRAFT.

Qué NO hace: no redacta el despido disciplinario, que corresponde a `carta-despido`, ni sanciones a personal estatutario o funcionario.

### `carta-despido`

Redacta la comunicación extintiva por decisión del empresario en sus cuatro modalidades individuales, exigiendo hechos concretos, individualizados y fechados, y calculando la indemnización con su fórmula a la vista.

Invocación: `/derecho-laboral:carta-despido`

Output: carta de despido disciplinario, carta de despido objetivo, comunicación de no superación del periodo de prueba o comunicación de finalización de contrato temporal, en markdown, DRAFT.

Qué NO hace: no cubre el despido colectivo, la extinción por voluntad del trabajador ni el mutuo acuerdo.

### `finiquito-liquidacion`

Cierra la relación en el plano económico, con el desglose y la fórmula de cada concepto. Comprueba en el convenio el periodo de devengo de las pagas extraordinarias —el dato que más veces se calcula mal— y advierte del efecto de las vacaciones no disfrutadas sobre la fecha de baja en la Seguridad Social.

Invocación: `/derecho-laboral:finiquito-liquidacion`

Output: recibo de finiquito, hoja de liquidación detallada, acuerdo de extinción por mutuo acuerdo o carta de baja voluntaria, en markdown, DRAFT.

Qué NO hace: no redacta la comunicación extintiva ni reclama judicialmente las cantidades impagadas.

### `conciliacion-previa`

Prepara la vía previa al proceso. Su primera función es de control: comprueba si el asunto está exceptuado del intento de conciliación por el artículo 64 de la Ley 36/2011 —porque presentar papeleta en un asunto exceptuado no suspende el plazo y puede consumirlo—, calcula el plazo restante e identifica el organismo territorialmente competente.

Invocación: `/derecho-laboral:conciliacion-previa`

Output: burofax de reclamación de cantidades, papeleta de conciliación por despido, por cantidad o por sanción, o acuerdo conciliatorio, en markdown, DRAFT.

Qué NO hace: no cubre las reclamaciones en materia de Seguridad Social ni redacta la demanda.

### `demanda-social`

Redacta la demanda ante el Juzgado de lo Social en cinco modalidades procesales. Antes de escribir resuelve el control de admisibilidad: vía previa, plazo, competencia, postulación y mapa de codemandados, porque quien no fue citado en conciliación no puede ser demandado sin subsanar el trámite.

Invocación: `/derecho-laboral:demanda-social`

Output: demanda por despido, de reclamación de cantidad, de impugnación de sanción, de impugnación de modificación sustancial o de tutela de derechos fundamentales, en markdown, DRAFT.

Qué NO hace: no cubre procesos colectivos, despido colectivo, impugnación de convenios ni prestaciones de Seguridad Social.

### `reclamacion-seguridad-social`

Impugna resoluciones en materia de prestaciones. Controla la vía —en esta materia la conciliación está exceptuada pero la reclamación administrativa previa es requisito inexcusable— y el plazo, y construye el escrito desde la separación estricta entre diagnóstico y limitación funcional, con la descripción real de las tareas del puesto como argumento central.

Invocación: `/derecho-laboral:reclamacion-seguridad-social`

Output: reclamación administrativa previa, escrito de disconformidad con el alta médica, solicitud de revisión del grado de incapacidad o demanda en materia de prestaciones, en markdown, DRAFT.

Qué NO hace: no cubre afiliación, cotización, recaudación ni sanciones administrativas, que siguen la vía administrativa común.

---

## Marco normativo

| Norma | Identificador BOE |
|---|---|
| Estatuto de los Trabajadores — texto refundido aprobado por Real Decreto Legislativo 2/2015 | BOE-A-2015-11430 |
| Ley 36/2011, reguladora de la Jurisdicción Social | BOE-A-2011-15936 |
| Ley General de la Seguridad Social — texto refundido aprobado por Real Decreto Legislativo 8/2015 | BOE-A-2015-11724 |

Normas complementarias que cada skill verifica en el BOE antes de citarlas: Real Decreto-ley 32/2021 de reforma laboral, Ley 10/2021 de trabajo a distancia, Ley 31/1995 de prevención de riesgos laborales, Ley Orgánica 3/2007 de igualdad efectiva, Ley 15/2022 integral para la igualdad de trato y la no discriminación, y Ley Orgánica 11/1985 de Libertad Sindical.

**Convenio colectivo:** localizado en cada asunto en REGCON (https://expinterweb.mites.gob.es/regcon/) o en el boletín autonómico o provincial correspondiente.

---

## Estructura

```
derecho-laboral/
├── .claude-plugin/plugin.json
├── .mcp.json
├── agent_tools.json
├── CLAUDE.md
├── README.md
└── skills/
    ├── carta-despido/               (4 assets, 5 references)
    ├── conciliacion-previa/         (5 assets, 5 references)
    ├── contrato-trabajo/            (6 assets, 5 references)
    ├── demanda-social/              (5 assets, 5 references)
    ├── finiquito-liquidacion/       (4 assets, 4 references)
    ├── modificacion-condiciones/    (4 assets, 5 references)
    ├── reclamacion-seguridad-social/(4 assets, 5 references)
    └── sancion-disciplinaria/       (4 assets, 4 references)
```

Total: 36 plantillas y 38 archivos de referencia normativa.
