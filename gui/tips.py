import customtkinter as ctk
import random


tips = [

    "🌿 Take a 10-minute walk every day.",

    "💧 Drink enough water.",

    "😴 Aim for 7–8 hours of sleep.",

    "📚 Focus on one task at a time.",

    "🧘 Practice deep breathing for 5 minutes.",

    "😊 Talk to someone you trust.",

    "🎵 Listen to your favorite music.",

    "📵 Take a break from social media.",

    "❤️ Celebrate your small achievements.",

    "🌞 Spend some time outdoors."

]


def show_tips(app):

    for widget in app.main.winfo_children():
        widget.destroy()

    ctk.CTkLabel(
        app.main,
        text="🌿 Mental Health Tips",
        font=("Arial",30,"bold")
    ).pack(pady=20)

    tip = random.choice(tips)

    box = ctk.CTkTextbox(
        app.main,
        width=700,
        height=250,
        font=("Arial",18)
    )

    box.pack(pady=30)

    box.insert("end", tip)