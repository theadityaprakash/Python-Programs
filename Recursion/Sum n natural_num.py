def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
x=sum(int(input("Enter the number: ")))
print(x)