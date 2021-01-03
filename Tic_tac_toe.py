Board = [' '] * 10

def printBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def game():
    
    player = 'X'
    count = 0
    
    for i in range(10):
        printBoard(Board)
        
        print("It's your turn, " + player + ".Move to which place?")
        
        move = int(input())
        
        if Board[move] == ' ':
            Board[move] = player
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        
        if count >= 5:
            if win():
                printBoard(Board)
                print("\nGame Over.")
                print(player + " won.")
                break                  
        
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            break
            
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
            
def win():
    if Board[7] == Board[8] == Board[9] != ' ':
        return True
    elif Board[4] == Board[5] == Board[6] != ' ':
        return True
    elif Board[1] == Board[2] == Board[3] != ' ':
        return True
    elif Board[1] == Board[4] == Board[7] != ' ':
        return True
    elif Board[2] == Board[5] == Board[8] != ' ':
        return True
    elif Board[3] == Board[6] == Board[9] != ' ':
        return True
    elif Board[7] == Board[5] == Board[3] != ' ':
        return True
    elif Board[1] == Board[5] == Board[9] != ' ':
        return True

while True: 
    print("The spaces are numbered from 1 to 9, from bottom left to top right")
    game()
    break