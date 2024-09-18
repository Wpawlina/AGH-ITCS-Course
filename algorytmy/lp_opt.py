from math import sqrt
def is_prime(n):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i<=sqrt(n):
        if n%i==0:
            return False
        i+=2
        if n%i==0:
            return False
        i+=4

    return True

print(is_prime(121))