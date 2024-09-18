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
def binToDec(n):
    x=n
    p=0
    l=0
    while x!=0:
        dig=x%10
        l+=dig*2**p
        p+=1
        x//=10
    return l

def zad5(T):
    n=len(T)
    value=False
    def rek(i,ciag,dl):
        nonlocal value
        if i==n:
            if isPrime(binToDec(ciag)):
                value=True
            return
        if isPrime(binToDec(ciag)):
            rek(i+1,T[i],1)
            if value==True:
                return
            if dl <30:
                rek(i+1,ciag*10+T[i],dl+1)
        else:
            if dl <30:
                rek(i+1,ciag*10+T[i],dl+1)
    rek(0,0,0)
    return value
print(zad5([1,1,0,1,0,0]))
            



