clean_weeks_vacation = ""
clean_days_public_transit = ""
clean_one_way = ""

weeks_feedback = "Ok, you were off work about {} weeks, so you worked about {} weeks." .format(clean_weeks_vacation, clean_weeks_vacation)
days_feedback = "Ok, you typically take public transit" + clean_days_public_transit + "days each week."
fare_feedback = "Gotcha, your one way fare is $" + clean_one_way + "."

print(weeks_feedback)
print(days_feedback)
print(fare_feedback)
