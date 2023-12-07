def isprime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True
    return False

def prime(n):
    for d in range(2,n+1):
        is_prime=isprime(d)
        if is_prime:
            print(d)

prime(int(input("Enter the range value: ")))   #prime(n)
