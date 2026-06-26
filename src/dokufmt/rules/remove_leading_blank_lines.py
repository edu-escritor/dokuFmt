from textwrap import dedent

from dokufmt.config.configuration import Configuration
from dokufmt.rules.rule import Rule


class RemoveLeadingBlankLines(Rule):
    code = Configuration.DR_001
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
        if not self.is_enabled:
            return content

        return content.lstrip("\n")
