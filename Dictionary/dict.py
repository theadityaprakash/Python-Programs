d={101:'Aditya',102:'Sumedha',103:'Khushboo',104:'Suman'}

print(d)   #print dict
print(d[102])   #print element at particular key

#print only key
for i in d:
    print(i)

#print only value
#method 1st
for i in d:
    print(d[i])
#method 2nd
print(d[101],d[102],d[103],d[104])     #print in single line


#print key and value both
for k in d:
    print(k,d[k])


#for changing any key value
d[104]="Shakti"
print(d)

#for adding any key and value
d[108]="Vishnu"
print(d)

#for adding any key and value
del d[108]
print(d)
