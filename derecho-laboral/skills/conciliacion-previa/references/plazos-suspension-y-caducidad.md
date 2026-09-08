# Plazos, Suspensión y Caducidad

> Referencia de cómputo para la skill `conciliacion-previa`. El cálculo se hace y se comunica antes de
> redactar cualquier documento.

---

## 1. Los plazos que gobiernan el asunto

| Acción | Plazo | Naturaleza | Precepto |
|---|---|---|---|
| Impugnación de despido | 20 días **hábiles** desde el día siguiente a la fecha de efectos | Caducidad | Artículo 59.3 del Estatuto de los Trabajadores y artículo 103 de la Ley 36/2011 |
| Impugnación de sanción | 20 días hábiles desde la notificación | Caducidad | Artículo 59.3 del Estatuto de los Trabajadores y artículo 114 de la Ley 36/2011 |
| Reclamación de cantidad | 1 año desde que la acción pudo ejercitarse | Prescripción | Artículo 59.1 y 59.2 del Estatuto de los Trabajadores |
| Acciones derivadas del contrato sin plazo especial | 1 año desde su terminación | Prescripción | Artículo 59.1 del Estatuto de los Trabajadores |
| Nulidad del acuerdo de conciliación | 30 días desde su celebración | Caducidad | Artículo 67 de la Ley 36/2011 |

## 2. Caducidad y prescripción no son lo mismo

| | Caducidad | Prescripción |
|---|---|---|
| Efecto de la papeleta | **Suspende** el cómputo | **Interrumpe** el cómputo |
| Al reanudarse | Continúa desde donde se quedó, descontados los días consumidos | Vuelve a contar **desde cero** |
| Apreciación de oficio | Sí | No, debe alegarse por la parte |
| Interrupción por reclamación extrajudicial | No | Sí, si es fehaciente |

Consecuencia práctica: en un despido, cada día consumido antes de presentar la papeleta se pierde para siempre. En una reclamación de cantidad, un burofax bien enviado reinicia el año completo.

## 3. Cómputo de los días hábiles

- Se excluyen **sábados, domingos y días festivos**, nacionales, autonómicos y **locales del lugar** donde deba presentarse el escrito.
- El plazo comienza el **día siguiente** a la fecha de efectos del despido o a la notificación de la sanción, no el mismo día.
- El **mes de agosto es hábil** en el orden social a estos efectos, a diferencia de otros órdenes jurisdiccionales.
- Verificar el calendario laboral oficial de la localidad con `web_search` antes de dar por vivo o vencido un plazo.

## 4. Efecto de la papeleta sobre el plazo (artículo 65)

La presentación de la solicitud de conciliación o de mediación **suspenderá los plazos de caducidad** e **interrumpirá los de prescripción**.

El cómputo de la caducidad **se reanudará al día siguiente** de:
- intentada la conciliación o mediación, o
- transcurridos **quince días hábiles** desde su presentación sin que se haya celebrado.

En todo caso, transcurridos **treinta días** sin haberse celebrado el acto, se tendrá por terminado el procedimiento y **cumplido el trámite**.

## 5. La aritmética que hay que explicar al cliente

Ejemplo de razonamiento que la skill debe reproducir con las fechas reales del asunto:

1. Fecha de efectos del despido: día 0.
2. Plazo total: 20 días hábiles, contados desde el día siguiente.
3. Días hábiles consumidos hasta la presentación de la papeleta: se descuentan.
4. Presentada la papeleta, el plazo queda **suspendido**.
5. Celebrada la conciliación sin avenencia, o transcurridos quince días hábiles sin celebrarse, el cómputo se reanuda al día siguiente.
6. Días hábiles restantes para presentar la demanda: los 20 iniciales menos los consumidos en el paso 3.

**Advertencia obligatoria:** presentar la papeleta el día decimonoveno deja **un solo día hábil** para demandar tras la conciliación. Presentarla en los primeros días conserva el margen. Esta es la explicación que evita la mayoría de las caducidades.

## 6. Interrupción de la prescripción en las reclamaciones de cantidad

La prescripción anual de las acciones para exigir percepciones económicas se interrumpe por:

- La presentación de la papeleta de conciliación.
- La **reclamación extrajudicial fehaciente** al deudor: burofax con certificación de texto y acuse de recibo, requerimiento notarial, o cualquier medio que acredite el contenido y la fecha de recepción.
- El reconocimiento de la deuda por la empresa.

Cada concepto prescribe por separado desde su propio devengo: en una reclamación de varios meses de salario, los meses más antiguos pueden estar prescritos aunque los recientes no lo estén. Revisar el desglose concepto a concepto antes de reclamar.

## 7. Lista de comprobación antes de presentar

1. ¿Cuál es la fecha exacta del hecho y cuál es el plazo aplicable?
2. ¿Se ha consultado el calendario laboral de la localidad para excluir los festivos locales?
3. ¿Cuántos días hábiles se han consumido y cuántos quedan?
4. ¿Está el asunto exceptuado del trámite, de modo que la papeleta no suspendería nada?
5. ¿Queda margen suficiente tras la conciliación para preparar y presentar la demanda?
6. ¿Hay conceptos económicos prescritos que deban excluirse del desglose?
7. ¿Se conserva prueba de la fecha de presentación con copia sellada o justificante telemático?
