n=int(input("Enter Number : "))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=' ')
    i+=1
    print()
