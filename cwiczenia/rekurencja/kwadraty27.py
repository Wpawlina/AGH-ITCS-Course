def czyNieZachodzi(T,i,j):
    if (T[j][0] <= T[i][0] < T[j][1] or T[j][0] <= T[i][1] < T[j][1]) and (T[j][2] <= T[i][2] < T[j][3] or T[j][2] <= T[i][3] < T[j][3]):
        return False
    return True

def zad27(T):
    n=len(T)
    Taken=[False for _ in range(n)]
    value=False
    def rek(i,Taken,cnt,area):
        nonlocal value
        if cnt==3 and area==6:
            value=True
            return
        if i==n:
            return
        flaga=True
        for j in range(len(Taken)):
            if Taken[j]:
                if not czyNieZachodzi(T,i,j):
                    flaga=False
        if flaga==True:
            Taken2=Taken.copy()
            Taken2[i]=True
            rek(i+1,Taken2,cnt+1,area+(T[i][1]-T[i][0])**2)
            if value==True:
                return 
        rek(i+1,Taken,cnt,area)
    rek(0,Taken,0,0)
    return value
T = [
    (1,2,1,2),
    (1,3,1,3),
    (4,5,4,5),
    (7,8,7,8)
]
print(zad27(T))





            

            