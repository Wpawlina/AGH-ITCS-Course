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

def generujFibDo(n):
    a=1
    b=1
    wynik=[]
    while b<n:
        wynik.append(b)
        a,b=b,a+b
        
    return wynik

def zad(t,fib):
    n=len(t)
    cnt=0
    for i in range(n):
        if i in fib:
            if pierwsza(t[i]):
                return False
        else:
            if pierwsza(t[i]):
                cnt=1
    if cnt==1:
        return True
    else:
        return False
    
    
        
            


        