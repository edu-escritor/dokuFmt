from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CliOptions:
    path: Path
