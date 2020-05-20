n=int(input("Enter the number:\n"))
for i in range(n,0,-1):
	for j in range(0,i*2-1):
		print(i if j%2==0 else "*" ,end="")
	print()
for i in range(1,n+1):
	for j in range(0,i*2-1):
		print(i if j%2==0 else "*", end="")
	print()
