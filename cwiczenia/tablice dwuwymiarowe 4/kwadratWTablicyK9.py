def zad9(t,k):
    n=len(t)
    for i in range(n):
        for j in range(n):
            bok=3
            while i+bok-1<n and j+bok-1 <n:
                iloczyn=t[i][j]*t[i][j+bok-1]*t[i+bok-1][j]*t[i+bok-1][j+bok-1]
                if iloczyn==k:
                    srodeki=(i+i+bok-1)//2
                    srodekj=(j+j+bok-1)//2
                    return srodeki,srodekj
                bok+=2
    return -1
t=[
    [3,1,1,1,3],
    [1,3,1,3,1],
    [3,1,1,1,1],
    [1,3,1,3,1],
    [3,1,1,1,1]
]
print(zad9(t,81))