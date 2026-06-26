import pytest

from dokufmt.config.configuration import Configuration
from dokufmt.exceptions.unknown_rule_error import UnknownRuleError
from dokufmt.rules.ensure_trailing_blank_line import EnsureTrailingBlankLine
from dokufmt.rules.remove_leading_blank_lines import RemoveLeadingBlankLines
from dokufmt.rules.rule_factory import RuleFactory


def test_get_remove_leading_blank_lines_rule() -> None:
    factory = __get_factory()

    rule = factory.get(key="DR-001")

    assert isinstance(rule, RemoveLeadingBlankLines)


def test_get_ensure_trailing_blank_line_rule() -> None:
    factory = __get_factory()

    rule = factory.get(key="DR-002")

    assert isinstance(rule, EnsureTrailingBlankLine)


def test_get_unknown_rule_raises_error() -> None:
    factory = __get_factory()

    with pytest.raises(UnknownRuleError, match="Rule does not exist: DR-999"):
        factory.get(key="DR-999")


def test_keys_returns_available_rule_codes() -> None:
    factory = __get_factory()

    keys = factory.keys

    assert "DR-001" in keys
    assert "DR-002" in keys


def test_all_returns_all_rules() -> None:
    factory = __get_factory()

    rules = factory.all()

    assert 2 == len(rules)
    assert any(isinstance(rule, RemoveLeadingBlankLines) for rule in rules)
    assert any(isinstance(rule, EnsureTrailingBlankLine) for rule in rules)


def __get_factory() -> RuleFactory:
    config = Configuration()

    return RuleFactory(config=config)
