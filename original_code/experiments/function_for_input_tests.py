def BadInputs(k,j,l):
    while (NumberTest(k) is False):
        print(not_number)
        k = input(j)
    while float(k) <0:
        print(too_small)
        k = input(j)
    while float(k) >=l:
        print(too_large)
        k = input(j)

def NumberTest(i):
    try:
        val = float(i)
        return True
    except ValueError:
        return False

not_number = "Error message: not a number"
too_small = "Error message: number too small"
too_large = "Error message: number too large"

weeks_max = 52
weeks_vacation_clarification = "Sorry, please enter a number between 0 and 52 for the number of weeks you were on vacation or leave this year: "

# Intro
print("Welcome to Amanda's D.C. Public Transit Annual Expense Calculator")
print("First, I need some information.")
print(" ")
# set variable weeks per year
weeks_vacation = input("""About how many weeks this year were you on vacation or leave? """)
#need an if or while statement to check the validity of each input

BadInputs(weeks_vacation,weeks_vacation_clarification,weeks_max)
