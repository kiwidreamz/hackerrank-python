#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    
    min_array = arr.copy()
    max_array = arr.copy()

    min_array.pop()
    max_array.pop(0)

    min_total = sum(min_array)
    max_total = sum(max_array)
    
    print(min_total, max_total)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    
    miniMaxSum(arr)
