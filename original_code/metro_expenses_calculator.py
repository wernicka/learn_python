# Intro
print("Welcome to Amanda's D.C. Public Transit Annual Expense Calculator")
print("First, I need some information.")
print(" ")
# set variable weeks per year
weeks_vacation = input("""About how many weeks this year were you on vacation or leave? """)
# Fix: I need to test if the input was an integer or only use the integer if the add other characters
weeks_worked_per_year = 52 - int(weeks_vacation)
print("Ok, you were off work about {} weeks, so you worked about {} weeks." .format(weeks_vacation, weeks_worked_per_year))
print(" ")
# set variable = average one ways per week
days_public_transit = input("""
Think about how many days per week you work from home, carpool, bike, or rideshare.
So how many days per week do you typically take public transit? """)
pt_commutes_per_week = float(days_public_transit) * 2
#Fix: also need to test this input was an integer
print("Ok, you typically take public transit", days_public_transit, "days each week.")
print(" ")
#what if the user takes the bus some days and the metro others? Those have different costs
#what the user commutes differently seasonally?
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
