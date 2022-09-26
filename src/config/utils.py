import os
import toml
from pathlib import Path
from typing import Any
from pydantic import BaseSettings


def toml_config_settings_source(settings: BaseSettings) -> dict[str, Any]:
    path = Path(os.path.dirname(__file__)) / 'settings.toml'
    return toml.loads(path.read_text())['settings']
