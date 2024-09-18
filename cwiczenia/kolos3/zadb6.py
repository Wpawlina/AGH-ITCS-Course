def seperate(p):
    even=None
    odd=None
    startE=None
    startO=None
    cur=p
    flag=False
    cnt=0
    while cur!=p or not flag:
        if cur.val%2==0 and cur.val>0:
            if even is None:
                startE=cur
                even=cur
            else:
                even.next=cur
                even=even.next
        elif cur.val%2==1 and cur.val<0:
                if odd is None:
                    odd=cur
                    startO=cur
                else:
                    odd.next=cur
                    odd=odd.next
        else:
             cnt+=1
        cur=cur.next
        flag=True
    if odd is not None:
         odd.next=startO
    if even is not None:
         even.next=startE
    return startE,startO,cnt    





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example linked list: 1 -> -3 -> 5 -> 2 -> -4 -> 7
linked_list = ListNode(4)
linked_list.next = ListNode(-3)
linked_list.next.next = ListNode(-5)
linked_list.next.next.next = ListNode(2)
linked_list.next.next.next.next = ListNode(-4)
linked_list.next.next.next.next.next = ListNode(7)
linked_list.next.next.next.next.next.next = linked_list  # pointing back to the head to form a loop

# Using the separate function
start_even, start_odd, count = seperate(linked_list)

# Displaying the results
print("Even Positive List:")
for i in range(3):
    print(start_even.val, end=" -> ")
    start_even = start_even.next


print("\nOdd Negative List:")
for i in range(3):
    print(start_odd.val, end=" -> ")
    start_odd = start_odd.next


print("\nCount of elements that don't meet the conditions:", count)