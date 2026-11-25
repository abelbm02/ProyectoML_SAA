"""Script de entrenamiento del modelo de predicción de abandono."""

import argparse
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from src.data.load_data import load_csv
from src.features.build_features import build_features
from src.utils.config import load_config


def train(config_path: str) -> Path:
    """Entrena el modelo según la configuración indicada y guarda el artefacto."""
    cfg = load_config(config_path)
    df = load_csv(cfg["data"]["raw_path"])
    df = build_features(df)

    target = cfg["data"]["target_column"]
    X = df.drop(columns=[target])
    y = df[target]

    X_train, _, y_train, _ = train_test_split(
        X,
        y,
        test_size=cfg["data"]["test_size"],
        random_state=cfg["project"]["random_state"],
        stratify=y,
    )

    model = RandomForestClassifier(
        random_state=cfg["project"]["random_state"],
        **cfg["model"]["params"],
    )
    model.fit(X_train, y_train)

    output_path = Path(cfg["model"]["output_path"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Entrenamiento del modelo de churn")
    parser.add_argument("--config", default="configs/config.yaml", help="Ruta al fichero YAML")
    args = parser.parse_args()
    saved_model = train(args.config)
    print(f"Modelo guardado en: {saved_model}")
