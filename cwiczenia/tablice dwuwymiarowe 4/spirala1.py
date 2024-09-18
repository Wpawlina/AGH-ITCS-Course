def spirala(t):
    n=len(t)
    i=0
    j=0
    v=1
    jk=n
    ik=n
    ip=-1
    jp=-1
    moves=[(0,1),(1,0),(0,-1),(-1,0)]
    m=0
    t[0][0]=1
    while v<=(n*n):
        while ip < i < ik and jp < j < jk :
            t[i][j]=v
            i+=moves[m][0]
            j+=moves[m][1]
            v+=1 
        i-=moves[m][0]
        j-=moves[m][1]
        if m==0:
            ip+=1
        elif m==1:
            jk-=1
        elif m==2:
            ik-=1
        elif m==3:
            jp+=1
        m+=1
        m=m%4
        i+=moves[m][0]
        j+=moves[m][1]
    return t

t=[[0 for _ in range(20)] for _ in range(20)]
t=spirala(t)
for i in range(len(t)):
        print(t[i])

# z4 4/5 , 7,8,9,13,17
  




