from transformers import pipeline

emotion_classifier = pipeline(
    task="text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

emotion_data = {
    "joy": {
        "emoji": "😊",
        "message": "Keep doing what makes you happy!"
    },
    "sadness": {
        "emoji": "😢",
        "message": "Remember, difficult days don't last forever. Consider talking to someone you trust."
    },
    "fear": {
        "emoji": "😨",
        "message": "It's okay to feel nervous sometimes. Take a few deep breaths and focus on one step at a time."
    },
    "anger": {
        "emoji": "😠",
        "message": "Take a short break before reacting. Calmness helps in making better decisions."
    },
    "love": {
        "emoji": "❤️",
        "message": "Cherish the positive relationships in your life."
    },
    "surprise": {
        "emoji": "😲",
        "message": "Unexpected moments can become valuable learning experiences."
    }
}

def detect_emotion(text):
    result = emotion_classifier(text)

    emotion = result[0][0]["label"]
    confidence = result[0][0]["score"]

    emoji = emotion_data[emotion]["emoji"]
    suggestion = emotion_data[emotion]["message"]

    return emotion, confidence, emoji, suggestion