#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("{} is not an integer".format(value))
        return False

if __name__ == "__main__":
    safe_print_integer("1")
