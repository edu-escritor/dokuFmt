from dokufmt.rules.ensure_trailing_blank_line import EnsureTrailingBlankLine
from dokufmt.rules.remove_leading_blank_lines import RemoveLeadingBlankLines
from dokufmt.rules.rule import Rule


class RuleFactory:
    __rules: dict[str, type[Rule]] = {
        RemoveLeadingBlankLines.code: RemoveLeadingBlankLines,
        EnsureTrailingBlankLine.code: EnsureTrailingBlankLine,
    }

    def get(self, key: str) -> Rule:
        rule_class = self.__rules.get(key)

        if rule_class is None:
            raise ValueError(f"Unknown rule: {key}")

        return rule_class()

    @property
    def keys(self) -> tuple[str, ...]:
        return tuple(self.__rules.keys())

    def all(self) -> list[Rule]:
        return [rule_class() for rule_class in self.__rules.values()]
