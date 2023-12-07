"""
#Arthematic number
n=int(input("Enter the num of term : "))
a=int(input("Enter the Starting Number: "))
d=int(input("Enter the difference: "))
sum=0
for i in range(n+1):
    sum=sum+a
    a+=d
print(sum)


#find the sum of Series 9+13+17.....n
a=9
n=int(input("Enter the term: "))
sum=0
for i in range(n+1):
    sum=sum+a
    a+=4
print(sum)

#Find the sum of series 2+4+6+8.....+20
a=2
for i in range(n+1):
    sum=sum+a
    a+=2
print(sum)


#Find the sum of series 10+9+8+7+6.....+1
a=10
n=int(input("Enter the num: "))
sum=0
for i in range(1,n+1):
    sum=sum+a
    a-=1
print(sum)


#find the sum of series 2^x + 3^x + 4^x.....20^x
sum=0
a=2
n=10
x=int(input("Enter the value of power: "))
for i in range(1,n+1):
    sum = sum+a**x
    a+=1
print(sum)


#find the sum of series 1/x + 3^3/x + 5^3/x + .....n
sum=0
n=int(input("Enter the num of term: "))
x=2
a=2
for i in range(1,n+1):
    sum=sum+(a**3/x)
    x+=1
    a+=1
print(sum)
"""

#find the sum of series 2/10 + 4/9 + 6/8 + 8/7 + 20/1
sum=0
n=int(input("Enter the value: "))
a=20
b=10
for i in range(1,n+1):
    sum = sum + a/b
    a+=1
    b-=1
print(sum)





































