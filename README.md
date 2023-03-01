# HANGMAN

## This is a Python script for a command-line based Hangman game.

The script uses the random module to generate a random word that the user has to guess. The get_name() function asks the user to enter their name and checks if it contains only alphanumeric characters. If it does, a welcome message is displayed, and the user is prompted to guess the word.

The play_again() function asks the user if they want to play again, and if the response is 'Y', the main() function is called again.

The get_word() function generates a random word from a list of pre-defined words.

The game_run() function takes the user's name as input and starts the game. It initializes the number of attempts to 6, creates an empty list to store the letters guessed by the user, and prompts the user to guess a letter. If the guessed letter is correct, it is added to the list of guessed letters. If it is incorrect, the number of attempts is decremented. The game continues until the user guesses the word correctly or runs out of attempts.

Finally, the main() function calls get_name() to get the user's name, and then calls game_run() to start the game.
