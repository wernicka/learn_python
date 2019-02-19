# Practice project from Automate the Boring Stuff chapter 3
def collatz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1

try:
    n_to_be_collatzed = int(input("Type a number:"))
    while n_to_be_collatzed != 1:
        print(collatz(n_to_be_collatzed))
        n_to_be_collatzed = collatz(n_to_be_collatzed)
except ValueError:
    print("Error:you must enter an integer.")

#try making this a recursive function

#hello world of recursive functions is a fibonacci function
