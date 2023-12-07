n=int(input("Enter Number : "))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=' ')
        j=i+1
    print()