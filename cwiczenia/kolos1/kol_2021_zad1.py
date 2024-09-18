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

def zad1(t):
    n=len(t)
    ip=1
    maxv=0
    maxi=-1
    if pierwsza(t[0]):
        ip*=t[0]
    for i in range(1,n):
        if t[i]==ip:
            if t[i]>maxv:
                maxv=t[i]
                maxi=i 
        if pierwsza(t[i]):
            ip*=t[i]
    return maxi if maxi > 0 else None

t=[2,4,5,7,70,7,2,980,1800]
print(zad1(t))

    
