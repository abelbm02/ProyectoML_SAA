# Análisis Previo del Proyecto de Machine Learning

## 1. Tipo de proyecto de Machine Learning imaginado

La empresa desea desarrollar un **sistema de predicción de abandono de clientes (*Customer Churn Prediction*)** para su plataforma de servicios por suscripción. El objetivo es identificar de manera anticipada qué clientes tienen mayor probabilidad de cancelar su suscripción en los próximos 30 días, de modo que el equipo de atención al cliente y marketing pueda activar campañas de retención personalizadas antes de que se produzca la baja.

## 2. Tipo de problema

Se trata de un problema de **aprendizaje supervisado de clasificación binaria**:

- **Variable objetivo (`churn`):** toma el valor `1` si el cliente cancela o no renueva su suscripción en el periodo evaluado, y `0` si permanece activo.
- Además de la etiqueta binaria, el modelo devolverá una **probabilidad estimada de abandono** (entre `0` y `1`) para priorizar los casos de mayor riesgo.

## 3. Tipo de datos que podría utilizar

El proyecto utilizará **datos tabulares** estructurados procedentes de las bases de datos internas de la empresa (debidamente anonimizados):

- **Información de la cuenta:** antigüedad del cliente (meses), tipo de plan contratado, canal de captación.
- **Facturación y pagos:** cuota mensual, descuentos aplicados, método de pago, histórico de incidencias de cobro o impagos.
- **Uso del producto:** número de sesiones mensuales, tiempo medio de uso, días desde el último acceso, funcionalidades utilizadas.
- **Atención al cliente:** cantidad de tickets de soporte abiertos, tiempo medio de resolución y encuestas de satisfacción (NPS/CSAT).

## 4. Posibles limitaciones del modelo

1. **Desbalanceo de clases:** normalmente el porcentaje de bajas mensuales es muy inferior al de clientes que permanecen activos, lo que puede sesgar al modelo hacia la clase mayoritaria si no se aplican técnicas de balanceo o métricas adecuadas (F1-score, ROC-AUC, PR-AUC).
2. **Datos insuficientes o incompletos:** clientes recientes apenas cuentan con historial de uso o facturación, y registros antiguos pueden contener valores nulos o campos no registrados.
3. **Ruido y errores de medición:** fallos puntuales en la telemetría de uso (sesiones no registradas) o tickets de soporte mal categorizados manualmente pueden introducir ruido en las variables de entrada.
4. **Deriva de datos (*Data / Concept Drift*):** cambios en tarifas, lanzamiento de nuevas funcionalidades o campañas promocionales estacionales pueden alterar el comportamiento de los clientes y degradar el rendimiento del modelo con el tiempo, haciendo necesario un reentrenamiento periódico.
5. **Sesgos y privacidad:** es imprescindible anonimizar identificadores personales y vigilar que ninguna variable introduzca discriminación indirecta.
