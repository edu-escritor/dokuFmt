from dataclasses import dataclass, field

from dokufmt.config.option import Option


@dataclass
class Configuration:
    __options: dict[str, Option] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.__options = self.defaults()

    @property
    def keys(self) -> tuple[str, ...]:
        return tuple(self.__options.keys())

    @property
    def options(self) -> dict[str, Option]:
        return self.__options

    @options.setter
    def options(self, value: dict[str, Option]) -> None:
        for key, option in value.items():
            self.set_option(key=key, option=option)

    def get_option(self, key: str) -> Option:
        return self.__options.get(key, Option())

    def set_option(self, key: str, option: Option) -> None:
        current_option = self.get_option(key=key)

        self.__options[key] = Option(
            enabled=option.enabled,
            values={
                **current_option.values,
                **option.values,
            },
        )

    def has_option(self, key: str) -> bool:
        return key in self.options

    def enable(self, key: str) -> None:
        option = self.get_option(key=key)

        self.__options[key] = Option(
            enabled=True,
            values=dict(option.values),
        )

    def disable(self, key: str) -> None:
        option = self.get_option(key=key)

        self.__options[key] = Option(
            enabled=False,
            values=dict(option.values),
        )

    @classmethod
    def defaults(cls) -> dict[str, Option]:
        return {
            "DR-001": Option(enabled=True),
            "DR-002": Option(enabled=True),
            "DR-003": Option(
                enabled=True,
                values={
                    "max-blank-lines": 1,
                },
            ),
        }
