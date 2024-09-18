def areFriends(num1,num2):
    t=[0 for _ in range(10)]
    n=len(t)
    while num1!=0:
        t[num1%10]=1
        num1//=10
    while num2!=0:
        if t[num2%10]==1:
            t[num2%10]=2
        else:
            return False
        num2//=10
    for i in range(n):
        if t[i]==1:
            return False
    return True

def side(t,i,j):
    n=len(t)
    moves=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for move in moves:
        if -1 < i+move[0] < n and -1 < j+move[1]< n :
            if not  areFriends(t[i][j],t[i+move[0]][j+move[1]]):
                return False
    return True    

def zad11(t):
    n=len(t)
    cnt=0
    for i in range(n):
        for j in range(n):
            if side(t,i,j):
                cnt+=1
    return cnt

    

    
            