#1st method using ASCII value
n=int(input("Enter Number : "))
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()

#2nd method4
n=int(input("Enter Number : "))
p='A'
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    p=str(chr(ord(p)+1))
    print()