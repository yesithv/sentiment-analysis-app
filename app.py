''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Commands:
#  python server.py


from flask import Flask, jsonify, render_template, request
from sentiment_analysis.analyzer import SentimentAnalyzer
from sentiment_analysis.implementations.transformers_analyzer import TransformersSentimentAnalyzer
from sentiment_analysis.implementations.textblob_analyzer import TextBlobSentimentAnalyzer

app = Flask("Sentiment Analyzer")
# analyzer: SentimentAnalyzer = TextBlobSentimentAnalyzer()
analyzer: SentimentAnalyzer = TransformersSentimentAnalyzer()


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return jsonify({
            "error": "Please enter some text to analyze."
        }), 400

    result = analyzer.analyze(text_to_analyze)

    return jsonify({
        "label": result.label,
        "score": result.score
    })


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__": app.run(host="0.0.0.0", port=5000)
