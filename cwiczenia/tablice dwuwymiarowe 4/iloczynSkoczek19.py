def zad19(t,x):
    n=len(t)
    moves=[(-2,1),(-1,2),(1,2),(2,1)]
    counter=0
    for i in range(n):
        for j in range(n):
            for move in moves:
                if -1 < i + move[1] < n and -1 < j + move[0] < n and t[i+move[1]][j+move[0]]*t[i][j]==x:
                    counter+=1
    return counter
    
 
