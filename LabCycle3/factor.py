num=int(input("Enter the number:"))
def factor(n):
    for i in range(1,n+1):
        if n%i==0:
        print(i)
        factor(n)

