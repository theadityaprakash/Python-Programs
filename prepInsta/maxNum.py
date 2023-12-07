#1st method
a=6
b=7
c=9

maxNum=max(a,b,c)
print(maxNum)



#using Function and string  2nd method
def find_max(a, b, c):
    return max(a, b, c)

a = '3'
b = '6'
c = '9'
result = find_max(a, b, c)
print(int(result))



#without function using string
a='3'
b='6'
print(int(max(a,b)))


