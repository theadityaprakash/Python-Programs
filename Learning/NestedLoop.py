#For loop
for k in ['apple','orange']:
    for i in ['red','yellow']:
        print(k," ",i)

#Nested for loop in one line
[print(k," ",i) for k in ['apple','orange']  for i in ['red','yellow']]


#while loop
i=1
j=1
while i<=3:
    while j<=3:
        print(i," ",j)
        j+=1
    i+=1