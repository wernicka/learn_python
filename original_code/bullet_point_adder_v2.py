# Practice program from Automate the Borting Stuff chapter 6
# Didn't ready past the outline of steps 1-3 before writing my first draft of code.
# Had to read example code to correct issues with pyperclip.copy and pyperclip.paste
# and correct the issue with only updating the variable i instead of the actual
# input_list itself.

import pyperclip
# String of text the user inputs is stored in variable text
text = pyperclip.paste()

# Splits up the user's input string on new lines, add a bullet in front of each
# line and join all the lines back together into one string
def add_bullets(input):
    input_list = input.split('\n')
    for i in range(len(input_list)):
        input_list[i] = '* '+ input_list[i]
    return '\n'.join(input_list)

pyperclip.copy(add_bullets(text))

#test = '''Lists of animals
#Lists of aquarium life
#Lists of biologists by author abbreviation
#Lists of cultivars'''

#print(add_bullets(test))
