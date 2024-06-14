#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # loop through each number from 1 to n (inclusive).
    for i in range(1, n + 1):
        # check if the number is divisible by both 3 and 5.
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # check if the number is divisible by 3.
        elif i % 3 == 0:
            print("Fizz")
        # check if the number is divisible by 5.
        elif i % 5 == 0:
            print("Buzz")
        # if the number is not divisible by 3 or 5, print the number itself.
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
