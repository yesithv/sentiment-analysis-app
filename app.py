''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Commands:
#  python server.py


from flask import Flask, render_template, request
from sentiment_analysis.analyzer import SentimentAnalyzer
from sentiment_analysis.implementations.transformers_analyzer import (
    TransformersSentimentAnalyzer,
)


app = Flask("Sentiment Analyzer")
analyzer: SentimentAnalyzer = TransformersSentimentAnalyzer()


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid input! Try again."

    # Pass the text to the sentiment_analyzer function and store the response
    result = analyzer.analyze(text_to_analyze)

    # Extract the label and score from the response
    label = result.label
    score = result.score

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        # return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
        return f"The given text has been identified as {label} with a score of {score}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__": app.run(host="0.0.0.0", port=5000)
