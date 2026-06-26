from abc import ABC, abstractmethod

from dokufmt.config.option import Option


class Rule(ABC):
    code: str
    name: str
    description: str

    def __init__(self, option: Option) -> None:
        self._option: Option = option

    @property
    @abstractmethod
    def example(self) -> str:
        pass

    @abstractmethod
    def apply(self, content: str) -> str:
        pass

    def is_enabled(self) -> bool:
        return self._option.enabled
