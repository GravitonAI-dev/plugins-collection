# Gestión del Despacho

Plugin de GravitonAI para la generación de los documentos que el **propio despacho profesional** necesita para organizarse y protegerse, verificando la normativa vigente en el BOE y la normativa deontológica del colegio de adscripción antes de redactar. **5 skills** que cubren la contratación con el cliente, la facturación y la reclamación de honorarios, los instrumentos de representación, el cumplimiento en prevención del blanqueo de capitales y el cumplimiento en protección de datos.

A diferencia del resto de plugins del catálogo, aquí el cliente del documento es el despacho, no un tercero.

---

## Qué hace

- Formaliza el encargo antes de empezar: hoja de encargo profesional con el alcance definido **por inclusión y por exclusión** —porque la mayoría de los conflictos por honorarios nace del alcance, no del precio—, presupuesto previo, hoja de encargo con retribución vinculada al resultado, y comunicación de finalización o renuncia al encargo.
- Recorre las cinco modalidades retributivas con su riesgo característico, exige un honorario determinado o determinable, y aplica el **control de transparencia** reforzado cuando el cliente es persona física consumidora.
- Emite la minuta detallada con relación fechada de actuaciones y desglose en tres bloques —honorarios, suplidos y liquidación—, requiere de pago, insta la **jura de cuentas del artículo 35 de la Ley de Enjuiciamiento Civil** y contesta la impugnación de la minuta, distinguiendo si es por indebida o por excesiva.
- Antes de cualquier reclamación comprueba si existe hoja de encargo firmada y qué dice, si el honorario se devengó en un asunto judicial —único supuesto en que cabe la jura de cuentas— y si el cliente es consumidor.
- Genera los instrumentos de representación: minuta de poder general para pleitos y de poder especial, apoderamiento apud acta, designación en el orden social y autorización de representación administrativa, **advirtiendo siempre de las facultades que exigen poder especial** y que un poder general no cubre.
- Documenta la diligencia debida en prevención del blanqueo: ficha de identificación, declaración de titularidad real, lista de comprobación por expediente e informe interno de examen especial, **delimitando primero si la actuación está sujeta y si opera la exención legal** relativa a la determinación de la posición jurídica y a la defensa.
- Genera el paquete de protección de datos: registro de actividades de tratamiento, contrato de encargado, cláusula informativa, compromiso de confidencialidad del personal y registro de brechas de seguridad con su análisis de riesgo.
- Atiende a las dos particularidades del despacho como responsable del tratamiento: el **secreto profesional**, que modula el ejercicio de los derechos de los interesados y el acceso de terceros, y el tratamiento cotidiano de **categorías especiales de datos** y de datos relativos a condenas e infracciones penales.
- **Identifica el colegio de adscripción** y comprueba su normativa antes de invocar cualquier deber deontológico o criterio de honorarios: lo que existe en un colegio puede no existir en otro.
- Verifica en cada asunto las magnitudes que cambian solas: tipos de impuesto sobre el valor añadido y de retención a cuenta, interés legal del dinero, umbrales y plazos de la normativa de prevención del blanqueo, y plazos de notificación de brechas. Nunca quedan escritas fijas en la plantilla.

## Qué NO hace

- No genera documentos del asunto del cliente —contratos, demandas, escritos procesales—, que corresponden a `derecho-civil`, `derecho-laboral` y `gestoria`.
- No genera la **comunicación por indicio** al órgano competente en materia de prevención del blanqueo: se formaliza en modelos oficiales, la efectúa el representante del sujeto obligado y exige asesoramiento especializado. Ante indicios, la skill se detiene y deriva.
- No diseña el sistema de prevención del blanqueo del despacho —manual, análisis de riesgo, designación de representante, examen externo— ni su sistema completo de protección de datos.
- No realiza la evaluación de impacto en protección de datos cuando resulta exigible, ni sustituye al delegado de protección de datos.
- No emite dictámenes de cumplimiento normativo ni certifica la adecuación de los sistemas del despacho.
- No sustituye el asesoramiento deontológico del colegio de adscripción.
- No cubre poderes preventivos ni medidas de apoyo a personas con discapacidad, que corresponden a `derecho-civil:medidas-apoyo-discapacidad`, ni poderes mercantiles de representación orgánica.
- No presenta ni comunica nada ante ninguna autoridad, colegio ni organismo.
- No da opinión jurídica concreta: el output es siempre un DRAFT para revisión por el profesional responsable.

---

## Skills

### `hoja-encargo`

Formaliza el encargo antes de iniciar la actuación. Recorre las modalidades retributivas explicando el riesgo de cada una, exige un honorario determinado o determinable, enumera las actuaciones excluidas —recursos, ejecución, procedimientos conexos, intervención de terceros profesionales— y aplica el control de transparencia cuando el cliente es consumidor.

Invocación: `/despacho:hoja-encargo`

Output: hoja de encargo profesional, presupuesto de honorarios, hoja de encargo con retribución vinculada al resultado, o comunicación de finalización del encargo, en markdown, DRAFT.

