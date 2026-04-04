#!/usr/bin/python3
def print_last_digit(number):
    temp = number
    if number >= 0:
        temp = number % 10
    else:
        temp = (number * -1) %10 
    print("{:d}.format(temp), end="")
    return temp
