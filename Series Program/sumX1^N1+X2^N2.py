n=int(input("enter the num of term: "))
a=int(input("Enter the number: "))
p=int(input("Enter the power: "))

sum=0
for i in range(1,n+1):
    sum=sum+(a**p)
    a+=2
    p+=1
print(sum)