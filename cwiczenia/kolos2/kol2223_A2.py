def king(n,l):
    maxM=0
    def rek(r,c,move,prev):
        nonlocal maxM
        if r==n-1 and c==n-1:
            maxM=max(maxM,move)
            return
        
        if c+1<n and (r,c+1) not in l:
            rek(r,c+1,move+1,'R')
        if r+1<n and (r+1,c) not in l and prev!='U':
            rek(r+1,c,move+1,'D')
        if r-1>=0 and (r-1,c) not in l and prev!='D':
            rek(r-1,c,move+1,'U')
    rek(0,0,0,'')
    return maxM if maxM > 0 else None
l=[(0,1)]
n=3
print(king(n,l))
        
            
        
