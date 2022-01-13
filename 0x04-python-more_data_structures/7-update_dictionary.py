#!/usr/bin/python3
'''
    A function to update dictionary
'''


def update_dictionary(a_dictionary, key, value):
    '''
    for k in sorted(list(a_dictionary.keys())):
        print("{}: {}".format(k, a_dictionary.get(k)))
    '''
    a_dictionary.update({key: value})
    return a_dictionary


'''
if not __name__ == "__main__":
    // Execute a test
'''
