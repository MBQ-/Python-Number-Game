# Loosely based on this tutorial: http://inventwithpython.com/chapter4.html

import random

# Variable for how many guesses have been taken. Dynamically changes
guessesTaken = 0

# Printing text that will initially pop up to essentially greet you
print('Hello! What is your name?')

# myName will be the variable based on the input of the users name
myName = input()

# the number is the initial variable, random.randint is the random integer alongside the random numbers, 1-20
number = random.randint(1, 20)
# Now let's print some more text so the user knows what's going on
print('Well, ' + myName + ', Im thinking of a number between one and twenty.')

# Next
