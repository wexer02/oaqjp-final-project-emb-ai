"""Deploy the Emotion Detector using Flask. Check with: pylint server.py."""

import requests
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Display the supplied Emotion Detector interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detect():
    """Analyze text and display the scores or an invalid-input message."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    try:
        result = emotion_detector(text_to_analyze)
    except requests.RequestException:
        return "Emotion service unavailable. Please try again later.", 503

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
