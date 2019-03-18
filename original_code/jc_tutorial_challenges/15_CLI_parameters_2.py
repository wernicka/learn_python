# CLI PARAMETERS 002 - EASY, FUNDAMENTAL
# Write a script that expects a command line argument; if it isn't given one
# it uses a default value.

import sys

name = "Amanda"
characteristic = "smart"

if len(sys.argv)>=2:
    name = sys.argv[1]

if len(sys.argv)>=3:
    characteristic = sys.argv[2]

print(f"{name} is sooooo {characteristic}!")