def zad7(T,masa):
    n=len(T)
    odw=[0]*n
    def rek(i,waga,p,odw):
        if i==n or waga==masa:
            if waga==masa:
                print(odw)
        else:
            rek(i+1,waga,p,odw.copy()) 
            odw[p]=T[i]
            rek(i+1,waga+T[i],p+1,odw.copy())
            odw[p]=-T[i]
            rek(i+1,waga-T[i],p+1,odw.copy())
    rek(0,0,0,odw)

zad7([7,4,6,1,5],13)
