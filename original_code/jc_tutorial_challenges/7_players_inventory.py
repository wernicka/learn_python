# IMPORT DICTIONARY KEYS/VALUES - MEDIUM
# Import a CSV file with two columns; map them to key/values in a dictionary.
# Print out every key and value in the dictionary.

file = open('inventory.csv')
content = file.read()
file.close()

my_things = {}
split_content = content.split("\n")
for line in split_content:
    line = line.strip()
    if line:
        (key, val) = line.split(",")
        my_things[key] = int(val)

for key, val in my_things.items():
    print(f"{key} : {val}")
