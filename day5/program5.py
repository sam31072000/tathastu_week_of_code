L =list(map(int,input("Enter the list: ").split()))
l1 = []
l2 = []
for i in range(len(L)):
	if (L[i]%2==0):
		l1.append(L[i])
	else:
		l2.append(L[i])
print(l1, l2)
l1.sort()
l2.sort(reverse=True)
l1.extend(l2)
print("The resultant list is: ",*l1)
