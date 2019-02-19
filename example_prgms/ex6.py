# set variable types_of_people to an integer: 10
types_of_people = 10
# set variable x to a string: sentence about types_of_people.
x = f"There are {types_of_people} types of people"

# unnecessarily set values of binary and do_not to strings
binary = "binary"
do_not = "don't"
# set variable y to another string which has two instances of placing strings within strings
y = f"Those who know {binary} and those who {do_not}."

#print variable x and y
print(x)
print(y)

#instance 3 of placing a string within a string
print(f"I said: {x}")
#instance 4 of placing a string within a string
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#instance 5 of placing a string within a string, because .format converts the boolean value of hilarious to a string and places it within the string set to variable joke_evaluation.
print(joke_evaluation.format(hilarious))

# set variables w and e to strings
w = "This is the left side of..."
e = "a string with a right side."

# print variable w and variable e together
print(w + e)
