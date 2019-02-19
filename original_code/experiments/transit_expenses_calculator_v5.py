#works! Bug in version 1 fixed! #new feature for seasonal commuters!

#error messages
not_number = "Invalid: not a number"
too_small = "Invalid: number too small"
too_large = "Invalid: number too large"

#clarifications to follow error messages
months_clarification = "Please enter a number between 0 and 12."
weeks_vacation_clarification = "Please enter a number between 0 and 52."
days_clarification = "Please enter a number between 0 and 7."
fare_clarification = "Please enter a number between 0 and 100."

# questions
months_question = "How many months of the year do you take public transit?"
weeks_question = "How many weeks were you on vacation or leave this year? "
days_question = """In the months when you do take transit, think about how many days per week you work from home, carpool, bike, or rideshare.
So how many days per week do you typically take public transit? """
fare_question = """Go to wmata.com and calculate your one way fare.
Make sure it's the rush hour fare if you commute during rush hour.
Enter that value here: """

#max values allowed for validation tests
months_max = 12
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

#function to test for bad inputs, provide user error messages, require new input,
# set valid input to pre-specified variable, and print user feedback
k = "" #is this necessary?
def validate(q,m,c):
    while True:
        print(q)
        k = input()
        if NumberTest(k) is False:
            print(not_number)
            print(c)
            continue
        if float(k) < 0:
            print(too_small)
            print(c)
            continue
        if float(k) >= m:
            print(too_large)
            print(c)
            continue
        else:
            break
    #print(k, "is valid")
    return k

# Intro
print("Welcome to Amanda's D.C. Public Transit Annual Expense Calculator")
print("First, I need some information.")
print(" ")

#determine how many months per year user takes public transit
x = ""
y = "yes"
n = "no"
while True:
    print("Do you take public transit year round, in all seasons?")
    x = input()
    x = x.lower()
    if x == y:
        break
    if x == n:
        break
    print("Please answer yes or no.")

if x == n:
    clean_months = validate(months_question, months_max, months_clarification)
    print("Thanks, you take public transit", clean_months, "months per year.")

if x == y:
    clean_months = 12
    print("You take public transit 12 months per year. Thanks.")
print(" ")

#convert months per year using public transit to a fraction
portion_year_pt = float(clean_months)/12

#collect and validate input
clean_weeks_vacation = validate(weeks_question, weeks_max, weeks_vacation_clarification)
#Set variable for weeks_worked_per_year by subtracting weeks of leave/vacaation from total weeks in a year
weeks_worked_per_year = 52 - float(clean_weeks_vacation)
#Provide user feedback
print("Ok, you were off work about {} weeks, so you worked about {} weeks." .format(clean_weeks_vacation, weeks_worked_per_year))
print(" ")

#get a number of weeks using public transit by taking into account both vacation and other forms of commuting
weeks_pt = weeks_worked_per_year * portion_year_pt

clean_days_public_transit = validate(days_question, days_max, days_clarification)
print("Ok, you typically take public transit", clean_days_public_transit, "days each week.")
print(" ")
# set variable pt_commutes_per_week to average one way transit trips per week by multiplying days taking transit by 2
pt_commutes_per_week = float(clean_days_public_transit) * 2

clean_one_way = validate(fare_question, fare_max, fare_clarification)
print("Gotcha, your one way fare is $", clean_one_way, ".")
print(" ")

total = float(clean_one_way) * float(pt_commutes_per_week) * float(weeks_pt)

# cost of public transit commutes per year
print ("Your approximate total public transit cost this year was $", int(total), ".")
print(" ")
print("Don't forget to use your employer's commuter benefit so you don't have to pay taxes on this $" , int(total), ".")
print("By using commuter benefits, you save roughly $",int(total * 0.33),".")
print(" ")
print("Thanks for using Amanda's D.C. Public Transit Annual Expense Calculator!")

#ideas for more complexities/modifications
#what if the user takes the bus some days and the metro others? Those have different costs
