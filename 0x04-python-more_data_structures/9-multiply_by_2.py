#!/usr/bin/python3
'''
    A function to multiply each value by 2 in a dictionary
'''


def multiply_by_2(a_dictionary):
    temp = {}
    for k, v in a_dictionary.items():
        temp[k] = v * 2
    return temp


'''
if not __name__ == "__main__":
    // Execute a test
'''
