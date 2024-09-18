def zad13(num):
    skl=[0]*num
    def rek(suma,maks,skl,p):
        if suma==num:
            print(skl)
        else:
            for i in range(maks,0,-1):
                if suma+i<=num:
                    skl[p]=i
                    rek(suma+i,i,skl.copy(),p+1)
    rek(0,num-1,skl,0)
zad13(10)
            
            
            

