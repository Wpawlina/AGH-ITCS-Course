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
def reverseList(first,prev=None):
    if first==None:
        return prev
    next=first.next
    first.next=prev
    return reverseList(next,first)
first=initSparseTab(5,10)

for i in range(5):
   setN(first,i,i)

for i in range(5):
    printN(first,i)


print('###############')

first=reverseList(first)

for i in range(5):
    printN(first,i)
