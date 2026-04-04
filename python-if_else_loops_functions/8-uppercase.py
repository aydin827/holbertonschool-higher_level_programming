#!/usr/bin/python3
def uppercase(str):
    for c in str:
        temp = c
        if ord(c) >= 97 and ord(c) <= 122:
            temp = chr(ord(c) - 32)
        print("{:s}".format(temp), end="")
    print("")
