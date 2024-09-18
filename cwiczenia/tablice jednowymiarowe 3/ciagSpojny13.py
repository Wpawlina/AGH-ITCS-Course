def podciag(a,b):
    for i in range(len(a)-len(b)+1):
        if a[i:i+len(b)]==b:
            return True
    return False
def zad(t):
    rev=t.copy()
    rev.reverse()
    for l in range(len(t),-1,-1):
        for i in range(0,len(t)-l+1):
            if podciag(rev,t[i:i+l]):
                return l
            






t=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] 

print(zad(t))
    

           
        
