#successful experiment!


l = 52
not_number = "Error message: not a number"
weeks_vacation_clarification = "Sorry, please enter a number between 0 and 52 for the number of weeks you were on vacation or leave this year: "
def NumberTest(i):
    try:
        val = float(i)
        return True
    except ValueError:
        return False

k = ""
while True:
    print("How many weeks were you on vacation or leave this year? ")
    k = input()
    if NumberTest(k) is False:
        print("Error message: not a number")
        print(weeks_vacation_clarification)
        continue
    if float(k) < 0:
        continue
    if float(k) >= l:
        continue
    else:
        break
print(k, "is a valid number of weeks") #return k

#seems to work from a logical standpoint (not thoroughly tested)
# but my error messages aren't printed

# I'm an idiot - the error messages that aren't printed aren't in this version



#while True:
#  print('Who are you?')
#  name = input()
#  if name != 'Joe':       #(1)
#    continue              #(2)
#  print('Hello, Joe. What is the password? (It is a fish.)')
#  password = input()      #(3)
#  if password == 'swordfish':
#    break                 #(4)
#print('Access granted.')  #(5)
