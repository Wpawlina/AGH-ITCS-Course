def cntChecked(T):
    n=len(T)
    moves=[(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if T[i][j]==0:
                flag=False
                for move in moves:
                    if 0<= i+move[0] < n and 0<= j+move[1] < n:
                        if T[i+move[0]][j+move[1]]==1:
                            flag=True
                if flag:
                    cnt+=1
    return cnt
def zad(T):
    n=len(T)
    sr=n//2
    sc=n//2
    maxCnt=cntChecked(T)
    maxr=-1
    maxc=-1
    for i in range(n):
        for j in range(n):
            if T[i][j]==0:
                T[i][j]=1
                cnt=cntChecked(T)
                if cnt > maxCnt:
                    maxr=i
                    maxc=j
                    maxCnt=cnt
                if cnt==maxCnt and max(abs(i-sr), abs(j-sc)) < max(abs(maxr-sr), abs(maxc-sc)):
                    maxr=i
                    maxc=j
                T[i][j]=0
    return maxr, maxc 






    


                