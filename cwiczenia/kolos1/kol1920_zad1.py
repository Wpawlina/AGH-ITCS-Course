def sumaKawalka(T):
    n=len(T)
    sum=0
    for i in range(n):
        sum+=T[i]
    return sum
def czyPotega(n):
    if n==1:
        return True
    i=2
    while i*i<=n:
        nCopy=n
        while nCopy%i==0:
            nCopy//=i
        if nCopy==1:
            return True
    return False

def zad1(t1,t2):
    n=len(t1)
    for l1 in range(1,24):
        l2=24-l1
        for i in range(n-l1+1):
            kawalek1=t1[i:i+l1]  
            for j in range(n-l2+1):
                kawalek2=t2[i:i+l2]
                suma=sumaKawalka(kawalek1)+sumaKawalka(kawalek2)
                if czyPotega(suma):
                    return True
    return False




