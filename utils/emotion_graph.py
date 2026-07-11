import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("data/mood_dataset.csv")

# Count emotions
emotion_counts = df["Emotion"].value_counts()

# -------- Bar Chart --------
plt.figure(figsize=(7,5))
emotion_counts.plot(kind="bar")

plt.title("Emotion Distribution")
plt.xlabel("Emotion")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("outputs/emotion_bar_chart.png")
plt.close()

# -------- Pie Chart --------
plt.figure(figsize=(6,6))
emotion_counts.plot(kind="pie", autopct="%1.1f%%")

plt.ylabel("")
plt.title("Emotion Distribution")

plt.tight_layout()
plt.savefig("outputs/emotion_pie_chart.png")
plt.close()

print("✅ Emotion graphs generated successfully!")