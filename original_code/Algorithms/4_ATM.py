# Providing the right denomination from ATM.
# Example - 
# Given the following current state of the ATM - 
# CurrencyNote X quantity
# 500x1
# 100x2
# 50x3
# 10x4
# 5x5
# 1x10
#
#
#
# Say, you need to take out $125
# then 125 should be dispensed as such - 
# 125 -> 100 + 10x2 + 5x1
#
#
# Leaving the state of the machine like this → 
# 500x1
# 100x1
# 50x3
# 10x2
# 5x4
# 1x10
#
#
# Now, 
# 225 - can dispense
# 325- can't dispense
#
#
# Problem -  Given the current state of the ATM as an input dictionary given below, see whether a given particular
# amount can be dispensed or not by the machine. Update the state of the machine. Return true if amount can be
# dispensed, otherwise false.
#
#
# Example input - 
# input dictionary
# Keys, Value
# 500,1
# 100,2
# 50,3
# 10,4
# 5,5
# 1,10

machine_state = {500:1, 100:2, 50:3, 10:4, 5:5, 1:10}

dispense_amount = 125

def can_dispense(machine_state, dispense_amount):
    largest_key = 0
    for key, value in machine_state:
        if value > 0:
            if key > largest_key:
                largest_key = key
    

    what is the largest key with a value greater than 1 that can go into the input? aka that the input is divisible by
    while loop?
    If the largest key can be subtracted from the input number without going lower than 0, then do that and move on to
    the next largest key that can be subtracted from the new value.

    Do I need to make a list that orders the keys so that I test the largest key first?

