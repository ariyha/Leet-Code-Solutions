class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        h1 = list1
        h2 = list2
        c1=1        
        while(c1<=b):
            if c1==a:
                k1=h1
            if c1==b:
                k2=h1.next.next
            c1=c1+1
            h1=h1.next
            if(h2.next):
                h2=h2.next   
        while(h2.next):
            h2=h2.next     
        k1.next = list2
        h2.next = k2
        return list1
