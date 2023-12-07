k=input("Enter the Range: ").split()
n,m=int(k[0]),int(k[1])
flag=0
for i in range(n,m+1):
    flag=0
    for j in range(2,i):
        if i % j == 0:
            flag=1
            break
    if flag==0:
      print(i)