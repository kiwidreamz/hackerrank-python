#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    
    while True:
        reduced = False
        new_s = ""
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i] == s[i+1]:
                reduced = True
                i += 2
            else:
                new_s += s[i]
                i += 1
        if not reduced:
            return new_s or "Empty String"
        s = new_s
    
    # Works but times out
    """
    while len(s) > 2:
        if s == "".join(set(s)):
            return s
        for i in range(len(s)):
            try:
                if ord(s[i]) == ord(s[i+1]):
                    s = s.replace(s[i+1],"", 1)
                    s = s.replace(s[i],"", 1)
            except IndexError:
                    pass
        
    return "Empty String"
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
