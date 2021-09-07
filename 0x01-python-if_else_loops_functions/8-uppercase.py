#!/usr/bin/python3
def uppercase(str):
    for s in str:
        temp = s
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(temp) - 32)
        print("{:s}".format(temp), end='')
    print("")
