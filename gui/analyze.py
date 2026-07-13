import customtkinter as ctk
from utils.emotion import detect_emotion
from utils.sentiment import predict_mood
from utils.session import get_user

from datetime import datetime
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt


def show_analyze(app):

    # Clear page
    for widget in app.main.winfo_children():
        widget.destroy()

    title = ctk.CTkLabel(
        app.main,
        text="😊 AI Mood Analysis",
        font=("Arial", 30, "bold")
    )
    title.pack(pady=20)

    textbox = ctk.CTkTextbox(
        app.main,
        width=700,
        height=180,
        font=("Arial", 16)
    )
    textbox.pack(pady=15)

    result = ctk.CTkTextbox(
        app.main,
        width=700,
        height=220,
        font=("Arial", 16)
    )
    result.pack(pady=20)

    def analyze():

        text = textbox.get("1.0", "end").strip()

        if text == "":
            result.delete("1.0", "end")
            result.insert("end", "Please enter how you are feeling.")
            return

        emotion, confidence, emoji, suggestion = detect_emotion(text)
        mood, score = predict_mood(text)

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ---------------- Current User ----------------

        username = get_user()

        if username is None:
            result.delete("1.0", "end")
            result.insert("end", "Please login first.")
            return

        # ---------------- User Folder ----------------

        user_folder = os.path.join("data", username)
        os.makedirs(user_folder, exist_ok=True)

        csv_file = os.path.join(user_folder, "mood_dataset.csv")

        # Create CSV if needed
        if not os.path.exists(csv_file):

            with open(csv_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerow([
                    "Date",
                    "Mood",
                    "Score",
                    "Emotion",
                    "Confidence"
                ])

        # ---------------- Save Mood ----------------

        with open(csv_file, "a", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                date,
                mood,
                score,
                emotion,
                round(confidence, 4)
            ])

        # ===================================================
        # Generate Graphs Automatically
        # ===================================================

        try:

            df = pd.read_csv(csv_file)

            output_folder = os.path.join(user_folder, "outputs")
            os.makedirs(output_folder, exist_ok=True)

            mood_counts = df["Mood"].value_counts()

            colors = {
                "Happy": "green",
                "Sad": "red",
                "Neutral": "blue",
                "Anxious": "orange"
            }

            bar_colors = [
                colors.get(m, "gray")
                for m in mood_counts.index
            ]

            # ---------------- Bar Chart ----------------

            plt.figure(figsize=(7, 5))

            bars = plt.bar(
                mood_counts.index,
                mood_counts.values,
                color=bar_colors
            )

            plt.title("Mood Frequency")
            plt.xlabel("Mood")
            plt.ylabel("Count")

            for bar in bars:

                h = bar.get_height()

                plt.text(
                    bar.get_x() + bar.get_width() / 2,
                    h + 0.05,
                    str(int(h)),
                    ha="center"
                )

            plt.tight_layout()

            plt.savefig(
                os.path.join(output_folder, "mood_bar_chart.png")
            )

            plt.close()

            # ---------------- Pie Chart ----------------

            plt.figure(figsize=(6, 6))

            plt.pie(
                mood_counts.values,
                labels=mood_counts.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=bar_colors
            )

            plt.title("Mood Distribution")

            plt.tight_layout()

            plt.savefig(
                os.path.join(output_folder, "mood_pie_chart.png")
            )

            plt.close()

        except Exception as e:
            print("Graph Error:", e)

        # ===================================================

        output = f"""
Emotion : {emoji} {emotion.capitalize()}

Confidence : {confidence*100:.2f} %

Mood : {mood}

Sentiment Score : {score}

Suggestion

{suggestion}

✅ Mood saved successfully.

📈 Graphs updated automatically.
"""

        result.delete("1.0", "end")
        result.insert("end", output)

    ctk.CTkButton(
        app.main,
        text="Analyze",
        width=220,
        height=45,
        command=analyze
    ).pack(pady=10)