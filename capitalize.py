#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    
    if s[0].isalpha():
        first = chr(ord(s[0])-32)
        s = first + s[1:]
    
    for i in range(len(s)):
        if s[i] == " ":
            if s[i+1].isalpha() and 96 < ord(s[i+1]) < 123:
                next_up = chr(ord(s[i+1])-32)
                s = s[:i+1] + next_up + s[i+2:]
                
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
