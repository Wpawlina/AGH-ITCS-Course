def zad3(T,k):
    mink=float('inf')
    moves=[(1,-1),(1,0),(1,1)]
    def rek(w,k,koszt):
        nonlocal mink
        if w==7:
            mink=min(mink,koszt)
            return
        for move in moves:
            if 0 <= k + move[1] < 8:
                rek(w+move[0],k+move[1],koszt+T[w+move[0]][k+move[1]])
    rek(0,k,T[0][k])
    return mink
    
T=[[2,2,2,2,2,2,2,2],
   [2,2,1,2,2,2,2,2],
   [2,2,2,1,2,2,2,2],
   [2,2,1,2,2,2,2,2],
   [2,2,2,1,2,2,2,2],
   [2,2,2,1,2,2,2,2],
   [2,2,1,2,2,2,2,2],
   [2,2,2,1,2,2,2,2],
   ]
print(zad3(T,3))
                



        


        