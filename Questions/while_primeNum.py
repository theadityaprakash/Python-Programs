#1st Method
x=int(input())
n=2
while(n<=x-1) :
    if x%n==0:
        break
    n+=1
if n==x:
    print("prime")
else:
    print("not prime")


#2nd Method  we can use else with while

y=int(input())
i=2
while i<=y-1:
    if(y%i==0):
        print("Not Prime")
        break
    i+=1
else:
    print("Prime")