import customtkinter as ctk
from datetime import datetime
from utils.chatbot import chat_response


def show_chat(app):

    # ---------------- Clear Page ----------------

    for widget in app.main.winfo_children():
        widget.destroy()

    # ---------------- Header ----------------

    header = ctk.CTkFrame(app.main, corner_radius=15)
    header.pack(fill="x", padx=20, pady=(15, 10))

    ctk.CTkLabel(
        header,
        text="🤖 AI Mental Health Companion",
        font=("Arial", 28, "bold")
    ).pack(pady=(15, 5))

    ctk.CTkLabel(
        header,
        text="I'm here to listen and support you.",
        font=("Arial", 15),
        text_color="gray"
    ).pack(pady=(0, 15))

    # ---------------- Chat Area ----------------

    chat_box = ctk.CTkScrollableFrame(
        app.main,
        width=900,
        height=470,
        corner_radius=15
    )

    chat_box.pack(fill="both", expand=True, padx=20)

    # ---------------- Welcome Message ----------------

    welcome = ctk.CTkFrame(chat_box, fg_color="#2B2B2B", corner_radius=15)
    welcome.pack(anchor="w", padx=10, pady=10)

    ctk.CTkLabel(
        welcome,
        text="🤖 Hello! 👋",
        font=("Arial", 16, "bold")
    ).pack(anchor="w", padx=15, pady=(10, 5))

    ctk.CTkLabel(
        welcome,
        text="How are you feeling today?\nI'm always here to listen.",
        justify="left",
        wraplength=450,
        font=("Arial", 14)
    ).pack(anchor="w", padx=15, pady=(0, 10))

    # ---------------- Bottom ----------------

    bottom = ctk.CTkFrame(app.main)
    bottom.pack(fill="x", padx=20, pady=15)

    entry = ctk.CTkEntry(
        bottom,
        placeholder_text="Type your message here...",
        height=45,
        font=("Arial", 14)
    )

    entry.pack(side="left", fill="x", expand=True, padx=(10, 10), pady=10)

    def send():

        message = entry.get().strip()

        if message == "":
            return

        time = datetime.now().strftime("%H:%M")

        # ---------------- User Bubble ----------------

        user_frame = ctk.CTkFrame(
            chat_box,
            fg_color="#1F6AA5",
            corner_radius=15
        )

        user_frame.pack(anchor="e", padx=10, pady=6)

        ctk.CTkLabel(
            user_frame,
            text=message,
            wraplength=450,
            justify="left",
            font=("Arial", 14)
        ).pack(anchor="e", padx=15, pady=(10, 5))

        ctk.CTkLabel(
            user_frame,
            text=time,
            font=("Arial", 10),
            text_color="lightgray"
        ).pack(anchor="e", padx=15, pady=(0, 8))

        # ---------------- AI Reply ----------------

        reply = chat_response(message)

        bot_frame = ctk.CTkFrame(
            chat_box,
            fg_color="#2B2B2B",
            corner_radius=15
        )

        bot_frame.pack(anchor="w", padx=10, pady=6)

        ctk.CTkLabel(
            bot_frame,
            text="🤖 AI Companion",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=15, pady=(10, 5))

        ctk.CTkLabel(
            bot_frame,
            text=reply,
            wraplength=500,
            justify="left",
            font=("Arial", 14)
        ).pack(anchor="w", padx=15)

        ctk.CTkLabel(
            bot_frame,
            text=time,
            font=("Arial", 10),
            text_color="gray"
        ).pack(anchor="w", padx=15, pady=(5, 10))

        entry.delete(0, "end")

        # Scroll to bottom
        app.update_idletasks()

    # ---------------- Send Button ----------------

    send_btn = ctk.CTkButton(
        bottom,
        text="📤 Send",
        width=120,
        height=45,
        command=send
    )

    send_btn.pack(side="right", padx=(0, 10), pady=10)

    # Press Enter to Send
    entry.bind("<Return>", lambda event: send())

    entry.focus()