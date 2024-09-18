def czyNieZachodzi(i,j,T):
    if T[j][0] <= T[i][0] <= T[j][1] or  T[j][0] <= T[i][1] <= T[j][1] :
        return False
    return True
def dlugosc(T,i):
    return abs(T[i][1]-T[i][0])
def zad2(T):
    n=len(T)
    value=False
    used=[False for _ in range(n)]
    def rek(i,suma):
        nonlocal value
        if suma==2022:
            value=True
            return
        if i==n:
            return
        flaga=True
        for j in range(n):
            if used[j]==True:
                if not czyNieZachodzi(i,j,T):
                    flaga=False
                    break
        if flaga==True:
            used[i]==True
            rek(i+1,suma+dlugosc(T,i))
            used[i]==False
            if value==True:
                return
        rek(i+1,suma)
    rek(0,0)
    return value





        