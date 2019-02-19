#Example program from Automate the Boring Stuff Ch 5

birthdays = {"Alice": 'Apr 1', "Bob": "Dec 12", "Carol": "Mar 4"}

while True:
    name = input("Enter a name: (blank to quit)")
    if name == '':
        break

if name in birthdays:
    print(f"{birthdays[name]} is the birthday of {name}")
else:
    print(f"I do not have birthday information for {name}")
    birthdays[name] = input("What is their birthday?")
    print("Birthday database updated.")

# All the data you enter in this program is forgotten when the program terminates.
# You’ll learn how to save data to files on the hard drive in Chapter 8.
