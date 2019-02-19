#define function formatter as a string of 4 empty strings with spaces between them
formatter = "{} {} {} {}"

#print string 1 2 3 4 using formatter function, which passes four arguments to the command format
print(formatter.format(1,2,3,4))
#print string one two three four using formatter function
print(formatter.format("one","two","three","four"))
#print string True False False True
print(formatter.format(True, False, False, True))
#print string of 12 bracket pairs with spaces in between
print(formatter.format(formatter, formatter,formatter, formatter))

print (formatter.format(
    "Hello little",
    "baby bump",
    "only four more",
    "little months"
))
