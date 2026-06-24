from textwrap import dedent

from dokufmt.rules.rule import Rule


class RemoveLeadingBlankLines(Rule):
    code = "DR-001"
    name = "Remove leading blank lines"
    description = "Remove blank lines from the beginning of the file."

    @property
    def example(self) -> str:
        return dedent(
            """
            Before:



            ====== Title ======

            After:

            ====== Title ======
            """
        ).strip()

    def apply(self, content: str) -> str:
        return content.lstrip("\n")
