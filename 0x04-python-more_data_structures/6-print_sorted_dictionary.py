#!/usr/bin/python3
'''
    A function to print a sorted dictionary
'''


def print_sorted_dictionary(a_dictionary):
    for k in sorted(list(a_dictionary.keys())):
        print("{}: {}".format(k, a_dictionary.get(k)))


'''
if not __name__ == "__main__":
    // Execute a test
'''
