#Using Function
def oddEven(n):
    if n%2==0:
        return True
    else:
        return False
k=oddEven(int(input("Enter the number: ")))
if k:
    print("Even")
else:
    print("Odd")


#Using Ternary operator
n=int(input("Enter the Number: "))
print("even") if n%2==0 else print("Odd")