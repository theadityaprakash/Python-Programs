import math as m
n=int(input("Enter the num of term: "))
x=int(input("Enter the term: "))
sum=0
for i in range(1,n+1):
    sum=sum+m.factorial(x)
    x+=1
print(sum)


#Calculate x1/5 + x2/5 + x3/5
n1=int(input("Enter the num of term: "))
x1=int(input("Enter the term: "))
sum=0
for i in range(n1):
    sum=sum+m.factorial(x1)/5
    x1+=1
print(sum)