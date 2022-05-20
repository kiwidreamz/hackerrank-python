# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i belongs to A, you add 1 to your happiness. If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# Enter your code here. Read input from STDIN. Print output to STDOUT

n_m = input()
array = input().split()
A = set(input().split())
B = set(input().split())

scoreA = 0
scoreB = 0

for i in array:
    if i in A:
        scoreA = scoreA + 1
    if i in B:
        scoreB = scoreB + 1

print(scoreA - scoreB)
