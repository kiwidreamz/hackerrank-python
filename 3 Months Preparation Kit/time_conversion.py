#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    if s[8] == "A":
        if s[0] == "1" and s[1] == "2":
            s = s[2:-2]
            s = ''.join(("00", s))
            return s
        else:
            s = s[:-2]
            return s
    else:
        if s[0] == "1" and s[1] == "2":
            s = s[:-2]
            return s
        else:
            hours1 = (int(s[0])) + 1
            hours2 = (int(s[1])) + 2
            s = s[2:-2]
            s = ''.join((str(hours1), str(hours2), s))
            return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
