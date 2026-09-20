
import random

def password_generator():
    lower_alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    upper_alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '<', '>', '?', '/', '|', '~', '`')

    print('password generator')
    length = int(input("How long should the password be ? (6-32) :"))
    if length < 6 or length > 32:
        print('invalid choice')
    else:
        print(f'Generating a strong {length} digits password :')

        upper = random.choice(upper_alphabet)
        lower = random.choice(lower_alphabet)
        symbol = random.choice(symbols)
        number = random.choice(numbers)
        all = upper_alphabet + lower_alphabet + symbols + numbers
        password = upper + lower + symbol + number
        for i in range(length - 4):
            password += random.choice(all)

        print(password)
password_generator()

while True:
    pass2 = input('generate more? (y/n) :').lower()
    if pass2=='n':
        print('Thank you for using our generator')
        break
    elif pass2=='y':
        password_generator()
    else:
        print('Invalid input')
