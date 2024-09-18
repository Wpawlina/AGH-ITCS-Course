def czyMoznaZlaczyc(A,B):

    if B[0] > A[len(A)-1]:
        return True
    if A[0] > B[len(B)-1]:
        return True
    return False
        




def zadB1(t):
    n=len(t)
    p=0
    k=0
    dl=2
    ciagi=[]
    while k+1 < n:
        if t[k+1]>t[k]:
            k+=1
        else:
            if k-p+1>=3:
                ciagi.append((p,k))
            k+=1
            p=k
    for i in range(len(ciagi)):
        for j in range(i+1,len(ciagi)):
            if czyMoznaZlaczyc(t[ciagi[i][0]:ciagi[i][1]+1],t[ciagi[j][0]:ciagi[j][1]+1]):
                return True
    return False

    
            
            
    

    

t= [2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2]
print(zadB1(t))


        

           




