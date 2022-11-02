# CSE 210 | Tic-Tac-Toe
# Norre Daroy


# Declare game board that is 3x3 squares
board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]

currentPlayer = 'x'
gameRunning = True
winner = None

def main():
    while gameRunning:
        displayGameBoard(board)
        playerInput(board, currentPlayer)
        checkWinner(board)
        switchPlayer()

# Display game board
def displayGameBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Ask for player input    
def playerInput(board, currentPlayer):
        if currentPlayer == 'x':
            # Ask player x to input chosen spot
            inputX = int(input("x's turn to choose a square (1-9): "))
             # Check if chosen spot is already taken by checking if it's neither o and x.
            if board[inputX-1] != "o" and board[inputX-1] != "x":
                board[inputX-1] = "x"
            else:
                # If spot is already filled, then its next players move
                print("Spot already filled!!")
        else:
            # Ask player o to input chosen spot
            inputO = int(input("o's turn to choose a square (1-9): "))
            # Check if chosen spot is already taken by checking if it's neither o and x.
            if board[inputO-1] != "o" and board[inputO-1] != "x":
                board[inputO-1] = "o"
            else:
                # If spot is already filled, then its next players move
                print("Spot already filled!!")

# Check every row of game board
def checkRow(board):
    global winner
    # Check for 3 marks in 1st row
    if board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    # Check for 3 marks in 2nd row
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    # Check for 3 marks in 3rd row
    elif board[6] == board[7] == board[8]:
        winner = board[6]
        return True

# Check every column of game board
def checkColumn(board):
    global winner
    # Check for 3 marks in 1st column
    if board[0] == board[3] == board[6] and (board[0] =='x' or board[0] =='o'):
        winner = board[0]
        return True
    # Check for 3 marks in 2nd column
    elif board[1] == board[4] == board[7] and (board[1] =='x' or board[1] =='o'):
        winner = board[1]
        return True
    # Check for 3 marks in 3rd column
    elif board[2] == board[5] == board[8] and (board[2] =='x' or board[2] =='o'):
        winner = board[2]
        return True

# Check every diagonal of game board
def checkDiagonal(board):
    global winner
    # Check for 3 marks for diagonal left-right
    if board[0] == board[4] == board[8] and (board[0] =='x' or board[0] =='o'):
        winner = board[0]
        return True
    # Check for 3 marks for diagonal right-left
    elif board[2] == board[4] == board[6] and (board[2] =='x' or board[2] =='o'):
        winner = board[2]
        return True

# Check if all spots on the board are filled
def isBoardFull():
    # Loop through all 9 spots in the board
    for spot in board:
        # If spot is neither x and o then spot is not filled yet
        if spot != 'o' and spot != 'x':
            return False 
    return True

# Check if there is a winner
def checkWinner(board):
    global gameRunning

    # If rows, columns or diagonal get 3 of players marks, then there's a winner 
    if checkRow(board) or checkColumn(board) or checkDiagonal(board):
        displayGameBoard(board)
        print(f"\nThe winner is {winner}!\n\n\033[1;34;43mGood game. Thanks for playing!")
        gameRunning = False
    # If all 9 spots are full and neither player has 3 marks in a row, then it's a draw
    elif isBoardFull():
        displayGameBoard(board)
        print(f"\nIt's a draw!\n\n\033[1;34;43mGood game. Thanks for playing!")
        gameRunning = False

# Function to switch players
def switchPlayer():
    global currentPlayer

    # If current player is x then switch to player o
    if currentPlayer == 'x':
        currentPlayer = 'o'
    else:
        currentPlayer = 'x'

main()