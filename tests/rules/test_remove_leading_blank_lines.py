from dokufmt.rules.remove_leading_blank_lines import RemoveLeadingBlankLines
from tests.rules.rule_metadata_tests import RuleMetadataTests


class TestRemoveLeadingBlankLines(RuleMetadataTests):
    rule_class = RemoveLeadingBlankLines
    expected_code = "DR-001"
    expected_name = "Remove leading blank lines"
    expected_description = "Remove blank lines from the beginning of the file."

    def test_removes_leading_blank_lines(self) -> None:
        rule = self.create_rule()

        result = rule.apply(content="\n\n====== Title ======\nText")

        assert "====== Title ======\nText" == result

    def test_removes_leading_blank_lines_no_line(self) -> None:
        rule = self.create_rule()

        result = rule.apply(content="====== Title ======\nText")

        assert "====== Title ======\nText" == result
