# CodeAlpha_HangmanGame

A Python text-based implementation of the classic **Hangman Game** developed as part of the **CodeAlpha Python Programming Internship**.

## 📌 Task Overview (Task 1)
- **Objective:** Create a text-based Hangman game where the player guesses a secret word one letter at a time.
- **Scope & Specifications:**
  - Uses a predefined list of 5 words (`python`, `coding`, `alpha`, `program`, `developer`).
  - Limits incorrect guesses to **6** attempts.
  - Interactive ASCII visual representation of the hangman pole and stages.
  - Console-based user input validation and replay option.

## 🛠️ Key Concepts Used
- `random` module for secret word selection
- `while` loops & conditional statements (`if-elif-else`)
- Strings & lists manipulation
- Python Sets for tracking unique guesses

## 🚀 How to Run
1. Make sure Python 3 is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/abhishek05082007gh-netizen/CodeAlpha_HangmanGame.git
   ```
3. Navigate into the directory:
   ```bash
   cd CodeAlpha_HangmanGame
   ```
4. Run the game:
   ```bash
   python hangman.py
   ```

## 🎮 Sample Gameplay Output
```text
================================================
        WELCOME TO CODEALPHA HANGMAN GAME       
================================================
Rules: Guess the secret word one letter at a time.
You have a limit of 6 incorrect guesses.

       ------
       |    |
       |
       |
       |
       |
    =========
Word: _ _ _ _ _ _
Guessed letters: None
Remaining attempts: 6
------------------------------------------------
Enter a letter: p
✅ Good guess! 'p' is in the word.
```
