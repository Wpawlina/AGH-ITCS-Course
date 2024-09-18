class Node:
    def __init__(self):
        self.val=None
        self.next=None
class LL:
     def __init__(self):
          self.first=None
          self.last=None
def create(ll,T):
        T.reverse()
        n=len(T)
        ll.first=None
        for i in range(n):
            s=T[i]
            p=Node()
            p.val=s
            p.next=ll.first
            ll.first=p
            if i==0:
                 ll.last=p
def wypisz(ll):
    p=ll.first
    while p!=None:
        print(p.val)
        p=p.next
def addFirst(ll,val):
     p=Node()
     p.val=val
     p.next=ll.first
     ll.first=p
def find(ll,x):
    while p!=None:
          if p.val==x:
               return p
          p=p.next
    return None
def addLast(ll,val):
    q=None
    p=ll.first
    if ll.first==None:
        p=Node()
        p.val=val
        p.next=None
        ll.first=p
        return
    while p!=None:
        q,p=p,p.next
    p=Node()
    p.val=val
    p.next=None
    q.next=p

    
    
    
     
    

          
          

     




ll=LL()
create(ll,[10,9,8,7,6,5,4,3,2,1])
wypisz(ll.first)
