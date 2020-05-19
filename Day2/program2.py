def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        print(a,end=" ")
        return
    elif n == 1:
        print(b,end=" ")
        return
    else:
        print(a,b,end=" ")
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
            print(c,end=" ")
        return
n = int(input("Enter the number: "))
print("The fibonacci series is:")
fibonacci(n)
