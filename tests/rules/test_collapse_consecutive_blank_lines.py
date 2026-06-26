from dokufmt.config.configuration import Configuration
from dokufmt.rules.collapse_consecutive_blank_lines import CollapseConsecutiveBlankLines
from tests.rules.rule_metadata_tests import RuleMetadataTests


class TestCollapseConsecutiveBlankLines(RuleMetadataTests):
    rule_class = CollapseConsecutiveBlankLines
    expected_code = Configuration.DR_003
    expected_name = "Collapse consecutive blank lines"
    expected_description = "Limit consecutive blank lines to the configured maximum."

    def test_collapses_multiple_blank_lines_to_default_maximum(self) -> None:
        rule = self.create_rule()

        result = rule.apply(content="First line\n\n\n\n\nSecond line")

        assert "First line\n\nSecond line" == result

    def test_keeps_one_blank_line_with_default_maximum(self) -> None:
        rule = self.create_rule()

        result = rule.apply(content="First line\n\nSecond line")

        assert "First line\n\nSecond line" == result

    def test_keeps_content_without_blank_lines(self) -> None:
        rule = self.create_rule()

        result = rule.apply(content="First line\nSecond line")

        assert "First line\nSecond line" == result
