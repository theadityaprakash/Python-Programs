"""Given a number x, your task is to find if this number is Deficient number or not.
A number x is said to be Deficient Number if sum of all the divisors of the number denoted by divisorsSum(x)
is less than twice the value of the number x.
And the difference between these two values is called the deficiency.

Input: x = 21
Output: YES
Explanation: Divisors are 1, 3, 7 and
21.Sum of divisors is 32.
This sum is less than 2*21 or 42."""

n = int(input("Enter the number: "))
factor = []
for i in range(1, n + 1):
    if n % i == 0:
        factor.append(i)
ElementSum = sum(factor)

if ElementSum < 2 * n:
    print("True")
else:
    print("False")

#Using Function
def DeficientNum(n1):
    factor=[]
    for i in range(1, n1+1):
        if n1%i==0:
            factor.append(i)
    ElementSum=sum(factor)

    if ElementSum<2*n1:
        return True
    else:
        return False

num=int(input("Enter the Number: "))
print(DeficientNum(num))
