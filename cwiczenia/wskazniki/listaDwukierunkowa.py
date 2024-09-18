class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

def createL(n):
    if n>0:
        q=Node(0)
        first=q
        for i in range(1,n):
            p=Node(i)
            p.prev=q
            q.next=p
            q=p
            
        return first
    
def insertFirst(first,value):
    p=Node(value)
    p.next=first
    first.prev=p
    first=p
    return first
def insertLast(first,value):
    q=None
    p=first
    while p!=None:
        q=p
        p=p.next
    p=Node(value)
    if q is not None:    
        q.next=p
        p.prev=q
    else:
        first=p
    return first
def printL(first):
    p=first
    while p!=None:
        print(p.val)
        print('->')
        p=p.next
def printLreverse(first):
    p=first
    q=None
    while p!=None:
        q=p
        p=p.next
    while q!=None:
        print(q.val)
        print('->')
        q=q.prev
def deleteEl(first,value):
    p=first
    q=None
    if p is not None:
        n=p.next
    while p is not None:
        if p.val==value:
            if q is not None:
                q.next=p.next
            else:
                first=p.next
            if n is not None:
                n.prev=p.prev
            return first
        q=p
        p=p.next
        if n is not None:
            n=n.next


first=createL(10)
first=insertFirst(first,-1) 
printL(first)
print('######')
printLreverse(first)







    



