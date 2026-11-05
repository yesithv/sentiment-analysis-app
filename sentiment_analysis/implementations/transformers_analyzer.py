from transformers import pipeline

from sentiment_analysis.analyzer import SentimentAnalyzer
from sentiment_analysis.result import SentimentResult


class TransformersSentimentAnalyzer(SentimentAnalyzer):

    MODEL_NAME = (
        "distilbert/"
        "distilbert-base-uncased-finetuned-sst-2-english"
    )

    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis",
            model=self.MODEL_NAME
        )

    def analyze(self, text: str) -> SentimentResult:
        result = self.classifier(text)[0]

        return SentimentResult(
            label=result["label"],
            score=round(result["score"], 2)
        )