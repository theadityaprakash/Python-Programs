for i in range(5):
    for j in range(1,5-i+1):
        print("*",end=' ')
    print()


#Taking input
n=int(input("Enter Number: "))
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()