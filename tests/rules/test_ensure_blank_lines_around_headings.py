from dokufmt.config.configuration import Configuration
from dokufmt.rules.ensure_blank_lines_around_headings import EnsureBlankLinesAroundHeadings
from tests.rules.rule_metadata_tests import RuleMetadataTests


class TestEnsureBlankLinesAroundHeadings(RuleMetadataTests):
    rule_class = EnsureBlankLinesAroundHeadings
    expected_code = Configuration.DR_004
    expected_name = "Ensure blank lines around headings"
    expected_description = "Ensure blank lines around headings, except at the start of the file."

    def test_empty_file(self) -> None:
        content = ""

        result = self.apply_rule(content)

        assert "" == result

    def test_file_without_headings_is_not_changed(self) -> None:
        content = "Something\nSomething else"

        result = self.apply_rule(content)

        assert content == result

    def test_file_with_only_one_heading_is_not_changed(self) -> None:
        content = "=== Header ==="

        result = self.apply_rule(content)

        assert content == result

    def test_heading_at_start_gets_blank_line_after(self) -> None:
        content = "=== Header ===\nSomething"
        expected = "=== Header ===\n\nSomething"

        result = self.apply_rule(content)

        assert expected == result

    def test_heading_at_end_gets_blank_line_before(self) -> None:
        content = "Something\n=== Header ==="
        expected = "Something\n\n=== Header ==="

        result = self.apply_rule(content)

        assert expected == result

    def test_heading_in_middle_gets_blank_lines_around(self) -> None:
        content = "Before\n=== Header ===\nAfter"
        expected = "Before\n\n=== Header ===\n\nAfter"

        result = self.apply_rule(content)

        assert expected == result

    def test_existing_blank_lines_are_not_duplicated(self) -> None:
        content = "Before\n\n=== Header ===\n\nAfter"

        result = self.apply_rule(content)

        assert content == result

    def test_consecutive_headings_get_one_blank_line_between_them(self) -> None:
        content = "=== Header 1 ===\n=== Header 2 ==="
        expected = "=== Header 1 ===\n\n=== Header 2 ==="

        result = self.apply_rule(content)

        assert expected == result

    def test_heading_with_leading_and_trailing_whitespace_is_matched(self) -> None:
        content = "Before\n   === Header ===   \nAfter"
        expected = "Before\n\n   === Header ===   \n\nAfter"

        result = self.apply_rule(content)

        assert expected == result

    def test_heading_can_have_equal_signs_as_content(self) -> None:
        content = "Before\n=== === ===\nAfter"
        expected = "Before\n\n=== === ===\n\nAfter"

        result = self.apply_rule(content)

        assert expected == result

    def test_heading_with_different_number_of_equal_signs_is_ignored(self) -> None:
        content = "Before\n=== Header ==\nAfter"

        result = self.apply_rule(content)

        assert content == result

    def test_heading_with_one_equal_sign_is_ignored(self) -> None:
        content = "Before\n= Header =\nAfter"

        result = self.apply_rule(content)

        assert content == result

    def test_heading_with_more_than_six_equal_signs_is_ignored(self) -> None:
        content = "Before\n======= Header =======\nAfter"

        result = self.apply_rule(content)

        assert content == result

    def test_heading_without_spaces_is_ignored(self) -> None:
        content = "Before\n===Header===\nAfter"

        result = self.apply_rule(content)

        assert content == result