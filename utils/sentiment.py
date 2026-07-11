from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create the analyzer object
analyzer = SentimentIntensityAnalyzer()

def predict_mood(text):
    # Analyze the sentiment of the text
    score = analyzer.polarity_scores(text)

    compound = score['compound']

    # Decide the mood based on sentiment score
    if compound >= 0.5:
        mood = "Happy"

    elif compound <= -0.3:
        mood = "Sad"

    elif compound < 0:
        mood = "Anxious"

    else:
        mood = "Neutral"

    return mood, compound