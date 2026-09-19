import random

while True:
    emojis = {
        'r' : 'Rock 🪨',
        'p' : 'paper 📃',
        's' : 'scissor ✂️' }
    choices = ('r', 'p', 's')

    uc = input('Rock, Paper or scissors? (r/p/s) -').lower()
    if uc not in choices:
        print("Invalid choices")
        continue
    else:
        print(f'\nyou choose {emojis[uc]}')

    cc = random.choice(choices)
    print(f'Computer choose {emojis[cc]}')

    if uc == cc:
        print("Tie.\n")
    elif (
        ( uc == 'r' and cc == 's') or
        ( uc == 'p' and cc == 'r') or
        ( uc == 's' and cc == 'p')) :
            print("You win.")

    else :
         print('You lose.')

    again = input('Play again ? (y/n)- ').lower()
    if again == 'y' :
         continue
    else:
         break