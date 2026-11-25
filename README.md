# Predicción de Abandono de Clientes (Customer Churn)

Proyecto de Machine Learning orientado a predecir qué clientes tienen mayor probabilidad de cancelar su suscripción o dejar de utilizar el servicio de la empresa, permitiendo activar acciones de retención de forma temprana.

---

## 1. ¿Qué problema intenta resolver el proyecto?

La pérdida de clientes (*churn*) tiene un impacto directo en los ingresos recurrentes de la empresa, ya que captar un nuevo cliente suele ser más costoso que retener uno existente.  
Este proyecto plantea un problema de **aprendizaje supervisado de clasificación binaria** cuyo objetivo es estimar la probabilidad de abandono (`churn = 1` frente a `churn = 0`) en un horizonte de 30 días, a partir del historial de comportamiento de cada cliente.

---

## 2. ¿Qué datos utiliza?

El modelo trabaja con **datos tabulares** procedentes de los sistemas internos de la empresa (anonimizados antes de su procesamiento):

- **Datos demográficos y de cuenta:** antigüedad del cliente, tipo de plan contratado, canal de alta.
- **Datos de facturación:** importe mensual, método de pago, historial de impagos o descuentos aplicados.
- **Datos de uso del servicio:** frecuencia de acceso, número de sesiones mensuales, funcionalidades utilizadas.
- **Datos de soporte:** número de incidencias abiertas, tiempo medio de resolución, puntuación de satisfacción.

Los ficheros originales se almacenan localmente en `data/raw/` (excluidos del control de versiones) y los conjuntos limpios listos para entrenar en `data/processed/`.

---

## 3. ¿Cómo se instala el entorno?

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. **Crear y activar un entorno virtual:**
   - En Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - En Linux / macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instalar las dependencias:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno (opcional):**
   Copiar `.env.example` a `.env` y ajustar las rutas o parámetros locales si fuera necesario.

---

## 4. ¿Cómo se ejecutaría el entrenamiento?

El flujo de entrenamiento está modularizado en `src/` y gobernado por el fichero de configuración `configs/config.yaml`:

1. Colocar el dataset original en `data/raw/clientes.csv`.
2. Ejecutar el script de entrenamiento desde la raíz del proyecto:
   ```bash
   python -m src.models.train --config configs/config.yaml
   ```
3. El proceso realizará la carga de datos, limpieza, generación de variables (*feature engineering*), división en entrenamiento/validación, ajuste del modelo y evaluación.
4. El modelo entrenado se guardará automáticamente en `models/churn_model.joblib` (ignorado por Git) y las métricas en `reports/`.

---

## 5. ¿Cómo se obtendrían predicciones?

Una vez entrenado y guardado el modelo en `models/`, se pueden generar predicciones sobre nuevos datos ejecutando:

```bash
python -m src.models.predict --input data/processed/nuevos_clientes.csv --output reports/predicciones.csv
```

El script cargará el artefacto del modelo, aplicará las mismas transformaciones de preprocesamiento y generará un fichero CSV con el identificador del cliente, la probabilidad estimada de abandono y la clase predicha (`0` o `1`).

---

## Estructura del repositorio

```text
.
├── README.md                 # Documentación principal del proyecto
├── requirements.txt          # Dependencias exactas de Python
├── .gitignore                # Exclusiones de control de versiones
├── .env.example              # Plantilla de variables de entorno
├── configs/                  # Hiperparámetros y rutas de configuración
├── data/                     # Datos (raw, processed, external) ignorados en Git
├── docs/                     # Análisis previo y justificación de la estructura
├── models/                   # Modelos entrenados serializados (ignorados en Git)
├── notebooks/                # Notebooks de exploración y prototipado
├── reports/                  # Gráficas, métricas y salidas de predicción
├── src/                      # Código fuente modularizado (data, features, models, utils)
└── tests/                    # Pruebas unitarias del pipeline
```
