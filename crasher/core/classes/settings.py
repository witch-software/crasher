
from __future__ import annotations

from typing import Any, Optional
from pathlib import Path

from crasher.core.utils.validate import are_keys_present, add_missing_values

import os.path
import toml
import loguru


DEFAULT_SETTINGS: dict[str, Any] = {
    "General": {
        "Interface": {
            "Theme": "Light"
        },
        "Language": "en_US"
    }
}


class QCrasherApplicationSettings:

    path: Path
    data: dict[Any, Any]
    logger: Optional[loguru.Logger]

    def __init__(self, path: Path, *, logger: Optional[loguru.Logger] = None) -> None:
        self.path = path
        self.logger = logger

    def load_settings(self, default_settings=DEFAULT_SETTINGS) -> None:

        if self.logger:
            self.logger.info(f"Try to load settings from \"{self.path}\"...")

        loaded_toml_data = default_settings

        if os.path.exists(self.path):
            try:
                loaded_toml_data = toml.load(self.path)

                if not are_keys_present(loaded_toml_data, default_settings):

                    if self.logger:
                        self.logger.warning(
                            "Settings do not contain the required values. They will be replaced by default values")

                    loaded_toml_data = add_missing_values(loaded_toml_data, default_settings)

            except Exception as e:
                if self.logger:
                    self.logger.error(f"Failed to load settings from \"{self.path}\": {e}")

        self.data = loaded_toml_data

    def save_settings(self) -> None:
        with open(self.path, "w") as toml_file:
            toml.dump(self.data, toml_file)

        if self.logger:
            self.logger.success(f"Settings were successfully saved to a file \"{self.path}\"!")

    def get_value(self, key: Any, default: Any = None) -> Any:
        keys = key.split('.')
        current_dict = self.data

        # Traverse the dictionary to get the value
        for k in keys:
            current_dict = current_dict.get(k, {})
            if not current_dict:
                return default

        return current_dict or default

    def set_value(self, key: Any, value: Any) -> None:
        keys = key.split('.')
        current_dict = self.data

        # Traverse the dictionary to set the value and create missing sections
        for k in keys[:-1]:
            current_dict = current_dict.setdefault(k, {})

        current_dict[keys[-1]] = value