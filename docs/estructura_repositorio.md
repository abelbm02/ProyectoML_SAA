# Diseño y Justificación de la Estructura del Repositorio

## Estructura completa de directorios

```text
churn-prediction-ml/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── configs/
│   └── config.yaml
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   ├── processed/
│   │   └── .gitkeep
│   └── external/
│       └── .gitkeep
├── docs/
│   ├── analisis_previo.md
│   └── estructura_repositorio.md
├── models/
│   └── .gitkeep
├── notebooks/
│   └── 01_exploracion_datos.ipynb
├── reports/
│   └── figures/
│       └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── load_data.py
│   ├── features/
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py
│   │   └── predict.py
│   └── utils/
│       ├── __init__.py
│       └── config.py
└── tests/
    ├── __init__.py
    └── test_pipeline.py
```

## Justificación de las decisiones adoptadas

- **`README.md` y `docs/`:** separan la guía rápida de entrada (`README.md`) de la documentación técnica y de análisis (`docs/`), facilitando que cualquier nuevo desarrollador entienda el problema, la arquitectura y la puesta en marcha sin saturar la raíz.
- **`requirements.txt` y `.env.example`:** garantizan la **reproducibilidad del entorno** fijando versiones mínimas de librerías y documentando las variables locales necesarias sin exponer credenciales reales (`.env` está excluido en `.gitignore`).
- **`configs/config.yaml`:** centraliza rutas, semillas aleatorias (`random_state`) e hiperparámetros fuera del código Python. Así el equipo puede experimentar cambiando parámetros sin modificar la lógica de entrenamiento.
- **`data/` (`raw/`, `processed/`, `external/`):** distingue los datos originales inmutables (`raw/`) de los datos limpios y transformados (`processed/`) y fuentes externas (`external/`). Su contenido se excluye de Git para no versionar ficheros pesados o sensibles, conservando la jerarquía con `.gitkeep`.
- **`notebooks/`:** aísla la fase exploratoria (EDA y prototipado rápido) del código productivo en `src/`. Los notebooks siguen un prefijo numérico (`01_...`) para mantener un orden cronológico claro.
- **`src/` modularizado (`data/`, `features/`, `models/`, `utils/`):** separa responsabilidades en módulos pequeños y reutilizables (carga de datos, ingeniería de características, entrenamiento/predicción y utilidades), facilitando las pruebas, la revisión de código y el trabajo en paralelo mediante ramas de Git.
- **`models/` y `reports/figures/`:** reservan un espacio dedicado para artefactos binarios de modelos entrenados (ignorados en Git) y para gráficas o informes de evaluación generados durante los experimentos.
- **`tests/`:** incorpora pruebas unitarias con `pytest` para validar el pipeline de datos y evitar regresiones cuando varios desarrolladores colaboran en el mismo repositorio.
