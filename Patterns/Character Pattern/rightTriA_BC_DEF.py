#1st Method
n=int(input("Enter Number: "))
char='A'
for i in range(n):
    for j in range(i+1):
        print(char,end=' ')
        char=chr(ord(char)+1)
    print()

#2nd Method
n=int(input("Enter Number: "))
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
        p+=1
    print()