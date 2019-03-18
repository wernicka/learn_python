# CLI PARAMETERS 003 - EASY, FUNDAMENTAL
# Write a  script that takes more than one command line argument and does
# something with them.  If they're not there, it should fail gracefully and
# provide guidance

import sys

user_inputs = sys.argv

if len(user_inputs)>3:
    print("Please provide only 2 parameters: name and characteristic")
elif len(user_inputs)==3:
    print(f"{user_inputs[1]} is sooooo {user_inputs[2]}!")
else:
    print("Please provide the name of the person as the first parameter and the characteristic you're praising as the second parameter")