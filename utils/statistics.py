import pandas as pd


def show_statistics():

    try:
        df = pd.read_csv("data/mood_dataset.csv")

        print("\n📊 Your Mental Health Statistics")
        print("=" * 45)

        print(f"Total Entries : {len(df)}")

        # Most common mood
        common_mood = df["Mood"].mode()[0]
        print(f"Most Common Mood : {common_mood}")

        # Average sentiment score
        avg_score = df["Score"].mean()
        print(f"Average Sentiment Score : {avg_score:.2f}")

        # Most common emotion
        if "Emotion" in df.columns:
            common_emotion = df["Emotion"].mode()[0]
            print(f"Most Common Emotion : {common_emotion}")

        print("=" * 45)

    except Exception as e:
        print("❌ Unable to load statistics.")
        print(e)