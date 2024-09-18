def is_coprime(a,b):
    while b!=0:
        a,b=b,a%b
    return a==1

def rook_race(T):
    rook1_time=float('inf')
    rook2_time=float('inf')
    n=len(T)
    def rook1(r,c,cnt):
        nonlocal rook1_time
        if r==c == n-1:
            rook1_time=min(rook1_time,cnt)
            return
        for i in range(r+1,n):
            if is_coprime(T[r][c],T[i][c]):
                rook1(r+i,c,cnt+1)
        for i in range(c+1,n):
            if is_coprime(T[r][c],T[r][i]):
                rook1(r,c+i,cnt+1)
    def rook2(r,c,cnt):
        nonlocal rook2_time
        if r==n-1 and c==0:
            rook2_time=min(rook1_time,cnt)
            return
        for i in range(r+1,n):
            if is_coprime(T[r][c],T[i][c]):
                rook1(r+i,c,cnt+1)
        for i in range(c-1,-1,-1):
            if is_coprime(T[r][c],T[r][i]):
                rook1(r,c-i,cnt+1)
            



