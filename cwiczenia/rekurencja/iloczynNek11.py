

def zad11(T,iloczynG,n):
    dl=len(T)
    cnt=0
    nki=[0]*n
    constN=n
    def rek(p,iloczyn,n,nki):
        nonlocal cnt
        if n==1:
            for i in range(p,dl):
                if iloczyn==T[i]:
                    nki[constN-1]=T[i]
                    print(nki)
                    cnt+=1
        else:
            for i in range(p,dl): 
                if iloczyn%T[i]==0:
                    nki[constN-n]=T[i]
                    rek(i+1,iloczyn//T[i],n-1,nki.copy())
    rek(0,iloczynG,n,nki) 
    return cnt


print(zad11([3,1,1,6,2,1,1,3],18,3))
            
                





    
    



