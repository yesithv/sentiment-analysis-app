async function RunSentimentAnalysis() {
    const textArea = document.getElementById("textToAnalyze");
    const analyzeButton = document.getElementById("analyzeButton");

    const resultContainer = document.getElementById("resultContainer");
    const sentimentResult = document.getElementById("sentimentResult");
    const confidenceResult = document.getElementById("confidenceResult");

    const textToAnalyze = textArea.value.trim();

    if (!textToAnalyze) {
        showError("Please enter some text to analyze.");
        return;
    }

    analyzeButton.disabled = true;
    analyzeButton.textContent = "Analyzing...";

    try {
        const response = await fetch(
            `/sentimentAnalyzer?textToAnalyze=${encodeURIComponent(textToAnalyze)}`
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Unable to analyze the text.");
        }

        const confidence = Math.round(data.score * 100);

        sentimentResult.textContent = data.label;
        confidenceResult.textContent = `${confidence}%`;

        sentimentResult.classList.remove(
            "positive",
            "negative",
            "neutral"
        );

        sentimentResult.classList.add(
            data.label.toLowerCase()
        );

        resultContainer.classList.remove("hidden");

    } catch (error) {
        showError(error.message);
    } finally {
        analyzeButton.disabled = false;
        analyzeButton.textContent = "Analyze Sentiment";
    }
}


function showError(message) {
    const resultContainer = document.getElementById("resultContainer");
    const sentimentResult = document.getElementById("sentimentResult");
    const confidenceResult = document.getElementById("confidenceResult");

    sentimentResult.textContent = "ERROR";
    sentimentResult.className = "sentiment-result error";

    confidenceResult.textContent = message;

    resultContainer.classList.remove("hidden");
}