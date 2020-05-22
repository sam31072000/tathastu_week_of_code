l = list(map(int, input("Enter the list").split()))
for i in range(len(l)-1):
	l[i]=max(l[i+1:])
print(l)
