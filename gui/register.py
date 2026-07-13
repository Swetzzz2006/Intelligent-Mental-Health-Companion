import customtkinter as ctk
from tkinter import messagebox
from utils.auth import register_user


class RegisterWindow(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Create Account")
        self.geometry("450x520")
        self.resizable(False, False)

        self.grab_set()

        ctk.CTkLabel(
            self,
            text="📝 Create Account",
            font=("Arial", 26, "bold")
        ).pack(pady=30)

        # Username
        ctk.CTkLabel(self, text="Username").pack(anchor="w", padx=50)

        self.username = ctk.CTkEntry(
            self,
            width=320
        )
        self.username.pack(pady=(5,20))

        # Password
        ctk.CTkLabel(self, text="Password").pack(anchor="w", padx=50)

        self.password = ctk.CTkEntry(
            self,
            width=320,
            show="*"
        )
        self.password.pack(pady=(5,20))

        # Confirm Password
        ctk.CTkLabel(
            self,
            text="Confirm Password"
        ).pack(anchor="w", padx=50)

        self.confirm = ctk.CTkEntry(
            self,
            width=320,
            show="*"
        )
        self.confirm.pack(pady=(5,30))

        ctk.CTkButton(
            self,
            text="Create Account",
            width=220,
            command=self.register
        ).pack()

    def register(self):

        username = self.username.get().strip()
        password = self.password.get().strip()
        confirm = self.confirm.get().strip()

        if username == "" or password == "" or confirm == "":
            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields."
            )
            return

        if password != confirm:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        success, message = register_user(username, password)

        if success:
            messagebox.showinfo(
                "Success",
                message
            )
            self.destroy()

        else:
            messagebox.showerror(
                "Error",
                message
            )