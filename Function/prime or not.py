def isprime(n):
    for d in range(2,n):
       if n%d==0:
           break
    else:
        return True
    return False

print(isprime(n=int(input())))
