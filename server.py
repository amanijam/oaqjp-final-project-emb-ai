from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detection(text_to_analyze)

    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return "For the given statement, the system response is 'anger': {}, \
            'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The \
            dominant emotion is {}.".format(str(res['anger']), str(res['disgust']), \
            str(res['fear']), str(res['joy']), str(res['sadness']), \
            res['dominant_emotion'])

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
