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
        


def CzyKomplementarna(t,i,j):
    n=len(t)
    num=t[i][j]
    for r in range(n):
        for c in range(n):
            if r!=i or c!=j:
                if isPrime(num+t[i][j]):
                    return True
    return False
def zad13(t):
    n=len(t)
    for i in range(n):
        for j in range(n):
            if not CzyKomplementarna(t,i,j):
                t[i][j]=0
    return t


