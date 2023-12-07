s='Aditya'
s1='sumedha'
s2='Studing in library'

'''
#------Built in Method-----------------
print(len(s))
print(max(s))
print(min(s))
print(sorted(s))

#-------Comprasion Operator-------------
print(s==s1)
print(s<=s1)
print(s>s1)
print(s<s1)
print(s!=s1)
print(s>=s1)
'''
#-----------------Object Method----------
print(s.index(s))
print(s2.count('i'))
print(s.startswith('i'))   #it give True False
print(s2.endswith('y'))
print(s2.split('   '))         #it will return in list
#print(s2.join())
print(s2.isdigit())
print(s2.isupper())
print(s2.islower())
print(s.lower())
print(s.upper())
print(s.replace('a','A'))       #This will convert only one letter
print(s2.replace('i','I',s2.count('i')))     #this will convert all