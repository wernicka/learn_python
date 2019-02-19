l = 52

not_number = "Error message: not a number"
too_small = "Error message: number too small"
too_large = "Error message: number too large"
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
    if NumberTest(k) is True:
        if float(k) > 0:
            if float(k) <= l:
                break
            else:
                print(too_large)
        else:
            print(too_small)
    else:
        print(not_number)
print(k, "is a valid number of weeks")
#return k
#clean_weeks_vacation = k
