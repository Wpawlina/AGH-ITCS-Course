def rook(n,l):
    minK=float('inf')
    def rek(r,c,cnt):
        nonlocal minK
        if r==n-1 and c==n-1:
            minK=min(minK,cnt)
            return
        for i in range(r+1,n):
            if (i,c) in l:
                break
            rek(i,c,cnt+1)
        for i in range(c+1,n):
            if (r,i) in l:
                break
            rek(r,i,cnt+1)
    rek(0,0,0)
    return minK if minK!= float('inf') else 0
l=[(1,0),(0,2),(2,1)]   
print(rook(3,l))

    
        
            