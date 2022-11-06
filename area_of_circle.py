#!/usr/bin/env python3

import math

def calculate_area(radius):
    """
    Calculates the area of a circle
    """
    return math.pi * (radius * radius)

data = ''
print('Program to calculate the area of a circle with a radius!')
print('Enter exit to stop the program')
while True:
    try:
        data = input('Please enter the radius of the circle ')
        if data == 'exit':
            break
        r = eval(data)
        print(calculate_area(r))
    except (NameError, SyntaxError):
        print('Input must be a number')
        continue
