# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns N.
# For example:
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160

def odd_one_out(input_array):
    count_evens = 0
    count_odds = 0
    for item in input_array:
        if item % 2 == 0:
            last_even_value = item
            count_evens +=1
        else:
            last_odd_value = item
            count_odds +=1
    if count_odds > count_evens:
        return last_even_value
    else:
        return last_odd_value

print(odd_one_out([2, 4, 0, 100, 4, 11, 2602, 36]))

print(odd_one_out([160, 3, 1719, 19, 11, 13, -21]))



    # NOTES FROM BEFORE I STARTED CODING
# determine whether each value in array is divisible by two - for loop?
    # store the last odd value and the last even value in variables
    # count up how many are even and how many are odd
    # if count of odd > count of even, return even variable
    # else return odd variable
