
# questions
weeks_question = "How many weeks were you on vacation or leave this year? "
days_question = """Think about how many days per week you work from home, carpool, bike, or rideshare.
So how many days per week do you typically take public transit? """
fare_question = """Go to wmata.com and calculate your one way fare.
Make sure it's the rush hour fare if you commute during rush hour.
Enter that value here: """

#names for validated/clean variables
clean_weeks_vacation = []
clean_days_public_transit = []
clean_one_way = []

#user weeks feedback
weeks_feedback = "Ok, you were off work about {} weeks, so you worked about {} weeks." .format(clean_weeks_vacation, 52 - float(clean_weeks_vacation)))
days_feedback = "Ok, you typically take public transit", clean_days_public_transit, "days each week."
fare_feedback = "Gotcha, your one way fare is $", clean_one_way, "."

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
#bug - if user puts in a value that passes the first test and fails the second (e.g., -15), they can then
#enter a value that causes a python error because they've bypassed the first test (e.g., asd)

#separate the validations so they're not sequential

#each input the user gives needs to run through ALL the valiations.
#instead of asking for inputs within the validation, I need to loop back to the original request (fewer lines of code)
# or have a new path for all invalid ks?

#what if I reverse the pattern so the program only continues if the inputs are valid.
#any invalid inputs else out and loop back to that original input...
#no that would have the same problem

#I need three pieces of information.
#For each piece of information there is a question and a max input parameter
# the output of the function should be a valid variable for that question
# I need to run the function 3 times
# could I pass a list of key value pairs?

def validate(q,m,c,f):
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
    c = float(k)
    print(f)
    print (" ")


# Intro
print("Welcome to Amanda's D.C. Public Transit Annual Expense Calculator")
print("First, I need some information.")


total = clean_one_way * (clean_days_public_transit * 2) * (52 - clean_weeks_vacation)

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
