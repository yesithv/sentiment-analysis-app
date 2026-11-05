import unittest

from sentiment_analysis.implementations.textblob_analyzer import (TextBlobSentimentAnalyzer, )


class TestTextBlobSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = TextBlobSentimentAnalyzer()

    def test_positive_sentiment(self):
        result = self.analyzer.analyze("I love working with python")
        self.assertEqual(result.label, "POSITIVE")
        self.assertGreater(result.score, 0)

    def test_negative_sentiment(self):
        result = self.analyzer.analyze("I hate working with python")
        self.assertEqual(result.label, "NEGATIVE")
        self.assertGreater(result.score, 0)

    def test_neutral_sentiment(self):
        result = self.analyzer.analyze("Python is a programming languaje")
        self.assertEqual(result.label, "NEUTRAL")
        self.assertEqual(result.score, 0)


if __name__ == "main":
    unittest.main()
