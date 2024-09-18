class Node:
    def init(self,val):
        self.val = val
        self.next = None
def czyWystepuje(first,value):
    cur=first
    while cur is not None and cur.val<value:
        cur=cur.next
    if cur is None:
        return False
    if cur.val==value:
        return True
    return False
    



def iloczyn(z1,z2,z3):
    w=Node(None)
    w.next=z1
    z1=w
    cur1=z1.next
    prev1=z1
    while cur1 is not None:
        if not czyWystepuje(cur1.val,z2):
            prev1.next=cur1.next
        elif not czyWystepuje(cur1.val,z3):
            prev1.next=cur1.next
        else:
            prev1=cur1
        cur1=cur1.next
    return z1


    
