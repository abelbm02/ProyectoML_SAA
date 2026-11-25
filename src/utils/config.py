"""Carga de ficheros de configuración YAML."""

from pathlib import Path
from typing import Any
import yaml


def load_config(path: str | Path) -> dict[str, Any]:
    """Lee un fichero YAML y devuelve su contenido como diccionario."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
