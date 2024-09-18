
def zad11(n,startowy,docelowy,pomocniczy):
    if n==0:
        return
    zad11(n-1,startowy,pomocniczy,docelowy)
    print('klocek '+str(n)+' przesnies z '+startowy+' na '+docelowy)
    zad11(n-1,pomocniczy,docelowy,startowy)

zad11(5,'A','B','C')



