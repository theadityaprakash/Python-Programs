#Remove duplicate element from the list
L=[2,4,5,4,2,4,3]
s=list(set(L))
print(s)


#taking input from the user
L1=list(set([int(x) for x in input("Enter the Elements: ").split(',')]))
print(L1)