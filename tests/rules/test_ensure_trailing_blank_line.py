from dokufmt.rules.ensure_trailing_blank_line import EnsureTrailingBlankLine
from tests.rules.rule_metadata_tests import RuleMetadataTests


class TestEnsureTrailingBlankLine(RuleMetadataTests):
    rule_class = EnsureTrailingBlankLine
    expected_code = "DR-002"
    expected_name = "Ensure trailing blank line"
    expected_description = "Ensure the file ends with exactly one trailing blank line."

    def test_ensure_trailing_blank_line(self) -> None:
        rule = self.create_rule()

        result = rule.apply(content="The last line")

        assert "The last line\n" == result

    def test_ensure_trailing_blank_line_does_not_duplicate_existing_breaks(
        self,
    ) -> None:
        rule = self.create_rule()

        result = rule.apply(content="The last line\n\n\n")

        assert "The last line\n" == result
