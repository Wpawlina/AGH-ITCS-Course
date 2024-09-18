


import math

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def ileCyfr(n):
    return int(math.log10(n))+1


def laczne(num1,num2):
    dig1=num1%10
    p=ileCyfr(num2)
    dig2=num2//(10**(p-1))
    if dig1==dig2:
        return True
    return False
def insert(p,n):
    cur=p
    flag=False
    while cur!=p or not flag:
        if laczne(cur.val,n):
            cnt=0
            test=cur.next
            while test!=cur:
                if laczne(n,test.val) and cnt>=2:
                    new=Node(n)
                    cur.next=new
                    new.next=test
                    return cnt-1
                cnt+=1
                test=test.next
            if laczne(n,cur.val) and cnt>=2:
                new=Node(n)
                cur.next=new
                new.next=cur
                return cnt-1
        cur=cur.next
        flag=True
    return 0



head = Node(2023)
head.next = Node(31)
head.next.next = Node(17)
head.next.next.next = Node(703)
head.next.next.next.next = Node(37)
head.next.next.next.next.next = Node(707)
head.next.next.next.next.next.next = Node(72)
head.next.next.next.next.next.next.next = Node(29)
head.next.next.next.next.next.next.next.next = Node(902)

# Call the insert function
result = insert(head, 303)

print(result)


                






        

