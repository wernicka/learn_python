# PRINT FILE - EASY
# Import a text file; print it to the screen

file = open('../inventory.txt')
content = file.read()
file.close()

print(content)
