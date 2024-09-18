def czyWieksze(A,B):
    n=len(A)
    for i in range(n):
        if A[i]!=B[i]:
            if A[i]==1:
                return True
            else:
                return False
    return False





def distance(t):
    n=len(t)
    maxi=0
    mini=0
    for i in range(1,n):
        if czyWieksze(t[i],t[maxi]):
            maxi=i
        elif czyWieksze(t[mini],t[i]):
            mini=i
    return abs(maxi-mini)

    



t=[[1,1,1,1],[1,0,1,1],[0,0,0,1],[0,1,1,0]]
print(distance(t))
    

