from utils.sentiment import predict_mood
from datetime import datetime
import csv

print("=" * 50)
print("      Intelligent Mental Health Companion")
print("=" * 50)

text = input("\nHow are you feeling today?\n> ")

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
date = datetime.now()

with open("data/mood_dataset.csv", mode="a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([date, mood, score])

print("\n✅ Mood data saved successfully.")