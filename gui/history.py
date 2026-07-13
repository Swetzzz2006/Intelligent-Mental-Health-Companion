import customtkinter as ctk
import pandas as pd
import os

from utils.session import get_user


def show_history(app):

    # ---------------- Clear Page ----------------

    for widget in app.main.winfo_children():
        widget.destroy()

    # ---------------- Current User ----------------

    username = get_user()

    if username is None:
        username = "User"

    csv_file = os.path.join("data", username, "mood_dataset.csv")

    # ---------------- Title ----------------

    ctk.CTkLabel(
        app.main,
        text="📖 Mood History",
        font=("Arial", 30, "bold")
    ).pack(pady=(20, 5))

    ctk.CTkLabel(
        app.main,
        text=f"Logged in as: {username}",
        font=("Arial", 15),
        text_color="gray"
    ).pack()

    ctk.CTkLabel(
        app.main,
        text="View all your previous mood analyses",
        font=("Arial", 15),
        text_color="gray"
    ).pack(pady=(0, 20))

    # ---------------- Table ----------------

    table = ctk.CTkScrollableFrame(
        app.main,
        width=950,
        height=520
    )

    table.pack(fill="both", expand=True, padx=20, pady=10)

    try:

        df = pd.read_csv(csv_file)

        headers = [
            "Date",
            "Mood",
            "Emotion",
            "Confidence"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                table,
                text=header,
                font=("Arial", 15, "bold"),
                width=220
            ).grid(row=0, column=col, padx=10, pady=10)

        # Show newest entries first
        df = df.iloc[::-1].reset_index(drop=True)

        for row in range(len(df)):

            ctk.CTkLabel(
                table,
                text=str(df.iloc[row]["Date"]),
                width=220
            ).grid(row=row + 1, column=0, padx=10, pady=5)

            ctk.CTkLabel(
                table,
                text=str(df.iloc[row]["Mood"]),
                width=120
            ).grid(row=row + 1, column=1, padx=10, pady=5)

            ctk.CTkLabel(
                table,
                text=str(df.iloc[row]["Emotion"]).capitalize(),
                width=120
            ).grid(row=row + 1, column=2, padx=10, pady=5)

            confidence = float(df.iloc[row]["Confidence"]) * 100

            ctk.CTkLabel(
                table,
                text=f"{confidence:.1f}%",
                width=120
            ).grid(row=row + 1, column=3, padx=10, pady=5)

    except Exception:

        ctk.CTkLabel(
            table,
            text="No mood history found.",
            font=("Arial", 18)
        ).pack(pady=40)

        ctk.CTkLabel(
            table,
            text="Start by analyzing your mood!",
            font=("Arial", 15),
            text_color="gray"
        ).pack()