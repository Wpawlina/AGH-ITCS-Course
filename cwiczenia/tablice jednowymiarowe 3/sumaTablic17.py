


def pierwsza(n):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
        if n%i==0:
            return False
        i+=4
    return True

def sumaTablic(t1,t2,pos,n,ciag,sumy):
    if(pos==n):
        suma=sum(ciag)
        if pierwsza(suma):
            sumy.append(sum(ciag))
        return
    ciag[pos]=t1[pos]
    sumaTablic(t1,t2,pos+1,n,ciag,sumy)
    ciag[pos]=t2[pos]
    sumaTablic(t1,t2,pos+1,n,ciag,sumy)
    ciag[pos]=t2[pos]+t1[pos]
    sumaTablic(t1,t2,pos+1,n,ciag,sumy)
sumy=[]
t1=[1,3,2,4]
t2=[9,7,4,8]
n=len(t1)
ciag=[0]*n


sumaTablic(t1,t2,0,n,ciag,sumy)
sumy=set(sumy)
print(sumy)


    
 


                          


