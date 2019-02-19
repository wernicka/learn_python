# Practice problem at the end of Chapter 6 of Automate the Boring Stuff
# version written without reading anything beyond the first line of the hint,
# which I couldn't help but see. Slightly different program than what the book
# author wrote but it still met the specifications and I think my resulting
# table looks nicer and is easier to read.
# Definetly think there are better ways to do this.
# Not sure if it should be one function.

TABLEDATA = [['dogs', 'cats', 'moose', 'goose'],
             ['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David']]


def get_max_num_char(things):
    max_num_char = 0
    for i in range(len(things[0])):
        for n in range(len(things)):
            if len(things[n][i]) > max_num_char:
                max_num_char = len(things[n][i])
    return max_num_char


# Takes a list of lists of strings and displays it in a well-organized table
# with each column right-justified.
# Assume that all the inner lists will contain the same number of strings
def print_table(things,span):
    table_string = ""
    for i in range(len(things[0])):
        for n in range(len(things)):
            table_string += f"{things[n][i].rjust(span)} "
        table_string += "\n"
    print(table_string)


print_table(TABLEDATA, get_max_num_char(TABLEDATA))

#this was my original psuedo code
    #iterate through each list
        #create a new list for each table row
        #add the item from each list to the corresponding new list
        #find the list item with the largest number of characters
        #right justify each item in the list across that number of characters
        #print each new list with a space separator instead of a comma separator
