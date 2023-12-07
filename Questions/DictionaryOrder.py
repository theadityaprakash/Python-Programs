s="patna"
s1="kolkata"
s2="mumbai"

#1st method
"""if s<s1<s2 :
        print(s2)
elif s>s1>s2 :
        print(s)
else:
        print(s1)"""

#2nd method
x=min(s,s1,s2)
if x==s:
        print(x,min(s1,s2),max(s1,s2))
elif x==s1:
        print(x,min(s,s2),max(s,s2))
else:
        print(x,min(s,s1),max(s,s1))