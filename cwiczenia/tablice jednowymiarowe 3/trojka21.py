def nwd(a,b):
    if a<b:
        pom=a
        a=b
        b=pom
    while b!=0:
        pom=b
        b=a%b
        a=pom
    return a

def zad(t):
    n=len(t)
    trojki=0
    i=0
    while i<n-2:
        j=i+1
        while j<n-1:
            if j>i+2:
                break
            k=j+1
            while k<n:
                if k > j+2:
                    break
                nwd1=nwd(t[i],t[j])
                nwd1=nwd(nwd1,t[k])
                if nwd1==1:
                    print(t[i],t[j],t[k])
                k+=1
            j+=1
        i+=1
    return trojki


tab= [2, 3, 5, 7, 11, 13]
print(zad(tab))

