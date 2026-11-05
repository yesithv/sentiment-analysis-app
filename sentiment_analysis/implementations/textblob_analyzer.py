from textblob import TextBlob
from sentiment_analysis.analyzer import SentimentAnalyzer
from sentiment_analysis.result import SentimentResult


class TextBlobSentimentAnalyzer(SentimentAnalyzer):
    def analyze(self, text: str) -> SentimentResult:
        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0:
            label = "POSITIVE"
        elif polarity < 0:
            label = "NEGATIVE"
        else:
            label = "NEUTRAL"

        return SentimentResult(
            label=label,
            score=round(abs(polarity), 2)
        )
