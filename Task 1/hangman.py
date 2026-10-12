import random

def play_hanggame():
    words = ["python", "hangman", "programming", "challenge", "computer"]
    word_to_guess = random.choice(words)
    guessed_letters = set()
    attempts_remaining = 6
    display_word = ["_"] * len(word_to_guess)

    print("Welcome to Hangman!")
    
    while attempts_remaining > 0 and "_" in display_word:
        print("\nCurrent word: " + " ".join(display_word))
        print(f"Attempts remaining: {attempts_remaining}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    display_word[index] = guess
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_remaining -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word: " + word_to_guess)
    else:
        print("\nGame over! The word was: " + word_to_guess)

if __name__ == "__main__":
    play_hanggame()
    