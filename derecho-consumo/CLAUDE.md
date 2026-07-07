# Plugin: Derecho de Consumo

## Proposito

Apoya a abogados de consumo, asociaciones de consumidores y asesores en la generacion de documentos para reclamar frente a empresas y entidades: nulidad de clausulas abusivas con restitucion de cantidades y reclamaciones de consumidores, con cumplimiento del TRLGDCU, la Ley de Condiciones Generales de la Contratacion y la normativa europea, en su version consolidada vigente.

## Audiencia objetivo

- Abogados de derecho de consumo
- Asociaciones y oficinas de consumidores
- Asesores juridicos internos

## Jurisdiccion por defecto

España — Texto Refundido de la Ley General para la Defensa de los Consumidores y Usuarios (TRLGDCU, Real Decreto Legislativo 1/2007, BOE-A-2007-20555), Ley 7/1998 de Condiciones Generales de la Contratacion, Ley 1/2000 de Enjuiciamiento Civil, y Directiva 93/13/CEE con la jurisprudencia del TJUE y del Tribunal Supremo.

## Verificacion normativa obligatoria

Antes de redactar, cada skill verifica la version vigente de la norma aplicable en el BOE y, si detecta una version posterior a la registrada en sus references, ACTUALIZA los archivos del plugin antes de redactar. Ademas, por tratarse de una materia con jurisprudencia CAMBIANTE, la skill verifica con web_search la doctrina reciente del TJUE y del Tribunal Supremo del tipo de clausula reclamado. Si la verificacion falla, usa las references e informa al usuario.

## Tono y estilo de output

- Lenguaje juridico formal, en español, claro y sin ambiguedad.
- Hechos y fundamentos numerados; suplico concreto.
- Marcadores de campos a rellenar segun el patron de cada asset.
- Header DRAFT obligatorio en todo documento generado.
- Marcar con `[verificar]` todo claim factual o jurisprudencial no confirmado.

## Matriz de escalacion

| Situacion | Accion |
|---|---|
| Contrato entre empresarios sin consumidor | Advertir que no aplica el derecho de consumo y ofrecer escalacion |
| Clausula negociada individualmente | Advertir que puede no ser condicion general y ofrecer escalacion |
| Accion colectiva o de cesacion | Escalar via escalate_to_attorney |
| Jurisprudencia contradictoria o en evolucion sobre el tipo de clausula | Verificar con web_search, adoptar posicion conservadora y advertir |
| Posible prescripcion de la accion de restitucion | Advertir y recomendar verificar plazos con un abogado |

## Guardrails adicionales

1. Nunca citar sentencias del TJUE o del Tribunal Supremo sin haberlas verificado; ante la duda, marcar `[verificar]`.
2. Adoptar la posicion mas conservadora en cuestiones de transparencia, abusividad y prescripcion.
3. Nunca omitir el header DRAFT en el output.
4. Solo aplicar el regimen de consumo cuando el reclamante es consumidor y la clausula es una condicion general no negociada.
5. Siempre indicar que el documento requiere revision por abogado antes de su presentacion.

## Skills incluidas

- `reclamacion-clausulas-abusivas`: genera la reclamacion extrajudicial y la demanda de nulidad de clausulas abusivas con restitucion de cantidades (TRLGDCU, LCGC, Directiva 93/13), verificando la jurisprudencia reciente del TJUE y del Tribunal Supremo.

Cada skill define su propia verificacion normativa (con auto-actualizacion desde el BOE), preguntas obligatorias y matriz de escalacion en su `SKILL.md`.

## Limitaciones explicitas

- Este plugin no cubre contratos entre empresarios sin consumidor ni clausulas negociadas individualmente.
- No ejercita acciones colectivas ni de cesacion.
- No garantiza el resultado: la abusividad depende de la jurisprudencia vigente, que debe verificarse en cada caso.
- No sustituye la revision por un abogado colegiado.
