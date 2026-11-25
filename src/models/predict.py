"""Script de inferencia para generar predicciones sobre nuevos clientes."""

import argparse
from pathlib import Path
import joblib
import pandas as pd

from src.data.load_data import load_csv
from src.features.build_features import build_features


def predict(model_path: str, input_path: str, output_path: str) -> Path:
    """Genera predicciones de abandono y las exporta a CSV."""
    model = joblib.load(model_path)
    df = build_features(load_csv(input_path))

    probabilities = model.predict_proba(df)[:, 1]
    predictions = model.predict(df)

    results = pd.DataFrame(
        {
            "churn_probability": probabilities,
            "churn_prediction": predictions,
        }
    )
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(out, index=False)
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predicción de churn")
    parser.add_argument("--model", default="models/churn_model.joblib")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="reports/predicciones.csv")
    args = parser.parse_args()
    out_file = predict(args.model, args.input, args.output)
    print(f"Predicciones guardadas en: {out_file}")
