# Example program in automate the boring stuff chapter 5

# a nested dictionary. Each guest is a dictionary
# with the items they are bringing as keys and the number brought as values.
# the parent dict's keys are guest names and values are their item dictionary
all_guests = {'Alice' : {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

# function parameters correspond to the keys of guest names
# and sub-dictionary keys of picnic items
def total_brought(guests,item):
    # sets the initial value to 0 for the item in the argument
    num_brought = 0
    #iterates through the key-value pairs in the parent dict using the items dict method
    for k, v in guests.items():
        # uses get dict method to retrieve the item count from the sub dictionary
        # if the argument matches, and adds it to the count stored in num_brought
        num_brought += v.get(item,0)
    #return the total for that item, which summed across all guests
    return num_brought

print("Number of things being brought:")
print(f" - Apples           {total_brought(all_guests, 'apples')}")
print(f" - Cups             {total_brought(all_guests, 'cups')}")
print(f" - Cakes            {total_brought(all_guests, 'cakes')}")
print(f" - Ham Sandwiches   {total_brought(all_guests, 'ham sandwiches')}")
print(f" - Apple Pies       {total_brought(all_guests, 'apple pies')}")
