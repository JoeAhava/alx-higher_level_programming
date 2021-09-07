#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    count = 0
    for s in str:
        count += 1
    if count < n:
        copy = str
    else:
        for i in str:
            if i == str[n]:
                continue
            else:
                copy += i

    return copy
