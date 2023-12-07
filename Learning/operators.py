#Arithimatic Operation
print(11/3)     #Normal Division
print(3.4/2)
print(2.5//2.1)  #Datatype Division
print(2.5//2)
print(21%2)    #modulus (reminder)
print(4+3)     #addition
print(4-3)     #subtraction
print(4*3)     #multiplication
print(4**3)     #power

print("-----------")
#Logical Operation
print(4 and 3)     #Logical and comprision
print(4 or 3)     #Logical or comprision
print(not 4)      #Logical not comprision

print("Sheeta" or "Geeta")
print("Sheeta" and "Geeta")

print("-----------")
#Relational Operation
print(4>3)    #Greater than
print(4<3)    #Smaller than
print(4<=3)    #Smaller than Equals to
print(4>=3)    #Greater than Equals to
print(4==3)    #Equals to Equals to
print(4!=3)    #Not Equals to


print("-----------")
#Bitwise Operator
x=3
y=4
print(x&y)     #Bitwise AND Operator
print(x|y)     #Bitwise OR Operator
print(~x)      #Bitwise NOT Operator
print(x^y)     #Bitwise XOR Operator
print(x>>y)    #Bitwise right shift Operator
print(x<<y)    #Bitwise left shift Operator

print("-----------")
#Assingment Operator
a=8
a+=5     #a=a+5
print(a)
a-=5     #a=a-5
print(a)
a*=5     #a=a*5
print(a)
a/=5     #a=a/5
print(a)
a%=5     #a=a%5
print(a)
a**=5     #a=a**5
print(a)

print("-----------")
#Identity Operators
x=10
y=10
print(id(x))
print(id(y))
print(x is y)  #By This we can say both are refering same object that why we get same id of both and get answer TRUE

x=5
y=8
print(id(x))
print(id(y))
print(x is y)  #By This we can say both are refering different object that why we dont get same id of both and get answer FALSE

x=5
y=8
print(id(x))
print(id(y))
print(x is not y)  #By This we can say both are refering different object that why we get differnt id of both and is not operator satisfied condition

print("-----------")
#Membership Operators
y="Aditya"
x="di"
z="op"
print(x in y)
print(x in z)

"""
this is not allowed because you cant iterate into any integer
x=4345
y=4
print(x in y)
"""
y="Aditya"
x="di"
z="op"
print(x not in y)
print(x not in z)
