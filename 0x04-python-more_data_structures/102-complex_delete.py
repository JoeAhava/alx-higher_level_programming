#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in [k for k in a_dictionary]:
        if a_dictionary.get(key) == value:
            del a_dictionary[key]
    return a_dictionary
