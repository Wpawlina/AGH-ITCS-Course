from math import log10

def podwojenieParzystych(a):
    b=0
    p=0
    while a!=0:
        dig=a%10
        if dig%2==0:
            b+=(dig+1)*10**p
        else:
            b+=dig*10**p
        p+=1
        a//=10
    return b
def zad2(x,y,n):
    ile=0
    def rek(x,y,i,poprzednia,ciag):
        nonlocal ile
        if x==y:
            print(ciag)
            ile+=1
            return
        if i==n:
            return
        if poprzednia!='A':
            rek(x+3,y,i+1,'A',ciag+'A')
        if poprzednia!='B':
            rek(2*x,y,i+1,'B',ciag+'B')
        if poprzednia!='C':
            rek(podwojenieParzystych(x),y,i+1,'C',ciag+'C')
    rek(x,y,0,None,'')
    return ile
print(zad2(11,32,4))






