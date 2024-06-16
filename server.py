"""Executing this function initiates the application of emotion detection
   to be executed over the Flask channel and deployed on
   localhost:5000."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function."""

    text_to_analyze = request.args.get('textToAnalyze')
    emotion = emotion_detector(text_to_analyze)
    anger = emotion["anger"]
    disgust = emotion["disgust"]
    fear = emotion["fear"]
    joy = emotion["joy"]
    sadness = emotion["sadness"]
    dominant_emotion = emotion["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is 'anger': {anger}, \
    'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.\
    The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """Renders index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
