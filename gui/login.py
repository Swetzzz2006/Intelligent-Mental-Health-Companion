import customtkinter as ctk
from tkinter import messagebox

from utils.auth import login_user


class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.title("Login - Mental Health Companion")

        width = 500
        height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)

        # ---------------- Logo ----------------

        ctk.CTkLabel(
            self,
            text="🧠",
            font=("Arial", 70)
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            self,
            text="Mental Health Companion",
            font=("Arial", 28, "bold")
        ).pack()

        ctk.CTkLabel(
            self,
            text="Welcome Back!",
            font=("Arial", 16),
            text_color="gray"
        ).pack(pady=(5, 35))

        # ---------------- Username ----------------

        ctk.CTkLabel(
            self,
            text="Username",
            font=("Arial", 15)
        ).pack(anchor="w", padx=70)

        self.username = ctk.CTkEntry(
            self,
            width=360,
            height=40
        )
        self.username.pack(pady=(5, 20))

        # ---------------- Password ----------------

        ctk.CTkLabel(
            self,
            text="Password",
            font=("Arial", 15)
        ).pack(anchor="w", padx=70)

        self.password = ctk.CTkEntry(
            self,
            width=360,
            height=40,
            show="*"
        )
        self.password.pack(pady=(5, 30))

        # ---------------- Login Button ----------------

        ctk.CTkButton(
            self,
            text="Login",
            width=220,
            height=45,
            command=self.login
        ).pack()

        # ---------------- Register ----------------

        ctk.CTkLabel(
            self,
            text="Don't have an account?",
            text_color="gray"
        ).pack(pady=(30, 5))

        ctk.CTkButton(
            self,
            text="Register",
            fg_color="green",
            hover_color="darkgreen",
            width=220,
            height=40,
            command=self.register
        ).pack()

    # ==================================
    # Login
    # ==================================

    def login(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        if username == "" or password == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )
            return

        if login_user(username, password):

            messagebox.showinfo(
                "Success",
                "Login Successful!"
            )

            from utils.session import set_user
            from gui.main_window import run

            # Save logged-in user
            set_user(username)

            # Close login window
            self.destroy()

            # Open main application
            run()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

    # ==================================
    # Register
    # ==================================

    def register(self):

        from gui.register import RegisterWindow

        RegisterWindow(self)


def run_login():

    app = LoginWindow()
    app.mainloop()