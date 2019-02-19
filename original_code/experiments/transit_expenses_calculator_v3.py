#nested dictionary - does not work

#error messages
not_number = "Error message: not a number"
too_small = "Error message: number too small"
too_large = "Error message: number too large"

#Dictionary of questions, max numbers, variables for validated data to be set to,
#and user feedback message for each of the three data points I need to analyze
allData = {
Weeks:
{weeks_question : "How many weeks were you on vacation or leave this year? ",
weeks_max : 52,
clean_weeks_vacation : [],
weeks_feedback : "Ok, you were off work about {} weeks, so you worked about {} weeks." .format(clean_weeks_vacation, 52 - float(clean_weeks_vacation)))
}
Days:
{days_question : """Think about how many days per week you work from home, carpool, bike, or rideshare.
So how many days per week do you typically take public transit? """,
days_max : 7,
clean_days_public_transit : [],
days_feedback : "Ok, you typically take public transit", clean_days_public_transit, "days each week."
}
Fare:
{fare_question : """Go to wmata.com and calculate your one way fare.
Make sure it's the rush hour fare if you commute during rush hour.
Enter that value here: """,
fare_max = 100,
clean_one_way : [],
fare_feedback : "Gotcha, your one way fare is $", clean_one_way, "."
}
}

#function to test if input is a float
def NumberTest(i):
    try:
        val = float(i)
        return True
    except ValueError:
        return False

#function to test for bad inputs, provide user error messages, require new input,
# set valid input to pre-specified variable, and print user feedback

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

For key in allData.values()
    validate()

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
