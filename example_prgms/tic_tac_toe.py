# Example program Automate the boring stuff chapter 5

# dictionary with the tic tac toe board space names as keys
# and the spaces or turns taken as values
the_board = {'top-L': ' ','top-M': ' ','top-R': ' ',
             'mid-L': ' ','mid-M': ' ','mid-R': ' ',
             'low-L': ' ','low-M': ' ','low-R': ' '}

# Visualizes a tic tac toe board with the contents of the dictionary populated
def print_board(board):
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print("-+-+-")
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print("-+-+-")
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']}")

# player x always goes first. Variable turn keeps track of which player's
# turn it is. The player will enter the representation of
# the space they want to take for their turn as the key.
turn = 'X'
for i in range(9):
    print_board(the_board)
    move = input(f"Turn for {turn}. Move on which space?")
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)

# Doesn't check whether anyone has one, just continues 9 times
# Also doesn't prevent a player over-writing another player's move.
