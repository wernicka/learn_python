# Practice program from Automate the Borting Stuff chapter 6
# Didn't ready past the outline of steps 1-3 before writing my first draft of code.
# Had to read example code to correct issues with pyperclip.copy and pyperclip.paste

import sys, pyperclip
# String of text the user inputs is stored in variable text
text = sys.argv[1]

pyperclip.copy(text)

# Splits up the user's input string on new lines, add a bullet in front of each
# line and join all the lines back together into one string
def add_bullets(input):
    input_list = input.split('\n')
    for i in input_list:
        i = '* '+ i
    input = '\n'.join(input_list)

add_bullets(text)

pyperclip.paste(text)
