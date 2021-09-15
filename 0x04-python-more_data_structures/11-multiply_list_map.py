#!/usr/bin/python3
'''
    A function to multiply by two
    every element in a list
'''


def multiply_list_map(my_list=[],number=0):
    return list(map(lambda x: x * number, my_list))


'''
if not __name__ == "__main__":
    // Execute a test
'''
