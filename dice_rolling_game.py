import random
print('Welcome to the game user.\nYou gotta roll a sum of 7 to win\n')
while True:

    start = input("Roll the dice ? (y/n)- ").lower()
    if start == "n":
        print("Thanks for playing")
        break
    elif start == "y":
        die1= random.randint(1, 6)
        die2= random.randint(1, 6)
        print(f"(You rolled {die1} and {die2})")
        if die1 + die2 == 7:
            print("you won")
        else :
            print('Better luck next time')
    else:
        print("Invalid choice.")



