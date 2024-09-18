
class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

def zad13(first):
    cur=first
    prev=None
    prevVal=-float('inf')
    while cur is not None:
        if prevVal>cur.val:
                prev.next=cur.next
        else:     
            prev=cur
        prevVal=cur.val
        cur=cur.next
    
            

head = Node(10)
head.next=Node(5)
head.next.next = Node(2)
head.next.next.next = Node(5)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(4)

# Wywołanie funkcji
zad13(head)

# Wyświetlenie zaktualizowanej listy
current = head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next





