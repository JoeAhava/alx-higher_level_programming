#!/usr/bin/python3
'''
    A function to add all uniq items
'''


def uniq_add(my_list=[]):
    total = 0
    temp = []
    for index, item in enumerate(my_list):
        if temp.count(item) == 0:
            total += item
            temp.append(item)
    return total


'''
if not __name__ == "__main__":
    // Execute a test
'''
