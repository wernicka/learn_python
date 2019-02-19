

weeks = ["How many weeks were you on vacation or leave this year? ", 52, "clean_weeks_vacation", "weeks_feedback"]

days = ["""Think about how many days per week you work from home, carpool, bike, or rideshare.
So how many days per week do you typically take public transit? """, 7, "clean_days_public_transit", "days_feedback"]

fare = ["""Go to wmata.com and calculate your one way fare.
Make sure it's the rush hour fare if you commute during rush hour.
Enter that value here: """, 100, "clean_one_way", "fare_feedback"]

allData = [weeks, days, fare]

for i in allData:
  print(i)
