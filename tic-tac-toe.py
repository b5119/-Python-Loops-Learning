from random import randrange


def display_board(board):
    """Display the board with proper formatting."""
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    """Handle user input with comprehensive validation."""
    ok = False
    while not ok:
        move = input("Enter your move: ")
        
        # Validate input is a single digit between 1-9
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Bad move - repeat your input!")
            continue
        
        # Convert to board coordinates
        move = int(move) - 1
        row = move // 3
        col = move % 3
        
        # Check if square is free
        sign = board[row][col]
        ok = sign not in ['O', 'X']
        if not ok:
            print("Field already occupied - repeat your input!")
            continue
    
    board[row][col] = 'O'


def make_list_of_free_fields(board):
    """Build a list of all free squares as (row, col) tuples."""
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free


def victory_for(board, sign):
    """
    Check if the player using the given sign has won.
    Returns 'you' for O, 'me' for X, or None if no winner.
    """
    if sign == "X":
        who = 'me'
    elif sign == "O":
        who = 'you'
    else:
        who = None
    
    # Check rows and columns
    for rc in range(3):
        # Check row
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who
        # Check column
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
    
    # Check diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return who
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return who
    
    return None


def draw_move(board):
    """Computer makes a random move from available squares."""
    free = make_list_of_free_fields(board)
    if free:
        move = free[randrange(len(free))]
        board[move[0]][move[1]] = 'X'


# Initialize board with numbers 1-9
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]

# Computer makes first move in the center
board[1][1] = 'X'

# Main game loop
free = make_list_of_free_fields(board)
human_turn = True

while free:
    display_board(board)
    
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    
    if victor:
        break
    
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

# Display final board and result
display_board(board)

if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won!")
else:
    print("Tie!")