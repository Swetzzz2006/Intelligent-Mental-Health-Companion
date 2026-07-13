import os
import pandas as pd
import matplotlib.pyplot as plt


def generate_graphs(username):

    csv_file = os.path.join("data", username, "mood_dataset.csv")

    if not os.path.exists(csv_file):
        return

    df = pd.read_csv(csv_file)

    if len(df) == 0:
        return

    output_folder = os.path.join("data", username, "outputs")
    os.makedirs(output_folder, exist_ok=True)

    mood_counts = df["Mood"].value_counts()

    colors = {
        "Happy": "green",
        "Sad": "red",
        "Neutral": "blue",
        "Anxious": "orange"
    }

    bar_colors = [colors.get(x, "gray") for x in mood_counts.index]

    # -------- Bar Chart --------

    plt.figure(figsize=(7,5))

    plt.bar(
        mood_counts.index,
        mood_counts.values,
        color=bar_colors
    )

    plt.title("Mood Frequency")
    plt.xlabel("Mood")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "mood_bar_chart.png")
    )

    plt.close()

    # -------- Pie Chart --------

    plt.figure(figsize=(6,6))

    plt.pie(
        mood_counts.values,
        labels=mood_counts.index,
        autopct="%1.1f%%",
        colors=bar_colors,
        startangle=90
    )

    plt.title("Mood Distribution")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "mood_pie_chart.png")
    )

    plt.close()