#!/bin/python3

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    counter = 4
    
    if n == 1:
        return 5
    elif n == 2:
        return 4
    elif n == 3:
        return 3
    
    a = False
    b = False
    c = False
    d = False
        
    for i in range(n):
        if password[i].isnumeric():
            a = True
        elif password[i].islower():
            b = True
        elif password[i].isupper():
            c = True
        elif password[i] in "!@#$%^&*()-+":
            d = True
    
    if a:
        counter -= 1
    if b:
        counter -= 1
    if c:
        counter -= 1
    if d:
        counter -= 1
    
    if counter + n < 6:
        while counter + n != 6:
            counter += 1
        
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
