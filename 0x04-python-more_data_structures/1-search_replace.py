#!/usr/bin/python3
'''
    A function to replace all occurrences of
    an element in a list
'''


def search_replace(my_list, search, replace):
    temp = [x for x in my_list]
    for index, item in enumerate(temp):
        if item == search:
            temp[index] = replace
    return temp


'''
if not __name__ == "__main__":
    // Execute a test
'''
