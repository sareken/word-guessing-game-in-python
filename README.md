# word-guessing-game-in-python
# Word Guessing Game (Terminal-based Python Game)

## Description
This is a simple, terminal-based word guessing game developed in Python.  
It selects a random word from a list of common computer science terms such as `function`, `dataset`, `network`, etc. The user tries to guess the word one letter at a time, similar to the traditional "Hangman" game.

## Features
- Random word selection from a predefined list
- Turn-based letter guessing system
- Point system:
  - Correct vowel → +3 points
  - Correct consonant → +2 points
  - Incorrect guess → -4 points
- Word length–based guess limit
- Turkish characters are filtered out automatically
- Simple UI via terminal print statements

## Gameplay
- The player is shown the number of letters in the randomly chosen word as underscores.
- The player inputs one letter per turn.
- The word is revealed progressively as correct letters are guessed.
- The game ends when:
  - the player guesses the word correctly,
  - or the player runs out of attempts.

At the end of a round, the user can:
- Choose to play with a new word
- Exit the game

## Technologies Used
- Python 3
- `random` module

## How to Run
1. Make sure you have Python 3 installed.
2. Copy the code into a file named `kelime_oyunu.py`.
3. Run the script using a terminal:
   ```bash
   python word_guessing.py
