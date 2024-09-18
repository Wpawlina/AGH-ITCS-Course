def wspolnoCzynnikowe(num1,num2):
    cnt=0
    i=2
    while num1!=1 and num2!=1:
        cnt_1=0
        while num1%i==0:
            num1//=i 
            cnt_1+=1
        cnt_2=0
        while num2%i==0:
            num2//=i 
            cnt_2+=1
        cnt+=min(cnt_1,cnt_2)
        if cnt>1:
            return False
        i+=1
        return cnt == 1
        
        

        





def four(t):
    n=len(t)
    moves=[(1,0),(-1,0),(0,1),(0,-1)]
    fours=0
    for i in range(1,n-1):
        for j in range(1,n-1):
            cnt=0
            for move in moves:
                if wspolnoCzynnikowe(t[i][j],t[i+move[0]][j+move[1]]):
                    cnt+=1
            if cnt==4:
                fours+=1
    return fours



            