#!/usr/bin/python3
def uppercase(str):
    for c in str:
        temp_char = c
        if ord(c) >= 97 and ord(c) <= 122:
            temp_char = chr(ord(c) - 32)
            print("{:s}".format(temp_char), end="")
   

    print("")            
