# Ask the person to think for a number
# Guess the number 

import random

num = random.randint(1, 100)

while True:
    guess = int(input("guess the number between 1-100 - "))

    if guess > 100 or guess < 0:
        print('Choose between the given parameters')
        continue
    if guess > num:
        print("High...!!")
        
    elif guess < num:
        print("Low...!!")
        
    elif num == guess :
        print("You won...!!")
        break
    elif guess > 100 :
        print("choose between the given parameters")
    else:
        print("Invalid action")

