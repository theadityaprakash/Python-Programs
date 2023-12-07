n=int(input("Enter Number: "))
for a in range(n):
    for b in range(a+1):
        print(" ",end=' ')
    for b in range(a,n):
        print("*",end=' ')
    for b in range(a,n-1):
        print("*",end=' ')
    print()

for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()