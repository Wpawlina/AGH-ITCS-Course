def zad31(n):
    suma=0
    def rek(n,k,iloczyn):
        nonlocal suma
        if n==1:
            suma+=iloczyn if iloczyn > 1 else 0
            return
        if n%k==0:
            while n%k==0: 
               n=n//k
            rek(n,k+1,iloczyn*k)
        rek(n,k+1,iloczyn)
    rek(n,2,1)
    return suma
print(zad31(60))
