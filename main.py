import random
# initialize the moves
moves = ("rock", "paper", "sccissor")
# scores
playerScore = 0
computerScore = 0

# loops the whole process
while True:
    # loops the computer pick
    compick = random.choice(moves)
    
    # serves as spaces
    print()
    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissor")
    
    playermove = input("Pick a move: ")
    print('')
    
    # loops the if statement, and if the move meets the condition it breaks the loop, else it will continue to loop until the condition is meet
    while True:
        if(playermove == '1' or playermove == '2' or playermove == '3'):
            break
        else:
            print("Invalid Move")
            break

            # compares the computer and player move to check if the player won or the computer won, or else tied
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
        # serves as spaces
    print("")
    print('Player: ' + str(playerScore))
    print('Computer: ' + str(computerScore))
    print("")
    
    # if one of them meets the score of 5 the game ends
    if(playerScore == 5):
        print('Player Won the Game')
        break
    elif(computerScore ==5):
        print('Computer Won the Game')
        break
    