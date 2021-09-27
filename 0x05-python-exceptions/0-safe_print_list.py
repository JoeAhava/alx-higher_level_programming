#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        while counter <= x: 
            print(my_list[counter], end='')
            counter += 1

        print('')
    except IndexError:
        pass


if __name__ == "__main__":
    safe_print_list(my_list=[1,2,3,4,5], x=7)
