# CSE 210 | Tic-Tac-Toe
# Norre Daroy


# Declare game board that is 3x3 squares
board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]

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