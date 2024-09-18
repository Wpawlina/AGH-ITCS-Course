def CreateMatrix(T,wiersz,kolumna):
    n=len(T)
    newT=[[0 for _ in range(n-1)]for _ in range(n-1)]
    j=0
    for i in range(n*n):
        w1=i//n
        k1=i%n
        if w1!=wiersz and k1!=kolumna:
            w2=j//(n-1)
            k2=j%(n-1)
            newT[w2][k2]=T[w1][k1]
            j+=1 
    return newT


T=[[1,1,1,1],
   [1,2,3,4],
   [1,-5,6,7],
   [1,8,9,10]
   ]

def printTab(T):
    n=len(T)
    for i in range(n):
        print(T[i])
    print('##########')


def det(T):
    n=len(T)
    if n==1:
        return T[0][0] 
    wyznacznik=0
    for i in range(n):
        wyznacznik+=(-1)**(1+i+1)*T[0][i]*det(CreateMatrix(T,0,i))
    return wyznacznik

print(det(T))




        
