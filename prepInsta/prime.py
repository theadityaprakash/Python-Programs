#1st method
n=int(input("Enter the number: "))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("not prime")
else:
    print("prime")


#Using Function
def isprime(n):
    for i in range(2,n):
          if n%i==0:
              break
    else:
      return True
    return False

k=isprime(n=int(input()))
if k:
    print("prime")
else:
    print("not prime")


#Range of prime
k=input().split()
#n,m=int(k[0]),int(k[1])
flag=0
for i in k:
    if k[i]%i==0:
        flag=1
        break
if flag==1:
    pass
else:
    print(k[i])
