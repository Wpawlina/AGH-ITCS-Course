def delLast(first):
    if first is None or first.next is None:
        return None
    cur=first
    prev=None
    prev2=None
    while cur!=None:
        prev2=prev
        prev=cur
        cur=cur.next
    prev2.next=None
    return first
    
    
class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
def initSparseTab(ile,default):
    if ile>0:
        p=Node(default)   
        first=p
        for i in range(1,ile):
            new=Node(default)
            p.next=new
            p=p.next
        return first
    return None
def printN(first,n):
    wsk=first
    i=0
    while wsk!=None and i<n:
        wsk=wsk.next
        i+=1
    if wsk==None:
        return None
    print(wsk.val,i) 
def setN(first,n,value):
    wsk=first
    i=0
    while wsk!=None and i<n:
        wsk=wsk.next
        i+=1
    if wsk==None:
        return None
    wsk.val=value
first=initSparseTab(5,2)
for i in range(5):
    printN(first,i)
print('###############')
first=delLast(first)
for i in range(5):
    printN(first,i)