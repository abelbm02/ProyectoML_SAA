"""Utilidades para cargar datasets desde data/raw/ o data/processed/."""

from pathlib import Path
import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Carga un fichero CSV en un DataFrame de pandas."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"No se encontró el fichero de datos: {file_path}")
    return pd.read_csv(file_path)
