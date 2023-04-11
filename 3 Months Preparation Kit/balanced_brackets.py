#!/bin/python3

import math
import os
import random
import re
import sys

def isBalanced(s):
    
    stack = []
    for c in s:
        if c in ["(", "[", "{"]:
            stack.append(c)
        elif c in [")", "]", "}"]:
            if not stack:
                return "NO"
            last = stack.pop()
            if (c == ")" and last != "(") or (c == "]" and last != "[") or (c == "}" and last != "{"):
                return "NO"
    if stack:
        return "NO"
    return "YES"
    
    # Checks for symetry
    """
    for i in range(len(s)//2):
        print(s[i])
        print(s[-(i+1)])
        if ord(s[i]) == 40 and ord(s[-(i+1)]) == 41:
            pass
        elif ord(s[i]) == 91 and ord(s[-(i+1)]) == 93:
            pass
        elif ord(s[i]) == 123 and ord(s[-(i+1)]) == 125:
            pass
        else:
            return "NO"
    return "YES"
	"""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()