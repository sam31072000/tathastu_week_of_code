from itertools import permutations
s = input("Enter a number: ")
p = list(permutations(s))
for i in p:
    print(*i,sep="")
