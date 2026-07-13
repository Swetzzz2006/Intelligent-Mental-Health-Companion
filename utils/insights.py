import pandas as pd
import os


def get_ai_insight(csv_file):

    if not os.path.exists(csv_file):
        return "Start analyzing your moods to receive AI insights."

    try:

        df = pd.read_csv(csv_file)

        if len(df) < 3:
            return "Keep logging your moods. More entries will improve AI insights."

        mood_counts = df["Mood"].value_counts()

        top = mood_counts.idxmax()

        if top.lower() == "happy":
            return "😊 Great job! Your recent mood trend is mostly positive. Keep maintaining healthy habits."

        elif top.lower() == "sad":
            return "💙 You've experienced sadness frequently. Consider talking to someone you trust or using the AI Chat."

        elif top.lower() == "anxious":
            return "😌 Your recent moods indicate anxiety. Try breathing exercises and mindfulness."

        elif top.lower() == "neutral":
            return "🌿 Your emotions are mostly balanced. Continue checking in with yourself."

        return "Continue tracking your moods regularly."

    except:
        return "Unable to generate AI insights."