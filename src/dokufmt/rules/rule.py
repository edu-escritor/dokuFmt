from abc import ABC, abstractmethod


class Rule(ABC):
    code: str
    name: str
    description: str

    @property
    @abstractmethod
    def example(self) -> str:
        pass

    @abstractmethod
    def apply(self, content: str) -> str:
        pass
