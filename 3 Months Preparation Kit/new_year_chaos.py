#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    p = q 
    counter = 0
    
    for i in range(len(p)-1, -1, -1):
        if p[i] - (i+1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, p[i]-2), i):
            if p[j] > p[i]:
                counter += 1
    
    print(counter)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
