class Node:
    def __init__(self,value):
        self.val=value
        self.next=None



def CzyWiekszy(str1,str2):
    i=0
    while i<len(str1) and i<len(str2):
        chr1=ord(str1[i])
        chr2=ord(str2[i])
        if chr1>chr2:
            return True
        if chr2>chr1:
            return False
        i+=1
    return len(str1)>len(str2)

def zad12(first,value):
    cur=first
    prev=None
    while cur is not None and CzyWiekszy(cur.val,value):
        prev=cur
        cur=cur.next
    if cur is not None and cur.val==value:
        return first, False
    if prev is not None:
        p=Node(value)
        p.next=cur
        prev.next=p
        return first,True
    p=Node(value)
    p.next=cur
    first=p
    return first ,True

