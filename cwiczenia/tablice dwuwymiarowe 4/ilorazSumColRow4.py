def sumOfRow(t,r):
    sum=0
    n=len(t)
    for i in range(n):
        sum+=t[r][i]
    return sum
def sumOfCol(t,c):
    sum=0
    n=len(t)
    for i in range(n):
        sum+=t[i][c]
    return sum
def zad4(t):
    n=len(t)
    maxRatio=-float('inf')
    maxC=-1
    maxR=-1
    for i in range(n):
        for j in range(n):
            sumR=sumOfRow(t,i)
            sumC=sumOfCol(t,j)
            iloraz=sumC/sumR
            if iloraz > maxRatio:
                maxRatio=iloraz
                maxC=j
                maxR=i
    return maxR,maxC
            
    


t=[
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,3]
]
print(zad4(t))