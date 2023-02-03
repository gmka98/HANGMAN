import random 


def get__name():
    try:
        name = input("Please enter your pseudo")
        if name.isalnum() == True:
            print(""">>>Welcome"""+ name +"""!<<< You will be playing against the computer today in THE HANGMAN GAME!!!.
            Guess which word the IA randomly choose.
            Good luck and have FUN!!!""")
        else:
            raise ValueError
    except ValueError:
                print("Invalid input. Please enter only alphabet and number")
                get__name()

def play_again():
    """This function asks user/player if he/she/it wishes to replay the hangman game """ 
    response = input("Would you like to play again? yes/no. Enter 'Y' or 'N").lower()   
while play_again not in["y","n","Y","N"]:
    if play_again == 'y':
        main()
    
    elif play_again == "n":  
        print('Hope to see you soon, Bye!')
        exit()  
    
    else:
        print("Input no Valid choose between y and n.")
        break
   

def get_word():
    """This function generates the word the user have to guess"""
    words =['candy','motivation','focus','winner','lose','basketball','johnson','happy','python']
    return random.choice(words).lower()

def game_run():
    get__name()

