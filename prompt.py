#!/usr/bin/env python3

print("Type exit to exit the program")

while True:
    name = input("Please input your name ")
    if name == 'exit':
        break
    dept = input("Please input your department ")
    if dept == 'exit':
        break
    s_exit = False
    while True:
        age = input ("Please input your age ")
        if age == 'exit':
            s_exit = True
            break
        if not age.isdigit():
            print("Age must be a number (literally)")
        else:
            break
    if s_exit:
        break
    print("Your name is {} from the department of {} of age, {}".format(name, dept, age))
