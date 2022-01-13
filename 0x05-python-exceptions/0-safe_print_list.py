#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        while counter < x:
            print("{}".format(my_list[counter]), end='')
            counter += 1

    except IndexError:
        pass

    print("", end='\n')
    return counter


if __name__ == "__main__":
    safe_print_list(my_list=[1, 2, "3", -1, 0.1], x=7)
