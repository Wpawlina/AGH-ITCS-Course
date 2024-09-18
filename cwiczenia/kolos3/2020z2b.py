class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def zad2b(first):
    w=Node(None)
    w.next=first
    first=w
    cur=first.next
    q=first
    minq=None
    curq=None
    minp=None
    cnt=0
    minl=float('inf')
    curl=1
    while cur is not None:
        if cur.next is not None and cur.val==cur.next.val:
            curl+=1
            if curl==2:
                curq=q
        else:
            if curl<minl and curl > 1:
                minq=curq
                minl=curl
                minp=cur
                cnt=1
            elif minl==curl:
                cnt+=1
            curq=None
            curl=1
        q=cur
        cur=cur.next
    if minl != float('inf') and cnt == 1:
        minq.next=minp.next
        return minl,first.next
    return 0,first


linked_list = Node(1)
linked_list.next = Node(2)
linked_list.next.next = Node(2)
linked_list.next.next.next = Node(2)
linked_list.next.next.next.next = Node(2)
linked_list.next.next.next.next.next = Node(5)
linked_list.next.next.next.next.next.next = Node(5)
ile,linked_list=zad2b(linked_list)
cur = linked_list # Skip the dummy node
print("Modified Linked List:")
while cur:
    print(cur.val, end=" -> ")
    cur = cur.next
print("None")

        


            
            
