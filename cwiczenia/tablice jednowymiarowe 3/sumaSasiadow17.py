def zad17(t):
    n=len(t)
    maxs=0
    maxi=0
    maxj=0
    moves=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    for i in range(n):
        for j in range(n):
            sumc=0
            for move in moves:
                if  0 <= i+move[0] < n and 0<= j+move[1]<n:
                    sumc+=t[i+move[0]][j+move[1]]
            if sumc>maxs:
                maxs=sumc
                maxi=i
                maxj=j
    return maxi,maxj

t=[
    [2,2,2],
    [2,1000,5],
    [2,2,3]
]
            
print(zad17(t))