#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_add = set(my_list)
    for i in uniq_add:
        result += i
    return result
