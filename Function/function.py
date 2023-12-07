#Takes nothing  return nothing
def f1():
    for i in range(1,8,1):
        print(i**2,end=' ')

f1()


print()
#Take somthing return nothing
def f1(a,b):
    c=a+b
    print(c)
f1(10,20)



#Takes nothing return something
def sum():
    a=5
    b=6
    c=a+b
    return c
sum()


#Takes something return nothing
def add(a,b):
    c=a+b
    return c
add(10,20)

#OR
def add(a,b):
    c=a+b
    return c
k=add(20,22)
print(k)


#Default Argument
def add(a=0,b=0,c=0):
    d=a+b+c
    print(d)

add()
add(10)
add(10,30)
add(10,20,30)

#This will not return value if it dont get argument
def add(a,b,c):
    d = a + b + c
    print(d)

'''add()
add(10)
add(10, 30)'''
add(10, 60, 30)  #in this case only is right


#Positional Argument
def f(a,b):
    print(a,b)
f(4,3)
f(b=4,a=3)
f(3,b=2)    #this is posible
#f(a=3,3)     #this will give error because it is wrong by syntax