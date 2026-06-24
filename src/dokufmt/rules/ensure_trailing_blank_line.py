from textwrap import dedent

from dokufmt.rules.rule import Rule


class EnsureTrailingBlankLine(Rule):
    code = "DR-002"
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
        return content.rstrip("\n") + "\n"
