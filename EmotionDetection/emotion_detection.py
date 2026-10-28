"""Detect emotions using the IBM Watson NLP emotion service."""

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyse):
    """Return five emotion scores and the dominant emotion; invalid input returns None."""
    empty_result = dict.fromkeys(EMOTIONS)
    empty_result["dominant_emotion"] = None
    if not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return empty_result

    response = requests.post(
        URL,
        json={"raw_document": {"text": text_to_analyse}},
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        timeout=20,
    )
    if response.status_code == 400:
        return empty_result
    response.raise_for_status()
    emotion_scores = response.json()["emotionPredictions"][0]["emotion"]
    result = {emotion: emotion_scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    return result
