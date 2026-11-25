"""Pruebas básicas para la ingeniería de características."""

import pandas as pd
from src.features.build_features import build_features


def test_build_features_adds_total_estimated_spend() -> None:
    df = pd.DataFrame({"monthly_fee": [20.0], "tenure_months": [6]})
    result = build_features(df)
    assert "total_estimated_spend" in result.columns
    assert result["total_estimated_spend"].iloc[0] == 120.0
