n=int(input("Enter Number: "))
for i in range(n):
    for k in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print()