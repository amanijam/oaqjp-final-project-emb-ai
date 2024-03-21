"""
This file initiates the Flask application of emotion detection to be 
    executed over the Flask channel and deployed on localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function calls the emotion_detection function with the given
        text as 'textToAnalyze'.

    Returns:
    str: text that provides emotion scores and dominant emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detection(text_to_analyze)

    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    output = (
        f"For the given statement, the system response is 'anger': "
        f"{str(res['anger'])}, 'disgust': {str(res['disgust'])}, 'fear': "
        f"{str(res['fear'])}, 'joy': {str(res['joy'])} and 'sadness': "
        f"{str(res['sadness'])}. The dominant emotion is {res['dominant_emotion']}."
    )
    return output

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application page over
        the Flask channel.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
