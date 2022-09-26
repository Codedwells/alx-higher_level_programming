#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_up = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_up.append(True)
        elif my_list[i] % 2 != (0):
            list_up.append(False)
    print(list_up)
    return list_up
