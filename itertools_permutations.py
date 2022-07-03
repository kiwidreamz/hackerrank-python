# You are given a string S. Your task is to print all possible permutations of size k of the string in lexicographic sorted order.


from itertools import permutations

a = [str(x) for x in input().split()]
number = a[1]
letters = a[0]

p = permutations(letters, int(number))

output = ["".join(i) for i in p]
output.sort()
print("\n".join(output))
