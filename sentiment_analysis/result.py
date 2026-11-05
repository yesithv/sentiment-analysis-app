from dataclasses import dataclass


@dataclass(frozen=True)
class SentimentResult:
    label: str
    score: float
