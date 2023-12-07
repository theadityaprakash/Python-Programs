#Accessing Local and Global Variable
a=4    #Global Variable [it can be access from anywhere in program]
def num():
    b=3    #Local Variable  [it can be access only within the assign function]
    print(b)
    print(a)
num()
print(a)
#print(b)   #this is not possible to access local variable outside the function
print("----------------------")


#making global variable inside function
a4=13
def f4():
    global a4
    a4=12
    print((a4))
    print(id(a4))
print(a4)
print(id(a4))
f4()
print(a4)
print(id(a4))