from dokufmt.config.configuration import Configuration
from dokufmt.exceptions.disabled_rule_error import DisabledRuleError
from dokufmt.exceptions.unknown_rule_error import UnknownRuleError
from dokufmt.rules.ensure_trailing_blank_line import EnsureTrailingBlankLine
from dokufmt.rules.remove_leading_blank_lines import RemoveLeadingBlankLines
from dokufmt.rules.rule import Rule


class RuleFactory:
    __rules: dict[str, type[Rule]] = {
        RemoveLeadingBlankLines.code: RemoveLeadingBlankLines,
        EnsureTrailingBlankLine.code: EnsureTrailingBlankLine,
    }

    def __init__(self, config: Configuration) -> None:
        self.__config: Configuration = config

    def get(self, key: str, include_disabled: bool = False) -> Rule:
        rule_class = self.__rules.get(key)

        if rule_class is None:
            raise UnknownRuleError(key=key)

        option = self.__config.get_option(key=key)

        if not include_disabled and not option.enabled:
            raise DisabledRuleError(key=key)

        return rule_class(option=option)

    @property
    def keys(self) -> tuple[str, ...]:
        return tuple(self.__rules.keys())

    def all(self, include_disabled: bool = False) -> list[Rule]:
        rules: list[Rule] = []

        for key in self.keys:
            try:
                rules.append(
                    self.get(
                        key=key,
                        include_disabled=include_disabled,
                    )
                )
            except DisabledRuleError:
                continue

        return rules
