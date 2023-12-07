t=(2,4,6,8,5)
print(t[1])
print(t[-2])
#print(t[6])   #it will give error

i=0
while(i<len(t)):
    print(t[i],end=' ')
    i+=1

print()

for e in t:
    print(e,end=' ')