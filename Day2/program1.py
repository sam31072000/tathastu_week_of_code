n=int(input("Enter a number: "))
if(n%2==0):
    print("Number is even")
else:
    print("Number is odd")
if str(n) == str(n)[::-1]:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
for i in range(2,n//2):
    if n%i==0:
        print("Number is not prime")
        break
else:
    print("Numberis prime")
s=0
for i in range(len(str(n))):
    r = int(str(n)[i])
    s += r*r*r
if s==n:
    print("Number is armstrong")
else:
    print("number is not a armstrong")
