from flask import Flask, request,render_template
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotion scores from the response text
    score_data = json.loads(response.text)
    anger_score = score_data.get('anger')
    disgust_score = score_data.get('disgust')
    fear_score = score_data.get('fear')
    joy_score = score_data.get('joy')
    sadness_score = score_data.get('sadness')
    dominant_emotion = score_data.get('dominant_emotion')
  
    # return scores and dominant_emotion
    return f"For the given statement, the system response is 'anger': {anger_score},\
    'disgust': {disgust_score},\
    'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}.\
    The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
