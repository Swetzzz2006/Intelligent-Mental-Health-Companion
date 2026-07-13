from utils.auth import register_user, login_user

print(register_user("swetha", "12345"))

print(login_user("swetha", "12345"))

print(login_user("swetha", "wrongpassword"))