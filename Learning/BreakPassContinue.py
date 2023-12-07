#Pass
print('Hello')
for i in range(1,6):
    pass
print("thanks")

#Break
for i in range(1,10):
    if(i==7):
        break
    print(i,end=' ')

print()
#Else with for loop
n=int(input("Enter Number Number: "))
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
else:
    print("Its me else")
if flag==1:
    print("not prime")
else:
    print("Prime")

#Continue
for i in range(1,12):
    if i==4:
        continue
    else:
        print(i)