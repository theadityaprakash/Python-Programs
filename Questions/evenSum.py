x=int(input("Enter num: "))
y=1
temp=0
k=0
while(y<=x):
    if(y%2==0):
        temp=temp+y
    y+=1
k=k+temp
print(k)