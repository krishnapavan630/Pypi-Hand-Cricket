# Hand Cricket

A fun, interactive hand cricket game where you can play against the computer. Choose to bat or bowl and see if you can win!

## Features

- **Interactive Gameplay**: Play against the computer in a classic hand cricket match.
- **Toss Mechanism**: Choose "Even" or "Odd" for the toss to decide your role.
- **Batting and Bowling**: Experience both roles and aim to outscore the opponent.

## What's New (Latest Version)

- **Improved Input Handling**: All user input is now validated in loops (no recursion), preventing crashes from repeated invalid input.
- **Graceful Exits**: The game now handles Ctrl+C/Ctrl+D (KeyboardInterrupt/EOFError) gracefully, exiting with a friendly message.
- **Playful User Experience**: All print statements have been rewritten to be more playful, clear, and consistent, making the game more engaging.
- **Direct Script Execution**: Added an entry point (`if __name__ == "__main__": main()`) so you can run the script directly.
- **Robust and User-Friendly**: The game is now safer, more robust, and easier to use for everyone.

### How is this different from older versions?

- No more recursion errors or stack overflows from repeated invalid input.
- Clearer, friendlier prompts and results throughout the game.
- Handles unexpected exits gracefully.
- Code is easier to maintain and extend.

## Installation

pip install handy_cricket

## Usage

- import handy_cricket
- handy_cricket.main()

This will automatically trigger the game, and you can start playing.

## Functions

Here is a quick overview of the main functions in the package:

### `main()`

Starts the hand cricket game. This function handles the main menu where you can start the game, view instructions, or exit.

### `start_game()`

Initiates the toss and begins the gameplay based on the user’s selection (Even or Odd).

### `toss(opt)`

Handles the toss logic where the user chooses either Even or Odd.

### `user_batting()`

Executes the gameplay when the user chooses to bat first.

### `comp_batting()`

Executes the gameplay when the computer bats first.

### `show_instructions()`

Displays the instructions on how to play the game.

# Contributing

Feel free to fork this repository and submit a pull request. Suggestions, issues, and improvements are always welcome!
