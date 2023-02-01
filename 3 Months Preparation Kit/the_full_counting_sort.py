#!/bin/python3

import math
import os
import random
import re
import sys

def countSort(arr):
    answer = []
    
    # Make first half of array ascii 45 character
    for i in range(int(len(arr)/2)):
        arr[i][1] = "-"
    
    # Sort based on index
    arr.sort(key=lambda x: int(x[0]))
    
    # Append the characters for output
    for z in range(len(arr)):
        answer.append(arr[z][1])
    
    # List into string
    print(' '.join(answer))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
