from math import log10

def ileCyfr(n):
    return int(log10(n))+1
    
def pierwsza(n):
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
def rozneCyfry(n):
    digits=[0]*10
    while n!=0:
        d=n%10
        if digits[d]==1:
            return False
        digits[d]=1
        n//=10
    return True


def zad1(K):
    dl=ileCyfr(K)
    maxp=0
    for m in range(dl-1):
        for n in range(dl-m-1):
            obcieta=K
            obcieta=obcieta%(10**(dl-m))
            obcieta=obcieta//(10**n)
            if pierwsza(obcieta) and rozneCyfry(obcieta):
                maxp=max(maxp,obcieta)
    return maxp

print(zad1(1202742516))



            
           




