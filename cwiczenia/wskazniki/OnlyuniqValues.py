def zad18(first):
    p=first
    while p!=None:
        q=p
        n=p.next
        while n!=None:
            if n.val==p.val:
                q.next=n.next
            else:
                q=n
            n=n.next
        p=p.next
    
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
ll=LL()

