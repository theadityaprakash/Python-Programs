a=int(input())
b=int(input())
l=max(a,b)
#l=a if a>b else b   (this way you can find which is greater)
while l<=a*b:
    if l%a==0 and l%b==0:
        print(l)
        break
    l+=1
