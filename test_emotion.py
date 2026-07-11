from utils.emotion import detect_emotion

print("=" * 50)
print(" Intelligent Mental Health Companion")
print("=" * 50)

text = input("How are you feeling today?\n> ")

emotion, confidence, emoji, suggestion = detect_emotion(text)

print("\nEmotion Detected")
print("-" * 30)
print(f"Emotion    : {emoji} {emotion.capitalize()}")
print(f"Confidence : {confidence * 100:.2f}%")

print("\nSuggestion")
print("-" * 30)
print(suggestion)