#find the sum of series 2+4+8+16+....N
sum=0
n=int(input("Enter the sum: "))
a=2
for i in range(n):
    sum=sum+a
    a=a*2
print(sum)


#find the sum of x/2 + x/4 + x/8 + x/16 +....N
sum =0
n=int(input("Enter the number: "))
x=12
d=2
for i in range(n):
    sum=sum+x/d
    x+=4
    d=d*2
print(sum)


#find the sum of series x+2/10 + x+4/30 + x+6/90 +......+N
x=2
n=20
d=10
n=int(input("Enter the number of term: "))
sum=0
for i in range(n):
    sum=sum+((n+x)/d)
    x+=2
    d=d*3
    print(sum)
print(sum)

