r=input().split()
n,m=int(r[0]),int(r[1])
sum=0
for k in range(n,m+1):
    sum=sum+k
print(sum)

#2nd method  using formula
r=input().split()
n,m=int(r[0]),int(r[1])
sum=int(m*(m+1)/2-n*(n+1)/2+n)
print(sum)
