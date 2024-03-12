class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next=head
        presum=0
        summap={}

        current=temp

        while(current):
            presum=presum+current.val
            summap[presum]=current
            current=current.next
        
        current=temp
        presum=0

        while(current):
            presum=presum+current.val
            if presum in summap:
                current.next = summap[presum].next
            current=current.next
        
        return temp.next