Qué NO hace: no reclama honorarios impagados ni redacta documentos del asunto.

### `minuta-jura-cuentas`

Factura y reclama. Comprueba primero la hoja de encargo, el ámbito del asunto y la naturaleza del cliente, calcula la prescripción, y construye la minuta detallada resolviendo la tensión característica del documento: necesita detalle para justificar el honorario y el secreto profesional limita lo que puede escribirse, de modo que se describen **actuaciones y no contenidos**.

Invocación: `/despacho:minuta-jura-cuentas`

Output: minuta de honorarios, requerimiento previo de pago, solicitud de jura de cuentas del artículo 35, o alegaciones frente a la impugnación de la minuta, en markdown, DRAFT.

Qué NO hace: no pacta los honorarios, ni insta la jura de cuentas por honorarios de asesoramiento extrajudicial, supuesto en que deriva a las vías civiles.

### `poder-representacion`

Genera los instrumentos de representación en los tres regímenes —civil, social y administrativo—, sin trasladar el esquema de uno a otro. Su aportación central es obligar al otorgante a pronunciarse **una a una** sobre las facultades que exigen poder especial, porque un despacho que llega a la vista sin la facultad de transigir no puede cerrar el acuerdo que el cliente necesita.

Invocación: `/despacho:poder-representacion`

Output: minuta de poder general para pleitos, minuta de poder especial, solicitud de apoderamiento apud acta, designación de representación en el orden social, o autorización de representación administrativa, en markdown, DRAFT.

Qué NO hace: la minuta de poder no es la escritura; corresponde al notario autorizante la forma del instrumento y la valoración de la capacidad y de la suficiencia de facultades.

### `prevencion-blanqueo`

Documenta la diligencia debida. Su primera función es de delimitación: la sujeción del profesional **no es general**, depende de la actuación concreta, y sobre ella opera además una exención legal cuyo alcance debe verificarse. Ante indicios, la skill se detiene, advierte de la prohibición de revelación y deriva.

Invocación: `/despacho:prevencion-blanqueo`

Output: ficha de identificación del cliente, declaración de titularidad real, lista de comprobación de diligencia debida, o informe interno de examen especial, en markdown, DRAFT.

Qué NO hace: no genera la comunicación por indicio, no diseña el sistema de prevención del despacho, y tiene prohibido sugerir formas de eludir las obligaciones de diligencia debida.

### `proteccion-datos-despacho`

Genera el paquete de cumplimiento en protección de datos, atendiendo a las particularidades del despacho: el secreto profesional y el tratamiento cotidiano de categorías especiales de datos. Determina primero si el despacho actúa como responsable o como encargado, y aplica la regla que evita el error más frecuente: **el consentimiento no es la base jurídica por defecto**.

Invocación: `/despacho:proteccion-datos-despacho`

Output: registro de actividades de tratamiento, contrato de encargado de tratamiento, cláusula informativa, compromiso de confidencialidad del personal, o registro y análisis de brecha de seguridad, en markdown, DRAFT.

Qué NO hace: no realiza la evaluación de impacto, no decide sobre la notificación de una brecha —documenta el análisis y deriva— ni sustituye al delegado de protección de datos.

---

## Marco normativo

| Materia | Norma de referencia |
|---|---|
| Ejercicio profesional y deontología | Estatuto General de la Abogacía Española aprobado por Real Decreto 135/2021, normativa deontológica del Consejo General de la Abogacía Española y del colegio de adscripción, y Ley 2/1974 de Colegios Profesionales |
| Reclamación de honorarios | Artículos 34 y 35 de la Ley 1/2000 de Enjuiciamiento Civil, y Ley 15/2007 de Defensa de la Competencia en cuanto a los criterios orientativos |
| Representación procesal | Artículos 23 a 26 de la Ley 1/2000, artículos 18 y 21 de la Ley 36/2011, y artículos 5 y 6 de la Ley 39/2015 |
| Secreto profesional | Artículo 542.3 de la Ley Orgánica 6/1985 del Poder Judicial |
| Prevención del blanqueo | Ley 10/2010 de prevención del blanqueo de capitales y de la financiación del terrorismo, y su reglamento de desarrollo |
| Protección de datos | Reglamento (UE) 2016/679 y Ley Orgánica 3/2018 |

**Regla de ámbito colegial:** ninguna skill invoca un deber deontológico concreto ni un criterio de honorarios sin haber identificado antes el colegio de adscripción y comprobado su normativa.

---

## Estructura

```
despacho/
├── .claude-plugin/plugin.json
├── .mcp.json
├── agent_tools.json
├── CLAUDE.md
├── README.md
└── skills/
    ├── hoja-encargo/               (4 assets, 4 references)
    ├── minuta-jura-cuentas/        (4 assets, 4 references)
    ├── poder-representacion/       (5 assets, 4 references)
    ├── prevencion-blanqueo/        (4 assets, 5 references)
    └── proteccion-datos-despacho/  (5 assets, 5 references)
```

Total: 22 plantillas y 22 archivos de referencia normativa.
