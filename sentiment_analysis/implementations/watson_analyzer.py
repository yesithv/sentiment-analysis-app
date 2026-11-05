import requests

from sentiment_analysis.analyzer import SentimentAnalyzer
from sentiment_analysis.result import SentimentResult


class WatsonSentimentAnalyzer(SentimentAnalyzer):
    API_URL = (
        "https://sn-watson-sentiment-bert.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    )

    MODEL_ID = "sentiment_aggregated-bert-workflow_lang_multi_stock"

    def analyze(self, text: str) -> SentimentResult:
        payload = {
            "raw_document": {
                "text": text
            }
        }

        headers = {
            "grpc-metadata-mm-model-id": self.MODEL_ID
        }

        response = requests.post(
            self.API_URL,
            json=payload,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()
        sentiment = data["documentSentiment"]

        return SentimentResult(
            label=sentiment["label"],
            score=round(sentiment["score"], 2)
        )
