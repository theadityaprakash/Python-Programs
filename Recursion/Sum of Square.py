def sum(n):
    if n==1:
        return 1
    return n*n+sum(n-1)
x=sum(3)
print(x)