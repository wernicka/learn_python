# Practice problem at the end of Automate the Boring Stuff chapter 4

# grid[x][y] are the x and y coordinates
# (0,0) origin is in the upper left corner
# x coordinates going right
# y coordinates increase going down

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def print_heart(inputs):
    heart = ""
    for n in range(6):
        for i in range(9):
            heart += f"{inputs[i][n]}"
        heart += f"\n"
    return heart

print(print_heart(grid))
