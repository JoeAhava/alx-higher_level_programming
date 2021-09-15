#!/usr/bin/python3
'''
    A function to get all common items
'''


def common_elements(set_1, set_2):
    return {x for x in set_1 if x in set_2}


'''
if not __name__ == "__main__":
    // Execute a test
'''
