# CLI PARAMETERS 002 - EASY, FUNDAMENTAL
# Write a script that expects a command line argument; if it isn't given one
# it uses a default value.

import sys

if len(sys.argv)>=3:
    print(f"{sys.argv[1]} is sooooo {sys.argv[2]}!")
elif len(sys.argv)==2:
    print(f"{sys.argv[1]} is soooo smart")
else:
    print("Amanda is sooooo smart")

