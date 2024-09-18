def zad18(t):
    n=len(t)
    biggestSum=-float('inf')
    for r in range(n):
        for c in range(n):
            i=0
            sum=0
            while c+i<n and i< 10:
                sum+=t[r][c+i]
                biggestSum=max(biggestSum,sum)
                i+=1
            i=0
            sum=0
            while r + i < n and i<10:
                sum+=t[r+1][c]
                biggestSum=max(biggestSum,sum)
                i+=1
    return biggestSum

t=[
    [1,2,-1,4],
    [2,4,-3,0],
    [3,2,4,5],
    [-1,-2,-3,-4]
]

