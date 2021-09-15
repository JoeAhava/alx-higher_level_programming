#!/usr/bin/python3
roman_constant = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    for c in roman_string:
        if roman_constant.get(c) is None:
            return 0
        result += roman_constant.get(c)
    return result
