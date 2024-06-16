import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotions = {}
        emotions['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
        emotions['disgust'] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        emotions['fear'] = formatted_response['emotionPredictions'][0]['emotion']['fear']
        emotions['joy'] = formatted_response['emotionPredictions'][0]['emotion']['joy']
        emotions['sadness'] = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        for emotion in emotions:
            if emotions[emotion] == max(emotions.values()):
                dominant_emotion = emotion     
        emotions['dominant_emotion'] = dominant_emotion
        return(emotions)

    elif response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    