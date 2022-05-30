# You are given a two lists  A and B. Your task is to compute their cartesian product A X b.

from itertools import product

a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]

print(*product(a, b))
