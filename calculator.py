#!/usr/bin/env python3

print("Simple Calculator")
print("Usage: Enter the calculation expression, ex. '3 + 4'")
print("The result will be printed as '3 + 4 = 7'")
print("To exit the program, type 'exit'")
print("To use the previous answer value, simple type 'ans'")

ans = 0

while True:
    try:
        exp = input("Please enter your expression ")
        if exp == 'exit':
            break
        result = eval(exp)
        ans = result
        print("{} = {}".format(exp, result))
    except (NameError, SyntaxError):
        print("Invalid input")
        print("Usage: 'a (sign) b', ex. '3 + 4'")
