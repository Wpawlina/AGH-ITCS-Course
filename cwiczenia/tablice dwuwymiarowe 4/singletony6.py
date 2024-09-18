def isSingleton(t,num):
    n=len(t)
    flag=False
    for i in range(n):
        for j in range(n):
            if t[i][j]==num and not flag:
                flag=True
            elif t[i][j]==num and flag:
                return False
    return True


def push(t,num,i):
    n=len(t)
    temp=t[i]
    t[i]=num
    for j in range(i+1,n):
        t[j],temp=temp,t[j]

def psuedosort(t,num):
    n=len(t)
    i=0
    while t[i]<num:
        if t[i]==0:
            t[i]=num
            return
        i+=1
    push(t,num,i)

def zad6(t1):
    n=len(t1)
    t2=[0 for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
            if isSingleton(t1,t1[i][j]):
                psuedosort(t2,t1[i][j])
    return t2

t=[[12,7,5],[5,8,6],[7,9,2]]
print(zad6(t))

            



