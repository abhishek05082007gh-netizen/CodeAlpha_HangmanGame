"""
CodeAlpha Internship - Task 1: Hangman Game
Author: Abhishek Singh
Description: A text-based Hangman game where the player guesses a secret word letter by letter within 6 attempts.
"""

import random

# Predefined list of 5 words as specified in the assignment
WORDS = ["python", "coding", "alpha", "program", "developer"]

# Visual ASCII stages for hangman progression
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    =========
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =========
    """
]

def play_game():
    word_to_guess = random.choice(WORDS).lower()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("\n" + "=" * 48)
    print("        WELCOME TO CODEALPHA HANGMAN GAME       ")
    print("=" * 48)
    print("Rules: Guess the secret word one letter at a time.")
    print(f"You have a limit of {max_incorrect_guesses} incorrect guesses.\n")

    while True:
        # Display current hangman visual
        print(HANGMAN_STAGES[incorrect_guesses])

        # Display word progress (e.g. "_ y _ h _ n")
        display_word = [letter if letter in guessed_letters else "_" for letter in word_to_guess]
        print("Word: " + " ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining attempts: {max_incorrect_guesses - incorrect_guesses}")
        print("-" * 48)

        # Check win condition
        if "_" not in display_word:
            print("\n🎉 CONGRATULATIONS! You correctly guessed the word:", word_to_guess.upper())
            break

        # Check loss condition
        if incorrect_guesses >= max_incorrect_guesses:
            print("\n💀 GAME OVER! You ran out of attempts.")
            print("The secret word was:", word_to_guess.upper())
            break

        # User input validation
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Invalid input! Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.")

def main():
    while True:
        play_game()
        choice = input("\nWould you like to play again? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nThank you for playing CodeAlpha Hangman! Goodbye.\n")
            break

if __name__ == "__main__":
    main()
