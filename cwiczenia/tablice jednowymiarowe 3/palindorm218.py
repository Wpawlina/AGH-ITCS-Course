def f(t):
    best=0
    n=len(t)
    for i in range(-n+1,n):
        cons=0
        for j in range(n-abs(i)):
            x=t[j+max(0,i)]
            y=t[n-1-j-max(0,-i)]
            if x==y:
                cons+=1
                if best < cons:
                    best=cons
            else:
                cons=0
    return best               
t=[9,3,1,3,5,5,3,1,8]
print(f(t))