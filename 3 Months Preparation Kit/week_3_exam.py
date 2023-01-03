#!/bin/python3

import math
import os
import random
import re
import sys


def getTotalX(a, b):

    print(a)
    print(b)

    first = []
    second = []
    answer = 0
    
    for number in range(1, 100):
        nope = False
        for a_a in a:
            if number%a_a:
                nope = True
        if not nope:
            first.append(number)
            
    for other_number in first:
        nope = False
        for b_b in b:
            if b_b%other_number:
                nope = True
        if not nope:
            second.append(other_number)
            answer = answer + 1
            
    return answer
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
