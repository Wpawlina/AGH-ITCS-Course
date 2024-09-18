def ileJedynek(num):
    cnt=0
    while num!=0:
        cnt+=num%2
        num//=2
    return cnt
def czyZgodne(num1,num2):
    if ileJedynek(num1)==ileJedynek(num2):
        return True
    return False
def zad14(t1,t2):
    n1=len(t1)
    n2=len(t2)
    maxper=0
    m=n1*n1
    for i in range(n2-n1+1):
        for j in range(n2-n1+1):
            cnt=0
            per=0
            for y in range(n1):
                for x in range(n1):
                    if czyZgodne(t1[y][x],t2[i+y][j+x]):
                        cnt+=1
            per=cnt/m
            maxper=max(maxper,per)
    if maxper>0.33:
        return True
    else:
        return False
    


t2=[[1,1,1,1],
    [0,0,1,1],
    [1,1,0,0],
    [0,0,0,0]
    ]
t1=[
    [3,1],
    [0,3]
]
print(zad14(t1,t2))


            



