# Practice exercise at end of Automate the Boring Stuff Chapter 5
# made more useful for an actual D&D player

def is_absolute_value_a_decimal(i):
    try:
        val = abs(int(i))
        return True
    except ValueError:
        return False


def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for key, val in inventory.items():
        print(f"{val} {key}")
        total_items += val
    print(f"Total number of items: {total_items}")


def add_to_inventory(inventory):
    while True:
        item_to_add = input("What's the singular name of the item\
 you're adding to or removing from your inventory? (0 to quit)")
        if item_to_add in ('','nothing',0):
            break
        if item_to_add.isalpha() is False:
            print("Invalid: your inventory item name must contain only letters")
            continue
        inventory.setdefault(item_to_add,0)
        num_items_to_add = input(f"How many {item_to_add} are you\
 adding/removing? (Use negative number to remove items)")
        if is_absolute_value_a_decimal(num_items_to_add) is False:
            print("Invalid: your inventory item amount to add/remove must be a\
 positive or negative integer")
            continue
        inventory[item_to_add] += int(num_items_to_add)
        print(f"You changed your inventory by {num_items_to_add} {item_to_add}.")


file = open('inventory.txt')
content = file.read()
file.close()

my_things = {}
split_content = content.split("\n")
for line in split_content:
    line = line.strip()
    if line:
        (key, val) = line.split(":")
        my_things[key] = int(val)

display_inventory(my_things)

add_to_inventory(my_things)

display_inventory(my_things)

file = open('inventory.txt', 'w')

for key, val in my_things.items():
    file.write(f"{key}:{val}\n")

file.close()
