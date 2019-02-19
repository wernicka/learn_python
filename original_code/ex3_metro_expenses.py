# set variable = one way rush hour fare from Crystal City to Foggy Bottom
one_way = 2.55

# set variable = average one ways per week assuming 2 ways Lyft or 1 WFH
metro_commutes_per_week = 8

# set variable weeks per year that I work assuming 3 weeks vacation
weeks_worked_per_year = 49



print ("One way rush hour fare from Crystal City to Foggy Bottom is $", one_way, ".")
print("The average one ways per week assuming 2 ways Lyft or 1 WFH is", metro_commutes_per_week, ".")
print("The average weeks per year that I work assuming 3 weeks vacation is",weeks_worked_per_year, ".")

# cost of metro commutes per year
print ("The cost of metro commutes per year is $", one_way * metro_commutes_per_week * weeks_worked_per_year, ".")
