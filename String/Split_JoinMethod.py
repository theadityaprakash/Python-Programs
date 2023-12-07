#----------Split Method-----------
s='Studing in library'
print(s.split(' '))

#Taking User input
n=input("Enter numbers")
l3=n.split(',')
print(l3)

l1=[int(x) for x in l3]      #it will change string list into integer list
print(l1)

#---------join Method-------------
l=['abc','bcd','lmn','pqr']
print(' '.join(l))

l5=['abc','bcd','lmn','pqr']
print('-'.join(l))