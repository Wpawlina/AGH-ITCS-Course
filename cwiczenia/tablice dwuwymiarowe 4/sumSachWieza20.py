def sumOfChecked(t,r1,c1,r2,c2):
    n=len(t)
    sum=0
    for i in range(n):
            if i!=c1:
                sum+=t[r1][i]
    for i in range(n):
            if i!=r1:
                sum+=t[i][c1]
    if r1!=r2 and c1!=c2:
        for i in range(n):
            if i!=c2:
                sum+=t[r2][i]
        for i in range(n):
            if i!=r2:
                sum+=t[i][c2]
        sum=sum-t[r1][c2]-t[r2][c1]
        return sum
    if r1==r2:
        for i in range(n):
            if i!=r2:
                sum+=t[i][c2]
        sum+=t[r1][c1]
        return sum
    if c1==c2:
        for i in range(n):
            if i!=c2:
                sum+=t[r2][i]
        sum+=t[r1][c1]
        return sum
        


    
    
        
        

        



def zad20(t):
    n=len(t)
    biggest_sum=-float('inf')
    maxr1=0
    maxc1=0
    maxr2=0
    maxc2=0
    for r in range(n):
        for c in range(n):
            for y in range(n):
                for x in range(n):
                    if x!=c or y!=r:
                        sum = sumOfChecked(t,r,c,y,x)
                        if sum > biggest_sum:
                            biggest_sum=sum
                            maxr1=r
                            maxc1=c
                            maxr2=y
                            maxc2=x
    return maxr1,maxc1,maxr2,maxc2
    


