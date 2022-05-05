# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# reading input
a = input()
b = input().split()

c = input()
d = input().split()

# initializing sets
set1 = set()
set2 = set()

# adding inputs to sets
for i in range(len(b)):
    set1.add(b[i])
    
for j in range(len(d)):
    set2.add(d[j])

# getting the differences
result1 = set1.difference(set2)
result2 = set2.difference(set1)

# traslating to a list
b2 = list(map(int, result1))
d2 = list(map(int, result2))

# appending to one list
for i in d2:
    b2.append(i)
    
b2.sort()

for i in b2:
    print(i)
