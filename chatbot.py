import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey 👋"],
    "how are you": ["I'm good, thanks!", "Doing great!"],
    "bye": ["Goodbye 👋", "See you later!"]
}

while True:
    user = input("You: ").lower()
    if user in responses:
        print("Bot:", random.choice(responses[user]))
    else:
        print("Bot: I don't understand that.")
    if user == "bye":
        break
