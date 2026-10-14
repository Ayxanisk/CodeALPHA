"""
CodeAlpha - Python Programming Internship
Task 4: Basic Chatbot

A simple rule-based chatbot that responds to predefined user inputs.

Key Concepts Used: if-elif, functions, loops, input/output.
"""

import random

RESPONSES = {
    "hello": ["Hi!", "Hello there!", "Hey! How can I help you today?"],
    "hi": ["Hi!", "Hello there!"],
    "how are you": ["I'm fine, thanks! How about you?", "Doing great, thanks for asking!"],
    "what is your name": ["I'm a simple chatbot built with Python!", "You can call me PyBot."],
    "what can you do": ["I can chat about basic things! Try saying hello, asking how I am, or saying bye."],
    "thank you": ["You're welcome!", "No problem!"],
    "thanks": ["You're welcome!", "Anytime!"],
    "bye": ["Goodbye!", "Bye! Have a great day!", "See you later!"],
}

EXIT_WORDS = {"bye", "exit", "quit"}


def get_response(user_input):
    text = user_input.lower().strip().strip("!?.")

    for keyword, replies in RESPONSES.items():
        if keyword in text:
            return random.choice(replies)

    return "Sorry, I didn't understand that. Could you rephrase?"


def chat():
    print("=== Simple Chatbot ===")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        if user_input.lower().strip("!?.") in EXIT_WORDS:
            break


if __name__ == "__main__":
    chat()
