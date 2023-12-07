def numb(n):
    if n==0:
        return
    numb(n-1)
    print(n)
    return
numb(int(input()))


#reverse number printing
def revnum(n):
    if n==0:
        return
    print(n)
    revnum(n-1)
revnum(int(input()))