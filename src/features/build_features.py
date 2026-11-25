"""Transformaciones y generación de variables para el modelo de churn."""

import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Prepara las variables de entrada a partir del DataFrame limpio."""
    result = df.copy()
    if "monthly_fee" in result.columns and "tenure_months" in result.columns:
        result["total_estimated_spend"] = result["monthly_fee"] * result["tenure_months"]
    return result
