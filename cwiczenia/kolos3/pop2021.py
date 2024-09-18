

class Node:
    def init(self,val):
        self.val = val
        self.next = None


def repair(p):
    head=Node(None)
    head.next=p
    p=head
    even=Node()
    while p.next != None:
        if p.next.val%2==0:
            tmp=p.next
            p.next=p.next.next
            tmp.next=even.next
            even.next=tmp
        else:
            p=p.next
    p.next=even.next
    return head.next


