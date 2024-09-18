def lastDigBigger(a,b):
    a=a%10
    while b>9:
        b//=10
    return True if a < b else False


def zad18(w,k,T):
    n=len(T)
    value=False
    X=[]
    moves=[(0,1),(1,1),(1,0)]
    def rek(i,j):
        nonlocal value
        if i==n-1 and j==n-1:
            value=True
        for move in moves:
            if 0<= i +move[0] < n and 0<= j+move[1] < n and lastDigBigger(T[i][j],T[i+move[0]][j+move[1]]):
                rek(i+move[0],j+move[1])
                if value==True:
                    X.append(move)
                    return
    rek(0,0)
    X=X[::-1]
    return value,X
T=[
    [24,1],
    [51,91]
   ]
print(zad18(0,0,T))



    
                
            


