# Matriz de Derivación a Skills Especializadas del Catálogo

Cuando una consulta planteada por el usuario corresponda de forma directa y específica a un trámite o contrato cubierto por una skill vertical especializada de `plugins-collection`, el asistente debe resolver la duda de encuadre inicial y sugerir de forma proactiva la activación de la skill adecuada.

---

## 1. Mapa de Derivaciones

| Materia / Requerimiento Concreto | Skill Especializada | Plugin |
|---|---|---|
| Redacción o adaptación de contrato de alquiler de vivienda, local, temporada o habitación | `arrendamiento-urbano` | `derecho-civil` |
| Contrato de arras y compraventa de inmuebles | `compraventa-inmueble` | `derecho-civil` |
| Contratos privados entre particulares (préstamo, comodato, reconocimiento de deuda) | `contratos-particulares` | `derecho-civil` |
| Demanda de desahucio por falta de pago, expiración de plazo o precario | `desahucio` | `derecho-civil` |
| Convenio regulador y demandas de separación o divorcio (mutuo acuerdo o contencioso) | `divorcio` | `derecho-civil` |
| Ejecución forzosa de títulos judiciales, no judiciales y pensiones de familia | `ejecucion-titulos` | `derecho-civil` |
| Tramitación de herencias (aceptación, renuncia, cuaderno particional, división judicial) | `herencia` | `derecho-civil` |
| Demanda y preparación integral de juicio ordinario civil (cuantía > 15.000 € o art. 249 LEC) | `juicio-ordinario` | `derecho-civil` |
| Liquidación del régimen económico matrimonial de sociedad de gananciales | `liquidacion-gananciales` | `derecho-civil` |
| Medidas voluntarias, poderes preventivos y curatela de apoyo a personas con discapacidad | `medidas-apoyo-discapacidad` | `derecho-civil` |
| Medidas paternofiliales sobre hijos comunes de parejas no casadas | `medidas-hijos-no-matrimoniales` | `derecho-civil` |
| Modificación o extinción de medidas definitivas de familia (custodia, alimentos, pensión) | `modificacion-medidas` | `derecho-civil` |
| Reclamación judicial rápida de deudas dinerarias líquidas mediante proceso monitorio | `monitorio` | `derecho-civil` |
| Constitución, pactos de convivencia y pactos de ruptura de parejas de hecho | `pareja-de-hecho` | `derecho-civil` |
| Reclamaciones de cuotas de comunidad, impugnación de acuerdos y cesación en LPH | `propiedad-horizontal` | `derecho-civil` |
| Reclamación extrajudicial o judicial de deudas dinerarias y elección de vía procesal | `reclamacion-cantidad` | `derecho-civil` |
| Reclamación extrajudicial y judicial de nulidad de cláusulas abusivas de consumo | `reclamacion-clausulas-abusivas` | `derecho-civil` |
| Reclamación extrajudicial y judicial de daños por responsabilidad civil y accidentes | `responsabilidad-civil` | `derecho-civil` |
| Minuta de testamento abierto y planificación sucesoria en derecho común | `testamento-planificacion` | `derecho-civil` |
| Alta o baja de autónomo en Hacienda (modelo 036) y en la Seguridad Social (RETA) | `alta-baja-autonomo` | `gestoria` |
| Afiliación, alta y baja de trabajadores por cuenta ajena y empleados de hogar (TGSS) | `alta-baja-seguridad-social` | `gestoria` |
| Cambio de titularidad de vehículos y notificación de venta ante la DGT | `transferencia-vehiculo` | `gestoria` |
| Liquidación y autoliquidación del Impuesto de Sucesiones (modelo 650) | `liquidacion-impuesto-sucesiones` | `gestoria` |
| Solicitud de NIE y autorizaciones de residencia / extranjería (modelos EX) | `extranjeria-residencia` | `gestoria` |
| Creación, parametrización y registro de plantillas personalizadas aportadas por el usuario | `registrar-plantillas` | `gestion-plantillas` |


---

## 2. Pautas de Comunicación para la Derivación

1. **Atender primero la duda planteada:** Dar una respuesta preliminar que aclare el concepto o encuadre legal.
2. **Presentar la alternativa especializada:** Indicar que para redactar el documento final o tramitar el expediente completo, se dispone de una herramienta diseñada específicamente para ese caso con todas las garantías de la normativa consolidada.
3. **No bloquear:** Permitir que el usuario elija si prefiere continuar con un informe general o saltar a la skill especializada.
