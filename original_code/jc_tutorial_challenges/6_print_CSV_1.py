# PRINT CSV 001- EASY
# Import a CSV file and print each line

file = open('../../../Desktop/test_file.csv')
content = file.read()
file.close()

print(content)
