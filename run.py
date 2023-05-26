"""
word guess game
"""

import random
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

"""
Assign credentials from our API's and access our words spreadsheet
"""
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("score-board")


scoreboard = SHEET.worksheet("Sheet1")

emotions = ['love', 'hate', 'anger', 'calm', 'cheerful',
            'scared', 'annoyed', 'bored', 'excited', 'confident']
animals = ['horse', 'lion', 'lizard', 'aligator', 'donkey',
           'panda', 'ibex', 'koala', 'shark', 'zebra', 'bear']
birds = ['seagull', 'owl', 'parrot', 'dove', 'falcon', 'raven',
         'turkey', 'toucan', 'quail', 'pheasant', 'hawk']
country = ['germany', 'france', 'italy', 'brazil', 'chile', 'lebanon',
           'morocco', 'nigeria', 'pakistan', 'serbia', 'hungary']


HINT = 'The word is'


print("\t\t\t\t Welcome to the Word Guess Game\n")
print("\t\t To Play the Game please choose a letter and press Enter!\n")
print("\t\t\t\t\t Have Fun :)\n")


def get_user_data():
    """
    In this function we will get user name.
    if the user types anything other then alphabates,
    the function will print a message to the user to type again.
    """
    user_name = " "

    while True:
        user_name = input("Please enter your name:\n")
        if not user_name.isalpha():
            print("Please type alphabates only.\n")
            continue
        else:
            break
    return user_name


def game_function():
    """
    The function will run and choose a random word from the list above.
    Then it will display the word in spaces with a hint and will ask the
    user to choosea letter and give it as a guess.Total number of attempts
    will be counted contniously untill the word is been guessed or all the
    guesses are wrong.Number of guesses will increase with each guess.
    At the end, the result will be displayed.
    """

    options = [emotions, animals, birds, country]
    choice = random.choice(random.choice(options))
    scores = 0

    if choice in options[0]:
        print(f'HINT: {HINT} an Emotion.')
    elif choice in options[1]:
        print(f'HINT: {HINT} the name of an Animal.')
    elif choice in options[2]:
        print(f'HINT: {HINT} the name of a Bird.')
    elif choice in options[3]:
        print(f'HINT: {HINT} the name of a Country.')
    else:
        print("keep Trying")

    attempts = 10
    correct_guess = []
    guess = 0
    all_guesses = []

    while attempts >= 1:

        # display the word to the user as '- - - - -'
        display_word = ''
        for letter in choice:
            if letter in correct_guess:
                display_word += letter
            else:
                display_word += '_ '
            display_word += ' '
        print("Guess the word:\n")
        print(display_word.strip())

        # display the total number of attempts

        print(f'You have {attempts} attempts left\n')

        # choose a letter
        make_a_choice = input('choose a letter:\n')

        # replace the correct letter with '_'

        correct_guess.append(make_a_choice)
        # print(correct_guess)
        # display if the letter is correct/ wrong
        valid_guess = True
        if not make_a_choice.isalpha():
            print("invalid input!!! please type elphabates only.\n ")
            valid_guess = False
        else:
            if len(make_a_choice) > 1:
                print("Enter one letter at a time.\n")
                valid_guess = False
            elif make_a_choice in all_guesses and guess:
                print("You already have tried the letter.\n")
                valid_guess = False
            elif make_a_choice in choice:
                print('Correct Letter, Good job!!!\n')
                correct_guess.append(make_a_choice)
            elif make_a_choice not in choice:
                print('wrong guess\n')

        # decrease number of attempts when the letter is wrong

        if valid_guess:
            all_guesses.append(make_a_choice)
            attempts -= 1
            guess += 1
        # check if win
            win = True
            for letter in choice:
                if letter not in correct_guess:
                    win = False
                    scores = 0
                    break
            if win:
                scores = guess * 5
                print(
                    f'Well Done!You guessed the right word "{choice}".\n')
                print(f'Total Guess: {guess}.\n')
                print(f"\t\t\t\t\t\t\t\t Scores : {scores}.\n")
                return scores

    print("Sorry, You loose the Game\n")
    print(f'The Word is "{choice}".\n')
    print(f"\t\t\t\t\t\t\t\t Scores : {scores}\n")
    return scores


def score_sheet(username, score_result):
    """
    function to add user name and user scores to gspread.
    """
    scoreboard.append_row([username, score_result])
    print(f'{username} your best scores are: {score_result}\n')


def main_function():
    """
    In this function all the functions will be called and executed.
    After each win or loose the user will be asked to play again
    or leave the game. If the user chooses 'y' which is yes then the
    game will start again and bring a new random word to guess, if
    the user chooses 'n' which is no, the game will end and show
    the scores multiplied with the number of guesses user has made
    and the Leaderboard. The Leaderboard will add and display the name
    and the best scores of the user.
    """
    username = get_user_data()
    best_score = 0
    while True:
        score_result = game_function()
        if score_result > best_score:
            best_score = score_result
        user_choice = input(
            'Hey would you like to play again? Please enter Y/N.\n').lower()
        if user_choice == "y":
            continue
        else:
            print("Good Bye")
            break
    score_sheet(username, best_score)

    def leaderboard():
        print('You can see your best scores on Leaderboard\n')
        print('LEADERBOARD\n')
        all_rows = SHEET.worksheet('Sheet1').get_all_values()
        for row in all_rows:
            print(row)
    leaderboard()


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S\n")
print("Date and Time =", dt_string)


main_function()   
