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

    # display the word to the user '- - - - -'
    display_word = ''
    for letter in guess:
        display_word += '_ '
    print(display_word)    
    # display the total number of attempts
    
    # guess a letter
    # display if the letter is correct
    # correct
    # display if the letter is wrong
    # the letter is not in the word
    # replace the letter with '-'
    # decrease number of attempts when the letter is wrong
    # check if win
    # congratulations you win, exit
    # check if loose
    # sorry you loose and display the letter, exit
    pass


word_guess_game()             
