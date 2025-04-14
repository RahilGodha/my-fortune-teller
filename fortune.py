import random

def get_fortune(mood, name):
    fortunes = {
        "happy": [
            f"Great things await you, {name}! Keep smiling.",
            "The universe is aligning in your favor—enjoy the vibes!"
        ],
        "sad": [
            "Tough times don’t last, but tough people do.",
            f"Hey {name}, even the darkest night will end and the sun will rise."
        ],
        "neutral": [
            "A calm day is a canvas for unexpected joy.",
            "Balance is beautiful—embrace the moment."
        ],
        "stressed": [
            "Take a deep breath—clarity will find you soon.",
            f"{name}, peace is one decision away. You've got this."
        ]
    }

    return random.choice(fortunes.get(mood.lower(), ["Sorry, I don't recognize that mood."]))


def main():
    name = "Rahil"  # Replace with your full name
    admission_number = "21JE0727"  # Replace with your actual admission number

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()
    print("\n✨ Your fortune:", get_fortune(mood, name), "✨")


if __name__ == "__main__":
    main()