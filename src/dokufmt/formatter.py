from pathlib import Path

from dokufmt.dokuwiki_file import DokuWikiFile
from dokufmt.rules.rule_factory import RuleFactory


class Formatter:
    def __init__(
        self, path: str | Path, rule_factory: RuleFactory | None = None
    ) -> None:
        self._file: DokuWikiFile = DokuWikiFile(path=path)
        self._rule_factory: RuleFactory = rule_factory or RuleFactory()

    def format(self) -> bool:
        for rule in self._rule_factory.all():
            self._file.content = rule.apply(content=self._file.content)

        changed = self._file.has_changed()

        self._file.save()

        return changed
