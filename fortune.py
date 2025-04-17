import random
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def get_time_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def get_fortune(mood, name):
    fortunes = {
        "happy": [
            f"Great things await you, {name}! Keep smiling.",
            "The universe is aligning in your favor—enjoy the vibes!",
            "Happiness is contagious. Spread it everywhere you go!"
        ],
        "sad": [
            "Tough times don’t last, but tough people do.",
            f"Hey {name}, even the darkest night will end and the sun will rise.",
            "It's okay to feel down. Brighter days are just around the corner."
        ],
        "neutral": [
            "A calm day is a canvas for unexpected joy.",
            "Balance is beautiful—embrace the moment.",
            "Sometimes no news is good news. Stay steady."
        ],
        "stressed": [
            "Take a deep breath—clarity will find you soon.",
            f"{name}, peace is one decision away. You've got this.",
            "Stress fades when you focus on progress, not perfection."
        ],
        "excited": [
            "Your energy is infectious—keep it up!",
            f"{name}, your enthusiasm will open unexpected doors!",
            "Let the excitement drive you toward greatness!"
        ]
    }

    if mood == "random":
        mood = random.choice(list(fortunes.keys()))
        print(Fore.YELLOW + f"\n🔁 Randomly selected mood: {mood}\n")

    return random.choice(fortunes.get(mood, ["😕 Sorry, I don't recognize that mood."]))


def print_welcome(name, admission_number):
    greeting = get_time_greeting()
    print(Fore.CYAN + Style.BRIGHT + "\n" + "=" * 50)
    print(Fore.MAGENTA + f"{greeting}, {name}! 👋")
    print(Fore.CYAN + Style.BRIGHT + f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")
    print("=" * 50 + "\n")


def main():
    name = "Rahil Godha"
    admission_number = "21JE0727"

    print_welcome(name, admission_number)

    print(Fore.GREEN + "📝 Moods you can choose: happy, sad, neutral, stressed, excited, random\n")
    mood = input(Fore.YELLOW + "👉 How are you feeling today? ").strip().lower()

    fortune = get_fortune(mood, name)

    print(Fore.CYAN + "\n✨ Your fortune:")
    print(Fore.LIGHTMAGENTA_EX + f"💬 {fortune} ✨\n")
    print(Fore.CYAN + "=" * 50)


if __name__ == "__main__":
    main()