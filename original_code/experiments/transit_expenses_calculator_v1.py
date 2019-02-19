# This runs and works well, but has a bug - if user puts in a value that passes the first test and fails the second (e.g., -15), they can then
#enter a value that causes a python error because they've bypassed the first test (e.g., asd)

#error messages
not_number = "Error message: not a number"
too_small = "Error message: number too small"
too_large = "Error message: number too large"

#clarifications to follow error messages
weeks_vacation_clarification = "Sorry, please enter a number between 0 and 52 for the number of weeks you were on vacation or leave this year: "
days_clarification = "Sorry, please enter a number between 0 and 7 for how many days per week you take public transit: "
fare_clarification = "Sorry, please enter a number between 0 and 100 for the cost of your one way fare: "

#max values allowed for validation tests
weeks_max = 52
days_max = 7
fare_max = 100

#function to test if input is a float
def NumberTest(i):
    try:
        val = float(i)
        return True
    except ValueError:
        return False

#function to test for bad inputs, provide user error messages, require new input, and return valid input
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
    return k

# Intro
print("Welcome to Amanda's D.C. Public Transit Annual Expense Calculator")
print("First, I need some information.")
print(" ")
# set variable for weeks per year on vacation
weeks_vacation = input("How many weeks were you on vacation or leave this year? ")
#clean input
clean_weeks_vacation = BadInputs(weeks_vacation,weeks_vacation_clarification,weeks_max)
#Set variable for weeks_worked_per_year by subtracting weeks of leave/vacaation from total weeks in a year
weeks_worked_per_year = 52 - float(clean_weeks_vacation)
#Provide user feedback
print("Ok, you were off work about {} weeks, so you worked about {} weeks." .format(clean_weeks_vacation, weeks_worked_per_year))
print(" ")

# set variable pt_commutes_per_week to average one way transit trips per week by multiplying days taking transit by 2
days_public_transit = input("""
Think about how many days per week you work from home, carpool, bike, or rideshare.
So how many days per week do you typically take public transit? """)
clean_days_public_transit = BadInputs(days_public_transit,days_clarification,days_max)
print("Ok, you typically take public transit", clean_days_public_transit, "days each week.")
print(" ")
pt_commutes_per_week = float(clean_days_public_transit) * 2

#Obtain one way rush hour fare and set as value of variable one_way
one_way = input("""Go to wmata.com and calculate your one way fare.
Make sure it's the rush hour fare if you commute during rush hour.
Enter that value here: """)
clean_one_way = BadInputs(one_way,fare_clarification,fare_max)
print("Gotcha, your one way fare is $", clean_one_way, ".")
print(" " )

total = float(clean_one_way) * float(pt_commutes_per_week) * float(weeks_worked_per_year)

# cost of public transit commutes per year
print ("Your approximate total public transit cost this year was $", int(total), ".")
print(" ")
print("Don't forget to use your employer's commuter benefit so you don't have to pay taxes on this $" , int(total), ".")
print("By using commuter benefits, you save roughly $",int(total * 0.33),".")
print(" ")
print("Thanks for using Amanda's D.C. Public Transit Annual Expense Calculator!")

#ideas for more complexities/modifications
#what if the user takes the bus some days and the metro others? Those have different costs
#what the user commutes differently seasonally? e.g. I bike for 6 months and metro the rest
