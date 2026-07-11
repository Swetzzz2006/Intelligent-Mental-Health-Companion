from utils.sentiment import predict_mood
from utils.emotion import detect_emotion
from utils.chatbot import chat
from utils.tips import show_tips
from utils.statistics import show_statistics
from datetime import datetime
import csv

print("=" * 50)
print("      Intelligent Mental Health Companion")
print("=" * 50)

while True:

    print("\nMain Menu")
    print("1. Analyze Mood")
    print("2. Chat with AI")
    print("3. Mental Health Tips")
    print("4. View Statistics")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\nMood Analysis Selected")

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

        mood_emoji = {
            "Happy": "😊",
            "Sad": "😔",
            "Anxious": "😟",
            "Neutral": "😐"
        }

        print("\nPrediction Result")
        print("-" * 30)
        print("Mood :", mood_emoji[mood], mood)
        print("Sentiment Score :", score)

        # Supportive response
        if mood == "Happy":
            print("\n😊 Keep smiling! Continue doing what makes you happy.")

        elif mood == "Sad":
            print("\n💙 Remember, difficult days don't last forever. Consider talking to someone you trust.")

        elif mood == "Anxious":
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
        input("\nPress Enter to return to the Main Menu...")


    elif choice == "2":
        chat()
        input("\nPress Enter to return to the Main Menu...")

    elif choice == "3":
        show_tips()
        input("\nPress Enter to return to the Main Menu...")

    elif choice == "4":
        show_statistics()
        input("\nPress Enter to return to the Main Menu...")

    elif choice == "5":
        print("\n👋 Thank you for using Intelligent Mental Health Companion.")
        break

    else:
        print("\n❌ Invalid choice. Please try again.")