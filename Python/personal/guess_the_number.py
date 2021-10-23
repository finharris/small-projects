import random
import sys

rand_number = random.randint(1, 100)

guess1 = int(input("You have 5 guesses to guess the number between 1 and 100.\n\nWhat is your first guess? "))
if guess1 == rand_number:
    print("Well done! You got it on your first guess!")
    sys.exit(0)
elif guess1 > rand_number:
    print("This is a bit too high, try something lower.")
elif guess1 < rand_number:
    print("Too low. Go up a bit.")
else:
    print("Please enter a number or valid input.")


guess2 = int(input("What is your second guess? "))
if guess2 == rand_number:
    print("Whoa! You got it on your second guess!")
    sys.exit(0)
elif guess2 > rand_number:
    print("This is a bit too high, try something lower.")
elif guess2 < rand_number:
    print("Too low. Go up a bit.")
else:
    print("Please enter a number or valid input.")


guess3 = int(input("What is your third guess? "))
if guess3 == rand_number:
    print("Nice! You got it on your third guess!")
    sys.exit(0)
elif guess3 > rand_number:
    print("This is a bit too high, try something lower.")
elif guess3 < rand_number:
    print("Too low. Go up a bit.")
else:
    print("Please enter a number or valid input.")


guess4 = int(input("What is your fourth guess? "))
if guess4 == rand_number:
    print("Cool! You got it on your fourth guess!")
    sys.exit(0)
elif guess4 > rand_number:
    print("This is a bit too high, try something lower.")
elif guess4 < rand_number:
    print("Too low. Go up a bit.")
else:
    print("Please enter a number or valid input.")


guess5 = int(input("What is your fifth guess? "))
if guess5 == rand_number:
    print("Alright! You got it on your last guess!")
    sys.exit(0)
elif guess5 > rand_number:
    print("Your final guess was a bit too high. The correct answer was " + str(rand_number))
elif guess5 < rand_number:
    print("Your final guess was just a little too low. The correct answer was " + str(rand_number))
else:
    print("Please enter a number or valid input.")
