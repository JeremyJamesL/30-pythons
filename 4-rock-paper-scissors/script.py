import random
game_over = 0
options = ["scissors", "paper", "rock"]

def run():
    global game_over
    guess = input("Scissors...paper...rock: ")
    computer = options[random.randint(0,2)]
    print(f'You went: {guess.upper()}, the computer went: {computer.upper()}')
    if(guess == computer):
        print('we keep going')
    elif(guess == "scissors" and computer == "rock"):
        print('computer wins')
        game_over = 1
    elif(guess == "scissors" and computer == "paper"):
        print('you win')
        game_over = 1
    elif(guess == "paper" and computer == "rock"):
        print('you win')
        game_over = 1
    elif(guess == "paper" and computer == "scissors"):
        print('computer wins')
        game_over = 1
    elif(guess == "rock" and computer == "paper"):
        print('computer wins')
        game_over = 1
    elif(guess == "rock" and computer == "scissors"):
        print('you win')
        game_over = 1
    else:
        print('this condition shouldn\'t be hit, check your logic')

while game_over == 0:
    run()
    if game_over == 1:
        print('game over')
        break
    
