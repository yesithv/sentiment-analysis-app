# Commands:
# pip install textblob
# from sentimental_process import sentiment_analyzer
# sentiment_analyzer("I love this technology")

from textblob import TextBlob

def sentiment_analyzer(text_to_analyze):

    polarity = TextBlob(text_to_analyze).sentiment.polarity

    if polarity > 0:
        label = "POSITIVE"
    elif polarity < 0:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"

    return {
        "label": label,
        "score": round(abs(polarity), 2)
    }