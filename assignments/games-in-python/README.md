

# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. Practice string manipulation, loops, conditionals, and random selection while creating an interactive game.

## 📝 Tasks

### 🛠️ Task 1: Initialize Game

#### Description
Create the initial setup for your Hangman game, including word selection and game state display.

#### Requirements
Completed program should:
- Use a predefined list of at least 5 words
- Randomly select one word for each game session
- Display the hidden word as underscores (e.g., _ _ _ _)
- Show the number of incorrect guesses allowed (e.g., 6 attempts)

Example:
```
Word: _ _ _ _
Incorrect guesses left: 6
```

### 🛠️ Task 2: Play Hangman

#### Description
Implement the main gameplay loop where the player guesses letters and the game updates accordingly.

#### Requirements
Completed program should:
- Accept single-letter guesses from the player
- Reveal correct letters in their positions
- Track and display incorrect guesses remaining
- Prevent repeated guesses of the same letter
- End the game with a win if the word is fully revealed
- End the game with a loss if attempts run out
- Display a win or lose message at the end

Example:
```
Word: h _ n g m a n
Incorrect guesses left: 2
You win! 🎉
```
