n=int(input("Enter year: "))
print("leap year") if n%400==0 or n%100!=0 and n%4==0 else print("Not leap")
