import requests
import json

def emotion_detector(text_to_analyze):	
	# Emotion Detection API url
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Request payload with the text to analyze
    payload = { "raw_document": { "text": text_to_analyze } }
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # POST request to the API with the payload and headers
    response = requests.post(url, json=payload, headers=header)
    
    # Parse the response from the API
    formatted_response = json.loads(response.text)
    emotions_list = formatted_response['emotionPredictions'][0]['emotion'] 

    # emotion scores
    anger_score = emotions_list['anger']
    disgust_score = emotions_list['disgust']
    fear_score = emotions_list['fear']
    joy_score = emotions_list['joy']
    sadness_score = emotions_list['sadness']
    # get dominant emotion using max function
    dominant_emotion = max(emotions_list, key=emotions_list.get)

    return f"{{ 'anger' : {anger_score},'disgust' : {disgust_score},\
    'fear' : {fear_score},'joy' : {joy_score}, 'sadness' : {sadness_score},\
    'dominant_emotion':'{dominant_emotion}'}}"