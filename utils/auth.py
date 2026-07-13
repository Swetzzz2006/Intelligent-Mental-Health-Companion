import bcrypt
import pandas as pd
import os

USERS_FILE = "data/users.csv"


# -----------------------------
# Create users.csv if missing
# -----------------------------
def initialize_users():

    if not os.path.exists(USERS_FILE):

        df = pd.DataFrame(columns=["Username", "Password"])

        df.to_csv(USERS_FILE, index=False)


# -----------------------------
# Register New User
# -----------------------------
def register_user(username, password):

    initialize_users()

    df = pd.read_csv(USERS_FILE)

    # Check if username exists
    if username.lower() in df["Username"].astype(str).str.lower().values:
        return False, "Username already exists."

    # Encrypt password
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    new_user = pd.DataFrame({
        "Username": [username],
        "Password": [hashed]
    })

    df = pd.concat([df, new_user], ignore_index=True)

    df.to_csv(USERS_FILE, index=False)

    return True, "Registration successful."


# -----------------------------
# Login User
# -----------------------------
def login_user(username, password):

    initialize_users()

    df = pd.read_csv(USERS_FILE)

    for _, row in df.iterrows():

        if str(row["Username"]).lower() == username.lower():

            stored_password = row["Password"]

            if bcrypt.checkpw(
                password.encode(),
                stored_password.encode()
            ):
                return True

            else:
                return False

    return False