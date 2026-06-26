from textwrap import dedent

from dokufmt.config.configuration import Configuration
from dokufmt.rules.rule import Rule


class EnsureTrailingBlankLine(Rule):
    code = Configuration.DR_002
    name = "Ensure trailing blank line"
    description = "Ensure the file ends with exactly one trailing blank line."

    @property
    def example(self) -> str:
        return dedent(
            """
            Before:

            The last line

            After:

            The last line
            """
        ).strip()

    def apply(self, content: str) -> str:
        if not self.is_enabled:
            return content

        return content.rstrip("\n") + "\n"
