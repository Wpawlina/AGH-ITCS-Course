def push(t,i,num):
    n=len(t)
    pom=t[i]
    t[i]=num
    i+=1
    while i < n:
        t[i],pom=pom,t[i]
        i+=1
def psuedoSort(t,num):
    n=len(t)
    i=0
    while t[i] < num:
        if t[i]==0:
            t[i]=num
            return
        i+=1
    push(t,i,num)
def zad7(t1):
    n=len(t1)
    m=n*n
    t2=[0 for _ in range(m)]
    for i in range(n):
        for j in range(n):
            psuedoSort(t2,t1[i][j])
    return t2


t=[
    [1,2,3,99],
    [3,5,7,9],
    [2,11,33,36],
    [34,51,72,98]
]
print(zad7(t))

    







