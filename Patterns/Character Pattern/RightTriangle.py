n=int(input("Enter your Number: "))
for i in range(n):
    for j in range(i+1):
        #print("A",end=' ')       #Both are correct
        print(chr(65),end=' ')
    print()