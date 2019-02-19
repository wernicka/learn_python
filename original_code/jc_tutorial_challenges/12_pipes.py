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

new_file = open('heart.txt', 'w')
new_file.write(print_heart(grid))
new_file.close()

#does this do what the problem intended?
