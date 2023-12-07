"""Juggler Sequence is a series of integers in which the first term starts with
a positive integer number a and the remaining terms are generated from the immediate previous term using the below recurrence relation:

Juggler Formula   if a  is  a positive and even integer than a^1/2 but if a is positive and odd integer than a^3/2

Given a number N, find the Juggler Sequence for this number as the first term of the sequence.
Input: 6
Output: 6 2 1
Input: 9
Output: 9 27 140 11 36 6 2 1"""

n=int(input("Enter the Number: "))
sequence=[n]
while n!=1:
    if n%2==0:
        n=int(n**(1/2))
    else:
        n=int(n**(3/2))
    sequence.append(n)
print(sequence)



#using Function
def juggler(n):
    sequence=[n]
    while n != 1:
        if n % 2 == 0:
            n = int(n ** (1 / 2))
        else:
            n = int(n ** (3 / 2))
        sequence.append(n)
    return sequence


num=int(input("Enter the number: "))
result=juggler(num)
print(result)
