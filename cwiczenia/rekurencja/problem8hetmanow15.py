

import copy


def szachowanie(T,w,k):
    
    moves=[(1,0),(1,1),(1,-1)]
    i=w
    j=k
    for move in moves:
        w=i
        k=j
        
        w+=move[0]
        k+=move[1]
        while w < 8 and -1< k < 8:
            T[w][k]=1
            w+=move[0]
            k+=move[1]
def printTab(T):
    for i in range(8):
        print(T[i])
    print('##########')




def zad15():
    cnt=0
    T=[[0 for _ in range(8)] for _ in range(8)]
    def rek(T,w):
        nonlocal cnt
        for i in range(8):
            if T[w][i]==0:
                if w==7:
                    cnt+=1
                    print('Znaleziono')
                    return
                t=copy.deepcopy(T)
                t[w][i]='*'
                szachowanie(t,w,i)
                printTab(t)
                rek(t,w+1)
    rek(T,0)
    return cnt

print(zad15())



        

       

