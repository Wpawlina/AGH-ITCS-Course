def palindrom(t):
    n=len(t)
    maxl=1
    for i in range(1,n-1):
        l=1
        p=i-1
        x=i+1
        while p>=0 and x<=n-1:
            if t[p]==t[x]:
                l+=2
                p-=1
                x+=1
            else:
                break
        if l>maxl:
            maxl=l
    for i in range(0,n-1):
        if t[i]==t[i+1]:
            l=2
            p=i-1
            x=i+2
        while p>=0 and x<=n-1:
            if t[p]==t[x]:
                l+=2
                p-=1
                x+=1
            else:
                break
        if l>maxl:
            maxl=l
    return maxl
            
t=[9,3,1,3,5,5,3,1,8]
print(palindrom(t))