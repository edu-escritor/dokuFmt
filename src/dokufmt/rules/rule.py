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
        """Return a human-readable before/after example for this rule."""
        pass

    @abstractmethod
    def apply(self, content: str) -> str:
        """Apply the rule to the given content and return the transformed content."""
        pass

    @property
    def is_enabled(self) -> bool:
        """Return whether this rule is enabled in the current configuration."""
        return self._option.enabled

    @staticmethod
    def is_last_line(index: int, lines: list[str]) -> bool:
        return index == len(lines) - 1

    @staticmethod
    def is_empty_line(line: str) -> bool:
        return "" == line.strip()

    @staticmethod
    def content_to_lines(content: str) -> list[str]:
        return content.splitlines()

    @staticmethod
    def lines_to_content(lines: list[str]) -> str:
        return "\n".join(lines)