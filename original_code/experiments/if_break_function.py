

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

weeks_question = "How many weeks were you on vacation or leave this year? "
weeks_max = 52
clean_weeks_vacation = []

def validate(q,m,c):
    while True:
        print(q)
        k = input()
        if NumberTest(k) is True:
            if float(k) > 0:
                if float(k) <= m:
                    break
                else:
                    print(too_large)
            else:
                print(too_small)
        else:
            print(not_number)
    c = k
    print(c, "is valid.")
#return k
#clean_weeks_vacation = k

validate(weeks_question,weeks_max,clean_weeks_vacation)
