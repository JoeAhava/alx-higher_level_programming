#!/usr/bin/python3
def weight_average(my_list=[]):
    div_top = 0
    div_bottom = 0
    result = [item[0] * item[1] for item in my_list]
    for r in result:
        div_top += r
    for x in [i[1] for i in my_list]:
        div_bottom += x
    return div_top / div_bottom if div_bottom > 0 else 0
