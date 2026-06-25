from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Option:
    enabled: bool = True
    values: dict[str, Any] = field(default_factory=dict)
