n=int(input())
m=0
for k in range(1,n+1):
    m=m+k**2
print(m)


#Using Function
def sum(n):
    s=0
    for k in range(1,n+1):
        s=s+k**2
    return s
p=sum(3)
print(p)