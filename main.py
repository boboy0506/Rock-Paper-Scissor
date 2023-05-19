import random

moves = ("rock", "paper", "sccissor")
playerScore = 0
computerScore = 0

while True:
    compick = random.choice(moves)
    
    print()
    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissor")
    
    playermove = input("Pick a move: ")
    print('')
    
    while True:
        if(playermove == '1' or playermove == '2' or playermove == '3'):
            break
        else:
            print("Invalid Move")
            break


    if(playermove == '1' and compick == 'rock'):
        print("TIE")
    elif(playermove == '1' and compick == 'paper'):
        print("Computer Won")
        computerScore+=1
    elif(playermove == '1' and compick == 'sccissor'):
        print("You Won")
        playerScore+=1
    elif(playermove == '2' and compick == 'paper'):
        print("Tie")
    elif(playermove == '2' and compick == 'rock'):
        print("You Won")
        playerScore+=1
    elif(playermove == '2' and compick == 'sccissor'):
        print("Computer Won")
        computerScore+=1
    elif(playermove == '3' and compick == 'sccissor'):
        print("Tie")
    elif(playermove == '3' and compick == 'paper'):
        print("You Won")
        playerScore+=1
    elif(playermove == '3' and compick == 'rock'):
        print("Computer Won")
        computerScore+=1
    print()
    print('Player: ' + str(playerScore))
    print('Computer: ' + str(computerScore))
    print("")
    
    if(playerScore == 5):
        print('Player Won the Game')
        break
    elif(computerScore ==5):
        print('Computer Won the Game')
        break
    