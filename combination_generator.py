#!/bin/python.exe

import itertools

def convert_tuple_to_ss_string(tup):
    ret = ""

    for i in tup:
        ret += str(i) + " "

    return ret

def run_test():
    elements = [1, 2, 3]
    for L in range(0, len(elements)+1):
        for subset in itertools.combinations(elements, L):
            print(subset)

            ret = convert_tuple_to_ss_string(subset)
            print(ret)


## test harness
run_test()