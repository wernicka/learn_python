# This program estimates the user's total D.C. public transit commuting expenses
# for one year.

# Questions asked in the get_months_public_transit_used
# and get_valid_user_input functions
MONTHS_PUBLIC_TRANSIT_QUESTION = "How many months of the year do you take\
 public transit?"
WEEKS_NOT_WORKING_QUESTION = "How many weeks were you on vacation or leave\
 this year? "
DAYS_PUBLIC_TRANSIT_PER_WEEK_QUESTION = """In the months when you do take\
 transit, think about how many days per week you work from home,\
 carpool, bike, or rideshare.
So how many days per week do you typically take public transit? """
ONE_WAY_FARE_QUESTION = """Go to wmata.com and calculate your one way fare.
Make sure it's the rush hour fare if you commute during rush hour.
Enter that value here: """

# Max values allowed in the get_valid_user_input function.
MONTHS_PULIC_TRANSIT_MAX = 12
WEEKS_NOT_WORKING_MAX = 52
DAYS_PUBLIC_TRANSIT_PER_WEEK_MAX = 7
ONE_WAY_FARE_MAX = 100

# Clarifications to follow error messages in the get_valid_user_input function
MONTHS_PULIC_TRANSIT_CLARIFICATION = "Please enter a number between 0 and 12."
WEEKS_NOT_WORKING_CLARIFICATION = "Please enter a number between 0 and 52."
DAYS_PUBLIC_TRANSIT_PER_WEEK_CLARIFICATION = "Please enter a number between\
 0 and 7."
ONE_WAY_FARE_CLARIFICATION = "Please enter a number between 0 and 100."


# This is a function to test if a user input is a float
def is_value_float(i):
    try:
        val = float(i)
        return True
    except ValueError:
        return False


# This is a function to test for inputs that cause errors or don't make sense.
# If the input is not a number, or the number is too small or too large,it
# provides the user additional input guidance and requires a new input.
def get_valid_user_input(question, max, clarification):
    while True:
        print(question)
        user_input = input()
        if is_value_float(user_input) is False:
            print("Invalid: not a number")
            print(clarification)
            continue
        if float(user_input) < 0:
            print("Invalid: number too small")
            print(clarification)
            continue
        if float(user_input) >= max:
            print("Invalid: number too large")
            print(clarification)
        else:
            break
    return user_input


# This is a function to determine how many months per year user
# takes public transit, and ensure it is a valid input.
def get_months_public_transit_used():
    while True:
        print("Do you take public transit year round, in all seasons?")
        pt_all_year = input().lower()
        if pt_all_year in ("yes", "y"):
            return 12
        elif pt_all_year in ("no", "n"):
            return get_valid_user_input(MONTHS_PUBLIC_TRANSIT_QUESTION,
                                        MONTHS_PULIC_TRANSIT_MAX,
                                        MONTHS_PULIC_TRANSIT_CLARIFICATION)
        else:
            print("Please answer yes or no.")


print("Welcome to Amanda's Annual D.C. Public Transit Commmute\
 Expense Calculator")
print("First, I need some information.")
print(" ")

months_public_transit_used = get_months_public_transit_used()
print(f"You take public transit {months_public_transit_used} months per year.\
 Thanks.")
print(" ")

portion_year_using_public_transit = float(months_public_transit_used)/12

weeks_not_working = get_valid_user_input(WEEKS_NOT_WORKING_QUESTION,
                                         WEEKS_NOT_WORKING_MAX,
                                         WEEKS_NOT_WORKING_CLARIFICATION)
weeks_worked_per_year = 52 - float(weeks_not_working)
print(f"Ok, you were off work about {weeks_not_working} weeks,\
 so you worked about {weeks_worked_per_year} weeks.")
print(" ")

annual_weeks_using_public_transit = weeks_worked_per_year *\
                             portion_year_using_public_transit

days_public_transit_per_week = get_valid_user_input(
                                  DAYS_PUBLIC_TRANSIT_PER_WEEK_QUESTION,
                                  DAYS_PUBLIC_TRANSIT_PER_WEEK_MAX,
                                  DAYS_PUBLIC_TRANSIT_PER_WEEK_CLARIFICATION)
print(f"Alright, you typically take public transit\
 {days_public_transit_per_week} days each week.")
print(" ")
public_transit_one_ways_per_week = float(days_public_transit_per_week) * 2

one_way_fare = get_valid_user_input(ONE_WAY_FARE_QUESTION, ONE_WAY_FARE_MAX,
                                    ONE_WAY_FARE_CLARIFICATION)
print(f"Gotcha, your one way fare is ${one_way_fare}.")
print(" ")

# Calculate cost of public transit commutes per year
total = float(one_way_fare) * float(public_transit_one_ways_per_week) *\
        float(annual_weeks_using_public_transit)

print(f"Your approximate total public transit commuting cost\
 this year was ${int(total)}.")
print(" ")
print(f"Don't forget to use your employer's commuter benefit\
 so you don't have to pay taxes on this ${int(total)}.")
print(f"By using commuter benefits, you save roughly ${int(total * 0.33)}.")
print(" ")
print("Thanks for using Amanda's Annual D.C. Public Transit Commmute\
 Expense Calculator!")

# Idea for more complexity/modification:
# What if the user takes the bus some days and the metro others?
# Those have different costs
