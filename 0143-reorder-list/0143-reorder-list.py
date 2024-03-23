class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow=fast=head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        curr = slow.next
        
        while(curr):
            nex = curr.next
            curr.next=prev
            prev=curr
            curr=nex

        slow.next=None

        a=head
        b=prev
        while(a and b):
            anex=a.next
            bnex=b.next

            a.next=b
            b.next=anex

            a=anex
            b=bnex
