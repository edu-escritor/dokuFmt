from pathlib import Path

DEFAULT_ENCODING = "utf-8"


class DokuWikiFile:
    def __init__(self, path: str | Path) -> None:
        file_path = Path(path)

        if ".txt" != file_path.suffix.lower():
            raise ValueError("A DokuWiki file must have a .txt extension.")

        self.path: Path = file_path
        self.content: str = self.path.read_text(encoding=DEFAULT_ENCODING)
        self._original_content: str = self.content

    def reset(self) -> None:
        self.content = self._original_content

    def has_changed(self) -> bool:
        return self.content != self._original_content

    def save(self) -> None:
        if not self.has_changed():
            return

        self.path.write_text(data=self.content, encoding=DEFAULT_ENCODING)
