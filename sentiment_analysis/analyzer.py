from abc import ABC, abstractmethod
from sentiment_analysis.result import SentimentResult


class SentimentAnalyzer(ABC):
    @abstractmethod
    def analyze(self, text: str) -> SentimentResult:
        """Analyze the sentiment of the provided text."""
        raise NotImplementedError
