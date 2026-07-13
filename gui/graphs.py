import os
import customtkinter as ctk
from PIL import Image

from utils.session import get_user


def show_graphs(app):

    # ---------------- Clear Page ----------------

    for widget in app.main.winfo_children():
        widget.destroy()

    username = get_user()

    if username is None:
        username = "User"

    output_folder = os.path.join("data", username, "outputs")

    bar_path = os.path.join(output_folder, "mood_bar_chart.png")
    pie_path = os.path.join(output_folder, "mood_pie_chart.png")

    # ---------------- Title ----------------

    ctk.CTkLabel(
        app.main,
        text="📈 Mood Analytics Dashboard",
        font=("Arial", 30, "bold")
    ).pack(pady=(20, 5))

    ctk.CTkLabel(
        app.main,
        text=f"Graphs for {username}",
        font=("Arial", 16),
        text_color="gray"
    ).pack(pady=(0, 20))

    try:

        bar_image = ctk.CTkImage(
            light_image=Image.open(bar_path),
            dark_image=Image.open(bar_path),
            size=(480, 300)
        )

        pie_image = ctk.CTkImage(
            light_image=Image.open(pie_path),
            dark_image=Image.open(pie_path),
            size=(320, 320)
        )

        graph_frame = ctk.CTkFrame(app.main)
        graph_frame.pack(pady=10, padx=20, fill="both", expand=True)

        left = ctk.CTkFrame(graph_frame)
        left.grid(row=0, column=0, padx=15, pady=15)

        ctk.CTkLabel(
            left,
            text="📊 Mood Frequency",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        ctk.CTkLabel(
            left,
            image=bar_image,
            text=""
        ).pack(padx=10, pady=10)

        right = ctk.CTkFrame(graph_frame)
        right.grid(row=0, column=1, padx=15, pady=15)

        ctk.CTkLabel(
            right,
            text="🥧 Mood Distribution",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        ctk.CTkLabel(
            right,
            image=pie_image,
            text=""
        ).pack(padx=10, pady=10)

        ctk.CTkLabel(
            app.main,
            text="💡 Tip: Track your moods regularly to discover emotional patterns.",
            font=("Arial", 14),
            wraplength=800
        ).pack(pady=15)

        ctk.CTkButton(
            app.main,
            text="🔄 Refresh",
            width=180,
            command=lambda: show_graphs(app)
        ).pack(pady=(0, 20))

    except Exception:

        ctk.CTkLabel(
            app.main,
            text="⚠️ No graphs found for this user.",
            font=("Arial", 22)
        ).pack(pady=80)

        ctk.CTkLabel(
            app.main,
            text="Analyze some moods and generate graphs first.",
            font=("Arial", 16)
        ).pack()