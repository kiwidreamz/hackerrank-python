#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    new_string = ""
    
    while k > 26:
        k = k - 26
    
    for i in s:
        if not i.isalpha():
            new_string = new_string + i
        elif 64 < ord(i) < 91:
            new_letter = (ord(i) - 65) + k 
            p = new_letter + 65
            if p < 91:
                new_string = new_string + chr(p)
            else:
                z = p - 26
                new_string = new_string + chr(z)
        else:
            new_letter = (ord(i) - 97) + k 
            p = new_letter + 97
            if p < 123:
                new_string = new_string + chr(p)
            else:
                z = p - 26
                new_string = new_string + chr(z)
    
    return new_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
