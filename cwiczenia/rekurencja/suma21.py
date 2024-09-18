import copy

def blokuj(w,k,T):
    n=len(T)
    for i in range(n):
        T[w][i]=1
    for i in range(n):
        T[i][k]=1
    


def zad21(T,suma):
    n=len(T)
    blocked=[[0 for _ in range(n)] for _ in range(n)]   
    value=False 
    def rek(i,csum,blocked):
        nonlocal value
        if csum==suma:
            value=True
            return
        if i==n*n:
            return
        w=i//n
        k=i%n
        if blocked[w][k]==0:
            

            blocked2=copy.deepcopy(blocked)
            blokuj(w,k,blocked2)
            rek(i+1,csum+T[w][k],blocked2)
            
            if value==True:
                return
        rek(i+1,csum,blocked)  
    rek(0,0,blocked)
    return value


t=[
    [3,2,1],
    [3,3,2],
    [3,5,2]
]
print(zad21(t,9))

