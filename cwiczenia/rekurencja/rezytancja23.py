def zad23(T,k):
    n=len(T)
    value=False
    def rek(i,p,r1,r2,r,flag):
        nonlocal value
        if p==3:
            if r==k:
                value=True
            return
        if i==n:
            return
        if p==0:
            rek(i+1,p+1,T[i],r2,T[i],False)
        if p==1:
            rek(i+1,p+1,r1,T[i],r+T[i],False)
            rek(i+1,p+1,r1,T[i],(r1*r2)/(r1+r2),True)
        if p==2:
            if not flag:
                rek(i+1,p+1,r1,r2,r+T[i],False)
                rek(i+1,p+1,r1,r2,(r1*T[i])/(r1+T[i])+r2,True)
                rek(i+1,p+1,r1,r2,(r2*T[i])/(r2+T[i])+r1,True)
                rek(i+1,p+1,r1,r2,((r)*T[i])/(r+T[i]),True)
            else:
                rek(i+1,p+1,r1,r2,r+T[i],True)
                rek(i+1,p+1,r1,r2,((r)*T[i])/(r+T[i]),True)
        rek(i+1,p,r1,r2,r,flag)
    rek(0,0,0,0,0,False)
    return value

                
T = [10,1,4]
R = 8
print(zad23(T,R))



        
            

            