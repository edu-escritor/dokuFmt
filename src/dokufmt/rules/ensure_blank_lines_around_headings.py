import re
from textwrap import dedent
from typing import Final

from dokufmt.config.configuration import Configuration
from dokufmt.config.option import Option
from dokufmt.rules.rule import Rule


class EnsureBlankLinesAroundHeadings(Rule):
    code = Configuration.DR_004
    name = "Ensure blank lines around headings"
    description = "Ensure blank lines around headings, except at the start of the file."

    _HEADING_PATTERN: Final[re.Pattern[str]] = re.compile(r"\s*(={2,6})\s+.+?\s+\1\s*")

    def __init__(self, option: Option) -> None:
        super().__init__(option=option)

    @property
    def example(self) -> str:
        return dedent(
            """
            Before:

            Something
            ===== Title =====
            Something

            After:

            Something

            ===== Title =====

            Something
            """
        ).strip()

    def apply(self, content: str) -> str:
        if not self.is_enabled:
            return content

        lines: list[str] = self.content_to_lines(content=content)
        handled_lines: list[str] = []
        prior_line: str|None = None

        for index, line in enumerate(lines):
            if not self._is_heading(line):
                handled_lines.append(line)
                prior_line = line
                continue

            # Ensure a header prior line is empty
            if prior_line is not None and not self.is_empty_line(line=prior_line):
                handled_lines.append("")

            handled_lines.append(line)

            if self.is_last_line(index=index, lines=lines):
                continue

            next_line = lines[index + 1]
            # Ensure a header next line is empty
            if not self.is_empty_line(line=next_line):
                handled_lines.append("")

        return self.lines_to_content(lines=handled_lines)

    def _is_heading(self, line: str) -> bool:
        return bool(self._HEADING_PATTERN.fullmatch(line))
