# Matriz de Derivación a Skills Especializadas del Catálogo

Cuando una consulta planteada por el usuario corresponda de forma directa y específica a un trámite o contrato cubierto por una skill vertical especializada de `plugins-collection`, el asistente debe resolver la duda de encuadre inicial y sugerir de forma proactiva la activación de la skill adecuada.

---

## 1. Mapa de Derivaciones

| Materia / Requerimiento Concreto | Skill Especializada | Plugin |
|---|---|---|
| Redacción o adaptación de contrato de alquiler de vivienda o local de negocio conforme a la LAU | `arrendamiento-urbano` | `derecho-civil` |
| Reclamación judicial de deudas dinerarias líquidas, vencidas y exigibles (facturas, impagos) | `monitorio` | `derecho-civil` |
| Demanda de desahucio por falta de pago o expiración de plazo de arrendamiento | `desahucio` | `derecho-civil` |
| Demanda de juicio ordinario civil (cuantía > 15.000 € o materias especiales art. 249 LEC) | `juicio-ordinario` | `derecho-civil` |
| Convenio regulador de divorcio o separación de mutuo acuerdo | `convenio-regulador` | `derecho-civil` |
| Cuaderno particional y reparto de herencia entre coherederos | `particion-herencia` | `derecho-civil` |
| Reclamación extrajudicial por cláusulas abusivas hipotecarias (gastos, comisión de apertura, IRPH) | `reclamacion-clausulas-abusivas` | `derecho-civil` |
| Alta o baja de autónomo en Hacienda (036) y en la Seguridad Social (RETA) | `alta-baja-autonomo` | `gestoria` |
| Afiliación, alta y baja de trabajadores por cuenta ajena y empleados de hogar | `alta-baja-seguridad-social` | `gestoria` |
| Cambio de titularidad de vehículos y notificación de venta ante la DGT | `transferencia-vehiculo` | `gestoria` |
| Liquidación y autoliquidación del Impuesto de Sucesiones (modelo 650) | `liquidacion-impuesto-sucesiones` | `gestoria` |
| Solicitud de NIE y autorizaciones de residencia / extranjería (modelos EX) | `extranjeria-residencia` | `gestoria` |
| Registro y parametrización de plantillas personalizadas aportadas por el usuario | `registrar-plantillas` | `gestion-plantillas` |

---

## 2. Pautas de Comunicación para la Derivación

1. **Atender primero la duda planteada:** Dar una respuesta preliminar que aclare el concepto o encuadre legal.
2. **Presentar la alternativa especializada:** Indicar que para redactar el documento final o tramitar el expediente completo, se dispone de una herramienta diseñada específicamente para ese caso con todas las garantías de la normativa consolidada.
3. **No bloquear:** Permitir que el usuario elija si prefiere continuar con un informe general o saltar a la skill especializada.
