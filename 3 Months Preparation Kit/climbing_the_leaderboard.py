#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

def climbingLeaderboard(ranked, player):
    result = []
    
    distinct = sorted(set(ranked), reverse=True)
    distinct.append(0)
    
    j = len(distinct) - 1 
    for p in player:
        while j >= 0 and p >= distinct[j]:
            j -= 1 
        result.append(j + 2)
        
    # Exceeds time limit
    """
    for i in range(len(player)):
        for j in range(len(distinct)):
            if distinct[j] > player[i]:
                pass
            elif distinct[j] == player[i]:
                result.append(j+1)
                break
            elif distinct[j] < player[i]:
                result.append(j+1)
                distinct.append(player[i])
                distinct = sorted(distinct, reverse=True)
                distinct = list(dict.fromkeys(ranked))
                break
    """
    
    return result
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
