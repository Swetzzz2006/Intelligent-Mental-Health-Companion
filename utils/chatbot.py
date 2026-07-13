from datetime import datetime
from utils.emotion import detect_emotion


def chat():

    print("\n🤖 AI Mental Health Companion")
    print("Type 'exit' anytime to return to the main menu.\n")

    while True:

        user = input("You: ")

        if user.lower() == "exit":
            print("\n🤖 It was nice talking with you. Take care! 🌸")
            break

        # Detect emotion using Hugging Face
        emotion, confidence, emoji, suggestion = detect_emotion(user)

        # Generate intelligent response based on detected emotion
        if emotion == "fear":
            reply = (
                "🌿 I understand you're feeling anxious.\n"
                f"{suggestion}\n\n"
                "Remember, one step at a time. You've overcome challenges before, and you can handle this too."
            )

        elif emotion == "sadness":
            reply = (
                "💙 I'm really sorry you're feeling this way.\n"
                f"{suggestion}\n\n"
                "You don't have to go through difficult moments alone."
            )

        elif emotion == "joy":
            reply = (
                "😊 That's wonderful to hear!\n\n"
                "I'm really happy you're having a good day. Keep enjoying these moments!"
            )

        elif emotion == "anger":
            reply = (
                "❤️ It's okay to feel angry sometimes.\n\n"
                "Take a few deep breaths, give yourself some space, and try responding after you've calmed down."
            )

        elif emotion == "love":
            reply = (
                "❤️ That's beautiful!\n\n"
                "Positive relationships and caring for others make life more meaningful."
            )

        elif emotion == "surprise":
            reply = (
                "😲 That sounds unexpected!\n\n"
                "I hope everything turns out well for you."
            )

        else:
            reply = (
                f"{suggestion}\n\n"
                "Thank you for sharing your feelings with me."
            )

        print("\nDetected Emotion")
        print("-" * 30)
        print(f"Emotion    : {emoji} {emotion.capitalize()}")
        print(f"Confidence : {confidence*100:.2f}%")

        print("\n🤖 AI Companion")
        print("-" * 30)
        print(reply)

        # Save chat history
        with open("data/chat_history.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{datetime.now()}\n")
            file.write(f"You : {user}\n")
            file.write(f"Emotion : {emotion}\n")
            file.write(f"Confidence : {confidence:.4f}\n")
            file.write(f"Bot : {reply}\n")

def chat_response(user):

    text = user.lower()

    if any(word in text for word in [
        "sad", "cry", "depressed", "upset",
        "lonely", "hurt", "heartbroken"
    ]):
        return (
            "I'm sorry you're feeling this way. 💙 "
            "Remember that difficult moments don't last forever. "
            "Talking to someone you trust can really help."
        )

    elif any(word in text for word in [
        "anxious", "nervous", "fear", "scared",
        "stress", "stressed", "worried", "pressure",
        "exam", "interview", "college"
    ]):
        return (
            "It sounds like you're under a lot of pressure. 🌿 "
            "Take one task at a time, and don't forget to take short breaks."
        )

    elif any(word in text for word in [
        "happy", "great", "good", "excited",
        "friend", "party", "celebrate", "fun"
    ]):
        return (
            "That's wonderful to hear! 😊 "
            "Enjoy the moment and make some great memories!"
        )

    elif any(word in text for word in [
        "angry", "annoyed", "frustrated", "mad"
    ]):
        return (
            "It's okay to feel angry sometimes. ❤️ "
            "Take a few deep breaths before reacting."
        )

    elif any(word in text for word in [
        "tired", "sleepy", "exhausted"
    ]):
        return (
            "You sound tired. 😴 "
            "Getting enough rest can make a big difference."
        )

    else:
        return (
            "Thank you for sharing your thoughts with me. 😊 "
            "I'm always here to listen."
        )
def chat_response(user):

    text = user.lower()

    if any(word in text for word in [
        "sad","cry","depressed","upset",
        "lonely","hurt","heartbroken"
    ]):
        return (
            "I'm sorry you're feeling this way. 💙 "
            "Remember that difficult moments don't last forever."
        )

    elif any(word in text for word in [
        "stress","stressed","exam",
        "interview","college","anxious",
        "nervous","pressure","worried"
    ]):
        return (
            "It sounds like you're under pressure. 🌿 "
            "Take one step at a time. You've got this!"
        )

    elif any(word in text for word in [
        "happy","good","friend",
        "party","excited","fun"
    ]):
        return (
            "That's wonderful! 😊 Enjoy the moment and keep smiling!"
        )

    elif any(word in text for word in [
        "angry","frustrated","mad"
    ]):
        return (
            "It's okay to feel angry. ❤️ Try taking a few deep breaths."
        )

    else:
        return (
            "Thank you for sharing. 😊 I'm always here to listen."
        )