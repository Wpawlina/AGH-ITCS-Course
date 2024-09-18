class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def repair(p):
    q=-2
    cur=p.next
    prev=p
    cnt=0
    while cur is not None:
        if (prev.val*q)!=cur.val:
            new=Node((prev.val*q))
            prev.next=new
            cnt+=1 
            while new.val*q!=cur.val:
                new.next=Node(new.val*q)
                new=new.next
                cnt+=1 
               
            new.next=cur
        prev=cur
        cur=cur.next

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example linked list: 2 -> 4 -> 8 -> 16
head = Node(4)
head.next = Node(-32)
head.next.next = Node(-128)
head.next.next.next = Node(-2048)

print("Original Linked List:")
print_linked_list(head)

# Call the repair function
repair(head)

print("\nRepaired Linked List:")
print_linked_list(head)