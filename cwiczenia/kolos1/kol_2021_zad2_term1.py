def sumOfRowBin(t,i):
    n=len(t)
    p=n-1
    value=0
    for j in range(n):
        value+=t[i][j]*(2**p)
        p-=1
    return value






def distance(t):
    n=len(t)
    v=[0 for _ in range(n)]
    for i in range(n):
        v[i]=sumOfRowBin(t,i)
    maxDif=0
    maxi=0
    maxj=1
    for i in range(n):
        for j in range(i+1,n):
            dif=abs(v[i]-v[j])
            if dif > maxDif:
                maxDif=dif
                maxi=i
                maxj=j
    return abs(maxi-maxj)



t=[[1,1,1,1],[1,0,1,1],[0,0,0,1],[0,1,1,0]]
print(distance(t))
    

