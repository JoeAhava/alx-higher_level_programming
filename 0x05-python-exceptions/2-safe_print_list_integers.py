#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            counter += 1
        except (ValueError, TypeError):
            pass

    print()
    return counter


if __name__ == "__main__":
    safe_print_list_integers(my_list=[1, 2, 3, "School", 4, 5, [1, 2, 3]], x=7)
