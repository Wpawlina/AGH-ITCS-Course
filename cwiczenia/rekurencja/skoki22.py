def zad22(T):
    n=len(T)
    value=0
    def rek(i):
        nonlocal value
        if i==n-1:
            value=True
        k=2
        x=T[i]
        while x!=1:
            if x%k==0:
                if k<T[i]:
                    rek(i+k)
                    if value==True:
                        return
                while x%k==0:
                    x//=k
            k+=1
    rek(0)
    return value

t=[8,1,5,3,2]
print(zad22(t))

    
            