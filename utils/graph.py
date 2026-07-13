import os
import pandas as pd
import matplotlib.pyplot as plt

from utils.session import get_user

# ---------------- Current User ----------------

username = get_user()

if username is None:
    username = "User"

# ---------------- Paths ----------------

user_folder = os.path.join("data", username)

csv_file = os.path.join(user_folder, "mood_dataset.csv")

output_folder = os.path.join(user_folder, "outputs")

os.makedirs(output_folder, exist_ok=True)

# ---------------- Check CSV ----------------

if not os.path.exists(csv_file):
    print("No mood data found.")
    exit()

df = pd.read_csv(csv_file)

if df.empty:
    print("No mood records available.")
    exit()

# ---------------- Mood Count ----------------

mood_counts = df["Mood"].value_counts()

colors = {
    "Happy": "green",
    "Sad": "red",
    "Anxious": "orange",
    "Neutral": "blue"
}

bar_colors = [colors.get(mood, "gray") for mood in mood_counts.index]

# =========================
# BAR CHART
# =========================

plt.figure(figsize=(7,5))

bars = plt.bar(
    mood_counts.index,
    mood_counts.values,
    color=bar_colors
)

plt.title(f"{username}'s Mood Frequency")
plt.xlabel("Mood")
plt.ylabel("Count")

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.05,
        str(int(height)),
        ha="center"
    )

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "mood_bar_chart.png")
)

plt.close()

# =========================
# PIE CHART
# =========================

plt.figure(figsize=(6,6))

pie_colors = [colors.get(mood, "gray") for mood in mood_counts.index]

plt.pie(
    mood_counts.values,
    labels=mood_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=pie_colors
)

plt.title(f"{username}'s Mood Distribution")

plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "mood_pie_chart.png")
)

plt.close()

print("✅ Graphs generated successfully!")