import customtkinter as ctk
import pandas as pd
import os
from utils.session import get_user


def show_profile(app):

    for widget in app.main.winfo_children():
        widget.destroy()

    username = get_user()

    # Correct file path
    filename = f"data/{username}/mood_dataset.csv"

    total = 0
    common_mood = "--"
    common_emotion = "--"

    if os.path.exists(filename):

        try:
            df = pd.read_csv(filename)

            total = len(df)

            if total > 0:
                common_mood = df["Mood"].mode()[0]
                common_emotion = df["Emotion"].mode()[0].capitalize()

        except Exception as e:
            print(e)

    ctk.CTkLabel(
        app.main,
        text="👤 My Profile",
        font=("Arial", 32, "bold")
    ).pack(pady=20)

    profile = ctk.CTkFrame(app.main, width=700, height=420)
    profile.pack(pady=20)
    profile.pack_propagate(False)

    ctk.CTkLabel(
        profile,
        text="👤",
        font=("Arial", 80)
    ).pack(pady=15)

    ctk.CTkLabel(
        profile,
        text=f"Username : {username}",
        font=("Arial", 20, "bold")
    ).pack(pady=8)

    ctk.CTkLabel(
        profile,
        text=f"Total Analyses : {total}",
        font=("Arial", 18)
    ).pack(pady=8)

    ctk.CTkLabel(
        profile,
        text=f"Most Common Mood : {common_mood}",
        font=("Arial", 18)
    ).pack(pady=8)

    ctk.CTkLabel(
        profile,
        text=f"Most Common Emotion : {common_emotion}",
        font=("Arial", 18)
    ).pack(pady=8)

    ctk.CTkLabel(
        profile,
        text="💙 Keep tracking your emotions every day!",
        font=("Arial", 16)
    ).pack(pady=25)