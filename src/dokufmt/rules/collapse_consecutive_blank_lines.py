import re
from textwrap import dedent

from dokufmt.rules.rule import Rule


class CollapseConsecutiveBlankLines(Rule):
    code = "DR-003"
    name = "Collapse consecutive blank lines"
    description = "Limit consecutive blank lines to the configured maximum."

    __max_blank_lines = 1

    @property
    def example(self) -> str:
        return dedent(
            """
            Before:

            First line




            Second line

            After:

            First line

            Second line
            """
        ).strip()

    def apply(self, content: str) -> str:
        max_line_breaks = self.__calculate_max_line_breaks()
        minimum_line_breaks_to_replace = max_line_breaks + 1

        return re.sub(
            pattern=rf"\n{{{minimum_line_breaks_to_replace},}}",
            repl="\n" * max_line_breaks,
            string=content,
        )

    def __calculate_max_line_breaks(self) -> int:
        return self.__max_blank_lines + 1
