from dataclasses import dataclass


@dataclass
class CardParams:
    color: str
    value: str
    suit: str
