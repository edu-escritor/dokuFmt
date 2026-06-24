import pytest

from dokufmt.rules.ensure_trailing_blank_line import EnsureTrailingBlankLine
from dokufmt.rules.remove_leading_blank_lines import RemoveLeadingBlankLines
from dokufmt.rules.rule_factory import RuleFactory


def test_get_remove_leading_blank_lines_rule() -> None:
    factory = RuleFactory()

    rule = factory.get(key="DR-001")

    assert isinstance(rule, RemoveLeadingBlankLines)


def test_get_ensure_trailing_blank_line_rule() -> None:
    factory = RuleFactory()

    rule = factory.get(key="DR-002")

    assert isinstance(rule, EnsureTrailingBlankLine)


def test_get_unknown_rule_raises_error() -> None:
    factory = RuleFactory()

    with pytest.raises(ValueError, match="Unknown rule: DR-999"):
        factory.get(key="DR-999")


def test_keys_returns_available_rule_codes() -> None:
    factory = RuleFactory()

    keys = factory.keys

    assert "DR-001" in keys
    assert "DR-002" in keys


def test_all_returns_all_rules() -> None:
    factory = RuleFactory()

    rules = factory.all()

    assert 2 == len(rules)
    assert any(isinstance(rule, RemoveLeadingBlankLines) for rule in rules)
    assert any(isinstance(rule, EnsureTrailingBlankLine) for rule in rules)
