from collections import Counter
t = tuple(input("Enter the elements in tuple: ").split())
c = dict(Counter(t))
print(c)
