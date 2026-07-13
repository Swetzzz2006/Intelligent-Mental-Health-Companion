import customtkinter as ctk
from tkinter import messagebox

# Import all pages
from gui.dashboard import show_dashboard
from gui.profile import show_profile
from gui.analyze import show_analyze
from gui.chatbot_page import show_chat
from gui.statistics import show_statistics
from gui.history import show_history
from gui.graphs import show_graphs
from gui.tips import show_tips

# Session
from utils.session import logout


class MentalHealthApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ---------------- Appearance ----------------

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # ---------------- Window ----------------

        self.title("🧠 Intelligent Mental Health Companion")

        width = 1250
        height = 850

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)

        # ---------------- Sidebar ----------------

        self.sidebar = ctk.CTkFrame(
            self,
            width=240,
            corner_radius=0
        )
        self.sidebar.pack(side="left", fill="y")

        # ---------------- Logo ----------------

        ctk.CTkLabel(
            self.sidebar,
            text="🧠",
            font=("Arial", 52)
        ).pack(pady=(25, 5))

        ctk.CTkLabel(
            self.sidebar,
            text="Mental Health\nCompanion",
            font=("Arial", 26, "bold")
        ).pack()

        ctk.CTkLabel(
            self.sidebar,
            text="AI Powered Wellness",
            font=("Arial", 13),
            text_color="gray"
        ).pack(pady=(5, 25))

        # ---------------- Theme ----------------

        ctk.CTkLabel(
            self.sidebar,
            text="Theme",
            font=("Arial", 15, "bold")
        ).pack(pady=(5, 5))

        self.theme = ctk.CTkOptionMenu(
            self.sidebar,
            values=["Dark", "Light", "System"],
            command=self.change_theme,
            width=180
        )

        self.theme.set("Dark")
        self.theme.pack(pady=(0, 20))

        # ---------------- Navigation ----------------

        self.create_button("🏠 Dashboard", lambda: show_dashboard(self))
        self.create_button("👤 Profile", lambda: show_profile(self))
        self.create_button("😊 Analyze Mood", lambda: show_analyze(self))
        self.create_button("🤖 AI Chat", lambda: show_chat(self))
        self.create_button("📊 Statistics", lambda: show_statistics(self))
        self.create_button("📖 Mood History", lambda: show_history(self))
        self.create_button("📈 Graphs", lambda: show_graphs(self))
        self.create_button("🌿 Tips", lambda: show_tips(self))

        # Spacer

        ctk.CTkLabel(
            self.sidebar,
            text=""
        ).pack(expand=True)

        # ---------------- Logout Button ----------------

        ctk.CTkButton(
            self.sidebar,
            text="🚪 Logout",
            width=180,
            height=40,
            fg_color="#D32F2F",
            hover_color="#B71C1C",
            command=self.logout_user
        ).pack(pady=25)

        # ---------------- Main Area ----------------

        self.main = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        self.main.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=18
        )

        # ---------------- Status Bar ----------------

        self.status = ctk.CTkLabel(
            self,
            text="🤖 AI Status : Ready",
            anchor="w",
            height=28,
            font=("Arial", 13)
        )

        self.status.pack(
            side="bottom",
            fill="x",
            padx=10,
            pady=(0, 5)
        )

        # ---------------- Open Dashboard ----------------

        show_dashboard(self)

    # =======================================
    # Navigation Button
    # =======================================

    def create_button(self, text, command):

        ctk.CTkButton(
            self.sidebar,
            text=text,
            width=190,
            height=42,
            corner_radius=10,
            command=command,
            hover_color="#2563EB"
        ).pack(pady=6)

    # =======================================
    # Theme
    # =======================================

    def change_theme(self, mode):
        ctk.set_appearance_mode(mode)

    # =======================================
    # Logout
    # =======================================

    def logout_user(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if not answer:
            return

        # Clear logged-in user
        logout()

        # Close dashboard
        self.destroy()

        # Open login page again
        from gui.login import run_login
        run_login()


def run():

    app = MentalHealthApp()
    app.mainloop()