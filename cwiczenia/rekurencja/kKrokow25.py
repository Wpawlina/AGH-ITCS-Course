def zad25(T):
    n=len(T)
    minK=n+1
    def rek(i,ile):
        nonlocal minK
        if i==n-1:
            minK=min(minK,ile)
            return
        x=T[i]
        k=2
        while x!=1:
            if x%k==0:
                if k<T[i] and i+k<n:
                    print(k)
                    rek(i+k,ile+1)
                    while x%k==0:
                        x//=k
            k+=1
    rek(0,0)
    return  minK if minK < n+1 else -1

T=[8,5,6,1,4,10,4,1,4,1,1]
print(zad25(T))


