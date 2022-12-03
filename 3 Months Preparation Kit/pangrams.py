#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    
    alphabet_list = [0] * 26
    position = 0
    keep_going = True
    
    for letter in s:
        if letter.isalpha():
            
            if ord(letter) < 97:
                position = ord(letter) - 65
            else:
                position = ord(letter) - 97
                
            alphabet_list[position] = 1
        else:
            pass
        
    for i in alphabet_list:
        if i == 0:
            return "not pangram"
        else:
            keep_going = True
    
    if keep_going == True:
        return "pangram"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
