def move(T):
    n=len(T)
    def poleSzachowane(r,c):
        for i in range(n):
             if T[r][i] or T[i][c]:
                 return True
        return False
    for i in range(n):
        for j in range(n):
            if not poleSzachowane(i,j):
                return i,j
            
                   
                   
       
           
                
        
            


    


