import random

emotions = ['love', 'hate', 'anger']
animals = ['horse', 'lion', 'lizard']
birds = ['seagull', 'owl', 'parrot']
country = ['germany', 'france', 'italy']

hint = 'The word is'

print("\t\t\t\t Welcome to the Word Guess Game\n")
print("\t\t To Play the Game please choose a letter and press Enter!\n")
print("\t\t\t\t\t Have Fun :)\n")


def main_function():
    """
        The function will run and choose a random word from the list above.Then
        it will display the word in spaces and will ask the user to choose a letter
        and give it as a guess.Total number of attempts will be counted contniously
        untill the word is been guessed or all the guesses are wrong. At the end,
         the result will be displayed.
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
            # game_playOver()
            return

    print("Sorry, You loose the Game\n")
    print(f'The Word is "{choice}".')



main_function()
