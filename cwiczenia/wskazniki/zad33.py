class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
       


def poprzedza(str1,str2):
    n=len(str1)
    let1=str1[n-1]
    let2=str2[0]
    if ord(let1)<ord(let2):
        return True
    return False
def zad33(first,napis):
    q=None
    p=first
    while True:
        word1=p.val
        word2=p.next.val
        if poprzedza(word1,napis)and poprzedza(napis,word2):
            new=Node(napis)
            p.next,new=new,p.next
            return True
        p=p.next
        if p==first:
            return False
            




            
        
            
            
        


       
     

