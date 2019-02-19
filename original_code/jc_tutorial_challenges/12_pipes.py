# PIPES - EASY, FUNDAMENTAL
# Write a script that prints something to the screen.  Write it to a file
# without using write logic within the script.

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


#type into Terminal: python3 12_pipes.py > heart.txt