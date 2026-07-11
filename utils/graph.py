import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("data/mood_dataset.csv")

# Count moods
mood_counts = df["Mood"].value_counts()

# Colors for moods
colors = {
    "Happy": "green",
    "Sad": "red",
    "Anxious": "orange",
    "Neutral": "blue"
}

bar_colors = [colors.get(mood, "gray") for mood in mood_counts.index]

# -------------------------
# Bar Chart
# -------------------------
plt.figure(figsize=(7,5))
bars = plt.bar(mood_counts.index, mood_counts.values, color=bar_colors)

plt.title("Mood Frequency")
plt.xlabel("Mood")
plt.ylabel("Count")

# Add values above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.05,
        str(int(height)),
        ha='center'
    )

plt.savefig("outputs/mood_bar_chart.png")
plt.show()

# -------------------------
# Pie Chart
# -------------------------
plt.figure(figsize=(6,6))

pie_colors = [colors.get(mood, "gray") for mood in mood_counts.index]

plt.pie(
    mood_counts.values,
    labels=mood_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=pie_colors
)

plt.title("Mood Distribution")

plt.savefig("outputs/mood_pie_chart.png")
plt.show()

print("✅ Graphs generated successfully!")