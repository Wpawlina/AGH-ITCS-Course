class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def zad3(first):
    l1=None
    l2=None
    first1=None
    first2=None
    cur=first
    while cur is not None:
        q=cur
        p=cur.next
        cnt=1
        value=cur.val
        while p is not None:
            if p.val==cur.val:
                cnt+=1
                q.next=p.next
            else:
                q=p
            p=p.next
        if cnt==2:
            if l1 is None:
                l1=cur
                first1=l1
                cur=cur.next
                new=Node(value)
                l1.next=new
                l1=l1.next
            else:
                l1.next=cur
                l1=l1.next
                cur=cur.next
                new=Node(value)
                l1.next=new
                l1=l1.next
        else:
            if l2 is None:
                l2=cur
                first2=l2
                cur=cur.next
                for i in range(cnt-1):
                    new=Node(value)
                    l2.next=new
                    l2=l2.next
            else:
                l2.next=cur
                l2=l2.next
                cur=cur.next
                for i in range(cnt-1):
                    new=Node(value)
                    l2.next=new
                    l2=l2.next
        
    if l1 is not None:
        l1.next=None
    if l2 is not None:
        l2.next=None
    return first1,first2

        
        
linked_list = Node(1)
linked_list.next = Node(2)
linked_list.next.next = Node(3)
linked_list.next.next.next = Node(2)
linked_list.next.next.next.next = Node(4)
linked_list.next.next.next.next.next = Node(3)
linked_list.next.next.next.next.next.next = Node(5)
linked_list.next.next.next.next.next.next.next = Node(7)
linked_list.next.next.next.next.next.next.next.next = Node(7)
linked_list.next.next.next.next.next.next.next.next.next = Node(7)


first1, first2 = zad3(linked_list)

# Display the modified linked lists
print("List with values appearing exactly twice:")
cur = first1
while cur:
    print(cur.val, end=" -> ")
    cur = cur.next
print("None")

print("\nList with values appearing more than twice:")
cur = first2
while cur:
    print(cur.val, end=" -> ")
    cur = cur.next
print("None")