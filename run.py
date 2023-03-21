"""
word guess game
"""

import random
from datetime import datetime

emotions = ['love', 'hate', 'anger']
animals = ['horse', 'lion', 'lizard']
birds = ['seagull', 'owl', 'parrot']
country = ['germany', 'france', 'italy']

hint = 'The word is'


print("\t\t\t\t Welcome to the Word Guess Game\n")
print("\t\t To Play the Game please choose a letter and press Enter!\n")
print("\t\t\t\t\t Have Fun :)\n")

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S\n")
print("Date and Time =", dt_string)


def get_user_data():
    """
    In this function we will get user name.
    if the user types anything other then alphabates,
    the function will print a message to the user to type again.
    """
    user_name = ""
    while True:
        user_name = input("Please enter your name: \n")

        if not user_name.isalpha():
            print("Please type alphabates only.\n")
            continue
        else:
            print(f"Have fun and best of Luck {user_name}.\n")
            break


get_user_data()


def game_playover():
    """
    this function will ask the user if he/she wants to play
    the game again. if yes then the game will start again,
    if not then the game will exit. 
    """
    user_choice = input('Hey would you like to play again? Please enter Y/N.\n').lower()
    if user_choice == "y":
        main_function()
    else:
        exit()


def main_function():
    """
    The function will run and choose a random word from the list above.
    Then it will display the word in spaces and will ask the user to choose
    a letter and give it as a guess.Total number of attempts will be counted
    contniously untill the word is been guessed or all the guesses are wrong.
    At the end, the result will be displayed.
    """

    options = [emotions, animals, birds, country]
    choice = random.choice(random.choice(options))

    if choice in options[0]:
        print(f'HINT: {hint} an Emotion.')
    elif choice in options[1]:
        print(f'HINT: {hint} the name of an Animal.')
    elif choice in options[2]:
        print(f'HINT: {hint} the name of a Bird.')
    elif choice in options[3]:
        print(f'HINT: {hint} the name of a Country.')
    else:
        print("keep Trying")

    attempts = 10
    correct_guess = []
    while attempts >= 1:
        # display the word to the user as '- - - - -'
        display_word = ''
        for letter in choice:
            if letter in correct_guess:
                display_word += letter
            else:
                display_word += '_ '
            display_word += ' '
        print(display_word.strip())
        # display the total number of attempts

        print(f'You have {attempts} attempts left\n')
        # choose a letter
        make_a_choice = input('choose a letter: \n')
        # replace the correct letter with '_'
        correct_guess.append(make_a_choice)

        # display if the letter is correct/ wrong
        if make_a_choice in choice:
            print('correct letter\n')
        elif make_a_choice.isnumeric():

            print("please enter alphabates only")
        else:
            print("This letter is not in the Word\n")

        # decrease number of attempts when the letter is wrong
        attempts -= 1
        # check if win
        win = True
        for letter in choice:
            if letter not in correct_guess:
                win = False
                break
        if win:
            print(
                f'Congratulations! You guessed the right word "{choice}".\n')
            game_playover()
            return

    print("Sorry, You loose the Game\n")
    print(f'The Word is "{choice}".')
    game_playover()


main_function()
