# This beginner Python project is a fun game that generates a random number (in a certain range) that the user must guess after receiving hints. For each wrong guess the user makes, they receive extra hints but at the cost of worsening their final score.

# This program is a great way to experiment with the Python standard library, as it uses the Python random module to generate random numbers. You can also get some hands-on practice with conditional statements, print formatting, user-defined functions, and various Python operators.

import random

is_correct = 0

while is_correct == 0:
    user_guess = input("Guess a random number between 0 and 100, no floats: ")
    if "." in user_guess:
        print('Your guess needs to be an integer (no .)')
        continue
    else:
        user_guess = int(user_guess)


    if user_guess > 100 or user_guess < 0:
        print("Your guess is higher than 100, or below 0")
    elif user_guess != is_correct:
        print("You guess incorrectly, try again!")
    elif user_guess == is_correct:
        print("You guessed correctly, well done")
        is_correct = 1

