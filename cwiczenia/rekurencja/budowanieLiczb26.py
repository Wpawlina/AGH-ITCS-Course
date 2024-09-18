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
def binTodec(liczba):
    wynik=0
    x=liczba
    p=0
    while x!=0:
        dig=x%10
        x//=10
        wynik+=dig*2**p
        p+=1
    return wynik

def zad26(A,B):
    ile=0
    def rek(a,b,dl,liczba):
        nonlocal ile
        if dl==A+B:
            if not isPrime(binTodec(liczba)):
                ile+=1
            return
        if a+1<=A:
            rek(a+1,b,dl+1,liczba*10+1)
        if b+1<=B:
            rek(a,b+1,dl+1,liczba*10)
    rek(1,0,1,1)
    return ile
print(zad26(20,30))

