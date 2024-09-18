from math import sqrt

def zad24(T):
    n=len(T)
    minOdl=float('inf')
    def rek(i,A,B,dlA,dlB,id):
        nonlocal minOdl
        if i==n:
            if dlA != 0 and dlB !=0 and ( id!=dlA or id!=dlB):
            
                odl=abs(sqrt((A[0]-B[0])**2+(A[1]-B[1])**2))
                minOdl=min(minOdl,odl)
            return
        if dlA==0:
            rek(i+1,(T[i][0],T[i][1]),B,dlA+1,dlB,id)
        else:
            rek(i+1,((A[0]+T[i][0])/2,(A[1]+T[i][1])/2),B,dlA+1,dlB,id)
        if dlB==0:
            rek(i+1,A,(T[i][0],T[i][1]),dlA,dlB+1,id)
        else:
            rek(i+1,A,((B[0]+T[i][0])/2,(B[1]+T[i][1])/2),dlA,dlB+1,id)
        if dlA==0:
            rek(i+1,(T[i][0],T[i][1]),((B[0]+T[i][0])/2,(B[1]+T[i][1])/2),dlA+1,dlB,id+1)
        elif dlB==0:
            rek(i+1,((A[0]+T[i][0])/2,(A[1]+T[i][1])/2),(T[i][0],T[i][1]),dlA,dlB+1,id+1)
        else:
            rek(i+1,((A[0]+T[i][0])/2,(A[1]+T[i][1])/2),((B[0]+T[i][0])/2,(B[1]+T[i][1])/2),dlA+1,dlB+1,id+1)
        rek(i+1,A,B,dlA,dlB,id)
    rek(0,(0,0),(0,0),0,0,0)
    return minOdl
T=[(2,2),(8,10)]
print(zad24(T))

        
        
        
            
        

