from dataclasses import dataclass
from typing import Optional


@dataclass
class FontParams:
    font_name: Optional[str]
    font_size: int
