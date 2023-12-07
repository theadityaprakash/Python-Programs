#find sum x*5^2/1+2! + x*25^2/2+3! +....N
import math as m
n=int(input("Enter the term: "))
x=2
n=5
d1=1
d2=2
sum=0
for i in range(n):
    sum=sum+(x*(n**2))/(d1+m.factorial(d2))
    n=n*5
    d1+=1
    d2+=1
    print(sum)
print(sum)
