import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers = headers, json = json_obj)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }

    response_json = json.loads(response.text)
    response_formatted = response_json.get('emotionPredictions')[0].get('emotion')
    response_formatted['dominant_emotion'] = max(response_formatted, key=response_formatted.get)
    return response_formatted
    