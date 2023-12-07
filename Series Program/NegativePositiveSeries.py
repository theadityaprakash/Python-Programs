#find the sum of series 2 - 6 + 18 - 24 +......-N
n=int(input("Enter the number of term: "))
sum=0
a=2
for i in range(n):
    if i%2==0:
        sum=sum+a
    else:
        sum=sum-a
    a=a*3
print(sum)