def czyWielokrotny(napis):
    n=len(napis)
    l=1
    while l <= n/2:
        if n%l==0:
            seq=napis[0:l]
            i=1
            while i*l <n:
                nextSeq=napis[i*l:(i+1)*l]
                if nextSeq!=seq:
                    break
                i+=1
            else:
                 return True
        l+=1
    return False
            





def mulit(t):
    n=len(t)
    maxl=0
    for i in range(n):
        if czyWielokrotny(t[i]):
            maxl=max(maxl,len(t[i]))
    return maxl
