class Node:
    def __init__(self,val):
        self.val=val
        self.next=None



def create(n):
    p=Node('X')
    first=p  
    for i in range(n):
        new=Node(i)
        p.next=new
        p=p.next
    return first
def printL(first):
    first=first.next
    while first!=None:
        print(first.val)
        first=first.next
def removeEl(first,el):
    q=first
    p=first.next
    while p!=None:
        if p.val==el:
            q.next=p.next
            break
        q=p
        p=p.next
def insertFirst(first,el):
    p=Node(el)
    p.next=first.next
    first.next=p
def insertLast(first,el):
    q=first
    p=first.next
    while p!=None:
        q=p
        p=p.next
    p=Node(el)
    q.next=p
    
    

    

        


    
        


first=create(5)
printL(first)
print('@@@')
removeEl(first,2)
printL(first)
print('@@@')
insertFirst(first,10)
printL(first)

    
