import json
from flask import Flask, request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion():  
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response_dict = emotion_detector(text_to_analyze)
    # Extract the emotion scores from the response
    anger_score = response_dict.get('anger')
    disgust_score = response_dict.get('disgust')
    fear_score = response_dict.get('fear')
    joy_score = response_dict.get('joy')
    sadness_score = response_dict.get('sadness')
    dominant_emotion = response_dict.get('dominant_emotion')
    # return formatted data
    return f"For the given statement, the system response is 'anger': {anger_score},\
    'disgust': {disgust_score},\
    'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}.\
    The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
