def zad4(T):
    n=len(T)
    moves=[(-2,1),(-1,2),(1,2),(-2,1),(-2,-1),(1,-2),(-1,-2),(-2,-1)]
    value=1
    def rek(w,k):
        nonlocal value
        T[w][k]=value
        if value==n*n:
                return 
        for move in moves: 
            if 0<= w + move[0] < n and  0<= k+ move[1] < n and T[w+move[0]][k+move[1]]==0:
                value+=1
                rek(w+move[0],k+move[1])
    rek(0,0)
def printTab(T):
    n=len(T)
    for i in range(n):
        print(T[i])



T=[[0 for _ in range(10)] for _ in range(10)]
zad4(T)
printTab(T)


# zestaw 5 10,14,18,19,21,22,23,24,
    
