l = input("Enter the list: ").split()
n = int(input("Enter the nth number: "))
m = sorted(l[n-1:])
print("The sorted list at nth letter: ",l[:n-1]+m)
