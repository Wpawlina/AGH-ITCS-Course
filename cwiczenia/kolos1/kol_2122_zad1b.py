from math import log10

def isPrime(n):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
        if n%i==0:
            return False
        i+=4
    return True
def iloczynSysPrime(n,sys):
    iloczyn=1
    while n!=0:
        d=n%sys
        iloczyn*=d
        n//=sys
    if isPrime(iloczyn):
        return True
    else:
        return False

def ileCyfr(n):
    return int(log10(n))+1

def rotuj(n):
    ile=ileCyfr(n)
    firstDig=n//(10**(ile-1))
    n=n%(10**(ile-1))
    n*=10
    n+=firstDig 

def minSysPrime(n):
    ile=ileCyfr(n)
    for i in range(2,17):
        for _ in range(ile):
            n=rotuj(n)
            if iloczynSysPrime(n,i):
                return True
    return None

    


