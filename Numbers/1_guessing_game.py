# Write a function (guessing_game) that takes no arguments
# When run, the function chooses a random integer between 0 and 100 (inclusive).
# Then ask the user to guess what number has been chosen.
# Each time the user enters a guess, the program indicates one of the following:
#     – Too high
#     – Too low
#     – Just right

# If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.

# The program only exits after the user guesses correctly

import random

def guessing_game():
    number_to_be_guessed = random.randint(1,100)
    while True :
        user_choice = int(input('Guess the number : '))
        if user_choice > number_to_be_guessed:
            print('Too High. Try again\n')
        elif user_choice < number_to_be_guessed:
            print('Too Low. try again\n')
        else:
            print('Just right!')
            break


guessing_game()