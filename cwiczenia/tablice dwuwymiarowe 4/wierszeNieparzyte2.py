def onlyOdd(num):
    while num!=0:
        d=num%10
        if d%2==0:
            return False
        num//=10
    return True
def rowHasOnlyOdd(t,r):
    n=len(t)
    for i in range(n):
        if onlyOdd(t[r][i]):
            return True
    return False
def zad2(t):
    n=len(t)
    for i in range(n):
        if not rowHasOnlyOdd(t,i):
            return False
    return True



t=[
    [1,2,4,8,10],
    [2,4,6,8,3],
    [1,2,4,8,10],
    [1,2,4,8,10],
    [1,2,4,8,10]
]
print(zad2(t))