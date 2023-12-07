n=int(input("Enter the number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    i+=1
print(sum)


#negative
sum=0
for i in range(1,n+1):
    sum=sum+i
    i-=1
print(sum)