import random
playing = 1

# Initialise game
while playing == 1:

# Prompt user to roll die
    input("Ready to roll the die? Press enter!")

# Randomly choose two numbers
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

# Add them together and display them
    print(f'Die 1 rolled {die_1}')
    print(f'Die 2 rolled {die_2}')
    print(f'-----------------------------\n')
    print(f'YOU ROLLED A TOTAL OF {die_1 +  die_2}')

# Prompt user if they want to play again
    x = input("Want to play again? 1 to play again, 0 to quit: ")
    playing = int(x)
