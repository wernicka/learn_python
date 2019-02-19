# Intro
print("Welcome to Amanda's D.C. Public Transit Annual Expense Calculator")
print("First, I need some information.")
print(" ")
# set variable weeks per year
weeks_vacation = input("""About how many weeks this year were you on vacation or leave? """)
#need an if or while statement to check the validity of each input

if float(weeks_vacation) >0 AND <53,
    print("True") #for debugging/testing
    weeks_worked_per_year = 52 - int(weeks_vacation)
    print("Ok, you were off work about {} weeks, so you worked about {} weeks." .format(weeks_vacation, weeks_worked_per_year))
    print(" ")
    # set variable = average one ways per week
    days_public_transit = input("""
    Think about how many days per week you work from home, carpool, bike, or rideshare.
    So how many days per week do you typically take public transit? """)

    if float(days_public_transit) >0 AND <8,
        pt_commutes_per_week = float(days_public_transit) * 2
        print("Ok, you typically take public transit", days_public_transit, "days each week.")
        print(" ")

        #Obtain one way rush hour fare and set as value of variable one_way
        one_way = input("""Go to wmata.com and calculate your one way fare.
        Make sure it's the rush hour fare if you commute during rush hour.
        Enter that here: """)
        #Fix: also need to test this input was an integer
        print("Gotcha, your one way fare is $", one_way, ".")
        print(" " )

        total = float(one_way) * float(pt_commutes_per_week) * float(weeks_worked_per_year)

        # cost of public transit commutes per year
        print ("Alright, all in all your approximate public transit cost this year was $", int(total), "!")
    else days_public_transit = input("""
    Think about how many days per week you work from home, carpool, bike, or rideshare.
    So how many days per week do you typically take public transit? """)

else weeks_vacation = input("Sorry, please enter a number between 0 and 52 for the number of weeks you were on vacation or leave this year: ")
# how do I loop in so I don't have duplicate code?

#what if the user takes the bus some days and the metro others? Those have different costs
#what the user commutes differently seasonally?
