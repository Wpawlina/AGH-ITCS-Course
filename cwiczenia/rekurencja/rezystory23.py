def komb(T,k):
    lista=[]
    n=len(T)
    def rek(i,perm):
        nonlocal lista
        if len(perm)==k:
            lista.append(perm)
            return
        if i==n:
            return 
        rek(i+1,perm)
        nperm=perm.copy()
        nperm.append(T[i])
        rek(i+1,nperm)
    perm=[]
    rek(0,perm)
    print(lista)


T=[1,6,7,8]        

komb(T,2)

      


    
    