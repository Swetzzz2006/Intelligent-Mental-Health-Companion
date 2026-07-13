import customtkinter as ctk
import pandas as pd
import os

from utils.session import get_user


def show_statistics(app):

    # ---------------- Clear Page ----------------

    for widget in app.main.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        app.main,
        text="📊 Mood Statistics",
        font=("Arial", 32, "bold")
    ).pack(pady=20)

    # ---------------- Current User ----------------

    username = get_user()

    if username is None:
        username = "User"

    csv_file = os.path.join("data", username, "mood_dataset.csv")

    # ---------------- Read User Data ----------------

    try:

        df = pd.read_csv(csv_file)

        total = len(df)
        latest_mood = df.iloc[-1]["Mood"]
        latest_emotion = df.iloc[-1]["Emotion"]
        average = df["Confidence"].mean() * 100

        # Most common mood
        most_common_mood = df["Mood"].mode()[0]

        # Most common emotion
        most_common_emotion = df["Emotion"].mode()[0]

    except Exception:

        total = 0
        latest_mood = "--"
        latest_emotion = "--"
        average = 0
        most_common_mood = "--"
        most_common_emotion = "--"

    # ---------------- Cards ----------------

    cards = ctk.CTkFrame(app.main)
    cards.pack(pady=20)

    def create_card(parent, title, value):

        frame = ctk.CTkFrame(
            parent,
            width=190,
            height=140,
            corner_radius=15
        )

        frame.pack(side="left", padx=12)
        frame.pack_propagate(False)

        ctk.CTkLabel(
            frame,
            text=title,
            font=("Arial", 17, "bold")
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            frame,
            text=str(value),
            font=("Arial", 24, "bold")
        ).pack()

    create_card(cards, "😊 Latest Mood", latest_mood)
    create_card(cards, "❤️ Latest Emotion", latest_emotion)
    create_card(cards, "📊 Total Analyses", total)
    create_card(cards, "🎯 Avg Confidence", f"{average:.1f}%")

    # ---------------- Summary ----------------

    summary = ctk.CTkFrame(app.main)
    summary.pack(fill="x", padx=30, pady=25)

    ctk.CTkLabel(
        summary,
        text="📋 Summary",
        font=("Arial", 22, "bold")
    ).pack(pady=(15, 10))

    ctk.CTkLabel(
        summary,
        text=f"👤 User : {username}",
        font=("Arial", 16)
    ).pack(pady=3)

    ctk.CTkLabel(
        summary,
        text=f"😊 Most Common Mood : {most_common_mood}",
        font=("Arial", 16)
    ).pack(pady=3)

    ctk.CTkLabel(
        summary,
        text=f"❤️ Most Common Emotion : {most_common_emotion}",
        font=("Arial", 16)
    ).pack(pady=3)

    ctk.CTkLabel(
        summary,
        text=f"📝 Total Mood Analyses : {total}",
        font=("Arial", 16)
    ).pack(pady=(3, 15))