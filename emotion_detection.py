import requests

def emotion_detector(text_to_analyze):	
	# Emotion Detection API url
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Request payload with the text to analyze
    payload = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # POST request to the API with the payload and headers
    response = requests.post(url, json=payload, headers=header)

    # return the response from the API
    return response.text