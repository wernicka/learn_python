#copied from a website to learn about while, if, and break

# import library called random random
import random
#set n to 20
n = 20
#set number user will guess to n times a random number plus 1
to_be_guessed = int(n * random.random()) + 1
# set variable guess to 0 as the initial test for the while loop's condition
guess = 0
# while guess is not equal to to_be guessed, while loop will continue
while guess != to_be_guessed:
    # get user's guess
    guess = input("New number: ")
    # if the user guesses a number greater than zero
    if guess > 0:
        # if the user guess is larger than the game's number tell them it's too large
        if guess > to_be_guessed:
            print "Number too large"
        #if the user guess is smaller than the game's number (but already checked to be a number greater than 0?), tell them it's too small
        else:
            print "Number too small"
        #while loop starts over
    # program interprets 0, negative number, any non integer guess as giving up ends the program?
    else:
        print "Sorry that you're giving up!"
        break
#when guess user's guess is equal to the random number, print congrats message.
else:
    print "Congratulation. You made it!"
