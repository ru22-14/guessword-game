"""
Word guessing game.
Choose a letter for the user to guess the word.
The user has 8 attempts to guess the word and win the game.
After each attempt, it displays thr right guesses, wrong guesses
and number of attempts left.
If the user loose it displays the right word.
"""

import random

words = ['strawberry', 'eclipse', 'chandelier', 'ketchup', 'toothpaste',
         'rainbow', 'bunk bed', 'boardgame', 'beehive', 'lemon', 'wreath',
         'waffles', 'bubble', 'whistle', 'snowball', 'bouquet', 'headphones',
         'fireworks', 'igloo', 'wheel', 'banana', 'lawnmower', 'summer',
         'whisk', 'cupcake', 'sleepingbag', 'bruise', 'Fog', 'crust',
         'battery']


def word_guess_game():
    # choose a random word
    # guess = random.choice(words)
    guess = "happy"
    attempts = 8
    correct_guess = []

    while attempts >= 0:
        # display the word to the user as '- - - - -'
        display_word = ''
        for letter in guess:
            if letter in correct_guess:
                display_word += letter
            else:
                display_word += '_ '    
            display_word += ' '
        print(display_word.strip())
    # display the total number of attempts

        print(f'You have {attempts} attempts left')
    # choose a letter
        make_a_choice = input('choose a letter: ')
        correct_guess.append(make_a_choice)
    # display if the letter is correct/ wrong
        if make_a_choice in guess:
            print('Correct letter')
        else:
            print("This letter is not in the Word")
        attempts -= 1

    # replace the letter with '-'
    # decrease number of attempts when the letter is wrong
    # check if win
    # congratulations you win, exit
    # check if loose
    # sorry you loose and display the letter, exit

    pass


word_guess_game()
