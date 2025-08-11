import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": { "text": text_to_analyse } }   
    response = requests.post(url, json = payload, headers = headers)
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotions_data = response_dict['emotionPredictions'][0]['emotion']
        emotion_results = {'anger':emotions_data["anger"],
        'disgust':emotions_data["disgust"],
        'fear':emotions_data["fear"],
        'joy':emotions_data["joy"],
        'sadness':emotions_data["sadness"]}
        dominant_emotion = max(emotions_data, key=emotions_data.get)
    elif response.status_code == 400:
        emotion_results = {'anger':'None',
        'disgust':'None',
        'fear':'None',
        'joy':'None',
        'sadness':'None'}
        dominant_emotion = 'None'

    return {'anger':emotion_results["anger"],
    'disgust':emotion_results["disgust"],
    'fear':emotion_results["fear"],
    'joy':emotion_results["joy"],
    'sadness':emotion_results["sadness"],
    'dominant_emotion':dominant_emotion}
