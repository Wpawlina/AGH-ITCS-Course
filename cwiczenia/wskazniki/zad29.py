def zad29(l1,l2):
        prev1=None
        cur1=l1
        cnt=0
        while cur1 is not None:
                test=l2
                while test is not None and test.val<cur1.val:
                        test=test.next
                if test is None or test.val!=cur1.val:
                        cnt+=1
                        if prev1 is None:
                            l1=cur1.next
                        else:
                            prev1.next=cur1.next
                else:
                      prev1=cur1
                cur1=cur1.next
        prev1=None
        cur1=l2        
        while cur1 is not None:
                test=l1
                while test is not None and test.val<cur1.val:
                        test=test.next
                if test is None or test.val!=cur1.val:
                        cnt+=1
                        if prev1 is None:
                            l2=cur1.next
                        else:
                            prev1.next=cur1.next
                else:
                      prev1=cur1
                cur1=cur1.next
        return cnt

              
                
                