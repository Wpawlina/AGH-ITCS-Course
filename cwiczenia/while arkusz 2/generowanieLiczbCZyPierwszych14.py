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


def ile_jedynek_bin(n):
    ile=0
    while n!=0:
        ile+=n%2
        n//=2
    return ile
def ileCyfr(n):
    if n==0:
        return 1
    ile=0
    while n!=0:
        n//=10
        ile+=1
    return ile
def zlaczLiczby(num1,num2,m):
    wynik=0
    p=0
    while m!=0:
        d=m%2
        if d==1:
            wynik+=(num1%10)*(10**p)
            num1//=10
        else:
            wynik+=(num2%10)*(10**p)
            num2//=10
        m//=2
        p+=1
    return wynik+num2*(10**p)




def generuj(num1,num2):
    ileJedynek=ileCyfr(num1)
    n=ileCyfr(num1)+ileCyfr(num2)
    maxMaska=2**n
    for m in range(1,maxMaska):
        if ile_jedynek_bin(m)==ileJedynek:
            liczba=zlaczLiczby(num1,num2,m)
            if pierwsza(liczba):
                print(liczba)
               



        











num1=81
num2=91
generuj(num1,num2)

