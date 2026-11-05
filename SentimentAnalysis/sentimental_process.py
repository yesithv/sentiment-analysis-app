# Commands
# Alternativa:
# pip install transformers torch
# python
# Installl certificates: pip install python-certifi-win32
# from sentiment_process import

from transformers import pipeline

classifier = pipeline("sentiment-analysis")
def sentiment_analyzer(text_to_analyze):
    result = classifier(text_to_analyze)[0]
    return {
        "label": result["label"],
        "score": result["score"]
    }