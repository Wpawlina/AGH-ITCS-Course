
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
def ileCyfr(n):
    return int(log10(n))+1
def zad(n):
    liczba=n
    cnt=0
    def rek(n,num=0,p=0):
        nonlocal cnt
        if n==0:
            if isPrime(num):
                if ileCyfr(num)>=2 and num !=liczba:
                    print(num)
            return
        digit=n%10
        n//=10
        rek(n,num,p)
        rek(n,num+digit*(10**p),p+1)
    rek(n)

print(zad(117))
    
    



