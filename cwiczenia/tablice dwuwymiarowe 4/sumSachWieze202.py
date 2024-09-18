
def sumOfTableWithout(t,r1,c1,r2,c2):
    n=len(t)
    sum=0
    for i in range(n):
        for j in range(n):
            if i!=r1 and i!=r2 and j!=c1 and j!=c2:
                sum+=t[i][j]
    return sum



def zad20(t):
    n=len(t)
    biggest_sum=-float('inf')
    sumOfAll=sumOfTableWithout(t,-1,-1,-1,-1)
    for r in range(n):
        for c in range(n):
            for y in range(n):
                for x in range(n):
                    if x!=c or y!=r:
                        sum=sumOfAll-sumOfTableWithout(t,r,c,y,x)-t[r][c]-t[y][x]
                        biggest_sum=max(biggest_sum,sum)
    return biggest_sum
t=[[2,0,0,1],
   [2,0,0,1],
   [1,0,0,0],
   [1,0,0,0]
   ]
print(zad20(t))