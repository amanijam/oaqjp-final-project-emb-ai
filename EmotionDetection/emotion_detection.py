import requests
import json

def emotion_detection(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        out = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, \
                 'sadness': None, 'dominant_emotion': None}

    else:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        out = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, \
                'joy': joy_score, 'sadness': sadness_score}

        dominant = max(out, key=lambda k: out[k])
        out['dominant_emotion'] = dominant

    return out