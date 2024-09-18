def zadA2(t):
    n=len(t)
    for i in range(n):
        for j in range(n):
                if t[i+2][j+2]==t[i][j]+t[i+1][j+1]-1:
                     dl=3
                     k=1
                     while i+k+2 < n and j+k+2<n:
                        if t[i+k+2][j+k+2]==t[i+k][j+k]+t[i+1+k][j+1+k]-1:
                            dl+=1
                        else:
                             break
                        k+=1     
                return dl
    return None


t=[
    [1,9,1,1],
    [8,6,2,2],
    [1,2,2,2],
    [1,2,2,5]
]
print(zadA2(t))




            
            