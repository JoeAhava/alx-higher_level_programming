#!/usr/bin/python3
'''
    A function to get a square of a matrix elements
'''


def square_matrix_simple(matrix):
    result = [[y ** 2 for y in x] for x in matrix]
    return result


'''
if not __name__ == "__main__":
    // Execute a test
'''
