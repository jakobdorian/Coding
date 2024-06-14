#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    
    cpos = 0
    cneg = 0
    czero = 0
    
    for num in arr:
        if num > 0:
            cpos += 1
        elif num < 0:
            cneg += 1
        else:
            czero += 1
    
    print(f"{cpos / n:.6f}")
    print(f"{cneg / n:.6f}")
    print(f"{czero / n:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
