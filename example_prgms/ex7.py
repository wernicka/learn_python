print("Mary had a little lamb.")
#insert string 'snow' inside a different string
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do? - Create a line of 10 periods

#setting 12 variables to the letters that form the phrase Cheese Burger, in order
end1 = "C"
end2 = "h"
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# when I include "end = ' '" at the end, it creates a space and makes the second line of code print on the same line ("Cheese Burger")
# when I exclude "end = ' '", it prints on two lines:
# Cheese
# Burger
# when I delete the space between the single quotes, it prints on the same line but no space ("CheeseBurger")
print (end1 + end2 + end3 + end4 + end5 + end6, end='')
print (end7 + end8 + end9 + end10 + end11 + end12)
