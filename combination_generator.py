#!/bin/python.exe

import itertools

elements = [1, 2, 3]
for L in range(0, len(elements)+1):
    for subset in itertools.combinations(elements, L):
        print(subset)
        print(":")

        for i in subset:
            print(str(i) + " " )
