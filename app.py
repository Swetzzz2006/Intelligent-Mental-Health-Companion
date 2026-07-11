from utils.sentiment import predict_mood
from datetime import datetime
import csv
from utils.emotion import detect_emotion

print("=" * 50)
print("      Intelligent Mental Health Companion")
print("=" * 50)

text = input("\nHow are you feeling today?\n> ")
emotion, confidence, emoji, suggestion = detect_emotion(text)

print("\nEmotion Detected")
print("-" * 30)
print(f"Emotion    : {emoji} {emotion.capitalize()}")
print(f"Confidence : {confidence*100:.2f}%")

print("\nSuggestion")
print("-" * 30)
print(suggestion)

mood, score = predict_mood(text)
emoji = {
    "Happy": "😊",
    "Sad": "😔",
    "Anxious": "😟",
    "Neutral": "😐"
}
print("\nPrediction Result")
print("-" * 30)
print("Mood :", emoji[mood], mood)
print("Sentiment Score :", score)

# Supportive response
if "Happy" in mood:
    print("\n😊 Keep smiling! Continue doing what makes you happy.")

elif "Sad" in mood:
    print("\n💙 Remember, difficult days don't last forever. Consider talking to someone you trust.")

elif "Anxious" in mood:
    print("\n🌿 Try taking a few deep breaths or a short walk. Small breaks can help.")

else:
    print("\n😌 You seem calm today. Wishing you a wonderful day!")

# Save data to CSV
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/mood_dataset.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        date,
        mood,
        score,
        emotion,
        round(confidence, 4)
    ])

print("\n✅ Mood and Emotion data saved successfully.")