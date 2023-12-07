#1st Method
a=6
b=5
print(a+b)

#This will happen because Python take input in String
a=input()
b=input()
c=a+b
print(c)      #if a=10  b=10  Output will be 1010

#2nd method Taking input from User
a=int(input())
b=int(input())
c=a+b
print(c)

#3rd method
a,b=(int(input())),(int(input()))
c=a+b
print(c)