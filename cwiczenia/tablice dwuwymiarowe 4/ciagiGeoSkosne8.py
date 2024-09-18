def zad8(t):
    n=len(t)
    maxl=0
    for i in range(n):
        for j in range(n):
            k=0 
            curl=2
        while i+k+2<n and j+k+2<n:
            q=t[i+k+1][j+k+1]/t[i+k][j+k]
            if t[i+k+2][j+k+2]/t[i+k+1][j+k+1]==q:
                curl+=1
            else:
                break
            k+=1
        maxl=max(maxl,curl)
    return maxl if maxl>2 else None

    



