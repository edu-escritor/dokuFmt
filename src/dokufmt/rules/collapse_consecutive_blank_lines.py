import re
from textwrap import dedent

from dokufmt.config.configuration import Configuration
from dokufmt.rules.rule import Rule


class CollapseConsecutiveBlankLines(Rule):
    code = Configuration.DR_003
    name = "Collapse consecutive blank lines"
    description = "Limit consecutive blank lines to the configured maximum."

    __max_blank_lines = 1
    __max_blank_lines_option = "max-blank-lines"

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
        if not self.is_enabled:
            return content

        max_line_breaks = self.__calculate_max_line_breaks()
        minimum_line_breaks_to_replace = max_line_breaks + 1

        return re.sub(
            pattern=rf"\n{{{minimum_line_breaks_to_replace},}}",
            repl="\n" * max_line_breaks,
            string=content,
        )

    def __calculate_max_line_breaks(self) -> int:
        max_blank_lines = self._option.values.get(
            self.__max_blank_lines_option,
            self.__max_blank_lines,
        )

        return max_blank_lines + 1
