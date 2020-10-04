import random
import math

# Inputs for lower number
lower = int(input("Emter Lower bound:- "))

# Inputs for upper number
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # Input guessing number
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ", count, " try")
        # Once guessed, loop will break
        break
        print()
    
    elif x > guess:
       print("You guessed too small!")
    else:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# then this is output.
    if count >= math.log(upper - lower + 1, 2):
      print("\nThe number is %d" % x)
      print("\tBetter Luck Next time!")


