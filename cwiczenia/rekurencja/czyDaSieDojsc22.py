def fact(i,k,T):
    if k>T[i]:
        return False
    if k<2:
        return False
    x=T[i]
    i=2
    while x!=1:
        while x%i==0:
            if k==i:
                return True
            x//=i  
        i+=1
    return False
def zad22(T):
    n=len(T)
    value=False
    def rek(i):
        nonlocal value
        if i==n-1:
            value=True
            return
        
        for j in range(i+2,n):
            if fact(i,j-i,T):
                rek(j)
                if value==True:
                    return
        rek(0)
        return value
        



