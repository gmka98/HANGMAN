import random

def get_name():
    try:
        name = input("Please enter your pseudo: ")
        if name.isalnum() == True:
            print(""">>>Welcome """+ name +"""!<<< You will be playing against the computer today in THE HANGMAN GAME!!!.
            Guess which word the IA randomly choose.
            Good luck and have FUN!!!""")
            return name
        else:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter only alphabets and numbers.")
        return get_name()

def play_again():
    """This function asks user/player if he/she/it wishes to replay the hangman game"""
    while True:
        response = input("Would you like to play again? Enter 'Y' or 'N': ").lower()
        if response == 'y':
            main()
        elif response == 'n':
            print('Hope to see you soon, Bye!')
            exit()
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def get_word():
    """This function generates the word the user have to guess"""
    words = ['candy', 'motivation', 'focus', 'winner', 'lose', 'basketball', 'johnson', 'happy', 'python']
    return random.choice(words).lower()

def game_run(name):
    word = get_word()
    print(f"The word has {len(word)} letters.")
    attempts = 6
    letters_guessed = []
    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        if guess in letters_guessed:
            print("You already guessed that letter. Try again.")
            continue
        elif guess in word:
            letters_guessed.append(guess)
            print("Correct!")
        else:
            attempts -= 1
            print(f"Incorrect. You have {attempts} attempts left.")
        if set(word) == set(letters_guessed):
            print(f"Congratulations {name}! You guessed the word '{word}'!")
            break
    if attempts == 0:
        print(f"Sorry {name}, you have no attempts left. The word was '{word}'.")
    play_again()

def main():
    name = get_name()
    game_run(name)

main()
