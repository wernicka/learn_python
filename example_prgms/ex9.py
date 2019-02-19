#Learned: two ways to make things print on a new line
# \n makes the thing that follows it appear on a new line
# three sets of quotes surrounding things makes line breaks appear in the printed thing whereever the line break appears in the code

days = "Mon Tue Wed Thur Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months:", months)

print("""
There's somtehing going on here.
With the three double-quotes.
We'll be able to type as much as we likeself.
Event 4 lines if we want, or 5, or 6.
""")
