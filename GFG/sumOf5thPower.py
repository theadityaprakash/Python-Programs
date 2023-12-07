#Given a number N.Find the sum of fifth powers of natural numbers till N i.e. 15+25+35+..+N5.

n=int(input("Enter the num: "))
series=[i**5 for i in range(1,n+1,1)]
print(series)
sum=sum(series)
print(sum)

