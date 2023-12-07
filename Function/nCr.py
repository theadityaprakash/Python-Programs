def facto(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a

n=int(input("Enter value of n: "))
r=int(input("Enter value of r: "))
n_fact=facto(n)
r_fact=facto(r)
n_r_fact=facto(n-r)
ncr=n_fact//(r_fact*n_r_fact)
print(ncr)