#!/usr/bin/python3
for c in range(122, 96, -1):
    print("{:s}".format(chr(c) if (c % 2 == 0) else chr(c - 32)), end='')
