import customtkinter as ctk
from datetime import datetime
import pandas as pd
import os

from gui.analyze import show_analyze
from gui.chatbot_page import show_chat
from gui.statistics import show_statistics

from utils.session import get_user
from utils.streak import calculate_streak
from utils.insights import get_ai_insight


def clear_page(app):
    for widget in app.main.winfo_children():
        widget.destroy()


def create_card(parent, title, value, color):

    card = ctk.CTkFrame(
        parent,
        width=200,
        height=140,
        corner_radius=15
    )

    card.pack_propagate(False)

    ctk.CTkLabel(
        card,
        text=title,
        font=("Arial", 17, "bold"),
        text_color=color
    ).pack(pady=(20, 5))

    ctk.CTkLabel(
        card,
        text=str(value),
        font=("Arial", 26, "bold")
    ).pack()

    return card

def show_dashboard(app):

    clear_page(app)

    # ---------------- Logged-in User ----------------

    username = get_user()

    if username is None:
        username = "User"

    # ---------------- User CSV ----------------

    user_folder = os.path.join("data", username)
    csv_file = os.path.join(user_folder, "mood_dataset.csv")

    # ---------------- Read Data ----------------

    try:

        df = pd.read_csv(csv_file)

        latest_mood = df.iloc[-1]["Mood"]
        latest_emotion = df.iloc[-1]["Emotion"]
        total = len(df)

    except Exception:

        latest_mood = "--"
        latest_emotion = "--"
        total = 0

    # ---------------- Mood Streak ----------------

    streak = calculate_streak(csv_file)

    # ---------------- AI Insight ----------------

    insight = get_ai_insight(csv_file)

    # ---------------- Welcome ----------------

    ctk.CTkLabel(
        app.main,
        text=f"👋 Welcome, {username}!",
        font=("Arial", 34, "bold")
    ).pack(pady=(20, 5))

    today = datetime.now().strftime("%d %B %Y")

    ctk.CTkLabel(
        app.main,
        text=f"📅 Today: {today}",
        font=("Arial", 15),
        text_color="gray"
    ).pack(pady=(0, 5))

    ctk.CTkLabel(
        app.main,
        text="Your Intelligent Mental Health Companion",
        font=("Arial", 18)
    ).pack()

    # ---------------- Cards ----------------

    cards = ctk.CTkFrame(app.main, fg_color="transparent")
    cards.pack(pady=30)

    create_card(
        cards,
        "😊 Latest Mood",
        latest_mood,
        "#4CAF50"
    ).grid(row=0, column=0, padx=12)

    create_card(
        cards,
        "❤️ Last Emotion",
        str(latest_emotion).capitalize(),
        "#FF6B6B"
    ).grid(row=0, column=1, padx=12)

    create_card(
        cards,
        "📊 Total Analyses",
        total,
        "#4DA6FF"
    ).grid(row=0, column=2, padx=12)

    create_card(
        cards,
        "🔥 Mood Streak",
        f"{streak} Days",
        "#FF9800"
    ).grid(row=0, column=3, padx=12)

    # ---------------- Wellness Progress ----------------

    progress_frame = ctk.CTkFrame(app.main)
    progress_frame.pack(fill="x", padx=20, pady=15)

    ctk.CTkLabel(
        progress_frame,
        text="🌱 Wellness Progress",
        font=("Arial", 18, "bold")
    ).pack(pady=(15, 5))

    progress = ctk.CTkProgressBar(
        progress_frame,
        width=500
    )
    progress.pack(pady=10)

    if total == 0:

        progress.set(0)
        progress_text = "Start your first mood analysis!"

    else:

        positive = len(df[df["Score"] >= 0])

        percentage = positive / total

        progress.set(percentage)

        progress_text = f"{int(percentage * 100)}% Positive Mood"

    ctk.CTkLabel(
        progress_frame,
        text=progress_text,
        font=("Arial", 14)
    ).pack(pady=(0, 15))

    # ---------------- AI Insights ----------------

    insight_frame = ctk.CTkFrame(app.main)
    insight_frame.pack(fill="x", padx=20, pady=15)

    ctk.CTkLabel(
        insight_frame,
        text="🧠 AI Insights",
        font=("Arial", 20, "bold")
    ).pack(pady=(15, 10))

    ctk.CTkLabel(
        insight_frame,
        text=insight,
        font=("Arial", 16),
        wraplength=850,
        justify="left"
    ).pack(padx=20, pady=(0, 20))

    # ---------------- AI Assistant ----------------

    ai_frame = ctk.CTkFrame(app.main, corner_radius=15)
    ai_frame.pack(fill="x", padx=20, pady=15)

    ctk.CTkLabel(
        ai_frame,
        text="🤖 AI Assistant",
        font=("Arial", 22, "bold")
    ).pack(pady=(20, 10))

    ctk.CTkLabel(
        ai_frame,
        text="Status : Ready ✅",
        font=("Arial", 16)
    ).pack()

    ctk.CTkLabel(
        ai_frame,
        text="Analyze your mood, chat with AI, and track your emotional well-being.",
        font=("Arial", 15),
        wraplength=800
    ).pack(pady=(10, 20))

    # ---------------- Daily Motivation ----------------

    quote = ctk.CTkFrame(app.main)
    quote.pack(fill="x", padx=20, pady=15)

    ctk.CTkLabel(
        quote,
        text="🌿 Daily Motivation",
        font=("Arial", 20, "bold")
    ).pack(pady=(15, 10))

    ctk.CTkLabel(
        quote,
        text='"Small steps every day lead to big changes."',
        font=("Arial", 16),
        wraplength=700
    ).pack(pady=(0, 20))

    # ---------------- Quick Actions ----------------

    actions = ctk.CTkFrame(app.main)
    actions.pack(pady=20)

    ctk.CTkButton(
        actions,
        text="😊 Analyze Mood",
        width=170,
        command=lambda: show_analyze(app)
    ).grid(row=0, column=0, padx=10)

    ctk.CTkButton(
        actions,
        text="🤖 AI Chat",
        width=170,
        command=lambda: show_chat(app)
    ).grid(row=0, column=1, padx=10)

    ctk.CTkButton(
        actions,
        text="📊 Statistics",
        width=170,
        command=lambda: show_statistics(app)
    ).grid(row=0, column=2, padx=10)

    # ---------------- Footer ----------------

    ctk.CTkLabel(
        app.main,
        text="💙 Take care of your mind. Every feeling matters.",
        font=("Arial", 14)
    ).pack(pady=20)