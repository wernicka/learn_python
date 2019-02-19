# TODO Apply PEP8

# These are error messages for the Validate function
NOT_NUMBER = "Invalid: not a number"
TOO_SMALL = "Invalid: number too small"
TOO_LARGE = "Invalid: number too large"

# These are clarifications to follow error messages in the Validate function
MONTHS_CLARIFICATION = "Please enter a number between 0 and 12."
WEEKS_CLARIFICATION = "Please enter a number between 0 and 52."
DAYS_CLARIFICATION = "Please enter a number between 0 and 7."
FARE_CLARIFICATION = "Please enter a number between 0 and 100."

#These are the questions used in the Valdiate and AllYear functions
MONTHS_QUESTION = "How many months of the year do you take public transit?"
WEEKS_QUESTION = "How many weeks were you on vacation or leave this year? "
DAYS_QUESTION = """In the months when you do take transit, think about how many days per week\
 you work from home, carpool, bike, or rideshare.
So how many days per week do you typically take public transit? """
FARE_QUESTION = """Go to wmata.com and calculate your one way fare.
Make sure it's the rush hour fare if you commute during rush hour.
Enter that value here: """

# These are the max values allowed in the Validate function.
MONTHS_MAX = 12
WEEKS_MAX = 52
DAYS_MAX = 7
FARE_MAX = 100

# This is a function to test if a user input is a float
def NumberTest(i):
    try:
        val = float(i)
        return True
    except ValueError:
        return False

# This is a function to test for bad inputs. If the input is not a number or the number is too small or too large,
# it provides the user error messages and additional input guidance, and requires a new input.
def Validate(q,m,c):
    flag1 = True
    while flag1:
        print(q)
        k = input()
        if NumberTest(k) is False:
            print(NOT_NUMBER)
            print(c)
            continue
        if float(k) < 0:
            print(TOO_SMALL)
            print(c)
            continue
        if float(k) >= m:
            print(TOO_LARGE)
            print(c)
            continue
        else:
            flag1 = False
    return k

# Intro
print("Welcome to Amanda's D.C. Public Transit Annual Expense Calculator")
print("First, I need some information.")
print(" ")

#determine how many months per year user takes public transit
#TODO turn this into a function called AllYear and move it above the intro.
flag2 = True
while flag2:
    print("Do you take public transit year round, in all seasons?")
    pt_all_year = input().lower()
    if pt_all_year in ("yes", "y"):
        flag2 = False
        clean_months = 12
        print(f"You take public transit {clean_months} months per year. Thanks.")
    elif pt_all_year in ("no", "n"):
        flag2 = False
        clean_months = Validate(MONTHS_QUESTION, MONTHS_MAX, MONTHS_CLARIFICATION)
        print(f"Thanks, you take public transit {clean_months} months per year.")
    else:
        print("Please answer yes or no.")
print(" ")

# This converts months per year using public transit into a fraction
portion_year_pt = float(clean_months)/12

# Collect and validate input
clean_weeks_vacation = Validate(WEEKS_QUESTION, WEEKS_MAX, WEEKS_CLARIFICATION)
# Set variable for weeks_worked_per_year by subtracting weeks of leave/vacaation from total weeks in a year
weeks_worked_per_year = 52 - float(clean_weeks_vacation)
# Provide user feedback about their input
print(f"Ok, you were off work about {clean_weeks_vacation} weeks, so you worked about {weeks_worked_per_year} weeks.")
print(" ")

# Get a number of weeks using public transit by taking into account both vacation and other forms of commuting
weeks_pt = weeks_worked_per_year * portion_year_pt

clean_days_public_transit = Validate(DAYS_QUESTION, DAYS_MAX, DAYS_CLARIFICATION)
print(f"Ok, you typically take public transit {clean_days_public_transit} days each week.")
print(" ")
# Set variable pt_commutes_per_week to average one way transit trips per week by multiplying days taking transit by 2
pt_commutes_per_week = float(clean_days_public_transit) * 2

clean_one_way = Validate(FARE_QUESTION, FARE_MAX, FARE_CLARIFICATION)
print(f"Gotcha, your one way fare is ${clean_one_way}.")
print(" ")

# Calculate cost of public transit commutes per year
total = float(clean_one_way) * float(pt_commutes_per_week) * float(weeks_pt)

print(f"Your approximate total public transit cost this year was ${int(total)}.")
print(" ")
print(f"Don't forget to use your employer's commuter benefit so you don't have to pay taxes on this ${int(total)}.")
print(f"By using commuter benefits, you save roughly ${int(total * 0.33)}.")
print(" ")
print("Thanks for using Amanda's D.C. Public Transit Annual Expense Calculator!")

# Idea for more complexity/modification:
# What if the user takes the bus some days and the metro others? Those have different costs
