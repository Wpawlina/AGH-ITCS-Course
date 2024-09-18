def zad19(t):
    n=len(t)
    p=0
    k=0
    suma=t[0]
    sumai=0
    maxl=0
    if suma==sumai:
        maxl=1
    while k<n-1:
        if t[k+1]>t[k]:
            suma+=t[k+1]
            sumai+=k+1
            k+=1
            if suma==sumai:
                maxl=max(maxl,k-p+1)
        else:
            k+=1
            p=k
            suma+=t[k]
            sumai+=k
            if suma==sumai:
                maxl=max(maxl,k-p+1)
    return maxl
            
            
        








t=[0,1,2,3,5,6,7,5,8,9,1,7,4]
print(zad19(t))