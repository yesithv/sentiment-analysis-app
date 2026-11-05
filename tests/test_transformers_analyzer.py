import unittest

from sentiment_analysis.implementations.transformers_analyzer import (
    TransformersSentimentAnalyzer,
)


class TestTransformersSentimentAnalyzer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analyzer = TransformersSentimentAnalyzer()

    def test_positive_sentiment(self):
        result = self.analyzer.analyze("I love working with Python")
        self.assertEqual(result.label, "POSITIVE")
        self.assertGreater(result.score, 0)

    def test_negative_sentiment(self):
        result = self.analyzer.analyze("I hate working with Python")
        self.assertEqual(result.label, "NEGATIVE")
        self.assertGreater(result.score, 0)


if __name__ == "__main__":
    unittest.main()
