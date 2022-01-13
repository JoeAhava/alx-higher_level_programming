#!/usr/bin/python3
'''
    A function to find the best score in a dictionary
'''


def best_score(a_dictionary):
    best = 0
    key = None
    if a_dictionary is None:
        return key
    for k in a_dictionary:
        if a_dictionary.get(k) > best:
            best = a_dictionary.get(k)
            key = k
    return key


'''
if not __name__ == "__main__":
    // Execute a test
'''
