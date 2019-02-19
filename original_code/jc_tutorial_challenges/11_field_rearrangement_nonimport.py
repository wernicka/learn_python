# Import a CSV that contains columns 0-4.  Print out the columns in a new order:
# 4, 3, 1, 0  (We don't care about column 2 anymore.)

with open('names.csv') as file:
    data = file.read()
    print(data)

# Split on commas to make each line into a list and then rearrange the lists
# based on indexes? Or call the list items in the rearranged order?
# Could also do a nested dictionary approach similar to table printer?
# Use readlines?
