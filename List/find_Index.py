l=[2,4,5,7,3,21,54,9]

#1st method
i=l.index(21)
print(i)

#2nd method
print(l.index(5))

#using condition
k=l.index(100) if 100 in l else 'not found'
print(k)