#sum of x^1+x^2+x^3....x^n
n=int(input("Enter the number of Digit: "))
num=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum=sum+num**i
    i+=1
print(sum)