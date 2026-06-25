import os
import tomllib
from pathlib import Path

from dokufmt.config.configuration import Configuration
from dokufmt.config.option import Option


class ConfigurationLoader:
    CONFIG_FILENAME = ".dokufmtrc"

    def __init__(self, path: str | Path | None = None) -> None:
        self.__path: Path = self.__validate_path(path)
        self.__configuration = Configuration()

    def load(self) -> Configuration:
        if not self.__path.exists():
            return Configuration()

        with self.__path.open("rb") as file:
            data = tomllib.load(file)

        return self.__build_configuration(data=data)

    def __build_configuration(self, data: dict) -> Configuration:
        configuration = Configuration()
        options: dict[str, Option] = {}

        for key, values in data.items():
            enabled = values.get("enabled", True)

            option_values = dict(values)
            option_values.pop("enabled", None)

            options[key] = Option(
                enabled=enabled,
                values=option_values,
            )

        configuration.options = options

        return configuration

    def __validate_path(self, path: str | Path | None) -> Path:
        to_validate = self.__resolve_path(path)

        if self.CONFIG_FILENAME != to_validate.name:
            raise ValueError(f"File is not valid: {to_validate}")

        if not to_validate.exists():
            return to_validate

        if not to_validate.is_file():
            raise ValueError(f"File is not valid: {to_validate}")

        if not os.access(to_validate, os.R_OK):
            raise PermissionError(f"File is not readable: {to_validate}")

        if not os.access(to_validate, os.W_OK):
            raise PermissionError(f"File is not writable: {to_validate}")

        return to_validate

    def __resolve_path(self, path: str | Path | None) -> Path:
        if path is None:
            return Path.home() / self.CONFIG_FILENAME

        return Path(path).expanduser()
