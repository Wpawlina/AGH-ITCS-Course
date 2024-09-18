def ciagDo1():
    maxK=0
    maxS=0
    for i in range(2,10001):
        a=i
        lKrokow=0
        while a!=1:
            a=(a%2)*(3*a+1)+(1-a%2)*(a/2)
            lKrokow+=1
        if lKrokow > maxK:
            maxK=lKrokow
            maxS=i
    return maxS

print(ciagDo1())
        