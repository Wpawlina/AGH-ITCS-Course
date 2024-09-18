def zad8(t):
    n=len(t)
    maxl=0
    for i in range(n):
        for j in  range(n):
            k=1
            if i+k<n and j+k<n:
                qp=t[i+k][j+k]/t[i][k]
                curl=2
                while i+k+1 <n and j+k+1<n:
                    q=t[i+k+1][j+k+1]/t[i+k][j+k]
                    if q==qp:
                        curl+=1
                    else:
                        break
                    k+=1
                maxl=max(maxl,curl) 
    return maxl if maxl>2 else 0

t=[
    [2,2,3],
    [1,10,6],
    [2,5,50]
]  
print(zad8(t))


