class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
       

def zad32(l1,l2):
    l3=None
    startl3=None
    while l1 is not None and l2 is not None:
        value=l1.val-l2.val
        p=Node(value)
        if l3 is None:
            l3=p
            startl3=l3
        else:
            l3.next=p
            l3=l3.next
        l1=l1.next
        l2=l2.next
    if l1 is None and l2 is not None:
        while l2 is not None:
            p=Node(-l2.val)
            if l3 is None:
                l3=p
                startl3=l3
            else:
                l3.next=p
                l3=l3.next
            l2=l2.next
    if l1 is not None and l2 is None:
         while l1 is not None:
            p=Node(l1.val)
            if l3 is None:
                l3=p
                startl3=l3
            else:
                l3.next=p
                l3=l3.next
            l1=l1.next
    return startl3






        
