num1 = float(input("Enter 1st number - "))

opp = input("enter your operation (eg. +, -, *, % etc) - ")

num2 = float(input("Enter 2nd number - "))


if opp == "+":
    print(num1 + num2)
elif opp == "-":
    print(num1 - num2)
elif opp == "*" :
    print(num1 * num2)
elif opp == "%" :
    print(num1 % num2)
elif opp == "/" :
    print(num1 / num2)
elif opp == "**" :
    print(num1 ** num2)
else:
    print("invalid operation selected")